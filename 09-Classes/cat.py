class Cat():
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate Cat sitting"""
        print(self.name.title() + " is sitting")

    def purr(self):
        """Simulate Cat purring"""
        print(self.name.title() + " is purring")

my_cat = Cat("kitty", 2)
print("My cat's name is '" + my_cat.name.title() + "' and its age is " + str(my_cat.age))
my_cat.sit()
my_cat.purr()

your_cat = Cat("smokey", 3)
print("\nYour cat's name is '" + your_cat.name.title() + "' and its age is " + str(your_cat.age))
your_cat.sit()
your_cat.purr()
