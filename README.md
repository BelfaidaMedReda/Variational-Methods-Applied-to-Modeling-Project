# Eigenvalue Computation and Vibrational Analysis using Finite Element Methods

This project explores eigenvalue problems related to the Laplacian operator, vibration modes of drumheads, and energy band computation in graphene using Finite Element Methods (FEM). The study includes analytical solutions, numerical implementations, and comparative analyses.

## Table of Contents
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Mathematical Background](#mathematical-background)
- [Implementation](#implementation)
- [Results](#results)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Files](#files)
- [References](#references)

## Project Overview
The project is divided into three main parts:
1. **Eigenvalue Computation for the Laplacian Operator**: Analytical and numerical solutions for the eigenvalue problem on a unit square with Dirichlet boundary conditions.
2. **Vibrations of a Drumhead**: Modeling and analysis of drumhead vibrations, including isospectral domains and the effect of thickness variations.
3. **Graphene Energy Band Computation**: Variational formulation and numerical solution for the Bloch Hamiltonian in graphene.

## Key Features
- Analytical derivation of eigenvalues and eigenfunctions for the Laplacian operator.
- Numerical implementation using FreeFem++ for eigenvalue problems and wave equations.
- Comparison of isospectral domains and analysis of geometric deformations.
- Study of thickness variations on drumhead vibrations.
- Spectral decomposition and finite element methods for solving the wave equation.
- Graphene energy band computation with periodic boundary conditions.

## Mathematical Background
### 1. Laplacian Eigenvalue Problem
The eigenvalue problem is defined as:

$$-\Delta u = \lambda u \quad \text{in } \Omega, \quad u = 0 \quad \text{on } \partial\Omega.$$

The analytical solutions are derived using separation of variables, yielding eigenvalues $\lambda_{m,n} = \pi^2(m^2 + n^2)$ and eigenfunctions $u_{m,n}(x,y) = \sin(m\pi x)\sin(n\pi y)$.

### 2. Vibrations of a Drumhead
The wave equation for drumhead vibrations is:

$$\frac{\partial^2 u}{\partial t^2} = c^2 \Delta u.$$

The problem is reduced to an eigenvalue problem for the Laplacian, and the effects of domain geometry and thickness variations are analyzed.

### 3. Graphene Energy Band Computation
The Bloch Hamiltonian for graphene is:

$$ H_k u_k = \left(-\frac{1}{2}\Delta - ik \cdot \nabla + \frac{1}{2}|k|^2\right) u_k = E_k u_k$$

The variational formulation is implemented numerically using FreeFem++.

## Implementation
The project uses FreeFem++ for numerical simulations. Key scripts include:
- `laplacien_eigen.edp`: Computes eigenvalues for the Laplacian.
- `eigen_error.edp`: Analyzes errors in eigenvalue approximations.
- `modified_eigen.edp`: Solves modified eigenvalue problems with mixed boundary conditions.
- `thicknessEffect1.edp` and `thicknessEffect2.edp`: Study thickness variations in drumheads.
- `NumericalResolution1.edp` and `NumericalResolution2.edp`: Compare time-marching and spectral methods for the wave equation.
- `graphene_solver.edp`: Computes energy bands for graphene.

## Results
- **Laplacian Eigenvalues**: Numerical results closely match theoretical predictions for lower modes, with errors increasing for higher frequencies.
- **Isospectral Domains**: Demonstrated numerically that certain non-congruent domains share identical spectra.
- **Thickness Effects**: Variable thickness significantly alters the eigenvalue distribution, particularly for higher modes.
- **Wave Equation Solutions**: Both finite element and spectral methods provide accurate solutions, with FEM being more versatile for complex geometries.

## Dependencies
- [FreeFem++](https://freefem.org/)
- Python (for plotting, optional)

## Usage
1. Install FreeFem++.
2. Run the scripts in FreeFem++:
   ```bash
   FreeFem++ laplacien_eigen.edp# Eigenvalue Computation and Vibrational Analysis using Finite Element Methods

This project explores eigenvalue problems related to the Laplacian operator, vibration modes of drumheads, and energy band computation in graphene using Finite Element Methods (FEM). The study includes analytical solutions, numerical implementations, and comparative analyses.

## Table of Contents
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Mathematical Background](#mathematical-background)
- [Implementation](#implementation)
- [Results](#results)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Files](#files)
- [References](#references)

## Project Overview
The project is divided into three main parts:
1. **Eigenvalue Computation for the Laplacian Operator**: Analytical and numerical solutions for the eigenvalue problem on a unit square with Dirichlet boundary conditions.
2. **Vibrations of a Drumhead**: Modeling and analysis of drumhead vibrations, including isospectral domains and the effect of thickness variations.
3. **Graphene Energy Band Computation**: Variational formulation and numerical solution for the Bloch Hamiltonian in graphene.

## Key Features
- Analytical derivation of eigenvalues and eigenfunctions for the Laplacian operator.
- Numerical implementation using FreeFem++ for eigenvalue problems and wave equations.
- Comparison of isospectral domains and analysis of geometric deformations.
- Study of thickness variations on drumhead vibrations.
- Spectral decomposition and finite element methods for solving the wave equation.
- Graphene energy band computation with periodic boundary conditions.

## Mathematical Background
### 1. Laplacian Eigenvalue Problem
The eigenvalue problem is defined as:
\[
-\Delta u = \lambda u \quad \text{in } \Omega, \quad u = 0 \quad \text{on } \partial\Omega.
\]
The analytical solutions are derived using separation of variables, yielding eigenvalues \(\lambda_{m,n} = \pi^2(m^2 + n^2)\) and eigenfunctions \(u_{m,n}(x,y) = \sin(m\pi x)\sin(n\pi y)\).

### 2. Vibrations of a Drumhead
The wave equation for drumhead vibrations is:
\[
\frac{\partial^2 u}{\partial t^2} = c^2 \Delta u.
\]
The problem is reduced to an eigenvalue problem for the Laplacian, and the effects of domain geometry and thickness variations are analyzed.

### 3. Graphene Energy Band Computation
The Bloch Hamiltonian for graphene is:
\[
H_k u_k = \left(-\frac{1}{2}\Delta - ik \cdot \nabla + \frac{1}{2}|k|^2\right) u_k = E_k u_k.
\]
The variational formulation is implemented numerically using FreeFem++.

## Implementation
The project uses FreeFem++ for numerical simulations. Key scripts include:
- `laplacien_eigen.edp`: Computes eigenvalues for the Laplacian.
- `eigen_error.edp`: Analyzes errors in eigenvalue approximations.
- `modified_eigen.edp`: Solves modified eigenvalue problems with mixed boundary conditions.
- `thicknessEffect1.edp` and `thicknessEffect2.edp`: Study thickness variations in drumheads.
- `NumericalResolution1.edp` and `NumericalResolution2.edp`: Compare time-marching and spectral methods for the wave equation.
- `graphene_solver.edp`: Computes energy bands for graphene.

## Results
- **Laplacian Eigenvalues**: Numerical results closely match theoretical predictions for lower modes, with errors increasing for higher frequencies.
- **Isospectral Domains**: Demonstrated numerically that certain non-congruent domains share identical spectra.
- **Thickness Effects**: Variable thickness significantly alters the eigenvalue distribution, particularly for higher modes.
- **Wave Equation Solutions**: Both finite element and spectral methods provide accurate solutions, with FEM being more versatile for complex geometries.

## Dependencies
- [FreeFem++](https://freefem.org/)
- Python (for plotting, optional)

## Usage
1. Install FreeFem++.
2. Run the scripts in FreeFem++:
   ```bash
   FreeFem++ laplacien_eigen.edp