# class animal:
#    def __init__(self,name):
#       self.name=name
#    def speak(self):   
#       print('this is my dog')
# class dog(animal): 
#    def __init__(self,name,eat): 
#       super().__init__(name)
#       self.eat=eat 
#    def speak(self):
#       super().speak()
#       print('ok its good') 
# d=dog('veeresh','biryani')
# print(d.name)
# print(d.eat) 
# # d.speak()  
# class test:
#    def __init__(self,name,age,marks):
#       self.name=name
#       self.age=age
#       self.marks=marks
#    def display(self):
#       print(self.name,self.age,self.marks)
#       print('hi',self.name,'this is your information')  
# class total(test):
#    def __init__(self,name,age,marks,per,grade):
#       super().__init__(name,age,marks) 
#       self.per=per
#       self.grade=grade
#    def display(self): 
#       super().display()
#       print(self.per)      
#       print(self.grade)
# t=total('veeresh',21,99.99,'100','a+')  
# t.display()
# class test:
#    def m1(self):
#       print('this is my first method')
#       print('ok bye')
#    def m2(self):
#       print('this is my second method') 
#       print('ok bye')
# class total(test):
#    def __init__(self,name,age): 
#       self.name=name  
#       self.age=age  
#    def display(self):
#       super().m1()
#       super().m2()
#       print(self.name)
#       print(self.age) 
# t=total('veeresh',99) 
# t.display()     
      
import numpy as np
lst=[1,2,3,4,6,7]   
a=np.array(lst)

print(type(a)) 
print(a)


    
    
    
    
    
    
    
    
    
    
    