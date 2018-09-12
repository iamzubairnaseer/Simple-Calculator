def comb():
    n=int(input('Enter nth value: '))
    r=int(input('Enter rth value: '))
    num=n-r
    if num<0 or r<0:
        print('Math Error')
        print("")
    else:
        factorial=1
        for i in range(1,num+1):
            factorial=factorial*i
        a=factorial
       
        nfactorial=1
        for i in range(1,n+1):
            nfactorial=nfactorial*i
        b=nfactorial

        rfactorial=1
        for i in range(1,r+1):
            rfactorial=rfactorial*i
        c=rfactorial
        Ans=b/(c*a)
        print(n,'C',r,' = ',Ans,sep='')
        print("")
