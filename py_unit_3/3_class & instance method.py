class Example:

    school = "ABC School"

    def show(self):
        print("This is Instance Method")

    @classmethod
    def display(cls):
        print("This is Class Method")
        print("School:", cls.school)

obj = Example()

obj.show()
Example.display()
