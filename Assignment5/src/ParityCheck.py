from Utils import parse_file_args
from Polynomial import Polynomial


def write_res(polynomial, code_length, out):
    big_coefficients = [0 for _ in range(code_length + 1)]
    big_coefficients[0] = -1
    big_coefficients[len(big_coefficients) - 1] = 1
    big_polynomial = Polynomial(big_coefficients, polynomial.mod)
    remainder = big_polynomial % polynomial
    if str(remainder) == '0':
        out.write('YES\n')
        checker = big_polynomial / polynomial
        coefficients = [0 for _ in range(code_length)]
        for index, val in enumerate(checker.coefficients):
            coefficients[index] = val
        out.write(" ".join(map(str, coefficients)) + '\n')
    else:
        out.write('NO\n')


def main():
    input_file, output_file = parse_file_args()
    with open(input_file, 'r') as inp:
        mod = int(inp.readline())
        code_length = int(inp.readline())
        coefficients = list(map(int, inp.readline().replace('\n', '').split()))
    polynomial = Polynomial(coefficients, mod)
    with open(output_file, 'w') as out:
        write_res(polynomial, code_length, out)

if __name__ == '__main__':
    main()
