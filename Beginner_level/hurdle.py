def jump():
move_left()
if wall_in_right:
    move() 
else:
    move_right()
    
move()
turn_right()
if front_is_clear():
    move()
else:
    turn_right()






while not goal()
    if wall_in_front():
        jump()
    else:
        turn_right()    

        

