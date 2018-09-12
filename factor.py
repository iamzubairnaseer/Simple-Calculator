def factr():
    num=int(input('Enter the number you want factor list:'))
    List=[]
    for x in range(1,num+1):
        if num%x==0:
            List.append(x)
    print(List,'\n')
