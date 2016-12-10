from Matrix import Matrix, read_matrix_from_file
from Utils import parse_file_args


def write_res_to_file(matrix: Matrix, out):
    matrix.write_to_buffer(out)
    for num in matrix.get_reverse_permutations():
        out.write("{} ".format(num + 1))


def main():
    input_file, output_file = parse_file_args()
    with open(input_file, 'r') as inp:
        matrix = read_matrix_from_file(inp)
    matrix.standard_form()
    with open(output_file, 'w') as out:
        write_res_to_file(matrix, out)

if __name__ == '__main__':
    main()
