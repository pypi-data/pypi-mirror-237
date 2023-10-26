# Spherical Harmonic Decomposition

This project contains a python class `SHD` that provides functionalities to perform Spherical Harmonic Decompositions on trajectories.

## Features:

- Convert cartesian coordinates to spherical and vice versa.
- Load trajectory data from different file formats.
- Distribute trajectory points along a generated grid.
- Compute the spherical harmonic expansion of the trajectory.
- Compute tension and bending coefficients.
- Plot the spectrum of the spherical harmonic expansion.

## Installation

The package can be installed using pip:
```bash
pip install sphericalHarmonicDecomposition
```

## Requirements:

This class leverages several libraries including:
- `numpy`
- `matplotlib`
- `icosphere`
- `orthopoly`
- `MDAnalysis`
- `scipy`

Make sure these libraries are installed to use this class effectively.

## Usage:

To use the class, instantiate an object of `SHD` and then call the desired methods. For instance:

```python
from sphericalHarmonicDecomposition import SHD

sph = SHD(name="SPH",
          Lmin=2,Lmax=10,
          expansionMode="abs",
          radiusMode="expansion")

sph.loadSPtraj("traj.sp")

sph.generateIcosahedralGrid(2)
sph.distributeTrajPointsAlongGrid()

sph.sphericalHarmonicExpansion()
sph.compute()
```
