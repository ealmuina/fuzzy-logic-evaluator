# Generated from /home/eddy/PycharmProjects/fuzzy_logic/parsing/Fuzzy.g4 by ANTLR 4.7
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .FuzzyParser import FuzzyParser
else:
    from FuzzyParser import FuzzyParser


# This class defines a complete generic visitor for a parse tree produced by FuzzyParser.

class FuzzyVisitor(ParseTreeVisitor):
    # Visit a parse tree produced by FuzzyParser#File.
    def visitFile(self, ctx: FuzzyParser.FileContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FuzzyParser#FuzzyRule.
    def visitFuzzyRule(self, ctx: FuzzyParser.FuzzyRuleContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FuzzyParser#Not.
    def visitNot(self, ctx: FuzzyParser.NotContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FuzzyParser#Or.
    def visitOr(self, ctx: FuzzyParser.OrContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FuzzyParser#Parens.
    def visitParens(self, ctx: FuzzyParser.ParensContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FuzzyParser#And.
    def visitAnd(self, ctx: FuzzyParser.AndContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FuzzyParser#VarValue.
    def visitVarValue(self, ctx: FuzzyParser.VarValueContext):
        return self.visitChildren(ctx)


del FuzzyParser
