import numpy as np

#def left_endpoint(x_vals: np.ndarray, func: np.ufunc) -> float:
#    sum_left_endpoint = 0
#    for i in range(len(x_vals)-1):
#        sum_left_endpoint += func(x_vals[i])* (x_vals[i+1] - x_vals[i])
#    return sum_left_endpoint

def left_endpoint(x_vals: np.array, func: np.ufunc)-> float:
    difference= np.diff(x_vals)
    return np.sum(func(x_vals[:-1])*difference)

def trapezoid(x_vals: np.ndarray, func: np.ufunc) -> float:
    dx = np.diff(x_vals)
    return np.sum((func(x_vals[:-1]) + func(x_vals[1:])) * dx / 2)


def simpson(x_vals: np.ndarray, func: np.ufunc) -> float:
    dx = np.diff(x_vals)
    n = len(x_vals) - 1
    if n % 2 == 1:
        raise ValueError("The number of intervals must be even for Simpson's rule.")
    return (dx[0] / 3) * np.sum(
        func(x_vals[:-1:2]) + 4 * func(x_vals[1::2]) + func(x_vals[2::2])
    )