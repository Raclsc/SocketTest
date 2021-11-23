import os
import time

class client:
    def connection(i):
        import socket

        Host = "127.0.0.1"    # The server's hostname or IP address
        Port = 65432          # Te port used by the server

        s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((Host, Port))

        ### 發送指令內容至伺服器端
        data = ""
        while data != "exit" and data != "quit":
            print("請輸入文字或指令，如果輸入的是指令，請在前方加上$")
            msg = input(": ")
            s.sendall(msg.encode())
            data = s.recv(1024).decode()
            if data == msg:
                condition = "Connection Successful!"
                print(condition)
            else:
                condition = "Connection Fail!"
                print(condition)
                print("在第%d次連線時失敗！", i+1)
            
        # print("Received:", repr(data))
        s.close
    
            
        


# -------------------------------
for i in range(10):
    client.connection(i)
    
    time.sleep(1)

print("已成功連線%d次", i)


