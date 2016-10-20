from Utils import byte_from_bin_string, get_bin_string_from_byte, get_bin_string_from_last_byte


class CompleteWriter:
    def __init__(self, file_name=None, file_descriptor=None):
        if file_name is not None and file_descriptor is None:
            self.file_descriptor = open(file_name, 'wb')
        else:
            self.file_descriptor = file_descriptor
        self.bin_string_buffer = ''
        self.last_byte_string = ''

    def close_file(self):
        last_byte_string = self.last_byte_string
        if len(last_byte_string) == 8:
            num = byte_from_bin_string(last_byte_string)
        else:
            if len(last_byte_string) == 0:
                last_byte_string = '10000000'
            else:
                last_byte_string += '1'
                for _ in range(8 - len(last_byte_string)):
                    last_byte_string += '0'
            num = byte_from_bin_string(last_byte_string)
        self.file_descriptor.write(num.to_bytes(1, byteorder='big'))
        self.file_descriptor.close()

    def write_data(self, bin_string):
        self.bin_string_buffer += bin_string
        self.check_flush()

    def check_flush(self):
        while len(self.bin_string_buffer) >= 8:
            next_byte_string = self.bin_string_buffer[:8]
            data_to_flush = byte_from_bin_string(next_byte_string)
            byte = data_to_flush.to_bytes(1, byteorder='big')
            self.file_descriptor.write(byte)
            self.bin_string_buffer = self.bin_string_buffer[8:]
        self.last_byte_string = self.bin_string_buffer


class CompleteReader:
    def __init__(self,  decoding_map, file_name=None, file_descriptor=None,):
        if file_name is not None and file_descriptor is None:
            self.file_descriptor = open(file_name, 'wb')
        else:
            self.file_descriptor = file_descriptor
        self.input_buffer = ''
        self.last_byte = None
        self.decoding_map = decoding_map

    def add_byte(self, byte):
        if self.last_byte is not None:
            self.input_buffer += get_bin_string_from_byte(self.last_byte)
        self.last_byte = byte
        self.flush()

    def flush(self):
        while True:
            decoded = False
            for bin_str_code in sorted(self.decoding_map.keys()):
                if self.try_decode(bin_str_code):
                    decoded = True
            if not decoded:
                break

    def try_decode(self, bin_str_code):
        if self.input_buffer.startswith(bin_str_code):
            character = self.decoding_map[bin_str_code]
            self.input_buffer = self.input_buffer[len(bin_str_code):]
            self.file_descriptor.write(character)
            return True
        return False

    def close_file(self):
        self.input_buffer += get_bin_string_from_last_byte(self.last_byte)
        self.flush()
        self.file_descriptor.close()
