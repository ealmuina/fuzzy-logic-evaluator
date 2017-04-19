from functools import reduce
from itertools import groupby

from .functions import Compose


def mamdani(rules_output, defuzzy, functions, step=0.1):
    """
    Mamdani model
    :param rules_output: List of tuples (w, outputVar, linguisticVal) representing the output of each rule's evaluation
    :param defuzzy: Defuzzification function
    :param functions: Dictionary which associates a linguistic value with its corresponding membership function
    :param step: Distance between values to discretize function's domains
    :return: Dictionary that associates each output variable name with its calculated numeric value
    """
    rules_output.sort(key=lambda r: r[1])
    result = {}

    for var_name, var_rules in groupby(rules_output, lambda r: r[1]):  # group rules_output by the output variables
        aggr_func = map(
            lambda ro: (ro[0], functions[ro[2]]),
            var_rules)  # List of tuples (trunc, function) which corresponds to variable 'var_name'
        compose = Compose(list(aggr_func))
        result[var_name] = defuzzy(compose, step)  # Defuzzify and store result corresponding to variable 'var_name'

    return result


def sugeno(rules_output):
    """
    Sugeno model with weighted average
    :param rules_output: List of tuples (w, outputVar, z) representing the output of each rule's evaluation
    :return: Dictionary that associates each output variable name with its calculated numeric value
    """
    num = {}
    den = {}

    for w, variable, z in rules_output:
        num[variable] = num.get(variable, 0) + w * z
        den[variable] = den.get(variable, 0) + w

    return _divide(num, den)


def tsukamoto(rules_output, functions, step=0.1):
    """
    Tsukamoto model
    :param rules_output: List of tuples (w, outputVar, linguisticVal) representing the output of each rule's evaluation
    :param functions: Dictionary which associates a linguistic value with its corresponding membership function
    :param step: Distance between values to discretize function's domains
    :return: Dictionary that associates each output variable name with its calculated numeric value
    """
    num = {}
    den = {}

    for w, variable, func in rules_output:
        func = functions[func]
        points = list(func.points(step))
        z = reduce(
            lambda x, y: x if abs(x[1] - w) < abs(y[1] - w) else y,  # choose the one whose image is closer to 'w'
            points,
            points[0])[0]  # 'z' is the value of function's domain with image approximately 'w'

        num[variable] = num.get(variable, 0) + w * z
        den[variable] = den.get(variable, 0) + w

    return _divide(num, den)


def _divide(num, den):
    """
    Divide values corresponding to the same key in two dictionaries
    :param num: Dividend dictionary
    :param den: Divider dictionary
    :return: New dictionary with the same keys as the parameters and the divisions results as values
    """
    results = {}
    for variable in num.keys():
        results[variable] = num[variable] / den[variable]
    return results
