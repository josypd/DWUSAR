'''
    @ MySQL Database Adapter
    @ Database Adapter to 'das_db' mysql database
    @ DWU Accommodation System
    @ Developers: Stafford Koki, Daniel Nelson, Louis Ronald
    @ Date: May, 2015
    @ Copyright (C) 2015
    @ DWU, Madang, Papua New Guinea.

    This is the MySQL Database Adapter that makes it possible for
    the system to communicate and manipulate data contained in the
    system database 'das_db.sql'. 
    
'''

import pymysql

class MySqlAdapter():
    def __init__(self,host=None,port=None,user=None,password=None,db=None):
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.db=db
        self.dbaseConnection = pymysql.connect(host=self.host,port=self.port,
                                          user=self.user,password=self.password,
                                          db=self.db)
        self.cursor = self.dbaseConnection.cursor()
    def __del__(self):
        self.dbaseConnection.commit()
        self.dbaseConnection.close()

    def execute(self,SqlCommandStr,DataValues=None):
        if(DataValues == None):
            command = self.cursor.execute(SqlCommandStr)
            results = self.cursor.fetchall()
        else:
            command = self.cursor.execute(SqlCommandStr,DataValues)
            results = self.dbaseConnection.commit()
        return results
    def selectWithParameters(self,SqlCommandStr,data):
        command = self.cursor.execute(SqlCommandStr,data)
        results = self.dbaseConnection.commit()
        return results

    def close(self):
        self.dbaseConnection.commit()
        self.dbaseConnection.close()
        




'''
e.g. running the adapter
print('MySqlAdapter Test Driver')
print('-'*40)
db = MySqlAdapter(host='172.17.19.77',
                  port=3306,
                  user='mctestdb',
                  password='test',
                  db='mcs_students')

print(db.execute('SELECT * FROM students WHERE FIRST_NAME="STAFFORD"'))
'''
