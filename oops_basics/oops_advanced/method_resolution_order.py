# ---------------------------------------------------------
# Program: Method Resolution Order (MRO)
# Description:
# This program shows how Python decides which method to call
# in multiple inheritance.
# ---------------------------------------------------------

class A:
    def show(self):
        print("Method from class A")


class B(A):
    def show(self):
        print("Method from class B")


class C(A):
    def show(self):
        print("Method from class C")


class D(B, C):
    pass


obj = D()
obj.show()

print("MRO of class D:")
for cls in D.__mro__:
    print(cls.__name__)
