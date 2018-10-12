print("Begin")
i=input('Enter fno:')
j=input('Enter sno:')
try:
    x=int(i)
    y=int(j)
    z=x/y
    print(z)
except:
    print('Erroor occured')
except(ZeroDivisionError):
    print('This no can not be Zero')
except(ValueError):
    print('Enter numerical value only')
print('End')



#OUTPUT
#Defaul except must be last
