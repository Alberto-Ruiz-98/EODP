
# MAIN FUNCTION TO CALL THE ISM MODULE

from ism.src.ism import ism

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = r'C:\ALBERTO\EODP\Test2\auxiliary'
indir = r"C:\ALBERTO\EODP\Test2\EODP_TER\EODP-TS-ISM\input\gradient_alt100_act150" # small scene
outdir = r"C:\ALBERTO\EODP\Test2\EODP_TER\\EODP-TS-ISM\outputsAlberto"


# Initialise the ISM
myIsm = ism(auxdir, indir, outdir)
myIsm.processModule()
