# ORTipy Documentation

The ORTipy - Operation Research Toolkit in Python Library is a collection of functions that allow you to solve and visualize linear programming problems. Linear programming is a mathematical optimization technique used to find the best outcome in a mathematical model with linear relationships. This library provides tools for solving linear programming problems using graphical methods, the simplex method, Gomory's cut method, and the perturbation method. Below, you'll find detailed explanations and usage examples for each function in the library.

## Installation

You can easily install ORTipy using `pip`. Open your terminal or command prompt and run the following command:

```bash
pip install ORTipy
```

This will download and install the latest version of ORTipy from the Python Package Index (PyPI). Make sure you have Python and pip installed on your system.

Once installed, you can start using the ORTipy library to solve and visualize linear programming problems in Python.

This installation section provides clear instructions for users on how to install your package using `pip`. It's a common and user-friendly way to distribute Python packages.


### `graphical_lpp`

The `graphical_lpp` function allows you to solve a 2-variable linear programming problem graphically. It plots the feasible region and the optimal solution on a 2D graph. This method is suitable for problems with only two decision variables and a few constraints.

**Usage Example:**

```python
import numpy as np
import matplotlib.pyplot as plt
from ORTipy import graphical_lpp

# Objective function: Z = c1*x + c2*y
objective_coefficients = [3, 2]

# Constraints: A*x <= b
constraint_coefficients = [[2, 1], [1, 2]]
constraint_bounds = [10, 8]

graphical_lpp(objective_coefficients, constraint_coefficients, constraint_bounds)

```

### `simplex_lpp`

The `simplex_lpp` function is used to solve linear programming problems using the simplex method. It takes the coefficients of the objective function, the constraint matrix, and the right-hand side vector as input and returns the optimal solution and value.

**Usage Example:**

```python
from ORTipy import simplex_lpp

# Objective function coefficients: Z = 3x + 2y
c = np.array([3, 2])

# Constraint coefficients
A = np.array([[2, 1], [1, 2]])
b = np.array([10, 8])

optimal_solution, optimal_value = simplex_lpp(c, A, b)
print("Optimal Solution:", optimal_solution)
print("Optimal Value:", optimal_value)

```

### `gomory_ilpp`

The `gomory_ilpp` function is used to solve integer linear programming problems using Gomory's cut method. It takes the objective function coefficients, constraint coefficients, and constraint bounds as input. It iteratively adds Gomory cuts until an integer solution is found.

**Usage Example:**

```python
from ORTipy import gomory_ilpp

# Objective function coefficients: Z = 3x + 2y
objective_coefficients = [3, 2]

# Constraint coefficients
constraint_coefficients = [[2, 1], [1, 2]]
constraint_bounds = [10, 8]

gomory_ilpp(objective_coefficients, constraint_coefficients, constraint_bounds)

```

### `perturbation_method`

The `perturbation_method` function is used to solve linear programming problems using the perturbation method. It takes the coefficients of the objective function, the constraint matrix, and the right-hand side vector as input. It iteratively perturbs the objective function and solves the perturbed linear system until convergence.

**Usage Example:**

```python
from ORTipy import perturbation_method

# Objective function coefficients: Z = 3x + 2y
c = np.array([3, 2])

# Constraint coefficients
A = np.array([[2, 1], [1, 2]]
b = np.array([10, 8])

optimal_solution = perturbation_method(c, A, b)
print("Optimal Solution:", optimal_solution)

```

These functions provide various methods for solving linear programming problems, making it easier to choose the most suitable approach for your specific problem. Whether you want to visualize the solution, apply the simplex method, use Gomory's cut method for integer linear programming, or solve using the perturbation method, this library has you covered.

ORTipy is developed by the twofoldtwins.

**©twofoldtwins**
