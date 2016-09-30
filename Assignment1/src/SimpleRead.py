import argparse


def get_bin_string_from_byte():
    res = ''
    for i in range(8):
        res += str((next_byte[0] >> (7 - i)) & 1)
    return res


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="input file")
    parser.add_argument("output_file", help="output file")
    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.output_file

    with open(input_file, 'rb') as inp:
        with open(output_file, 'w') as out:
            while True:
                next_byte = inp.read(1)
                if len(next_byte) == 0:
                    break
                bin_string = get_bin_string_from_byte()
                out.write(bin_string)
