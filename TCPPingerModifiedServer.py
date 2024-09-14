# TCPPingerModifiedServer.py 
from socket import * 
 
# Create a TCP socket  
# Notice the use of SOCK_STREAM for TCP packets 
serverSocket = socket(AF_INET, SOCK_STREAM) 

# Assign IP address and port number to socket 
serverSocket.bind(('', 12000)) 

# Listen for incoming connections one at a time
serverSocket.listen(1)

# Print the status of server
print("The server is ready to receive")

# Loop to get multiple client connection sequentially
while True:
    
    # Wait for a client to connect
    connectionSocket, clientAddress = serverSocket.accept()

    # Loop to get multiple message sequentially
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
        
        #send the response back to the client
        connectionSocket.send(message.encode())
        # Print a message when the server sends a packet
        print(f"Sent message: {message} to {clientAddress}")


    # Close the connection with the client
    connectionSocket.close()

