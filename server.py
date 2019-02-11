import socket

HOST = 'localhost'
PORT = 4242
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data:
             break
        print(data.decode('utf-8'))
        conn.sendall(data)
# запускается из консоли