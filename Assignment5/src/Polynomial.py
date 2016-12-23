from Utils import div_modulo


def _member(x):
    coefficient, exponent = x
    if exponent == 0:
        return str(coefficient)

    res = 'x'
    if coefficient > 1:
        res = str(coefficient) + res

    if exponent > 1:
        res = res + '^' + str(exponent)

    return res


def remove_trailing_zeros(res):
    last_non_zero_index = 0
    for index, val in enumerate(res):
        if val > 0:
            last_non_zero_index = index
    return res[:last_non_zero_index + 1]


class Polynomial:
    def __init__(self, coefficients=None, mod: int = 2):
        if coefficients is None:
            coefficients = []
        self.mod = mod
        self.coefficients = remove_trailing_zeros(list(map(lambda x: x % mod, coefficients)))

    def __str__(self):
        powers = [(c, i) for i, c in enumerate(self.coefficients)]
        filtered_powers = list(filter(lambda x: x[0] > 0, powers))
        if len(filtered_powers) == 0:
            return '0'
        res = map(lambda x: _member(x), filtered_powers)
        return ' + '.join(res)

    def __add__(self, other):
        self._check_type(other)

        new_coefficients = self._added_coefficients(other.coefficients)
        return Polynomial(new_coefficients, self.mod)

    def __sub__(self, other):
        self._check_type(other)

        return self + other * (-1)

    def _added_coefficients(self, coefficients):
        one = self.coefficients
        two = coefficients
        if len(one) < len(two):
            one, two = two, one
        res = one.copy()
        for index, value in enumerate(two):
            res[index] = (value + one[index]) % self.mod
        return remove_trailing_zeros(res)

    def __mul__(self, other):
        if type(other) == Polynomial:
            if other.mod != self.mod:
                raise ValueError("mod params must be the same")
            new_coefficients = self._multiplied_coefficients(other.coefficients)
        elif type(other) == int:
            new_coefficients = list(map(lambda x: (x * other) % self.mod, self.coefficients))
        else:
            raise TypeError("wrong type")
        removed_zeros = remove_trailing_zeros(new_coefficients)
        return Polynomial(removed_zeros, self.mod)

    def _multiplied_coefficients(self, coefficients):
        one = self.coefficients
        two = coefficients

        res_len = len(one) + len(two) - 1
        res = [0 for _ in range(res_len)]
        for exponent1, coefficient1 in enumerate(one):
            for exponent2, coefficient2 in enumerate(two):
                res[exponent1 + exponent2] += (coefficient1 * coefficient2)
                res[exponent1 + exponent2] %= self.mod

        return remove_trailing_zeros(res)

    def __truediv__(self, other):
        floor_div = self // other
        if str(self - floor_div * other) != '0':
            raise ValueError("does not divide")
        return floor_div

    def _check_type(self, other):
        if type(other) != Polynomial:
            raise TypeError("wrong type")
        if other.mod != self.mod:
            raise ValueError("mod params must be the same")

    def __floordiv__(self, other):
        if type(other) == int:
            res_coefficients = list(map(lambda x: div_modulo(x, other, self.mod), self.coefficients))
            return Polynomial(res_coefficients, self.mod)
        self._check_type(other)

        to_divide = Polynomial(self.coefficients.copy(), self.mod)
        res = Polynomial(mod=self.mod)
        while True:
            exponent_diff = len(to_divide.coefficients) - len(other.coefficients)
            if exponent_diff < 0:
                return res

            coefficients = [0 for _ in range(exponent_diff)]
            to_divide_coefficient = to_divide.coefficients[len(to_divide.coefficients) - 1]
            other_coefficient = other.coefficients[len(other.coefficients) - 1]
            num_coefficient = div_modulo(to_divide_coefficient, other_coefficient, to_divide.mod)
            coefficients.append(num_coefficient)

            p = Polynomial(coefficients, to_divide.mod)
            multiple = other * p
            to_divide -= multiple
            res += p

    def __mod__(self, other):
        self._check_type(other)
        div_res = self // other
        return self - div_res * other

    def get_code(self, code_length):
        code = [0 for _ in range(code_length)]
        for index, val in enumerate(self.coefficients):
            code[index] = val
        return code

    def degree(self):
        return len(self.coefficients) - 1

    def degree_coefficient(self):
        return self.coefficients[len(self.coefficients) - 1]

    def value_for_(self, x):
        res = 0
        for exponent, coefficient in enumerate(self.coefficients):
            res += (x ** exponent) * coefficient
        return res

    def copy(self):
        return Polynomial(self.coefficients.copy(), self.mod)

    def to_power(self, power):
        res = Polynomial([1], self.mod)
        for _ in range(power):
            res *= self
        return res

    def max_degree_equals(self):
        last_coefficient = self.coefficients[len(self.coefficients) - 1]
        new_coefficients = list(map(lambda x: -x, self.coefficients[:-1]))
        return Polynomial(new_coefficients, self.mod) / last_coefficient

    def components(self):
        for exponent, coefficient in enumerate(self.coefficients):
            if coefficient != 0:
                p = Polynomial.simple_power(exponent, self.mod)
                yield p * coefficient

    @classmethod
    def simple_power(cls, power, mod):
        coefficients = [0 for _ in range(power + 1)]
        coefficients[len(coefficients) - 1] = 1
        return Polynomial(coefficients, mod)
