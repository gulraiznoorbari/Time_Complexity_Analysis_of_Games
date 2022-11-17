
import random # For dice values each turn.
import snakeorladder as s #importing module function.


dict1 = {}

def board():
    for i in range(100, 0, -1):
        # time complexity O(100) constant time
        if (i == 8):
            dict1[i] = str("L1S")  # + " "+str(i)
        elif (i == 59):
            dict1[i] = str("L2S")  # + " "+str(i)
        elif (i == 75):
            dict1[i] = str("L3S")  # + " "+str(i)
        elif (i == 91):
            dict1[i] = str("S1H")  # + " "+str(i)
        elif (i == 78):
            dict1[i] = str("S2H")  # + " "+str(i)
        elif (i == 36):
            dict1[i] = str("S3H")  # + " "+str(i)
        elif (i == 40):
            dict1[i] = str("S4H")  # + " "+str(i)
        elif (i == 32):
            dict1[i] = str("L1E")
        elif (i == 99):
            dict1[i] = str("L2E")
        elif (i == 97):
            dict1[i] = str("L3E")
        elif (i == 54):
            dict1[i] = str("S1T")
        elif (i == 55):
            dict1[i] = str("S2T")
        elif (i == 25):
            dict1[i] = str("S3T")
        elif (i == 19):
            dict1[i] = str("S4T")

        else:
            dict1[i] = str(i)
    return ("\t | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t | % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s  | %s  | %s  | %s | %s  | %s  | %s  | %s  | %s  | \n\t---------------------------------------------------\n\t " % tuple(
            dict1.values()))


board()


def boardp1():
    # time complexity O(100) constant time
    for i in range(100, 0, -1):
        if dict1[i] == "P1":
            dict1[i] = str(i)
        elif dict1[i] == "P2":
            dict1[i] = "P2"
        elif dict1[i] == "P1 , P2":
            dict1[i] = "P2"
        elif (i == 8):
            dict1[i] = str("L1S")  # + " "+str(i)
        elif (i == 59):
            dict1[i] = str("L2S")  # + " "+str(i)
        elif (i == 75):
            dict1[i] = str("L3S")  # + " "+str(i)
        elif (i == 91):
            dict1[i] = str("S1H")  # + " "+str(i)
        elif (i == 78):
            dict1[i] = str("S2H")  # + " "+str(i)
        elif (i == 36):
            dict1[i] = str("S3H")  # + " "+str(i)
        elif (i == 40):
            dict1[i] = str("S4H")  # + " "+str(i)
        elif (i == 32):
            dict1[i] = str("L1E")
        elif (i == 99):
            dict1[i] = str("L2E")
        elif (i == 97):
            dict1[i] = str("L3E")
        elif (i == 54):
            dict1[i] = str("S1T")
        elif (i == 55):
            dict1[i] = str("S2T")
        elif (i == 25):
            dict1[i] = str("S3T")
        elif (i == 19):
            dict1[i] = str("S4T")
        else:
            dict1[i] = str(i)
    return (
                "\t | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t | % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s  | %s  | %s  | %s | %s  | %s  | %s  | %s  | %s  | \n\t---------------------------------------------------\n\t " % tuple(
            dict1.values()))


def boardp2():
    # time complexity O(100) constant time
    for i in range(100, 0, -1):
        if dict1[i] == "P2":
            dict1[i] = str(i)
        elif dict1[i] == "P1":
            dict1[i] = "P1"
        elif dict1[i] == "P1 , P2":
            dict1[i] = "P1"
        elif dict1[i] == "P2":
            dict1[i] = "P2"
        elif dict1[i] == "P1 , P2":
            dict1[i] = "P2"
        elif (i == 8):
            dict1[i] = str("L1S")  # + " "+str(i)
        elif (i == 59):
            dict1[i] = str("L2S")  # + " "+str(i)
        elif (i == 75):
            dict1[i] = str("L3S")  # + " "+str(i)
        elif (i == 91):
            dict1[i] = str("S1H")  # + " "+str(i)
        elif (i == 78):
            dict1[i] = str("S2H")  # + " "+str(i)
        elif (i == 36):
            dict1[i] = str("S3H")  # + " "+str(i)
        elif (i == 40):
            dict1[i] = str("S4H")  # + " "+str(i)
        elif (i == 32):
            dict1[i] = str("L1E")
        elif (i == 99):
            dict1[i] = str("L2E")
        elif (i == 97):
            dict1[i] = str("L3E")
        elif (i == 54):
            dict1[i] = str("S1T")
        elif (i == 55):
            dict1[i] = str("S2T")
        elif (i == 25):
            dict1[i] = str("S3T")
        elif (i == 19):
            dict1[i] = str("S4T")
        else:
            dict1[i] = str(i)
    return (
                "\t | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t | % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s  | %s  | %s  | %s | %s  | %s  | %s  | %s  | %s  | \n\t---------------------------------------------------\n\t " % tuple(
            dict1.values()))


