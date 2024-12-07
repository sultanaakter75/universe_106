a=[]
b={}
def myfunc():
    
    print('\n')
    print('---------press 1, for data input-----------')
    print('---------press 0, for end of input---------')
    t=input()
    if t=='0':
        return
    elif t=='1': 
        name= input('Name: ')
        a.append(name)
        b.update({'NAME': name})
        roll=input('Roll :')
        b.update({'ROLL': roll})
        a.append(roll)
        sub=input('Subject :')
        b.update({'SUBJECT': sub})
        a.append(sub)
        myfunc()
    else:
        print ('Invalid Choice')  
        myfunc()  

myfunc()
print('All item shown in a list : \n',a)
print('All item shown in a dictionary : \n',b)

print('\n')


