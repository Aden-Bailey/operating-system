import socket

HOST = "127.0.0.1"
PORT = 8081

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "UDP_TEST_DATAGRAM"
client_socket.sendto(message.encode(), (HOST, PORT))

print("UDP datagram sent")

client_socket.close()