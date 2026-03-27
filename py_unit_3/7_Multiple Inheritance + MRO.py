class A:
    def show(self):
        print("Class A")

class B:
    def display(self):
        print("Class B")

class C(A, B):
    def printmsg(self):
        print("Class C")

obj = C()

obj.show()
obj.display()
obj.printmsg()

print("\nMRO:", C.mro())
