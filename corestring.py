'''
upper()
lower()
endswith()
startswith()
replace()
count()
index()
find()
removeprefix()
removesufix()
strip()
lstrip()
rstrip()
split()
'''
# a="python life"
# print(a.upper())
# a="PYTHON LIFE"
# print(a.lower())
# a='hi nanna'
# print(a.endswith('hi'))
# a="popular singer"
# print(a.startswith("popular"))
# print(a.replace("popular","youtube"))
# print(a.find("popular"))
# a='12346789'
# print(a[0:8])

'''string slicing'''
# a='123406789'
# print(a[1:8])

s='0123446789'
# print(s[2:8:1])
# print(s[2:8:-1])
# print(s[-1:-6:-1])
# print(s[2:-4:1])
# print(s[:0:-1])

'''w a p to access each character of string in forard direction and back ward direction by using while loop?'''
# s=input('enter somme string:')
# n=len(s)
# i=0
# print('forward direction:')
# while i<n:
#     print(s[i],end="")
#     i+=1
    
# s='sunnyi'
# i=0
# while i<6:
#     print(s[i],end="")
#     i+=1

# s='sunnyi'
# n=len(s)
# i=n-1
# print('backord direction')
# while i>=-n:
#     print(s[i],end="")
#     i-=1
# '''cheking membership'''
# s=input('enter the first string')
# s2=input('enter the second string')
# if s2 in s:
#     print('first string is found')
# else:
#     print('first string is not found')    
# a=(1,2,3,4,'veeresh','ramu','sita')
# b=(1,2,3,'sita,','rahul','satay')
# if 7 in a and b:
#     print('yes the number is in the a')
# else:
#     print('sorryboss the number is no there')
# '''coparing in string'''   
# s=input('enter the f value:')
# s1=input('enter the sec value:') 
# if s==s1:
#     print('yes correct')
# else:
#     print('no wrong')    
# l1=['a','g','d']  
# l2=['a','g','d'] 
# l3=l2
# print(l1 is l2)  false,becouse l1 and l2 id is change
# print(l3 is l2)   true,becouse l2=l3 is same,so id also same
# print(l1==l2)        true,l1==l2 values are same  
                 
                 
'''finding sub strings
forward direction(left to right)
*find()
*index()
backard direction(right to left)
*rfind()
*rindrx

'''       
a='my name is veeresh'  
# print(a.find('i'))              
# print(a.find('e'))                 
# print(a.index('e'))               
# print(a.index('e'))                 
# print(a.rfind('e'))               
# print(a.rindex('v'))                  
# print(a.find('y'))                 
# print(a.index('d'))
# print(a.find('e',7,20))                 
# print(a.index('e',13,19))     

# for i in range(10,30):
#     if i==24:
#         break
#     print(i)
# a=[1,2,3,4,6,7,8]
# for i in a:
#     if i==6:
#         break
#     print(i)
    
'''changing case  of a string'''
a='veeresh is good boy'
# print(a.replace('veeresh','suresh'))
# print(a.replace('good','most powerful'))        
# print(a.split()) 
# a='the new crush boy'
# b=a.split()       
# for i in b:
#     print(i)
# c='veeresh is a good person'
# b=c.split()
# for i in b:   
#    print(i)
# s='this is one of the best ' 
# print(s.upper()) 
# s='THIS IS my Book please give Me'
# print(s.swapcase()) 
# a='veersh is my best friend'
# print(a.capitalize())  Veeresh is my best friend
# a='veeresh rara babu'  
# print(a.title())      Veeresh Rara Babu
# a='veera raara swamy' 
# print(a.startswith('veera'))  
# print(a.endswith('swamy'))
'''joining of string---- syntsx ' '.join()
'''
# a=('sita','rama','raju')
# # print(''.join(a))
# print(':'.join(a))
# amar=('hi nanna','ravana','12amaran')
# print(' '.join(amar))
'''print a odd numbers and even numbers'''
# a=input('enter the some string:')
# print('this is even position:',a[0::2])
# print('this is odd position:',a[1::2])
a='my name is veeresh'
print(a[::-1])
# for i in reversed(a):
#     print(i,end=''y) 