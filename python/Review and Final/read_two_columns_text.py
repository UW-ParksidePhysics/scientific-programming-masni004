import numpy as np

def read_two_columns_text(filename: str) -> np.ndarray:
    """
    Uses a string as input, outputs a 2D array, one dimension for x and y values respectively.
    """
    try:
        # Unloads the text file
        data = np.loadtxt(filename, unpack=True)
    except OSError as e:
        # Informs that there is an error
        raise
    return data

if __name__ == "__main__":
    # Test: read in volumes_energies.dat and print data with its shape
    text_file = "volumes_energies.dat"
    data = read_two_columns_text(text_file)
    print(f"{data=}, shape={data.shape}")