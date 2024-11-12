# Exercise 1

student = {"name": "John", "age": 14, "major": "Computer Science"}

print(student)

# Exercise 2
print(student["name"], student["major"])

# Exercise 3

def check_keys(key):
    for k in student.keys():
        if k == key:
            return True
    return False

# Exercise 4

student['graduation_year'] = 2027
student['age'] = 15
del student['major']
print(student)

# Exercise 5

for key in student.keys():
    print(key)
    
for value in student.values():
    print(value)
    
for key in student:
    print(key, student[key])

# Exercise 6

book1 = {"title": 'Python Programming', "author": "John Doe", "year": 2020}
book2 = {'title': 'Data Science Basics', 'author': 'Jane Smith', 'year': 2021}

library = {"book1": book1, "book2": book2}

print(library)

# Exercise 7

def add_product(name, price, quantity, inventory):
    inventory[name] = {'quantity': quantity, 'price': price, 'items_sold': 0}
    
def restock_product(product, amount, inventory):
    inventory[product]['quantity'] += amount

def sell_product(name, items_sold, inventory):
    if inventory[name]['quantity'] < items_sold:
        print('Error: more items sold than in inventory')
        print(inventory[name]['quantity'])
    else:
        inventory[name]['quantity'] -= items_sold
        inventory[name]['items_sold'] += items_sold
        print("Total sale amount: $", str(items_sold * inventory[name]['price']))
    
def inventory_report(inventory):
    for product in inventory:
            q = inventory[product]['quantity']
            p = inventory[product]['price']
            print('Product: ', product)
            print('Current quantity: ', q)
            print('Current price: ', p)
            print('Current value of product in stock: ', q * p)

def sales_report(inventory):
    for product in inventory:
        sold = inventory[product]['items_sold']
        print('Product: ', product)
        print('Quantity sold: ', sold)
        print('Total revenue made from {a}: {b}'.format(a=product, b=inventory[product]['price'] * sold))


def main():
    inventory = {}
    running = True
    while running:
        print("""Welcome to the inventory manager. Here are your options:
              1: add a product to the inventory
              2: restock a product
              3: sell product
              4: inventory report
              5: sales report
              6: quit manager
              """)
        choice = input()
        
        if choice == "1":
            name = input('What is the name of the product? ')
            price = input('What is the price of the item? ')
            quantity = input('What is the quantity of the item? ')
            add_product(name, float(price), int(quantity), inventory)
            print('Inventory updated.')
        elif choice == '2':
            product = input('What is the name of the product? ')
            if product not in inventory.keys():
                print('Sorry, please try again.')
                continue
            amount = input('What is the amount of restock? ')
            restock_product(product, int(amount), inventory)
            print('Inventory updated.')
        elif choice == '3':
            name = input('What is the name of the product? ')
            if name not in inventory.keys():
                print('Sorry, please try again.')
                continue
            items_sold = input('How much of the item was sold? ')
            print(sell_product(name, int(items_sold), inventory))
        elif choice == '4':
            inventory_report(inventory)
        elif choice == '5':
            sales_report(inventory)
        elif choice == '6':
            print('Thank you for using the product manager.')
            inventory = {}
            running = False
            
main()