def power():
    print("Welcome to the power department!")
    print("")
    nums=float(input('enter the number: '))
    power=float(input('enter the power: '))
    if nums==power==0:
        print('Math Error')
        print("")
    elif nums==0 and power<0:
        print('Math Error')
        print("")
    else:
        print(nums**power)
        print("")
