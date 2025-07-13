run =True
while run:
    def add(num1,num2):
        return num1+num2
    def sub(num1,num2):
        return num1-num2
    def multiply(num1,num2):
        return num1*num2
    def divide(num1,num2):
        return num1/num2
    
    dict={"+":add,"-":sub,"*":multiply,"/":divide}
     
    num1 = int(input("enter the number1 : "))
    num2 = int(input("enter the number2 : "))
    operator = input("enter the operator : ")

    if operator=='+':
        print(dict["+"](num1,num2))
    elif operator=='-':
        print(dict["-"](num1,num2))
    elif operator=='*':
        print(dict["*"](num1,num2))
    elif operator == '/':
        print(dict["/"](num1,num2))
    else:
        print("invalid operand selection!!!")

    again = True
    while again:
        a=input("do you want to continue(yes or no ) : ").lower()
        if a=="yes":
            run = True
            break
        elif a=="no":
            run = False
            print("thank you!!")
            break
        else:
            print("invalid input selection !!")
            run = True
            break
