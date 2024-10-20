
# MyTCP/UDPPinger

## Project Overview

UDPPinger is a network simulation project that implements both UDP and TCP pinger servers and clients. The project is designed to test the transmission of messages over the network, measure round-trip times (RTT), and simulate packet loss.

### Key Features:

- **UDP Server and Client:**: Implements a basic UDP server and client for sending and receiving ping messages.
Simulates 33% packet loss to evaluate network reliability.
- **TCP Server and Client:**: Similar functionality using TCP sockets, ensuring reliable message delivery.
Includes a concurrent server capable of handling multiple clients simultaneously.
- **RTT Calculation:**: Measures the time taken for messages to travel to the server and back, providing insights into network performance.
- **Packet Loss Monitoring:**: Tracks packet loss percentage, comparing theoretical calculations with actual results.

## Installation

### Prerequisites:
- Python 3.x
- Required Python libraries:
  - `socket`
  - `threading`
  - `json`
  - `BeautifulSoup4` (`bs4`)
  - `matplotlib`
  - Any additional libraries for translation (e.g., `googletrans`)

### Steps:
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd your-repository
   ```

2. Navigate to the project directory:
   ```bash
   cd Prg-Assignment-1-MyTCP/UDPPinger
   ```

3. Start the UDP Server:
   ```bash
   python3 UDPPingerServer.py
   ```

4. Start the UDP Client:
   ```bash
   python3 UDPPingerClient.py
   ```

5. Start the TCP Server:
   ```bash
   python3 TCPPingerServer.py
   ```

4. Start the TCP Client:
   ```bash
   python3 TCPPingerClient.py
   ```

## Simulating Packet Loss

```bash
   sudo tc qdisc add dev eth0 root netem loss 33%
   ```
