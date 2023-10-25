import numpy as np

def simplex_lpp(c, A, b):
    m, n = A.shape
    tableau = np.zeros((m + 1, n + m + 1))

    tableau[:-1, :n] = A
    tableau[:-1, n:n + m] = np.eye(m)
    tableau[:-1, -1] = b
    tableau[-1, :n] = -c
    tableau[-1, n:n + m] = 0

    while np.any(tableau[-1, :-1] < 0):
        pivot_col = np.argmin(tableau[-1, :-1])
        if np.all(tableau[:-1, pivot_col] <= 0):
            raise Exception("The problem is unbounded.")

        pivot_row = np.argmin(tableau[:-1, -1] / tableau[:-1, pivot_col])

        pivot_element = tableau[pivot_row, pivot_col]
        tableau[pivot_row, :] /= pivot_element
        for i in range(m + 1):
            if i != pivot_row:
                tableau[i, :] -= tableau[i, pivot_col] * tableau[pivot_row, :]

    optimal_solution = tableau[:-1, -1]
    optimal_value = -tableau[-1, -1]

    return optimal_solution, optimal_value


optimal_solution, optimal_value = simplex_lpp(c, A, b)
print("Optimal Solution:", optimal_solution)
print("Optimal Value:", optimal_value)

    
if __name__ == "__main__":
    pass
