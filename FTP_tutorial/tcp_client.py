import socket 

if __name__ == "__main__":
    # defining the socket parameters
    host="127.0.01"
    port=8080
    sock=int(input('Enter number of clients: '))
    sock.connect((host,port))


    while True:
        filename=input(Filename)