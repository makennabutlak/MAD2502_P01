import numpy as np
def get_barycentric_coordinates(triangle_coordinates: np.array, point_coordinates: np.array) -> np.array:
    #Solomiia Ivanovska coded 
    x1 = triangle_coordinates[0, 0]
    x2 = triangle_coordinates[0, 1]
    x3 = triangle_coordinates[0, 2]
    y1 = triangle_coordinates[1, 0]
    y2 = triangle_coordinates[1, 1]
    y3 = triangle_coordinates[1, 2]

    x = point_coordinates[0]
    y = point_coordinates[1]

    # got this by solving for each element of the barycentric coordinates with te system
    barycentric_1 = ((y2 - y3) * (x - x3) + (x3 - x2) * (y - y3)) / ((y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3))
    barycentric_2 = ((y3 - y1) * (x - x3) + (x1 - x3) * (y - y3)) / ((y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3))
    barycentric_3 = 1 - barycentric_1 - barycentric_2

    return [barycentric_1, barycentric_2, barycentric_3]

def get_cartesian_coordinates(triangle_coordinates: np.array, barycentric_coordinates: np.array) -> np.array:
    x1 = triangle_coordinates[0, 0]
    x2 = triangle_coordinates[0, 1]
    x3 = triangle_coordinates[0, 2]
    y1 = triangle_coordinates[1, 0]
    y2 = triangle_coordinates[1, 1]
    y3 = triangle_coordinates[1, 2]

    b1 = barycentric_coordinates[0]
    b2 = barycentric_coordinates[1]
    b3 = barycentric_coordinates[2]

    x = b1 * x1 + b2 * x2 + b3 * x3
    y = b1 * y1 + b2 * y2 + b3 * y3

    return [x, y]

def is_inside_triangle(triangle_coordinates: np.array, point_coordinates: np.array) -> bool:
    barycentric_coords = get_barycentric_coordinates(triangle_coordinates, point_coordinates)
    barycentric_coords = np.array(barycentric_coords)
    return np.all(barycentric_coords >= 0) and np.all(barycentric_coords <= 1)

