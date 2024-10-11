import flask
from flask import jsonify, request
import creds
import mysql.connector
from datetime import date
from mysql.connector import Error 
from mysqlhelper import create_connection
from mysqlhelper import execute_query 
from mysqlhelper import execute_read_query


myCreds = creds.Creds() 

conn = create_connection(myCreds.conString, myCreds.username, myCreds.password, myCreds.dbName)

cursor = conn.cursor(dictionary=True)

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#create CRUD API 

'''                                    INVESTOR TABLE                                    '''

#Retrieves a singular investor given an investor ID
@app.route('/api/investor', methods=['GET'])
def select_investor():
    request_data = request.get_json()
    investor_id = request_data['id']
    query = f'''SELECT * from investor where id = {investor_id} '''
    cursor.execute(query)
    var_print = cursor.fetchall()

    return var_print


#JSON Input Example
'''
{
    "id":1
}
'''


#Creates an investor given a first and last name
@app.route('/api/investor', methods=['POST'])
def create_investor():
    request_data = request.get_json()
    firstname = request_data['firstname']
    lastname = request_data['lastname']
    query = f'''INSERT INTO investor(firstname, lastname) VALUES ("{firstname}", "{lastname}")  '''
    execute_query(conn, query)

    return 'Created Investor!'


#JSON Input Example
'''
{
    "firstname":"John",
    "lastname":"Doe"
}
'''

#Updates investor given an investor ID and variable to change
@app.route('/api/investor', methods=['PUT'])
def update_investor():
    request_data = request.get_json()
    paramlist = []
    for param in request_data:
        paramlist.append(param)
    setstring = ''
    for param in request_data:
        try:
            value = int(request_data[param])
        except ValueError:
            value = f'"{request_data[param]}"'
        if param == 'id':
            continue
        if param == paramlist[-1]:
            setstring = setstring + f'{param}={value}'
        else:
            setstring = setstring + f'{param}={value}, '
    idtochange = request_data['id']
    print(setstring)
    query = f'''UPDATE investor SET {setstring} WHERE id={idtochange}'''
    print(query)
    execute_query(conn, query)

    return 'Updated Investor!'


#JSON Input Example
'''
{
    "id":"1",
    "firstname":"Avanduh"
}
'''


#Deletes investor given an investor ID
@app.route('/api/investor', methods=['DELETE']) 
def delete_investor():
    request_data = request.get_json()
    idToDelete = request_data['id']
    query = f'''DELETE FROM investor WHERE id = {idToDelete};'''

    execute_query(conn, query)
    return 'Deleted Investor!'


#JSON Input Example
'''
{
    "id":1
}
'''


'''                                    STOCK TABLE                                    '''


#Creates a stock given a stockname, abbreviation, and current price
@app.route('/api/stock', methods=['POST'])
def create_stock():
    request_data = request.get_json()
    stockname = request_data['stockname']
    abbreviation = request_data['abbreviation']
    currentprice = request_data['currentprice']

    query = f'''INSERT INTO stock(stockname, abbreviation, currentprice) VALUES ("{stockname}", "{abbreviation}", {currentprice})  '''
    execute_query(conn, query)

    return 'Stock Created!'


#JSON Input Example
'''
{
    "stockname":"Dollar",
    "abbreviation":"USD",
    "currentprice":1.00
}
'''

#Updates stock given an stock ID and variable to change
@app.route('/api/stock', methods=['PUT'])
def update_stock():
    request_data = request.get_json()
    paramlist = []
    for param in request_data:
        paramlist.append(param)
    setstring = ''
    for param in request_data:
        try:
            value = float(request_data[param])
        except ValueError:
            value = f'"{request_data[param]}"'
        if param == 'id':
            continue
        if param == paramlist[-1]:
            setstring = setstring + f'{param}={value}'
        else:
            setstring = setstring + f'{param}={value}, '
    idtochange = request_data['id']
    print(setstring)
    query = f'''UPDATE stock SET {setstring} WHERE id={idtochange}'''
    print(query)
    execute_query(conn, query)

    return 'Updated Stock!'


#JSON Input Example
'''
{
    "id":4,
    "currentprice":0.99
}
'''


#Deletes stock given an stock ID
@app.route('/api/stock', methods=['DELETE']) 
def delete_stock():
    request_data = request.get_json()
    idToDelete = request_data['id']
    query = f'''DELETE FROM stock WHERE id = {idToDelete};'''

    execute_query(conn, query)
    return 'Deleted Stock!'


#JSON Input Example
'''
{
    "id":4
}
'''


