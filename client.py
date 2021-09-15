import socket
import http.server

import sys


def get_base_prefix_compat():
    """Get base/real prefix, or sys.prefix if there is none."""
    return getattr(sys, "base_prefix", None) or getattr(
        sys, "real_prefix", None) or sys.prefix


def in_virtualenv():
    return get_base_prefix_compat() != sys.prefix


if __name__ == '__main__':

    #sys.stdout.write(str(in_virtualenv()))

    google_address = "www.google.com"
    s = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM
    )  #AF_INET: using IPV4, using tuple with two elements. SOCK_STREAM: using TCP.
    s.connect((google_address, 80))
    s.sendall(b'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n')
    data1 = s.recv(1024)
    data2 = s.recv(1024)
    print(repr(data1) + '\n')
    print(repr(data2))
