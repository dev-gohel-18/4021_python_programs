class Student:

    def AddStudent(self):
        self.roll = int(input("Enter Roll No: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.gender = input("Enter Gender: ")

    def DisplayStudent(self):
        print("\nStudent Details")
        print("Roll No:", self.roll)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)

s = Student()

s.AddStudent()
s.DisplayStudent()
