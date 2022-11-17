def snakeorladder(position):#time complaxity O(1)
    #Ladders at specific scores.
    ladder1 = 8
    ladder2 = 59
    ladder3 = 75
    #Snakes at specific scores.
    snake1 = 91
    snake2 = 78
    snake3 = 36
    snake4 = 40
    #If position is equal to ladder, position will be added. 
    if position == ladder1:
        position = position +24
        print("\nLadder Boost")
        print("\nUpdated score " , position)

    elif position == ladder2:
        position = position + 40
        print("\nLadder Boost")
        print("\nUpdated Score = " , position)

    elif position == ladder3:
        position = position + 22
        print("\nLadder Boost")
        print("\nUpdated Score = " , position)

    
    #If position is equal to snake, position will be subtracted.
    elif position == snake1:
        position = position - 37
        print("\nSnake Bite !!")
        print("\nUpdated Score = " , position)

    elif position == snake2:
        position = position - 23
        print("\nSnake Bite !!!")
        print("\nUpdated Score = " , position)

    elif position == snake3:
        position = position - 11
        print("\nSnake Bite !!")
        print("\nUpdated Score = " , position)

    elif position == snake4:
        position = position - 21
        print("\nSnake Bite !!!")
        print("\nUpdated Score = " , position)

    return position
