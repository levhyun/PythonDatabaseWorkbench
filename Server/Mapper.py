import pymysql as db
import pandas as pd

connect = db.connect(host='localhost', user='root', password='2345s', db='Pysql', charset='utf8', autocommit=True, cursorclass=db.cursors.DictCursor)

def selectTableList():
    try:
        handle = connect.cursor()
        sql = 'SHOW TABLES;' 
        handle.execute(sql)
        result = handle.fetchall()
        handle.close()
        result = pd.DataFrame(result)
        return result
    except:
        return '[ERROR] 조회 실패.'

def selectSql(table, filed, filter):
    if filter != '':
        return f'SELECT {filed} FROM {table} WHERE {filter};' 
    else:
        return f'SELECT {filed} FROM {table};' 

def selectTable(table, filed, filter):
    try:
        handle = connect.cursor()
        sql = selectSql(table, filed, filter)
        handle.execute(sql)
        result = handle.fetchall()
        handle.close()
        result = pd.DataFrame(result)
        return result
    except:
        return '[ERROR] 조회 실패.'

def selectTableType(command):
    try:
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
    except:
        return '[ERROR] 조회 실패.'

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
    try:
        handle = connect.cursor()
        sql = createSql(table, filed, type)
        handle.execute(sql)
        handle.close()
        return f'TABLE({table}) 생성 완료.'
    except:
        return '[ERROR] 생성 실패.'

def insertValueFormat(value):
    result = ""
    temp = ""
    cnt = 0
    for i in range(0, len(value)):
        if value[i] == ',':
            result += f'\"{temp}\",'
            cnt += 1
            temp = ""
        else:
            temp += value[i]
    result += f' \"{temp}\"'
    return result


def insertSql(table, filed, value):
    value = insertValueFormat(value)
    return f'INSERT INTO {table}({filed}) VALUES({value});'

def insertValue(table, filed, value):
    try:
        handle = connect.cursor()
        sql = insertSql(table, filed, value)
        handle.execute(sql)
        handle.close()
        return f'{value} 추가 완료.'
    except:
        return '[ERROR] 추가 실패.'
    
def deleteTable(table):
    try:
        handle = connect.cursor()
        sql = f'DROP TABLE {table};'
        handle.execute(sql)
        handle.close()
        return f'{table} 삭제 완료.'
    except:
        return '[ERROR] 삭제 실패.'
    
def deleteValue(table, filter):
    try:
        handle = connect.cursor()
        sql = f'DELETE FROM {table} WHERE {filter};'
        handle.execute(sql)
        handle.close()
        return f'행 삭제 완료.'
    except:
        return '[ERROR] 삭제 실패.'