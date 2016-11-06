# -*- coding: utf-8 -*-

# Author: Ivo Romario <ivo.romario@gmail.com>
# License:

import numpy as np
from scipy.spatial import distance

def cosine_similarity(x, y):
    """
    Compute cosine similarity between arrays x and y.

    Parameters:
    ----------
    x : numpy array with shape=(1, n_features)

    y : numpy array with shape=(1, n_features)

    Returns:
    -------
    similarity score : float with value between 0.0 and 1.0
    """

    if x.shape != y.shape:
        raise ValueError("Incompatible dimension for x and y arrays: "
                "x.shape == {0} and y.shape == {1}".format(x.shape, y.shape))
    xy = sum([m*n for m,n in zip(x,y)])
    x = np.sqrt(sum([n**2 for n in x]))
    y = np.sqrt(sum([n**2 for n in y]))
    return xy / (x*y)

def cosine_distance(X, axis=0):
    X = X.T if axis==1 else X
    rows, cols = X.shape
    similarities = [distance.cdist(X, X[row, :].reshape(1,-1), 'cosine') for row in xrange(rows)]
    return np.hstack(similarities)

