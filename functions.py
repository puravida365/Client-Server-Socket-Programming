from socket import *
import os
import sys


def put(fileName, ServerPort):

    # Open the file
    fileObj = open(fileName, "r")

    # The number of bytes sent
    numSent = 0

    # The file data
    fileData = None

    # Keep sending until all is sent
    while True:
        
        # Read 65536 bytes of data
        fileData = fileObj.read(65536)
        
        # Make sure we did not hit EOF
        if fileData:
            
                
            # Get the size of the data read
            # and convert it to string
            dataSizeStr = str(len(fileData))
            
            # Prepend 0's to the size string
            # until the size is 10 bytes
            while len(dataSizeStr) < 10:
                dataSizeStr = "0" + dataSizeStr
        
        
            # Prepend the size of the data to the
            # file data.
            fileData = dataSizeStr + fileData   
            
            # The number of bytes sent
            numSent = 0
            
            # Send the data!
            while len(fileData) > numSent:
                numSent += connSock.send(fileData[numSent:])
        
        # The file has been read. We are done
        else:
            break


    print "Sent ", numSent, " bytes."
        
    # Close the socket and the file
    connSock.close()
    fileObj.close()

def get(filename):
    print 'Ill get it'

def listFiles(x, mysocket):
    data = x

    bytesSent = 0

    # Keep sending bytes until all bytes are sent
    while bytesSent != len(data): 
        # Send that string !
        bytesSent += mysocket.send(data[bytesSent:])

def quit():
    #sys.exit(1)
    print 'quit'

def other():
    print 'Wrong input. The following commands are avaiable'
    print 'put followed by filename'
    print 'get followed by filename'
    print 'ls - prints out files on server'
    print 'quit - exits program'