from Utils import parse_three_file_args, read_num_list
from Polynomial import Polynomial


def read_data(inp):
    return list(map(int, inp.readline().replace('\n', '').split()))


def main():
    pol_file, data_file, output_file = parse_three_file_args('pol', 'data', 'out')
    with open(pol_file, 'r') as pol:
        mod = int(pol.readline())
        code_length = int(pol.readline())
        coefficients = read_num_list(pol)
    generator = Polynomial(coefficients, mod)

    with open(data_file, 'r') as inp_data:
        data_len = int(inp_data.readline())
        data = read_num_list(inp_data)

    encoded = []
    data_index = 0
    chunk_length = code_length - generator.degree()
    while data_index < data_len:
        cur_data = data[data_index: data_index + chunk_length]
        encode_p = generator * Polynomial(cur_data, mod)
        encoded += encode_p.get_code(code_length)
        data_index += chunk_length

    with open(output_file, 'w') as out:
        res_len = len(encoded)
        out.write(str(res_len) + '\n')
        out.write(" ".join(map(str, encoded)) + '\n')


if __name__ == '__main__':
    main()
