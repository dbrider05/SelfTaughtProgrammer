import wordlist
import random

def hangman(word):
    wrong = 0 
    stages = ["",
    "________      ",
    "|       |     ",
    "|       0     ",
    "|       |     ",
    "|      /|\    ",
    "|      / \    "]
    win = False
    rword = list(word)
    board = ["_"] * len(word)
    while wrong < len(stages) - 1:
        char = input("Guess a word:")
        if char in rword:
            ind = rword.index(char)
            board[ind] = char
            rword[ind] = "$"
        else:
            wrong += 1
            print(" ".join(board))
            print("\n".join(stages[0:wrong+1]))
        
        if "_" not in board:
            win = True
            print("Hola Amigos! You Win")
            break
    if not win:
        print("You Lost:(, The correct word was {}".format(word))

hangman(random.choice(wordlist.words))