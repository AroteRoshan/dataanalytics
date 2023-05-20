class A:
    a=56
    def __init__(self):
       print("class A run")

    def fun1(self):
       print("class A function fun1 run")

class B(A):   
    b=96
    def __init__(self):
       print("constuctor of class B")

    def fun2(self):
       print("Class B function")

class c(B):   

    def __init__(self):
       print("constuctor of class c")

    def fun3(self):
       print("Class c function")  

class D(B):   

    def __init__(self):
       print("constuctor of class D")

    def fun4(self):
       print("Class D function")       

obj = A()
obj.fun1()
obj1 = B()
obj1.fun2()
obj3=c() 
obj3.fun3()
obj4=D()
obj4.fun4()
print(obj4.b)
print(obj3.a)