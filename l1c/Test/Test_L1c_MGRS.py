#7. EODP-TS-L1C-0001. MGRS

from common.io.writeToa import readToa
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from config import globalConfig
from config.l1bConfig import l1bConfig

# STATEMENT
# Check for all bands that the differences with respect to the output TOA (l1b_toa_) are <0.01% for at
# least 3-sigma of the points.

bands = ['VNIR-0','VNIR-1','VNIR-2','VNIR-3']
Alberto_toa_path = r"C:\ALBERTO\EODP\Test2\EODP_TER\EODP-TS-L1C\outputsAlberto"
luss_toa_path = r"C:\ALBERTO\EODP\Test2\EODP_TER\EODP-TS-L1C\output"

l1b_toa = 'l1c_toa_'

#Check for all bands that the differences with respect to the output TOA are <0.01% for 3-sigma of the points.

for band in bands:

    # 1. Read LUSS
    luss_toa = readToa(luss_toa_path, l1b_toa + band + '.nc')

    # 2. Read my outputs
    Alberto_toa = readToa(Alberto_toa_path, l1b_toa + band + '.nc')

    # 3. Comparison
    Diff = np.sort(Alberto_toa) - np.sort(luss_toa)
    Error = Diff / Alberto_toa * 100
    df = pd.DataFrame(Error)
    Error_df = df.fillna(0) # The division per zero gives some annoying NaN values
    boolean_comparison = np.array(Error_df < 0.01)

    # Calculations #
    # Calculate the total number of values in each matrix
    Tot_Values = boolean_comparison.size
    Trues_Matrix = np.full(boolean_comparison.shape, True)
    # Calculate the number of matching values 
    matching_values = np.sum(boolean_comparison == Trues_Matrix)
    # 3-Sigma Condition
    threshold = 0.997 * total_values
    # Apply 3-Sigma Condition to the matching values
    is_3sigma = matching_values >= threshold

    if is_3sigma == True:
        print("The differences with respect to the output TOA (", l1b_toa + band,
            ") ARE <0.01% for at least 3-sigma of the points.")
    else:
        print("The differences with respect to the output TOA (", l1b_toa + band,
            ") ARE NOT all <0.01% for at least 3-sigma of the points.")


   
    a = 2