import socket, sys, time
from multiprocessing import Process

def hand_proxy_network():



def handle_user_proxy(address, connection, client_sent_data):
    data = connection.recv(10240)
   
    connection.sendall(client_sent_data)
    


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
        client_sent_data = proxy_network(data.decode(), 80)
        p = Process(target = handle_user_proxy,
                    args=(address, connection, client_sent_data),
                    daemon=True)
        p.start()
        


if __name__ == '__main__':
    #user_proxy('localhost', 8001)



    HOST = 'localhost'
    PORT = 8001
    net_PORT = 80
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
        s1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s1.bind((HOST, PORT))
        s1.listen(5)

        while True:
            connection, address = s1.accept()
            net_HOST = connection.recv(10240)
            ip_address = socket.gethostbyname(net_HOST)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
                s2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s2.connect((ip_address, net_PORT))
                s2.sendall(net_HOST)
                data = s2.recv(10240)
                s2.shutdown(socket.SHUT_RDWR)