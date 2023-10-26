#!/usr/bin/env python
# -*- coding=utf-8 -*-

import os
import sys
import numpy as np
from datetime import datetime, timedelta
from scipy.spatial import KDTree

# 采用dk树插值算法
class KDResampler:
    def __init__(self, data, x, y, roi=0.5):
        self.tree = KDTree(np.dstack((x.ravel(), y.ravel()))[0])
        self.data = data
        self.roi = roi

    def map_data(self, x_out, y_out):
        out_coords = np.dstack((x_out.ravel(), y_out.ravel()))[0]
        _, self.indices = self.tree.query(out_coords, distance_upper_bound=self.roi)
        # 表示是否有超过self.roi距离，超过True
        self.invalid_mask = self.indices == self.tree.n
        self.indices[self.invalid_mask] = 0
        data = self.data.ravel()[self.indices]
        data[self.invalid_mask] = np.nan
        return data

