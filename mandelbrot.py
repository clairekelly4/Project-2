import numpy as np

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

