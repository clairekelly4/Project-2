import numpy as np

# Part 1
def get_escape_time(c: complex, max_iterations: int) -> int | None:
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

# Part 3
def get_escape_time_color_arr(
    c_arr: np.ndarray,
    max_iterations: int
) -> np.ndarray:
    color_arr = np.array([])
    for mini in c_arr:
        for c in mini:
            escape_time = get_escape_time(c, max_iterations)
            if escape_time is not None:
                color_arr = np.append(color_arr, (max_iterations - escape_time + 1)/(max_iterations + 1))
            else:
                color_arr = np.append(color_arr, 0/(max_iterations + 1))

    color_final = color_arr.reshape(c_arr.shape)
    return color_final
