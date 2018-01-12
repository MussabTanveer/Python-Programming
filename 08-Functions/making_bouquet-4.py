# Importing All Functions in a Module
# to import every function in a module use the asterisk (*) operator
# because every function is imported, you can call each function by name without using the dot notation
# it’s best not to use this approach when you’re working with larger modules that you did not write
# from module_name import *

from bouquet import *

make_bouquet("small", "rose")
make_bouquet("large", "rose", "tulip", "jasmine")
