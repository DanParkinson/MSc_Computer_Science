'''
A fruit company sells bananas for £3.00 a kilogram plus £4.99 per order for postage and
packaging. If an order is over £50.00, the P&P is reduced by £1.50. Write a script that requests
the user to enter the number of kilo of bananas and print the cost of the order in pence.
'''

import random


def exercise_1():
    bananas = int(input("Please enter the bananas: "))

    price = bananas * 3

    if price > 50:
        print(f"{price + 4.99 - 1.50}")
    else:
        print(f"{price + 4.99}")

def exercise_3():
    number_to_guess = random.randint(1,10)

    guess = None

    while guess != number_to_guess:
        guess = int(input("Guess a number: "))

        if guess == number_to_guess:
            print("yaya")
            break
        elif guess < number_to_guess:
            print("Guess higher dickhead")
        else:
            print("Guss lower dickhead")

# exercise 4

def length(password):
    if len(password) < 8:
        print("It must be at least 8 characters")
        return False
    return True


def cases(password):
    uppercase = 0
    lowercase = 0

    for character in password:
        if character.isupper():
            uppercase += 1
        if character.islower():
            lowercase += 1

    if uppercase < 1 or lowercase < 1:
        print("It must contain uppercase and lowercase letters")
        return False
    return True


def numbers(password):
    digit_count = 0

    for char in password:
        if char.isdigit():
            digit_count += 1

    if digit_count < 1:
        print("It must contain at least one number")
        return False
    return True


def exercise_4():
    valid_password = False

    while not valid_password:
        password = input("Give me a password: ")

        length_check = length(password)
        cases_check = cases(password)
        numbers_check = numbers(password)

        if length_check and cases_check and numbers_check:
            valid_password = True
            print("Password accepted")

    return password



if __name__ == "__main__":
    exercise_4()
