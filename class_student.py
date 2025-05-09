class Student:
    count = 0
    student_list = []

    def __init__ (self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.get_count()

    # instance methods have self keyword
    def full_name(self): 
        # print(f'{self.first_name} {self.last_name}')
        # print(self.first_name +  " " + self.last_name)
        print("{} {}".format(self.first_name, self.last_name))

    # class methods have @classmethod property
    # cls => class

    @classmethod
    def get_count(cls):
        cls.count += 1
    

   
        


student_1 = Student("Evans", "Kennedy", 20)

# print(student_1.first_name)
# print(student_1.full_name())

student_2 = Student("Lavendar", "Chelsea", 19)
# print(student_2.first_name)

# print(Student.count)
# print(Student.student_list)

print(Student.count)


   