def multi():
    count=int(input('How many number would you like to perform? '))
    l=[]
    for x in range(count):
        num=float(input('Enter number: '))
        l.append(num)
    mult=1
    for i in l:
        mult*=i
    Ans=mult
    print(Ans)
    while True:
        print("You want to multiply again in the previous answer?if yes type '1',if no type '2' ")
        select=int(input('Select option: '))
        if select==1:
            nume=float(input('Enter number: '))
            Ans=Ans*nume
            print(Ans)
        else:
            print("")
            break
