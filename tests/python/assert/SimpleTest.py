# A test by Sanix darker
# We import the Tesla module
from Tesla import Tesla
import math

# A testing method that return the Square of a value
def square(value):
    return math.sqrt(value)

#
# We instantiate the Tesla Test
#
TeslaTest = Tesla()

#
# We Start the TeslaTest
#
TeslaTest.start()

#
# We can generate a Report of the test we are going to do:
#
TeslaTest.setgenerateReport(True)

#
# TeslaTest.isTrue method
# [Required] param 1 : The statement
# [Optionnal] param 2 : A small title of the test or the statement in string
# [Optionnal] param 3 : A Description of the current test with more details
#
TeslaTest.isTrue( square(25) == 5, "Check SQRT(25) == 5 ?", "We are trying to check here if sqrt of 25 is equal to 5" )
 
#
# TeslaTest.isEqual method
# Checking if 1 == 1
#
TeslaTest.isEqual(1, 1)

#
# TeslaTest.isEqual method
# Checking if 1 > 1
#
TeslaTest.isSup(1, 1)

# ...
# There is a lot of more method, you can check on the Wiki
# ...

# Most Important, ALWAYS We need to End the test.
TeslaTest.end()

# We Print the Report resume:
print(TeslaTest.getresume()) 