def sub():
    count=int(input('How many number would you like to perform? '))
    l=[]
    for x in range(count):
        num=float(input('Enter number: '))
        l.append(num)
    a=l[0]
    for i in l[1:]:
        a-=i    
    Ans=a
    print(Ans)
    while True:
        print("You want to subtract again in the previous answer?if yes type '1',if no type '2' ")
        select=int(input('Select option: '))
        if select==1:
            nume=float(input('Enter number: '))
            Ans=Ans-nume
            print(Ans)
        else:
            print("")
            break

