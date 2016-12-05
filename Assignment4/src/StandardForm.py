from Matrix import Matrix, read_matrix_from_file
from Utils import parse_file_args


def write_res_to_file(matrix: Matrix, out):
    out.write("{} {}\n".format(matrix.num_cols, matrix.num_rows))
    for row in matrix.values:
        for num in row:
            out.write(str(num))
        out.write("\n")
    for num in matrix.permutations:
        out.write("{} ".format(num))


def main():
    input_file, output_file = parse_file_args()
    with open(input_file, 'r') as inp:
        matrix = read_matrix_from_file(inp)
    matrix.standard_form()
    with open(output_file, 'w') as out:
        write_res_to_file(matrix, out)

if __name__ == '__main__':
    main()
