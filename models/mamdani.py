from parsing.FuzzyParser import FuzzyParser
from parsing.FuzzyVisitor import FuzzyVisitor


# noinspection SpellCheckingInspection
class Mamdani(FuzzyVisitor):
    def __init__(self, values, funcs):
        self.values = values
        self.funcs = funcs

    def visitFile(self, ctx: FuzzyParser.FileContext):
        return [self.visit(r) for r in ctx.fuzzy_rule()]

    def visitFuzzyRule(self, ctx: FuzzyParser.FuzzyRuleContext):
        trunc = self.visit(ctx.expr())
        variable = ctx.ID(0).getText()
        func = ctx.ID(1).getText()
        return trunc, variable, func

    def visitVarValue(self, ctx: FuzzyParser.VarValueContext):
        variable = ctx.ID(0).getText()
        func = ctx.ID(1).getText()
        return self.funcs[func](self.values[variable])

    def visitParens(self, ctx: FuzzyParser.ParensContext):
        return self.visit(ctx.expr())

    def visitAnd(self, ctx: FuzzyParser.AndContext):
        return min(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))

    def visitOr(self, ctx: FuzzyParser.OrContext):
        return max(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))

    def visitNot(self, ctx: FuzzyParser.NotContext):
        return 1 - self.visit(ctx.expr())
