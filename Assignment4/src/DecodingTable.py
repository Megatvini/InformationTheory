import pickle
from itertools import combinations
from Utils import parse_three_file_args
from Matrix import Matrix, read_matrix_from_file


def generate_errors(message_length, num_errors):
    lst = [i for i in range(message_length)]
    for comb in combinations(lst, r=num_errors):
        res = [0 for _ in range(message_length)]
        for index in comb:
            res[index] = 1
        yield res


def save_deciding_data(matrix: Matrix, max_errors: int, out):
    matrix.standard_form()
    check_matrix = matrix.generate_parity_matrix()
    lookup_table = {}
    message_length = matrix.num_cols
    for num_errors in range(1, max_errors + 1):
        for e in generate_errors(message_length, num_errors):
            product = check_matrix.times_vector(e)
            lookup_table[str(product)] = e

    data = {"check_matrix": check_matrix, "lookup_table": lookup_table}
    pickle.dump(data, out)


def main():
    generator_file, num_file, output_file = parse_three_file_args()

    with open(generator_file, 'r') as inp:
        matrix = read_matrix_from_file(inp)

    with open(num_file, 'r') as inp:
        max_errors = int(inp.readline())

    with open(output_file, 'wb') as out:
        save_deciding_data(matrix, max_errors, out)


if __name__ == '__main__':
    main()
