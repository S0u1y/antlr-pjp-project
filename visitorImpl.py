from languageParser import languageParser
from languageVisitor import languageVisitor
from antlr4.tree.Tree import TerminalNodeImpl

from antlr4.Token import Token
from typing import Any


def _resolve_binary_signature(left, right, callback):
    if type(left) is str and type(right) is str:
        print(f"Operation signature failure. operation does not subscribe strings")
        return "error", 0
    if type(left) is not type(right):
        if type(left) is float and type(right) is int:
            return float, callback()
        print(f"Operation signature failure. expected {type(left)} x {type(left)}, but got {type(left)} x {type(right)}")
        return "error", 0
    return type(left), callback()


def _resolve_expression(left, operator, right):
    match operator:
        case '/':
            return _resolve_binary_signature(left, right, lambda: left / right)
        case '*':
            return _resolve_binary_signature(left, right, lambda: left * right)
        case '+':
            return _resolve_binary_signature(left, right, lambda: left + right)
        case '-':
            return _resolve_binary_signature(left, right, lambda: left - right)
        case "==":
            return bool, left == right
        case "&&":
            return _resolve_binary_signature(left, right, lambda: left and right)
        case "||":
            return _resolve_binary_signature(left, right, lambda: left or right)
        case "%":
            if type(left) is not int or type(right) is not int:
                print("Modulo operation can only be int x int.")
                return "error", 0
            return int, left % right
        case ".":
            if type(left) is not str or type(right) is not str:
                print("Concat operation takes only strings.")
                return "error", 0
            return str, left + right
        case "<":
            if type(left) not in (int, float) or type(right) not in (int ,float):
                print(f"Relation operator signature error. ")
                return "error", 0
            return bool, left < right
        case ">":
            if type(left) not in (int, float) or type(right) not in (int, float):
                print(f"Relation operator signature error. ")
                return "error", 0
            return bool, left > right

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
            # print(_resolve_expression(left[1], operator, right[1]))
            return _resolve_expression(left[1], operator, right[1])

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
        rtrn = self.visit(ctx.expression())
        if rtrn:
            return self.visit(ctx.statement(0))
        return self.visit(ctx.statement(1))

    def visitWhile_loop(self, ctx: languageParser.While_loopContext):
        condition = self.visit(ctx.expression())
        if condition[0] != bool:
            print(f"While statement condition is not a bool.")
            return "error", 0
        return "error", 0

    def visitDo_while_loop(self, ctx: languageParser.Do_while_loopContext):
        condition = self.visit(ctx.expression())
        if condition[0] != bool:
            print(f"While statement condition is not a bool at{ctx.expression().start.line}:{ctx.expression().start.column} ")
            return "error", 0
        return "error", 0

    def visitAssignment(self, ctx: languageParser.AssignmentContext):
        # maybe replace ctx.IDENTIFIER().symbol with str(ctx.IDENTIFIER())
        variable = self.get_symbol(ctx.IDENTIFIER().symbol)
        right = self.visit(ctx.expression())
        right_type = type(right)
        # print(variable, right, right_type, ctx.IDENTIFIER().symbol)
        if (variable[0] == "error") or right[0] == "error":
            return "error", 0
        # if (variable[0] == "int" or variable[0] == int) and (right[0] in (float, "float")):
        #     print(f"Variable '{ctx.IDENTIFIER().getText()}' type is int, but the assigned value is float.")
        #     return "error", 0
        # if (variable[0] in (int, "int")) and right[0] in (bool, "bool"):
        #     print(f"Variable '{ctx.IDENTIFIER().getText()}' type is int, but assigned value is bool.")
        #     return "error", 0
        if variable[0] != right[0].__name__ and (variable[0] != "string" and right is not str):
            if (variable[0] in (float, "float")) and (right[0] in (int, "int")):
                value = "float", float(right[1])
                name: str = ctx.IDENTIFIER().symbol.text.strip()
                self.symbol_table[name] = value
                return value
            else:
                print(f"Variable '{ctx.IDENTIFIER().getText()}' type is {variable[0]}, but assigned value is {right[0].__name__}.")
                return "error", 0

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
