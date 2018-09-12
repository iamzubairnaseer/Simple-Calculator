def cuber():
    print("Welcome to the cube root department!")
    print("")
    num=float(input('Enter number: '))
    if num<0:
        a=(-1)*num
        print('-',a**(1/3))
        print("")
    else:
        print(num**(1/3))
        print("")
