import socket

IP = '127.0.0.1'
PORT = 9999

# Create client socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data
client.sendto(b"Bonjour",(IP,PORT))

# Receive data
response, addr = client.recvfrom(4096)

print(response.decode())
client.close()