def driver():
    # time complexity O(n)


    print("###############################GAME STARTED ☺ ###########################")
    print("instructions:\n 1) S1H Represents Snake 1 HEAD\n 2) S1T Represents Snake 1 Tail and represents the same for other snakes on the board ")
    print(" 3) L1S represents Ladder 1 Start \n 4) L1E represents Ladder1 End and represents the same for other ladders on the board.\n")
    print(board())
    player1 = 0
    player2 = 0
    score = 0

    # When any of the player gets to 100 score game will end.

    while (score != 100):  # time complexity O(n)
        boardp1() #O(100)
        user_input = input("\nPlayer 1, Press Y/y to roll the dice: ")
        if (user_input == "y" or user_input == "Y"):
            die = random.randint(1, 6)  # Rolling the dice, Value can be 1,2,3,4,5 and 6.
            print("\nPlayer 1 rolled the dice, Die value = ", die)

            a = player1 + die  # Adding the score of player , with dice value.
            if a <= 100:
                player1 = player1 + die  # If the score is below 100, player can move his gitti.
            else:
                player1 = player1 + 0  # If the score is going above 100, player is not allowed to move his gitti, hence staying in his current position.
            print("\nPlayer 1 Score = ", player1)
            x = s.snakeorladder(player1)  # Check if player's is on ladder or snake.
            player1 = x  # Update the score
            if dict1[player1] == "P2":
                dict1[player1] = "P1 , P2"
            else:
                dict1[player1] = "P1"
            print("\n")
            print(
                "\t | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t | % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s  | %s  | %s  | %s | %s  | %s  | %s  | %s  | %s  | \n\t---------------------------------------------------\n\t " % tuple(
                    dict1.values()))

            # If player 1 's score is 100, then End the game, No need for player 2 to take his turn.
            if player1 == 100:
                score = player1
                break;
        user_input2 = input("\nPlayer 2, Press Y/y to roll the dice; ")
        if (user_input2 == "y" or user_input2 == "Y"):
            die2 = random.randint(1, 6)  # Rolling the dice, Value can be 1,2,3,4,5 and 6.
            print("\nPlayer 2 rolled the dice, Die Value = ", die2)
            b = player2 + die2  # Adding the score of player , with dice value.
            if b <= 100:
                player2 = player2 + die2  # If the score is below 100, player can move his gitti.
            else:
                player2 = player2 + 0  # If the score is going above 100, player is not allowed to move his gitti, hence staying in his current position.
            print("\nPlayer 2 Score = ", player2)
            y = s.snakeorladder(player2)  # Check if player's is on ladder or snake.
            player2 = y  # Update the score
            boardp2()
            if dict1[player2] == "P1":
                dict1[player2] = "P1 , P2"
            else:
                dict1[player2] = "P2"
            print("\n")
            print(
                "\t | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t | % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s  | %s  | %s  | %s | %s  | %s  | %s  | %s  | %s  | \n\t---------------------------------------------------\n\t " % tuple(
                    dict1.values()))

            # If player 2 's score is 100, then End the game, No need for player 1 to take his turn.

            if player2 == 100:
                score = player2
                break;
    if player1 == score:
        print("\nPlayer 1 WINS !!!")
    elif player2 == score:
        print("\nPlayer 2 WINS !!!")
