import argparse


def byte_from_bin_string(bin_string):
    res = 0
    for i in range(8):
        if bin_string[i] == '1':
            res += 1 << (7 - i)
    return res


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="input file")
    parser.add_argument("output_file", help="output file")
    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.output_file

    with open(input_file, 'rb') as inp:
        with open(output_file, 'wb') as out:
            while True:
                next_byte = inp.read(8).decode()
                if len(next_byte) == 8:
                    num = byte_from_bin_string(next_byte)
                    out.write(num.to_bytes(1, byteorder='big'))
                else:
                    if len(next_byte) == 0:
                        next_byte = '10000000'
                    else:
                        next_byte += '1'
                        for _ in range(8 - len(next_byte)):
                            next_byte += '0'
                    num = byte_from_bin_string(next_byte)
                    out.write(num.to_bytes(1, byteorder='big'))
                    break
