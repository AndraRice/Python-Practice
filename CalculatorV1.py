# Lesson 01, Andra Rice
# Task:
# Create a calculator that:
# Accepts input of the format "1+1"
# Performs addition, subtraction, multiplication, and division

# Todo: 
# Brackets
# Negatives?
# Symbols that arent operators?

print("Welcome to my super cool calculator!\nType 'Abandon Ship!' to end the program.\nDo not include letters or spaces in your equations.\nHave fun!")

while True:

    eq=input("\nEnter a mathematical equation: ")

    if (eq=="Abandon Ship!"):
        exit()

    #check for letters or spaces in the equation
    i=0
    alpha_or_space=False
    while(i<len(eq)):
        if(eq[i].isalpha()==True or eq[i].isspace()==True):
            alpha_or_space=True
        i=i+1

    if(alpha_or_space==True):
        print("Do not include spaces or letters in your equation.")
        continue

    #make sure theres an operator
    i=0
    include_operator=False
    op=0
    while(i<len(eq)):
        if(eq[i]=="+" or eq[i]=="-" or eq[i]=="*" or eq[i]=="/"):
            include_operator=True
            operator_index=i
            op=op+1
        i=i+1

    if(include_operator==False):
        print("Don't Forget your operator!")
        continue

    if(op>1):
        print("Only include one operator!")
        continue

    #make sure there is a number before the operator
    if(eq[0].isnumeric==False):
        print("Don't forget the first number!")
        continue

    #make sure there is a number after the operator
    if(len(eq)<operator_index+2):
        print("Don't forget the second number!")
        continue

    num1=""
    i=0

    #Seperate the first number from the entered equation
    while(eq[i].isnumeric() or eq[i]=="."):
        num1=num1+eq[i]
        i=i+1

    num1=float(num1) #typecast the first number

    operator=eq[i] #Seperate the operator from the equation

    num2=""
    i=i+1
    #Seperate the second number from the entered equation
    while(i<len(eq) and (eq[i].isnumeric() or eq[i]==".")):
        num2=num2+eq[i]
        i=i+1

    num2=float(num2) #typecast the second number     
    if (num2==0 and operator=="/"):
        print("You can't divide by zero!")
        continue

    result=0

    if(operator=="+"):
        result=num1+num2
        print(eq+"="+str(result))
        continue

    if(operator=="-"):
        result=num1-num2
        print(eq+"="+str(result))
        continue

    if(operator=="/"):
        result=num1/num2
        print(eq+"="+str(result))
        continue

    if(operator=="*"):
        result=num1*num2
        print(eq+"="+str(result))
        continue
