from collections import Counter
from Utils import parse_file_args, write_float_list,\
    get_distribution_list, get_one_gram_letters, get_bi_gram_letters


def split_grams(letter_distribution):
    one_gram = Counter()
    two_gram = Counter()
    for gram, count in letter_distribution.items():
        if len(gram) == 1:
            one_gram[gram] = count
        else:
            two_gram[gram] = count
    return one_gram, two_gram


def print_distribution_gram(letters, gram_count, out):
    distribution = get_distribution_list(gram_count, letters)
    write_float_list(distribution, out)


def print_distribution(letter_distribution, out):
    one_gram, two_gram = split_grams(letter_distribution)
    single_letters = get_one_gram_letters()
    print_distribution_gram(single_letters, one_gram, out)
    out.write('\n')
    two_letters = get_bi_gram_letters(single_letters)
    print_distribution_gram(two_letters, two_gram, out)


def print_distribution_to_file(letter_distribution, out_file):
    with open(out_file, 'w', encoding='UTF-8') as out:
        print_distribution(letter_distribution, out)


def count_line_distribution(line, last_letter=''):
    letter_counts = Counter()
    for ch in line:
        letter_counts[ch] += 1
        if last_letter is not None and last_letter != '':
            letter_counts[last_letter + ch] += 1
        last_letter = ch
    return letter_counts


def count_distribution(inp):
    letter_counts = Counter()
    last_letter = None
    for line in inp:
        line_letter_counts = count_line_distribution(line, last_letter)
        letter_counts += line_letter_counts
        last_letter = line[len(line) - 1]
    return letter_counts


def read_distribution(input_filename):
    with open(input_filename, 'r', encoding='UTF-8') as inp:
        return count_distribution(inp)


def main():
    inp, out = parse_file_args()
    letter_distribution = read_distribution(inp)
    print_distribution_to_file(letter_distribution, out)

if __name__ == '__main__':
    main()