'''                                    BOND TABLE                                    '''



#Creates a bond given a stockname, abbreviation, and current price
@app.route('/api/bond', methods=['POST'])
def create_bond():
    request_data = request.get_json()
    bondname = request_data['bondname']
    abbreviation = request_data['abbreviation']
    currentprice = request_data['currentprice']

    query = f'''INSERT INTO bond(bondname, abbreviation, currentprice) VALUES ("{bondname}", "{abbreviation}", {currentprice})  '''
    execute_query(conn, query)

    return 'Created Bond!'


#JSON Input Example
'''
{
    "bondname":"Dollar",
    "abbreviation":"USD",
    "currentprice":1.00
}
'''

#Updates bond given an bond ID and variable to change
@app.route('/api/bond', methods=['PUT'])
def update_bond():
    request_data = request.get_json()
    paramlist = []
    for param in request_data:
        paramlist.append(param)
    setstring = ''
    for param in request_data:
        try:
            value = float(request_data[param])
        except ValueError:
            value = f'"{request_data[param]}"'
        if param == 'id':
            continue
        if param == paramlist[-1]:
            setstring = setstring + f'{param}={value}'
        else:
            setstring = setstring + f'{param}={value}, '
    idtochange = request_data['id']
    print(setstring)
    query = f'''UPDATE bond SET {setstring} WHERE id={idtochange}'''
    print(query)
    execute_query(conn, query)

    return 'Updated Bond!'


#JSON Input Example
'''
{
    "id":4,
    "currentprice":0.99
}
'''


#Deletes bond given an bond ID
@app.route('/api/bond', methods=['DELETE']) 
def delete_bond():
    request_data = request.get_json()
    idToDelete = request_data['id']
    query = f'''DELETE FROM bond WHERE id = {idToDelete};'''

    execute_query(conn, query)
    return 'Deleted Bond!'


#JSON Input Example
'''
{
    "id":4
}
'''

'''                                    INVESTOR'S PORTFOLIO -BOND/STOCK-                                     '''

#Retrieves the investor's porfolio that contains stocks and bonds
@app.route('/api/iportfolio', methods=['GET'])
def investor_porfolio():
    request_data = request.get_json()
    investor_id = request_data['id']
    query = f'''SELECT * from investor where id = {investor_id} '''
    cursor.execute(query)
    var_print = cursor.fetchall()

    #link Bond and stocks that's associated with their ID 

    return var_print
'''                                    INVESTOR'S PORTFOLIO TRANSACTION                                   '''

#User makes a transaction for the investor (buy or sell a stock)
@app.route('/api/transactionstock', methods = ['POST'])
def transaction():
    current_day = date.today()
    total = 0
    query = f'''SELECT * from stock'''
    cursor.execute(query)
    stocks = cursor.fetchall()
    message = ''
    request_data = request.get_json()
    investor_id = request_data['id']
    id = request_data['stock_id']
    quantity = request_data['quantity']
    if quantity == 0:
        message = 'Quantity cannot be 0 enter negative number for sell or positive for buy'
    elif quantity > 0:
        for stock in stocks:
            if stock['id'] == id:
                query = f'''INSERT INTO stocktransaction (STdate, investorid, stockid, quantity) values ({current_day}, {investor_id}, {id}, {quantity}) '''
                message = 'Stock Bought!'
        message = 'Stock Not Found'
    else:
        for stock in stocks:
            if stock['id'] == id:
                query = f'''select quantity from stocktransaction where stockid = {id} and id = {investor_id}'''
                cursor.execute(query)
                quantities = cursor.fetchall()
                for quantity in quantities:
                    total += quantity['quantity']
            if total < quantity:
                message = 'Selling quantity greater than investor portfolio'
                break
            else:
                f'''INSERT INTO stocktransaction (STdate, investorid, stockid, quantity) values ({current_day}, {investor_id}, {id}, {quantity}) '''
                message = 'Stock Sold'
                break
                    
    return jsonify(message)


#User makes a transaction for the investor (buy or sell a bond)

    
    


#how do we identify the transaction in order to just only delete the transaction and not the variables associated with transaction 

#User cancels (deletes) a transaction (stock or bond) entirely

@app.route('/api/transaction', methods=['DELETE']) 
def delete_transaction():
    request_data = request.get_json()
    deltransaction = request_data['tbd']
    query = f'''DELETE FROM transaction WHERE id = {deltransaction};'''

    execute_query(conn, query)
    return 'Deleted transaction!'











#Final Code line
app.run()
