from Utils import parse_file_args, write_string_list,\
    precision_str_from_float, write_float_list


def read_input(inp):
    n_messages = int(inp.readline())
    probabilities = [float(x) for x in inp.readline().split(" ")]
    return n_messages, probabilities


def read_file_input(input_file):
    with open(input_file, 'r', encoding='UTF-8') as inp:
        return read_input(inp)


def generate_huffman_codes(probabilities):
    names = []
    for index, prob in enumerate(probabilities):
        names.append((prob, None, None, index))

    while len(names) > 1:
        names = sorted(names, key=lambda x: x[0], reverse=True)
        one = names.pop()
        two = names.pop()
        names.append((one[0] + two[0], one, two, None))
    return names


def find_index(index, cur_node):
    if cur_node is None:
        return None

    if cur_node[3] == index:
        return ""

    left_road = find_index(index, cur_node[1])
    if left_road is not None:
        return left_road + "1"

    right_road = find_index(index, cur_node[2])
    if right_road is not None:
        return right_road + "0"


def get_huffman_code(index, code_words):
    res = ""
    res += find_index(index, code_words[0])
    return res


def get_codes_list(n_words, code_words):
    res = []
    for i in range(n_words):
        word_code = get_huffman_code(i, code_words)
        res.append(word_code)
    return res


def write_huffman_codes(n_words, code_words, probabilities, out):
    mean_length = calculate_mean_length(code_words, probabilities)
    out.write(precision_str_from_float(mean_length) + '\n')
    code_list = get_codes_list(n_words, code_words)
    write_string_list(code_list, out)
    out.write('\n')
    write_float_list(probabilities, out)


def write_codes_to_file(n_words, code_words, probabilities, output_file):
    with open(output_file, 'w', encoding='UTF-8') as out:
        write_huffman_codes(n_words, code_words, probabilities, out)


def calculate_mean_length(code_words, probabilities):
    products = []
    for index, word in enumerate(code_words):
        products.append(len(word) * probabilities[index])
    return sum(products)/len(products)


def main():
    input_file, output_file = parse_file_args()
    n_words, probabilities = read_file_input(input_file)
    code_words = generate_huffman_codes(probabilities)
    write_codes_to_file(n_words, code_words, probabilities, output_file)

if __name__ == '__main__':
    main()
