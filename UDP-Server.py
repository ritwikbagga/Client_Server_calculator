#!/usr/bin/env python3

import socket

def server_side():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('127.0.0.1', 51234))
    print("Server started")

    while True:
        data, address = server_socket.recvfrom(1024)
        data = data.decode().split()
        if len(data) != 3:
            server_socket.sendto((str(300) + ' ' + str(-1)).encode('utf-8'), address)
            break
        oc = data[0]
        op1 = data[1]
        op2 = data[2]
        if oc not in ['*','+','-','/']:
            server_socket.sendto((str(300) + ' ' + str(-1)).encode('utf-8'), address)
        try:
            op1 = int(op1)
            op2 = int(op2)
            result = ''
            if oc == '*':
                result = op1 * op2
            elif oc == '+':
                result = op1 + op2
            elif oc == '-':
                result = op1 - op2
            else:
                result = op1 / op2
            server_socket.sendto((str(200) + ' ' + str(result)).encode('utf-8'), address)
        except KeyboardInterrupt:
            print("Shutting Down Server")
            server_socket.close()
        except:
            server_socket.sendto((str(300) + ' ' + str(-1)).encode('utf-8'), address)

if __name__ == '__main__':
    server_side()
