from Utils import parse_three_file_args, read_num_list
from Polynomial import Polynomial


def simplify(alpha, p, power_simplification_map, polynomial):
    if p.degree() in power_simplification_map:
        return power_simplification_map[p.degree()] * p.degree_coefficient()

    if p.degree() < polynomial.degree():
        return p

    if p.degree() == polynomial.degree():
        return polynomial.max_degree_equals() * p.degree_coefficient()

    divide = Polynomial.simple_power(polynomial.degree(), alpha.mod)
    last = simplify(alpha, p / divide, power_simplification_map, polynomial)
    cur = last * simplify(alpha, divide, power_simplification_map, polynomial)
    simplified = Polynomial(mod=alpha.mod)
    for c in cur.components():
        simplified += simplify(alpha, c, power_simplification_map, polynomial)

    return simplified


def calculate_polynomial_sum(mod, coefficients, power_simplification_map):
    res = Polynomial(mod=mod)
    for index, key in enumerate(sorted(power_simplification_map)):
        p = power_simplification_map[key]
        res += p * coefficients[index]
    return res


def find_polynomial(max_coefficient, power_simplification_map):
    coefficients = [0 for _ in range(len(power_simplification_map))]
    for _ in range(max_coefficient ** len(power_simplification_map) - 1):
        coefficients[0] += 1
        index = 0
        while coefficients[index] == max_coefficient:
            coefficients[index] = 0
            coefficients[index + 1] += 1
            index += 1
        candidate = calculate_polynomial_sum(max_coefficient, coefficients, power_simplification_map)
        if str(candidate) == '0':
            return Polynomial(coefficients, max_coefficient)


def find_minimal_polynomial(start_size, polynomial, alpha_power):
    power_simplification_map = {}
    alpha = Polynomial.simple_power(alpha_power, start_size)
    cur_power = 0
    while True:
        alpha_to_power = alpha.to_power(cur_power)
        simple = simplify(alpha, alpha_to_power, power_simplification_map, polynomial)
        power_simplification_map[alpha_to_power.degree()] = simple
        cur_power += 1
        res = find_polynomial(start_size, power_simplification_map)
        if res is not None:
            return res


def main():
    data_file, power_file, output_file = parse_three_file_args('data', 'power', 'output')
    with open(data_file, 'r') as data_inp:
        start_size = int(data_inp.readline())
        data_inp.readline()
        polynomial = Polynomial(read_num_list(data_inp), start_size)

    with open(power_file, 'r') as power_inp:
        alpha_power = int(power_inp.readline())

    minimal_polynomial = find_minimal_polynomial(start_size, polynomial, alpha_power)

    with open(output_file, 'w') as out:
        out.write('{}\n'.format(start_size))
        out.write('{}\n'.format(minimal_polynomial.degree()))
        out.write(' '.join(map(str, minimal_polynomial.coefficients)) + '\n')

if __name__ == '__main__':
    main()
