import mysql.connector

class ConnectFactory:
    def __init__(self):    
        self.connection = mysql.connector.connect(    
            host = "db4free.net",
            user = "root_jere",
            password = "1234qwer",
            database = "testes0161"
        )
        
    def get_cursor(self):
        self.cursor = self.connection.cursor()
        return self.cursor

    def get_connection(self):
        return self.connection 