#import modules

#from data import write_data,read_data 

balance_account = 0

history = []

inventory = {}

commands = ['balance', 'sale', 'purchase', 'account', 'list', 'warehouse', 'review', 'end']

class Manager:
    def __init__(self):
        self.commands = {}

    def assign(self, label):
        def inner(callback):
            self.commands[label] = callback
        return inner
    
    def user_input(self):
        while True:
            command = input("Enter one of the commmand here: ")
            if not command:
                break
            if command not in self.commands:
                print("Sorry, not a valid command")
                break
            if command == 'end':
                print("Goodbye!")
                break
            self.commands[command](self)
        

manager = Manager()

print("Welcome to your warehouse software. These are the following commands: \n" )
print('''\n
    1. 'balance': add or subtract from the account.\n 
    2. 'sale': insert the name of the product, its price, and quantity and update the account \n 
    3. 'purchase': insert the name of the product, its price, and quantity and update the account\n 
    4. 'account': display the current account balance.\n 
    5. 'list': display the total inventory in the warehouse along with product prices and quantities.\n
    6. 'warehouse': display the product status in the warehouse.\n
    7. 'review': display recorded operations\n
    8. 'end': terminate the program\n''')

@manager.assign("account")
def account(manager):
    print(f"\nTotal balance: {balance_account}" )

@manager.assign("balance")
def balance(manager):
    global balance_account
    amount = float(input( "\nInsert a value: "))
    operation = input("\nEnter which operation would you like to perform? +/- ")
    if operation == '+':
        balance_account = balance_account + amount 
    elif operation == '-':
        if balance_account - amount < 0:
            print("\nNot enough balance. ")
        elif balance_account - amount > 0:
            balance_account= balance_account - amount
        history.append(operation)
        history.append(amount)

@manager.assign("end")
def end(manager):
    manager.end = True
    
@manager.assign("sale")
def sale(manager):
    global balance_account
    item = input("\nInsert an item name: ")

    if item not in inventory:
        print("\nNot available for sale")

    elif item in inventory:
            
        quantity = int(input("\nInsert a quantity: "))

        if inventory[item][0] < int(quantity):
                print("\nNot enough quantity")

        else:
            inventory[item][0] -= int(quantity)

            price = float(input("\nInsert a price: "))
            balance_account = balance_account + price * quantity
            history.append(f"Name: {item}")
            history.append(f"Price: {price}")
            history.append(quantity)

@manager.assign("purchase")
def purchase(manager):
    global balance_account
    item = input("\nInsert an item name: ")
    quantity = int(input("\nInsert a quantity: "))
    price = float(input("\nInsert a price: "))

    if balance_account - price * quantity < 0:
        print("\nNot enough amount. Sorry :( ")

    else:
        balance_account = balance_account - price * quantity
        history.append(f"Price: {price}")
        history.append(f"Name: {item}")
        history.append(quantity)
        inventory[item] = [quantity, f"Price:{price}"]

@manager.assign("list")
def list(manager):
    if len(inventory) == 0:
        print("\nNo record found")
    else:
        print(inventory)

@manager.assign("warehouse")
def warehouse(manager):
    search = input("\nInsert the name of the item you want to search: ")

    if search in inventory:
        print("\nItem found. ")

        ware = inventory.get(search)
        print(ware)

    else:
        print("\nNot available")

@manager.assign("review")
def review(manager):
    log = input("\nPress 'ALL' to see all history or 'range' to input range values: ")

    if log == 'ALL':
        print(history)

    elif log == 'range':

        print("\nInsert a 'from' and 'to' value to see the history: ")

        lenght = len(history)
        from_value = int(input("\nFrom: "))
        to_value = int(input("\nTo: "))
        if lenght < to_value:
            print("Wrong input.")
        else:
            print(history[from_value : to_value])


while True:

    print("\nCommands: 'balance', 'sale', 'purchase', 'account', 'list', 'warehouse', 'review', 'end'.\n")
    
    manager.user_input()

    break
