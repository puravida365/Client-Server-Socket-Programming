import socket
import os
import sys
from functions import *

# Client code
from socket import *

def listen():
    # Start listening for incoming connections
    clientSocket.listen(1)
    print "Client Socket listening"

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
    while(1):
        x = raw_input('>ftp ')
        b = x.split(" ")
        cmd = b[0] 
        if len(b) == 1:
            cmd = b[0]
        else:
            cmd = b[0]
            fileName = b[1]

        # based on user input call appropriate function
        if cmd == 'put':
            #call put function
            put(fileName, serverPort)
        elif cmd == 'get':
            #call get function
            get(fileName, serverPort)
        elif cmd == 'ls':
            #list files on server
            listFiles(cmd, mysocket)
        elif cmd == 'quit':
            #quit program
            quit()
        else:
            # print menu options
            other()

def main():
    # Command line checks 
    if len(sys.argv) < 2:
        print "USAGE python " + sys.argv[0] + " <Port Number to connect to>" 
        sys.exit(1)

    filename = sys.argv[0]
    serverPort = int(sys.argv[1])

    mysocket = connect(serverPort)
    getData(mysocket)

    listen()

if __name__ == '__main__':
    main()