
# MAIN FUNCTION TO CALL THE L1B MODULE

from l1b.src.l1b import l1b

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = r'C:\ALBERTO\EODP\Test2\auxiliary'
indir = r'C:\ALBERTO\EODP\Test2\EODP_TER\EODP-TS-L1B\input'
outdir = r'C:\ALBERTO\EODP\Test2\EODP_TER\EODP-TS-L1B\outputsAlberto'

# Initialise the ISM
myL1b = l1b(auxdir, indir, outdir)
myL1b.processModule()
