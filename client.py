#import ephemeral
#import cmds
import ftplib

# Client code
from socket import *

# Name and port number of the server to # which want to connect .
serverName = '127.0.0.1'
serverPort = 12001
filename = 't.txt'

# Create a socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to the server
clientSocket.connect(( serverName , serverPort ))

# A string we want to send to the server
#data = "ftp put" + 

while(1):
    x = raw_input('>ftp')
    data = x

bytesSent = 0

# Keep sending bytes until all bytes are sent
while bytesSent != len(data): 
    # Send that string !
    bytesSent += clientSocket.send(data[bytesSent:])

# Close the socket
clientSocket.close()