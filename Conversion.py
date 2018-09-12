def conv():
    print('Which conversion you want to use? ')
    print('1.Fahrenheit to Celsius ')
    print('2.Celsius to Fahrenheit ')
    print('3.Km/h to m/s ')
    print('4.m/s to km/h ')
    print("")

    select=int(input('Select any one option: '))
    print("")

    if select==1:
        x=float(input('Enter the temperature in fahrenheit: '))
        c=(x-32)*(5/9)
        print("The temperature in celsius is",c)
        print("")
        
    elif select==2:
        x=float(input('Enter the temperature in celcius:'))
        c=x*(9/5)+32
        print("The temperature in fahrenheit is",c)
        print("")

    elif select==3:
        n=float(input('Enter number: '))
        a=1000/3600
        k=n*a
        print(k)
        print("")

    elif select==4:
        n=float(input('Enter number: '))
        a=3600/1000
        k=n*a
        print(k)
        print("")
