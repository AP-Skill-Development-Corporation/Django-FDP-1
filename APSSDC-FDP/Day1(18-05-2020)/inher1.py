class A:
    a,b=10,20
    def msg():
        print('i am from class A')

class B(A):
    c,d=20,30
    def msg1():
        print('i am from class B')

obj = B
print(obj.c,obj.a)
obj.msg1()
obj.msg()
