from Utils import read_int_lines, read_matrix_row, swap_values, vector_product


class Matrix:
    def __init__(self, num_rows: int, num_cols: int):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.values = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
        self.permutations = [i for i in range(self.num_cols)]

    def standard_form(self):
        for row_index in range(self.num_rows):
            if self.values[row_index][row_index] == 0:
                self.__standard_till_row(row_index)
            self.__make_below_zero(row_index)

        for row_index in range(self.num_rows):
            for col_index in range(self.num_rows):
                if row_index == col_index:
                    need_value = 1
                else:
                    need_value = 0
                if self.values[row_index][col_index] != need_value:
                    self.__xor_rows(row_index, col_index)

    def set_row(self, row_index: int, row_values: list):
        if len(row_values) != self.num_cols:
            raise ValueError("wrong row size")
        self.values[row_index] = row_values

    def __standard_till_row(self, row_index: int):
        if not self.__try_swiping_row(row_index):
            self.__swiping_col(row_index)

    def __try_swiping_row(self, row_index):
        for i in range(row_index + 1, self.num_rows):
            if self.values[i][row_index] == 1:
                self.__swipe_rows(row_index, i)
                return True
        return False

    def __swipe_rows(self, row_index1: int, row_index2: int):
        tmp = self.values[row_index1].copy()
        self.values[row_index1] = self.values[row_index2]
        self.values[row_index2] = tmp

    def __swiping_col(self, row_index: int):
        for cur_col in range(row_index + 1, self.num_cols):
            if self.values[row_index][cur_col] == 1:
                self.__swipe_cols(row_index, cur_col)
                swap_values(self.permutations, row_index, cur_col)
                return
        raise ValueError("Wrong matrix format")

    def __make_below_zero(self, row_index: int):
        for cur_row in range(row_index + 1, self.num_rows):
            if self.values[cur_row][row_index] != 0:
                self.__xor_rows(cur_row, row_index)

    def __swipe_cols(self, col_index_1: int, col_index_2: int):
        tmp = [self.values[i][col_index_1] for i in range(self.num_rows)]

        for i in range(self.num_rows):
            self.values[i][col_index_1] = self.values[i][col_index_2]

        for i in range(self.num_rows):
            self.values[i][col_index_2] = tmp[i]

    def __xor_rows(self, row_to_change, row_to_xor):
        for col in range(self.num_cols):
            val = self.values[row_to_change][col]
            self.values[row_to_change][col] = (val + self.values[row_to_xor][col]) % 2

    def clone(self):
        res = Matrix(self.num_rows, self.num_cols)
        for i in range(self.num_rows):
            res.set_row(i, self.values[i].copy())
        return res

    def write_to_buffer(self, out):
        out.write("{} {}\n".format(self.num_cols, self.num_rows))
        for row in self.values:
            for num in row:
                out.write(str(num))
            out.write("\n")

    def generate_parity_matrix(self):
        res = Matrix(num_rows=self.num_cols - self.num_rows, num_cols=self.num_cols)
        for row_index in range(self.num_rows):
            for col_index in range(self.num_rows, self.num_cols):
                val = self.values[row_index][col_index]
                res.values[col_index - self.num_rows][row_index] = val

        i = 0
        j = self.num_rows
        for _ in range(self.num_cols - self.num_rows):
            res.values[i][j] = 1
            i += 1
            j += 1

        res.__permute_cols(self.permutations)
        return res

    def times_vector(self, vector: list):
        if not len(vector) == self.num_cols:
            raise ValueError("bad vector size")
        return [vector_product(self.values[i], vector) for i in range(self.num_rows)]

    def __permute_cols(self, permutations: list):
        new_values = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        reverse_permutation = [0 for _ in range(len(permutations))]
        for index, num in enumerate(permutations):
            reverse_permutation[num] = index

        for j in range(self.num_cols):
            for i in range(self.num_rows):
                new_values[i][j] = self.values[i][reverse_permutation[j]]
        self.values = new_values


def read_matrix_from_file(inp):
    num_cols, num_rows = read_int_lines(inp)
    res = Matrix(num_rows=num_rows, num_cols=num_cols)
    for row_index in range(num_rows):
        res.set_row(row_index, read_matrix_row(inp))
    return res
