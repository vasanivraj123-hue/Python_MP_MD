class Student:
    def student_info(self):
        print("This is Student class")


class Course:
    def course_info(self):
        print("This is Course class")


class Marks:
    def marks_info(self):
        print("This is Marks class")


class Result(Student, Course, Marks):
    def result_info(self):
        print("This is Result class (Derived)")


obj = Result()

obj.student_info()
obj.course_info()
obj.marks_info()
obj.result_info()

print("\nMethod Resolution Order (MRO):")
for cls in Result.__mro__:
    print(cls)
