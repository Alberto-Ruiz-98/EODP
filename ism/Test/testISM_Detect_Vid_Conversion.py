#5. EODP-TS-ISM-0002_DETECTION_&_VIDEO_CONVERSION
import pandas as pd

from common.io.writeToa import readToa
from common.io.readMat import readMat
from common.io.readArray import readArray
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from config import globalConfig
from config.l1bConfig import l1bConfig

# STATEMENT
#Check for all bands that the differences with respect to the output TOA (ism_toa_) are <0.01% for at least 3-sigma of the points.

bands = ['VNIR-0','VNIR-1','VNIR-2','VNIR-3']
Alberto_toa_path = r"C:\ALBERTO\EODP\EODP_TER\\EODP-TS-ISM\outputsAlberto"
luss_toa_path = r"C:\ALBERTO\EODP\Test2\EODP_TER\EODP-TS-ISM\output"

ism_toa_ = 'ism_toa_'

for band in bands:

    # 1. Read LUSS Outputs to compare
    luss_toa = readToa(luss_toa_path, ism_toa_ + band + '.nc')

    # 2. Read my outputs
    Alberto_toa = readToa(Alberto_toa_path, ism_toa_ + band + '.nc')

    # 3. Comparison
    Diff = Alberto_toa - luss_toa
    Error = Diff / Alberto_toa * 100
    df = pd.DataFrame(Error)
    Error_df = df.fillna(0) 
    boolean_comparison = np.array(Error_df < 0.01)

    # Calculations #
    # Calculate the total number of values in each matrix
    Tot_values = boolean_comparison.size
    Trues_Matrix = np.full(boolean_comparison.shape, True)
    # Calculate the number of matching values 
    matching_values = np.sum(boolean_comparison == Trues_Matrix)
    # 3-Sigma Condition
    threshold = 0.997 * Tot_values
    # Apply 3-Sigma condition to the matching values
    is_3sigma = matching_values >= threshold

    if is_3sigma == True:
        print("The differences with respect to the output TOA (", ism_toa_ + band,
            ") ARE <0.01% for at least 3-sigma of the points.")
    else:
        print("The differences with respect to the output TOA (", ism_toa_ + band,
            ") ARE NOT all <0.01% for at least 3-sigma of the points.")



    # Percentage of saturated pixels per band.

    Alberto_toa = readToa(Alberto_toa_path, ism_toa_ + band + '.nc')

    number_saturated_values = np.sum(Alberto_toa == 4095)
    Error_saturated = number_saturated_values * 100 / Alberto_toa.size
    print("The percentage of saturated values for", ism_toa_ + band,"is", "{:.2f}".format(Error_saturated), "%.")
