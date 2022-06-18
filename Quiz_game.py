print("Welcome to  my computer quiz !")
playing = input("do you want to play? (y/n) ")
if playing.lower() == "y" or playing.lower() == "yes":
    print("Let's start!")
    score = 0
    for i in range(1, 6):
        print("Question {}".format(i))
        answer = input("What is the output of the following code?\n"
                       ">>> print(\"Hello World\")\n"
                       "Hello World\n")
        if answer == "Hello World":
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    print("You got {} correct answers out of 5".format(score))
    if score == 5:
        print("You are a computer genius!")
    elif score == 4:
        print("You are a computer pro!")
    elif score == 3:
        print("You are a computer intermediate!")
    elif score == 2:
        print("You are a computer beginner!")
    elif score == 1:
        print("You are a computer newbie!")
    else:
        print("You are a computer noob!")
else:
    print("Bye!")
print("Thanks for playing!")
print("Goodbye!")
print("Have a nice day!")
