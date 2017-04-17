from functools import reduce


def mamdani(rules_output, defuzzy, functions):
    pass


def sugeno(rules_output):
    """
    Sugeno model with weighted average.
    :param rules_output:
    :return: 
    """
    num = {}
    den = {}

    for w, variable, z in rules_output:
        num[variable] = num.get(variable, 0) + w * z
        den[variable] = den.get(variable, 0) + w

    return _divide(num, den)


def tsukamoto(rules_output, functions, step=0.1):
    num = {}
    den = {}

    for w, variable, func in rules_output:
        def _best(x, y):
            return x if abs(x[1] - w) < abs(y[1] - w) else y

        func = functions[func]
        points = list(func.points(step))
        z = reduce(_best, points, points[0])[0]

        num[variable] = num.get(variable, 0) + w * z
        den[variable] = den.get(variable, 0) + w

    return _divide(num, den)


def _divide(num, den):
    results = {}
    for variable in num.keys():
        results[variable] = num[variable] / den[variable]
    return results
