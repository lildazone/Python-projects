from math import *
def solve_it ():
    
    a=int(input('entre a value '))
    b=int(input('entre b value '))
    c=int(input('entre c value '))
    d= (b*b) - (4*a*c)

    if a > 0 : 
        
        print('Delta= ',d)
        if d<0 : print('this equation has no solution !')
        elif d==0: 
            x= -b/(2*a)
            print('this equation has one solution =', x)
        else: 
            x1= (-b-sqrt(d))/(2*a)
            x2= (-b+sqrt(d))/(2*a)
            print('this equation has two solution =', x1 ,'and ', x2)
            
    else: print('this is an equation of 1st degree')
solve_it()
print('Solve an other equation')
solve_it()