print("Welcome to the treasure island.Your mission is to find the treasure.")
first = input('You have to select one either left or right?')


if first == "left" :
    second = input("now choose either u want to swim or wait?")
    if second == "wait" :
        door = input("which door u wanna choose - red ,  blue or yellow?")
        if door == "red" or door == "blue" :
            print("game over") 
        elif door == "yellow" :
            print("you win.")
        else:
            print("you loose.")    
    else:
        print('game over')
else:
    print("game over") 


    
           