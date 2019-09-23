import os
import cv2
import numpy as np
import time
import random
from airtest.core.api import *


crop_img=[255,0,0,255,255]
if len(np.nonzero(crop_img)[0]) == 0:
    print("xxx")
print(np.nonzero(crop_img)[0][-1])
print(np.nonzero(crop_img)[0])
print(int(np.mean(np.nonzero(crop_img)[0])))