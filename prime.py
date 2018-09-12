def prime():
    num=int(input('Enter the number to be tested:'))
    List=[]
    for x in range(1,num+1):
        if num%x==0:
            List.append(x)
        else:
            continue
    if len(List)==2:
        print(num,'is prime number.')
    else:
        print(num,'is not prime number.')
    print('')
