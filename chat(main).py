import socket

#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM,)
sock = socket.socket()
sock.bind(('0.0.0.0', 4242))

print(sock.getsockname())

sock.listen()
conn, addr = sock.accept()

#server_address = ('192.168.1.100', 8080)# откуда мы берем эти данные???
#sock.connect(server_address)

