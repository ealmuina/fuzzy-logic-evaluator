import json
import sys

from antlr4 import *

import functions
from models.mamdani import Mamdani
from parsing.FuzzyLexer import FuzzyLexer
from parsing.FuzzyParser import FuzzyParser


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

    # noinspection SpellCheckingInspection
    mamdani = Mamdani(values, funcs)
    print(mamdani.visit(tree))


if __name__ == '__main__':
    main(sys.argv)
