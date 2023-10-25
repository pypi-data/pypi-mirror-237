import numpy as np


import numpy as np

def perturbation_method(c, A, b, max_iterations=100, tolerance=1e-6):
    m, n = A.shape
    x = np.zeros(n)
    iteration = 0

    while iteration < max_iterations:
        iteration += 1

        # Solve the unperturbed LP
        c_perturbed = c - x  # Apply perturbation
        x = np.linalg.lstsq(A, b - A @ x, rcond=None)[0]

        if np.max(np.abs(A @ x - b)) <= tolerance:
            break

    if iteration < max_iterations:
        return x
    else:
        raise Exception("Perturbation method did not converge.")

if __name__ == "__main__":
    pass
