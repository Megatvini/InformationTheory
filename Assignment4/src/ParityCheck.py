from Utils import parse_file_args
from Matrix import read_matrix_from_file


def main():
    input_file, output_file = parse_file_args()
    with open(input_file, 'r') as inp:
        matrix = read_matrix_from_file(inp)
    matrix.standard_form()
    check_matrix = matrix.generate_parity_matrix()
    with open(output_file, 'w') as out:
        check_matrix.write_to_buffer(out)

if __name__ == '__main__':
    main()
