# -*- coding:utf-8 -*-
import MySQLdb
from MySQLdb.cursors import DictCursor 

#mysql_mod Class help you use MySQLdb module
class mysql_md:

    #Constructor:when you make instance,constructor connect database and make cursor.
    #params hostname:your database hostname,dbname:your database name,username:your user name,password:your user password
    #return void
    def __init__(self,hostname,dbname,username,password):
        self.con=MySQLdb.connect(host=hostname, db=dbname, user=username, passwd=password)
        self.cur=self.con.cursor(DictCursor)

    #query:if you input correct sql,query(sql) easily execute your input sql.
    #params sql:sql
    #return True:correct sql,and execute sql False:Invalid sql
    def query(self,sql):
        try:
            self.cur.execute(sql)
            return True
        except MySQLdb.OperationalError:
            return False
    
    #update_query: function update_query(sql) is same function as query(sql), but for only UPDATE method.
    #params sql:sql(only UPDATE method)
    #eturn True:correct sql,and execute sql False:Invalid sql
    def update_query(self,sql):
        try:
            self.cur.execute(sql)
            self.con.commit()
            return True
        except MySQLdb.OperationalError:
            return False

    #fetch_all: if you finish execute sql,you call this function.this function fetch sql result and retrn dicttionary.
    #params void
    #return dictionary key:your fetching column's name value:column's value
    def fetch_all(self):
        return self.cur.fetchall()
    
    #Destructor:when you trush instance,destructor close cursor and mysql connection
    #params void
    #return void
    def __del__(self):
        self.cur.close()
        self.con.close()
