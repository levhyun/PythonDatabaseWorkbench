import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Server import Service
    
def recvDataSet(data):
    setData = Service.deleteSpace(data)
    commandList = Service.InterpretCommands(setData)
    commandNumber = Service.getCommandNumber(commandList[0])
    command = commandList[1]
    if commandNumber == 0:
        return Service.select(command)
    elif commandNumber == 1:
        return Service.create(command)
    elif commandNumber == 3:
        return Service.insert(command)
    elif commandNumber == 4:
        return Service.delete(command)
    elif commandNumber == 5:
        return Service.update(command)
    else:
        return '[ERROR] 존재하지 않는 명령어.'