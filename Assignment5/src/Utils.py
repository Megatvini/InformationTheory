import argparse


def parse_file_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="input file")
    parser.add_argument("output_file", help="output file")
    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.output_file
    return input_file, output_file


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


def div_modulo(a, b, p):
    return (b ** (p - 2) * a) % p


def read_num_list(inp_buffer):
    return list(map(int, inp_buffer.readline().replace('\n', '').split()))
