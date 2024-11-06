import random


# Exercise 1

def one():
    for i in range(1, 11):
        print(i)
        
# Exercise 2

def two():
    sum = 0
    for i in range(1, 101):
        sum += i
    print(sum)

# Exercise 3

def three():
    sum = 0
    for i in range(1, 51):
        sum += i if not i % 2 else 0
        
    print(sum)

    # could also do 
    # for i in range(2, 51, 2):
    #    sum += i
    
# Exercise 4
def four():
    r = int(input('What number do you want to iterate to?\n'))
    if r < 1:
        print('please input a number greater than 0.')
        four()
    else:
        for i in range(1, r+1):
            print(i)
            
# Exercise 5

def five():
    r = int(input('What number do you want to see a multiplication table of? \n'))
    if r < 1:
        print('please input a positive integer.')
        five()
    else:
        for i in range(1, 11):
            print(r * i)

# Exercise 6

def six():
    for i in range(10, 0, -1):
        print(i)
    print('Blast off!!')
    
# Exercise 7

def seven():
    answer = random.randrange(1, 101)
    guesses = 0
    while guesses < 5:
        inp = int(input('Guess what the number is: \n'))
        if inp == answer:
            print('You guessed the number correctly! Congratulations!')
            return
        elif inp < answer:
            print('Your guess was lower than the answer.')
            guesses += 1
            print('You have {a} guess(es) left.'.format(a=5-guesses))
        elif inp > answer:
            print('Your guess was larger than the answer.')
            guesses += 1
            print('You have {a} guess(es) left.'.format(a=5-guesses))
        else:
            print('Your input was invalid. Try again')
    print('You did not guess the number. The number was {a}'.format(a=answer))
    
    
one()
two()
three()
four()
five()
six()
seven()