import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

def graphical_lpp(objective_coefficients, constraint_coefficients, constraint_bounds):
    # Objective function: Z = c1*x + c2*y
    c1, c2 = objective_coefficients

    # Constraints: A*x <= b
    A = np.array(constraint_coefficients)
    b = np.array(constraint_bounds)

    # Calculate intersection points for the constraint lines
    x = np.linspace(0, 10, 400)
    y1 = (b[0] - A[0, 0] * x) / A[0, 1]
    y2 = (b[1] - A[1, 0] * x) / A[1, 1]

    # Plot the constraint lines and shade the feasible region
    plt.plot(x, y1, label="2x + y <= 10")
    plt.plot(x, y2, label="x + 2y <= 8")
    plt.fill_between(x, np.minimum(y1, y2), where=(x >= 0), interpolate=True, alpha=0.2, color='gray', label='Feasible Region')

    # Calculate Z for each point in the feasible region
    Z = c1 * x + c2 * np.minimum(y1, y2)

    # Find the optimal solution
    optimal_point = np.argmax(Z)
    optimal_x = x[optimal_point]
    optimal_y = np.minimum(y1, y2)[optimal_point]
    optimal_Z = Z[optimal_point]

    # Plot the optimal solution
    plt.plot(optimal_x, optimal_y, 'ro', label=f'Optimal Solution (x={optimal_x}, y={optimal_y}, Z={optimal_Z})')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.title('Linear Programming Problem')
    plt.show()


if __name__ == "__main__":
    pass
