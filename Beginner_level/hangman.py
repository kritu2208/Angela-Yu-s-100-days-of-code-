import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["ardvart" , "baboon" , "camel"]
chosen_word = random.choice(word_list)

lives = 6 


print(chosen_word)
display = []
word_length = len(chosen_word)

for _ in range(word_length):
    display += "_"
print(display)

end_game =  False
while not end_game :

    guess = input("Guess a letter?").lower()
    print(guess)

    for  position in range(word_length) :
        letter = chosen_word[position]
        if letter == guess :
            display[position] = letter
               
    if guess not in chosen_word :
            lives -= 1
                     
            if lives == 0:
                end_game = True    
                print("you lose.")  
    

            
  
    if "_" not in display:
        end_game =  True
        print("you wins.")
        
    print(stages[lives])
    print(display)








