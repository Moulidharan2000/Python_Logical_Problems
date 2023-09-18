from random import randint


def guess():
    generated_num = randint(1, 10)
    while True:
        user_num = int(input("Entre the number from 1 to 10 : "))
        if user_num == generated_num and user_num > 0:
            print("You Guessed Correct")
            break
        elif user_num > generated_num and user_num > 0:
            print("Number is Greater than Random Number, Guess lower Number\n")
        else:
            print("Number is Lesser than Random Number, Guess higher number\n")


if __name__ == '__main__':
    guess()
