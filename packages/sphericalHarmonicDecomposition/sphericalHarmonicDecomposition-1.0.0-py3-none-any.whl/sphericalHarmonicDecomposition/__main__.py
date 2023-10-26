from . import SHD

import argparse

if __name__ == "__main__":

    #Create argument parser
    parser = argparse.ArgumentParser(description='Analyze a spherical harmonic decomposition of a molecular dynamics trajectory.')

    #Add arguments

    parser.add_argument('-n', '--name', type=str, help='Analysis name', required=False, default="SPH")
    parser.add_argument('-lm', '--Lmin', type=int, help='Minimum L value', required=False, default=2)
    parser.add_argument('-lM', '--Lmax', type=int, help='Maximum L value', required=False, default=10)
    parser.add_argument('-em', '--expansionMode', type=str, help='Expansion mode', required=False, default="abs")
    parser.add_argument('-rm', '--radiusMode', type=str, help='Radius mode', required=False, default="expansion")

    #Input trajectory is a list of files
    parser.add_argument('-i', '--inputTrajectory', type=str, nargs='+', help='Input trajectory', required=True)
    parser.add_argument('-f', '--inputFormat', type=str, help='Input trajectory format', required=False, default="sp")

    parser.add_argument('-res', '--gridResolution', type=int,help='Grid resolution', required=False, default=2)


    ################################################################################################

    name = parser.parse_args().name

    Lmin = parser.parse_args().Lmin
    Lmax = parser.parse_args().Lmax

    expansionMode = parser.parse_args().expansionMode
    radiusMode = parser.parse_args().radiusMode

    ################################################################################################

    inputTrajectory = parser.parse_args().inputTrajectory
    inputFormat = parser.parse_args().inputFormat

    if inputFormat == "sp":
        #Check trajectory is just one file
        if len(inputTrajectory) != 1:
            raise Exception("Input trajectory must be a single file for sp format.")
    elif inputFormat == "psf" or inputFormat == "dcd":
        #Check trajectory is two files
        if len(inputTrajectory) != 2:
            raise Exception("Input trajectory must be two files for psf/dcd format.")
        print("Warning: For psf/dcd format, the psf file must be the first file in the list.")
    else:
        raise Exception("Input trajectory format not recognized, must be sp, psf, or dcd.")

    ################################################################################################

    gridResolution = parser.parse_args().gridResolution

    ################################################################################################

    #Create SPH object

    sph = SHD(name=name,
              Lmin=Lmin,Lmax=Lmax,
              expansionMode=expansionMode,
              radiusMode=radiusMode)

    #Load trajectory
    if inputFormat == "sp":
        sph.loadSPtraj(inputTrajectory[0])
    elif inputFormat == "psf" or inputFormat == "dcd":
        sph.loadPSF_DCDtraj(inputTrajectory[0],inputTrajectory[1])
    else:
        raise Exception("Input trajectory format not recognized, must be sp, psf, or dcd.")

    #Compute spherical harmonic decomposition
    sph.generateIcosahedralGrid(gridResolution)
    sph.distributeTrajPointsAlongGrid()

    sph.sphericalHarmonicExpansion()

    sph.compute(Brooks=True)







