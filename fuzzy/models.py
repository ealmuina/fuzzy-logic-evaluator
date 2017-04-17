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
        if variable not in num:
            num[variable] = 0
            den[variable] = 0
        num[variable] += w * z
        den[variable] += w

    results = {}
    for variable in num.keys():
        results[variable] = num[variable] / den[variable]
    return results


def tsukamoto(rules_output, functions):
    pass
