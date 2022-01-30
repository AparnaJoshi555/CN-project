import os
import socket

s=socket.socket()
print("Socket Created")
s.bind(('',9999))
s.listen(1)
print("waiting for connection")
c,addr=s.accept()
print("Connected to IP address : ",addr)

while True:

    a = c.recv(1024).decode()
    file_name = c.recv(1024).decode()
   
    if(a == '1'):
        text = "A:/Python/"+file_name
        try:

           f = open(text,"x")
           c.send(bytes("File created", "utf-8"))
           print("FILE CREATED")
           f.close()
        except:
           c.send(bytes("FILE ALREADY PRESENT", "utf-8"))
           print("FILE ALREADY PRESENT")

    elif(a =='2'):
        text = "A:/Python/"+file_name
        try:

           f = open(text,"r")
           content=f.read()
           #print(content)
           c.send(bytes(content, "utf-8"))
           f.close()
        except:
            c.send(bytes("FILE NOT EXIST!!!", "utf-8"))
            print("FILE NOT EXIST!!!")

    elif(a == '3'):
        text = "A:/Python/"+file_name
        try:
            f = open(text,"a")
            req_edit = c.recv(1024).decode()
            f.write(req_edit)
            print("FILE EDITED")
            c.send(bytes("File edited", "utf-8"))
            f.close()
        except:
            c.send(bytes("FILE NOT EXIST!!!", "utf-8"))
            print("FILE NOT EXIST!!!")

    elif (a == '4'):
        text = "A:/Python/"+file_name
        try:
            os.remove(text)
            c.send(bytes("File deleted", "utf-8"))
            print("FILE DELETED")
            f.close()
        except:
            c.send(bytes("FILE NOT EXIST!!!", "utf-8"))
            print("FILE NOT EXIST!!!")
    elif(a == '5'):
        print('exited from server')
        quit()


c.close()

