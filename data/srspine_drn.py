# -*- coding: utf-8 -*-
# @Author  : runze.wang
# @Time    : 2020/10/14 10:58 上午

import os
from data import srdata

class SRSpine_DRN(srdata.SRData):
    def __init__(self, args, name='SRSpine_DRN', train=True, benchmark=False):
        super(SRSpine_DRN, self).__init__(
            args, name=name, train=train, benchmark=benchmark
        )

    def _set_filesystem(self, data_dir):
        super(SRSpine_DRN, self)._set_filesystem(data_dir)
        if self.train:
            self.dir_hr = os.path.join(self.apath, 'train_HR')
            self.dir_lr = os.path.join(self.apath, 'train_LR')
        else:
            self.dir_hr = os.path.join(self.apath, 'val_HR')
            self.dir_lr = os.path.join(self.apath, 'val_LR')

