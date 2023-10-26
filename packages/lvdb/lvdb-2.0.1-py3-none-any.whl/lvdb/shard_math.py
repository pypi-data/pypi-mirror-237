import numpy as np

from .error_handler import ErrorHandler


def normalize(a, order = 1, axis = -1):
    if len(a.shape) > 2:
        handler = ErrorHandler
        handler.shape_error()

    l1_norm = np.atleast_1d(np.linalg.norm(a, order, axis))
    l1_norm[l1_norm==0] = 1
    return a / np.expand_dims(l1_norm, axis)

def shard_reference(basis, unit_vector):
    # Add 1 to shift bounds from [-1, 1] to [0, 2]
    return np.dot(basis, unit_vector) + 1
