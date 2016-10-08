# -*- coding: utf-8 -*-

# Author: Ivo Romario <ivo.romario@gmail.com>
# License:

import numpy as np


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
