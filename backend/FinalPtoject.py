import flask
from flask import jsonify, request
import creds
import mysql.connector
from datetime import date
from mysql.connector import Error 
from mysqlhelper import create_connection
from mysqlhelper import execute_query 
from mysqlhelper import execute_read_query
from flask_cors import CORS


myCreds = creds.Creds() 

conn = create_connection(myCreds.conString, myCreds.username, myCreds.password, myCreds.dbName)

cursor = conn.cursor(dictionary=True)

app = flask.Flask(__name__)
app.config["DEBUG"] = True

CORS(app)

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
    try:
        request_data = request.get_json()
        idToDelete = request_data['id']
        print(f"Attempting to delete investor with ID: {idToDelete}")
        query = f'''DELETE FROM investor WHERE id = {idToDelete};'''
        execute_query(conn, query)
        return jsonify({"message": "Investor deleted successfully!"}), 200
    except Exception as e:
        print(f"Error deleting investor: {e}")
        return jsonify({"error": "Error deleting investor"}), 500



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
@app.route('/api/portfolio', methods=['POST'])
def investor_porfolio():
    request_data = request.get_json()
    investor_id = request_data['id']

    stock_query = '''
        SELECT 
            i.firstname, 
            i.lastname, 
            s.stockname, 
            s.abbreviation, 
            SUM(st.quantity) AS total_quantity, 
            (SUM(st.quantity) * s.currentprice) AS total_value
        FROM 
            investor i
        JOIN 
            stocktransaction st ON i.id = st.investorid
        JOIN 
            stock s ON st.stockid = s.id
        WHERE 
            i.id = %s
        GROUP BY 
            i.firstname, i.lastname, s.stockname, s.abbreviation, s.currentprice
        HAVING 
            total_quantity > 0;
    '''
    
    cursor.execute(stock_query, (investor_id,))
    stock_result = cursor.fetchall()
    
    bond_query = '''
        SELECT 
            i.firstname, 
            i.lastname, 
            b.bondname, 
            b.abbreviation, 
            SUM(bt.quantity) AS total_quantity, 
            (SUM(bt.quantity) * b.currentprice) AS total_value
        FROM 
            investor i
        JOIN 
            bondtransaction bt ON i.id = bt.investorid
        JOIN 
            bond b ON bt.bondid = b.id
        WHERE 
            i.id = %s
        GROUP BY 
            i.firstname, i.lastname, b.bondname, b.abbreviation, b.currentprice
        HAVING 
            total_quantity > 0;
    '''
    
    cursor.execute(bond_query, (investor_id,))
    bond_result = cursor.fetchall()

    return jsonify(stock_result, bond_result)

#Chat GPT helped with sql query

#JSON INPUT
'''
{
    "id": 1
}
'''

'''                                    INVESTOR'S PORTFOLIO TRANSACTION                                   '''

#User makes a transaction for the investor (buy or sell a stock)
@app.route('/api/transactionstock', methods = ['POST'])
def transaction_stock():
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
                query = f'''INSERT INTO stocktransaction (investorid, stockid, quantity) values ({investor_id}, {id}, {quantity});'''
                execute_query(conn, query)
                message = 'Stock bought'
                break
            else:
                message = 'Stock not found'
    else:
        for stock in stocks:
            if stock['id'] == id:
                query = f'''select quantity from stocktransaction where stockid = {id} and investorid = {investor_id}'''
                cursor.execute(query)
                quantities = cursor.fetchall()
                for quantity1 in quantities:
                    total += quantity1['quantity']
            else:
                message = 'Stock not found'
            if total + quantity < 0:
                message = 'Selling quantity greater than investor portfolio'
                break
            else:
                query = f'''INSERT INTO stocktransaction (investorid, stockid, quantity) values ({investor_id}, {id}, {quantity});'''
                execute_query(conn, query)
                message = 'Stock Sold'
                break
                    
    return jsonify(message)

#JSON Input Example
#Buy stock
'''
{
    "id": 1,
    "stock_id": 1,
    "quantity": 5.00
}
'''
#Sell stock
'''
{
    "id": 1,
    "stock_id": 1,
    "quantity": -5.00
}
'''



#User makes a transaction for the investor (buy or sell a bond)
@app.route('/api/transactionbond', methods = ['POST'])
def transaction_bond():
    total = 0
    query = f'''SELECT * from bond'''
    cursor.execute(query)
    bonds = cursor.fetchall()
    message = ''
    request_data = request.get_json()
    investor_id = request_data['id']
    id = request_data['bond_id']
    quantity = request_data['quantity']
    if quantity == 0:
        message = 'Quantity cannot be 0 enter negative number for sell or positive for buy'
    elif quantity > 0:
        for bond in bonds:
            if bond['id'] == id:
                query = f'''INSERT INTO bondtransaction (investorid, bondid, quantity) values ({investor_id}, {id}, {quantity});'''
                execute_query(conn, query)
                message = 'Bond bought'
                break
            else:
                message = 'Bond not found'
    else:
        for bond in bonds:
            if bond['id'] == id:
                query = f'''select quantity from bondtransaction where bondid = {id} and investorid = {investor_id}'''
                cursor.execute(query)
                quantities = cursor.fetchall()
                for quantity1 in quantities:
                    total += quantity1['quantity']
            if total + quantity < 0:
                message = 'Selling quantity greater than investor portfolio'
                break
            else:
                query = f'''INSERT INTO bondtransaction (investorid, bondid, quantity) values ({investor_id}, {id}, {quantity});'''
                execute_query(conn, query)
                message = 'Bond Sold'
                break
                    
    return jsonify(message)


#JSON Input Example
#Buy bond
'''
{
    "id": 1,
    "bond_id": 1,
    "quantity": 5.00
}
'''
#Sell bond
'''
{
    "id": 1,
    "bond_id": 1,
    "quantity": -5.00
}
'''
    

#User cancels (deletes) a transaction (stock or bond) entirely

@app.route('/api/deletestock', methods=['DELETE']) 
def delete_stock_transaction():
    request_data = request.get_json()
    id = request_data['id']
    query = f'''DELETE FROM stocktransaction WHERE id = {id};'''

    execute_query(conn, query)
    return 'Deleted stock transaction!'


#JSON Delete Example
#Delete Stock 
'''
{
    "id": 1
}
'''
@app.route('/api/deletebond', methods=['DELETE']) 
def delete_bond_transaction():
    request_data = request.get_json()
    id = request_data['id']
    query = f'''DELETE FROM bondtransaction WHERE id = {id};'''

    execute_query(conn, query)
    return 'Deleted bond transaction!'
#JSON Delete Example
#Delete Bond 
'''
{
    "id": 1
}
'''


#show all investors
@app.route('/api/investor/all', methods=["GET"])
def api_all_investors():
    select_investors = "SELECT id, firstname, lastname FROM investor"
    investors = execute_read_query(conn, select_investors)
    return jsonify({"investors": investors})







#Final Code line
app.run()
