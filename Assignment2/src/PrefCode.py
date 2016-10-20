from Utils import parse_file_args, write_string_list


def read_word_lengths(input_file):
    with open(input_file, 'r', encoding='UTF-8') as inp:
        return [int(x) for x in inp.readline().split(" ")]


def count_craft_sum(word_lengths, base):
    res = 0
    for word_length in word_lengths:
        res += base ** (-word_length)
    return res


def holds_craft_inequality(word_lengths):
    craft_sum = count_craft_sum(word_lengths, 2)
    return craft_sum <= 1


def add_bit(word):
    num = int(word, base=2)
    res = str(bin(num + 1))[2:]
    if len(res) > len(word):
        raise ValueError("Encountered bad word {} when adding bit".format(word))
    while len(res) < len(word):
        res = '0' + res
    return res


def generate_new_word(word_length, last_used_word):
    res = ''
    if last_used_word is not None:
        res = add_bit(last_used_word)
    while len(res) < word_length:
        res += '0'
    return res


def generate_code_words(word_lengths):
    word_lengths = sorted(word_lengths)
    res = []
    last_used_word = None
    for word_length in word_lengths:
        new_word = generate_new_word(word_length, last_used_word)
        res.append(new_word)
        last_used_word = new_word
    return res


def align_lengths(code_words, word_lengths):
    words_map = generate_length_map(code_words)
    res = []
    for word_length in word_lengths:
        res.append(words_map[word_length].pop())
    return res


def generate_length_map(code_words):
    words_map = {}
    for code_word in code_words:
        word_len = len(code_word)
        words_list = words_map.get(word_len, [])
        words_list.append(code_word)
        words_map[word_len] = words_list

    for k, v in words_map.items():
        words_map[k] = sorted(v, reverse=True)
    return words_map


def write_code_words(word_lengths, out):
    if not holds_craft_inequality(word_lengths):
        return
    code_words = generate_code_words(word_lengths)
    ordered_code_words = align_lengths(code_words, word_lengths)
    write_string_list(ordered_code_words, out, delimiter='\n')


def write_code_words_to_file(word_lengths, output_file):
    with open(output_file, 'w', encoding='UTF-8') as out:
        write_code_words(word_lengths, out)


def main():
    input_file, output_file = parse_file_args()
    word_lengths = read_word_lengths(input_file)
    write_code_words_to_file(word_lengths, output_file)

if __name__ == '__main__':
    main()
