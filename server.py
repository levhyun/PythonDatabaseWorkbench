import socket
import threading
import Controller

def recvDataSet(data):
    result = ""
    for i in data:
        result += i
    return result

def Handle(conn, SERVER, count):
    while True:
        message = conn.recv(1024).decode()
        print(f"RECEIVE([{SERVER}:6060][Thread:{str(count)}]{message})")
        data = ""
        for i in range(0, len(message)):
            if message[i] == ']':
                name = message[1:i]
                data = message[i+1:]
                break
        resultSendData = Controller.recvDataSet(data)
        resultSendData = f'{resultSendData}'
        conn.send(bytes(resultSendData.encode()))
        #각각의 클라이언트의 메시지, 소켓정보, 쓰레드 번호를 send로 보냄

def init():
    # PORT 지정
    PORT = 6060

    # SERVER 설정
    SERVER = socket.gethostbyname(socket.gethostname())
    # socket.gethostname() -> PC Name
    # socket.gethostbyname(PC Name) -> IP Adress

    # Final Server Aress
    ADDR = (SERVER, PORT)
    # result : ('PC Adress(IPV4)', PORT(6060))

    print(f"※STARTING※\nserver is starting......\nserver adress : {SERVER}:{PORT}\n")

    # socket 설정
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # AF_INET -> 해당 소켓은 IPV4(IP version 4)로 사용을 의미
    # SOCK_STREAM -> 해당 소켓에 TCP 패킷을 받겠다는 의미

    # 서버와 PORT 연결
    server.bind(ADDR)
    # 서버(PC Adress(IPV4))에 PORT(6060)를 연결
    # bind는 값을 튜플로 받기에 괄호가 두개이어야한다
    # result : server.bind(('PC Adress', 6060))

    server.listen()
    # server에 새로운 연결을 listen
    # 소켓 연결, 여기서 파라미터는 접속수를 의미
    print(f"※LISTENING※\nserver is listening on {SERVER}\n")

    count = 0 
    # 쓰레드 번호 카운트
    group = [] 
    #연결된 클라이언트의 소켓정보를 리스트로 묶기 위함
    
    while True:
        count += 1
        conn, addr = server.accept()  
        # 해당 소켓을 열고 대기

        group.append(conn) 
        #연결된 클라이언트의 소켓정보
        print(f"※NEW CONNECTION※\n{str(addr)} connected.")

        #소켓에 연결된 모든 클라이언트에게 동일한 메시지를 보내기 위한 쓰레드(브로드캐스트)
        #연결된 클라이언트가 1명 이상일 경우 변경된 group 리스트로 반영
        #소켓에 연결된 각각의 클라이언트의 메시지를 받을 쓰레드
        recvthread = threading.Thread(target=Handle, args=(conn, SERVER, count))
        recvthread.start()

init()