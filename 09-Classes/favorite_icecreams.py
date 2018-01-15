from collections import OrderedDict

favorite_ice_creams = OrderedDict()

favorite_ice_creams["jenny"] = "chocolate"
favorite_ice_creams["anna"] = "vanilla"
favorite_ice_creams["kevin"] = "strawberry"
favorite_ice_creams["albert"] = "mango"

print(favorite_ice_creams)
for name, ice_cream in favorite_ice_creams.items():
    print(name.title() + "'s favorite ice cream is " + ice_cream.title() + ".")
