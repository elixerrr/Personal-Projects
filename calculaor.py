number1= input("Enter the first number:")
if not number1.isdigit():
    print("Please enter a valid number.")
    exit()
number2= input("Enter the second number:")
if not number2.isdigit():
    print("Please enter a valid number.")
    exit()
question= input("Do you want more numbers? (yes/no):")
if question.lower()== "yes":
    number3= input("Enter the third number:")
    if not number3.isdigit():
        print("Please enter a valid number.")
        exit()
if question.lower()== "no":
    print("No more numbers will be added to the calculation.")
    number3= None
if question.lower() not in ["yes", "no"]:
    print("Please enter a valid response (yes/no)")
    exit()
if question.lower()== "no":
    print("You have entered", number1, number2)
if question.lower()== "yes":
    print("You have entered", number1,number2, number3)
operation = input("Enter the operation you want to perform with the two numbers (+,-,*,/) :") if question.lower() == "no" else input("Enter the operation you want to perform with the first two numbers (+,-,*,/)")
if operation not in ["+", "-", "*", "/"]:
    print("Invalid operation. Please enter +,-,*, or /.")
    exit()
if question.lower() == "yes":
     operation2 = input("Enter the operation you want to perform with the third number (+,-,*,/):")
no1 = float(number1)
no2 = float(number2)
no3 = float(number3) if question.lower() == "yes" else None
if operation == "+" and no3 == None:
    result = no1 + no2
    print("The result of the calculation is", result)
if operation == "-" and no3 == None:
    order = input("Do you want to subtract the second number from the first or vice versa? (first/second):")
    if order.lower() == "first" or order.lower() == "1" or order.lower() == "one" or order.lower() == "1st":
        result = no1 - no2
        print("The result of the calculation is", result)
    if order.lower() == "second" or order.lower() == "2" or order.lower() == "two" or order.lower() == "2nd":
        result = no2 - no1
        print("The result of the calculation is", result)
if operation == "*" and no3 == None:
    result = no1 * no2
    print("The result of the calculation is", result)
if operation == "/" and no3 == None:
    order = input("Do you want to divide the first number by the second or vice versa? (first/second)")
    if order.lower() == "first" or order.lower() == "1" or order.lower() == "1st" or order.lower() == "one":
        result = no1 / no2
        print("The result of the calculation is", result, ".")
    if order.lower() == "second" or order.lower() == "2" or order.lower() == "2nd" or order.lower() == "two":
        result = no2 / no1
        print("The result of the calculation is", result, ".")
if operation == "+" and question.lower()== "yes" and operation2 == "+":
    result = no1 + no2 + no3
    print("The result of the operation is", result, ".")
if operation == "-" and operation2 == "-" and question.lower()=="yes":
    order = input("Pick the numbers you want to subtract from the leftover numbers(First/Second/Third)")
    if order.lower() == "first" or order.lower() == "1" or order.lower() == "1st" or order.lower() == "one":
        result = no1 - no2 - no3
        print("The results of the calculation is", result, ".")
    if order.lower() in ["second", "2", "2nd", "two"]:
        result = no2 - no1 - no3
        print("The results of the calculation is", result, ".")
    if order.lower() in ["third", "3", "3rd", "three"]:
        result = no3 - no2 - no1
        print("The result of the calculation is", result, '.')
if ((operation == "+" and operation2 == "*") or (operation == "*" and operation2 == "+")) and question.lower()== "yes":
    order = input("Which number do you want to add to the product of the other two numbers(First/Second/Third)")
    if order.lower() in ["first", "1st", "one", "1"]:
        result = no1 + (no2 * no3)
        print("The results of the calculation is", result, ".")
    if order.lower() in ["second", "2nd", "2", "two"]:
        result = no2 + (no1 * no3)
        print("The results of the calculation is", result, ".")
    if order.lower() in ['third', "3rd", "3", "three"]:
        result = no3 + (no2 * no1)
        print("The results of the calculation is", result, ".")
if ((operation=="+" and operation2== "/") or (operation=="/" and operation2=="+")) and question.lower()== "yes":
    order=input("Which two numbers do you want to divide(first/second,second/third etc) and add to the remaining number.")
    if order.lower() in ["first/second", "first by second", "first divided by second", "1/2","2 divided by 1"]:
        result = no3 + (no1 / no2)
        print("The results of the calculation is", result, ".")
    if order.lower() in ["second/first","second by first","second divided by first","1/2", "1 divided by 2"]:
        result= no3+(no2/no1)
        print("The results of the calculation is", result, ".")
    if order.lower() in ["second/third", "second by third", "second divided by third", "2/3","2 divided by 3"]:
        result= no1+(no2/no3)
        print("The results of the calculation is", result, ".")
    if order.lower() in ["third/second","third by second","third divided by second","3/2","3 divided by 2"]:
        result= no1+(no3/no2)
        print("The results of the calculation is", result, ".")
    if order.lower() in ["first/third","first by third","first divided by third","1/3","1 divided by 3"]:
        result= no2+(no1/no3)
        print("The results of the calculation is", result, ".")
    if order.lower() in ["third/first","third by first","third divided by first","3/1","3 divided by 1"]:
        result= no2+(no3/no1)
        print("The results of the calculation is", result, ".")
