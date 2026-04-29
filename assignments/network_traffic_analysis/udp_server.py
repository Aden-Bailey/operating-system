import socket

HOST = "127.0.0.1"
PORT = 8081

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"UDP server listening on {HOST}:{PORT}")

data, addr = server_socket.recvfrom(1024)

print(f"Received datagram from {addr}")
print(f"Payload: {data.decode()}")

server_socket.close()