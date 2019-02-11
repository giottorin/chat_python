import socket
s=socket.socket()
s.connect(('localhost',4242))
s.sendall(b'aki')
print(s.recv(1024).decode('utf-8'))
s.close()
# запускается из консоли