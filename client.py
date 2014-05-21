import socket
import os
import sys
from functions import *

# Client code
from socket import *

def listen(mysocket, serverPort):
    newport = serverPort + 1
    # Start listening for incoming connections
    #mysocket.listen(1)
    # Create a TCP socket
    mysocket = socket(AF_INET,SOCK_STREAM)
    
    # Bind the socket to the port
    mysocket.bind(( '', newport ))

    # Start listening for incoming connections
    mysocket.listen(1)
    
    mysocket.send(newport)

def connect(port):
    # Name and port number of the server to # which want to connect .
    serverName = '127.0.0.1'
    serverPort = port

    # Create a socket
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # Connect to the server
    clientSocket.connect(( serverName , serverPort ))

    return clientSocket


def getData(mysocket):
    # get data from user
    x = raw_input('>ftp ')
    b = x.split(" ")
    cmd = b[0]

    while cmd != 'quit':
        if len(b) == 1:
            cmd = b[0]
        else:
            cmd = b[0]
            fileName = b[1]

        # based on user input call appropriate function
        if cmd == 'put':
            #call put function
            transfer(cmd, mysocket)
            transfer(fileName, mysocket)
            put(fileName, mysocket)

        elif cmd == 'get':
            #call get function
            get(fileName, mysocket)

        elif cmd == 'ls':
            #list files on server
            transfer(cmd, mysocket)
            lsoutput = mysocket.recv(1024)
            print lsoutput

        elif cmd == 'quit':
            #quit program
            quit()
        else:
            # print menu options
            other()

        x = raw_input('>ftp ')
        b = x.split(" ")
        cmd = b[0] 


def main():
    # Command line checks 
    if len(sys.argv) < 2:
        print "USAGE python " + sys.argv[0] + " <Port Number to connect to>" 
        sys.exit(1)

    filename = sys.argv[0]
    serverPort = int(sys.argv[1])

    mysocket = connect(serverPort)
    getData(mysocket)


    #listen(mysocket, serverPort)

if __name__ == '__main__':
    main()