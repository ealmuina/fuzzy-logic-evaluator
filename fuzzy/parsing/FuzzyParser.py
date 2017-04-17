# Generated from /home/eddy/PycharmProjects/fuzzy_logic/fuzzy/parsing/Fuzzy.g4 by ANTLR 4.7
# encoding: utf-8
import sys
from io import StringIO

from antlr4 import *
from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\35")
        buf.write("i\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\6\3\27\n\3\r\3\16\3\30\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\6\3!\n\3\r\3\16\3\"\3\3\3\3\6\3")
        buf.write("\'\n\3\r\3\16\3(\5\3+\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\5\6C\n\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6K\n\6\f\6\16")
        buf.write("\6N\13\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7Y\n\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7d\n\7\f\7\16\7")
        buf.write("g\13\7\3\7\2\4\n\f\b\2\4\6\b\n\f\2\5\3\2\t\13\3\2\26\27")
        buf.write("\3\2\30\31\2q\2\16\3\2\2\2\4*\3\2\2\2\6,\3\2\2\2\b\62")
        buf.write("\3\2\2\2\nB\3\2\2\2\fX\3\2\2\2\16\17\7\3\2\2\17\20\7\4")
        buf.write("\2\2\20\21\7\5\2\2\21\22\5\4\3\2\22\23\7\2\2\3\23\3\3")
        buf.write("\2\2\2\24\26\7\6\2\2\25\27\5\6\4\2\26\25\3\2\2\2\27\30")
        buf.write("\3\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31+\3\2\2\2\32\33")
        buf.write("\7\7\2\2\33\34\7\3\2\2\34\35\7\b\2\2\35\36\7\5\2\2\36")
        buf.write(" \t\2\2\2\37!\5\b\5\2 \37\3\2\2\2!\"\3\2\2\2\" \3\2\2")
        buf.write("\2\"#\3\2\2\2#+\3\2\2\2$&\7\f\2\2%\'\5\b\5\2&%\3\2\2\2")
        buf.write("\'(\3\2\2\2(&\3\2\2\2()\3\2\2\2)+\3\2\2\2*\24\3\2\2\2")
        buf.write("*\32\3\2\2\2*$\3\2\2\2+\5\3\2\2\2,-\5\n\6\2-.\7\r\2\2")
        buf.write("./\7\33\2\2/\60\7\16\2\2\60\61\5\f\7\2\61\7\3\2\2\2\62")
        buf.write("\63\5\n\6\2\63\64\7\r\2\2\64\65\7\33\2\2\65\66\7\17\2")
        buf.write("\2\66\67\7\33\2\2\67\t\3\2\2\289\b\6\1\29:\7\33\2\2:;")
        buf.write("\7\17\2\2;C\7\33\2\2<=\7\20\2\2=>\5\n\6\2>?\7\21\2\2?")
        buf.write("C\3\2\2\2@A\7\24\2\2AC\5\n\6\3B8\3\2\2\2B<\3\2\2\2B@\3")
        buf.write("\2\2\2CL\3\2\2\2DE\f\5\2\2EF\7\22\2\2FK\5\n\6\6GH\f\4")
        buf.write("\2\2HI\7\23\2\2IK\5\n\6\5JD\3\2\2\2JG\3\2\2\2KN\3\2\2")
        buf.write("\2LJ\3\2\2\2LM\3\2\2\2M\13\3\2\2\2NL\3\2\2\2OP\b\7\1\2")
        buf.write("PY\7\33\2\2QY\7\32\2\2RS\7\20\2\2ST\5\f\7\2TU\7\21\2\2")
        buf.write("UY\3\2\2\2VW\7\31\2\2WY\5\f\7\3XO\3\2\2\2XQ\3\2\2\2XR")
        buf.write("\3\2\2\2XV\3\2\2\2Ye\3\2\2\2Z[\f\6\2\2[\\\7\25\2\2\\d")
        buf.write("\5\f\7\7]^\f\5\2\2^_\t\3\2\2_d\5\f\7\6`a\f\4\2\2ab\t\4")
        buf.write("\2\2bd\5\f\7\5cZ\3\2\2\2c]\3\2\2\2c`\3\2\2\2dg\3\2\2\2")
        buf.write("ec\3\2\2\2ef\3\2\2\2f\r\3\2\2\2ge\3\2\2\2\f\30\"(*BJL")
        buf.write("Xce")
        return buf.getvalue()


