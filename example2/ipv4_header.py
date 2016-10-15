import socket
from struct import *


class IPv4_header:


    def __init__ (self, header):
        iph = unpack('!BBHHHBBH4s4s' , header)
        
        self.version = iph[0] >> 4
        self.ihl = iph [0] & 0xF
        self.ttl = iph[5]
        self.protocol = iph[6]

        self.iph_length = self.ihl * 4
        self.source_address = socket.inet_ntoa(iph[8]);
        self.dest_address = socket.inet_ntoa(iph[9]);

    def show(self):
        print   " Version: " + str(self.version) + \
                ", ihl: " + str(self.ihl) +  \
                ", ttl: " + str(self.ttl) + \
                ", protocol: " + str(self.protocol) + \
                ", length: " + str(self.iph_length) +  \
                ", source_address: " + str(self.source_address) + \
                ", dest address: " + str(self.source_address) 


    def get_version(self):
        return self.version

    def get_ihl(self):
        return self.ihl

    def get_ttl(self):
        return self.ttl
    
    def get_protocol(self):
        return self.protocol

    def get_source_address(self):
        return self.source_address

    def get_dest_address(self):
        return self.dest_address

    def get_size_header_ip(self):
        return self.iph_length
    
    



    
