class Dog:
    def __init__(self, name="Unknown", age=0):  
        self.name = name
        self.age = age
    
    def bark(self):  
        print("woooooof")


dog_1 = Dog("Terry", 20)  
dog_2 = Dog("John", 5)


dog_1.bark()  
dog_2.bark()  