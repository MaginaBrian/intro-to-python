class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks



class Course:
    def __init__(self,course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def course_average(self):
        count = 0
        for student in self.students:
            count += student.marks

        print(count / len(self.students) )

# creating student instances
s1 = Student("Brian",25,90)
s2 = Student("Sonia",24,94)
s3 = Student("Oliver",26,91)

# creaing course instances
c1 = Course("software development")

c1.add_student(s1)
c1.add_student(s2)
c1.add_student(s3)

for student in c1.students:
    print(student.name)
average = c1.course_average()
print(average)
