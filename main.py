

positions = [" ", " ", " ", " ", " ", " ", " ", " ", " ",]
player = 0


def main():
    run(positions)


def draw_board(li):
    """takes in the board list as an argument and draws the board"""
    print("     |     |     ")
    print("  " + li[0]  + "  |  " + li[1]  + "  |  " + li[2]  + "  ")
    print("     |     |     ")
    print("___________________")

    print("     |     |     ")
    print("  " + li[3]  + "  |  " + li[4]  + "  |  " + li[5]  + "  ")
    print("     |     |     ")
    print("___________________")

    print("     |     |     ")
    print("  " + li[6]  + "  |  " + li[7]  + "  |  " + li[8]  + "  ")
    print("     |     |     ")

def sign(player):
    """takes in the player and returns an x or o depending on which players turn it is"""
    if player == 0:
        return "o"
    elif player == 1:
        return "x"
    else:
        print("An error occured. Please restart the game")
        return

def change_player(player):
    """Takes in a player and returns the other number which can then be reassigned"""
    if player == 0:
        return 1
    else:
        return 0

def run(li):
    player = 1
    while True:
        #call to change player
        player = change_player(player)
        turn = sign(player)
        print(f"player {turn}'s turn")
        

        #take in the position from the player and ensure that it is a proper value. If it is not a proper value it prompts the user to enter a new number
        while True:
            try:
                position = int(input())
                if position not in range(1, 10):
                    print("Invalid entry")
                    continue

                position -= 1
                if li[position] != " ":
                    print("Place already taken. Try again")
                    continue
                else:
                    li[position] = turn
                    draw_board(li)

                    winner = is_winner(li)
                    if winner != 0:
                        if winner == 1:
                            i = "o"
                        elif winner == 2:
                            print("Game Over, Tie Game")
                            return
                        elif winner == -1:
                            i = "x"
                        print(f"The winner is {i}!")
                        return


                break
            except:
                print("Invalid Entry")


def is_winner(li):
    """
    Takes in the list of positions and returns if there is a winner. 0 if there is no winner, 1 if O won, and -1 if X won and 2 if it is a tie.
    """
    #check the horizontal
    for i in range(0, 9, 3):
        if li[i] != " " and li[i] == li[i + 1] and li[i + 1] == li[i + 2]:
            if li[i] == "x":
                return -1
            else:
                return 1

    #check the vertical
    for i in range(3):
        if li[i] != " " and li[i] == li[i + 3] and li[i + 3] == li[i + 6]:
            if li[i] == "x":
                return -1
            else:
                return 1

    #check the diagnol
    if li[0] != " " and li[0] == li[4] and li[4] == li[8] or li[2] != " " and li[2] == li[4] and li[4] == li[6]:
        if li[4] == "x":
            return -1
        else:
            return 1

    if " " not in li:
        return 2

    return 0



if __name__ == "__main__":
    main()


