import pymysql as db
import pandas as pd

connect = db.connect(host='localhost', user='root', password='2345s', db='Pysql', charset='utf8', autocommit=True, cursorclass=db.cursors.DictCursor)

def selectTableList():
    handle = connect.cursor()
    sql = 'SHOW TABLES;' 
    handle.execute(sql)
    result = handle.fetchall()
    handle.close()
    result = pd.DataFrame(result)
    return result

def selectSql(table, filed, filter):
    if filter != '':
        return f'SELECT {filed} FROM {table} WHERE {filter};' 
    else:
        return f'SELECT {filed} FROM {table};' 

def selectTable(table, filed, filter):
    handle = connect.cursor()
    sql = selectSql(table, filed, filter)
    handle.execute(sql)
    result = handle.fetchall()
    handle.close()
    result = pd.DataFrame(result)
    return result

def selectTableType(command):
    handle = connect.cursor()
    table = ""
    for i in command:
        if i != '[' and i != ']':
            table += i
    sql = f'DESC {table};' 
    handle.execute(sql)
    result = handle.fetchall()
    handle.close()
    result = pd.DataFrame(result)
    return result

def createSqlFormat(filed, type):
    List = []
    for i in range(0, len(filed)):
        List.append(f'{filed[i]} {type[i]} NULL, ')
    result = ""
    for str in List:
        result += str
    return result

def createSql(table, filed, type):
    rows = createSqlFormat(filed, type)
    return f'CREATE TABLE {table}(ID INT NOT NULL AUTO_INCREMENT, {rows}PRIMARY KEY(ID));'

def createTable(table, filed, type):
    handle = connect.cursor()
    sql = createSql(table, filed, type)
    handle.execute(sql)
    handle.close()
    return f'TABLE({table}) 생성 완료.'