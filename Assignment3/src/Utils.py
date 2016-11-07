import os
from math import log2
import argparse


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


def precision_str_from_float(num):
    res = "{:.7f}".format(num)
    return res


def parse_file_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="input file")
    parser.add_argument("output_file", help="output file")
    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.output_file
    return input_file, output_file


def parse_three_file_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("code_file", help="code file")
    parser.add_argument("input_file", help="input file")
    parser.add_argument("output_file", help="output file")
    args = parser.parse_args()
    code_file = args.code_file
    input_file = args.input_file
    output_file = args.output_file
    return code_file, input_file, output_file


def get_file_size_in_bytes(file_name):
    return os.path.getsize(file_name)


def get_log_len(num):
    return int(log2(num)) + 1


def get_bin_repr(num):
    res = bin(num)[2:]
    return res


def elias_gama_code(num):
    res = ''
    if num == 0:
        return res

    log_len = get_log_len(num)
    for i in range(log_len - 1):
        res += '0'
    res += '1'
    res += get_bin_repr(num)[1:]
    return res


if __name__ == '__main__':
    for i in range(10):
        print(elias_gama_code(i))