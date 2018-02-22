import socket

import sys
from _thread import start_new_thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

host = 'AB'
port = 8889


try:
    s.bind((host, port))
    print("Socket bound to "+host+" "+port.__str__())
except socket.error as msg:
    print("Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]")
    sys.exit()

s.listen(10)
print('Socket now listening')


def clientthread(conn):

    conn.send(b'HELLOOOO !! WELCOME\n')

    while True:

        data = conn.recv(1024)
        reply = 'OK ' + data.decode()
        if not data:
            break

        conn.sendall(reply.encode())
    conn.close()

while 1:
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
    start_new_thread(clientthread, (conn,))

s.close()



