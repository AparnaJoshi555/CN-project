import socket
c=socket.socket()


addr=input("Enter IP address : ")
c.connect((addr,9999))
#c.send(bytes('Hello ',"utf-8"))


print("\n\t\t\t\tCommand Operations")
print("\n\t->>>Create a file( Syntax : create <file_name.txt> )")
print("\n\t->>>Read a file( Syntax   : cat <file_name.txt> )")
print("\n\t->>>Write a file( Syntax  : edit <file_name.txt> )")
print("\n\t->>>Delete a file( Syntax : delete <file_name.txt> )")
print("\n\t->>>Exit( Syntax : exit or Exit)")


print("\n")

while True:
    inp = input("\t>>> ")
    if(inp.startswith("create")):

        c.send(bytes("1","utf-8"))
        str1 = inp[7:]
        c.send(bytes(str1, "utf-8"))
        empty_file = c.recv(1024).decode()
        print(empty_file)
        #break
    elif(inp.startswith("cat")):
        c.send(bytes("2", "utf-8"))
        str2 = inp[4:]
        c.send(bytes(str2, "utf-8"))
        read_file = c.recv(1024).decode()
        print(read_file)
        #break
    elif(inp.startswith("edit")):
        c.send(bytes("3", "utf-8"))
        str3 = inp[5:]
        c.send(bytes(str3, "utf-8"))
        req_edit = input("Enter the string to be added : ")
        c.send(bytes(req_edit, "utf-8"))
        write_file = c.recv(1024).decode()
        print(write_file)
        #break
    elif(inp.startswith("delete")):
        c.send(bytes("4", "utf-8"))
        str4 = inp[7:]
        c.send(bytes(str4, "utf-8"))
        delete_file = c.recv(1024).decode()
        print(delete_file)
        #break
    elif (inp=='exit' or inp=='Exit'):
        c.send(bytes("5","utf-8"))
        print('...CONNECTION DECLINED...')
        quit()
    else:
        print("Wrong Command")
        #break

