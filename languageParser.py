# Generated from ./language.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,37,155,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,4,0,24,8,0,11,0,12,0,25,
        1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,42,8,
        1,1,2,1,2,1,2,1,2,5,2,48,8,2,10,2,12,2,51,9,2,1,2,1,2,1,3,1,3,1,
        3,1,3,5,3,59,8,3,10,3,12,3,62,9,3,1,3,1,3,1,4,1,4,1,4,1,4,5,4,70,
        8,4,10,4,12,4,73,9,4,1,4,1,4,1,5,1,5,5,5,79,8,5,10,5,12,5,82,9,5,
        1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,93,8,6,1,7,1,7,1,7,1,7,1,
        7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,128,8,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,5,9,148,8,9,10,9,12,9,151,9,9,1,10,1,10,1,10,0,1,18,11,0,2,
        4,6,8,10,12,14,16,18,20,0,5,2,0,26,27,30,30,2,0,28,29,31,31,1,0,
        36,37,1,0,32,33,1,0,15,18,172,0,23,1,0,0,0,2,41,1,0,0,0,4,43,1,0,
        0,0,6,54,1,0,0,0,8,65,1,0,0,0,10,76,1,0,0,0,12,85,1,0,0,0,14,94,
        1,0,0,0,16,100,1,0,0,0,18,127,1,0,0,0,20,152,1,0,0,0,22,24,3,2,1,
        0,23,22,1,0,0,0,24,25,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,27,
        1,0,0,0,27,28,5,0,0,1,28,1,1,0,0,0,29,42,5,1,0,0,30,42,3,4,2,0,31,
        32,3,18,9,0,32,33,5,1,0,0,33,42,1,0,0,0,34,42,3,6,3,0,35,42,3,8,
        4,0,36,42,3,10,5,0,37,42,3,12,6,0,38,42,3,14,7,0,39,42,3,16,8,0,
        40,42,5,22,0,0,41,29,1,0,0,0,41,30,1,0,0,0,41,31,1,0,0,0,41,34,1,
        0,0,0,41,35,1,0,0,0,41,36,1,0,0,0,41,37,1,0,0,0,41,38,1,0,0,0,41,
        39,1,0,0,0,41,40,1,0,0,0,42,3,1,0,0,0,43,44,3,20,10,0,44,49,5,24,
        0,0,45,46,5,2,0,0,46,48,5,24,0,0,47,45,1,0,0,0,48,51,1,0,0,0,49,
        47,1,0,0,0,49,50,1,0,0,0,50,52,1,0,0,0,51,49,1,0,0,0,52,53,5,1,0,
        0,53,5,1,0,0,0,54,55,5,3,0,0,55,60,5,24,0,0,56,57,5,2,0,0,57,59,
        5,24,0,0,58,56,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,
        61,63,1,0,0,0,62,60,1,0,0,0,63,64,5,1,0,0,64,7,1,0,0,0,65,66,5,4,
        0,0,66,71,3,18,9,0,67,68,5,2,0,0,68,70,3,18,9,0,69,67,1,0,0,0,70,
        73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,74,1,0,0,0,73,71,1,0,0,
        0,74,75,5,1,0,0,75,9,1,0,0,0,76,80,5,5,0,0,77,79,3,2,1,0,78,77,1,
        0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,83,1,0,0,0,82,
        80,1,0,0,0,83,84,5,6,0,0,84,11,1,0,0,0,85,86,5,7,0,0,86,87,5,8,0,
        0,87,88,3,18,9,0,88,89,5,9,0,0,89,92,3,2,1,0,90,91,5,10,0,0,91,93,
        3,2,1,0,92,90,1,0,0,0,92,93,1,0,0,0,93,13,1,0,0,0,94,95,5,11,0,0,
        95,96,5,8,0,0,96,97,3,18,9,0,97,98,5,9,0,0,98,99,3,2,1,0,99,15,1,
        0,0,0,100,101,5,12,0,0,101,102,5,8,0,0,102,103,3,18,9,0,103,104,
        5,1,0,0,104,105,3,18,9,0,105,106,5,1,0,0,106,107,3,18,9,0,107,108,
        5,9,0,0,108,109,3,2,1,0,109,17,1,0,0,0,110,111,6,9,-1,0,111,112,
        5,29,0,0,112,128,3,18,9,15,113,114,5,13,0,0,114,128,3,18,9,14,115,
        128,5,19,0,0,116,128,5,20,0,0,117,128,5,21,0,0,118,128,5,23,0,0,
        119,128,5,24,0,0,120,121,5,8,0,0,121,122,3,18,9,0,122,123,5,9,0,
        0,123,128,1,0,0,0,124,125,5,24,0,0,125,126,5,14,0,0,126,128,3,18,
        9,1,127,110,1,0,0,0,127,113,1,0,0,0,127,115,1,0,0,0,127,116,1,0,
        0,0,127,117,1,0,0,0,127,118,1,0,0,0,127,119,1,0,0,0,127,120,1,0,
        0,0,127,124,1,0,0,0,128,149,1,0,0,0,129,130,10,13,0,0,130,131,7,
        0,0,0,131,148,3,18,9,14,132,133,10,12,0,0,133,134,7,1,0,0,134,148,
        3,18,9,13,135,136,10,11,0,0,136,137,7,2,0,0,137,148,3,18,9,12,138,
        139,10,10,0,0,139,140,7,3,0,0,140,148,3,18,9,11,141,142,10,9,0,0,
        142,143,5,34,0,0,143,148,3,18,9,10,144,145,10,8,0,0,145,146,5,35,
        0,0,146,148,3,18,9,9,147,129,1,0,0,0,147,132,1,0,0,0,147,135,1,0,
        0,0,147,138,1,0,0,0,147,141,1,0,0,0,147,144,1,0,0,0,148,151,1,0,
        0,0,149,147,1,0,0,0,149,150,1,0,0,0,150,19,1,0,0,0,151,149,1,0,0,
        0,152,153,7,4,0,0,153,21,1,0,0,0,10,25,41,49,60,71,80,92,127,147,
        149
    ]

