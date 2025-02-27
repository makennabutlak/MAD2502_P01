import numpy as np

def left_endpoint(x_vals: np.array, func: np.ufunc)-> float:
    """
    Approximates the integral using the left endpoint Riemann sum.

    The function calculates the sum of the values at the left endpoints 
    of each subinterval (using slicing), multiplied by the width (dx of difference in x) of each subinterval.

    Parameters:
    x_vals : np.array
        1 dimensional array of x values that define the intervals for integration.
    func : np.ufunc
        numpy function used to integrate an array
    Returns:
    float
        The left endpoint approximation of the integral.
    """
    #takes the differences of all of the x values (representing the width, dx) in the array 
    dx= np.diff(x_vals)
    #returns the sum of the difference in x values (dx) by x plugged into the equation (f(x)) stopping before the last indexed value since it is a left endpoint integral 
    return np.sum(func(x_vals[:-1])*dx)

def trapezoid(x_vals: np.ndarray, func: np.ufunc) -> float:
    """
    Approximates a trapezoidal integral

    Parameters: x_vals : np.ndarray - >  1 dimensional array of x-values that defines the intervals for integration.
    func : np.ufunc - > numpy  function that integratesan array
    Returns:
    float
        The trapezoidal approximation of the integral.
    """
    #takes the difference of all of the x values in the array (representing dx)
    dx = np.diff(x_vals)
    #returns the trapezoidal integral by finding the sum of left handed x values plus the right handed x values multiplied by the difference in x values and then divided by 2 since that is the formula for a trapezoid 
    return np.sum((func(x_vals[:-1]) + func(x_vals[1:])) * dx / 2)


def simpson(x_vals: np.ndarray, func: np.ufunc) -> float:
    """
    Approximates the integral of a function using Simpson's Rule.

    :param x_vals: A numpy array of x values defining the integration interval.
    :param func: A NumPy universal function (ufunc) representing the function to integrate.
    :return: The approximate integral value using Simpson's Rule.
    """
    # Determine the number of intervals (must be even for Simpson's Rule)
    n = len(x_vals) - 1
    # If n is odd, remove the last x value to make n even
    if n % 2 == 1:
        x_vals = x_vals[:-1]# Remove the last point
        n -= 1  # Update the number of intervals
      
       # Compute the step size (dx) based on the first and last x values 
    dx = (x_vals[-1]-x_vals[0])/n
     # Apply Simpson's Rule formula:
    # Integral ≈ (dx/3) * [ f(x0) + 4*f(x1) + 2*f(x2) + 4*f(x3) + ... + f(xn) ]
    return (dx/3)* (
            func(x_vals[0]) # First term: f(x0)
        + 4 * np.sum(func(x_vals[1:-1:2]))  # Sum of odd-indexed terms multiplied by 4
        + 2 * np.sum(func(x_vals[2:-2:2]))  # Sum of even-indexed terms (except first & last) multiplied by 2
        + func(x_vals[-1])  # Last term: f(xn)
    )
