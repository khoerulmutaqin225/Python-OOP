class A:
    
    def methode_A(self):
        print("ini adalah method A")
        
class B:
    def method_B(self):
        print("ini adalah method B")
        
class C(A,B):
    pass

objeck = C()
objeck.methode_A()

objeck = C()
objeck.method_B()