import math as m                   #math module is imported
def add(num1,num2):                         # defining function to add two no's.  
    sum=num1+num2
    print("sum= ",sum) 
def sub(num1,num2):                        #defining function to subtract two no's.
    sub=num1-num2
    print("difference= ",sub)
def mult(num1,num2):                      #defining function to multiply two no's.
    product=num1*num2
    print("product= ",product)
def div(num1,num2):                       # defining function to diviide two no's.
    divison=num1/num2
    print("divison= ",divison)
def mod(num1,num2):                       #defining function to find remainder of two no's
    mod=num1%num2
    print("remainder= ",mod)
def sqrt(num):
    sqrt=m.sqrt(num)                      #defining function to find the square root of a no.
    print("square root= ",sqrt)
def pow(base,power):                       #defining function to find the  power .
    power=m.pow(base,power)
    print("power= ",power)
def sin(radian):                     # defining function to find the value of sine.  
    sine=m.sin(radian)
    print("value of sine function= ",sine)
def cos(radian):                      #defining function to find the value of cosine.
    cosine=m.cos(radian)
    print("value of cosine function= ",cosine)
def tan(radian):                      #defining function to find the value of tangent.  
   tangent=m.tan(radian)
   print("value of tangent function= ",tangent)
def degrees(radian):                 #defining function to convert the radians to degrees.
    degrees=m.degrees(radian)
    print("degrees= ",degrees)
def rn(degree):                  #defining function to convert the degrees to radians.   
    radian=m.radians(degree)
    print("radian= ",radian)
while True:                     
    print("1) addition    2) subtraction        3) multiplication") 
    print("4) divison     5) mod(remainder)     6) square root  ")
    print("7) power       8) sin()              9) cos() ")
    print("10) tan()      11) radian to degrees 12) degrees to radians") 
    choice=int(input("choose the operation from 1 to 12:  "))             # entering the choice of user.
    if choice==1 or choice==2 or choice==3  or choice==4 or choice==5:
        num1=float(input("num1: "))                                       
        num2=float(input("num2: "))
        if choice==1:
            add(num1,num2)
        elif choice==2:
            sub(num1,num2)
        elif choice==3:
            mult(num1,num2)
        elif choice==4:
            div(num1,num2)
        elif choice==5:
            mod(num1,num2) 
    elif choice==6:
        num=float(input("num: "))
        sqrt(num)
    elif choice==7:
        base=float(input("base: "))
        power=float(input("power:"))
        pow(base,power)
    elif choice==8 or choice==9 or choice==10 or choice==11:
        radian=float(input("radian: "))
        if choice==8:
            sin(radian)
        elif choice==9:
            cos(radian)
        elif choice==10:
            tan(radian)
        elif choice==11:
            degrees(radian)
    elif choice==12:
        degree=float(input("degrees: "))
        rn(degree)        
    else:
        print(".................wrong choice..............") 
    cont_=input("Do you want to do more operations?(y/n) --  ")    
    if cont_=="y" or cont_=="Y":
        continue                              # use of continue statement to do more operations.
    else:
        print("...E..X..I..T...")
        break                                 #use of break statements to close the loop.
                                   
                                   