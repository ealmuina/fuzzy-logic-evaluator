# Generated from /home/eddy/PycharmProjects/fuzzy_logic/fuzzy/parsing/Fuzzy.g4 by ANTLR 4.7
# encoding: utf-8
import sys
from io import StringIO

from antlr4 import *
from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("Z\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\5\2\23\n\2\3\2\6\2\26\n\2\r\2\16\2\27\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3(\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\64")
        buf.write("\n\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4<\n\4\f\4\16\4?\13\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5J\n\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5U\n\5\f\5\16\5X\13\5\3\5")
        buf.write("\2\4\6\b\6\2\4\6\b\2\4\3\2\20\21\3\2\22\23\2b\2\n\3\2")
        buf.write("\2\2\4\'\3\2\2\2\6\63\3\2\2\2\bI\3\2\2\2\n\13\7\3\2\2")
        buf.write("\13\f\7\4\2\2\f\r\7\5\2\2\r\22\7\25\2\2\16\17\7\3\2\2")
        buf.write("\17\20\7\6\2\2\20\21\7\5\2\2\21\23\7\25\2\2\22\16\3\2")
        buf.write("\2\2\22\23\3\2\2\2\23\25\3\2\2\2\24\26\5\4\3\2\25\24\3")
        buf.write("\2\2\2\26\27\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\31")
        buf.write("\3\2\2\2\31\32\7\2\2\3\32\3\3\2\2\2\33\34\5\6\4\2\34\35")
        buf.write("\7\7\2\2\35\36\7\25\2\2\36\37\7\b\2\2\37 \5\b\5\2 (\3")
        buf.write("\2\2\2!\"\5\6\4\2\"#\7\7\2\2#$\7\25\2\2$%\7\t\2\2%&\7")
        buf.write("\25\2\2&(\3\2\2\2\'\33\3\2\2\2\'!\3\2\2\2(\5\3\2\2\2)")
        buf.write("*\b\4\1\2*+\7\25\2\2+,\7\t\2\2,\64\7\25\2\2-.\7\n\2\2")
        buf.write("./\5\6\4\2/\60\7\13\2\2\60\64\3\2\2\2\61\62\7\16\2\2\62")
        buf.write("\64\5\6\4\3\63)\3\2\2\2\63-\3\2\2\2\63\61\3\2\2\2\64=")
        buf.write("\3\2\2\2\65\66\f\5\2\2\66\67\7\f\2\2\67<\5\6\4\689\f\4")
        buf.write("\2\29:\7\r\2\2:<\5\6\4\5;\65\3\2\2\2;8\3\2\2\2<?\3\2\2")
        buf.write("\2=;\3\2\2\2=>\3\2\2\2>\7\3\2\2\2?=\3\2\2\2@A\b\5\1\2")
        buf.write("AJ\7\25\2\2BJ\7\24\2\2CD\7\n\2\2DE\5\b\5\2EF\7\13\2\2")
        buf.write("FJ\3\2\2\2GH\7\23\2\2HJ\5\b\5\3I@\3\2\2\2IB\3\2\2\2IC")
        buf.write("\3\2\2\2IG\3\2\2\2JV\3\2\2\2KL\f\6\2\2LM\7\17\2\2MU\5")
        buf.write("\b\5\7NO\f\5\2\2OP\t\2\2\2PU\5\b\5\6QR\f\4\2\2RS\t\3\2")
        buf.write("\2SU\5\b\5\5TK\3\2\2\2TN\3\2\2\2TQ\3\2\2\2UX\3\2\2\2V")
        buf.write("T\3\2\2\2VW\3\2\2\2W\t\3\2\2\2XV\3\2\2\2\13\22\27\'\63")
        buf.write(";=ITV")
        return buf.getvalue()