class languageParser ( Parser ):

    grammarFileName = "language.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "'read'", "'write'", "'{'", 
                     "'}'", "'if'", "'('", "')'", "'else'", "'while'", "'for'", 
                     "'!'", "'='", "'int'", "'float'", "'bool'", "'string'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'*'", "'/'", 
                     "'+'", "'-'", "'%'", "'.'", "'=='", "'!='", "'&&'", 
                     "'||'", "'>'", "'<'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INT_LITERAL", 
                      "FLOAT_LITERAL", "BOOL_LITERAL", "SINGLE_LINE_COMMENT", 
                      "STRING_LITERAL", "IDENTIFIER", "WS", "MUL", "DIV", 
                      "ADD", "SUB", "MOD", "CONCAT", "EQUAL", "NOTEQUAL", 
                      "AND", "OR", "GT", "LT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_declaration = 2
    RULE_read_statement = 3
    RULE_write_statement = 4
    RULE_block = 5
    RULE_conditional = 6
    RULE_while_loop = 7
    RULE_for_loop = 8
    RULE_expression = 9
    RULE_type_keyword = 10

    ruleNames =  [ "program", "statement", "declaration", "read_statement", 
                   "write_statement", "block", "conditional", "while_loop", 
                   "for_loop", "expression", "type_keyword" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    INT_LITERAL=19
    FLOAT_LITERAL=20
    BOOL_LITERAL=21
    SINGLE_LINE_COMMENT=22
    STRING_LITERAL=23
    IDENTIFIER=24
    WS=25
    MUL=26
    DIV=27
    ADD=28
    SUB=29
    MOD=30
    CONCAT=31
    EQUAL=32
    NOTEQUAL=33
    AND=34
    OR=35
    GT=36
    LT=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(languageParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(languageParser.StatementContext)
            else:
                return self.getTypedRuleContext(languageParser.StatementContext,i)


        def getRuleIndex(self):
            return languageParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = languageParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.statement()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 570407354) != 0)):
                    break

            self.state = 27
            self.match(languageParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(languageParser.DeclarationContext,0)


        def expression(self):
            return self.getTypedRuleContext(languageParser.ExpressionContext,0)


        def read_statement(self):
            return self.getTypedRuleContext(languageParser.Read_statementContext,0)


        def write_statement(self):
            return self.getTypedRuleContext(languageParser.Write_statementContext,0)


        def block(self):
            return self.getTypedRuleContext(languageParser.BlockContext,0)


        def conditional(self):
            return self.getTypedRuleContext(languageParser.ConditionalContext,0)


        def while_loop(self):
            return self.getTypedRuleContext(languageParser.While_loopContext,0)


        def for_loop(self):
            return self.getTypedRuleContext(languageParser.For_loopContext,0)


        def SINGLE_LINE_COMMENT(self):
            return self.getToken(languageParser.SINGLE_LINE_COMMENT, 0)

        def getRuleIndex(self):
            return languageParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = languageParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.match(languageParser.T__0)
                pass
            elif token in [15, 16, 17, 18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.declaration()
                pass
            elif token in [8, 13, 19, 20, 21, 23, 24, 29]:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.expression(0)
                self.state = 32
                self.match(languageParser.T__0)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 34
                self.read_statement()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 35
                self.write_statement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 36
                self.block()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 7)
                self.state = 37
                self.conditional()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 8)
                self.state = 38
                self.while_loop()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 9)
                self.state = 39
                self.for_loop()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 10)
                self.state = 40
                self.match(languageParser.SINGLE_LINE_COMMENT)
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


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_keyword(self):
            return self.getTypedRuleContext(languageParser.Type_keywordContext,0)


        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(languageParser.IDENTIFIER)
            else:
                return self.getToken(languageParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return languageParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = languageParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.type_keyword()
            self.state = 44
            self.match(languageParser.IDENTIFIER)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 45
                self.match(languageParser.T__1)
                self.state = 46
                self.match(languageParser.IDENTIFIER)
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(languageParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(languageParser.IDENTIFIER)
            else:
                return self.getToken(languageParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return languageParser.RULE_read_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead_statement" ):
                listener.enterRead_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead_statement" ):
                listener.exitRead_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead_statement" ):
                return visitor.visitRead_statement(self)
            else:
                return visitor.visitChildren(self)




    def read_statement(self):

        localctx = languageParser.Read_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_read_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(languageParser.T__2)
            self.state = 55
            self.match(languageParser.IDENTIFIER)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 56
                self.match(languageParser.T__1)
                self.state = 57
                self.match(languageParser.IDENTIFIER)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 63
            self.match(languageParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Write_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(languageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(languageParser.ExpressionContext,i)


        def getRuleIndex(self):
            return languageParser.RULE_write_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite_statement" ):
                listener.enterWrite_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite_statement" ):
                listener.exitWrite_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite_statement" ):
                return visitor.visitWrite_statement(self)
            else:
                return visitor.visitChildren(self)




    def write_statement(self):

        localctx = languageParser.Write_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_write_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(languageParser.T__3)
            self.state = 66
            self.expression(0)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 67
                self.match(languageParser.T__1)
                self.state = 68
                self.expression(0)
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
            self.match(languageParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(languageParser.StatementContext)
            else:
                return self.getTypedRuleContext(languageParser.StatementContext,i)


        def getRuleIndex(self):
            return languageParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = languageParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(languageParser.T__4)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 570407354) != 0):
                self.state = 77
                self.statement()
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 83
            self.match(languageParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.condition = None # ExpressionContext
            self.if_body = None # StatementContext
            self.else_body = None # StatementContext

        def expression(self):
            return self.getTypedRuleContext(languageParser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(languageParser.StatementContext)
            else:
                return self.getTypedRuleContext(languageParser.StatementContext,i)


        def getRuleIndex(self):
            return languageParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = languageParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_conditional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(languageParser.T__6)
            self.state = 86
            self.match(languageParser.T__7)
            self.state = 87
            localctx.condition = self.expression(0)
            self.state = 88
            self.match(languageParser.T__8)
            self.state = 89
            localctx.if_body = self.statement()
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 90
                self.match(languageParser.T__9)
                self.state = 91
                localctx.else_body = self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.condition = None # ExpressionContext

        def statement(self):
            return self.getTypedRuleContext(languageParser.StatementContext,0)


        def expression(self):
            return self.getTypedRuleContext(languageParser.ExpressionContext,0)


        def getRuleIndex(self):
            return languageParser.RULE_while_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_loop" ):
                listener.enterWhile_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_loop" ):
                listener.exitWhile_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_loop" ):
                return visitor.visitWhile_loop(self)
            else:
                return visitor.visitChildren(self)




    def while_loop(self):

        localctx = languageParser.While_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(languageParser.T__10)
            self.state = 95
            self.match(languageParser.T__7)
            self.state = 96
            localctx.condition = self.expression(0)
            self.state = 97
            self.match(languageParser.T__8)
            self.state = 98
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(languageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(languageParser.ExpressionContext,i)


        def statement(self):
            return self.getTypedRuleContext(languageParser.StatementContext,0)


        def getRuleIndex(self):
            return languageParser.RULE_for_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_loop" ):
                listener.enterFor_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_loop" ):
                listener.exitFor_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop" ):
                return visitor.visitFor_loop(self)
            else:
                return visitor.visitChildren(self)




    def for_loop(self):

        localctx = languageParser.For_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(languageParser.T__11)
            self.state = 101
            self.match(languageParser.T__7)
            self.state = 102
            self.expression(0)
            self.state = 103
            self.match(languageParser.T__0)
            self.state = 104
            self.expression(0)
            self.state = 105
            self.match(languageParser.T__0)
            self.state = 106
            self.expression(0)
            self.state = 107
            self.match(languageParser.T__8)
            self.state = 108
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return languageParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulDivModContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a languageParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(languageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(languageParser.ExpressionContext,i)

        def MUL(self):
            return self.getToken(languageParser.MUL, 0)
        def DIV(self):
            return self.getToken(languageParser.DIV, 0)
        def MOD(self):
            return self.getToken(languageParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivMod" ):
                listener.enterMulDivMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivMod" ):
                listener.exitMulDivMod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivMod" ):
                return visitor.visitMulDivMod(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesesContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a languageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(languageParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentheses" ):
                listener.enterParentheses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentheses" ):
                listener.exitParentheses(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentheses" ):
                return visitor.visitParentheses(self)
            else:
                return visitor.visitChildren(self)


    class LogicalNotContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a languageParser.ExpressionContext
            super().__init__(parser)
            self.prefix = None # Token
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(languageParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalNot" ):
                listener.enterLogicalNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalNot" ):
                listener.exitLogicalNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalNot" ):
                return visitor.visitLogicalNot(self)
            else:
                return visitor.visitChildren(self)


    class EqualNotEqualContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a languageParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(languageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(languageParser.ExpressionContext,i)

        def EQUAL(self):
            return self.getToken(languageParser.EQUAL, 0)
        def NOTEQUAL(self):
            return self.getToken(languageParser.NOTEQUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualNotEqual" ):
                listener.enterEqualNotEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualNotEqual" ):
                listener.exitEqualNotEqual(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualNotEqual" ):
                return visitor.visitEqualNotEqual(self)
            else:
                return visitor.visitChildren(self)


    class AddSubConcatContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a languageParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(languageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(languageParser.ExpressionContext,i)

        def ADD(self):
            return self.getToken(languageParser.ADD, 0)
        def SUB(self):
            return self.getToken(languageParser.SUB, 0)
        def CONCAT(self):
            return self.getToken(languageParser.CONCAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubConcat" ):
                listener.enterAddSubConcat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubConcat" ):
                listener.exitAddSubConcat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubConcat" ):
                return visitor.visitAddSubConcat(self)
            else:
                return visitor.visitChildren(self)


    class AssignmentContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a languageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(languageParser.IDENTIFIER, 0)
        def expression(self):
            return self.getTypedRuleContext(languageParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)


    class IntLiteralContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a languageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT_LITERAL(self):
            return self.getToken(languageParser.INT_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntLiteral" ):
                listener.enterIntLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntLiteral" ):
                listener.exitIntLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntLiteral" ):
                return visitor.visitIntLiteral(self)
            else:
                return visitor.visitChildren(self)


    class LesserGreaterContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a languageParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(languageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(languageParser.ExpressionContext,i)

        def LT(self):
            return self.getToken(languageParser.LT, 0)
        def GT(self):
            return self.getToken(languageParser.GT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLesserGreater" ):
                listener.enterLesserGreater(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLesserGreater" ):
                listener.exitLesserGreater(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLesserGreater" ):
                return visitor.visitLesserGreater(self)
            else:
                return visitor.visitChildren(self)


    class LogicalAndContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a languageParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(languageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(languageParser.ExpressionContext,i)

        def AND(self):
            return self.getToken(languageParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAnd" ):
                listener.enterLogicalAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAnd" ):
                listener.exitLogicalAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAnd" ):
                return visitor.visitLogicalAnd(self)
            else:
                return visitor.visitChildren(self)


    class BoolLiteralContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a languageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL_LITERAL(self):
            return self.getToken(languageParser.BOOL_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolLiteral" ):
                listener.enterBoolLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolLiteral" ):
                listener.exitBoolLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolLiteral" ):
                return visitor.visitBoolLiteral(self)
            else:
                return visitor.visitChildren(self)


    class StringLiteralContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a languageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING_LITERAL(self):
            return self.getToken(languageParser.STRING_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteral" ):
                listener.enterStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteral" ):
                listener.exitStringLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLiteral" ):
                return visitor.visitStringLiteral(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a languageParser.ExpressionContext
            super().__init__(parser)
            self.prefix = None # Token
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(languageParser.ExpressionContext,0)

        def SUB(self):
            return self.getToken(languageParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinus" ):
                listener.enterUnaryMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinus" ):
                listener.exitUnaryMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinus" ):
                return visitor.visitUnaryMinus(self)
            else:
                return visitor.visitChildren(self)


    class FloatLiteralContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a languageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT_LITERAL(self):
            return self.getToken(languageParser.FLOAT_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatLiteral" ):
                listener.enterFloatLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatLiteral" ):
                listener.exitFloatLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatLiteral" ):
                return visitor.visitFloatLiteral(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a languageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(languageParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class LogicalOrContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a languageParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(languageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(languageParser.ExpressionContext,i)

        def OR(self):
            return self.getToken(languageParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOr" ):
                listener.enterLogicalOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOr" ):
                listener.exitLogicalOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOr" ):
                return visitor.visitLogicalOr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = languageParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = languageParser.UnaryMinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 111
                localctx.prefix = self.match(languageParser.SUB)
                self.state = 112
                self.expression(15)
                pass

            elif la_ == 2:
                localctx = languageParser.LogicalNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 113
                localctx.prefix = self.match(languageParser.T__12)
                self.state = 114
                self.expression(14)
                pass

            elif la_ == 3:
                localctx = languageParser.IntLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 115
                self.match(languageParser.INT_LITERAL)
                pass

            elif la_ == 4:
                localctx = languageParser.FloatLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 116
                self.match(languageParser.FLOAT_LITERAL)
                pass

            elif la_ == 5:
                localctx = languageParser.BoolLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 117
                self.match(languageParser.BOOL_LITERAL)
                pass

            elif la_ == 6:
                localctx = languageParser.StringLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 118
                self.match(languageParser.STRING_LITERAL)
                pass

            elif la_ == 7:
                localctx = languageParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 119
                self.match(languageParser.IDENTIFIER)
                pass

            elif la_ == 8:
                localctx = languageParser.ParenthesesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 120
                self.match(languageParser.T__7)
                self.state = 121
                self.expression(0)
                self.state = 122
                self.match(languageParser.T__8)
                pass

            elif la_ == 9:
                localctx = languageParser.AssignmentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 124
                self.match(languageParser.IDENTIFIER)
                self.state = 125
                self.match(languageParser.T__13)
                self.state = 126
                self.expression(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 149
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 147
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = languageParser.MulDivModContext(self, languageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 129
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 130
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1275068416) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 131
                        self.expression(14)
                        pass

                    elif la_ == 2:
                        localctx = languageParser.AddSubConcatContext(self, languageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 132
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 133
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2952790016) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 134
                        self.expression(13)
                        pass

                    elif la_ == 3:
                        localctx = languageParser.LesserGreaterContext(self, languageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 135
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 136
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==36 or _la==37):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 137
                        self.expression(12)
                        pass

                    elif la_ == 4:
                        localctx = languageParser.EqualNotEqualContext(self, languageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 138
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 139
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==32 or _la==33):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 140
                        self.expression(11)
                        pass

                    elif la_ == 5:
                        localctx = languageParser.LogicalAndContext(self, languageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 141
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 142
                        localctx.op = self.match(languageParser.AND)
                        self.state = 143
                        self.expression(10)
                        pass

                    elif la_ == 6:
                        localctx = languageParser.LogicalOrContext(self, languageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 144
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 145
                        localctx.op = self.match(languageParser.OR)
                        self.state = 146
                        self.expression(9)
                        pass

             
                self.state = 151
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Type_keywordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return languageParser.RULE_type_keyword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_keyword" ):
                listener.enterType_keyword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_keyword" ):
                listener.exitType_keyword(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_keyword" ):
                return visitor.visitType_keyword(self)
            else:
                return visitor.visitChildren(self)




    def type_keyword(self):

        localctx = languageParser.Type_keywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_type_keyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 491520) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 8)
         




