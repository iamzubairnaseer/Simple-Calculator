def hyper():
    print('Which Hyperbolic function you want to use?:')
    trig=input('a)sinhx\t\tb)coshx\t\tc)tanhx\n')
    angle=int(input('Enter the angle:'))
    e=2.718281828459045
    sinhx=((e**angle)-(e**(-angle)))/2
    coshx=((e**angle)+(e**(-angle)))/2
    if trig=='a':
        print(sinhx)
        print('')
    elif trig=='b':
        print(coshx)
        print('')
    elif trig=='c':
        tanhx=sinhx/coshx
        print(tanhx)
        print('')