class FuzzyParser(Parser):

    grammarFileName = "Fuzzy.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'['", "'model'", "']'", "'defuzzy'",
                    "'then'", "'='", "'is'", "'('", "')'", "'and'", "'or'",
                    "'not'", "'**'", "'*'", "'/'", "'+'", "'-'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "NUMBER", "ID", "COMMENT",
                     "WS"]

    RULE_compileUnit = 0
    RULE_fuzzy_rule = 1
    RULE_logic_expr = 2
    RULE_arithmetic_expr = 3

    ruleNames = ["compileUnit", "fuzzy_rule", "logic_expr", "arithmetic_expr"]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    NUMBER = 18
    ID = 19
    COMMENT = 20
    WS = 21

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

        def ID(self, i: int = None):
            if i is None:
                return self.getTokens(FuzzyParser.ID)
            else:
                return self.getToken(FuzzyParser.ID, i)
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
            self.state = 8
            self.match(FuzzyParser.T__0)
            self.state = 9
            self.match(FuzzyParser.T__1)
            self.state = 10
            self.match(FuzzyParser.T__2)
            self.state = 11
            self.match(FuzzyParser.ID)
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == FuzzyParser.T__0:
                self.state = 12
                self.match(FuzzyParser.T__0)
                self.state = 13
                self.match(FuzzyParser.T__3)
                self.state = 14
                self.match(FuzzyParser.T__2)
                self.state = 15
                self.match(FuzzyParser.ID)

            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.fuzzy_rule()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and (
                    (1 << _la) & ((1 << FuzzyParser.T__7) | (1 << FuzzyParser.T__11) | (1 << FuzzyParser.ID))) != 0)):
                    break

            self.state = 23
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

    class SRuleContext(Fuzzy_ruleContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a FuzzyParser.Fuzzy_ruleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def logic_expr(self):
            return self.getTypedRuleContext(FuzzyParser.Logic_exprContext, 0)

        def ID(self):
            return self.getToken(FuzzyParser.ID, 0)
        def arithmetic_expr(self):
            return self.getTypedRuleContext(FuzzyParser.Arithmetic_exprContext, 0)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitSRule"):
                return visitor.visitSRule(self)
            else:
                return visitor.visitChildren(self)

    class MTRuleContext(Fuzzy_ruleContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a FuzzyParser.Fuzzy_ruleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def logic_expr(self):
            return self.getTypedRuleContext(FuzzyParser.Logic_exprContext, 0)

        def ID(self, i: int = None):
            if i is None:
                return self.getTokens(FuzzyParser.ID)
            else:
                return self.getToken(FuzzyParser.ID, i)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMTRule"):
                return visitor.visitMTRule(self)
            else:
                return visitor.visitChildren(self)

    def fuzzy_rule(self):

        localctx = FuzzyParser.Fuzzy_ruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_fuzzy_rule)
        try:
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 2, self._ctx)
            if la_ == 1:
                localctx = FuzzyParser.SRuleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.logic_expr(0)
                self.state = 26
                self.match(FuzzyParser.T__4)
                self.state = 27
                self.match(FuzzyParser.ID)
                self.state = 28
                self.match(FuzzyParser.T__5)
                self.state = 29
                self.arithmetic_expr(0)
                pass

            elif la_ == 2:
                localctx = FuzzyParser.MTRuleContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.logic_expr(0)
                self.state = 32
                self.match(FuzzyParser.T__4)
                self.state = 33
                self.match(FuzzyParser.ID)
                self.state = 34
                self.match(FuzzyParser.T__6)
                self.state = 35
                self.match(FuzzyParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Logic_exprContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FuzzyParser.RULE_logic_expr

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)


    class LVarValueContext(Logic_exprContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a FuzzyParser.Logic_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i: int = None):
            if i is None:
                return self.getTokens(FuzzyParser.ID)
            else:
                return self.getToken(FuzzyParser.ID, i)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLVarValue"):
                return visitor.visitLVarValue(self)
            else:
                return visitor.visitChildren(self)


    class LNotContext(Logic_exprContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a FuzzyParser.Logic_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def logic_expr(self):
            return self.getTypedRuleContext(FuzzyParser.Logic_exprContext, 0)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLNot"):
                return visitor.visitLNot(self)
            else:
                return visitor.visitChildren(self)


    class LAndContext(Logic_exprContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a FuzzyParser.Logic_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def logic_expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(FuzzyParser.Logic_exprContext)
            else:
                return self.getTypedRuleContext(FuzzyParser.Logic_exprContext, i)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLAnd"):
                return visitor.visitLAnd(self)
            else:
                return visitor.visitChildren(self)


    class LParensContext(Logic_exprContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a FuzzyParser.Logic_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def logic_expr(self):
            return self.getTypedRuleContext(FuzzyParser.Logic_exprContext, 0)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLParens"):
                return visitor.visitLParens(self)
            else:
                return visitor.visitChildren(self)


    class LOrContext(Logic_exprContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a FuzzyParser.Logic_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def logic_expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(FuzzyParser.Logic_exprContext)
            else:
                return self.getTypedRuleContext(FuzzyParser.Logic_exprContext, i)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLOr"):
                return visitor.visitLOr(self)
            else:
                return visitor.visitChildren(self)

    def logic_expr(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = FuzzyParser.Logic_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_logic_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FuzzyParser.ID]:
                localctx = FuzzyParser.LVarValueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 40
                self.match(FuzzyParser.ID)
                self.state = 41
                self.match(FuzzyParser.T__6)
                self.state = 42
                self.match(FuzzyParser.ID)
                pass
            elif token in [FuzzyParser.T__7]:
                localctx = FuzzyParser.LParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 43
                self.match(FuzzyParser.T__7)
                self.state = 44
                self.logic_expr(0)
                self.state = 45
                self.match(FuzzyParser.T__8)
                pass
            elif token in [FuzzyParser.T__11]:
                localctx = FuzzyParser.LNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 47
                self.match(FuzzyParser.T__11)
                self.state = 48
                self.logic_expr(1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 59
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 5, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 57
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input, 4, self._ctx)
                    if la_ == 1:
                        localctx = FuzzyParser.LAndContext(self, FuzzyParser.Logic_exprContext(self, _parentctx,
                                                                                               _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logic_expr)
                        self.state = 51
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 52
                        self.match(FuzzyParser.T__9)
                        self.state = 53
                        self.logic_expr(4)
                        pass

                    elif la_ == 2:
                        localctx = FuzzyParser.LOrContext(self,
                                                          FuzzyParser.Logic_exprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logic_expr)
                        self.state = 54
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 55
                        self.match(FuzzyParser.T__10)
                        self.state = 56
                        self.logic_expr(3)
                        pass

                self.state = 61
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 5, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Arithmetic_exprContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FuzzyParser.RULE_arithmetic_expr

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)


    class ANegContext(Arithmetic_exprContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a FuzzyParser.Arithmetic_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arithmetic_expr(self):
            return self.getTypedRuleContext(FuzzyParser.Arithmetic_exprContext, 0)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitANeg"):
                return visitor.visitANeg(self)
            else:
                return visitor.visitChildren(self)


    class AVarContext(Arithmetic_exprContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a FuzzyParser.Arithmetic_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(FuzzyParser.ID, 0)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAVar"):
                return visitor.visitAVar(self)
            else:
                return visitor.visitChildren(self)


    class ANumberContext(Arithmetic_exprContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a FuzzyParser.Arithmetic_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(FuzzyParser.NUMBER, 0)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitANumber"):
                return visitor.visitANumber(self)
            else:
                return visitor.visitChildren(self)


    class AArithmeticContext(Arithmetic_exprContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a FuzzyParser.Arithmetic_exprContext
            super().__init__(parser)
            self.op = None  # Token
            self.copyFrom(ctx)

        def arithmetic_expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(FuzzyParser.Arithmetic_exprContext)
            else:
                return self.getTypedRuleContext(FuzzyParser.Arithmetic_exprContext, i)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAArithmetic"):
                return visitor.visitAArithmetic(self)
            else:
                return visitor.visitChildren(self)


    class AParensContext(Arithmetic_exprContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a FuzzyParser.Arithmetic_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arithmetic_expr(self):
            return self.getTypedRuleContext(FuzzyParser.Arithmetic_exprContext, 0)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAParens"):
                return visitor.visitAParens(self)
            else:
                return visitor.visitChildren(self)

    def arithmetic_expr(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = FuzzyParser.Arithmetic_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_arithmetic_expr, _p)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FuzzyParser.ID]:
                localctx = FuzzyParser.AVarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 63
                self.match(FuzzyParser.ID)
                pass
            elif token in [FuzzyParser.NUMBER]:
                localctx = FuzzyParser.ANumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 64
                self.match(FuzzyParser.NUMBER)
                pass
            elif token in [FuzzyParser.T__7]:
                localctx = FuzzyParser.AParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 65
                self.match(FuzzyParser.T__7)
                self.state = 66
                self.arithmetic_expr(0)
                self.state = 67
                self.match(FuzzyParser.T__8)
                pass
            elif token in [FuzzyParser.T__16]:
                localctx = FuzzyParser.ANegContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 69
                self.match(FuzzyParser.T__16)
                self.state = 70
                self.arithmetic_expr(1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 84
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 8, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 82
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input, 7, self._ctx)
                    if la_ == 1:
                        localctx = FuzzyParser.AArithmeticContext(self,
                                                                  FuzzyParser.Arithmetic_exprContext(self, _parentctx,
                                                                                                     _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expr)
                        self.state = 73
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 74
                        localctx.op = self.match(FuzzyParser.T__12)
                        self.state = 75
                        self.arithmetic_expr(5)
                        pass

                    elif la_ == 2:
                        localctx = FuzzyParser.AArithmeticContext(self,
                                                                  FuzzyParser.Arithmetic_exprContext(self, _parentctx,
                                                                                                     _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expr)
                        self.state = 76
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 77
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not (_la == FuzzyParser.T__13 or _la == FuzzyParser.T__14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 78
                        self.arithmetic_expr(4)
                        pass

                    elif la_ == 3:
                        localctx = FuzzyParser.AArithmeticContext(self,
                                                                  FuzzyParser.Arithmetic_exprContext(self, _parentctx,
                                                                                                     _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expr)
                        self.state = 79
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 80
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not (_la == FuzzyParser.T__15 or _la == FuzzyParser.T__16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 81
                        self.arithmetic_expr(3)
                        pass

                self.state = 86
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 8, self._ctx)

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
        self._predicates[2] = self.logic_expr_sempred
        self._predicates[3] = self.arithmetic_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logic_expr_sempred(self, localctx: Logic_exprContext, predIndex: int):
        if predIndex == 0:
            return self.precpred(self._ctx, 3)

        if predIndex == 1:
            return self.precpred(self._ctx, 2)

    def arithmetic_expr_sempred(self, localctx: Arithmetic_exprContext, predIndex: int):
        if predIndex == 2:
            return self.precpred(self._ctx, 4)

        if predIndex == 3:
            return self.precpred(self._ctx, 3)

        if predIndex == 4:
            return self.precpred(self._ctx, 2)
