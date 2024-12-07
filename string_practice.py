c = input("Enter 1st Spring ")
#print (f'1st = {a}')
#b = input('Enter 2nd string ')
#print (f'2nd = {b}')
#c = (a+" " +b)
#print (f'{a} + {b} = {c}')
# print (c.upper())
# print (c.title())
# print (c.capitalize())
# print (len(c))
#print (c.count('m'))
# print (c.strip('-'))
# print (c[0:6])
# print (c[0:])
# print (c[-len(c):])
# print (c[-1:])
# print (c.index(' '))
# print (c.find(' '))
# print (c.replace(' ',','))
   
#c=c.lower()
#s = c.split()[::-1]
#for i in s:
#    print(i, end=' ')


#m=0 
#m = m + c.count('a')
#m = m + c.count('e')
#m = m + c.count('i')
#m = m + c.count('o')
#m = m + c.count('u')
#print (m)
# mid = len(c)//2
# if c[:mid]==c[mid:]:
#    print('The entered string is symmetrical')
# elif c[:mid]==c[mid+1:]:
#    print ('The entered string is symmetrical')
# else :
#    print('The entered string is not symmetrical')   

# d = c[::-1]
# if c==d :
#    print('The entered string is palindrome')
# else :
#    print('The entered string is not palindrome')

#s=c.split()
#for i in s:
#    if (len(i)%2==0) :
#        print (i, end=' ')
# len=len(c)//2
# print (c[:len], end='')
# print(c[len::].upper())
digit=0
letter=0
for i in c:
    if i.isdigit():
        digit=1
    elif i.isalpha():
        letter=1
if letter==1 and digit==1:
    print('yes')   
else :
    print('no')     
#print('yes' if letter==1 and digit==1 else 'no')