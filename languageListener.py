# Generated from ./language.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .languageParser import languageParser
else:
    from languageParser import languageParser

# This class defines a complete listener for a parse tree produced by languageParser.
class languageListener(ParseTreeListener):

    # Enter a parse tree produced by languageParser#program.
    def enterProgram(self, ctx:languageParser.ProgramContext):
        pass

    # Exit a parse tree produced by languageParser#program.
    def exitProgram(self, ctx:languageParser.ProgramContext):
        pass


    # Enter a parse tree produced by languageParser#statement.
    def enterStatement(self, ctx:languageParser.StatementContext):
        pass

    # Exit a parse tree produced by languageParser#statement.
    def exitStatement(self, ctx:languageParser.StatementContext):
        pass


    # Enter a parse tree produced by languageParser#declaration.
    def enterDeclaration(self, ctx:languageParser.DeclarationContext):
        pass

    # Exit a parse tree produced by languageParser#declaration.
    def exitDeclaration(self, ctx:languageParser.DeclarationContext):
        pass


    # Enter a parse tree produced by languageParser#read_statement.
    def enterRead_statement(self, ctx:languageParser.Read_statementContext):
        pass

    # Exit a parse tree produced by languageParser#read_statement.
    def exitRead_statement(self, ctx:languageParser.Read_statementContext):
        pass


    # Enter a parse tree produced by languageParser#write_statement.
    def enterWrite_statement(self, ctx:languageParser.Write_statementContext):
        pass

    # Exit a parse tree produced by languageParser#write_statement.
    def exitWrite_statement(self, ctx:languageParser.Write_statementContext):
        pass


    # Enter a parse tree produced by languageParser#block.
    def enterBlock(self, ctx:languageParser.BlockContext):
        pass

    # Exit a parse tree produced by languageParser#block.
    def exitBlock(self, ctx:languageParser.BlockContext):
        pass


    # Enter a parse tree produced by languageParser#conditional.
    def enterConditional(self, ctx:languageParser.ConditionalContext):
        pass

    # Exit a parse tree produced by languageParser#conditional.
    def exitConditional(self, ctx:languageParser.ConditionalContext):
        pass


    # Enter a parse tree produced by languageParser#while_loop.
    def enterWhile_loop(self, ctx:languageParser.While_loopContext):
        pass

    # Exit a parse tree produced by languageParser#while_loop.
    def exitWhile_loop(self, ctx:languageParser.While_loopContext):
        pass


    # Enter a parse tree produced by languageParser#for_loop.
    def enterFor_loop(self, ctx:languageParser.For_loopContext):
        pass

    # Exit a parse tree produced by languageParser#for_loop.
    def exitFor_loop(self, ctx:languageParser.For_loopContext):
        pass


    # Enter a parse tree produced by languageParser#mulDivMod.
    def enterMulDivMod(self, ctx:languageParser.MulDivModContext):
        pass

    # Exit a parse tree produced by languageParser#mulDivMod.
    def exitMulDivMod(self, ctx:languageParser.MulDivModContext):
        pass


    # Enter a parse tree produced by languageParser#parentheses.
    def enterParentheses(self, ctx:languageParser.ParenthesesContext):
        pass

    # Exit a parse tree produced by languageParser#parentheses.
    def exitParentheses(self, ctx:languageParser.ParenthesesContext):
        pass


    # Enter a parse tree produced by languageParser#logicalNot.
    def enterLogicalNot(self, ctx:languageParser.LogicalNotContext):
        pass

    # Exit a parse tree produced by languageParser#logicalNot.
    def exitLogicalNot(self, ctx:languageParser.LogicalNotContext):
        pass


    # Enter a parse tree produced by languageParser#equalNotEqual.
    def enterEqualNotEqual(self, ctx:languageParser.EqualNotEqualContext):
        pass

    # Exit a parse tree produced by languageParser#equalNotEqual.
    def exitEqualNotEqual(self, ctx:languageParser.EqualNotEqualContext):
        pass


    # Enter a parse tree produced by languageParser#addSubConcat.
    def enterAddSubConcat(self, ctx:languageParser.AddSubConcatContext):
        pass

    # Exit a parse tree produced by languageParser#addSubConcat.
    def exitAddSubConcat(self, ctx:languageParser.AddSubConcatContext):
        pass


    # Enter a parse tree produced by languageParser#assignment.
    def enterAssignment(self, ctx:languageParser.AssignmentContext):
        pass

    # Exit a parse tree produced by languageParser#assignment.
    def exitAssignment(self, ctx:languageParser.AssignmentContext):
        pass


    # Enter a parse tree produced by languageParser#intLiteral.
    def enterIntLiteral(self, ctx:languageParser.IntLiteralContext):
        pass

    # Exit a parse tree produced by languageParser#intLiteral.
    def exitIntLiteral(self, ctx:languageParser.IntLiteralContext):
        pass


    # Enter a parse tree produced by languageParser#lesserGreater.
    def enterLesserGreater(self, ctx:languageParser.LesserGreaterContext):
        pass

    # Exit a parse tree produced by languageParser#lesserGreater.
    def exitLesserGreater(self, ctx:languageParser.LesserGreaterContext):
        pass


    # Enter a parse tree produced by languageParser#logicalAnd.
    def enterLogicalAnd(self, ctx:languageParser.LogicalAndContext):
        pass

    # Exit a parse tree produced by languageParser#logicalAnd.
    def exitLogicalAnd(self, ctx:languageParser.LogicalAndContext):
        pass


    # Enter a parse tree produced by languageParser#boolLiteral.
    def enterBoolLiteral(self, ctx:languageParser.BoolLiteralContext):
        pass

    # Exit a parse tree produced by languageParser#boolLiteral.
    def exitBoolLiteral(self, ctx:languageParser.BoolLiteralContext):
        pass


    # Enter a parse tree produced by languageParser#stringLiteral.
    def enterStringLiteral(self, ctx:languageParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by languageParser#stringLiteral.
    def exitStringLiteral(self, ctx:languageParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by languageParser#unaryMinus.
    def enterUnaryMinus(self, ctx:languageParser.UnaryMinusContext):
        pass

    # Exit a parse tree produced by languageParser#unaryMinus.
    def exitUnaryMinus(self, ctx:languageParser.UnaryMinusContext):
        pass


    # Enter a parse tree produced by languageParser#floatLiteral.
    def enterFloatLiteral(self, ctx:languageParser.FloatLiteralContext):
        pass

    # Exit a parse tree produced by languageParser#floatLiteral.
    def exitFloatLiteral(self, ctx:languageParser.FloatLiteralContext):
        pass


    # Enter a parse tree produced by languageParser#id.
    def enterId(self, ctx:languageParser.IdContext):
        pass

    # Exit a parse tree produced by languageParser#id.
    def exitId(self, ctx:languageParser.IdContext):
        pass


    # Enter a parse tree produced by languageParser#logicalOr.
    def enterLogicalOr(self, ctx:languageParser.LogicalOrContext):
        pass

    # Exit a parse tree produced by languageParser#logicalOr.
    def exitLogicalOr(self, ctx:languageParser.LogicalOrContext):
        pass


    # Enter a parse tree produced by languageParser#type_keyword.
    def enterType_keyword(self, ctx:languageParser.Type_keywordContext):
        pass

    # Exit a parse tree produced by languageParser#type_keyword.
    def exitType_keyword(self, ctx:languageParser.Type_keywordContext):
        pass



del languageParser