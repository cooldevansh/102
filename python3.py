number1=input("enter digit number 1 :")
operation=input("enter operation / * + - :")
number2=input("enter digit number 2 :")
total=0
if operation=="/":
    total=int(number1)/int(number2)
    print(number1,"/",number2,"=", total)
if operation=="*":
    total=int(number1)*int(number2)
    print(number1,"*",number2,"=", total)
if operation=="+":
    total=int(number1)+int(number2)
    print(number1,"+",number2,"=", total)
if operation=="-":
    total=int(number1)-int(number2)
    print(number1,"-",number2,"=", total)