
'''method overloading'''
# class test:
#     def m1(self):
#         print('zero arg')
#     def m1(self,a):
#         print('one argument')
#     def m1(self,a,b): 
#         print('two argumentts')
# t=test()
# t.m1()    only last method executed ,and 0 arguments are passed os this is a type error
# t.m1(10)   only last method excecuted ,and only  one argument passed so,this is also type error
# t.m1(12,22)    valid,becuase of last method excecute and passign the two arguments

# class person:
#     def n1(self,a):
#         print('one arg passed')
#     def n1(self): 
#         print('yes this is correct')   
# p=person()
# p.n1()       
'''constructor overloading'''
# class Test:
#     def __init__(self):
#         print('only zero constructor method')
#     def __init__(self,a):
#         print('three constructor methods')
#     def __init__(self,a,b):
#         print('two constructor methods')
# thi=Test(10,20)   

# class variable:
#     def __init__(self): 
#         print('0 constructor method')  
#     def __init__(self,a,b,c): 
#         print('three constructor methods')
#     def __init__(self,a,b):
#         print('two constructor methos')
# v=variable(2,0)
'''method overriding'''
# class p:
#     def m1(self):
#         print('my nme is veeresh')
#     def m2(self):
#         print('what is your name')  
# class c(p):
#     def m2(self):
#         super().m2()
#         print('ok thats it')
# av=c()
# av.m1()
# av.m2()

# class hi:
#     def m(self):
#         print('this is method of m')
#     def m1(self):
#         print('this is method of m1') 
# class bye(hi):
#     def m1(self):
#         super().m1()
#         print('this is child m1 method')
# haa=bye()
# haa.m()
# haa.m1()       

'''contructor overriding'''
# class parent:
#     def __init__(self):  
#         print('the first constructor') 
# class child(parent): 
#     def __inti__(self):
#         super().__init__()   
#         print('this is child class constuctor')
# ac=child() 

# class p:
#     def __init__(self): 
#               print('parent cons') 
# class c(p):
#     def __init__(self): 
#         super().__init__() 
#         print('child cons') 
# a=c()                                
  
# class p:
#     def __init__(self):  
#         print('this is constructor method')  
# class c(p): 
#     def __init__(self):
#         super().__init__()  
#         print('this is child constructor method') 
# av=c()   
            
# class test:
#     def m1(self,a):
#         print('this is the m1 methd of overloading')
#     def m1(self,a):  
#         print('this is m2 method of overloding')  
#     def m1(self,a,b):
#         print('this si m3 method of overloading') 
#         print(a+b)
# t=test()
# t.m1(20,10)

# class test:
#     def __init__(self,a,b):
#         print('this is the first constructor of the overloading')
#     def __init__(self,a):
#         print('this si second constructor off the overloading')
#     def __init__(self,a,b,c):
#         print('this is the third constructor of the overloading')
#         print(a*b*c) 
# t=test(10,2,3)
# f1=open('mytxt','w')
# f1.write('hello students ho are you') 
# f1.write('i amveeresh,and i am currently staying in hydrabad')
# print(f1)
# f1.close()
# f2=open('mytxt','r') 
# f=f2.read(10)
# print(f)
     
       

      
          
           
              