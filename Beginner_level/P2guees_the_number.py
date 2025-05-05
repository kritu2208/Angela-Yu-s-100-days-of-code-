import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
def difficulty_level():    
        level = input("Choose difficulty lever : 'easy' or 'hard'")
        if level == "easy":
            return EASY_LEVEL_TURNS
        else:
            return HARD_LEVEL_TURNS
def check_answer(guess , number , turns):
    if guess <number:
        print("too low")
        return turns- 1 
    elif guess > number:
        print("too high")
        return turns- 1
    else:
        print("you win.") 

def game():
    print("WELCOME TO GUESS THE NUMBER")
    print("I m thinking about a number betweeen 1 and 100.")
    ran_number = random.randint(1,100)

         
    turns = difficulty_level()
    print(f"You have {turns} attempts remaining for guessing. ") 
     
    guess = 0
    while guess!=  ran_number:
        guess = int(input("Make a guess:"))     
        turns = check_answer(guess , ran_number , turns)
    
            
game()     

    
      
    
        
            
    