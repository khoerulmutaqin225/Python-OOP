# method resolution order // multiple inheritance

class A:
    
    def show(self):
        print("ini adalah show A")
        
class B(A):
    pass
        
class C(A):
    
    pass


class D(B,C):
    pass


objek = D()
objek.show()
help(objek)
