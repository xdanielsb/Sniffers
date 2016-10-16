
import socket, sys
from ipv4_header import *
from tcp_header import *

"""
    Daniel Santos
    2016
    This class create the INET using socket raw and the protocol tcp
"""


class Controller:

    def __init__(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        except socket.error , msg:
            print 'The socket could not be created, the error was'  \
                    + str(msg[0]) + \
                    ' and the  Message  was' \
                    + msg[1]
            sys.exit()

    def listen(self):
        while True:
            packet = self.socket.recvfrom(65565)
            #Select the correct data
            packet = packet[0]
            ip_header = packet[0:20]
            
            #Instance the object for ipv4 header
            iph = IPv4_header(ip_header)
            iph.show()

            #Get the length of the ip header 
            iph_length = iph.get_size_header_ip()

            tcp_header = packet[iph_length:iph_length+20]
            #instance the object for tcp header
            tcph = TCP_header(tcp_header)
            tcph.show()

            #Print the data of the message
            h_size = iph.get_size_header_ip() + tcph.get_length() * 4
            data_size = len(packet) - h_size

            #get data from the packet

            data = packet[h_size:]
            print "Data: "
            print data
            print ""

            
if __name__ == "__main__":
    control = Controller ()
    control.listen()

