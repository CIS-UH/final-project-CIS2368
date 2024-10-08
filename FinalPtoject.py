import flask
from flask import jsonify, request
import creds
import mysql.connector
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

    return 'Investor Created'


#JSON Input Example
'''
{
    "firstname":"John",
    "lastname":"Doe"
}
'''

#Updates investor given an investor ID and variable to change
@app.route('/api/investor', methods=['PUT'])
def api_updateall():
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
    return 'Delete request worked'


#JSON Input Example
'''
{
    "id":1
}
'''


'''                                    STOCK TABLE                                    '''


#Creates an investor given a first and last name
@app.route('/api/investor', methods=['POST'])
def create_investor():
    request_data = request.get_json()
    firstname = request_data['firstname']
    lastname = request_data['lastname']
    query = f'''INSERT INTO investor(firstname, lastname) VALUES ("{firstname}", "{lastname}")  '''
    execute_query(conn, query)

    return 'Investor Created'


#JSON Input Example
'''
{
    "firstname":"John",
    "lastname":"Doe"
}
'''

#Updates investor given an investor ID and variable to change
@app.route('/api/investor', methods=['PUT'])
def api_updateall():
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
    return 'Delete request worked'


#JSON Input Example
'''
{
    "id":1
}
'''


'''                                    BOND TABLE                                    '''


#Final Code line
app.run()
