import socket
import os
Host = "127.0.0.1"    # Standard loopback interface address (Localhost)
Port = 65432          # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((Host, Port))
    s.listen()

    conn, addr = s.accept()
    with conn:
        print("Connected by:", addr)
        while True:
            data = conn.recv(1024).decode()
            print(data)
            if not data:
                break
            if data[0] == "$":
                os.system(data[1:])
            conn.sendall(data.encode())