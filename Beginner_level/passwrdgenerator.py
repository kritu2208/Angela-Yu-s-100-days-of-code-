import random
numbers = ['0','1','2','3','4','5','6','7','8','9']
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['@','#','%','^','*']
print("welcome to the password generator....")
num_letters = int(input("how many number of letters you want in password generattor?"))
num_numbers = int(input("how many number of numbers you want in password generattor?"))
num_symbols = int(input("how many number of symbols you want in password generattor?"))

# password = ""

# for char in range( 1 , num_letters+1):
    # password +=  random.choice(letters)

# for char in  range( 1 , num_numbers + 1):
#     password +=  random.choice(numbers)

# for char in range( 1 , num_symbols + 1):
#     password +=  random.choice(symbols)
# print(password)


passwprd_list =[]

for char in range( 1 , num_letters + 1):
    passwprd_list.append(random.choice(letters))
for char in range ( 1 + num_numbers + 1):
    passwprd_list += random.choice(numbers) 
for char in range ( 1 + num_symbols + 1):
    passwprd_list += random.choice(symbols)     

print(passwprd_list)
random.shuffle(passwprd_list)
print(passwprd_list)

password = ""
for char in passwprd_list:
    password += char
print(f"your password is {password}")    