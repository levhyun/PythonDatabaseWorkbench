import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Server import Mapper

def deleteSpace(data):
    result = ""
    for i in data:
        if i != ' ':
            result += i
    return result

def InterpretCommands(data):
    command = ""
    option = ""
    for i in range(0, len(data)):
        if data[i] == '-' or data[i] == '[':
            option = data[i:]
            break
        else:
            command += data[i]
    return [command, option]

def getCommandNumber(command):
    commandNameList = ['조회','생성','사용','추가','삭제','수정']
    for i in range(0,6):
        if commandNameList[i] in command:
            return i
    return -1

def CommandDecomposition3(command):
    optionList = []
    temp = ""
    for i in command:
        if i != '[' and i != ']':
            temp += i
        if i == ']':
            optionList.append(temp)
            temp = ""
    return optionList[0], optionList[1], optionList[2]

def optionCommand(command):
    option = ""
    for i in range(0,len(command)):
        if command[i] == '[':
            option = command[:i]
            command = command[i:]
            break
    return option, command

def select(command):
    if command == "-t": # 테이블 목록 조회
        return Mapper.selectTableList()
    else:
        option, command = optionCommand(command)
        if option == "-r": # 테이블 조회
            table, filed, filter = CommandDecomposition3(command)
            return Mapper.selectTable(table, filed, filter)
        elif option == "-a": # 테이블 타입 조회
            return Mapper.selectTableType(command)

def toList(str):
    List = []
    temp = ""
    for i in str:
        if i != ',':
            temp += i
        else:
            List.append(temp)
            temp = ""
    List.append(temp)
    return List

def create(command):
    table, filed, type = CommandDecomposition3(command)
    return Mapper.createTable(table, toList(filed), toList(type))


def insert(command):
    table, filed, value = CommandDecomposition3(command)
    return Mapper.insertValue(table, filed, value)

def CommandDecomposition1(command):
    result = ""
    for i in command:
        if i != '[' and i != ']':
            result += i
        if i == ']':
            break
    return result

def CommandDecomposition2(command):
    optionList = []
    temp = ""
    for i in command:
        if i != '[' and i != ']':
            temp += i
        if i == ']':
            optionList.append(temp)
            temp = ""
    return optionList[0], optionList[1]

def delete(command):
    option, command = optionCommand(command)
    if option == "-t": # 테이블 삭제
        table = CommandDecomposition1(command)
        return Mapper.deleteTable(table)
    elif option == "-r": # 테이블 값 삭제
        table, filter = CommandDecomposition2(command)
        return Mapper.deleteValue(table, filter)
    
def update(command):
    option, command = optionCommand(command)
    if option == "-t": # 테이블 수정
        # comming soon
        return 'comming soon'
    elif option == "-r": # 테이블 값 수정
        table, update, filter = CommandDecomposition3(command)
        return Mapper.tableValueUpdate(table, update, filter)