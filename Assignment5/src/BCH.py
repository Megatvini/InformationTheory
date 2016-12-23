from Utils import parse_three_file_args, read_num_list
from Polynomial import Polynomial
from MinimalPolynomial import find_minimal_polynomial


def find_lcm(polynomials, start_size):
    res = Polynomial([1], start_size)
    for p in polynomials:
        res *= p
    return res


def find_generator(start_size, primitive_polynomial, min_distance):
    polynomials = set()
    for i in range(min_distance - 1):
        min_polynomial = find_minimal_polynomial(start_size, primitive_polynomial, i + 1)
        polynomials.add(min_polynomial)

    lcm = find_lcm(polynomials, start_size)
    return lcm


def main():
    data_file, min_distance_file, output_file = parse_three_file_args('data', 'min_distance', 'output')
    with open(data_file, 'r') as data_inp:
        start_size = int(data_inp.readline())
        n = int(data_inp.readline())
        coefficients = read_num_list(data_inp)
        primitive_polynomial = Polynomial(coefficients, start_size)

    with open(min_distance_file, 'r') as inp:
        min_distance = int(inp.readline())

    generator = find_generator(start_size, primitive_polynomial, min_distance)

    with open(output_file, 'w') as out:
        out.write('{}\n'.format(start_size))
        res_len = start_size ** n - 1
        out.write('{}\n'.format(res_len))
        coefficients = generator.coefficients.copy()
        while len(coefficients) < res_len:
            coefficients.append(0)
        out.write(' '.join(map(str, coefficients)) + '\n')

if __name__ == '__main__':
    main()
