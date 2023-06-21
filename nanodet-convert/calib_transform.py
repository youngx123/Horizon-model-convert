"""
# -*- coding: utf-8 -*-
# @Author  : youngx
# @Time    : 2023/6/21 16:33
# @FileName : calib_transform
"""
import cv2
from nanodet.data.transform import Pipeline
import os
import numpy as np
from tqdm import tqdm


# pipline = {"normalize": [[103.53, 116.28, 123.675], [57.375, 57.12, 58.395]]}
pipline = {"normalize": [[0, 0, 0], [1,1, 1]]}
keep_ratio = False


transform = Pipeline(pipline, keep_ratio)

if __name__ == '__main__':
    src_dir = r"E:\Share_Files\hb_mapper infer\nanodet-convert\src_data"
    save_dir = r"E:\Share_Files\hb_mapper infer\nanodet-convert\calibration-data"
    file_names = os.listdir(src_dir)

    meta = dict()
    for file in tqdm(file_names, desc="convert data formate ..."):
        save_name = os.path.join(save_dir, file)
        file = os.path.join(src_dir, file)

        image = cv2.imread(file)
        meta["img"] = image

        meta = transform(None,meta, (320, 320))

        meta["img"].transpose(2,1,0).astype(np.float32).tofile(save_name)