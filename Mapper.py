import pymysql as db
import pandas as pd

connect = db.connect(host='localhost', user='root', password='2345s', db='Pysql', charset='utf8', autocommit=True, cursorclass=db.cursors.DictCursor)
handle = connect.cursor()

def selectTableList():
    sql = 'SHOW TABLES;' 
    handle.execute(sql)
    result = handle.fetchall()
    handle.close()
    result = pd.DataFrame(result)
    return result

def selectCommandSet(command):
    optionList = ['','','']
    temp = ""
    cnt = 0
    for i in command:
        if i != '[' and i != ']':
            temp += i
        if i == ']':
            optionList[cnt] = temp
            cnt += 1
            temp = ""
    return optionList[0], optionList[1], optionList[2]

def selectSql(table, filed, filter):
    if filter != '':
        return f'SELECT {filed} FROM {table} WHERE {filter};' 
    else:
        return f'SELECT {filed} FROM {table};' 

def selectTable(command):
    table, filed, filter = selectCommandSet(command)
    sql = selectSql(table, filed, filter)
    handle.execute(sql)
    result = handle.fetchall()
    handle.close()
    result = pd.DataFrame(result)
    return result

def selectTableType(command):
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