import socket

HOST = "127.0.0.1"
PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"TCP server listening on {HOST}:{PORT}")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

data = conn.recv(1024)
print(f"Received: {data.decode()}")

conn.sendall(b"ACK from TCP server")

conn.close()
server_socket.close()