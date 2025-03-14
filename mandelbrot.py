import numpy as np

# Part 1
def get_escape_time(c: complex, max_iterations: int) -> int | None:
    """"
    Computes the escape time for a given complex number in the Mandelbrot set by iterating the function z = z**2 + c,
    starting with z = c to determine how many iterations it takes for the absolute value of z to exceed 2.
    """
    z = c
    for Iterations in range(max_iterations):
        if abs(z) > 2:
            return Iterations
        z = z**2 + c
    return None

#Part 2
def get_complex_grid(
        top_left: complex,
        bottom_right: complex,
        step: float,
) -> np.ndarray:
    real_value = np.arange(top_left.real, bottom_right.real, step) #Generate Real Values
    imag_value = np.arange(top_left.imag, bottom_right.imag, -step) #Generate Imaginary Values

    grid = real_value[np.newaxis, :] + 1j * imag_value[:, np.newaxis] #Generate Complex Grid

    return grid


def get_julia_escape_time(z: complex, c: complex, max_iterations: int) -> int:
    """
    Computes the escape time for a given complex number z under the Julia set iteration by going through Julia set to
    see if complex number escapes and if a complex number never escapes, the max number of iterations will be returned
    instead.

    z_array is a """
    for i in range(max_iterations):
        if abs(z) > 2:
            return i
        z = z**2 + c
    return max_iterations  # If it never escapes, return max_iterations


def get_julia_color_arr(z_arr: np.ndarray, c: complex, max_iterations: int) -> np.ndarray:
    """
    Generates the Julia set color array by computing escape times and printing the resulting shape of the Julia set in
    MatPlot.
    """
    color_arr = np.array([])

    for row in z_arr:
        for z in row:
            escape_time = get_julia_escape_time(z, c, max_iterations)
            color_arr = np.append(color_arr, (max_iterations - escape_time + 1) / (max_iterations + 1))

    return color_arr.reshape(z_arr.shape)  # Reshape to match input grid









