import argparse


geo_letters = ['ა', 'ბ', 'გ', 'დ', 'ე', 'ვ',
               'ზ', 'თ', 'ი', 'კ', 'ლ', 'მ',
               'ნ', 'ო', 'პ', 'ჟ', 'რ', 'ს',
               'ტ', 'უ', 'ფ', 'ქ', 'ღ', 'ყ',
               'შ', 'ჩ', 'ც', 'ძ', 'წ', 'ჭ',
               'ხ', 'ჯ', 'ჰ']


def precision_str_from_float(num):
    res = "{:.7f}".format(num)
    return res


def get_distribution_list(gram_count, letters):
    total = sum(gram_count.values())
    distribution = []
    for letter in letters:
        count = gram_count[letter]
        part = count / total
        distribution.append(part)
    return distribution


def write_float_list(distribution, out):
    for val in distribution[:-1]:
        str_value = precision_str_from_float(val)
        out.write(str_value + " ")
    out.write(precision_str_from_float(distribution[len(distribution) - 1]))


def write_string_list(str_list, out):
    out.write(str(str_list).replace(',', '').replace("'", "")[1:-1])


def get_bi_gram_letters(single_letters):
    two_letters = [ch1 + ch2 for ch1 in single_letters for ch2 in single_letters]
    return two_letters


def get_one_gram_letters():
    single_letters = sorted(geo_letters + [" "])
    return single_letters


def parse_file_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="input file")
    parser.add_argument("output_file", help="output file")
    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.output_file
    return input_file, output_file
