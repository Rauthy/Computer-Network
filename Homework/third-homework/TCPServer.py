from socket import *
serverPort=12000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
while True:
    connectSocket,addr=serverSocket.accept()
    sentence=connectSocket.recv(1024)
    capitalizedSentence=sentence.upper()
    connectSocket.send(capitalizedSentence)
    connectSocket.close()
