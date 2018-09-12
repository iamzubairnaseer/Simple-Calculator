def add():
    count=int(input('How many number would you like to perform? '))
    l=[]
    for x in range(count):
        num=float(input('Enter number: '))
        l.append(num)

    sum=0
    for i in l:
        sum+=i
    ans=sum
    print(ans)
    while True:
        print("You want to add again in the previous answer?if yes type '1',if no type '2' ")
        select=int(input('Select option: '))
        if select==1:
            nume=float(input('Enter number: '))
            ans=ans+nume
            print(ans)
        else:
            print("")
            break
