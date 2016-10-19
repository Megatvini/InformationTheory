from math import log2
from Utils import parse_file_args, precision_str_from_float
from Distrib import read_distribution, split_grams,\
    get_distribution_list, get_bi_gram_letters, get_one_gram_letters


def write_entropy_gram(gram_counts, letters, out):
    distribution_list = get_distribution_list(gram_counts, letters)
    entropy_list = [x*log2(x) if x > 0 else 0 for x in distribution_list]
    entropy = -sum(entropy_list)
    out.write(precision_str_from_float(entropy))


def write_conditional_entropy(one_gram, two_grams, out):
    pass


def write_entropy(letter_distribution, out):
    one_gram_counts, two_gram_counts = split_grams(letter_distribution)
    all_letters = get_one_gram_letters()
    write_entropy_gram(one_gram_counts, all_letters, out)
    out.write('\n')
    all_bi_gram_letters = get_bi_gram_letters(all_letters)
    write_entropy_gram(two_gram_counts, all_bi_gram_letters, out)
    out.write('\n')
    write_conditional_entropy(one_gram_counts, two_gram_counts, out)


def write_entropy_to_file(letter_distribution, output_file):
    with open(output_file, 'w', encoding='UTF-8') as out:
        write_entropy(letter_distribution, out)


def main():
    input_file, output_file = parse_file_args()
    letter_distribution = read_distribution(input_file)
    write_entropy_to_file(letter_distribution, output_file)

if __name__ == '__main__':
    main()
