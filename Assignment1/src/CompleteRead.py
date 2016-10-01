import argparse


def get_bin_string_from_byte(byte):
    res = ''
    for i in range(8):
        res += str((byte[0] >> (7 - i)) & 1)
    return res


def get_bin_string_from_last_byte(byte):
    res = get_bin_string_from_byte(byte)
    index = len(res) - 1
    while res[index] == '0':
        index -= 1
    return res[0:index]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="input file")
    parser.add_argument("output_file", help="output file")
    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.output_file

    with open(input_file, 'rb') as inp:
        with open(output_file, 'w') as out:
            last_byte = inp.read(1)
            while True:
                next_byte = inp.read(1)
                if len(next_byte) == 0:
                    bin_string = get_bin_string_from_last_byte(last_byte)
                    if len(bin_string) > 0:
                        out.write(bin_string)
                    break
                bin_string = get_bin_string_from_byte(last_byte)
                out.write(bin_string)
                last_byte = next_byte
