import sys, socket
if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    HOST, PORT = "localhost", 8001
    s.bind((HOST, PORT))
    s.listen()
    connection, address = s.accept()
    print(f'Connection: {connection}, \n Address: {address} \n')
    with connection:
        while True:
            data = connection.recv(5120)
            print(data)
            if not data:
                break
            connection.sendall(data)
