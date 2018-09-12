def trig():
    print('Which trignometric function you want to use?:')
    trig=input('a)sinx\t\tb)cosx\t\tc)tanx\nd)cosecx\te)secx\t\tf)cotx\n')
    angle=int(input('Enter the angle in degrees:'))
    y=angle*((3.141592654)/180)
    sinx=y-(y**3/(3*2*1))+(y**5/(5*4*3*2*1))-(y**7/(7*6*5*4*3*2*1))+(y**9/(9*8*7*6*5*4*3*2*1))
    cosx=1-(y**2/(2*1))+(y**4/(4*3*2*1))-(y**6/(6*5*4*3*2*1))
    if trig=='a':
        print('Your ans in degrees is=',sinx)
        print('')
    elif trig=='b':
        print('Your ans in degrees is=',cosx)
        print('')
    elif trig=='c':
        if angle==90 or angle==-90:
            print('Math Error')
            print('')
        else:
            tanx=sinx/cosx
            print('Your ans in degrees is=',tanx)
            print('')
    elif trig=='d':
        cosecx=1/sinx
        print('Your ans in degrees is=',cosecx)
        print('')
    elif trig=='e':
        secx=1/cosx
        print('Your ans in degrees is=',secx)
        print('')
    elif trig=='f':
        cotx=cosx/sinx
        print('Your ans in degrees is=',cotx)
        print('')
