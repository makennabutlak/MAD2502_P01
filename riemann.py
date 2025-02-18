import numpy as np

import numpy as np


def left_endpoint(x_vals: np.ndarray, func: np.ufunc) -> float:
    sum_left_endpoint = 0
    a = 0
    b = 1
    while x_vals[b] <= x_vals.size:
        sum_left_endpoint += func(x_vals[a]) * (x_vals[b] - x_vals[a])
    return sum_left_endpoint

def trapezoid(x_vals: np.ndarray, func: np.ufunc) -> float:
    dx = np.diff(x_vals)
    return np.sum((func(x_vals[:-1]) + func(x_vals[1:])) * dx / 2)