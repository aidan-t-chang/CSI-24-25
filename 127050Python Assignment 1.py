# Aidan Chang - Python Assignment 1 10/22/24

# 1.1) In analogy to the example, write a script that asks users for the temperature in F and prints
# the temperature in C. (Conversion: Celsius = (F - 32) * 5/9 )

def one():
    f = int(input('Input a temperature in fahrenheit: '))
    return (f - 32) * 5/9

# 2.1) Write a python script that prints the following figure without using a multiline print.

def two():
    return "\\    |    /\n   @   @\n     *     \n   \\\"\"\"/"

# 3.1) Write a program that asks users for their favorite color. Create the following output
# (assuming "red" is the chosen color). Use "+" and "*".

def three():
    color = input('What is your favorite color? ')
    color = color + ' ' # string appendage using the + 
    print(color * 10)
    linetwo = color
    for i in range(8): # ten repetitions of the color input, second and third lines have 8 blank spaces
        for j in range(len(color)):
            linetwo += ' '
    linetwo = linetwo + color
    print(linetwo)
    print(linetwo)
    print(color * 10)

# 4.1) Modify the program so that it answers "That is great!" if the answer was "yes", "That is
# disappointing" if the answer was "no" and "That is not an answer to my question."
# otherwise. Use "if ... elif ... else ...".

def four():
    answer = input("Do you like Python? ")
    if answer == "yes":
        print("That is great!")
    elif answer == "no":
        print('That is disappointing!')
    else:
        print("That is not an answer to my question.")
        four()
        

print(one())
print(two())
three()
four()