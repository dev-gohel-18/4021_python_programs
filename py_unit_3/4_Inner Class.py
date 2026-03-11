class Outer:

    def __init__(self):
        print("Outer class object created")

    class Inner:
        def show(self):
            print("This is Inner Class Method")

o = Outer()

i = o.Inner()
i.show()
