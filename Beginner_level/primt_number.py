import math
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number%i == 0:
            is_prime = False
    if is_prime:
        print("it is a prime number.")
    else:
        print("is  not prime number.")            
            
  


n = int(input("write the number?"))
prime_checker(number=n)
