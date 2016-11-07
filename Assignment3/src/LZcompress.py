from Utils import parse_file_args, get_file_size_in_bytes, elias_gama_code
from CompleteIO import CompleteWriter


def write_file_size(input_size, writer):
    gama_code = elias_gama_code(input_size)
    writer.write_data(gama_code)


def write_compressed_data(inp_buffer, writer):
    pass


def lz_compress_buffers(input_size, inp_buffer, out_buffer):
    writer = CompleteWriter(file_descriptor=out_buffer)
    write_file_size(input_size, writer)
    write_compressed_data(inp_buffer, writer)
    writer.close_file()


def lz_compress(input_file, output_file):
    input_size = get_file_size_in_bytes(input_file)
    with open(input_file, 'rb') as inp:
        with open(output_file, 'wb') as out:
            lz_compress_buffers(input_size, inp, out)


def main():
    input_file, output_file = parse_file_args()
    lz_compress(input_file, output_file)

if __name__ == '__main__':
    main()
