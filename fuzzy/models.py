from functools import reduce
from itertools import groupby

from .functions import Compose


def mamdani(rules_output, defuzzy, functions):
    rules_output.sort(key=lambda r: r[1])
    result = {}

    for k, g in groupby(rules_output, lambda r: r[1]):
        aggr_func = map(
            lambda ro: (ro[0], functions[ro[2]]),
            rules_output)
        compose = Compose(list(aggr_func))
        result[k] = defuzzy(compose)

    return result


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
        func = functions[func]
        points = list(func.points(step))
        z = reduce(
            lambda x, y: x if abs(x[1] - w) < abs(y[1] - w) else y,
            points,
            points[0])[0]

        num[variable] = num.get(variable, 0) + w * z
        den[variable] = den.get(variable, 0) + w

    return _divide(num, den)


def _divide(num, den):
    results = {}
    for variable in num.keys():
        results[variable] = num[variable] / den[variable]
    return results
