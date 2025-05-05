first_name = input("what is first name?")
second_name = input("what is second name?")
                    
first_name = first_name.upper()
second_name = second_name.upper()
print(first_name)
print(second_name)

T= first_name.count("T") + second_name.count("T")
R = first_name.count("R") + second_name.count("R")
U = first_name.count("U") + second_name.count("U")
E = first_name.count("E") + second_name.count("E")
L = first_name.count("L") + second_name.count("L")
O = first_name.count("O") + second_name.count("O")
V = first_name.count("V") + second_name.count("V")
E = first_name.count("E") + second_name.count("E")

first_number = T+R+U+E
print(first_number)

second_number = L+O+V+E
print(second_number)

score = str(first_number) + str(second_number)

print(f"the score is {score}")





