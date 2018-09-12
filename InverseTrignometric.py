def intrig():
    print('Which inverse trignometric function you want to use?:')
    trig=input('a)sinx\t\tb)cosx\t\tc)tanx\nd)cosecx\te)secx\t\tf)cotx\n')
    angle=float(input('Enter the number:'))

    if trig=='a':
        y=angle
        ans_sinx=y+(y**3/(3*2*1))+((3)*y**5/(5*4*2*1))+((3*5)*y**7/(7*6*4*2*1))+((3*5*7)*y**9/(9*8*6*4*2*1))
        sinx=ans_sinx*(180/3.141592654)
        print(sinx)
        print('')
    elif trig=='b':
        y=angle
        ans_cosx=(3.141592654/2)-(y+(y**3/(3*2*1))+((3)*y**5/(5*4*2*1))+((3*5)*y**7/(7*6*4*2*1))+((3*5*7)*y**9/(9*8*6*4*2*1)))
        cosx=ans_cosx*(180/3.141592654)
        print(cosx)
        print('')
    elif trig=='c':
        if angle>-1 and angle<1:
            y=angle
            ans_tanx=y-(y**3/(3))+(y**5/(5))-(y**7/(7))+(y**9/(9))
            tanx=ans_tanx*(180/3.141592654)
            print(tanx)
            print('')
        elif angle>=1:
            y=1/angle
            ans_tanx=(3.141592654/2)-y+(y**3/(3))-(y**5/(5))+(y**7/(7))-(y**9/(9))
            tanx=ans_tanx*(180/3.141592654)
            print(tanx)
            print('')
        elif angle<=1:
            y=1/angle
            ans_tanx=-(3.141592654/2)-y+(y**3/(3))-(y**5/(5))+(y**7/(7))-(y**9/(9))
            tanx=ans_tanx*(180/3.141592654)
            print(tanx)
            print('')
        else:
            print('Math Error')
            print('')
    elif trig=='d':
        if angle>1:
            y=1/angle
            ans_cscx=y+(y**3/(3*2*1))+((3)*y**5/(5*4*2*1))+((3*5)*y**7/(7*6*4*2*1))+((3*5*7)*y**9/(9*8*6*4*2*1))
            cscx=ans_cscx*(180/3.141592654)
            print(cscx)
            print('')
        else:
            print('Math Error')
            print('')
    elif trig=='e':
        if angle>1:
            y=1/angle
            ans_secx=(3.141592654/2)-(y+(y**3/(3*2*1))+((3)*y**5/(5*4*2*1))+((3*5)*y**7/(7*6*4*2*1))+((3*5*7)*y**9/(9*8*6*4*2*1)))
            secx=ans_secx*(180/3.141592654)
            print(secx)
            print('')
        else:
            print("Math Error")
            print('')
    elif trig=='f':
        if angle>-1 and angle<1:
            y=angle
            ans_tanx=y-(y**3/(3))+(y**5/(5))-(y**7/(7))+(y**9/(9))
            tanx=ans_tanx*(180/3.141592654)
            cotx=(3.141592654/2)-tanx
            print(cotx)
            print('')
        elif angle>=1:
            y=1/angle
            ans_tanx=(3.141592654/2)-y+(y**3/(3))-(y**5/(5))+(y**7/(7))-(y**9/(9))
            tanx=ans_tanx*(180/3.141592654)
            cotx=(3.141592654/2)-tanx
            print(cotx)
            print('')
        elif angle<=1:
            y=1/angle
            ans_tanx=-(3.141592654/2)-y+(y**3/(3))-(y**5/(5))+(y**7/(7))-(y**9/(9))
            tanx=ans_tanx*(180/3.141592654)
            cotx=(3.141592654/2)-tanx
            print(cotx)
            print('')
        else:
            print('Math Error')
            print('')
