from Utils import parse_three_file_args, read_whole_buffer
from Matrix import Matrix, read_matrix_from_file
from CompleteIO import CompleteWriter


def write_encoded_data(matrix: Matrix, inp: str, out):
    writer = CompleteWriter(file_descriptor=out)
    read_index = 0
    read_len = matrix.num_rows
    while read_index < len(inp):
        next_chunk = inp[read_index: read_index + read_len]
        encoded = matrix.encode(next_chunk)
        writer.write_data(encoded)
        read_index += read_len
    writer.close_file()


def main():
    generator_file, input_file, output_file = parse_three_file_args(
        'generator matrix file name',
        'input file name',
        'output file name'
    )

    with open(generator_file, 'r') as inp:
        matrix = read_matrix_from_file(inp)

    with open(input_file, 'rb') as inp:
        input_bin_string = read_whole_buffer(inp)

    with open(output_file, 'wb') as out:
        write_encoded_data(matrix, input_bin_string, out)

if __name__ == '__main__':
    main()
