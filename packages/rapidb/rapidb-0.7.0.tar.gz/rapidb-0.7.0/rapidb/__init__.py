# -*- coding: utf-8 -*-
"""
@author: franc
"""

try:
    import pyodbc
except:
    print("pyodbc not found")

try:
    import mariadb as mdb
except:
    print("mariadb not found")
    
import sqlite3
import pandas as pd
from datetime import datetime
import numpy as np
import os




class dbhandler:
    
    
    def __init__(self,conn,dbtype):
        
        self.conn = conn
        self.dbtype = dbtype
        
        self.cur = self.conn.cursor()

        if self.dbtype in ["mssql","mariadb"]:   
            try: 
                self.cur.execute("USE rapidb ;")
            except:
                self.cur.execute("CREATE DATABASE rapidb ;")
                self.cur.execute("USE rapidb ;")
        
        self.table_memory = []
        
        
        
    def key_transform(self,key):
        # Transform key
        key = key.replace(' ','_').lower()
        return key
        
        
        
    def insert_row(self,table_name,values):
        
        # Check if table was already called
        if( (table_name in self.table_memory) == False ):
            
            self.table_memory.append(table_name)
            
            try:
                if self.dbtype == "mssql":
                    self.cur.execute(f"""
                                        CREATE TABLE {table_name}
                                        (
                                            id INT IDENTITY(1,1) PRIMARY KEY,
                                            date_time DATETIME DEFAULT CURRENT_TIMESTAMP
                                        );    
                                    """)
                elif self.dbtype in ["mariadb"]:
                    self.cur.execute(f"""
                                        CREATE TABLE IF NOT EXISTS {table_name}
                                        (
                                            id INT AUTO_INCREMENT PRIMARY KEY,
                                            date_time DATETIME(6) DEFAULT CURRENT_TIMESTAMP
                                        );    
                                    """)
                elif self.dbtype in ["sqlite"]:
                    self.cur.execute(f"""
                                        CREATE TABLE IF NOT EXISTS {table_name}
                                        (
                                            id INTEGER PRIMARY KEY,
                                            date_time DATETIME(6) DEFAULT CURRENT_TIMESTAMP
                                        );    
                                    """)
                    self.conn.commit()
                                    
            except:
                0
        
        # Query beginning
        if(self.dbtype == "mssql"):
            query_part1 = f" INSERT INTO {table_name} ("
            query_part2 = """ VALUES ( """
            
        elif(self.dbtype in ["mariadb","sqlite"]):
            query_part1 = f" INSERT INTO {table_name} (date_time,"
            query_part2 = f""" VALUES ("{datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")}","""    
            
        # Query data insertion
        all_keys = []
        for key in list(values.keys()):
            key_original = key
            all_keys.append(key_original)
            key = self.key_transform(key)
            query_part1 = query_part1 + key + ","
            valm = values[key_original]
            if( isinstance(valm, str) ): # Transform string
                valm = values[key_original].replace("'","\\'")
            if( isinstance(valm, bool) ): # Transform boolean
                valm = valm*1
            query_part2 = query_part2 + f"""'{valm}',"""
            
        # Query completion
        query_part1 = query_part1[:-1]
        query_part2 = query_part2[:-1]
        query_total = query_part1 + ") " + query_part2 + ") "
        
        try:
            self.cur.execute(query_total)
            print("ERROR | Missing columns")
            if self.dbtype == "sqlite":
                self.conn.commit()
            
        except:
            
            # List columns
            if(self.dbtype == "mssql"):
                self.cur.execute(f"""SELECT *
                                    FROM INFORMATION_SCHEMA.COLUMNS
                                    WHERE TABLE_NAME = N'{table_name}'""")
                all_columns = self.cur.fetchall()
                all_columns = list(np.array(all_columns).flatten())
            elif(self.dbtype in ["mariadb"]):
                self.cur.execute(f"SHOW COLUMNS FROM {table_name}")
                all_columns = self.cur.fetchall()
                all_columns = list(np.array(all_columns)[:,0])
            elif(self.dbtype in ["sqlite"]):
                self.cur.execute(f"PRAGMA table_info({table_name});")
                all_columns_fetch = self.cur.fetchall()
                all_columns = []
                for c in all_columns_fetch:
                    all_columns.append(c[1])
                
            # Add missing columns
            for key in all_keys:
                if( ( key in all_columns ) == False ):
                    
                    if( isinstance(values[key],str) ):
                        typec = "TEXT"
                    elif( isinstance(values[key],bool) ):
                        typec = {"mssql":"BIT","mariadb":"BOOL","sqlite":"BOOL"}[self.dbtype]
                    elif( isinstance(values[key],float) | isinstance(values[key],int) ):
                        typec = {"mssql":"FLOAT","mariadb":"DOUBLE","sqlite":"DOUBLE"}[self.dbtype]
                    else:
                        raise "TYPE ERROR"
                    
                    key = self.key_transform(key)
                    
                    if(self.dbtype == "mssql"):
                        self.cur.execute(f"ALTER TABLE {table_name} ADD {key} {typec}")
                    elif(self.dbtype in ["mariadb","sqlite"]):
                        self.cur.execute(f"ALTER TABLE {table_name} ADD COLUMN {key} {typec}")
            
            # Call again row insertion to add data
            self.cur.execute(query_total)
            if self.dbtype == "sqlite":
                self.conn.commit()
            
            
            
    def get_DataFrame(self,table_name,start=None,end=None):
        query = f"SELECT * FROM {table_name}"
        
        if( ( start is not None ) | ( end is not None ) ):
            query = query + " WHERE "
            
        count_where = 0 
        if( start is not None ):
            dts = start.strftime("%Y-%m-%d %H:%M:%S.%f")
            if(self.dbtype == "mssql"):
                dts = dts.replace(" ","T")[:19]
            query = query + f" date_time >= '{dts}' "
            count_where += 1
            
        if( end is not None ):
            if (count_where > 0):
                query = query + " AND "
            dts = end.strftime("%Y-%m-%d %H:%M:%S.%f")
            if(self.dbtype == "mssql"):
                dts = dts.replace(" ","T")[:19]
            query = query + f" date_time <= '{dts}' "
            
        df = pd.read_sql(query,self.conn,index_col="id")
        if(self.dbtype == "sqlite"):
            df["date_time"] = pd.to_datetime(df['date_time'])
        
        return df
    
    
    


class mssql(dbhandler):
    
    def __init__(self,
                 server=None,
                 user_id=None,
                 password=None,
                 driver="SQL Server"):
        
        if server is None:
            server = os.environ['COMPUTERNAME'] + "\SQLEXPRESS"
        
        add_conn = ""
        if(user_id is not None):
            add_conn = add_conn + "User Id="+user_id+";"
        if(password is not None):
            add_conn = add_conn + "Password="+password+";"
        
        conn = pyodbc.connect('Driver={'+driver+'};'+\
                                      'Server={'+server+'};'+\
                                      'Trusted_Connection=yes;'+add_conn
                              ,autocommit=True)
        
        dbhandler.__init__(self,conn,"mssql")



class mariadb(dbhandler):
    
    def __init__(self,
                 user="root",
                 host="127.0.0.1",
                 port=3306,
                 password=""):
        
        conn = mdb.connect(
                        user=user,
                        host=host,
                        port=port,
                        password=password,
                        autocommit=True
                    )
        
        dbhandler.__init__(self,conn,"mariadb")
       
        
       
class sqlite(dbhandler):
    
    def __init__(self,dbname="rapi.db"):
        
        conn = sqlite3.connect(dbname)
        dbhandler.__init__(self,conn,"sqlite")
        
        

