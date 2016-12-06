import pickle
from Utils import parse_three_file_args, read_whole_buffer
from Matrix import Matrix
from CompleteIO import CompleteWriter


def write_decoded_data(check_matrix: Matrix, lookup_table: dict, input_bin_string: str, out):
    writer = CompleteWriter(file_descriptor=out)
    read_index = 0
    read_len = check_matrix.num_cols
    while read_index < len(input_bin_string):
        cur_chunk = input_bin_string[read_index: read_index + read_len]
        read_index += read_len
        decoded = check_matrix.decode(cur_chunk, lookup_table)
        writer.write_data(decoded)
    writer.close_file()


def main():
    support_file, input_file, output_file = parse_three_file_args(
        'support file name',
        'input file name',
        'output file name'
    )

    with open(support_file, 'rb') as inp:
        support_data = pickle.load(inp)

    check_matrix = support_data['check_matrix']
    lookup_table = support_data['lookup_table']

    with open(input_file, 'rb') as inp:
        input_bin_string = read_whole_buffer(inp)
        input_bin_string = input_bin_string[:input_bin_string.rfind('1')]

    with open(output_file, 'wb') as out:
        write_decoded_data(check_matrix, lookup_table, input_bin_string, out)

if __name__ == '__main__':
    main()
