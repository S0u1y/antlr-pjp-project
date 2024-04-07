# Generated from ./language.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .languageParser import languageParser
else:
    from languageParser import languageParser

# This class defines a complete generic visitor for a parse tree produced by languageParser.

class languageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by languageParser#prog.
    def visitProg(self, ctx:languageParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#statement.
    def visitStatement(self, ctx:languageParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#expression.
    def visitExpression(self, ctx:languageParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#parantheses.
    def visitParantheses(self, ctx:languageParser.ParanthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#declaration.
    def visitDeclaration(self, ctx:languageParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#read.
    def visitRead(self, ctx:languageParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#write.
    def visitWrite(self, ctx:languageParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#block.
    def visitBlock(self, ctx:languageParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#condition.
    def visitCondition(self, ctx:languageParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#while_loop.
    def visitWhile_loop(self, ctx:languageParser.While_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#assignment.
    def visitAssignment(self, ctx:languageParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#type.
    def visitType(self, ctx:languageParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#int.
    def visitInt(self, ctx:languageParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#float.
    def visitFloat(self, ctx:languageParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#bool.
    def visitBool(self, ctx:languageParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#string.
    def visitString(self, ctx:languageParser.StringContext):
        return self.visitChildren(ctx)



del languageParser