print('\t\t\tWELCOME TO CALCULATOR')
print("")
while True:
#=============================================================================================
    print("""You have 23 options.They are listed below:
1.Addition  2.Subtraction  3.Multiplication  4.Division  5.Quadratic Equation
6.Factorial  7.Nth Power  8.Square   9.Cube   10.Square root   11.Cube root
12.Combination   13.Permutation   14.Trigonometric   15.Inverse Function
16.Inverse Trignometric  17.Exponential  18.Logarithm  19.Nth Root
20.Hyperbolic Function   21.Inverse Hyperbolic Function  22.conversion
23.FactorList   24.Prime(Test)""")
    print("")
    menu_choice=float(input('Please choose an option: '))
    print("")
#=============================================================================================
    if menu_choice==1:
        from ADD import add
        add()
#=============================================================================================
    elif menu_choice==2:
        from SUB import sub
        sub()
#=============================================================================================
    elif menu_choice==3:
        from MULT import multi
        multi()
#=============================================================================================
    elif menu_choice==4:
        from DIVI import div
        div()
#=============================================================================================
    elif menu_choice==5:
        from Quadratic import quadratic
        quadratic()
#=============================================================================================
    elif menu_choice==6:
        from Factorial import factorial
        factorial()
#=============================================================================================
    elif menu_choice==7:
        from Power import power
        power()
#=============================================================================================
    elif menu_choice==8:
        from Square import Square
        Square()
#=============================================================================================
    elif menu_choice==9:
        from Cube import cube
        cube()
#=============================================================================================
    elif menu_choice==10:
        from Square_root import square_root
        square_root()
#=============================================================================================
    elif menu_choice==11:
        from Cuberoot import cuber
        cuber()
#=============================================================================================
    elif menu_choice==12:
        from Combination import comb
        comb()
#=============================================================================================
    elif menu_choice==13:
        from Permutation import perm
        perm()
#=============================================================================================
    elif menu_choice==14:
        from Trignometric import trig
        trig()
#=============================================================================================
    elif menu_choice==15:
        from InverseFunction import rev
        rev()
#=============================================================================================
    elif menu_choice==16:
        from InverseTrignometric import intrig
        intrig()
#=============================================================================================
    elif menu_choice==17:
        from Exponential import exp
        exp()
#=============================================================================================
    elif menu_choice==18:
        from Logarithm import log
        log()
#=============================================================================================
    elif menu_choice==19:
        from nthroot import nthr
        nthr()
#=============================================================================================
    elif menu_choice==20:
        from hyperf import hyper
        hyper()
#=============================================================================================
    elif menu_choice==21:
        from inhyperf import inhyper
        inhyper()
#=============================================================================================
    elif menu_choice==22:
        from Conversion import conv
        conv()
#=============================================================================================
    elif menu_choice==23:
        from factor import factr
        factr()
#===============================================================================
    elif menu_choice==24:
        from prime import prime
        prime()
#===================================================================================
    else:
        print('Please! See Options Agian.')
        print('')
