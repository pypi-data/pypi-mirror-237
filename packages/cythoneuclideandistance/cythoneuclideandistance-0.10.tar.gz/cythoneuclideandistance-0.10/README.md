# Calculate Euclidean distances between two sets of coordinates (Cython and Numexpr)

## Tested against Windows / Python 3.11 / Anaconda

## pip install cythoneuclideandistance

```python
Calculate Euclidean distances between two sets of coordinates.

This function computes the Euclidean distance matrix between two sets of coordinates.

Args:
    coords1 (numpy.ndarray): An array of shape (n, 2) containing the first set of coordinates.
    coords2 (numpy.ndarray): An array of shape (m, 2) containing the second set of coordinates.

Returns:
    numpy.ndarray: A 2D array of shape (n, m) containing the Euclidean distances between all pairs of coordinates.

Example:
    import random
    import cythoneuclideandistance
    import numpy as np

    coords1 = np.array(
        [[random.randint(1, 1000), random.randint(1, 1000)] for _ in range(23000)],
        dtype=np.int32,
    )
    coords2 = np.array(
        [[random.randint(1, 1000), random.randint(1, 1000)] for _ in range(22150)],
        dtype=np.int32,
    )

    distance_matrix = cythoneuclideandistance.calculate_euc_distance(coords1, coords2)
    print(distance_matrix)

```