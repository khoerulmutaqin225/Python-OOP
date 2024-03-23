# method resolution order // multiple inheritance

class A:
    
    def show(self):
        print("ini adalah show A")
        
class B:
    def show(self):
        print("ini adalah show B")
        
# methode di urutkan dari C ke B baru ke A
class C(B,A):
    pass

objeck = C()
objeck.show()
help(objeck)
