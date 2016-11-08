from Utils import parse_file_args, read_whole_buffer, \
    read_elias_code, get_bin_repr, time_fn
from CompleteIO import SimpleWriter


def update_dic(dic, code_int):
    dic[len(dic)] = dic[code_int] + '1'
    dic[code_int] += '0'


def decompress(bin_string_data, start_of_file, file_size):
    res = ''
    dic = {0: '0', 1: '1'}
    cur_index = start_of_file
    cur_len = 1
    while len(res) < file_size * 8:
        code = bin_string_data[cur_index: cur_index + cur_len]
        code_int = int(code, base=2)
        res += dic[code_int]
        update_dic(dic, code_int)
        cur_index += cur_len
        cur_len = len(get_bin_repr(len(dic) - 1))

    return res


def lz_decompress_buffers(input_buff, out_buff):
    bin_string_data = read_whole_buffer(input_buff)
    file_size, start_of_file = read_elias_code(bin_string_data)
    decompressed_data = decompress(bin_string_data, start_of_file, file_size)
    writer = SimpleWriter(file_descriptor=out_buff)
    writer.write_data(decompressed_data)
    writer.close_file()


def lz_decompress(input_file, output_file):
    with open(input_file, 'rb') as inp:
        with open(output_file, 'wb') as out:
            lz_decompress_buffers(inp, out)


def main():
    input_file, output_file = parse_file_args()
    lz_decompress(input_file, output_file)


if __name__ == '__main__':
    time_fn(main)
