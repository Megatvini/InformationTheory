import argparse


def parse_file_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="input file")
    parser.add_argument("output_file", help="output file")
    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.output_file
    return input_file, output_file


def read_int_lines(inp_buffer):
    return list(map(int, inp_buffer.readline().replace("\n", "").split()))


def read_matrix_row(inp_buffer):
    line = inp_buffer.readline().replace("\n", "")
    return [int(ch) for ch in line]


def swap_values(data: list, index1: int, index2: int):
    tmp = data[index1]
    data[index1] = data[index2]
    data[index2] = tmp


def parse_three_file_args(arg1_name: str, arg2_name: str, arg3_name: str):
    parser = argparse.ArgumentParser()
    parser.add_argument("arg1", help=arg1_name)
    parser.add_argument("arg2", help=arg2_name)
    parser.add_argument("arg3", help=arg3_name)
    args = parser.parse_args()
    arg1 = args.arg1
    arg2 = args.arg2
    arg3 = args.arg3
    return arg1, arg2, arg3


def vector_product(one: list, two: list):
    if len(one) != len(two):
        raise ValueError()
    res = 0
    for i in range(len(one)):
        res += one[i] * two[i]
    return res


def byte_from_bin_string(bin_string):
    res = 0
    for i in range(8):
        if bin_string[i] == '1':
            res += 1 << (7 - i)
    return res


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


def read_whole_buffer(inp_buffer):
    res = ''
    while True:
        next_byte = inp_buffer.read(1)
        if len(next_byte) == 0:
            break
        res += get_bin_string_from_byte(next_byte)
    return res
