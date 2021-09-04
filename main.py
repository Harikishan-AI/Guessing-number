print("Guessing number\n")
a = 18
no_of_guess = 9
count = 0
while True:
    user = int(input("number: "))
    count = count + 1
    no_of_guess = no_of_guess - 1
    if user < a and count < 10:
        print("Guessing number is lesser")
        print("Number of guesses left out ", no_of_guess)
        if no_of_guess == 0:
            print("Game over!!!")
            break
    elif user > a and count < 10:
        print("Guessing number is greater")
        print("Number of guesses left out ", no_of_guess)
        if no_of_guess == 0:
            print("Game Over!!!")
            break
    elif user == a and count < 10:
        print("You won!!!")
        print("Number of chances taken", count)
        print("Number of Guesses left out ", no_of_guess)
        break
