import random

def guess(x):           #the user have to guess the number
    print("WELCOME !!!\n*****This is a guess number game, you have to guess a number*****")
    randomNumber = random.randint(1,x)
    guess = 0
    while guess != randomNumber:
        guess = int(input(f'Guess a number between 1 and {x} : '))
        if guess < randomNumber :
            print("Sorry, guess again. Too low")
        elif guess > randomNumber :
            print("Sorry, guess again. Too high")
    print(f"Congrats, you have guessed the right number {randomNumber}!!!")

guess(120)

def computerGuess(x):   #the computer have to guess the number(the user know his self the number)
    print("WELCOME !!!\n*****This is a computer guess number game, the computer have to guess your number*****")
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high :
            guess = random.randint(low, high)
        else :
            guess = low
        feedback = input(f'Is {guess} too high(H), too low(L) or correct(c) ? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Congrats, the computer have guessed your number, {guess}, correctly!!!")

computerGuess(100)