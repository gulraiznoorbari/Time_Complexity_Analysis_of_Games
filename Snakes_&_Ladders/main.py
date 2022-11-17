#22-1440738 M.Hamza Shahid
#23-10903 Muhammad Muzafar

import board as b


if __name__ == '__main__':

    start = input("\n Start the game by pressing y: ")  # Players will be asked to start the game
    if start == "y":
        b.driver()
    user_input3 = input("\nGAME OVER, Do you want to restart game? press y or n: ")  #After the game is completed players can retart the game or exit it.
    if user_input3 == "y":
        print("\n")
        print("\n")
        b.driver()
    if user_input3 == "n":
        exit()



