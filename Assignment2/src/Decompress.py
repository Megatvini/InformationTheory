from Utils import parse_three_file_args, read_decoding_map
from CompleteIO import CompleteReader


def decompress_data(inp, out, decoding_map):
    reader = CompleteReader(decoding_map, file_descriptor=out)
    while True:
        byte = inp.read(1)
        if len(byte) == 0:
            break
        reader.add_byte(byte)
    reader.close_file()


def decompress_file(input_file, output_file, decoding_map):
    with open(input_file, 'rb') as inp:
        with open(output_file, 'w', encoding='UTF-8') as out:
            decompress_data(inp, out, decoding_map)


def main():
    code_file, input_file, output_file = parse_three_file_args()
    decoding_map = read_decoding_map(code_file)
    decompress_file(input_file, output_file, decoding_map)

if __name__ == '__main__':
    main()
