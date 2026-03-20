class Outer:
    def __init__(self, name):
        self.name = name
        self.inner = self.Inner()  

    def show_outer(self):
        print("Outer class name:", self.name)

    class Inner:
        def __init__(self):
            self.value = 100

        def show_inner(self):
            print("Inner class value:", self.value)


obj = Outer("Python")

obj.show_outer()

obj.inner.show_inner()
