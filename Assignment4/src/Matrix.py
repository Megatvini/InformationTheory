from Utils import read_int_lines, read_matrix_row, swap_values


class Matrix:
    def __init__(self, num_rows: int, num_cols: int):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.values = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
        self.permutations = [i + 1 for i in range(self.num_cols)]

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


def read_matrix_from_file(inp):
    num_cols, num_rows = read_int_lines(inp)
    res = Matrix(num_rows=num_rows, num_cols=num_cols)
    for row_index in range(num_rows):
        res.set_row(row_index, read_matrix_row(inp))
    return res
