#4. EODP-TS-ISM-0001_OPTICAL STAGE
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
#Check for all bands that the differences with respect to the output TOA (ism_toa_isrf) are <0.01% for at least 3-sigma of the points.

bands = ['VNIR-0','VNIR-1','VNIR-2','VNIR-3']
Alberto_toa_path = r"C:\ALBERTO\EODP\Test2\EODP_TER\EODP-TS-ISM\outputsAlberto"
luss_toa_path = r"C:\ALBERTO\EODP\Test2\EODP_TER\EODP-TS-ISM\output"

ism_toa_isrf = 'ism_toa_isrf_'
ism_toa_optical = 'ism_toa_optical_'
Hdiff = 'Hdiff_'
Hdefoc = 'Hdefoc_'
Hwfe = 'Hwfe_'
Hdet = 'Hdet_'
Hsmear = 'Hsmear_'
Hmotion = 'Hmotion_'
Hsys = 'Hsys_'
fnAct = 'fnAct_'
fnAlt = 'fnAlt_'

for band in bands:

    # 1. Read LUSS Outputs to compare
    luss_toa = readToa(luss_toa_path, ism_toa_isrf + band + '.nc')

    # 2. Read my outputs
    Alberto_toa = readToa(Alberto_toa_path, ism_toa_isrf + band + '.nc')

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
    N_Match_Values = np.sum(boolean_comparison == Trues_Matrix)
    # 3-Sigma Condition
    threshold = 0.997 * Tot_values
    # Apply 3-Sigma condition to the matching values
    is_3sigma = N_Match_Values >= threshold

    if is_3sigma == True:
        print("The differences with respect to the output TOA (", ism_toa_isrf + band,
            ") ARE <0.01% for at least 3-sigma of the points.")
    else:
        print("The differences with respect to the output TOA (", ism_toa_isrf + band,
            ") ARE NOT all <0.01% for at least 3-sigma of the points.")

    # Check for all bands that the differences with respect to the output TOA (ism_toa_optical) are <0.01%
    # for at least 3-sigma of the points.

    # 1. Read LUSS Outputs to compare
    luss_toa = readToa(luss_toa_path, ism_toa_optical + band + '.nc')

    # 2. Read my outputs
    Alberto_toa = readToa(Alberto_toa_path, ism_toa_optical + band + '.nc')

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
    N_Match_Values = np.sum(boolean_comparison == Trues_Matrix)
    # 3-Sigma Condition
    threshold = 0.997 * Tot_values
    # Apply 3-Sigma condition to the matching values
    is_3sigma = N_Match_Values >= threshold

    if is_3sigma == True:
        print("The differences with respect to the output TOA (", ism_toa_optical + band,
                  ") ARE <0.01% for at least 3-sigma of the points.")
    else:
        print("The differences with respect to the output TOA (", ism_toa_optical + band,
                  ") ARE NOT all <0.01% for at least 3-sigma of the points.")

    #Plotting the system MTF and all of its contributors
        #:param Hdiff: Diffraction MTF
        #:param Hdefoc: Defocusing MTF
        #:param Hwfe: Wavefront electronics MTF
        #:param Hdet: Detector MTF
        #:param Hsmear: Smearing MTF
        #:param Hmotion: Motion blur MTF
        #:param Hsys: System MTF
        #:param nlines: Number of lines in the TOA
        #:param ncolumns: Number of columns in the TOA
        #:param fnAct: normalised frequencies in the ACT direction (f/(1/w))
        #:param fnAlt: normalised frequencies in the ALT direction (f/(1/w))
        #:param directory: output directory
        #:param band: band
        #:return: N/A

    # Read my outputs
    Alberto_Hdiff = readMat(Alberto_toa_path, Hdiff + band + '.nc')
    Alberto_Hdefoc = readMat(Alberto_toa_path, Hdefoc + band + '.nc')
    Alberto_Hwfe = readMat(Alberto_toa_path, Hwfe + band + '.nc')
    Alberto_Hdet = readMat(Alberto_toa_path, Hdet + band + '.nc')
    Alberto_Hsmear = readMat(Alberto_toa_path, Hsmear + band + '.nc')
    Alberto_Hmotion = readMat(Alberto_toa_path, Hmotion + band + '.nc')
    Alberto_Hsys = readMat(Alberto_toa_path, Hsys + band + '.nc')
    Alberto_fnAct = readArray(Alberto_toa_path, fnAct + band + '.nc')
    Alberto_fnAlt = readArray(Alberto_toa_path, fnAlt + band + '.nc')

    #fnAct: 1D normalised frequencies 2D ACT (f/(1/w))
    number_lines_ALT = Alberto_Hdiff.shape[0]
    ACT_central_line = int(number_lines_ALT / 2)
    number_lines_ACT = Alberto_Hdiff.shape[1]
    ALT_central_line = int(number_lines_ACT / 2)


    # ACT
    plt.plot(Alberto_fnAct[75:150], Alberto_Hdiff[ACT_central_line, 75:150])
    plt.plot(Alberto_fnAct[75:150], Alberto_Hdefoc[ACT_central_line, 75:150])
    plt.plot(Alberto_fnAct[75:150], Alberto_Hwfe[ACT_central_line, 75:150])
    plt.plot(Alberto_fnAct[75:150], Alberto_Hdet[ACT_central_line, 75:150])
    plt.plot(Alberto_fnAct[75:150], Alberto_Hsmear[ACT_central_line, 75:150])
    plt.plot(Alberto_fnAct[75:150], Alberto_Hmotion[ACT_central_line, 75:150])
    plt.plot(Alberto_fnAct[75:150], Alberto_Hsys[ACT_central_line, 75:150], color='black', linewidth=3)
    plt.plot(np.full(2, 0.5), np.linspace(0, 1, 2), linestyle='--', color='black')
    plt.xlabel('Spatial frequencies f/(1/w) [-]')
    plt.ylabel('MTF')
    plt.title("System MTF, slice ACT for " + band )
    plt.legend(['Diffraction MTF', 'Defocus MTF', 'WFE Aberration MTF', 'Detector MTF', 'Smearing MTF', 'Motion blur MTF', 'System MTF','f Nyquist'])
    plt.xlim(-0.025, 0.525)
    plt.ylim(-0.025, 1.025)
    plt.savefig("ism_plot_MTF_ACT_" + band + ".png")
    plt.show()


    # ALT
    plt.plot(Alberto_fnAlt[50:100], Alberto_Hdiff[50:100, ALT_central_line])
    plt.plot(Alberto_fnAlt[50:100], Alberto_Hdefoc[50:100, ALT_central_line])
    plt.plot(Alberto_fnAlt[50:100], Alberto_Hwfe[50:100, ALT_central_line])
    plt.plot(Alberto_fnAlt[50:100], Alberto_Hdet[50:100, ALT_central_line])
    plt.plot(Alberto_fnAlt[50:100], Alberto_Hsmear[50:100, ALT_central_line])
    plt.plot(Alberto_fnAlt[50:100], Alberto_Hmotion[50:100, ALT_central_line])
    plt.plot(Alberto_fnAlt[50:100], Alberto_Hsys[50:100, ALT_central_line], color='black', linewidth=3)
    plt.plot(np.full(2, 0.5), np.linspace(0, 1, 2), linestyle='--', color='black')
    plt.xlabel('Spatial frequencies f/(1/w) [-]')
    plt.ylabel('MTF')
    plt.title("System MTF, slice ALT for " + band )
    plt.legend(
        ['Diffraction MTF', 'Defocus MTF', 'WFE Aberration MTF', 'Detector MTF', 'Smearing MTF', 'Motion blur MTF',
         'System MTF', 'f Nyquist'])
    plt.xlim(-0.025, 0.525)
    plt.ylim(-0.025, 1.025)
    plt.savefig("ism_plot_MTF_ALT_" + band + ".png")
    plt.show()

    a = 2


    



