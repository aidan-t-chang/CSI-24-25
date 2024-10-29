def main():
    flag = False
    while flag == False:
        print("""Einstein Game -- Rules:
          - Input a 3 digit integer
          - The hundreds place of the number must differ from ones place number by at least two
          - Input "quit" to quit
          --------
          1. Your number will be reversed and substracted from the original number
          2. This new number from step 1 will be reversed again and added to the originally reversed number
          
          I\'m willing to bet I can guess the end number right now: 1089.""")
        first_number = input('Let\'s try it out- input a 3 digit number: ')
        if first_number == "quit":
            return
        # cehcks if all the digits of first_number are in the digits 0-9 and the length of first_number is 3
        if not all(48 <= ord(num) <= 57 for num in first_number) or len(first_number) != 3:
            print('Please input a 3 digit integer.')
        first_number = int(first_number)
        if abs(first_number // 100 - first_number % 10) < 2: # if the hundreds digit is not 2 or more larger trhan the ones digit
            print('Please make sure that the hundreds place number and ones place number differ by at least 2.')
        else:
            flag = True
    reverse_number = int(str(first_number)[::-1])
    # line 23 is equivalent to (n % 10) * 100 + (n % 100) * 10 + (n // 100)
    print('Your number: {a}'.format(a=first_number))
    print('{a} reversed is: {b}'.format(a=first_number, b=reverse_number))
    second_number = abs(first_number - reverse_number)
    print('Difference between {a} and {b}: {c}'.format(a=first_number, b=reverse_number, c=second_number))
    third_number = int(str(second_number)[::-1])
    # line 29 is equivalent to (n % 10) * 100 + (n % 100) * 10 + (n // 100)
    print('The reverse of {a}: {b}'.format(a=second_number, b=third_number))
    final_number = third_number + second_number
    print('The sum of the {a} and {b}: {c}'.format(a=second_number, b=third_number, c=final_number))
    print('I told you so!')
    
    




main()
    
    
    