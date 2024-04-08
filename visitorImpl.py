from languageParser import languageParser
from languageVisitor import languageVisitor
from antlr4.tree.Tree import TerminalNodeImpl

from antlr4.Token import Token
from typing import Any


def _resolve_expression(left, operator, right):
    match operator:
        case '/':
            return left / right
        case '*':
            return left * right
        case '+':
            return left + right
        case '-':
            return left - right


class visitorImpl(languageVisitor):
    def __init__(self):
        self.symbol_table: dict[str, tuple[str, Any]] = {}

    def add_symbol(self, variable: Token, type_: str):
        name = variable.text.strip()
        if name in self.symbol_table:
            print(f"Variable {name} was already declared.")
            return
        self.symbol_table[name] = (type_, 0 if type_ == "int" else 0.0)
        pass

    def get_symbol(self, variable: Token | str):
        name = variable
        if type(variable) != str:
            name = variable.text.strip()
        if name in self.symbol_table:
            return self.symbol_table[name]
        print(f"Variable {name} was not declared.")
        return "error", 0
        pass

    def visitStatement(self, ctx: languageParser.StatementContext):
        return super().visitStatement(ctx)

    def visitExpression(self, ctx: languageParser.ExpressionContext):
        if None not in (ctx.left, ctx.right):
            left = self.visit(ctx.left)
            right = self.visit(ctx.right)
            operator = ctx.op.text
            return _resolve_expression(left, operator, right)

        if ctx.IDENTIFIER() is not None:
            var = self.get_symbol(str(ctx.IDENTIFIER()))
            return var

        return super().visitExpression(ctx)

    def visitDeclaration(self, ctx: languageParser.DeclarationContext):
        _type = self.visit(ctx.type_())
        for identifier in ctx.IDENTIFIER():
            identifier: TerminalNodeImpl
            self.add_symbol(identifier.symbol, _type)

        return "error", 0

    def visitParantheses(self, ctx: languageParser.ParanthesesContext):
        return self.visit(ctx.expression())

    def visitCondition(self, ctx: languageParser.ConditionContext):
        return super().visitCondition(ctx)

    def visitWhile_loop(self, ctx: languageParser.While_loopContext):
        return super().visitWhile_loop(ctx)

    def visitAssignment(self, ctx: languageParser.AssignmentContext):
        # maybe replace ctx.IDENTIFIER().symbol with str(ctx.IDENTIFIER())
        variable = self.get_symbol(ctx.IDENTIFIER().symbol)
        right = self.visit(ctx.expression())
        right_type = type(right)
        print(variable, right, right_type, ctx.IDENTIFIER().symbol)
        if (variable[0] == "error") or right[0] == "error":
            return "error", 0
        if (variable[0] == "int" or variable[0] == int) and (right[0] in (float, "float")):
            print(f"Variable '{ctx.IDENTIFIER().getText()}' type is int, but the assigned value is float.")
            return "error", 0
        if (variable[0] == "float") and ((right_type == str and right == "int") or (
                right_type == tuple and (right[0] == "int" or type(right[0]) is int)) or right_type == int):

            value = "float", float(right)
            name: str = ctx.IDENTIFIER().symbol.text.strip()
            self.symbol_table[name] = value
            return value
        self.symbol_table[ctx.IDENTIFIER().symbol.text.strip()] = right
        return right

    def visitType(self, ctx: languageParser.TypeContext):
        return ctx.getText()

    def visitInt(self, ctx: languageParser.IntContext):
        return int, int(ctx.INT().getText())

    def visitFloat(self, ctx: languageParser.FloatContext):
        return float, float(ctx.FLOAT().getText())

    def visitBool(self, ctx: languageParser.BoolContext):
        return bool, bool(ctx.BOOL().getText())

    def visitString(self, ctx: languageParser.StringContext):
        return str, ctx.STRING().getText()
