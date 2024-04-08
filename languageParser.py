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
        4,1,36,175,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,4,0,
        28,8,0,11,0,12,0,29,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,3,1,45,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,56,8,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,5,2,76,8,2,10,2,12,2,79,9,2,1,3,1,3,1,3,1,3,1,4,1,4,1,
        4,1,4,1,4,5,4,90,8,4,10,4,12,4,93,9,4,1,4,5,4,96,8,4,10,4,12,4,99,
        9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,5,5,108,8,5,10,5,12,5,111,9,5,1,
        5,1,5,1,6,1,6,1,6,1,6,1,6,5,6,120,8,6,10,6,12,6,123,9,6,1,6,1,6,
        1,7,1,7,5,7,129,8,7,10,7,12,7,132,9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,3,8,143,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,5,10,153,
        8,10,10,10,12,10,156,9,10,1,10,1,10,5,10,160,8,10,10,10,12,10,163,
        9,10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,1,12,3,12,173,8,12,1,12,
        0,1,4,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,5,2,0,31,32,35,35,2,
        0,33,34,36,36,1,0,2,3,1,0,4,5,1,0,20,23,192,0,27,1,0,0,0,2,44,1,
        0,0,0,4,55,1,0,0,0,6,80,1,0,0,0,8,84,1,0,0,0,10,102,1,0,0,0,12,114,
        1,0,0,0,14,126,1,0,0,0,16,135,1,0,0,0,18,144,1,0,0,0,20,150,1,0,
        0,0,22,166,1,0,0,0,24,172,1,0,0,0,26,28,3,2,1,0,27,26,1,0,0,0,28,
        29,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,31,1,0,0,0,31,32,5,0,0,
        1,32,1,1,0,0,0,33,45,5,1,0,0,34,45,3,8,4,0,35,36,3,4,2,0,36,37,5,
        1,0,0,37,45,1,0,0,0,38,45,3,10,5,0,39,45,3,12,6,0,40,45,3,14,7,0,
        41,45,3,16,8,0,42,45,3,18,9,0,43,45,5,27,0,0,44,33,1,0,0,0,44,34,
        1,0,0,0,44,35,1,0,0,0,44,38,1,0,0,0,44,39,1,0,0,0,44,40,1,0,0,0,
        44,41,1,0,0,0,44,42,1,0,0,0,44,43,1,0,0,0,45,3,1,0,0,0,46,47,6,2,
        -1,0,47,48,5,34,0,0,48,56,3,4,2,12,49,50,5,33,0,0,50,56,3,4,2,11,
        51,56,3,6,3,0,52,56,3,20,10,0,53,56,5,29,0,0,54,56,3,24,12,0,55,
        46,1,0,0,0,55,49,1,0,0,0,55,51,1,0,0,0,55,52,1,0,0,0,55,53,1,0,0,
        0,55,54,1,0,0,0,56,77,1,0,0,0,57,58,10,10,0,0,58,59,7,0,0,0,59,76,
        3,4,2,11,60,61,10,9,0,0,61,62,7,1,0,0,62,76,3,4,2,10,63,64,10,8,
        0,0,64,65,7,2,0,0,65,76,3,4,2,9,66,67,10,7,0,0,67,68,7,3,0,0,68,
        76,3,4,2,8,69,70,10,6,0,0,70,71,5,6,0,0,71,76,3,4,2,7,72,73,10,5,
        0,0,73,74,5,7,0,0,74,76,3,4,2,6,75,57,1,0,0,0,75,60,1,0,0,0,75,63,
        1,0,0,0,75,66,1,0,0,0,75,69,1,0,0,0,75,72,1,0,0,0,76,79,1,0,0,0,
        77,75,1,0,0,0,77,78,1,0,0,0,78,5,1,0,0,0,79,77,1,0,0,0,80,81,5,8,
        0,0,81,82,3,4,2,0,82,83,5,9,0,0,83,7,1,0,0,0,84,85,3,22,11,0,85,
        86,5,10,0,0,86,97,5,29,0,0,87,91,5,11,0,0,88,90,5,10,0,0,89,88,1,
        0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,94,1,0,0,0,93,
        91,1,0,0,0,94,96,5,29,0,0,95,87,1,0,0,0,96,99,1,0,0,0,97,95,1,0,
        0,0,97,98,1,0,0,0,98,100,1,0,0,0,99,97,1,0,0,0,100,101,5,1,0,0,101,
        9,1,0,0,0,102,103,5,12,0,0,103,104,5,10,0,0,104,109,5,29,0,0,105,
        106,5,11,0,0,106,108,5,29,0,0,107,105,1,0,0,0,108,111,1,0,0,0,109,
        107,1,0,0,0,109,110,1,0,0,0,110,112,1,0,0,0,111,109,1,0,0,0,112,
        113,5,1,0,0,113,11,1,0,0,0,114,115,5,13,0,0,115,116,5,10,0,0,116,
        121,3,4,2,0,117,118,5,11,0,0,118,120,3,4,2,0,119,117,1,0,0,0,120,
        123,1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,124,1,0,0,0,123,
        121,1,0,0,0,124,125,5,1,0,0,125,13,1,0,0,0,126,130,5,14,0,0,127,
        129,3,2,1,0,128,127,1,0,0,0,129,132,1,0,0,0,130,128,1,0,0,0,130,
        131,1,0,0,0,131,133,1,0,0,0,132,130,1,0,0,0,133,134,5,15,0,0,134,
        15,1,0,0,0,135,136,5,16,0,0,136,137,5,8,0,0,137,138,3,4,2,0,138,
        139,5,9,0,0,139,142,3,2,1,0,140,141,5,17,0,0,141,143,3,2,1,0,142,
        140,1,0,0,0,142,143,1,0,0,0,143,17,1,0,0,0,144,145,5,18,0,0,145,
        146,5,8,0,0,146,147,3,4,2,0,147,148,5,9,0,0,148,149,3,2,1,0,149,
        19,1,0,0,0,150,154,5,29,0,0,151,153,5,10,0,0,152,151,1,0,0,0,153,
        156,1,0,0,0,154,152,1,0,0,0,154,155,1,0,0,0,155,157,1,0,0,0,156,
        154,1,0,0,0,157,161,5,19,0,0,158,160,5,10,0,0,159,158,1,0,0,0,160,
        163,1,0,0,0,161,159,1,0,0,0,161,162,1,0,0,0,162,164,1,0,0,0,163,
        161,1,0,0,0,164,165,3,4,2,0,165,21,1,0,0,0,166,167,7,4,0,0,167,23,
        1,0,0,0,168,173,5,24,0,0,169,173,5,25,0,0,170,173,5,26,0,0,171,173,
        5,28,0,0,172,168,1,0,0,0,172,169,1,0,0,0,172,170,1,0,0,0,172,171,
        1,0,0,0,173,25,1,0,0,0,14,29,44,55,75,77,91,97,109,121,130,142,154,
        161,172
    ]

