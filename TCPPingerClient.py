# Time module is imported to record time and calculate RTT
import time
from socket import *

# Server address and port is assigned to a variable
server_address = ('172.31.0.3', 12000)

# Get the input of number of ping message
N = int(input("Enter the number of pings message to be sent: "))

# Create a TCP socket and connect the client to the server
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(server_address)

# variables initalization to calclate RTT and lost packets.
# minimum rtt to highest positive value and maximum RTT, 
# total RTT and packets lost and duplicate count to zero.
min_rtt = float('inf')
max_rtt = 0
total_rtt = 0
packets_lost = 0

# This variable store the value of number of packet lost to 
# get an idea about how many message will be retransmitted 
# in future bacuse of reliable TCP protocol.
duplicate_count = 0

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
    # Here \n is added to detect correct message when received.
    message = f"ping {sequence_number} {timestamp}\n"
    
    # Print the message sent
    print(f"Sent: ping {sequence_number} {timestamp}")
    
    # Store the start time to calculate RTT after message received.
    start_time = time.time()
    
    # Try block is used to send exception if the message is not 
    # received in the given time.
    try:
        # Send the ping message to the server
        client_socket.send(message.encode())
        
        # Set socket timeout to required time, which help to create 
        # timeout exception if packet is not received in the given time.
        client_socket.settimeout(1) 

        # Receive the response from the server
        response = client_socket.recv(1024)
        
        # As TCP is reliable transport service, hence the dropout packets 
        # packets are send along with next ping response taht are separated
        # using split and stored as list 
        response_parts = response.decode().split("\n")
        
        # last entry from list is removed which a escape charatcter added
        # at the end of ping message
        response_parts.pop()
        
        # Store the time at which message received to calculate RTT.
        end_time = time.time()

        # Calculate the round-trip time (RTT) in seconds
        rtt = end_time - start_time
        
        # Loop to remove duplicate entries received
        while len(response_parts) >= 1:
            
            # if duplicate count is zero then print the details and 
            # update stastics
            if duplicate_count  == 0:
                # Print the response message and RTT
                print(f"Received: {response_parts.pop(0)}, RTT: {rtt:.6f} seconds")
                
                # Update Total RTT time, minimum and maximum RTT.
                total_rtt += rtt
                min_rtt = min(min_rtt, rtt)
                max_rtt = max(max_rtt, rtt)
            else:
                
                # if duplicate count is nonzero the remove entries from 
                # the begining of list to get the correct entry and 
                #decrease duplicate count by one.
                response_parts.pop(0)
                duplicate_count -= 1

    # Handle timeout
    except timeout:
        
        #Print the timeout message for the packet
        print("Request timed out")
        
        # Update the number of packet lost and duplicate count
        packets_lost += 1
        duplicate_count += 1

# Print connection ping message status
print("\nAll transmission of ping messages completed")

# Calculate packet loss rate and the average RTT
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

