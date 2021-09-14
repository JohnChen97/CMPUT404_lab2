import socket, sys, time


def proxy_network(HOST, POST):
    ip_address = socket.gethostbyname(HOST)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s2.connect((ip_address, POST))
    s2.sendall(HOST)
    data = s2.recv(10240)
    s2.shutdown(socket.SHUT_RDWR)

    return data


def user_proxy(HOST, PORT):
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s1.bind((HOST, PORT))
    s1.listen(5)
    while True:
        connection, address = s1.accept()
        data = connection.recv(10240)
        if not data:
            break
        connection.sendall(proxy_network(data.decode(), 80))
    s1.close()


if __name__ == '__main__':
    user_proxy('localhost', 8001)
