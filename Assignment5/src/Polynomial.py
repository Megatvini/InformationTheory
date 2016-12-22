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
    def __init__(self, coefficients: list, mod: int):
        self.mod = mod
        self.coefficients = list(map(lambda x: x % mod, coefficients))

    def __str__(self):
        powers = [(c, i) for i, c in enumerate(self.coefficients)]
        filtered_powers = list(filter(lambda x: x[0] > 0, powers))
        if len(filtered_powers) == 0:
            return '0'
        res = map(lambda x: _member(x), filtered_powers)
        return ' + '.join(res)

    def __add__(self, other):
        if type(other) != Polynomial:
            raise TypeError("wrong type")

        if other.mod != self.mod:
            raise ValueError("mod params must be the same")

        new_coefficients = self._added_coefficients(other.coefficients)
        return Polynomial(new_coefficients, self.mod)

    def __sub__(self, other):
        if type(other) != Polynomial:
            raise TypeError("wrong type")

        if other.mod != self.mod:
            raise ValueError("mod params must be the same")

        return self + other * (-1)

    def _added_coefficients(self, coefficients):
        one = self.coefficients
        two = coefficients
        if len(one) < len(two):
            one, two = two, one
        res = one.copy()
        for index, value in enumerate(two):
            res[index] = (value + one[index]) % self.mod
        return res

    def __mul__(self, other):
        if type(other) == Polynomial:
            if other.mod != self.mod:
                raise ValueError("mod params must be the same")
            new_coefficients = self._multiplied_coefficients(other.coefficients)
        elif type(other) == int:
            new_coefficients = list(map(lambda x: (x * other) % self.mod, self.coefficients))
        else:
            raise TypeError("wrong type")
        return Polynomial(remove_trailing_zeros(new_coefficients), self.mod)

    def _multiplied_coefficients(self, coefficients):
        one = self.coefficients
        two = coefficients

        res_len = len(one) + len(two)
        res = [0 for _ in range(res_len)]
        for exponent1, coefficient1 in enumerate(one):
            for exponent2, coefficient2 in enumerate(two):
                res[exponent1 + exponent2] += (coefficient1 * coefficient2)
                res[exponent1 + exponent2] %= self.mod

        return remove_trailing_zeros(res)

    def __truediv__(self, other):
        pass

    def __floordiv__(self, other):
        pass
