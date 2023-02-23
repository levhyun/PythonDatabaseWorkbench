import function as set
    
def recvDataSet(data):
    setData = set.deleteSpace(data)
    commandList = set.InterpretCommands(setData)
    commandNumber = set.getCommandNumber(commandList[0])
    if commandNumber == 0:
        print('조회')
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
    return commandList