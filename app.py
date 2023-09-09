from flask import Flask, flash
from flask import render_template
from flask import request
from flask import redirect, url_for
from os import listdir
#from main import Manager

app = Flask(__name__)

#http://127.0.0.1:5000
@app.route('/')
def main_page():
    return render_template('task.html')

#http://127.0.0.1:5000/success
#@app.route('/success')
#def success():
    #return 'Products purchased!'
 
#http://127.0.0.1:5000/Purchase
@app.route("/Purchase",methods = ['GET'])
def purchase():
    return render_template('purchase.html')

@app.route('/handle_get_purchase', methods=['GET'])
def handle_get_purchase():
    if request.method == 'GET':
        productname = request.args['productname']
        quantity = request.args['quantity']
        price = request.args['price']
        print(productname, quantity, price)

        return redirect(url_for('Purchase'))
    else:
        return render_template('task.html')

#http://127.0.0.1:5000/Sale
@app.route("/Sale", methods = ['GET'])
def sale():
    return render_template('sale.html')

@app.route('/handle_get_sale', methods=['GET'])
def handle_get_sale():
    if request.method == 'GET':
        saleproductname = request.args['saleproductname']
        salequantity = request.args['salequantity']
        saleprice = request.args['saleprice']
        print(saleproductname, salequantity, saleprice)

        return redirect(url_for('/Sale'))
    else:
        return render_template('task.html')

#http://127.0.0.1:5000/Balance
@app.route("/Balance", methods = ['GET'])
def balance():
    return render_template('balance.html')

@app.route("/Balance", methods = ['GET'])
def get_balance():
    if request.method == 'GET':
        money = request.args['money']
        print(money)

        return render_template('balance.html')
    
    else:
        return render_template('task.html')


@app.route("/List-History", methods = ['GET'])
def history():
    return render_template('history.html')

#@app.route("/List-History", methods = ['GET'])
app.route("/", methods = ['GET'])
def history_get(from_value, to_value):
        from_value = request.args['from_value']
        to_value = request.args['to_value']
        #from_value = request.form.get['from_value']
        #to_value = request.form.get['to_value']
        if request.method == 'GET' and from_value and to_value:
            #with open(r'C:\Users\miria\OneDrive\Desktop\Flask\log.txt', 'w') as f:
            with open('log.txt', 'a') as f:
                f.write(from_value, to_value)
                f.close
            return render_template('history.html', from_value = from_value)
        return render_template('history.html', from_value = from_value)

        #else:
            #return render_template('task.html')

if __name__ == '__main__':
    app.run()