class FuzzyParser(Parser):
    grammarFileName = "Fuzzy.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'['", "'model'", "']'", "'Sugeno'", "'Mamdani'",
                    "'defuzzy'", "'Centroid'", "'Bisecter'", "'Mean of Max'",
                    "'Tsukamoto'", "'=>'", "'='", "'is'", "'('", "')'",
                    "'and'", "'or'", "'not'", "'**'", "'*'", "'/'", "'+'",
                    "'-'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "NUMBER", "ID", "COMMENT", "WS"]

    RULE_compileUnit = 0
    RULE_model = 1
    RULE_sugeno_rule = 2
    RULE_mamdani_tsukamoto_rule = 3
    RULE_logic_expr = 4
    RULE_arithmetic_expr = 5

    ruleNames = ["compileUnit", "model", "sugeno_rule", "mamdani_tsukamoto_rule",
                 "logic_expr", "arithmetic_expr"]

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
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    NUMBER = 24
    ID = 25
    COMMENT = 26
    WS = 27

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

        def model(self):
            return self.getTypedRuleContext(FuzzyParser.ModelContext, 0)

        def EOF(self):
            return self.getToken(FuzzyParser.EOF, 0)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitFile"):
                return visitor.visitFile(self)
            else:
                return visitor.visitChildren(self)

    def compileUnit(self):

        localctx = FuzzyParser.CompileUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_compileUnit)
        try:
            localctx = FuzzyParser.FileContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(FuzzyParser.T__0)
            self.state = 13
            self.match(FuzzyParser.T__1)
            self.state = 14
            self.match(FuzzyParser.T__2)
            self.state = 15
            self.model()
            self.state = 16
            self.match(FuzzyParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModelContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return FuzzyParser.RULE_model

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class SugenoContext(ModelContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a FuzzyParser.ModelContext
            super().__init__(parser)
            self.mod = None  # Token
            self.copyFrom(ctx)

        def sugeno_rule(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(FuzzyParser.Sugeno_ruleContext)
            else:
                return self.getTypedRuleContext(FuzzyParser.Sugeno_ruleContext, i)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitSugeno"):
                return visitor.visitSugeno(self)
            else:
                return visitor.visitChildren(self)

    class MamdaniContext(ModelContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a FuzzyParser.ModelContext
            super().__init__(parser)
            self.mod = None  # Token
            self.defuzzy = None  # Token
            self.copyFrom(ctx)

        def mamdani_tsukamoto_rule(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(FuzzyParser.Mamdani_tsukamoto_ruleContext)
            else:
                return self.getTypedRuleContext(FuzzyParser.Mamdani_tsukamoto_ruleContext, i)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMamdani"):
                return visitor.visitMamdani(self)
            else:
                return visitor.visitChildren(self)

    class TsukamotoContext(ModelContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a FuzzyParser.ModelContext
            super().__init__(parser)
            self.mod = None  # Token
            self.copyFrom(ctx)

        def mamdani_tsukamoto_rule(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(FuzzyParser.Mamdani_tsukamoto_ruleContext)
            else:
                return self.getTypedRuleContext(FuzzyParser.Mamdani_tsukamoto_ruleContext, i)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitTsukamoto"):
                return visitor.visitTsukamoto(self)
            else:
                return visitor.visitChildren(self)

    def model(self):

        localctx = FuzzyParser.ModelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_model)
        self._la = 0  # Token type
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FuzzyParser.T__3]:
                localctx = FuzzyParser.SugenoContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                localctx.mod = self.match(FuzzyParser.T__3)
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 19
                    self.sugeno_rule()
                    self.state = 22
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & (
                            (1 << FuzzyParser.T__13) | (1 << FuzzyParser.T__17) | (1 << FuzzyParser.ID))) != 0)):
                        break

                pass
            elif token in [FuzzyParser.T__4]:
                localctx = FuzzyParser.MamdaniContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                localctx.mod = self.match(FuzzyParser.T__4)
                self.state = 25
                self.match(FuzzyParser.T__0)
                self.state = 26
                self.match(FuzzyParser.T__5)
                self.state = 27
                self.match(FuzzyParser.T__2)
                self.state = 28
                localctx.defuzzy = self._input.LT(1)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and (
                    (1 << _la) & ((1 << FuzzyParser.T__6) | (1 << FuzzyParser.T__7) | (1 << FuzzyParser.T__8))) != 0)):
                    localctx.defuzzy = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 29
                    self.mamdani_tsukamoto_rule()
                    self.state = 32
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & (
                            (1 << FuzzyParser.T__13) | (1 << FuzzyParser.T__17) | (1 << FuzzyParser.ID))) != 0)):
                        break

                pass
            elif token in [FuzzyParser.T__9]:
                localctx = FuzzyParser.TsukamotoContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                localctx.mod = self.match(FuzzyParser.T__9)
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 35
                    self.mamdani_tsukamoto_rule()
                    self.state = 38
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & (
                            (1 << FuzzyParser.T__13) | (1 << FuzzyParser.T__17) | (1 << FuzzyParser.ID))) != 0)):
                        break

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Sugeno_ruleContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return FuzzyParser.RULE_sugeno_rule

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class SRuleContext(Sugeno_ruleContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a FuzzyParser.Sugeno_ruleContext
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

    def sugeno_rule(self):

        localctx = FuzzyParser.Sugeno_ruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sugeno_rule)
        try:
            localctx = FuzzyParser.SRuleContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.logic_expr(0)
            self.state = 43
            self.match(FuzzyParser.T__10)
            self.state = 44
            self.match(FuzzyParser.ID)
            self.state = 45
            self.match(FuzzyParser.T__11)
            self.state = 46
            self.arithmetic_expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Mamdani_tsukamoto_ruleContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return FuzzyParser.RULE_mamdani_tsukamoto_rule

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class MTRuleContext(Mamdani_tsukamoto_ruleContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a FuzzyParser.Mamdani_tsukamoto_ruleContext
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

    def mamdani_tsukamoto_rule(self):

        localctx = FuzzyParser.Mamdani_tsukamoto_ruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_mamdani_tsukamoto_rule)
        try:
            localctx = FuzzyParser.MTRuleContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.logic_expr(0)
            self.state = 49
            self.match(FuzzyParser.T__10)
            self.state = 50
            self.match(FuzzyParser.ID)
            self.state = 51
            self.match(FuzzyParser.T__12)
            self.state = 52
            self.match(FuzzyParser.ID)
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
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_logic_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FuzzyParser.ID]:
                localctx = FuzzyParser.LVarValueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 55
                self.match(FuzzyParser.ID)
                self.state = 56
                self.match(FuzzyParser.T__12)
                self.state = 57
                self.match(FuzzyParser.ID)
                pass
            elif token in [FuzzyParser.T__13]:
                localctx = FuzzyParser.LParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 58
                self.match(FuzzyParser.T__13)
                self.state = 59
                self.logic_expr(0)
                self.state = 60
                self.match(FuzzyParser.T__14)
                pass
            elif token in [FuzzyParser.T__17]:
                localctx = FuzzyParser.LNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 62
                self.match(FuzzyParser.T__17)
                self.state = 63
                self.logic_expr(1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 74
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 6, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 72
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input, 5, self._ctx)
                    if la_ == 1:
                        localctx = FuzzyParser.LAndContext(self, FuzzyParser.Logic_exprContext(self, _parentctx,
                                                                                               _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logic_expr)
                        self.state = 66
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 67
                        self.match(FuzzyParser.T__15)
                        self.state = 68
                        self.logic_expr(4)
                        pass

                    elif la_ == 2:
                        localctx = FuzzyParser.LOrContext(self,
                                                          FuzzyParser.Logic_exprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logic_expr)
                        self.state = 69
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 70
                        self.match(FuzzyParser.T__16)
                        self.state = 71
                        self.logic_expr(3)
                        pass

                self.state = 76
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 6, self._ctx)

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
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_arithmetic_expr, _p)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FuzzyParser.ID]:
                localctx = FuzzyParser.AVarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 78
                self.match(FuzzyParser.ID)
                pass
            elif token in [FuzzyParser.NUMBER]:
                localctx = FuzzyParser.ANumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 79
                self.match(FuzzyParser.NUMBER)
                pass
            elif token in [FuzzyParser.T__13]:
                localctx = FuzzyParser.AParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 80
                self.match(FuzzyParser.T__13)
                self.state = 81
                self.arithmetic_expr(0)
                self.state = 82
                self.match(FuzzyParser.T__14)
                pass
            elif token in [FuzzyParser.T__22]:
                localctx = FuzzyParser.ANegContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 84
                self.match(FuzzyParser.T__22)
                self.state = 85
                self.arithmetic_expr(1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 99
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 9, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 97
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input, 8, self._ctx)
                    if la_ == 1:
                        localctx = FuzzyParser.AArithmeticContext(self,
                                                                  FuzzyParser.Arithmetic_exprContext(self, _parentctx,
                                                                                                     _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expr)
                        self.state = 88
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 89
                        localctx.op = self.match(FuzzyParser.T__18)
                        self.state = 90
                        self.arithmetic_expr(5)
                        pass

                    elif la_ == 2:
                        localctx = FuzzyParser.AArithmeticContext(self,
                                                                  FuzzyParser.Arithmetic_exprContext(self, _parentctx,
                                                                                                     _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expr)
                        self.state = 91
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 92
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not (_la == FuzzyParser.T__19 or _la == FuzzyParser.T__20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 93
                        self.arithmetic_expr(4)
                        pass

                    elif la_ == 3:
                        localctx = FuzzyParser.AArithmeticContext(self,
                                                                  FuzzyParser.Arithmetic_exprContext(self, _parentctx,
                                                                                                     _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expr)
                        self.state = 94
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 95
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not (_la == FuzzyParser.T__21 or _la == FuzzyParser.T__22):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 96
                        self.arithmetic_expr(3)
                        pass

                self.state = 101
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 9, self._ctx)

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
        self._predicates[4] = self.logic_expr_sempred
        self._predicates[5] = self.arithmetic_expr_sempred
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
