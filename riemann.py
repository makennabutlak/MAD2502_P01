import numpy as np

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
        return trapezoid(x_vals, func)
    dx = (x_vals[-1]-x_vals[0])/n
    return (dx/3)* (func(x_vals[0])+4* np.sum(func(x_vals[1:-1:2]))+2 * np.sum(func(x_vals[2:-2:2]))+ func(x_vals[-1]))