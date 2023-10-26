import sys,os

from itertools import combinations
from tqdm import tqdm

import logging

import matplotlib.pyplot as plt
import numpy as np

from icosphere import icosphere

import orthopoly

import MDAnalysis as mda
from MDAnalysis.analysis import align

from scipy import spatial
from scipy.optimize import least_squares
from scipy.optimize import lsq_linear
from scipy.optimize import curve_fit
from scipy.stats import linregress

#Import curve_fit from scipy
from scipy.optimize import curve_fit

#References:
#Brooks III: https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.106.188101
#Atzberger:  https://arxiv.org/pdf/1901.05085.pdf

class SHD:

    def __cart2sph(self,cartPositions):
        """
        Convert cartesian coordinates to spherical coordinates
        """
        x,y,z       = cartPositions.T
        r,theta,phi = orthopoly.spherical_harmonic.cart2sph(-x,-y,z) #Bug in library
        return np.asarray([r,theta,phi]).T

    def __sph2cart(self,sphPositions):
        """
        Convert spherical coordinates to cartesian coordinates
        """
        r,theta,phi = sphPositions.T
        x,y,z       = orthopoly.spherical_harmonic.sph2cart(r,theta,phi)
        return np.asarray([x,y,z]).T

    def __degreeOfTruncationToLM(self,n):
        A = orthopoly.spherical_harmonic.Tnm(self.__Lmax)
        l,m = A[0][n],A[1][n]
        return l,m

    def __init__(self,name="SHD",Lmin=2,Lmax=10,debug=False,
                 radiusMode    = "geometric",
                 expansionMode = "abs"):

        self.__availableRadiusModes    = ["expansion","geometric"]
        self.__availableExpansionModes = ["fluct","abs"]

        self.__DEBUG = debug

        self.__Lmin = Lmin
        self.__Lmax = Lmax
        self.__name = name

        self.logger = logging.getLogger("sphAnalysis")
        self.logger.setLevel(logging.DEBUG)
        #Formatter, ascii time to day, month, year, hour, minute, second
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',"%d-%b-%Y %H:%M:%S")

        #Set logger to console, with level INFO
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)

        #Create other logger. Log to file, with level DEBUG
        fh = logging.FileHandler(f'{self.__name}.log')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)

        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

        ######################################################

        if radiusMode not in self.__availableRadiusModes:
            self.logger.error("Radius mode {} not available. Available modes are: {}".format(radiusMode,self.__availableRadiusModes))
            raise ValueError
        else:
            self.__radiusMode = radiusMode

        if expansionMode not in self.__availableExpansionModes:
            self.logger.error("Traj mode {} not available. Available modes are: {}".format(expansionMode,self.__availableExpansionModes))
            raise ValueError
        else:
            self.__expansionMode = expansionMode

        if self.__radiusMode == "expansion" and self.__expansionMode == "fluct":
            #Not compatible
            self.logger.error("Radius mode {} and traj mode {} not compatible".format(self.__radiusMode,self.__expansionMode))
            raise ValueError

    def loadSPtraj(self,spTrajFile):
        """
        Load traj from sp format.

        # Frame info
        x y z r type
        x y z r type
        ...
        # Frame info
        x y z r type
        x y z r type
        ...
        """

        self.logger.info("Loading sp trajectory from file {} ...".format(spTrajFile))

        nFrames = 0
        with open(spTrajFile,"r") as f:
            for i,line in enumerate(f):
                if "#" in line:
                    nFrames+=1

        self.nFrames = nFrames
        self.traj    = np.loadtxt(spTrajFile)[:,[0,1,2]].reshape(nFrames,-1,3)

        #Remove the first frame, which is the initial configuration
        self.traj = self.traj[1:]
        self.nFrames-=1

        for i,frame in enumerate(self.traj):
            self.traj[i]=frame-frame.mean(axis=0)

        self.logger.info("Loaded sp trajectory with {} frames and {} particles".format(nFrames,self.traj.shape[1]))

        ref   =mda.Universe(self.traj,inmemory=True)
        mobile=mda.Universe(self.traj,inmemory=True)

        ref.trajectory[0].positions=ref.trajectory[0].positions-ref.select_atoms("all").centroid()

        aligner = align.AlignTraj(mobile, ref, select='all',weights=None,inmemory=True,match_atoms=False).run()

        self.traj    = mobile.trajectory.coordinate_array
        self.trajSph = self.__cart2sph(self.traj.reshape(-1,3)).reshape(self.nFrames,-1,3)

    def loadPSF_DCDtraj(self,psfTrajFile,dcdTrajFile):
        """
        Load traj from psf and dcd format.
        """

        self.logger.info("Loading psf trajectory from files {} and {} ...".format(psfTrajFile,dcdTrajFile))

        ref   =mda.Universe(psfTrajFile,dcdTrajFile,inmemory=True)
        mobile=mda.Universe(psfTrajFile,dcdTrajFile,inmemory=True)

        #Center all frames for mobile trajectory
        for i,frame in enumerate(mobile.trajectory):
            mobile.trajectory[i].positions=mobile.trajectory[i].positions-mobile.select_atoms("all").centroid()

        ref.trajectory[0].positions=ref.trajectory[0].positions-ref.select_atoms("all").centroid()

        aligner = align.AlignTraj(mobile, ref, select='all',weights=None,inmemory=True,match_atoms=False).run()

        mobile=mda.Universe(psfTrajFile,"rmsfit_"+dcdTrajFile,inmemory=True)

        self.nFrames = mobile.trajectory.n_frames

        self.traj    = np.empty((self.nFrames,mobile.atoms.n_atoms,3))
        for fn,frame in enumerate(mobile.trajectory):
            self.traj[fn]=frame.positions

        self.trajSph = self.__cart2sph(self.traj.reshape(-1,3)).reshape(self.nFrames,-1,3)

        self.logger.info("Loaded sp trajectory with {} frames and {} particles".format(self.nFrames,self.traj.shape[1]))

        os.system("rm rmsfit_{}".format(dcdTrajFile))

        if self.__DEBUG:

            self.logger.debug("Saving trajectory to file ...")

            with open("input.sp","w") as f:
                for frame in self.traj:
                    f.write("#\n")
                    for p in frame:
                        f.write("{} {} {} 1.0 0\n".format(p[0],p[1],p[2]))


    def __setGrid(self):
        self.gridSize = self.thetaGrid.shape[0]
        self.grid = np.asarray([self.thetaGrid,self.phiGrid]).T

        r=[1.0]*self.gridSize
        self.gridVectors = self.__sph2cart(np.asarray([r,self.thetaGrid,self.phiGrid]).T)

        self.gridKDtree = spatial.KDTree(self.gridVectors)

    def generateIcosahedralGrid(self,n):

        self.logger.info("Generating icosahedral grid with {} subdivisions ...".format(n))

        self.thetaGrid,self.phiGrid=orthopoly.spherical_harmonic.grid_icosahedral(n)
        self.__setGrid()

        #fig = plt.figure()
        #ax = fig.add_subplot(projection='3d')

        #r=[1.0]*self.thetaGrid.shape[0]
        #x,y,z = self.__sph2cart(np.asarray([r,self.thetaGrid,self.phiGrid]).T).T
        #ax.scatter(x,y,z)
        #plt.show()

    def generateRegularGrid(self,n):

        self.logger.info("Generating regular grid with {} subdivisions ...".format(n))

        self.thetaGrid,self.phiGrid=orthopoly.spherical_harmonic.grid_regular(n)
        self.__setGrid()

        #fig = plt.figure()
        #ax = fig.add_subplot(projection='3d')

        #r=[1.0]*self.thetaGrid.shape[0]
        #x,y,z = self.__sph2cart(np.asarray([r,self.thetaGrid,self.phiGrid]).T).T
        #ax.scatter(x,y,z)
        #plt.show()

    def generateFibonacciGrid(self,n):

        self.logger.info("Generating fibonacci grid with {} points ...".format(n))

        self.thetaGrid,self.phiGrid=orthopoly.spherical_harmonic.grid_fibonacci(n)
        self.__setGrid()

        #fig = plt.figure()
        #ax = fig.add_subplot(projection='3d')

        #r=[1.0]*self.thetaGrid.shape[0]
        #x,y,z = self.__sph2cart(np.asarray([r,self.thetaGrid,self.phiGrid]).T).T
        #ax.scatter(x,y,z)
        #plt.show()

    def distributeTrajPointsAlongGrid(self):
        """
        Distribute the trajectory points along the grid.
        """

        #Check if the trajectory has been loaded
        if self.traj is None:
            self.logger.error("Trying to distribute trajectory points along grid, but no trajectory has been loaded.")
            raise RuntimeError("No trajectory loaded.")

        #Check if the grid has been generated
        if self.grid is None:
            self.logger.error("Trying to distribute trajectory points along grid, but no grid has been generated.")
            raise RuntimeError("No grid generated.")

        self.logger.info("Distributing trajectory points along grid ...")

        r,theta,phi = self.__cart2sph(self.traj.reshape(-1,3)).T

        #Projects points over sphere
        r=np.asarray([1.0]*r.shape[0])
        trajOverSphere = self.__sph2cart(np.asarray([r,theta,phi]).T)

        self.trajBeadsGridPosition = self.gridKDtree.query(trajOverSphere)[1].reshape(self.nFrames,-1)

        self.trajGridSph = np.empty((self.nFrames,self.gridSize,3))
        for f,[framePos,frameGrid] in enumerate(tqdm(zip(self.trajSph,self.trajBeadsGridPosition),total=self.nFrames)):
            for i in range(self.gridSize):
                mask = (frameGrid == i)

                if not np.any(mask):
                    self.logger.error("Grid point with no data. Try to decrease the number of grid points.")
                    raise Exception("Grid point with no data")

                r,theta,phi = framePos[mask].T

                self.trajGridSph[f,i] = np.asarray([np.mean(r),self.thetaGrid[i],self.phiGrid[i]])

        if self.__DEBUG:

            self.logger.debug("Distributed trajectory points along grid. Writing to file ...")

            with open("gridPos.sp","w") as f:
                for framePos,frameGrid in zip(self.traj,self.trajBeadsGridPosition):
                    f.write("#\n")
                    for p,g in zip(framePos,frameGrid):
                        f.write("{} {} {} 1.0 {}\n".format(p[0],p[1],p[2],g))

            with open("gridTraj.sp","w") as f:
                for frame in self.trajGridSph:
                    f.write("#\n")
                    for p in frame:
                        x,y,z = self.__sph2cart(np.asarray([p[0],p[1],p[2]]).T).T
                        f.write("{} {} {} 1.0 0\n".format(x,y,z))

    def sphericalHarmonicExpansion(self):
        """
        Compute the spherical harmonic expansion of the trajectory.
        """

        #Check if the trajectory has been added and distributed along the grid
        if self.traj is None:
            self.logger.error("Trying to compute spherical harmonic expansion, but no trajectory has been loaded.")
            raise RuntimeError("No trajectory loaded.")

        if self.trajGridSph is None:
            self.logger.error("Trying to compute spherical harmonic expansion, but trajectory has not been distributed along grid.")
            raise RuntimeError("No trajectory distributed along grid.")

        self.logger.info("Performing spherical harmonic expansion ...")

        R = self.trajGridSph.mean(axis=0)[:,0]

        self.aCoeffComputed      = []
        for frame in (pbar := tqdm(self.trajGridSph)):
            f,theta,phi = frame.T
            infoY = orthopoly.spherical_harmonic.sph_har_T_matrix(theta,phi,self.__Lmax)
            Y = infoY[0]

            if self.__expansionMode == "fluct":
                fFluct = f-R
                aFluct=lsq_linear(Y,fFluct,max_iter=1000,tol=0.000001,lsq_solver='lsmr')
                self.aCoeffComputed.append(aFluct.x)
            elif self.__expansionMode == "abs":
                a=lsq_linear(Y,f,max_iter=1000,tol=0.000001,lsq_solver='lsmr')
                self.aCoeffComputed.append(a.x)
            else:
                self.logger.error("Expansion mode not recognized.")
                raise RuntimeError

        self.aCoeffComputed = np.asarray(self.aCoeffComputed)

    def compute(self,Brooks=False):
        """
        Plot the spectrum of the spherical harmonic expansion.
        """

        #Check if the spherical harmonic expansion has been computed
        if self.aCoeffComputed is None:
            self.logger.error("Trying to plot spectrum, but spherical harmonic expansion has not been computed.")
            raise RuntimeError("No spherical harmonic expansion computed.")

        self.logger.info("Plotting spectrum ...")

        if  self.__radiusMode == "expansion":
            R = np.mean(self.aCoeffComputed[:,0])/np.sqrt(4.0*np.pi)
        elif self.__radiusMode == "geometric":
            R = np.mean(self.trajGridSph.mean(axis=0)[:,0])
        else:
            self.logger.error("Unknown radius mode: {}".format(self.__radiusMode))
            raise RuntimeError

        self.logger.info("R = {}".format(R))

        N = orthopoly.spherical_harmonic.T2nharm(self.__Lmax)
        lm2n = {}
        for n in range(N):
            l,m = self.__degreeOfTruncationToLM(n)
            lm2n[(l,m)]=n

        aCoeffMean         = np.mean(self.aCoeffComputed,axis=0)
        aCoeffMeanSquared  = np.mean(self.aCoeffComputed,axis=0)**2
        aCoeffSquaredMean  = np.mean(self.aCoeffComputed**2,axis=0)

        L   = []
        a2l = []
        for l in range(self.__Lmax+1):
            L.append(l)
            a2 = 0
            for m in range(-l,l+1):
                a2       += aCoeffSquaredMean[lm2n[(l,m)]]/(2*l+1)
                #a2Fluct += aCoeffFluctSquaredMean[lm2n[(l,m)]]/(2*l+1)
                #Dividing by 2l+1 is done in the paper of Atzberger but not in the paper of
                #Brooks III. I think it is correct to do it.
                #We are not computing the harmonic spectrum. We are computing the harmonic mean.
                #We sum over all m and then we comute the mean, so we have to divide by 2l+1.
                #If we were computing the harmonic spectrum, we won't have to divide by 2l+1.
                #(But in some normalization yes, but not here). Everything is a mess.
                #Summarizing:
                #a2 is the harmonic mean of the squared coefficients. Dividing by 2l+1 is correct.
                #a2 is the power spectrum. Dividing by 2l+1 is not correct for this normalization. But could be correct for another normalization.

            a2l.append(a2)

        LF    = []
        invLF = []
        for l in L[self.__Lmin::]:
            fl = l*(l+2.0)*(l*l-1)
            LF.append(fl)
            invLF.append(1.0/fl)
        LF    = np.asarray(LF)
        invLF = np.asarray(invLF)

        if not Brooks:
            plt.plot(invLF,a2l[self.__Lmin::],label="a2l",marker="o")
            #log(a2l) = b + m*log(invLF), we fit to b and m. Linear regression
            a,m           = curve_fit(lambda x,a,m: a+m*x,np.log(invLF),np.log(a2l[self.__Lmin::]))[0]

            self.logger.info("Spectrum fit: a = {}, m = {}".format(a,m))

            #a = log(2*R**2/kc)
            kc = 2.0*R**2/np.exp(a)

            self.logger.info("b  = 0.0 KbT")
            self.logger.info("kc = {} KbT (kc --> kc/2, corrected?, kc = {} KbT)".format(kc,kc/2.0))
            plt.plot(invLF,np.exp(a+m*np.log(invLF)),label="fit",marker="",linestyle="--")
            plt.xscale('log')
            plt.yscale('log')
            plt.xlabel(r"$[l(l+2)(l^2-1)]^{-1}$")
            plt.ylabel(r"$Var[a_l]$")

        else:
            plt.plot(LF,a2l[self.__Lmin::],label="a2l",marker="o")
            #<al**2> = 1/(8b+kc*l*(l+2)*(l**2-1)/R**2), where b and kc are in KbT units
            LFdivR   = LF/R**2
            b,kc = curve_fit(lambda x,b,kc: 1.0/(8.0*b+kc*x),LFdivR,a2l[self.__Lmin::])[0]

            self.logger.info("Spectrum fit: b = {}, kc = {}".format(b,kc))

            self.logger.info("b = {}  KbT".format(b))
            self.logger.info("kc = {} KbT".format(kc))

            plt.plot(LF,1.0/(8.0*b+kc*LFdivR),label="fit",marker="",linestyle="--")
            plt.xscale('log')
            plt.yscale('log')
            plt.xlabel(r"$l(l+2)(l^2-1)/R^2$")
            plt.ylabel(r"$Var[a_l]$")

        plt.title(self.__name)

        plt.savefig("spectrum_{}.png".format(self.__name))

        self.logger.info("Spectrum:")
        for l,a2 in zip(L,a2l):
            self.logger.info("{} {}".format(l,a2))

    def test(self,nCopies,icosphereOrder,radius,radialVariationMax,radialVariationVar):

        self.logger.info("Testing the spherical harmonics")

        #Expansion mode must be abs for testing
        if self.__expansionMode != "abs":
            self.logger.error("Expansion mode must be abs for testing.")
            raise RuntimeError

        self.logger.info("Generating random harmonics ...")
        N = orthopoly.spherical_harmonic.T2nharm(self.__Lmax)
        sph = []
        for n in range(N):
            l,m = self.__degreeOfTruncationToLM(n)
            sph.append(np.random.uniform(-radialVariationMax,radialVariationMax))

        self.logger.info("Generating random trajectory ...")
        #generateTraj
        points,_ = icosphere(icosphereOrder)
        points   = points*radius

        self.traj    = np.empty((nCopies,points.shape[0],3))
        self.nFrames = nCopies

        for fn in tqdm(range(self.nFrames)):
            r,theta,phi = self.__cart2sph(points).T
            for n,c in enumerate(sph):
                l,m = self.__degreeOfTruncationToLM(n)

                c_var = c + np.random.normal(0.0,radialVariationVar)

                ylm = orthopoly.spherical_harmonic.sph_har(theta,phi,l,m)

                r = r + c_var*r*ylm

            self.traj[fn]=self.__sph2cart(np.asarray([r,theta,phi]).T)

        self.trajSph = self.__cart2sph(self.traj.reshape(-1,3)).reshape(self.nFrames,-1,3)

        with open("genTraj.sp","w") as f:
            for frame in self.traj:
                f.write("#\n")
                for p in frame:
                    f.write("{} {} {} 1 0\n".format(p[0],p[1],p[2]))

        #self.generateFibonacciGrid(1001)
        sphA.generateIcosahedralGrid(3)
        self.distributeTrajPointsAlongGrid()

        self.sphericalHarmonicExpansion()

        N = orthopoly.spherical_harmonic.T2nharm(self.__Lmax)
        lm2n = {}
        for n in range(N):
            l,m = self.__degreeOfTruncationToLM(n)
            lm2n[(l,m)]=n

        aCoeffMean        = np.mean(self.aCoeffComputed/radius,axis=0)
        aCoeffMeanSquared = np.mean(self.aCoeffComputed/radius,axis=0)**2

        L   = []
        a2l = []
        a2lTheo  = []
        for l in range(self.__Lmax+1):
            L.append(l)
            a2 = 0
            a2Theo = 0
            for m in range(-l,l+1):
                a2      += aCoeffMeanSquared[lm2n[(l,m)]]
                a2Theo  += sph[lm2n[(l,m)]]**2

            a2l.append(a2)
            a2lTheo.append(a2Theo)

        plt.plot(L[self.__Lmin::],    a2l[self.__Lmin::],label="a2l",marker="o")
        plt.plot(L[self.__Lmin::],a2lTheo[self.__Lmin::],label="a2lTheo",marker="o")

        plt.title(self.__name)
        plt.xscale('log')
        plt.yscale('log')
        plt.xlabel(r"$l$")
        plt.ylabel(r"$Var[a_l]$")

        plt.show()
