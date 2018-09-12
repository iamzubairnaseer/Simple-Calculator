def factorial():
    num=int(input('Enter number: '))
    factorial=1
    if num<0:
        print('Math Error\nNumber must be +ve')
        print("")
    elif num==0:
        print('The factorial of 0 is 1')
        print("")
    else:
        for i in range(1,num+1):
            factorial=factorial*i
        print('the factorial of',num,'is',factorial)
        print("")
