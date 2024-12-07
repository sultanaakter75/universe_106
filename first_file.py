
#for i in range (1,6):
 #   print (f'{i} - {i*i}')
a=input()
b=""
l= len(a)
for i in a:
    b[i] = a[l]
    l-=1
print(b)    
