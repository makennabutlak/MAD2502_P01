import numpy as np
def get_barycentric_coordinates(triangle_coordinates: np.array, point_coordinates: np.array) -> np.array:
    '''
    Calculates the barycentric coordinates of P given a point P=(x,y) and a triange with verticies A1=(x1,y1), A2=(x2,y2), and A3=(x3,y3).

    Parameters:
    triangle_coordinates - the 3 coordinates of the triangle given as a 2-by-3 numpy array
    point_coordinates - the point P as a 1d numpy array

    Returns:
    Barycentric coordinates as a 1d numpy array
    '''
    
    # Verticies of triangle
    x1 = triangle_coordinates[0, 0]
    x2 = triangle_coordinates[0, 1]
    x3 = triangle_coordinates[0, 2]
    y1 = triangle_coordinates[1, 0]
    y2 = triangle_coordinates[1, 1]
    y3 = triangle_coordinates[1, 2]

    # Point P
    x = point_coordinates[0]
    y = point_coordinates[1]

    # got this by solving for each element of the barycentric coordinates with the system
    barycentric_1 = ((y2 - y3) * (x - x3) + (x3 - x2) * (y - y3)) / ((y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3))
    barycentric_2 = ((y3 - y1) * (x - x3) + (x1 - x3) * (y - y3)) / ((y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3))
    barycentric_3 = 1 - barycentric_1 - barycentric_2

    return [barycentric_1, barycentric_2, barycentric_3]

def get_cartesian_coordinates(triangle_coordinates: np.array, barycentric_coordinates: np.array) -> np.array:
    '''
    Calculates the cartesian coordinates of a triange with verticies A1=(x1,y1), A2=(x2,y2), and A3=(x3,y3) provided the barycentric_coordinates.

    Parameters:
    triangle_coordinates - the 3 coordinates of the triangle given as a 2-by-3 numpy array
    barycentric_coordinates - the barycentric coordinates as a 1d numpy array

    Returns:
    Cartesian coordinates as a 1d numpy array in the form (x,y)
    '''

    # Verticies of triangle
    x1 = triangle_coordinates[0, 0]
    x2 = triangle_coordinates[0, 1]
    x3 = triangle_coordinates[0, 2]
    y1 = triangle_coordinates[1, 0]
    y2 = triangle_coordinates[1, 1]
    y3 = triangle_coordinates[1, 2]

    # Barycentric coordinates
    b1 = barycentric_coordinates[0]
    b2 = barycentric_coordinates[1]
    b3 = barycentric_coordinates[2]
    
    # Calculation of point using system
    x = b1 * x1 + b2 * x2 + b3 * x3
    y = b1 * y1 + b2 * y2 + b3 * y3

    return [x, y]

def is_inside_triangle(triangle_coordinates: np.array, point_coordinates: np.array) -> bool:

    """
    Determines whether a given point is inside a triangle using barycentric coordinates.

    :param triangle_coordinates: A 2x3 numpy array where each column represents a vertex (x, y).
    :param point_coordinates: A numpy array (x, y) representing the point to check.
    :return: True if the point is inside the triangle, False otherwise.
    """
     # Compute the barycentric coordinates of the given point with respect to the triangle
    barycentric_coords = get_barycentric_coordinates(triangle_coordinates, point_coordinates)
    # Convert the result into a NumPy array to enable vectorized operations
    barycentric_coords = np.array(barycentric_coords)
    # Check if all barycentric coordinates are within the range [0, 1]
    # If all values are between 0 and 1, the point is inside or on the triangle
    return np.all(barycentric_coords >= 0) and np.all(barycentric_coords <= 1)

