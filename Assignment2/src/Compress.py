from CompleteWrite import CompleteWriter
from Utils import parse_three_file_args, read_encoding_map


def get_next_char(inp):
    one_byte = inp.read(1)
    value = int.from_bytes(one_byte, byteorder='big')
    if value == 32:
        return " "
    else:
        res = one_byte + inp.read(2)
        return res.decode(encoding='UTF-8')


def compress_data(inp, out, encoding_map):
    writer = CompleteWriter(file_descriptor=out)
    while True:
        next_msg = get_next_char(inp)
        if len(next_msg) == 0:
            break
        encoded_msg = encoding_map[next_msg]
        writer.write_data(encoded_msg)
    writer.close_file()


def compress_file(input_file, output_file, encoding_map):
    with open(input_file, 'rb') as inp:
        with open(output_file, 'wb') as out:
            compress_data(inp, out, encoding_map)


def main():
    code_file, input_file, output_file = parse_three_file_args()
    encoding_map = read_encoding_map(code_file)
    compress_file(input_file, output_file, encoding_map)

if __name__ == '__main__':
    main()