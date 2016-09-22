import getpass

# string_ha =""

guess = ''

count = 6
play_again = "Y"
str_print = ""

def hanged(ct):
    if ct == 6:
        frame [0][2] = "|"
    elif ct == 5:
        frame[1][2] = " O"
    elif ct == 4:
        frame[2][2] = "|"
    elif ct == 3:
        frame[2][1] = "\\"
    elif ct == 2:
        frame[2][3] = "/  "
    elif ct == 1:
        frame[3][2] = "|"
    elif ct == 0:
        frame[4][1] = "/"
        frame[4][3] = "\\ "
    for row in frame:
        print ''.join(row)


while (play_again == "Y"):
    count = 6
    frame = [["--","--","--","--","|"," "],
            [" "," "," ","  ","  |"," "],
            ["  "," "," ","   "," |"," "],
            ["  "," "," "," ","   |"," "],
            ["  "," "," ","  ","  |"," "],
            [" ","  ","  ","---"," ","---"]]

    string_ha = getpass.getpass(prompt='Player 1: Enter a word for hangman game: ')
    hang_man_str = str(string_ha)
    guessed = ['_']*len(hang_man_str)
    while (count > 0) and (hang_man_str != ''.join(guessed)):
        guess = raw_input("Player 2: Guess a letter in the word: ")
        guess_exist = False
        for i in range(0,len(hang_man_str)):
            if(hang_man_str[i] == guess):
                guessed[i] = guess
                guess_exist = True
        if guess_exist != True:
            count-=1
        print ''.join(guessed)
        print "You have %d guesses left." % count
        # Print the hang man
        hanged(count)

    if((''.join(guessed)) == hang_man_str):
        print "Player 2: Good Job. You guessed the string correctly."
    else:
        print "Player 2: You suck at guessing!, go read a dictionary. Player 1 entered %s as the secret hangman word. " % string_ha
# Play again
    play_again = raw_input("Do you want to try your luck again. (Y or N)")
