#!/usr/bin/env python3

import socket
import sys

def client_side():
    if len(sys.argv) != 2:
        print("Incorrect parameters specified. Please provide the file name")
        sys.exit()
    file_name = sys.argv[1]
    ct = 0
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    with open(file_name, 'r') as f:
        while ct != 6:
            ct += 1
            data_to_send = f.readline().encode('utf-8')
            client_socket.sendto(data_to_send, ('127.0.0.1', 51234))
            server_reply, address = client_socket.recvfrom(1024)
            server_reply = server_reply.decode().split()
            status_code = server_reply[0]
            if status_code != '200':
                print("There has been a failure in receiving the server response")
                continue
            print("Result: " + str(server_reply[1]))
    print("Closing connection")
    client_socket.close()

if __name__ == '__main__':
    client_side()
    sys.exit(0)
