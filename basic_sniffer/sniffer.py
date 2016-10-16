#Packet sniffer in python
#For Linux
 
import socket
 
#create an INET, raw socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
 
# receive a packet
while True:
  print s.recvfrom(65565)

#Note: This packets are received in form of hex
