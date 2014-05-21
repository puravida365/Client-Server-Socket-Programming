# Server code
from socket import *
import commands
import os
import sys

def main():

    # Command line checks 
    if len(sys.argv) < 2:
        print "USAGE python " + sys.argv[0] + " <Port #>" 
        sys.exit(1)

    filename = sys.argv[0]
    port = int(sys.argv[1])

    # The port on which to listen
    serverPort = port

    # Create a TCP socket
    serverSocket = socket(AF_INET,SOCK_STREAM)

    
    # Bind the socket to the port
    serverSocket.bind(( '', serverPort ))

    # Start listening for incoming connections
    serverSocket.listen(1)
    print "Server Socket listening"

    # Forever accept incoming connections
    while 1:
        
        print 'Ready to receive'

        # Accept a connection and get client 's socket
        connectionSocket , addr = serverSocket.accept()

        # The temporary buffer
        tmpBuff = ""
        data = ""

        # accept commands from client forever
        while not len(data) == 40:
            # Receive whatever the newly connected client has to send
            tmpBuff = connectionSocket.recv(40)

            # The other side unexpectedly closed it 's socket
            if not tmpBuff : 
                break

            # Save the data
            data += tmpBuff 

            # do commands
            for line in commands.getstatusoutput(data):
                #print line
                # Send back directory listing
                serverSocket.send(data)

        # Close the socket
        connectionSocket.close()

if __name__ == '__main__':
    main()

