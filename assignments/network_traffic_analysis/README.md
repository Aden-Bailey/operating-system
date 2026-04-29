## Language Used

Python 3.13


## Libraries

* socket (built-in)
* scapy


## Requirements (Windows)

* Install Npcap (for packet sniffing)
* Run terminal or VS Code as Administrator


## Files

* tcp_server.py → TCP server (port 8080)
* tcp_client.py → TCP client (sends "TCP_TEST_PACKET")
* udp_server.py → UDP server (port 8081)
* udp_client.py → UDP client (sends "UDP_TEST_DATAGRAM")
* sniffer.py → Packet sniffer


## Network Interface Used

The sniffer uses: \Device\NPF_Loopback
This captures traffic on localhost (127.0.0.1).


## How to Run

### 1. Start Sniffer

python sniffer.py

### 2. Run TCP Test

Terminal 2:
python tcp_server.py

Terminal 3:
python tcp_client.py

Expected:

* Client sends TCP_TEST_PACKET
* Server replies with ACK
* Sniffer shows [DETECTED TCP PACKAGE]

### 3. Run UDP Test

Terminal 2:
python udp_server.py

Terminal 3:
python udp_client.py

Expected:

* Client sends UDP_TEST_DATAGRAM
* Server receives it
* Sniffer shows [DETECTED UDP DATAGRAM]


## Notes

* Run as Administrator for packet sniffing
* Sniffer filters ports 8080 (TCP) and 8081 (UDP)
* Multiple TCP packets may appear (normal behavior)
