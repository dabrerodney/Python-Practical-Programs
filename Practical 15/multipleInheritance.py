class Parent1:
    def method1(self):
        print("Method 1 from Parent 1")

class Parent2:
    def method2(self):
        print("Method 2 from Parent 2")

class Child(Parent1, Parent2):
    pass

# Example usage:
child = Child()
child.method1()
child.method2()
