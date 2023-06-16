# Guessing Game Challenge

from random import randint

num = randint(1,100)

# printing introduction to the game and the rules
print("WELCOME TO THE GUESSING GAME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll display COLD")
print("If your guess is within 10 of my number, I'll display WARM")
print("If your guess is farther than your most recent guess, I'll display COLDER")
print("If your guess is closer than your most recent guess, I'll display WARMER")
print("LET'S PLAY!")

# list to contain all the guesses
# adding 0 as a placeholder
guesses = [0]

while True:
    
    guess = int(input("What is your guess? "))
    
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Try again: ')
        continue
    
    if guess == num:
        print('CONGRATULATIONS, YOU GUESSED IT IN {} GUESSES!!'.format(len(guesses)))
        break  
    
    # if guess is incorrect, adding guess to the list
    guesses.append(guess)
    
    # when testing the first guess, guesses[-2]==0, which evaluates to False
    # thus else statement gets executed 
    if guesses[-2]:  
        if abs(num-guess) < abs(num-guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
   
    else:
        if abs(num-guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')

    # an alternate way
        """
        if abs(num - guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')
    else:
        if abs(num - guess) < abs(num - guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!') """
            
