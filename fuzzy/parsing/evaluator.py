from .FuzzyParser import FuzzyParser
from .FuzzyVisitor import FuzzyVisitor


class Evaluator(FuzzyVisitor):
    def __init__(self, values, funcs):
        self.values = values
        self.funcs = funcs
        self.tnorm = self.tconorm = None

    def visitFile(self, ctx: FuzzyParser.FileContext):
        self.tnorm = _get_function(ctx.ID(1).getText().lower())
        self.tconorm = _get_function(ctx.ID(2).getText().lower())

        return ctx.ID(0).getText(), \
               ctx.ID(3).getText() if ctx.ID(3) else None, \
               [self.visit(r) for r in ctx.fuzzy_rule()]

    def visitSRule(self, ctx: FuzzyParser.SRuleContext):
        w = self.visit(ctx.logic_expr())
        variable = ctx.ID().getText()
        z = self.visit(ctx.arithmetic_expr())
        return w, variable, z

    def visitMTRule(self, ctx: FuzzyParser.MTRuleContext):
        trunc = self.visit(ctx.logic_expr())
        variable = ctx.ID(0).getText()
        func = ctx.ID(1).getText()
        return trunc, variable, func

    def visitLVarValue(self, ctx: FuzzyParser.LVarValueContext):
        variable = ctx.ID(0).getText()
        func = ctx.ID(1).getText()
        return self.funcs[func](self.values[variable])

    def visitLParens(self, ctx: FuzzyParser.LParensContext):
        return self.visit(ctx.logic_expr())

    def visitLAnd(self, ctx: FuzzyParser.LAndContext):
        return self.tnorm(self.visit(ctx.logic_expr(0)), self.visit(ctx.logic_expr(1)))

    def visitLOr(self, ctx: FuzzyParser.LOrContext):
        return self.tconorm(self.visit(ctx.logic_expr(0)), self.visit(ctx.logic_expr(1)))

    def visitLNot(self, ctx: FuzzyParser.LNotContext):
        return 1 - self.visit(ctx.logic_expr())

    def visitAVar(self, ctx: FuzzyParser.AVarContext):
        return self.values[ctx.ID().getText()]

    def visitANumber(self, ctx: FuzzyParser.ANumberContext):
        return float(ctx.NUMBER().getText())

    def visitAParens(self, ctx: FuzzyParser.AParensContext):
        return self.visit(ctx.arithmetic_expr())

    def visitAArithmetic(self, ctx: FuzzyParser.AArithmeticContext):
        e1 = self.visit(ctx.arithmetic_expr(0))
        e2 = self.visit(ctx.arithmetic_expr(1))
        op = ctx.op.text

        if op == '**':
            return e1 ** e2
        if op == '*':
            return e1 * e2
        if op == '/':
            return e1 / e2
        if op == '+':
            return e1 + e2
        if op == '-':
            return e1 - e2

    def visitANeg(self, ctx: FuzzyParser.ANegContext):
        return -self.visit(ctx.arithmetic_expr())


def _get_function(name):
    if name == 'product':
        return lambda x, y: x * y
    elif name == 'sum':
        return lambda x, y: x + y - x * y
    elif name == 'max':
        return max
    elif name == 'min':
        return min
