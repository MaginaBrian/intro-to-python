class Cat:

    def __init__(self,name):
        self.name = name

    def speak (self):
        print(f"{self.name} meooow")


cat_1= Cat ("Garfield")
cat_1.speak()