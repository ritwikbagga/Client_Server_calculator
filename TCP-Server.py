#!/usr/bin/env python3

import socket

def server_side():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 51234))

    server_socket.listen(5);
    print("Server started")

    while True:
        conn, address = server_socket.accept()
        while True:
            data = conn.recv(1024).decode().split()
            if len(data) != 3:
                conn.send((str(300) + ' ' + str(-1)).encode('utf-8'))
                break
            oc = data[0]
            op1 = data[1]
            op2 = data[2]
            if oc not in ['*','+','-','/']:
                conn.send((str(300) + ' ' + str(-1)).encode('utf-8'))
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
                conn.send((str(200) + ' ' + str(result)).encode('utf-8'))
            except KeyboardInterrupt:
                print("Shutting Down Server")
                server_socket.close()
            except:
                conn.send((str(300) + ' ' + str(-1)).encode('utf-8'))

if __name__ == '__main__':
    server_side()
