class Student:

    def getStudent(self):
        self.roll = input("Enter Roll No: ")
        self.name = input("Enter Name: ")
        self.gender = input("Enter Gender: ")
        self.age = input("Enter Age: ")

class Course(Student):

    def getCourse(self):
        self.course = input("Enter Course Name: ")
        self.duration = input("Enter Duration: ")
        self.fee = input("Enter Fee: ")

    def display(self):
        print("\nStudent Details")
        print(self.roll, self.name, self.gender, self.age)
        print("Course:", self.course)
        print("Duration:", self.duration)
        print("Fee:", self.fee)

obj = Course()

obj.getStudent()
obj.getCourse()
obj.display()
