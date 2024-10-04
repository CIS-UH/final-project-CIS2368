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

#Create investor table in mySQL 
create_investor_table = '''
    CREATE TABLE investor (
    id INT AUTO_INCREMENT, 
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL, 
    FOREIGN KEY fk_id(id) REFERENCES users1(id),
    PRIMARY KEY (id) )'''

#Create stock table in mySQL 
create_stock_table = '''
    CREATE TABLE stock (
    id INT AUTO_INCREMENT, 
    stockname VARCHAR(255) NOT NULL,
    abbreviation VARCHAR(255) NOT NULL, 
    currentprice decimal(5,2), 
    FOREIGN KEY fk_id(id) REFERENCES users1(id),
    PRIMARY KEY (id) )'''