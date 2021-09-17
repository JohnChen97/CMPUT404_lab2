import socket, sys, time
from multiprocessing import Pool


def client_connection(address):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect(address)
    s.sendall(b'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n')
    #s.shutdown(socket.SHUT_RDWR)
    data = s.recv(20480)
    sys.stdout.write('Here is the data sent from the server:')
    sys.stdout.write('\n' + repr(data) + '\n')
    s.close()


if __name__ == '__main__':
    address = [('localhost', 8001)]
    #p = Pool()
    #p.map(client_connection, address * 10)

    with Pool() as pool:
        pool.map(client_connection, address * 5)
