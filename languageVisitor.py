# Generated from language.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .languageParser import languageParser
else:
    from languageParser import languageParser

# This class defines a complete generic visitor for a parse tree produced by languageParser.

class languageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by languageParser#program.
    def visitProgram(self, ctx:languageParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#statement.
    def visitStatement(self, ctx:languageParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#declaration.
    def visitDeclaration(self, ctx:languageParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#read_statement.
    def visitRead_statement(self, ctx:languageParser.Read_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#write_statement.
    def visitWrite_statement(self, ctx:languageParser.Write_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#block.
    def visitBlock(self, ctx:languageParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#conditional.
    def visitConditional(self, ctx:languageParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#while_loop.
    def visitWhile_loop(self, ctx:languageParser.While_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#for_loop.
    def visitFor_loop(self, ctx:languageParser.For_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#glF.
    def visitGlF(self, ctx:languageParser.GlFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#mulDivMod.
    def visitMulDivMod(self, ctx:languageParser.MulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#parentheses.
    def visitParentheses(self, ctx:languageParser.ParenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#logicalNot.
    def visitLogicalNot(self, ctx:languageParser.LogicalNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#equalNotEqual.
    def visitEqualNotEqual(self, ctx:languageParser.EqualNotEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#glI.
    def visitGlI(self, ctx:languageParser.GlIContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#addSubConcat.
    def visitAddSubConcat(self, ctx:languageParser.AddSubConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#eqS.
    def visitEqS(self, ctx:languageParser.EqSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#assignment.
    def visitAssignment(self, ctx:languageParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#intLiteral.
    def visitIntLiteral(self, ctx:languageParser.IntLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#lesserGreater.
    def visitLesserGreater(self, ctx:languageParser.LesserGreaterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#logicalAnd.
    def visitLogicalAnd(self, ctx:languageParser.LogicalAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#boolLiteral.
    def visitBoolLiteral(self, ctx:languageParser.BoolLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#glS.
    def visitGlS(self, ctx:languageParser.GlSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#stringLiteral.
    def visitStringLiteral(self, ctx:languageParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#eqB.
    def visitEqB(self, ctx:languageParser.EqBContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#unaryMinus.
    def visitUnaryMinus(self, ctx:languageParser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#floatLiteral.
    def visitFloatLiteral(self, ctx:languageParser.FloatLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#eqF.
    def visitEqF(self, ctx:languageParser.EqFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#id.
    def visitId(self, ctx:languageParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#eqI.
    def visitEqI(self, ctx:languageParser.EqIContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#logicalOr.
    def visitLogicalOr(self, ctx:languageParser.LogicalOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#greater_lesser.
    def visitGreater_lesser(self, ctx:languageParser.Greater_lesserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#equal_notequal.
    def visitEqual_notequal(self, ctx:languageParser.Equal_notequalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by languageParser#type_keyword.
    def visitType_keyword(self, ctx:languageParser.Type_keywordContext):
        return self.visitChildren(ctx)



del languageParser