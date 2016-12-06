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


def parse_three_file_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("generator_matrix", help="generator matrix file name")
    parser.add_argument("num", help="num file name")
    parser.add_argument("output", help="output file name")
    args = parser.parse_args()
    matrix_file = args.generator_matrix
    input_file = args.num
    output_file = args.output
    return matrix_file, input_file, output_file


def vector_product(one: list, two: list):
    if len(one) != len(two):
        raise ValueError()
    res = 0
    for i in range(len(one)):
        res += one[i] * two[i]
    return res
