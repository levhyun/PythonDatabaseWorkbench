import Mapper

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
    commandNameList = ['조회','생성','사용','추가','삭제','변경']
    for i in range(0,5):
        if commandNameList[i] in command:
            return i
    return -1

def select(command):
    if command == "-t": # 테이블 목록 조회
        return Mapper.selectTableList()
    else:
        option = ""
        for i in range(0,len(command)):
            if command[i] == '[':
                option = command[:i]
                command = command[i:]
                break
        if option == "-r": # 테이블 조회
            return Mapper.selectTable(command)
        elif option == "-a": # 테이블 타입 조회
            return Mapper.selectTableType(command)
