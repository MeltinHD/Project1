import mysql.connector
from datetime import datetime

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='testdatabase'
        )
        self.cursor = self.connection.cursor()

        # Create users table if not exists
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY UNIQUE,
                username VARCHAR(20) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL,
                firstname VARCHAR(255) NOT NULL,
                lastname VARCHAR(255) NOT NULL,
                gender VARCHAR(10) NOT NULL,
                dateofbirth VARCHAR(20) NOT NULL,
                bloodtype VARCHAR(10) NOT NULL,
                address VARCHAR(255),
                city VARCHAR(50),
                province VARCHAR(50),
                postalcode VARCHAR(10)
            )
        ''')
        self.connection.commit()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor

    def fetch_all(self):
        self.cursor.execute('SELECT * FROM users')
        return self.cursor.fetchall()

    # def fetch_one(self, user_id):
    #     self.cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
    #     return self.cursor.fetchone()
    
    def fetch_one(self, user_name):
        self.cursor.execute('SELECT * FROM users WHERE username = %s', (user_name,))
        return self.cursor.fetchone()

    # def create_user(self, username, password, firstname, lastname):
    #     query = 'INSERT INTO users (username, password, firstname, lastname) VALUES (%s, %s, %s, %s)'
    #     self.execute_query(query, (username, password, firstname, lastname))

    def create_user(self, username, password, firstname, lastname, gender, dateofbirth, bloodtype, address, city, province, postalcode):
        query = 'INSERT INTO users (username, password, firstname, lastname, gender, dateofbirth, bloodtype, address, city, province, postalcode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        self.execute_query(query, (username, password, firstname, lastname, gender, dateofbirth, bloodtype, address, city, province, postalcode))

    # def update_user(self, user_id, username, password):
    #     query = 'UPDATE users SET username = %s, password = %s WHERE id = %s'
    #     self.execute_query(query, (username, password, user_id))
    
    def update_user(self, username, password, firstname, lastname, gender, dateofbirth, bloodtype, address, city, province, postalcode):
        query = 'UPDATE users SET password = %s, firstname = %s, lastname = %s, gender = %s, dateofbirth = %s, bloodtype = %s, address = %s, city = %s, province = %s, postalcode = %s WHERE username = %s'
        self.execute_query(query, (password, firstname, lastname, gender, dateofbirth, bloodtype, address, city, province, postalcode, username))
        
    def delete_user(self, user_name):
        query = 'DELETE FROM users WHERE username = %s'
        self.execute_query(query, (user_name,))