n=18
number_of_guesses = 1
print("Number of guesses is only 9 \n")
while(number_of_guesses<10):
    guess_number = int(input("Guess a number \n"))
    if (guess_number < 18):
        print("You enter too less number, Please enter high number ! \n")
    elif (guess_number > 18):
        print("You enter too high number, Please enter smaller number ! \n")
    else:
        print("You win !!!!!!!!!!")
        print(number_of_guesses, "Number of guesses you took to finish")
        break
    number_of_guesses = number_of_guesses + 1
    if(number_of_guesses == 6):
        print("#### 4 Number of guesses left !!!!!!!\n")
k=number_of_guesses
if (k > 9):
    print("Game Over !!!!!")











