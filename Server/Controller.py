import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Server import Service
    
def recvDataSet(data):
    setData = Service.deleteSpace(data)
    commandList = Service.InterpretCommands(setData)
    print(commandList)
    commandNumber = Service.getCommandNumber(commandList[0])
    command = commandList[1]
    if commandNumber == 0:
        return Service.select(command)
    elif commandNumber == 1:
        print('생성')
    elif commandNumber == 2:
        print('사용')
    elif commandNumber == 3:
        print('추가')
    elif commandNumber == 4:
        print('삭제')
    elif commandNumber == 5:
        print('변경')
    else:
        print('[ERROR] not found command.')