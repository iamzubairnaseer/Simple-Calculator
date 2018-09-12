#suppose quadratic equation
#ax**2+bx+c=0
def quadratic():
    a=float(input('a=coefficient of x**2= '))
    b=float(input('b=coefficient of x= '))
    c=float(input('c=constant value= '))
    #formula
    x1=(-b+((b**2)-(4*a*c))**(0.5))/(2*a)
    x2=(-b-((b**2)-(4*a*c))**(0.5))/(2*a)
    print('The roots of the quadratic equation are',x1,',' , x2)
    print("")
