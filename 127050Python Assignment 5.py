import random
# Exercise 1

favorite_fruits = ['apple', 'banana', 'kiwi', 'grapes']
print(favorite_fruits[0], favorite_fruits[2], favorite_fruits[-1])

# Exercise 2

numbers = [random.randint(1, 100) for _ in range(5)]

print('Previous list: ', numbers)

numbers[1] = 200
print('Updated list: ', numbers)

sum = 0
for number in numbers:
    sum += number
    
print('Sum of all numbers: ', sum)

numbers.append(sum)
print('Updated array: ', numbers)

# Exercise 3

arr = [1, 5, 7, 9, 10, 12, 244]

num = input('Input a number you think is in the predetermined array: ')

if int(num) in arr:
    print('That number is actually in the array!')
else:
    print('Sorry, that number is not in the array.')
    

def len2(list):
    return len(list)

# Exercise 4

arr2 = [i for i in range(1, 11)]
# print(arr2)

print('First three elements: ', arr2[:3])
print('Last 3 elements: ', arr2[-3:])
floor_index = len(arr2)//2-2
ceiling_index = len(arr2)//2+1
middle_3_elements = arr2[floor_index:ceiling_index]
print('Middle 3 elements: ', middle_3_elements)

# Exercise 5

randoms = [random.randint(1, 50) for _ in range(10)]

sum2 = 0
for int in randoms:
    sum2 += int
    
print('Array: ', randoms)
print('Sum of all numbers in array: ', sum2)


def pizzeria():
    running = True
    toppings = []
    while running:
        if len(toppings) == 0:
            print('You do not have any toppings right now.')
        inp = input("""Welcome to Pizza. What do you want to do?
              a: add topping
              c: change a topping
              o: order pizza
              q: quit order
              r: remove
              s: restart the order\n""")
        
        if inp == "q":
            running = False
        elif inp == "a":
            top = input('What topping do you want to add? ')
            toppings.append(top)
        elif inp == "c":
            change = input('What topping do you want to change? ')
            if change in toppings:
                to = input('What do you want to change it to?')
                for i in range(len(toppings)):
                    if toppings[i] == change:
                        toppings[i] = to
            else:
                print('That topping is not on your pizza.')
        elif inp == 'o':
            print('Thank you for using Pizza.')
            maybe = input('Would you like to order again? y/n')
            if maybe == 'y':
                pizzeria()
            else:
                running = False
        elif inp == 'r':
            to_remove = input('What topping do you want to remove? ')
            if to_remove in toppings:
                toppings.remove(to_remove)
            else:
                print('That topping is not on your pizza.')
        elif inp == 's':
            toppings = []
        else:
            print('I dont understand. Please try again')
            
        print(toppings, "\n Number of toppings: ", len(toppings))
        
        
pizzeria()