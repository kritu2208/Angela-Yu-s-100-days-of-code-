def add(x,y):
    return x + y 

def subtract(x,y):
    return x - y 

def multiply(x,y):
    return x * y 

def divide(x,y):
    return x / y 

operations= { "+" : add,
            "-" : subtract,
            "*" : multiply,
            "/" : divide
}

def calculator():
    num1 = int(input("Enter the first number:"))


    for symbols in operations:
        print(symbols)


    operational_symbol = input("Do choose any operation from the above list:") 
    num2 = int(input("Enter the second number:"))
        
    calculation_function = operations[operational_symbol]
    answer = calculation_function(num1, num2)

    print (f"{num1} {operational_symbol} {num2} = {answer}")
    to_continue = True
    while to_continue:

        choice = input(f"type 'y' if u want to continue with {answer} or type'n' if you want to exit.")
        if choice == 'y':
            to_continue
            operational_symbol = input("choose other operation:") 
            new_num = int(input("Enter the new number:"))
                
            calculation_function = operations[operational_symbol]
            second_answer = calculation_function(calculation_function(num1,num2), new_num)

            print (f"{answer} {operational_symbol} {new_num} = {second_answer}")
        else:
            to_continue = False
            print("exit")
    
calculator()    
    
    


