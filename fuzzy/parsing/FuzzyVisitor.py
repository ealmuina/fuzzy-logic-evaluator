# Generated from /home/eddy/PycharmProjects/fuzzy_logic/fuzzy/parsing/Fuzzy.g4 by ANTLR 4.7
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


    # Visit a parse tree produced by FuzzyParser#SRule.
    def visitSRule(self, ctx: FuzzyParser.SRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuzzyParser#MTRule.
    def visitMTRule(self, ctx: FuzzyParser.MTRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuzzyParser#LVarValue.
    def visitLVarValue(self, ctx: FuzzyParser.LVarValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuzzyParser#LNot.
    def visitLNot(self, ctx: FuzzyParser.LNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuzzyParser#LAnd.
    def visitLAnd(self, ctx: FuzzyParser.LAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuzzyParser#LParens.
    def visitLParens(self, ctx: FuzzyParser.LParensContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FuzzyParser#LOr.
    def visitLOr(self, ctx: FuzzyParser.LOrContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FuzzyParser#ANeg.
    def visitANeg(self, ctx: FuzzyParser.ANegContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FuzzyParser#AVar.
    def visitAVar(self, ctx: FuzzyParser.AVarContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FuzzyParser#ANumber.
    def visitANumber(self, ctx: FuzzyParser.ANumberContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FuzzyParser#AArithmetic.
    def visitAArithmetic(self, ctx: FuzzyParser.AArithmeticContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FuzzyParser#AParens.
    def visitAParens(self, ctx: FuzzyParser.AParensContext):
        return self.visitChildren(ctx)


del FuzzyParser