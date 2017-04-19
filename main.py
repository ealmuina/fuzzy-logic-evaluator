import argparse
import json

from antlr4 import *

import fuzzy.defuzzifiers as defuzzifiers
import fuzzy.functions as functions
import fuzzy.models as models
from fuzzy.parsing.FuzzyLexer import FuzzyLexer
from fuzzy.parsing.FuzzyParser import FuzzyParser
from fuzzy.parsing.evaluator import Evaluator


def print_dict(d: dict):
    for key, value in d.items():
        print('%s: %.3f' % (key, value))


def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('rules')
    parser.add_argument('data')
    parser.add_argument('--step', default=0.1, type=float)
    args = parser.parse_args()

    # Grab rules, data and step from parsed arguments
    rules = FileStream(args.rules)
    data = json.load(open(args.data))
    step = args.step

    # Parse rules file
    lexer = FuzzyLexer(rules)
    stream = CommonTokenStream(lexer)
    parser = FuzzyParser(stream)
    tree = parser.compileUnit()

    # Retrieve dictionaries from data JSON file
    values = data['variables']
    funcs = data['functions']

    for f, l in funcs.items():
        f_name = l.pop(0)
        funcs[f] = getattr(functions, f_name)(*l)

    # Evaluate rules expressions
    evaluator = Evaluator(values, funcs)
    model, defuzzy, output = evaluator.visit(tree)

    model = model.lower()

    if model == 'mamdani':
        defuzzy = getattr(defuzzifiers, defuzzy.lower())
        print_dict(models.mamdani(output, defuzzy, funcs, step))

    elif model == 'sugeno':
        print_dict(models.sugeno(output))

    elif model == 'tsukamoto':
        print_dict(models.tsukamoto(output, funcs, step))

    else:
        raise AttributeError()


if __name__ == '__main__':
    main()
