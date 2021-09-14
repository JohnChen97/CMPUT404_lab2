import socket, sys, time

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect(('localhost', 8001))
    s.sendall(b'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n')
    #s.shutdown(socket.SHUT_RDWR)
    data = s.recv(20480)
    sys.stdout.write(repr(data))
    s.close()