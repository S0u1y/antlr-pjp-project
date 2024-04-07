# Generated from ./language.g4 by ANTLR 4.13.1
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


    # Enter a parse tree produced by languageParser#statement.
    def enterStatement(self, ctx:languageParser.StatementContext):
        pass

    # Exit a parse tree produced by languageParser#statement.
    def exitStatement(self, ctx:languageParser.StatementContext):
        pass


    # Enter a parse tree produced by languageParser#expression.
    def enterExpression(self, ctx:languageParser.ExpressionContext):
        pass

    # Exit a parse tree produced by languageParser#expression.
    def exitExpression(self, ctx:languageParser.ExpressionContext):
        pass


    # Enter a parse tree produced by languageParser#parantheses.
    def enterParantheses(self, ctx:languageParser.ParanthesesContext):
        pass

    # Exit a parse tree produced by languageParser#parantheses.
    def exitParantheses(self, ctx:languageParser.ParanthesesContext):
        pass


    # Enter a parse tree produced by languageParser#declaration.
    def enterDeclaration(self, ctx:languageParser.DeclarationContext):
        pass

    # Exit a parse tree produced by languageParser#declaration.
    def exitDeclaration(self, ctx:languageParser.DeclarationContext):
        pass


    # Enter a parse tree produced by languageParser#read.
    def enterRead(self, ctx:languageParser.ReadContext):
        pass

    # Exit a parse tree produced by languageParser#read.
    def exitRead(self, ctx:languageParser.ReadContext):
        pass


    # Enter a parse tree produced by languageParser#write.
    def enterWrite(self, ctx:languageParser.WriteContext):
        pass

    # Exit a parse tree produced by languageParser#write.
    def exitWrite(self, ctx:languageParser.WriteContext):
        pass


    # Enter a parse tree produced by languageParser#block.
    def enterBlock(self, ctx:languageParser.BlockContext):
        pass

    # Exit a parse tree produced by languageParser#block.
    def exitBlock(self, ctx:languageParser.BlockContext):
        pass


    # Enter a parse tree produced by languageParser#condition.
    def enterCondition(self, ctx:languageParser.ConditionContext):
        pass

    # Exit a parse tree produced by languageParser#condition.
    def exitCondition(self, ctx:languageParser.ConditionContext):
        pass


    # Enter a parse tree produced by languageParser#while_loop.
    def enterWhile_loop(self, ctx:languageParser.While_loopContext):
        pass

    # Exit a parse tree produced by languageParser#while_loop.
    def exitWhile_loop(self, ctx:languageParser.While_loopContext):
        pass


    # Enter a parse tree produced by languageParser#assignment.
    def enterAssignment(self, ctx:languageParser.AssignmentContext):
        pass

    # Exit a parse tree produced by languageParser#assignment.
    def exitAssignment(self, ctx:languageParser.AssignmentContext):
        pass


    # Enter a parse tree produced by languageParser#type.
    def enterType(self, ctx:languageParser.TypeContext):
        pass

    # Exit a parse tree produced by languageParser#type.
    def exitType(self, ctx:languageParser.TypeContext):
        pass


    # Enter a parse tree produced by languageParser#int.
    def enterInt(self, ctx:languageParser.IntContext):
        pass

    # Exit a parse tree produced by languageParser#int.
    def exitInt(self, ctx:languageParser.IntContext):
        pass


    # Enter a parse tree produced by languageParser#float.
    def enterFloat(self, ctx:languageParser.FloatContext):
        pass

    # Exit a parse tree produced by languageParser#float.
    def exitFloat(self, ctx:languageParser.FloatContext):
        pass


    # Enter a parse tree produced by languageParser#bool.
    def enterBool(self, ctx:languageParser.BoolContext):
        pass

    # Exit a parse tree produced by languageParser#bool.
    def exitBool(self, ctx:languageParser.BoolContext):
        pass


    # Enter a parse tree produced by languageParser#string.
    def enterString(self, ctx:languageParser.StringContext):
        pass

    # Exit a parse tree produced by languageParser#string.
    def exitString(self, ctx:languageParser.StringContext):
        pass



del languageParser