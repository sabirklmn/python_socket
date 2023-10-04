
import socket
import sys

try:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as err:
    print("Failed to create a socket")
    print("Reason"+str(err))
    sys.exit()
print('socket created')


target_host=input("enter the target_host name to connect")
target_port=input("enter the target port")
try:
    sock.connect((target_host,int(target_port)))
    print("socket connected to:"+ target_host+target_port)
    sock.shutdown(2)
except socket.error as err:
    print("Failed connect"+target_host+target_port)
    print("reason"+str(err))
    sys.exit()