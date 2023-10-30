# 6. EODP-TS-L1B-0001_Equalization_&_Restoration

from common.io.writeToa import readToa
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from config import globalConfig
from config.l1bConfig import l1bConfig

# # Check for all bands that the differences with respect to the output TOA (l1b_toa_) are <0.01% for at
# least 3-sigma of the points.
bands = ['VNIR-0','VNIR-1','VNIR-2','VNIR-3']
my_toa_path = r"C:\EODP\EODP_TER\EODP-TS-L1B\outputcarlos"
luss_toa_path = r"C:\EODP\EODP_TER\EODP-TS-L1B\output"
isrf_toa_path = r"C:\EODP\EODP_TER\EODP-TS-ISM\output"
l1b_toa = 'l1b_toa_'
l1b_toa_eq = 'l1b_toa_eq_'
ism_toa_isrf = 'ism_toa_isrf_'


# 1.- Read LUSS


toa_luss = readToa()


#2.- Read my outputs

#3. Compare