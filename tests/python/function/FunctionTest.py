#
# Unit test on a file
# Containing multiple functions
# With specifics test
#
import importlib.util
spec = importlib.util.spec_from_file_location("Tesla", "../../../src/Tesla/Tesla.py")
Tesla = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Tesla)

#
# We instantiate the Tesla Test
#
TeslaTest = Tesla.Tesla()

#
# We Start the TeslaTest
#
TeslaTest.start()

#
# We can generate a Report of the test we are going to do:
#
TeslaTest.setgenerateReport(True)

#
# Let's test all methods contains in the file : Functiontest.py
# Or a directory:
#

# In case we test all functions contains in a file
TeslaTest.Function("./Functions.py")

#Functions
#Functionses in a specific directory, recursively
#Functionsll proceed with tests
#Functions
#TeslaTest.Function("./group_of_script_files", [".py"])

# Most Important, ALWAYS We need to End the test.
TeslaTest.end()

# We Print the Report resume:
print(TeslaTest.getresume()) 