class languageParser ( Parser ):

    grammarFileName = "language.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'<'", "'>'", "'=='", "'!='", "'&&'", 
                     "'||'", "'('", "')'", "' '", "','", "'read'", "'write'", 
                     "'{'", "'}'", "'if'", "'else'", "'while'", "'='", "'int'", 
                     "'float'", "'bool'", "'string'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'*'", "'/'", "'+'", "'-'", "'%'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT", "FLOAT", "BOOL", "ONE_LINE_COMMENT", "STRING", 
                      "IDENTIFIER", "WS", "MUL", "DIV", "ADD", "SUB", "MOD", 
                      "CONCAT" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_expression = 2
    RULE_parantheses = 3
    RULE_declaration = 4
    RULE_read = 5
    RULE_write = 6
    RULE_block = 7
    RULE_condition = 8
    RULE_while_loop = 9
    RULE_assignment = 10
    RULE_type = 11
    RULE_literal = 12

    ruleNames =  [ "prog", "statement", "expression", "parantheses", "declaration", 
                   "read", "write", "block", "condition", "while_loop", 
                   "assignment", "type", "literal" ]

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
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    INT=24
    FLOAT=25
    BOOL=26
    ONE_LINE_COMMENT=27
    STRING=28
    IDENTIFIER=29
    WS=30
    MUL=31
    DIV=32
    ADD=33
    SUB=34
    MOD=35
    CONCAT=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
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
            return languageParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = languageParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.statement()
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 26842853634) != 0)):
                    break

            self.state = 31
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


        def read(self):
            return self.getTypedRuleContext(languageParser.ReadContext,0)


        def write(self):
            return self.getTypedRuleContext(languageParser.WriteContext,0)


        def block(self):
            return self.getTypedRuleContext(languageParser.BlockContext,0)


        def condition(self):
            return self.getTypedRuleContext(languageParser.ConditionContext,0)


        def while_loop(self):
            return self.getTypedRuleContext(languageParser.While_loopContext,0)


        def ONE_LINE_COMMENT(self):
            return self.getToken(languageParser.ONE_LINE_COMMENT, 0)

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
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.match(languageParser.T__0)
                pass
            elif token in [20, 21, 22, 23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.declaration()
                pass
            elif token in [8, 24, 25, 26, 28, 29, 33, 34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.expression(0)
                self.state = 36
                self.match(languageParser.T__0)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 38
                self.read()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 5)
                self.state = 39
                self.write()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 6)
                self.state = 40
                self.block()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 7)
                self.state = 41
                self.condition()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 8)
                self.state = 42
                self.while_loop()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 9)
                self.state = 43
                self.match(languageParser.ONE_LINE_COMMENT)
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


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # ExpressionContext
            self.prefix = None # Token
            self.op = None # Token
            self.right = None # ExpressionContext

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(languageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(languageParser.ExpressionContext,i)


        def SUB(self):
            return self.getToken(languageParser.SUB, 0)

        def ADD(self):
            return self.getToken(languageParser.ADD, 0)

        def parantheses(self):
            return self.getTypedRuleContext(languageParser.ParanthesesContext,0)


        def assignment(self):
            return self.getTypedRuleContext(languageParser.AssignmentContext,0)


        def IDENTIFIER(self):
            return self.getToken(languageParser.IDENTIFIER, 0)

        def literal(self):
            return self.getTypedRuleContext(languageParser.LiteralContext,0)


        def MUL(self):
            return self.getToken(languageParser.MUL, 0)

        def DIV(self):
            return self.getToken(languageParser.DIV, 0)

        def MOD(self):
            return self.getToken(languageParser.MOD, 0)

        def CONCAT(self):
            return self.getToken(languageParser.CONCAT, 0)

        def getRuleIndex(self):
            return languageParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = languageParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 47
                localctx.prefix = self.match(languageParser.SUB)
                self.state = 48
                self.expression(12)
                pass

            elif la_ == 2:
                self.state = 49
                localctx.prefix = self.match(languageParser.ADD)
                self.state = 50
                self.expression(11)
                pass

            elif la_ == 3:
                self.state = 51
                self.parantheses()
                pass

            elif la_ == 4:
                self.state = 52
                self.assignment()
                pass

            elif la_ == 5:
                self.state = 53
                self.match(languageParser.IDENTIFIER)
                pass

            elif la_ == 6:
                self.state = 54
                self.literal()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 77
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 75
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = languageParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 57
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 58
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 40802189312) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 59
                        localctx.right = self.expression(11)
                        pass

                    elif la_ == 2:
                        localctx = languageParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 60
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 61
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 94489280512) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 62
                        localctx.right = self.expression(10)
                        pass

                    elif la_ == 3:
                        localctx = languageParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 63
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 64
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==2 or _la==3):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 65
                        localctx.right = self.expression(9)
                        pass

                    elif la_ == 4:
                        localctx = languageParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 66
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 67
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==5):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 68
                        localctx.right = self.expression(8)
                        pass

                    elif la_ == 5:
                        localctx = languageParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 69
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 70
                        localctx.op = self.match(languageParser.T__5)
                        self.state = 71
                        localctx.right = self.expression(7)
                        pass

                    elif la_ == 6:
                        localctx = languageParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 72
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 73
                        localctx.op = self.match(languageParser.T__6)
                        self.state = 74
                        localctx.right = self.expression(6)
                        pass

             
                self.state = 79
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ParanthesesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(languageParser.ExpressionContext,0)


        def getRuleIndex(self):
            return languageParser.RULE_parantheses

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParantheses" ):
                listener.enterParantheses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParantheses" ):
                listener.exitParantheses(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParantheses" ):
                return visitor.visitParantheses(self)
            else:
                return visitor.visitChildren(self)




    def parantheses(self):

        localctx = languageParser.ParanthesesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_parantheses)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(languageParser.T__7)
            self.state = 81
            self.expression(0)
            self.state = 82
            self.match(languageParser.T__8)
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

        def type_(self):
            return self.getTypedRuleContext(languageParser.TypeContext,0)


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
        self.enterRule(localctx, 8, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.type_()
            self.state = 85
            self.match(languageParser.T__9)
            self.state = 86
            self.match(languageParser.IDENTIFIER)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 87
                self.match(languageParser.T__10)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 88
                    self.match(languageParser.T__9)
                    self.state = 93
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 94
                self.match(languageParser.IDENTIFIER)
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100
            self.match(languageParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadContext(ParserRuleContext):
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
            return languageParser.RULE_read

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead" ):
                return visitor.visitRead(self)
            else:
                return visitor.visitChildren(self)




    def read(self):

        localctx = languageParser.ReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_read)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(languageParser.T__11)
            self.state = 103
            self.match(languageParser.T__9)
            self.state = 104
            self.match(languageParser.IDENTIFIER)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 105
                self.match(languageParser.T__10)
                self.state = 106
                self.match(languageParser.IDENTIFIER)
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 112
            self.match(languageParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteContext(ParserRuleContext):
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
            return languageParser.RULE_write

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite" ):
                listener.enterWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite" ):
                listener.exitWrite(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)




    def write(self):

        localctx = languageParser.WriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_write)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(languageParser.T__12)
            self.state = 115
            self.match(languageParser.T__9)
            self.state = 116
            self.expression(0)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 117
                self.match(languageParser.T__10)
                self.state = 118
                self.expression(0)
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
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
        self.enterRule(localctx, 14, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(languageParser.T__13)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 26842853634) != 0):
                self.state = 127
                self.statement()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 133
            self.match(languageParser.T__14)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(languageParser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(languageParser.StatementContext)
            else:
                return self.getTypedRuleContext(languageParser.StatementContext,i)


        def getRuleIndex(self):
            return languageParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = languageParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(languageParser.T__15)
            self.state = 136
            self.match(languageParser.T__7)
            self.state = 137
            self.expression(0)
            self.state = 138
            self.match(languageParser.T__8)
            self.state = 139
            self.statement()
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 140
                self.match(languageParser.T__16)
                self.state = 141
                self.statement()


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

        def expression(self):
            return self.getTypedRuleContext(languageParser.ExpressionContext,0)


        def statement(self):
            return self.getTypedRuleContext(languageParser.StatementContext,0)


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
        self.enterRule(localctx, 18, self.RULE_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(languageParser.T__17)
            self.state = 145
            self.match(languageParser.T__7)
            self.state = 146
            self.expression(0)
            self.state = 147
            self.match(languageParser.T__8)
            self.state = 148
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(languageParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(languageParser.ExpressionContext,0)


        def getRuleIndex(self):
            return languageParser.RULE_assignment

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




    def assignment(self):

        localctx = languageParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(languageParser.IDENTIFIER)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 151
                self.match(languageParser.T__9)
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 157
            self.match(languageParser.T__18)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 158
                self.match(languageParser.T__9)
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 164
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return languageParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = languageParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15728640) != 0)):
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


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return languageParser.RULE_literal

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BoolContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a languageParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(languageParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool" ):
                return visitor.visitBool(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a languageParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(languageParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class FloatContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a languageParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(languageParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a languageParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(languageParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def literal(self):

        localctx = languageParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_literal)
        try:
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                localctx = languageParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.match(languageParser.INT)
                pass
            elif token in [25]:
                localctx = languageParser.FloatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.match(languageParser.FLOAT)
                pass
            elif token in [26]:
                localctx = languageParser.BoolContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 170
                self.match(languageParser.BOOL)
                pass
            elif token in [28]:
                localctx = languageParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 171
                self.match(languageParser.STRING)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         




