# Generated from ./language.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,35,238,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,
        1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,
        1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,
        1,13,1,13,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,
        1,16,1,16,1,16,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,
        1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,22,1,22,1,23,1,23,5,23,155,8,23,10,23,12,23,158,9,23,1,23,
        3,23,161,8,23,1,24,4,24,164,8,24,11,24,12,24,165,1,24,1,24,4,24,
        170,8,24,11,24,12,24,171,1,24,1,24,4,24,176,8,24,11,24,12,24,177,
        3,24,180,8,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,
        191,8,25,1,26,1,26,1,26,1,26,5,26,197,8,26,10,26,12,26,200,9,26,
        1,26,1,26,1,27,1,27,5,27,206,8,27,10,27,12,27,209,9,27,1,27,1,27,
        1,28,1,28,5,28,215,8,28,10,28,12,28,218,9,28,1,29,4,29,221,8,29,
        11,29,12,29,222,1,29,1,29,1,30,1,30,1,31,1,31,1,32,1,32,1,33,1,33,
        1,34,1,34,1,35,1,35,0,0,36,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,
        9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,
        20,41,21,43,22,45,0,47,23,49,24,51,25,53,26,55,27,57,28,59,29,61,
        30,63,31,65,32,67,33,69,34,71,35,1,0,7,2,0,65,90,97,122,1,0,49,57,
        1,0,48,57,2,0,10,10,13,13,4,0,10,10,13,13,34,34,92,92,3,0,48,57,
        65,90,97,122,2,0,9,10,13,13,247,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,
        0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,
        0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,
        0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,
        0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,47,1,0,0,
        0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,
        0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,
        0,0,69,1,0,0,0,0,71,1,0,0,0,1,73,1,0,0,0,3,75,1,0,0,0,5,77,1,0,0,
        0,7,79,1,0,0,0,9,82,1,0,0,0,11,85,1,0,0,0,13,88,1,0,0,0,15,91,1,
        0,0,0,17,93,1,0,0,0,19,95,1,0,0,0,21,97,1,0,0,0,23,102,1,0,0,0,25,
        108,1,0,0,0,27,110,1,0,0,0,29,112,1,0,0,0,31,115,1,0,0,0,33,120,
        1,0,0,0,35,126,1,0,0,0,37,128,1,0,0,0,39,132,1,0,0,0,41,138,1,0,
        0,0,43,143,1,0,0,0,45,150,1,0,0,0,47,160,1,0,0,0,49,179,1,0,0,0,
        51,190,1,0,0,0,53,192,1,0,0,0,55,203,1,0,0,0,57,212,1,0,0,0,59,220,
        1,0,0,0,61,226,1,0,0,0,63,228,1,0,0,0,65,230,1,0,0,0,67,232,1,0,
        0,0,69,234,1,0,0,0,71,236,1,0,0,0,73,74,5,59,0,0,74,2,1,0,0,0,75,
        76,5,60,0,0,76,4,1,0,0,0,77,78,5,62,0,0,78,6,1,0,0,0,79,80,5,61,
        0,0,80,81,5,61,0,0,81,8,1,0,0,0,82,83,5,33,0,0,83,84,5,61,0,0,84,
        10,1,0,0,0,85,86,5,38,0,0,86,87,5,38,0,0,87,12,1,0,0,0,88,89,5,124,
        0,0,89,90,5,124,0,0,90,14,1,0,0,0,91,92,5,40,0,0,92,16,1,0,0,0,93,
        94,5,41,0,0,94,18,1,0,0,0,95,96,5,44,0,0,96,20,1,0,0,0,97,98,5,114,
        0,0,98,99,5,101,0,0,99,100,5,97,0,0,100,101,5,100,0,0,101,22,1,0,
        0,0,102,103,5,119,0,0,103,104,5,114,0,0,104,105,5,105,0,0,105,106,
        5,116,0,0,106,107,5,101,0,0,107,24,1,0,0,0,108,109,5,123,0,0,109,
        26,1,0,0,0,110,111,5,125,0,0,111,28,1,0,0,0,112,113,5,105,0,0,113,
        114,5,102,0,0,114,30,1,0,0,0,115,116,5,101,0,0,116,117,5,108,0,0,
        117,118,5,115,0,0,118,119,5,101,0,0,119,32,1,0,0,0,120,121,5,119,
        0,0,121,122,5,104,0,0,122,123,5,105,0,0,123,124,5,108,0,0,124,125,
        5,101,0,0,125,34,1,0,0,0,126,127,5,61,0,0,127,36,1,0,0,0,128,129,
        5,105,0,0,129,130,5,110,0,0,130,131,5,116,0,0,131,38,1,0,0,0,132,
        133,5,102,0,0,133,134,5,108,0,0,134,135,5,111,0,0,135,136,5,97,0,
        0,136,137,5,116,0,0,137,40,1,0,0,0,138,139,5,98,0,0,139,140,5,111,
        0,0,140,141,5,111,0,0,141,142,5,108,0,0,142,42,1,0,0,0,143,144,5,
        115,0,0,144,145,5,116,0,0,145,146,5,114,0,0,146,147,5,105,0,0,147,
        148,5,110,0,0,148,149,5,103,0,0,149,44,1,0,0,0,150,151,7,0,0,0,151,
        46,1,0,0,0,152,156,7,1,0,0,153,155,7,2,0,0,154,153,1,0,0,0,155,158,
        1,0,0,0,156,154,1,0,0,0,156,157,1,0,0,0,157,161,1,0,0,0,158,156,
        1,0,0,0,159,161,5,48,0,0,160,152,1,0,0,0,160,159,1,0,0,0,161,48,
        1,0,0,0,162,164,7,2,0,0,163,162,1,0,0,0,164,165,1,0,0,0,165,163,
        1,0,0,0,165,166,1,0,0,0,166,167,1,0,0,0,167,169,5,46,0,0,168,170,
        7,2,0,0,169,168,1,0,0,0,170,171,1,0,0,0,171,169,1,0,0,0,171,172,
        1,0,0,0,172,180,1,0,0,0,173,175,5,46,0,0,174,176,7,1,0,0,175,174,
        1,0,0,0,176,177,1,0,0,0,177,175,1,0,0,0,177,178,1,0,0,0,178,180,
        1,0,0,0,179,163,1,0,0,0,179,173,1,0,0,0,180,50,1,0,0,0,181,182,5,
        116,0,0,182,183,5,114,0,0,183,184,5,117,0,0,184,191,5,101,0,0,185,
        186,5,102,0,0,186,187,5,97,0,0,187,188,5,108,0,0,188,189,5,115,0,
        0,189,191,5,101,0,0,190,181,1,0,0,0,190,185,1,0,0,0,191,52,1,0,0,
        0,192,193,5,47,0,0,193,194,5,47,0,0,194,198,1,0,0,0,195,197,8,3,
        0,0,196,195,1,0,0,0,197,200,1,0,0,0,198,196,1,0,0,0,198,199,1,0,
        0,0,199,201,1,0,0,0,200,198,1,0,0,0,201,202,6,26,0,0,202,54,1,0,
        0,0,203,207,5,34,0,0,204,206,8,4,0,0,205,204,1,0,0,0,206,209,1,0,
        0,0,207,205,1,0,0,0,207,208,1,0,0,0,208,210,1,0,0,0,209,207,1,0,
        0,0,210,211,5,34,0,0,211,56,1,0,0,0,212,216,7,0,0,0,213,215,7,5,
        0,0,214,213,1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,0,216,217,1,0,
        0,0,217,58,1,0,0,0,218,216,1,0,0,0,219,221,7,6,0,0,220,219,1,0,0,
        0,221,222,1,0,0,0,222,220,1,0,0,0,222,223,1,0,0,0,223,224,1,0,0,
        0,224,225,6,29,0,0,225,60,1,0,0,0,226,227,5,42,0,0,227,62,1,0,0,
        0,228,229,5,47,0,0,229,64,1,0,0,0,230,231,5,43,0,0,231,66,1,0,0,
        0,232,233,5,45,0,0,233,68,1,0,0,0,234,235,5,37,0,0,235,70,1,0,0,
        0,236,237,5,46,0,0,237,72,1,0,0,0,13,0,156,160,165,171,177,179,190,
        198,207,214,216,222,1,6,0,0
    ]

class languageLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

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
    INT = 23
    FLOAT = 24
    BOOL = 25
    ONE_LINE_COMMENT = 26
    STRING = 27
    IDENTIFIER = 28
    WS = 29
    MUL = 30
    DIV = 31
    ADD = 32
    SUB = 33
    MOD = 34
    CONCAT = 35

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'<'", "'>'", "'=='", "'!='", "'&&'", "'||'", "'('", 
            "')'", "','", "'read'", "'write'", "'{'", "'}'", "'if'", "'else'", 
            "'while'", "'='", "'int'", "'float'", "'bool'", "'string'", 
            "'*'", "'/'", "'+'", "'-'", "'%'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "BOOL", "ONE_LINE_COMMENT", "STRING", "IDENTIFIER", 
            "WS", "MUL", "DIV", "ADD", "SUB", "MOD", "CONCAT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "CHARACTER", "INT", "FLOAT", "BOOL", 
                  "ONE_LINE_COMMENT", "STRING", "IDENTIFIER", "WS", "MUL", 
                  "DIV", "ADD", "SUB", "MOD", "CONCAT" ]

    grammarFileName = "language.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

