import random
card = [ 11,2,3,4,5,6,7,8,9,10,10,10,10]

game_exit = True
while not game_exit:
    ask = input("Do you want the game Blackjack? 'yes' or 'no'")    
    if ask == 'yes':
        def deal_card():
            return random.choice(card)
        dealer_cards = [deal_card(),deal_card()]
        current_score = dealer_cards[0] + dealer_cards[1]
        print(f"Your cards : {dealer_cards} , Current score: {current_score}")
        computer_cards = [deal_card()]
        print(f"Computer's first card is {computer_cards}")

        another_card = input("Type 'y' to get another card or 'n' for pass?")
        if another_card == 'y':
            dealer_new_cards = [dealer_cards , deal_card()]
            new_current_score = current_score + dealer_new_cards[1]
            print(f"Your cards : {dealer_new_cards} , Your current score: {new_current_score}")
            
            
            computer_cards = [deal_card()]
            print(f"Computer's first card is {computer_cards}")
            print(f"Your final hand : {dealer_new_cards} , final score : {new_current_score}")

            computers_final_cards = [computer_cards , deal_card()]
            computers_final_score = computer_cards[0] + computers_final_cards[1]
            print(f"Computer's final hand : {computers_final_cards} , final score : {computers_final_score} ")
            
        
        
            if new_current_score > 21 or computers_final_score > new_current_score:
                print("You went over,you lose")
                
            elif computers_final_score > 21 or new_current_score>computers_final_score:
                print("you win")
                
            elif new_current_score == computers_final_score:
                print("its a draw.") 
            else:
                game_exit

        
                
    else:
        game_exit
        print("exit")        


