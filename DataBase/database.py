import pandas as pd
import psycopg2


# 데이터 베이스 연결하기
class Databases():
    def __init__(self):
        self.db = psycopg2.connect(host='34.42.241.68', database='hana-2023-database',user='postgres',password='1234',port=5432)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()
        self.cursor.close()

    def execute(self,query,args={}):
        self.cursor.execute(query,args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.cursor.commit()

from database import Databases

class CRUD(Databases):
    def insertDB(self,schema,table,colum,data):
        sql = " INSERT INTO {schema}.{table}({colum}) VALUES ('{data}') ;".format(schema=schema,table=table,colum=colum,data=data)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e :
            print(" insert DB err ",e) 
    
    def readDB(self,schema,table,colum):
        sql = " SELECT {colum} from {schema}.{table}".format(colum=colum,schema=schema,table=table)
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e :
            result = (" read DB err",e)
        
        return result

    def updateDB(self,schema,table,colum,value,condition):
        sql = " UPDATE {schema}.{table} SET {colum}='{value}' WHERE {colum}='{condition}' ".format(schema=schema
        , table=table , colum=colum ,value=value,condition=condition )
        try :
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e :
            print(" update DB err",e)

    def deleteDB(self,schema,table,condition):
        sql = " delete from {schema}.{table} where {condition} ; ".format(schema=schema,table=table,
        condition=condition)
        try :
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print( "delete DB err", e)
if __name__ == "__main__":
    db = CRUD()
    db.insertDB(schema='myschema',table='table',colum='ID',data='유동적변경')
    print(db.readDB(schema='myschema',table='table',colum='ID'))
    db.updateDB(schema='myschema',table='table',colum='ID', value='와우',condition='유동적변경')
    db.deleteDB(schema='myschema',table='table',condition ="id != 'd'")