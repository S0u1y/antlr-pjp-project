# Generated from language.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .languageParser import languageParser
else:
    from languageParser import languageParser

# This class defines a complete listener for a parse tree produced by languageParser.
class languageListener(ParseTreeListener):

    # Enter a parse tree produced by languageParser#prog.
    def enterProg(self, ctx:languageParser.ProgContext):
        pass

    # Exit a parse tree produced by languageParser#prog.
    def exitProg(self, ctx:languageParser.ProgContext):
        pass


    # Enter a parse tree produced by languageParser#expr.
    def enterExpr(self, ctx:languageParser.ExprContext):
        pass

    # Exit a parse tree produced by languageParser#expr.
    def exitExpr(self, ctx:languageParser.ExprContext):
        pass



del languageParser