# 6. EODP-TS-L1B-0001_Equalization_&_Restoration

from common.io.writeToa import readToa
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from config import globalConfig
from config.l1bConfig import l1bConfig

# STATEMENT
# Check for all bands that the differences with respect to the output TOA (l1b_toa_) are <0.01% for at
# least 3-sigma of the points.

bands = ['VNIR-0','VNIR-1','VNIR-2','VNIR-3']
Alberto_toa_path = r"C:\ALBERTO\EODP\Test2\EODP_TER\EODP-TS-L1B\outputsAlberto"
luss_toa_path = r"C:\ALBERTO\EODP\Test2\EODP_TER\EODP-TS-L1B\output"
isrf_toa_path = r"C:\ALBERTO\EODP\Test2\EODP_TER\EODP-TS-ISM\output"


l1b_toa = 'l1b_toa_'
l1b_toa_eq = 'l1b_toa_eq_'
ism_toa_isrf = 'ism_toa_isrf_'

for band in bands:

    # 1. Read LUSS
    luss_toa = readToa(luss_toa_path, l1b_toa + band + '.nc')

    # 2. Read my outputs
    Alberto_toa = readToa(Alberto_toa_path, l1b_toa + band + '.nc')
    Alberto_toa_eq = readToa(Alberto_toa_path, l1b_toa_eq + band + '.nc')

    # 3. Comparison
    Diff = Alberto_toa - luss_toa
    Error = Diff / Alberto_toa * 100
    df = pd.DataFrame(Error)
    Error_df = df.fillna(0)  # The division per zero gives some annoying NaN values
    boolean_comparison = np.array(Error_df < 0.01)

    # Calculations #
    # Calculate the total number of values in each matrix
    Tot_Values = boolean_comparison.size
    Trues_Matrix = np.full(boolean_comparison.shape, True)
    # Calculate the number of matching values
    matching_values = np.sum(boolean_comparison == Trues_Matrix)
    # 3-Sigma Condition
    threshold = 0.997 * Tot_Values
    # Apply 3-Sigma condition to the matching values
    is_3sigma = matching_values >= threshold
    
    
    if is_3sigma == True:
        print("The differences with respect to the output TOA (", l1b_toa + band,") ARE <0.01% for at least 3-sigma of the points.")
    else:
        print("The differences with respect to the output TOA (", l1b_toa + band,") ARE NOT all <0.01% for at least 3-sigma of the points.")


    #For the central ALT position, plot the restored signal (l1b_toa), and the TOA after the ISRF
    #(ism_toa_isrf). 

    # For restored I understand ours equalizated toa
    number_lines_ALT = Alberto_toa.shape[0]
    ALT_central_line = int(number_lines_ALT/2)
    isrf_toa = readToa(isrf_toa_path, ism_toa_isrf + band + '.nc')

    # Ploting with Condition if we are equalizing or not

    if l1bConfig().do_equalization == True:
        plt.plot(Alberto_toa[ALT_central_line])
        plt.plot(isrf_toa[ALT_central_line])
        plt.xlabel('ACT pixel [-]')
        plt.ylabel('TOA [mW/m2/sr]')
        plt.title("Effect of equalization for " + band)
        plt.legend(['TOA LB1 with eq', 'TOA after the ISRF'])
        plt.savefig("l1b_plot_eq"+band+".png") 
        plt.show() 
    else:
        plt.plot(Alberto_toa[ALT_central_line])
        plt.plot(isrf_toa[ALT_central_line])
        plt.xlabel('ACT pixel [-]')
        plt.ylabel('TOA [mW/m2/sr]')
        plt.title("Effect of no equalization for " + band)
        plt.legend(['TOA LB1 without eq', 'TOA after the ISRF'])
        plt.savefig("l1b_plot_no_eq" + band + ".png")
        plt.show()


