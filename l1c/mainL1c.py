
# MAIN FUNCTION TO CALL THE L1C MODULE

from l1c.src.l1c import l1c

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = r'C:\ALBERTO\EODP\Test2\auxiliary'
# GM dir + L1B dir
indir = r'C:\ALBERTO\EODP\Test2\EODP_TER\EODP-TS-L1C\input\gm_alt100_act_150,C:\ALBERTO\EODP\Test2\EODP_TER\EODP-TS-L1C\input\l1b_output'
outdir = r'C:\ALBERTO\EODP\Test2\EODP_TER\EODP-TS-L1C\outputsAlberto'

# Initialise the ISM
myL1c = l1c(auxdir, indir, outdir)
myL1c.processModule()
