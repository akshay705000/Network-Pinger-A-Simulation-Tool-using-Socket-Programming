# TCPPingerConcurrentServer.py 
# random module is used to generate randomized lost packets
# and threading module is used to create threads,
import random
import threading
from socket import *

# Function to handle a client's connection
def handle_client(connectionSocket, clientAddress):
    
    # Loop to get multiple message sequentially from a client
    while True:
        # Receive data from the client
        message = connectionSocket.recv(1024).decode()

        # Check if the client has closed the connection
        if not message:
            print(f"Connection with {clientAddress} closed.")
            break
        else:
            # Print a message when the server receives a packet
            print(f"Received message: {message} from {clientAddress}")

        # Capitalize the received message
        message = message.upper()
        
        # Send the response back to the client
        connectionSocket.send(message.encode())
        # Print a message when the server sends a packet
        print(f"Sent message: {message} to {clientAddress}")

    # Close the connection with the client
    connectionSocket.close()

# Create a TCP socket
# Notice the use of SOCK_STREAM for TCP packets
serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

# Listen for incoming connections, the parameter value 
# can be changed to handle 'n' number of clients.
serverSocket.listen(10)

# Print the status of server
print("The server is ready to receive")

while True:
    # Wait for a client to connect
    connectionSocket, clientAddress = serverSocket.accept()

    # Create a new thread to handle the client concurrently
    client_thread = threading.Thread(target=handle_client, 
                                     args=(connectionSocket, 
                                     clientAddress))
    
    # Start the thread
    client_thread.start()

