# Server code
from socket import *

# The port on which to listen
serverPort = 12000

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

    while len(data) != 40:
        # Receive whatever the newly connected client has to send
        tmpBuff = connectionSocket.recv(40)

        # The other side unexpectedly closed it 's socket
        if not tmpBuff : 
            break

        # Save the data
        data += tmpBuff 

    print data
    # Close the socket
    connectionSocket.close()