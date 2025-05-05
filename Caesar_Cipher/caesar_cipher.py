alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True
while should_continue:
    direction = input("type 'encode' to encrypt an 'decode' to decrypt:\n")
    text = input("typr your message:\n").lower()
    shift = int(input("type the shift number:\n"))

    shift = shift % 26

    def caesar (start_text , shift_amount , direction_type):
        end_text = ""
        if direction_type== 'decode':
            shift_amount *= -1
        for letters in start_text:
            position = alphabet.index(letters)
            new_position = position+ shift_amount
            end_text += alphabet[new_position]
        print(f"the {direction_type}ed code is {end_text}.")


    caesar(start_text = text , shift_amount= shift , direction_type= direction)
    result= input("type yes to continue or no to not continue")
    if result == "no":
        should_continue=False 
    else:
        should_continue=True    
# def encrypt(plain_text,shift_amount):
#     cipher_text = ""
#     for letters in plain_text:
#         position = alphabet.index(letters)
#         new_position = position + shift_amount
#         # old_letter = alphabet[position]
#         # print(old_letter)
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"the cipher code is:{cipher_text}")

       

# def decrypt(plain_text ,  shift_amount):
#     cipher_text = ""
#     for letters in plain_text:
#         position = alphabet.index(letters)
#         new_position = position - shift_amount
#         # old_letter = alphabet[position]
#         # print(old_letter)
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"the cipher code is:{cipher_text}")  


# if direction == 'encode':
#     encrypt(plain_text=text , shift_amount= shift) 
# else:
#     decrypt(plain_text=text , shift_amount= shift)

