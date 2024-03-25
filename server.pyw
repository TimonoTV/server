import socket
import os
import webbrowser

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostbyname_ex(socket.gethostname())[-1][-1], 8080))





server.listen()

while True:
    user, adres = server.accept()
    
    while True:
        data = user.recv(1024).decode("utf-8").lower()
        
        if data == "youtube":
            webbrowser.open('https://www.youtube.com')
                      
            
        
        
            
        