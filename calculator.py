def calaculator(op1, op2, op):
    if op=="*" or op=="/" or op=="+" or op=="-"  :
        if op=="*":
            return op1*op2
        elif op=="-":
            return op1-op2
        elif op=="+":
            return op1+op2
        elif op=="/":
            if op2!=0:
                return op1/op2
            else:
                print("Division by zero is not possible!!!")
    else:
        print("Invalid operand or not supported!!!")

while(True):
    print()
    op1=input("Enter the first operand: ")
    op2=input("Enter the second operand: ")
    op=input("Enter the operation you want to perform: ")
    if op1.isdigit() and op2.isdigit():
        op1 = int(op1)
        op2 = int(op2)
        print(op1, op, op2,"=",calaculator(op1, op2, op)) 
    else:
        print("Invalid operands!!!")
    print()
    u_input=input('Enter n to exit or any other key to calculate agian:')
    if u_input=="n":
        break