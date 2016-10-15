from struct import *

class TCP_header():
    def __init__(self, header):
        tcph = unpack('!HHLLBBHHH' , header)
        
        self.source_port = tcph[0]
        self.dest_port = tcph[1]
        self.sequence_number = tcph[2]
        self.acknowledgement = tcph[3]
        self.data_offset = tcph[4]
        self.length = self.data_offset >> 4

    def get_source_port(self):
        return self.source_port

    def get_dest_port(self):
        return self.dest_port

    def get_sequence_number(self):
        return self.sequence_number

    def get_acknowledgement(self):
        return self.acknowledgement

    def get_data_offset(self):
        return self.get_data_offset

    def get_length(self):
        return self.length

        
