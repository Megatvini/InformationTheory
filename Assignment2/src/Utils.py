import argparse


def byte_from_bin_string(bin_string):
    res = 0
    for i in range(8):
        if bin_string[i] == '1':
            res += 1 << (7 - i)
    return res


def read_decoding_map(code_file):
    encoding_map = read_encoding_map(code_file)
    res = {}
    for k, v in encoding_map.items():
        res[v] = k
    return res


def read_encoding_map(code_file):
    all_letters = get_one_gram_letters()
    codes_list = read_code_list(code_file)
    encoding_map = dict(zip(all_letters, codes_list))
    return encoding_map


def read_code_list(code_file):
    with open(code_file, 'r', encoding='UTF-8') as inp:
        return get_code_list(inp)


def get_code_list(inp):
    res = []
    for line in inp:
        res.append(line.replace('\n', ''))
    return res


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


def write_float_list(distribution, out, delimiter=" "):
    for val in distribution[:-1]:
        str_value = precision_str_from_float(val)
        out.write(str_value + delimiter)
    out.write(precision_str_from_float(distribution[len(distribution) - 1]))


def write_string_list(str_list, out, delimiter=" "):
    for elem in str_list[:-1]:
        out.write(elem + delimiter)
    out.write(str_list[len(str_list) - 1])


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


def parse_three_file_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("code_file", help="code file")
    parser.add_argument("input_file", help="input file")
    parser.add_argument("output_file", help="output file")
    args = parser.parse_args()
    code_file = args.code_file
    input_file = args.input_file
    output_file = args.output_file
    return code_file, input_file, output_file
