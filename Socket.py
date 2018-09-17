import socket

HOST = '192.168.0.111'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    connection, address = s.accept()
    with connection:
        print('Connected to', address)
        while True:
            data = connection.recv(1024)
            if not data:
                break
            print(repr(data))
            connection.sendall(data)