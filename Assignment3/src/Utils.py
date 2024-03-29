import time
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


def get_bin_repr(num, res_len=None):
    res = bin(num)[2:]

    if res_len is not None:
        while len(res) < res_len:
            res = '0' + res

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


def read_elias_code(data):
    cur_index = 0
    num_len = 0
    while data[cur_index] != '1':
        cur_index += 1
        num_len += 1

    bin_string = '1' + data[cur_index + 1: cur_index + num_len + 1]
    res_num = int(bin_string, base=2)

    cur_index += num_len + 1

    return res_num, cur_index


def read_whole_buffer(inp_buffer):
    res = ''
    while True:
        next_byte = inp_buffer.read(1)
        if len(next_byte) == 0:
            break
        res += get_bin_string_from_byte(next_byte)
    return res


def time_fn(fn, args=None):
    start = time.time()
    fn() if args is None else fn(args)
    end = time.time()
    print('elapsed: {} sec'.format(round(end - start, 2)))