if ((operation == "-" and operation2 == "/") or
    (operation == "/" and operation2 == "-")) and question.lower() == "yes":

    order = input(
        "Which two numbers do you want to divide first?\n"
        "Choose from 1/2, 2/1, 1/3, 3/1, 2/3, 3/2 : "
    ).strip().lower()
    if order in ["1/2", "first/second", "first by second", "first divided by second"]:
        quotient = no1 / no2
        leftover = no3
    elif order in ["2/1", "second/first", "second by first", "second divided by first"]:
        quotient = no2 / no1
        leftover = no3
    elif order in ["1/3", "first/third", "first by third"]:
        quotient = no1 / no3
        leftover = no2
    elif order in ["3/1", "third/first", "third by first"]:
        quotient = no3 / no1
        leftover = no2
    elif order in ["2/3", "second/third", "second by third"]:
        quotient = no2 / no3
        leftover = no1
    elif order in ["3/2", "third/second", "third by second"]:
        quotient = no3 / no2
        leftover = no1
    else:
        print("⚠️  I didn’t recognise that pair, try again.")
        exit()
    direction = input(
        "Type 'q-l' to do quotient − leftover, or 'l-q' for leftover − quotient: "
    ).strip().lower()
    result = quotient - leftover if direction == "q-l" else leftover - quotient
    print("The result of the calculation is", result, ".")
if ((operation == "-" and operation2 == "*") or (operation == "*" and operation2 == "-")) and question.lower() == "yes":
    order = input("What numbers do you want to multiply? (first/second, second/first, etc)\nThe remaining number will be subtracted from the result of the first calculation. ")

    if order.lower() in ["first/second", "first by second", "first multiplied by second", "1*2", "1/2"]:
        result = (no1 * no2) - no3
        print("The result of the calculation is", result, ".")
    if order.lower() in ["second/first", "second by first", "second multiplied by first", "2*1", "2/1"]:
        result = (no2 * no1) - no3
        print("The result of the calculation is", result, ".")
    if order.lower() in ["first/third", "first by third", "first multiplied by third", "1*3", "1/3"]:
        result = (no1 * no3) - no2
        print("The result of the calculation is", result, ".")
    if order.lower() in ["third/first", "third by first", "third multiplied by first", "3*1", "3/1"]:
        result = (no3 * no1) - no2
        print("The result of the calculation is", result, ".")
    if order.lower() in ["second/third", "second by third", "second multiplied by third", "2*3", "2/3"]:
        result = (no2 * no3) - no1
        print("The result of the calculation is", result, ".")
    if order.lower() in ["third/second", "third by second", "third multiplied by second", "3*2", "3/2"]:
        result = (no3 * no2) - no1
        print("The result of the calculation is", result, ".")
if ((operation == "*" and operation2 == "/") or (operation == "/" and operation2 == "*")) and question.lower() == "yes":
    order = input("What numbers do you want to divide? (first/second, second/first, etc)\nThe quotient will be multiplied by the remaining number. ")

    if order.lower() in ["first/second", "first by second", "first divided by second", "1/2"]:
        result = (no1 / no2) * no3
        print("The result of the calculation is", result, ".")
    if order.lower() in ["second/first", "second by first", "second divided by first", "2/1"]:
        result = (no2 / no1) * no3
        print("The result of the calculation is", result, ".")
    if order.lower() in ["first/third", "1/3", "first by third"]:
        result = (no1 / no3) * no2
        print("The result of the calculation is", result, ".")
    if order.lower() in ["third/first", "3/1", "third by first"]:
        result = (no3 / no1) * no2
        print("The result of the calculation is", result, ".")
    if order.lower() in ["second/third", "2/3", "second by third"]:
        result = (no2 / no3) * no1
        print("The result of the calculation is", result, ".")
    if order.lower() in ["third/second", "3/2", "third by second"]:
        result = (no3 / no2) * no1
        print("The result of the calculation is", result, ".")
if ((operation == "-" and operation2 == "+") or (operation == "+" and operation2 == "-")) and question.lower() == "yes":
    order = input("What numbers do you want to add? (first+second, first+third, etc)\nThe remaining number will be subtracted from the result of the first calculation. ")

    if order.lower() in ["first+second", "first and second", "1+2", "1/2"]:
        result = (no1 + no2) - no3
        print("The result of the calculation is", result, ".")
    if order.lower() in ["first+third", "first and third", "1+3", "1/3"]:
        result = (no1 + no3) - no2
        print("The result of the calculation is", result, ".")
    if order.lower() in ["second+third", "second and third", "2+3", "2/3"]:
        result = (no2 + no3) - no1
        print("The result of the calculation is", result, ".")



    

        

    
    
        



