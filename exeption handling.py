'''exeption handling by using     try and   except'''

# print('my name is veeresh')
# try:
#  print(10/0)
# except:ZeroDivisionError
# print(10//2)
# try: 
#  print('a'+4)
# except:TypeError
# print(4+4)  
'''using one try block and two except blocks'''
# try: 
#   x=int(input('enter f number:'))
#   y=int(input('enter s number:')) 
#   print(x/y)
# except ZeroDivisionError:
#     print('yes this is zero division error')
# except ValueError:
#     print('yes this is value error') 
# try:
#   print('stmt 1') 
#   print('stmt 2') 
#   print('stmt 3') 
#   print(10/0)
# except ZeroDivisionError:
#     print('hi hi') 
#     print(20+9) 
# print(100//4)

# try:
#     print('this is try block')
#     x=10
#     y=2
#     print(x/y)
# except:
#     print('this is except block')
#     print('this is anothe except block') 
# else:
#     print('this is else block ') 
# finally:
#     print('this is finslly block')     
# try:
#     print('this is try block')
#     x=10
#     y=0
#     print(x/y)
# except ZeroDivisionError:
#     print('this is except block')
#     print('this is anothe except block') 
# else:
#     print('this is else block ') 
# finally:
#     print('this is finslly block')      
'''try block inside another try block''' 
# try:
#     print('this is my first try') 
#     print('this is my second try')
#     x=10
#     y='hi'
#     print(x+y)    
#     try:
#       print('inner try block')
#       a=10
#       b=0
#       print(a/b)
#     except ZeroDivisionError: 
#       print('this is not correct block') 
# except TypeError:
#     print('yes this is correcy') 
# else:
#     print('this is else block') 
# finally:
#     print('my work is done') 
# l=[1,2,3,4]   
# l.reverse()
# print(l)
# a=[2,4,7,8,90,2,1,3]
# a.sort()
# print(a)
# from random import*
# for i in range(20):
#   print(randint(0,1))
# from random import*
# a=['va','vi','hi','bye']
# print(choice(a))

# try:
#   x=10
#   y=0
#   print(x+y)
#   for i in range(1,10):
#       print(i,end=' ')
# except ZeroDivisionError:
#     print('this is new statement')
#     x=10
#     y=2
#     print(x/y)
# else: 
#     print('the statement is declared')  
# finally:
#     for i in range(1,20,2):
#         print(i,end=' ')
#     print('this processe is complete')  

# f=open('aaa.txt','w')
# print('file name',f.name)
# print('file mode',f.mode)
# print(f.readable())
# print(f.writable())
# print(f.closed)

   

        


