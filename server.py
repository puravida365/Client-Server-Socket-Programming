# Server code
from socket import *
import commands
import os
import sys
import subprocess
from functions import *

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
            fileName = connectionSocket.recv(40)

            # The other side unexpectedly closed it 's socket
            if not tmpBuff : 
                break

            # Save the data
            data += tmpBuff 

            # do commands

            if data == 'ls':
                lsoutput = subprocess.Popen(['ls','-1'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
                output = lsoutput.stdout.read()
                connectionSocket.send(output)
            elif data == 'put':
                
                # The buffer to all data received from the
                # the client.
                fileData = ""
                
                # The temporary buffer to store the received
                # data.
                recvBuff = ""
                
                # The size of the incoming file
                fileSize = 0    
                
                # The buffer containing the file size
                fileSizeBuff = ""
                
                # Receive the first 10 bytes indicating the
                # size of the file
                fileSizeBuff = recvAll(connectionSocket, 10)
                
                # Get the file size
                fileSize = int(fileSizeBuff)
                
                print "The file size is ", fileSize
                
                # Get the file data
                fileData = recvAll(connectionSocket, fileSize)
                
                print "The file data is: "
                print fileData

        # Close the socket
        connectionSocket.close()

if __name__ == '__main__':
    main()

