def addition(a,b):
    print(a+b)
def subtraction (a,b):
    print(a-b)
def multiplication (a,b):
    print(a*b)
def division (a,b):
    print(a/b)
    
def main():
    
    go_on = "da"
    while go_on == "da":
        
    
    
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        operation = input("Select an operation +,-,*,/: ")
        if operation == '+':
            addition(a,b)
        elif operation == '-':
            subtraction(a,b)
        elif operation == '*':
            multiplication(a,b)
        elif operation == '/':
            division(a,b)
        else:
            print("Wrong input, BYE")
            
        go_on = input("Do you want continue, yes/no: ")
            
            
    
        

    
    
main()