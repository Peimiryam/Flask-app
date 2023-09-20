import os
import json

INVENTORY_FILE =  "inventory.json"

BALANCE_FILE = "balance.json"

HISTORY_FILE = "history.json"


def load_inventory():
    if not os.path.exists(INVENTORY_FILE):
        return {}
    
    with open (INVENTORY_FILE, 'r') as f:
        return json.load(f)
    

def load_balance():
    if not os.path.exists(BALANCE_FILE):
        return 0
    with open(BALANCE_FILE, 'r') as f:
        return json.load(f)
    
#def load_history():
    #if not os.path.exists(HISTORY_FILE):
        #return {}
def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, 'r') as f:
        return json.load(f)

def save_inventory(inventory):
    with open(INVENTORY_FILE, 'w') as f:
        json.dump(inventory ,f)

def save_balance(balance):
    with open(BALANCE_FILE, 'w') as f:
        json.dump(balance, f)

def save_history(history):

    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f)




