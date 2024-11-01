# Exercise 1

def calculate(operation, num1, num2):
    res = 0 # variable to return instead of multiple return statements
    if operation == "add":
        res = num1 + num2
    elif operation == "subtract":
        res =  num1 - num2
    elif operation == "multiply":
        res = num1 * num2
    elif operation == "divide":
        res = num1 / num2
    else:
        print("please try again using a valid operation.")
    return res
    
operation = input("please input an operation to use:\n")
num1 = int(input("input the first number: \n"))
num2 = int(input("input the second number: \n"))

print(calculate(operation, num1, num2))

# Exercise 2

def convert_temperature(temp, unit):
    res = 0
    if unit == "C":
        res = (temp * 9/5) + 32
    elif unit == "F":
        res = (32 - temp) * 5/9
    else: # it's possible the temperature is also not a valid input ("welcome") so as an blanket statement the 
        # else statement tells the user to input a valid temp or unit.
        print("please input a valid temp/unit for conversion.")
        
    return res

unit = input("What unit would you like to convert from?\n")
temp = int(input("Input the temperature. \n"))

print(convert_temperature(temp, unit))

# Exercise 3

def fizzbuzz(n): # i don't know how many times i have had to write a fizzbuzz function... lol
    res = ""
    if not n % 5 and not n % 3: # equivalent to writing if n % 5 == 0 and n % 5 == 0; not just means the value is 0
        res = "FizzBuzz"
    elif not n % 5:
        res = "Buzz"
    elif not n % 3:
        res = "Fizz"
    else:
        res = n
    return res

n = int(input('Input a number for the FizzBuzz function: \n'))
print(fizzbuzz(n))

# Exercise 4

def is_even(num):
    return not num % 2
# return statement is a contracted way of writing:
# if num % 2 == 0:
#   return True
# else:
#   return False
# writing return num % 2 would return False, since an even number % 2 == 0, which is a value of 0. Therefore,
# the not has to be used as well.

num = int(input("Find out if a number is even or odd: \n"))

print(is_even(num))


# Exercise 5

def grade(score):
    res = ""
    if grade >= 90:
        res = "A"
    elif 80 <= grade < 90:
        res = "B"
    elif 70 <= grade < 80:
        res = "C"
    elif 60 <= grade < 70:
        res = "D"
    else:
        res = "F" # all other if/elif statements cover all the other grades, so the only grade left over is F
        
score = int(input("what was your score for an assignment?\n"))
print(grade(score))

# Exercise 7

def largest_of_three(num1, num2, num3):
    res = 0
    # num1 can be greater than num2 and still be less than num3 so you still need or conditional statements
    if num1 >= num2 >= num3 or num1 >= num3 >= num2: 
        res = num1
    elif num2 >= num1 >= num3 or num2 >= num3 >= num1:
        res = num2
    else:
        res = num3
    return res
    # return max(num1, max(num2, num3)) 

num1 = int(input('input a number: \n'))
num2 = int(input('input a number: \n'))
num3 = int(input('input a number: \n'))

print(largest_of_three(num1, num2, num3))

# Exercise 8

def calculate_discount(amount): # start with the full amount, and based on amount, substract the discount
    res = amount 
    if 50 <= amount <= 100:
        res -= (.1 * amount)
    elif amount > 100:
        res -= (.2 * amount)
    return res

amount = input("what was your purchase amount? \n")

print(calculate_discount(amount))

# Exercise 9

# find if the concatenation of two strings (in both ways) creates a valid palindrome.
def valid_palindrome_after_concatenation(s1, s2):
    concat = s1 + s2
    l, r = 0, len(concat) - 1
    while l < r:
        if concat[l] != concat[r]:
            return False
        l += 1
        r -= 1
        
        
    concat2 = s2 + s1
    l, r = 0, len(concat2) - 1
    while l < r:
        if concat2[l] != concat2[r]:
            return False
        l += 1
        r -= 1
        
    return True

print(valid_palindrome_after_concatenation('ab', 'ba'))
print(valid_palindrome_after_concatenation('ba', 'ab'))
print(valid_palindrome_after_concatenation('123', '123'))
print(valid_palindrome_after_concatenation('abc', 'ba'))

s1 = input("Input a text string \n")
s2 = input("Input another text string to find if the concatenation of both is a palindrome in both ways\n")

