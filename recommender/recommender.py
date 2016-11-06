# -*- coding: utf-8 -*-

# Author: Ivo Romario <ivo.romario@gmail.com>
# License:

import numpy as np
import pandas as pd

from similarity import cosine_similarity, cosine_distance

class BaseRecommender(object):

    def __init__(self, path):
        self.dataset = self.load_dataset(path)

    def recommend(self):
        raise NotImplementedError("class method cannot be called")

    def load_dataset(self, path):
        try:
            return pd.read_hdf(path, 'uiMatrix').as_matrix()
        except Exception as e:
            raise e


class SocialRecommender(BaseRecommender):

    def __init__(self, path):
        super(self.__class__, self).__init__(path)
#        self.users_similarity = self.generate_users_similarity()

    def generate_users_similarity(self, metric='cosine'):
        if metric not in ['cosine']:
            raise ValueError("Metric {} is not implemented".format(metric))
        if metric == 'cosine':
            return cosine_distance(self.dataset, axis=0)

    def recommend(self):
        raise NotImplementedError("class method cannot be called")
