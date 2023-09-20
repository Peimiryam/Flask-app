from flask import Flask, flash
from flask import render_template
from flask import request
from flask import redirect, url_for
from os import listdir
from inventory import load_inventory, load_balance, save_inventory, save_balance, load_history, save_history

app = Flask(__name__)

app.config["SECRET_KEY"] = "12345678asdfg"

#http://127.0.0.1:5000
@app.route('/')
def main_page():
    return render_template('task.html')
 
#http://127.0.0.1:5000/Purchase
@app.route("/Purchase",methods = ['GET', 'POST'])
def purchase():
    if request.method == "POST":
        productname = request.form.get("productname")
        quantity = float(request.form.get("quantity"))
        price = float(request.form.get("price"))
        #print(productname, price, quantity)
        inventory = load_inventory()
        balance = load_balance()
        history = load_history()

        if balance < quantity * price:
            flash("Not enough funds")
            return redirect(url_for("purchase"))

        if productname not in inventory:
            inventory[productname] = 0
        inventory[productname] += quantity
        balance = balance - price * quantity
        #history = inventory, balance
        history.append(productname)
        history.append(quantity)
        history.append(price)
        flash("Purchase successfully")
        save_inventory(inventory)
        save_balance(balance)
        save_history(history)
        return render_template('purchase.html')

    return render_template('purchase.html')

#http://127.0.0.1:5000/Sale
@app.route("/Sale", methods = ['GET', 'POST'])
def sale():
    if request.method == 'POST':
        saleproductname = request.form.get('saleproductname')
        salequantity = int(request.form.get('salequantity'))
        saleprice = float(request.form.get('saleprice'))

        inventory = load_inventory()
        balance = load_balance()
        history = load_history()

        if saleproductname not in inventory:
            flash("\nNot available for sale")
            return redirect(url_for("sale"))

        if saleproductname in inventory:
            
            inventory[saleproductname] -= salequantity

            #flash("\nSale successfully")
                #return redirect(url_for("sale"))
            balance = balance + saleprice * salequantity
            history.append(saleproductname)
            history.append(salequantity)
            history.append(saleprice)
            save_inventory(inventory)
            save_balance(balance)
            save_history(history)
            return render_template('sale.html')

    return render_template('sale.html')


#http://127.0.0.1:5000/Balance
@app.route("/Balance", methods = ['GET', 'POST'])
def balance():
    if request.method == 'POST':
        money = float(request.form.get('money'))
        balance = load_balance()
        history = load_history()
        
        if balance + money < 0:
            flash("Not enough amount")
            return render_template('balance.html')
        
        if balance + money > 0:

            balance = balance + money
        
            if money > 0:
                flash("Added money successfully")
            if money < 0:
                flash("Subtract money successfully")
            save_balance(balance)
        save_history(history)
        return render_template('balance.html')
        
    return render_template('balance.html')


@app.route("/History", methods = ['GET', 'POST'])
def history():
    if request.method == 'POST':
        history = load_history()
        from_value = int(request.form.get('from_value'))
        to_value = int(request.form.get('to_value'))

        if from_value and to_value:
            #lenght = len(history)
            #if lenght < to_value:
                #flash("Wrong input.")
                #return render_template('history.html')
            #else:
            flash(history[from_value : to_value])
            return render_template('history.html')
        else:
            flash("Both Values required.")
            return render_template('history.html')
        
    return render_template('history.html')


if __name__ == '__main__':
    app.run()