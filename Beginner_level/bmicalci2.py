value = input("your bmi value?")
value = float(value)
if value < 18.5 :
    print("you are underweight.")
elif  18.5 < value < 25:
    print("you are normal weight.")

elif 25 < value < 30:

    print("you are over weight.")

elif 30 < value < 35:  
    print("you are obese.")

else:
    print("they are cliniclally obese")
   else: