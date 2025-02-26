import numpy as np

def left_endpoint(x_vals: np.array, func: np.ufunc)-> float:
    #takes the differences of all of the x values (representing the width, dx) in the array 
    dx= np.diff(x_vals)
    #returns the sum of the difference in x values (dx) by x plugged into the equation (f(x)) stopping before the last indexed value since it is a left endpoint integral 
    return np.sum(func(x_vals[:-1])*dx)

def trapezoid(x_vals: np.ndarray, func: np.ufunc) -> float:
    #takes the difference of all of the x values in the array (representing dx)
    dx = np.diff(x_vals)
    #returns the trapezoidal integral by finding the sum of left handed x values plus the right handed x values multiplied by the difference in x values and then divided by 2 since that is the formula for a trapezoid 
    return np.sum((func(x_vals[:-1]) + func(x_vals[1:])) * dx / 2)


def simpson(x_vals: np.ndarray, func: np.ufunc) -> float:
    
    n = len(x_vals) - 1
    if n % 2 == 1:
        x_vals = x_vals[:-1]
        n-=1
        
    dx = (x_vals[-1]-x_vals[0])/n
    return (dx/3)* (
            func(x_vals[0])
            +4 * np.sum(func(x_vals[1:-1:2]))
            +2 * np.sum(func(x_vals[2:-2:2]))
            + func(x_vals[-1])
)
