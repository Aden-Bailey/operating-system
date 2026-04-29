from scapy.all import sniff, IP, TCP, UDP

TCP_PORT = 8080
UDP_PORT = 8081

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        if TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport

            if src_port == TCP_PORT or dst_port == TCP_PORT:
                print("[DETECTED TCP PACKAGE]")
                print(f"Source IP: {src_ip}")
                print(f"Destination IP: {dst_ip}")
                print(f"Source Port: {src_port}")
                print(f"Destination Port: {dst_port}")
                print("-" * 40)

        elif UDP in packet:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

            if src_port == UDP_PORT or dst_port == UDP_PORT:
                print("[DETECTED UDP DATAGRAM]")
                print(f"Source IP: {src_ip}")
                print(f"Destination IP: {dst_ip}")
                print(f"Source Port: {src_port}")
                print(f"Destination Port: {dst_port}")
                print("-" * 40)

print("Starting packet sniffer...")
print("Listening for TCP port 8080 and UDP port 8081 traffic...")

sniff(
    iface="\\Device\\NPF_Loopback",
    filter="tcp port 8080 or udp port 8081",
    prn=packet_callback,
    store=False
)