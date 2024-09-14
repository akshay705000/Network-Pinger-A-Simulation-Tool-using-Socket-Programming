# UDPPingerModifiedServer.py 
from socket import *

# Create a UDP socket  
# Notice the use of SOCK_DGRAM for UDP packets 
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket 
serverSocket.bind(('', 12000))

# Print the status of server
print("The server is ready to receive")

while True:
    # Receive the client packet along with the address it is coming from   
    message, address = serverSocket.recvfrom(1024)

    # Print a message when the server receives a packet
    print(f"Received message: {message.decode()} from {address}")

    # Capitalize the message from the client  
    message = message.upper()
    # The server responds with the modified message     
    serverSocket.sendto(message, address)

    # Print a message when the server sends a packet
    print(f"Sent message: {message} to {address}")

