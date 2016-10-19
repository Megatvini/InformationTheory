from collections import Counter
from Utils import parse_file_args


def split_grams(letter_distribution):
    one_gram = Counter()
    two_gram = Counter()
    for gram, count in letter_distribution.items():
        if len(gram) == 1:
            one_gram[gram] = count
        else:
            two_gram[gram] = count
    return one_gram, two_gram


geo_letters = ['ა', 'ბ', 'გ', 'დ', 'ე', 'ვ',
               'ზ', 'თ', 'ი', 'კ', 'ლ', 'მ',
               'ნ', 'ო', 'პ', 'ჟ', 'რ', 'ს',
               'ტ', 'უ', 'ფ', 'ქ', 'ღ', 'ყ',
               'შ', 'ჩ', 'ც', 'ძ', 'წ', 'ჭ',
               'ხ', 'ჯ', 'ჰ']


def print_distribution_list(distribution, out):
    for val in distribution[:-1]:
        str_value = "{:.7f}".format(val)
        out.write(str_value + " ")
    out.write("{:.7f}".format((distribution[len(distribution) - 1])))


def print_distribution_gram(letters, gram_count, out):
    total = sum(gram_count.values())
    distribution = []
    for letter in letters:
        count = gram_count[letter]
        part = count/total
        distribution.append(part)
    print_distribution_list(distribution, out)


def print_distribution(letter_distribution, out):
    one_gram, two_gram = split_grams(letter_distribution)
    single_letters = sorted(geo_letters + [" "])
    print_distribution_gram(single_letters, one_gram, out)
    out.write('\n')
    two_letters = [ch1 + ch2 for ch1 in single_letters for ch2 in single_letters]
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
