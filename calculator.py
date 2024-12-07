print ('\nSIMPLE ARITHMATIC CALCULATION\n')
# p=0
# while p==0:
#     print ("Press '+' for addition")
#     print ("Press '-' for Subtruction")
#     print ("Press '*' fo Multiplication")
#     print ("Press '/' for Division")
#     print ('Press E for exit')
#     c = input()
    
#     if c == '+' :
#         a = int(input("enter 1st no : "))
#         b = int(input("enter 2nd no : "))
#         print (f'\n   result : {a} + {b} = {a+b}\n\n')
#     elif c == '-' :
#         a = int(input("enter 1st no : "))
#         b = int(input("enter 2nd no : "))
#         print (f'\n   result : {a} - {b} = {a-b}\n\n')  
#     elif  c == '*' :
#         a = int(input("enter 1st no : "))
#         b = int(input("enter 2nd no : "))
#         print (f'\n   result : {a} * {b} = {a*b}\n\n')   
#     elif c == '/' :
#         a = int(input("enter 1st no : "))
#         b = int(input("enter 2nd no : "))
#         print (f'\n   result : {a} / {b} = {a/b}\n\n')  
#     elif c == "E" or c == 'e' :  
#         break
#     else: 
#         print('Invalid Operator\n')

def operator():
    print ("Press '+' for addition")
    print ("Press '-' for Subtruction")
    print ("Press '*' fo Multiplication")
    print ("Press '/' for Division")
    print ('Press E for exit')
    c = input()
    return c

def jog(a, b):
    print (f'\n   result : {a} + {b} = {a+b}\n\n')

def biyog(a, b):
    print (f'\n   result : {a} - {b} = {a-b}\n\n')  

def goon(a, b):
    print (f'\n   result : {a} * {b} = {a*b}\n\n')  

def vag(a, b):
     print (f'\n   result : {a} / {b} = {a/b}\n\n')   

p=0

while p==0:
    c = operator() 
    
    if c=='+':
        x = int(input("enter 1st no : "))
        y = int(input("enter 2nd no : "))
        jog(x,y)
    elif  c=='-':
        x = int(input("enter 1st no : "))
        y = int(input("enter 2nd no : "))
        biyog(x,y)
    elif  c=='*':
        x = int(input("enter 1st no : "))
        y = int(input("enter 2nd no : "))
        goon(x,y) 
    elif  c=='/':
        x = int(input("enter 1st no : "))
        y = int(input("enter 2nd no : "))
        vag(x,y)   
    elif c == "E" or c == 'e' :  
        print ('***** THANK YOU *****\n')
        break
    else: 
        print('Invalid Operator\n')     