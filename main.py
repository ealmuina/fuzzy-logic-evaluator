import json
import sys

from antlr4 import *

import fuzzy.defuzzifiers as defuzzifiers
import fuzzy.functions as functions
import fuzzy.models as models
from fuzzy.parsing.FuzzyLexer import FuzzyLexer
from fuzzy.parsing.FuzzyParser import FuzzyParser
from fuzzy.parsing.evaluator import Evaluator


def main(argv):
    rules = FileStream(argv[1])
    data = json.load(open(argv[2]))

    lexer = FuzzyLexer(rules)
    stream = CommonTokenStream(lexer)
    parser = FuzzyParser(stream)
    tree = parser.compileUnit()

    values = data['variables']
    funcs = data['functions']

    for f, l in funcs.items():
        f_name = l.pop(0)
        funcs[f] = getattr(functions, f_name)(*l)

    evaluator = Evaluator(values, funcs)
    model, defuzzy, output = evaluator.visit(tree)

    model = model.lower()

    if model == 'mamdani':
        defuzzy = defuzzifiers.get_defuzzy(defuzzy.lower())
        print(models.mamdani(output, defuzzy, funcs))

    elif model == 'sugeno':
        print(models.sugeno(output))

    elif model == 'tsukamoto':
        print(models.tsukamoto(output, funcs))

    else:
        raise AttributeError()


if __name__ == '__main__':
    main(sys.argv)
