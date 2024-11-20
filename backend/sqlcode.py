#Create investor table in mySQL - created in mysql 
create_investor_table = '''
    CREATE TABLE investor (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL
   '''

#    Extra code 
#    user_id INT,
#    PRIMARY KEY (id),
#    FOREIGN KEY fk_id(user_id) REFERENCES users1(id))

#Create stock table in mySQL - created in mysql 
create_stock_table = '''
    CREATE TABLE stock (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    stockname VARCHAR(255) NOT NULL,
    abbreviation VARCHAR(15) NOT NULL, 
    currentprice decimal(10,2)
     )'''

#    Extra code
#    user_id INT,
#    PRIMARY KEY (id),
#    FOREIGN KEY fk_id(user_id) REFERENCES users1(id))

#Create bond table in mySql - created in mysql 
create_bond_table = '''
    CREATE TABLE bond (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    bondname VARCHAR(255) NOT NULL,
    abbreviation VARCHAR(15) NOT NULL, 
    currentprice decimal(10,2)
     )'''

#    Extra code
#    user_id INT,
#    PRIMARY KEY (id),
#    FOREIGN KEY fk_id(user_id) REFERENCES users1(id))

#Create stocktransaction table in mySql - created in mysql 
create_stocktransaction_table = '''
    CREATE TABLE stocktransaction (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    STdate DATE,
    investorid INT NOT NULL, 
    stockid INT NOT NULL, 
    quantity DECIMAL(10,2),
    PRIMARY KEY (id),
    FOREIGN KEY (investorid) REFERENCES investor(id),
    FOREIGN KEY (stockid) REFERENCES stock(id)
     )'''

#Create bondtransaction table in mySql - created in mysql 
create_bondtransaction_table = '''
    CREATE TABLE bondtransaction (
    id INT AUTO_INCREMENT, 
    BTdate DATE,
    investorid INT NOT NULL, 
    bondid INT NOT NULL, 
    quantity DECIMAL(10,2),
    PRIMARY KEY (id),
    FOREIGN KEY (investorid) REFERENCES investor(id),
    FOREIGN KEY (bondid) REFERENCES bond(id)
    )'''

#input for investor table --------------------------------------
insert_investor_avanduh_witerally = '''
    INSERT INTO investor (firstname, lastname)
    VALUES ('avanduh', 'witerally');
'''

insert_investor_Luumin_Steb = '''
    INSERT INTO investor (firstname, lastname)
    VALUES ('Luumin', 'Steb');
'''

insert_investor_D_Vo = '''
    INSERT INTO investor (firstname, lastname)
    VALUES ('D', 'Vo');
'''
#input for stock table -------------------------------------------
insert_stock_placeholder_1 = '''
    INSERT INTO stock (stockname,abbreviation,currentprice)
    VALUES ('Panda', 'HUA', 4.20 );'''

insert_stock_placeholder_2 = '''
    INSERT INTO stock (stockname,abbreviation,currentprice)
    VALUES ('Circle', 'PIE', 3.14 );'''

insert_stock_placeholder_3 = '''
    INSERT INTO stock (stockname,abbreviation,currentprice)
    VALUES ('Nerds', 'DND', 4.04 );'''

#input for bond table ---------------------------------------------
insert_bond_placeholder_1 = '''
    INSERT INTO bond  (bondname,abbreviation,currentprice)
    VALUES ('James', 'JB', 0.07 );'''

insert_bond_placeholder_2= '''
    INSERT INTO bond  (bondname,abbreviation,currentprice)
    VALUES ('Catanag', 'CAT', 0.69 );'''

insert_bond_placeholder_3= '''
    INSERT INTO bond  (bondname,abbreviation,currentprice)
    VALUES ('Barri', 'DOG', 0.88 );'''