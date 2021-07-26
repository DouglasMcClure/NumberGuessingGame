import random

# Random Number generator guessing game
# Created by Douglas McCLure

guesses = 0
number_guessed = False
point_amount = 0
have_won = False

# This function is to randomly generate a number


def random_number(size):
    random_num = random.randrange(1, size)
    return random_num

# This function checks if the number is


def check_number(guessed_number, gen_number):
    if guessed_number > gen_number:
        return 1

    elif guessed_number == gen_number:
        return 0

    elif guessed_number < gen_number:
        return -1


# This function is point calculator


def point_system(guess_amount):
    points = point_amount
    if guess_amount < num_range / 2:
        points = points + 3
    elif guess_amount == num_range / 2:
        points = points + 2
    elif guess_amount > 0:
        points = points + 1
    else:
        points = 0

    return points


# This is the main method to the game


num_range = int(input("Enter the range you want the number to go to: "))
generated_number = random_number(num_range)

while not have_won:
    user_number_guess = int(input("Enter your guessed number: "))
    if guesses < 5:
        if user_number_guess > num_range:
            print("This number is out of range")
        else:
            guesses = guesses + 1
            check_number(user_number_guess, generated_number)

        if check_number(user_number_guess, generated_number) == 0:
            point_amount = point_system(guesses)
            if point_amount < 5:
                print("\nYOU HAVE GUESSED THE NUMBER!!!")
                print("You have:", point_amount, "points.\n")
                num_range = int(input("Enter the range you want the number to go to: "))
                generated_number = random_number(num_range)
                print()
                guesses = 0
            elif point_amount >= 5:
                print("\nYOU HAVE WON!!!")
                have_won = True
        if check_number(user_number_guess, generated_number) != 0:
            if guesses >= 5:
                print("YOU HAVE LOST!!!")
                have_won = False
        if check_number(user_number_guess, generated_number) > 0:
            print("Your guess is too high!")
        elif check_number(user_number_guess, generated_number) < 0:
            print("Your guess is too low!")
