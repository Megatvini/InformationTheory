from math import ceil, log2
from Utils import parse_file_args, get_file_size_in_bytes,\
    elias_gama_code, get_bin_repr, read_whole_buffer, time_fn
from CompleteIO import CompleteWriter


def write_file_size(input_size, writer):
    gama_code = elias_gama_code(input_size)
    writer.write_data(gama_code)


def get_code(cur_buffer, dic):
    num = dic[cur_buffer]
    res_len = int(ceil(log2(len(dic))))
    bin_code = get_bin_repr(num, res_len)
    return bin_code


def update_dic(cur_word, dic):
    dic[cur_word + '0'] = dic[cur_word]
    dic.pop(cur_word)
    dic[cur_word + '1'] = len(dic)


def compress(data):
    res = ''
    dic = {'0': 0, '1': 1}
    cur_buffer = ''
    for ch in data:
        cur_buffer += ch
        if cur_buffer in dic:
            res += get_code(cur_buffer, dic)
            update_dic(cur_buffer, dic)
            cur_buffer = ''

    if cur_buffer != '':
        while cur_buffer not in dic:
            cur_buffer += '0'
        res += get_code(cur_buffer, dic)

    return res


def write_compressed_data(inp_buffer, writer):
    data = read_whole_buffer(inp_buffer)
    compressed_data = compress(data)
    writer.write_data(compressed_data)


def lz_compress_buffers(input_size, inp_buffer, out_buffer):
    writer = CompleteWriter(file_descriptor=out_buffer)
    write_file_size(input_size, writer)
    write_compressed_data(inp_buffer, writer)
    writer.close_file()


def lz_compress(input_file, output_file):
    input_size = get_file_size_in_bytes(input_file)
    with open(input_file, 'rb') as inp:
        with open(output_file, 'wb') as out:
            lz_compress_buffers(input_size, inp, out)


def main():
    input_file, output_file = parse_file_args()
    lz_compress(input_file, output_file)

if __name__ == '__main__':
    time_fn(main)
