# imports


# globals


# functions
def print_menu():
    print("** PyCalc")
    print("------------")
    print('[1] Sum')
    print('[2] Subtract')
    print('[3] Multiply')
    print('[4] Divide')

    print('[q] Quit')


# instructions
opc = ''
while(opc != 'q'):
    print_menu()
    opc = input("PLease select an option: ")
    if(opc == 'q'):
        break

    try:
        num1 = float(input("Provide Num 1: "))
        num2 = float(input("Provide Num 2: "))


        if(opc == '1'):
            res = num1 + num2

        elif(opc == '2'):
            res = num1 - num2

        elif(opc == '3'):
            res = num1 * num2

        elif(opc == '4'):
            res = num1 / num2
            if(num2 == 0):
                
                print("**Error, verify and try again!")
                 

        print(f"Result:{res}")

    except:
         print("**Error, verify and try again!")

print("Good Bye!")

"""
HW:
    -multiplication
    -division:
        NOTE: dont allow the user to divide by 0 9/0
        SHOW AN ERROR

"""

