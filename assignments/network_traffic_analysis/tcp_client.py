import socket

HOST = "127.0.0.1"
PORT = 8080

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

message = "TCP_TEST_PACKET"
client_socket.sendall(message.encode())

ack = client_socket.recv(1024)
print(f"Server response: {ack.decode()}")

client_socket.close()