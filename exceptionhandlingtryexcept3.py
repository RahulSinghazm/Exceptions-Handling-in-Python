print("Begin")
i=input('Enter fno:')
j=input('Enter sno:')
x=int(i)
y=int(j)
try:
    z=x/y
    print(z)
except(ZeroDivisionError):
    print('This no can not be Zero')
print('End')
