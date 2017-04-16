# Generated from /home/eddy/PycharmProjects/fuzzy_logic/parsing/Fuzzy.g4 by ANTLR 4.7
import sys
from io import StringIO

from antlr4 import *
from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("S\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\7\139\n\13\f\13\16\13<\13\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\7\fC\n\f\f\f\16\fF\13\f\3\f\3\f\3\f\3\f\3\f\3\r\6")
        buf.write("\rN\n\r\r\r\16\rO\3\r\3\r\3D\2\16\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\2\23\2\25\n\27\13\31\f\3\2\5\4\2C\\c|\3\2")
        buf.write("\62;\5\2\13\f\17\17\"\"\2V\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2")
        buf.write("\2\5\36\3\2\2\2\7!\3\2\2\2\t#\3\2\2\2\13%\3\2\2\2\r)\3")
        buf.write("\2\2\2\17,\3\2\2\2\21\60\3\2\2\2\23\62\3\2\2\2\25\64\3")
        buf.write("\2\2\2\27=\3\2\2\2\31M\3\2\2\2\33\34\7?\2\2\34\35\7@\2")
        buf.write("\2\35\4\3\2\2\2\36\37\7k\2\2\37 \7u\2\2 \6\3\2\2\2!\"")
        buf.write("\7*\2\2\"\b\3\2\2\2#$\7+\2\2$\n\3\2\2\2%&\7c\2\2&\'\7")
        buf.write("p\2\2\'(\7f\2\2(\f\3\2\2\2)*\7q\2\2*+\7t\2\2+\16\3\2\2")
        buf.write("\2,-\7p\2\2-.\7q\2\2./\7v\2\2/\20\3\2\2\2\60\61\t\2\2")
        buf.write("\2\61\22\3\2\2\2\62\63\t\3\2\2\63\24\3\2\2\2\64:\5\21")
        buf.write("\t\2\659\5\21\t\2\669\5\23\n\2\679\7a\2\28\65\3\2\2\2")
        buf.write("8\66\3\2\2\28\67\3\2\2\29<\3\2\2\2:8\3\2\2\2:;\3\2\2\2")
        buf.write(";\26\3\2\2\2<:\3\2\2\2=>\7\61\2\2>?\7,\2\2?D\3\2\2\2@")
        buf.write("C\5\27\f\2AC\13\2\2\2B@\3\2\2\2BA\3\2\2\2CF\3\2\2\2DE")
        buf.write("\3\2\2\2DB\3\2\2\2EG\3\2\2\2FD\3\2\2\2GH\7,\2\2HI\7\61")
        buf.write("\2\2IJ\3\2\2\2JK\b\f\2\2K\30\3\2\2\2LN\t\4\2\2ML\3\2\2")
        buf.write("\2NO\3\2\2\2OM\3\2\2\2OP\3\2\2\2PQ\3\2\2\2QR\b\r\2\2R")
        buf.write("\32\3\2\2\2\b\28:BDO\3\b\2\2")
        return buf.getvalue()


class FuzzyLexer(Lexer):
    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

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

    channelNames = [u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = ["<INVALID>",
                    "'=>'", "'is'", "'('", "')'", "'and'", "'or'", "'not'"]

    symbolicNames = ["<INVALID>",
                     "ID", "COMMENT", "WS"]

    ruleNames = ["T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6",
                 "LETTER", "DIGIT", "ID", "COMMENT", "WS"]

    grammarFileName = "Fuzzy.g4"

    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
