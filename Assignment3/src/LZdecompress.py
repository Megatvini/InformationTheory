from Utils import parse_file_args, read_whole_buffer, read_elias_code
from CompleteIO import CompleteWriter


def decompress(input_buff, start_of_file, file_size):
    return 'NIKA'


def lz_decompress_buffers(input_buff, out_buff):
    bin_string_data = read_whole_buffer(input_buff)
    file_size, start_of_file = read_elias_code(bin_string_data)
    decompressed_data = decompress(bin_string_data, start_of_file, file_size)
    writer = CompleteWriter(file_descriptor=out_buff)
    writer.write_data(decompressed_data)
    writer.close_file()


def lz_decompress(input_file, output_file):
    with open(input_file, 'rb') as inp:
        with open(output_file, 'wb') as out:
            lz_decompress_buffers(inp, out)


def main():
    input_file, output_file = parse_file_args()
    lz_decompress(input_file, output_file)


if __name__ == '__main__':
    main()
