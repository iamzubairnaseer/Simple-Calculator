def inhyper():
    print('Which inverse hyperbolic function you want to use?:')
    trig=input('a)sinhx\t\tb)coshx\t\tc)tanhx\n')
    y=float(input('Enter the number:'))
    n=1000.0
    if trig=='a':
        x=(y+((y**2)+1)**0.5)
        print(n * ((x**(1/n))-1))
        print('')
    elif trig=='b':
        x=(y+((y**2)-1)**0.5)
        print(n * ((x**(1/n))-1))
        print('')
    elif trig=='c':
        x=((1-y)/(1+y))
        print(0.5*(n * ((x**(1/n))-1)))
        print('')
