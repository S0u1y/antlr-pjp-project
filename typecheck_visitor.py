from antlr4.tree.Tree import TerminalNodeImpl

from errors import Errors
from languageParser import languageParser
from languageVisitor import languageVisitor
from symbol_table import SymbolTable
from type_enum import Type


class TypeCheckingVisitor(languageVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.binary_operations_table: dict[tuple[Type, Type, int], Type] = {
            (Type.Int, Type.Int, languageParser.MUL): Type.Int,
            (Type.Float, Type.Float, languageParser.MUL): Type.Float,
            (Type.Int, Type.Int, languageParser.DIV): Type.Int,
            (Type.Float, Type.Float, languageParser.DIV): Type.Float,
            (Type.Int, Type.Int, languageParser.MOD): Type.Int,
            (Type.Int, Type.Int, languageParser.ADD): Type.Int,
            (Type.Float, Type.Float, languageParser.ADD): Type.Float,
            (Type.Int, Type.Int, languageParser.SUB): Type.Int,
            (Type.Float, Type.Float, languageParser.SUB): Type.Float,
            (Type.String, Type.String, languageParser.CONCAT): Type.String,
        }

    def visitType_keyword(self, ctx: languageParser.Type_keywordContext):
        match ctx.getText():
            case "float":
                return Type.Float
            case "int":
                return Type.Int
            case "string":
                return Type.String
            case "bool":
                return Type.Bool

    @staticmethod
    def resolve_left_right_types(type_a: Type, type_b: Type) -> tuple[Type, Type]:
        if TypeCheckingVisitor.check_float_cast(type_a, type_b):
            return Type.Float, Type.Float

        return type_a, type_b

    @staticmethod
    def check_float_cast(type_a: Type, type_b: Type) -> bool:
        if (type_a == Type.Int) or (type_b == Type.Int):
            if (type_a == Type.Float) or (type_b == Type.Float):
                return True

        return False

    def visitConditional(self, ctx: languageParser.ConditionalContext):
        condition = self.visit(ctx.condition)
        if condition != Type.Bool:
            Errors.report_error_rule_context(
                ctx.condition,
                f"Invalid condition. Should an expression with a type bool!",
            )

        self.visitChildren(ctx)

        return Type.Error

    def visitWhile_loop(self, ctx: languageParser.While_loopContext):
        condition = self.visit(ctx.condition)
        if condition != Type.Bool:
            Errors.report_error_rule_context(
                ctx.condition,
                f"Invalid condition. Should an expression with a type bool!",
            )

        self.visitChildren(ctx)

        return Type.Error

    def visitFor_loop(self, ctx:languageParser.For_loopContext):
        self.visit(ctx.expression()[0])
        condition = self.visit(ctx.expression()[1])
        self.visit(ctx.expression()[2])

        if condition != Type.Bool:
            Errors.report_error_rule_context(
                ctx.expression()[1],
                f"Invalid condition. Should an expression with a type bool!",
            )


    def visitIntLiteral(self, ctx: languageParser.IntLiteralContext):
        return Type.Int

    def visitFloatLiteral(self, ctx: languageParser.FloatLiteralContext):
        return Type.Float

    def visitBoolLiteral(self, ctx: languageParser.BoolLiteralContext):
        return Type.Bool

    def visitStringLiteral(self, ctx: languageParser.StringLiteralContext):
        return Type.String

    def visitLogicalNot(self, ctx: languageParser.LogicalNotContext):
        variable = self.visit(ctx.expression())
        if variable == Type.Bool:
            return Type.Bool

        Errors.report_error(
            ctx.prefix,
            f"Invalid type for logical negation!",
        )

        return Type.Error

    def visitUnaryMinus(self, ctx: languageParser.UnaryMinusContext):
        variable = self.visit(ctx.expression())
        if variable in (Type.Int, Type.Float):
            return variable

        Errors.report_error(
            ctx.prefix,
            f"Invalid type for unary minus!",
        )

        return Type.Error

    def visitMulDivMod(self, ctx: languageParser.MulDivModContext):
        left = self.visit(ctx.expression()[0])
        right = self.visit(ctx.expression()[1])

        type_left, type_right = self.resolve_left_right_types(left, right)
        if type_ := self.binary_operations_table.get(
                (type_left, type_right, ctx.op.type)
        ):
            return type_

        Errors.report_error(ctx.op, f"Invalid operation. \"{left.name} {ctx.op.text} {right.name}\"")

        return Type.Error

    def visitAddSubConcat(self, ctx: languageParser.AddSubConcatContext):
        left = self.visit(ctx.expression()[0])
        right = self.visit(ctx.expression()[1])
        print(ctx.expression())

        if (left == Type.Error) or (right == Type.Error):
            return Type.Error

        type_left, type_right = self.resolve_left_right_types(left, right)
        if type_ := self.binary_operations_table.get(
                (type_left, type_right, ctx.op.type)
        ):
            return type_

        Errors.report_error(ctx.op, f"Invalid operation. \"{left.name} {ctx.op.text} {right.name}\"")

        return Type.Error

    def visitLesserGreater(self, ctx: languageParser.LesserGreaterContext):
        left = self.visit(ctx.expression()[0])
        right = self.visit(ctx.expression()[1])
        if (left == Type.Error) or (right == Type.Error):
            return Type.Error

        if (left in (Type.Int, Type.Float)) and (right in (Type.Int, Type.Float)):
            return Type.Bool

        Errors.report_error(
            ctx.op,
            f"Invalid type for comparison!",
        )

        return Type.Error

    def visitEqualNotEqual(self, ctx: languageParser.EqualNotEqualContext):
        left = self.visit(ctx.expression()[0])
        right = self.visit(ctx.expression()[1])

        left_type, right_type = self.resolve_left_right_types(left, right)
        if left_type == right_type:
            return Type.Bool

        Errors.report_error(
            ctx.op,
            f"Invalid type for equality testing!",
        )

        return Type.Error

    def visitLogicalAnd(self, ctx: languageParser.LogicalAndContext):
        left = self.visit(ctx.expression()[0])
        right = self.visit(ctx.expression()[1])
        if (left == Type.Error) or (right == Type.Error):
            return Type.Error

        if (left == Type.Bool) and (right == Type.Bool):
            return Type.Bool

        Errors.report_error(
            ctx.op,
            f"Invalid type for logical AND!",
        )

        return Type.Error

    def visitLogicalOr(self, ctx: languageParser.LogicalAndContext):
        left = self.visit(ctx.expression()[0])
        right = self.visit(ctx.expression()[1])
        if (left == Type.Error) or (right == Type.Error):
            return Type.Error

        if (left == Type.Bool) and (right == Type.Bool):
            return Type.Bool

        Errors.report_error(
            ctx.op,
            f"Invalid type for logical OR!",
        )

        return Type.Error

    def visitDeclaration(self, ctx: languageParser.DeclarationContext):
        type_ = self.visit(ctx.type_keyword())
        for identifier in ctx.IDENTIFIER():
            identifier: TerminalNodeImpl
            self.symbol_table.add(identifier.symbol, type_)
        return Type.Error

    def visitParentheses(self, ctx: languageParser.ParenthesesContext):
        return self.visit(ctx.expression())

    def visitId(self, ctx: languageParser.IdContext):
        return self.symbol_table[ctx.IDENTIFIER().symbol]

    def visitAssignment(self, ctx: languageParser.AssignmentContext):
        variable = self.symbol_table[ctx.IDENTIFIER().symbol]
        right = self.visit(ctx.expression())

        if (variable == Type.Error) or (right == Type.Error):
            return Type.Error

        if (variable == Type.Int) and (right == Type.Float):
            Errors.report_error(
                ctx.IDENTIFIER().symbol,
                f"Variable '{ctx.IDENTIFIER().getText()}' type is int, but the assigned value is float.",
            )
            return Type.Error

        if (variable == Type.Float) and (right == Type.Int):
            value = Type.Float
            self.symbol_table[ctx.IDENTIFIER().symbol] = value
            return value
        else:
            if right != self.symbol_table[ctx.IDENTIFIER().symbol]:
                Errors.report_error(
                    ctx.IDENTIFIER().symbol,
                    f"Variable '{ctx.IDENTIFIER().getText()}' type is {variable.name.lower()},"
                    f" but the assigned is {right.name.lower()}",
                )

            return right
