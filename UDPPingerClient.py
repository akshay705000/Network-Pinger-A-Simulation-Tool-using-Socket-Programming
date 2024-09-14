# Time module is imported to record time and calculate RTT
import time
from socket import *

# Server address and port is assigned to a veriable
server_address = ('172.31.0.3', 12000)

# Get the input of number of ping message
N = int(input("Enter the number of pings message to be sent: "))

# Create a UDP socket
client_socket = socket(AF_INET, SOCK_DGRAM)

# Set socket timeout to 1 second, which helip to create 
# timeout exception if packet is not received in 1 second.
client_socket.settimeout(1)

# variables initalization to calclate RTT and lost packets.
# minimum rtt to highest positive value and maximum RTT, 
# total RTT and packets lost to zero.
min_rtt = float('inf')
max_rtt = 0
total_rtt = 0
packets_lost = 0

# Welcome message
print("\n-------Welcome to UDP Ping simulator-------\n")
print("Details of ping messages sent and received\n")

# Use for loop to send N message to server and receive corresponding
# response to calculate all details of ping message.
for i in range(1, N + 1):
    
    # Use variable to store sequence number and timsetamp for each ping message
    sequence_number = i
    timestamp = time.time()
    
    # Generate the ping message in the given format using f-string.
    message = f"ping {sequence_number} {timestamp}"
    
    # Print the message sent
    print("Sent: ", message)
    
    # Store the start time to calculate RTT after message received.
    start_time = time.time()
    
    # Try block is used to send exception if the message is not 
    # received in the given time of 1 second.
    try:
        
        # Send the ping message to the server
        client_socket.sendto(message.encode(), server_address)

        # Receive the response from the server
        response, server = client_socket.recvfrom(1024)
        
        # Store the time at which message received to calculate RTT.
        end_time = time.time()

        # Calculate the round-trip time (RTT) in seconds
        rtt = end_time - start_time

        # Update Total RTT time, minimum and maximum RTT.
        total_rtt += rtt
        min_rtt = min(min_rtt, rtt)
        max_rtt = max(max_rtt, rtt)
        

        # Print the response message and RTT
        print(f"Received: {response.decode()}, RTT: {rtt:.6f} seconds")
    
    # Handle timeout
    except timeout:
        
        #Print the timeout message for the packet
        print("Request timed out")
        
        # Update the number of packet lost
        packets_lost += 1

# Print completion of transmission
print("\nTransmission of ping messages are completed")

# Calculate the packet loss rate and the average RTT
packet_loss_rate = (packets_lost / N) * 100
average_rtt = total_rtt / (N - packets_lost)

# Print summary of the complete ping 
print("\nPing statistics:")
print(f"Number of packets sent    : {N}")
print(f"Number of Packets received: {N - packets_lost}")
print(f"Number of Packets lost:     {packets_lost}")
print(f"Packets lost rate:          {packet_loss_rate:.2f}% loss")
print(f"Minimum RTT:                {min_rtt:.6f} seconds")
print(f"Maximum RTT:                {max_rtt:.6f} seconds")
print(f"Average RTT:                {average_rtt:.6f} seconds")

# Close the socket
client_socket.close()

