
'''
This module shows how the improvements mentioned in the bottom of the exercise
text could be implemented. 
'''

import numpy as np


def extract_intervals(x, *x_bounds):
    ''' Return the indices values in y that are within the range x_bounds.

    As many intervals as desired can be given.

    Parameters
    ----------
    x : 1D numpy array
        x-coordinates sorted in ascending order.
    *x_bounds : tuple(s)
        Two-element tuple(s) defining the interval(s) within which to
        extract x-indices. Both boundary values in each tuple are inclusive.

    Returns
    -------
    numpy 1D array
        Array of indices for `x`-values that reside within `x_bounds`.

    Assumptions
    ------------
    The function assumes that the input array `x` is sorted in ascending order.
    '''

    # Create list of boolean arrays for each interval (mask arrays)
    mask = [(x >= xb[0]) & (x <= xb[1]) for xb in x_bounds]

    # Overlay boolean arrays, keep 'True' at an index if it is in any array
    s = mask[0] if len(mask) == 1 else np.logical_or.reduce(mask)

    # Extract idx in intervals by fancy indexing (extract where cond is True)
    idx = np.where(s)

    return idx


if __name__ == '__main__':

    x = np.array([ -5.2, -3.7, -1.4, 1.4, 3.5, 4.2, 8.2, 10.4, 12.0])
    idx = extract_intervals(x, (-2.0, 1.9))
    print(idx)

    x = np.array([ -5.2, -3.7, -1.4, 1.4, 3.5, 4.2, 8.2, 10.4, 12.0])
    idx = extract_intervals(x, (-2.0, 1.9), (4.1, 11.3))
    print(idx)

