def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def calculate(n1, n2, fun):
    return fun(n1, n2)


print(calculate(3, 2, multiply))
