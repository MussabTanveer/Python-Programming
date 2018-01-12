# Using as to Give a Function an Alias
# use alias if the name of a function importing conflict with an existing name in program or if the function name is long
# from module_name import function_name as fn

from bouquet import make_bouquet as mb

mb("small", "rose")
mb("large", "rose", "tulip", "jasmine")
