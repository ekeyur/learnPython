import random

play_again = "Y"
while (play_again == "Y"):
    count = 5;
    secret_number = random.randint(1,10)
    print "I'm thinking of a number between 1 and 10"
    print "You have 5 guess left. "
    while (count>0):
        count-=1
        play_again == "Y"
        guess = raw_input("What's the number? ")
        if int(guess) == secret_number:
            print "Yes! You Win!"
            break;
        elif int(guess)<secret_number:
            print "%d is too low" % int(guess)
            print "You have %d guesses left." % count
        else:
            int(guess)>secret_number
            print "%d is too high" % int(guess)
            print "You have %d guesses left." % count        
    play_again = raw_input("Do you want to play again? (Y or N)")

print "Good Bye!"
