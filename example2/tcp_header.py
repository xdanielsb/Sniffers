class TCP_header():
    def __init__(header):
        tcph = unpack('!HHLLBBHHH' , tcp_header)
        
        self.source_port = tcph[0]
        self.dest_port = tcph[1]
        self.sequence_number = tcph[2]
        self.acknowledgement = tcph[3]
        self.data_offset = tcph[4]
        self.length = data_offset >> 4
        
