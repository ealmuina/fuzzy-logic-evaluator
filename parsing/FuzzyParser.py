# Generated from /home/eddy/PycharmProjects/fuzzy_logic/parsing/Fuzzy.g4 by ANTLR 4.7
# encoding: utf-8
import sys
from io import StringIO

from antlr4 import *
from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("-\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\n\n\2\r\2\16\2\13\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\5\4 \n\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4")
        buf.write("(\n\4\f\4\16\4+\13\4\3\4\2\3\6\5\2\4\6\2\2\2.\2\t\3\2")
        buf.write("\2\2\4\17\3\2\2\2\6\37\3\2\2\2\b\n\5\4\3\2\t\b\3\2\2\2")
        buf.write("\n\13\3\2\2\2\13\t\3\2\2\2\13\f\3\2\2\2\f\r\3\2\2\2\r")
        buf.write("\16\7\2\2\3\16\3\3\2\2\2\17\20\5\6\4\2\20\21\7\3\2\2\21")
        buf.write("\22\7\n\2\2\22\23\7\4\2\2\23\24\7\n\2\2\24\5\3\2\2\2\25")
        buf.write("\26\b\4\1\2\26\27\7\n\2\2\27\30\7\4\2\2\30 \7\n\2\2\31")
        buf.write("\32\7\5\2\2\32\33\5\6\4\2\33\34\7\6\2\2\34 \3\2\2\2\35")
        buf.write("\36\7\t\2\2\36 \5\6\4\3\37\25\3\2\2\2\37\31\3\2\2\2\37")
        buf.write("\35\3\2\2\2 )\3\2\2\2!\"\f\5\2\2\"#\7\7\2\2#(\5\6\4\6")
        buf.write("$%\f\4\2\2%&\7\b\2\2&(\5\6\4\5\'!\3\2\2\2\'$\3\2\2\2(")
        buf.write("+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*\7\3\2\2\2+)\3\2\2\2\6")
        buf.write("\13\37\')")
        return buf.getvalue()


class FuzzyParser(Parser):
    grammarFileName = "Fuzzy.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'=>'", "'is'", "'('", "')'", "'and'",
                    "'or'", "'not'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "ID", "COMMENT", "WS"]

    RULE_compileUnit = 0
    RULE_fuzzy_rule = 1
    RULE_expr = 2

    ruleNames = ["compileUnit", "fuzzy_rule", "expr"]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    ID = 8
    COMMENT = 9
    WS = 10

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class CompileUnitContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return FuzzyParser.RULE_compileUnit

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class FileContext(CompileUnitContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a FuzzyParser.CompileUnitContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EOF(self):
            return self.getToken(FuzzyParser.EOF, 0)

        def fuzzy_rule(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(FuzzyParser.Fuzzy_ruleContext)
            else:
                return self.getTypedRuleContext(FuzzyParser.Fuzzy_ruleContext, i)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitFile"):
                return visitor.visitFile(self)
            else:
                return visitor.visitChildren(self)

    def compileUnit(self):

        localctx = FuzzyParser.CompileUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_compileUnit)
        self._la = 0  # Token type
        try:
            localctx = FuzzyParser.FileContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.fuzzy_rule()
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and (
                    (1 << _la) & ((1 << FuzzyParser.T__2) | (1 << FuzzyParser.T__6) | (1 << FuzzyParser.ID))) != 0)):
                    break

            self.state = 11
            self.match(FuzzyParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fuzzy_ruleContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return FuzzyParser.RULE_fuzzy_rule

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class FuzzyRuleContext(Fuzzy_ruleContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a FuzzyParser.Fuzzy_ruleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(FuzzyParser.ExprContext, 0)

        def ID(self, i: int = None):
            if i is None:
                return self.getTokens(FuzzyParser.ID)
            else:
                return self.getToken(FuzzyParser.ID, i)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitFuzzyRule"):
                return visitor.visitFuzzyRule(self)
            else:
                return visitor.visitChildren(self)

    def fuzzy_rule(self):

        localctx = FuzzyParser.Fuzzy_ruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_fuzzy_rule)
        try:
            localctx = FuzzyParser.FuzzyRuleContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.expr(0)
            self.state = 14
            self.match(FuzzyParser.T__0)
            self.state = 15
            self.match(FuzzyParser.ID)
            self.state = 16
            self.match(FuzzyParser.T__1)
            self.state = 17
            self.match(FuzzyParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return FuzzyParser.RULE_expr

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class NotContext(ExprContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a FuzzyParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(FuzzyParser.ExprContext, 0)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitNot"):
                return visitor.visitNot(self)
            else:
                return visitor.visitChildren(self)

    class OrContext(ExprContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a FuzzyParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(FuzzyParser.ExprContext)
            else:
                return self.getTypedRuleContext(FuzzyParser.ExprContext, i)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitOr"):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)

    class ParensContext(ExprContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a FuzzyParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(FuzzyParser.ExprContext, 0)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitParens"):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)

    class AndContext(ExprContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a FuzzyParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(FuzzyParser.ExprContext)
            else:
                return self.getTypedRuleContext(FuzzyParser.ExprContext, i)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAnd"):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)

    class VarValueContext(ExprContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a FuzzyParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i: int = None):
            if i is None:
                return self.getTokens(FuzzyParser.ID)
            else:
                return self.getToken(FuzzyParser.ID, i)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitVarValue"):
                return visitor.visitVarValue(self)
            else:
                return visitor.visitChildren(self)

    def expr(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = FuzzyParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FuzzyParser.ID]:
                localctx = FuzzyParser.VarValueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 20
                self.match(FuzzyParser.ID)
                self.state = 21
                self.match(FuzzyParser.T__1)
                self.state = 22
                self.match(FuzzyParser.ID)
                pass
            elif token in [FuzzyParser.T__2]:
                localctx = FuzzyParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 23
                self.match(FuzzyParser.T__2)
                self.state = 24
                self.expr(0)
                self.state = 25
                self.match(FuzzyParser.T__3)
                pass
            elif token in [FuzzyParser.T__6]:
                localctx = FuzzyParser.NotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 27
                self.match(FuzzyParser.T__6)
                self.state = 28
                self.expr(1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 3, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 37
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input, 2, self._ctx)
                    if la_ == 1:
                        localctx = FuzzyParser.AndContext(self, FuzzyParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 31
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 32
                        self.match(FuzzyParser.T__4)
                        self.state = 33
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = FuzzyParser.OrContext(self, FuzzyParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 35
                        self.match(FuzzyParser.T__5)
                        self.state = 36
                        self.expr(3)
                        pass

                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 3, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    def sempred(self, localctx: RuleContext, ruleIndex: int, predIndex: int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx: ExprContext, predIndex: int):
        if predIndex == 0:
            return self.precpred(self._ctx, 3)

        if predIndex == 1:
            return self.precpred(self._ctx, 2)
