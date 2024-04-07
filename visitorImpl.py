from languageParser import languageParser
from languageVisitor import languageVisitor
from antlr4.tree.Tree import TerminalNodeImpl


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
    def visitStatement(self, ctx: languageParser.StatementContext):
        return super().visitStatement(ctx)

    def visitExpression(self, ctx: languageParser.ExpressionContext):
        if None not in (ctx.left, ctx.right):
            left = self.visit(ctx.left)
            right = self.visit(ctx.right)
            operator = ctx.op.text
            print(_resolve_expression(left, operator, right))

        return super().visitExpression(ctx)

    def visitDeclaration(self, ctx: languageParser.DeclarationContext):
        _type = self.visit(ctx.type_())
        for identifier in ctx.IDENTIFIER():
            identifier: TerminalNodeImpl
            #TODO add symbol table

        return super().visitDeclaration(ctx)

    def visitParantheses(self, ctx: languageParser.ParanthesesContext):
        return self.visit(ctx.expression())

    def visitCondition(self, ctx: languageParser.ConditionContext):
        return super().visitCondition(ctx)

    def visitWhile_loop(self, ctx: languageParser.While_loopContext):
        return super().visitWhile_loop(ctx)

    def visitAssignment(self, ctx: languageParser.AssignmentContext):

        return ctx.getText()

    def visitType(self, ctx: languageParser.TypeContext):
        return super().visitType(ctx)

    def visitInt(self, ctx: languageParser.IntContext):
        return int(ctx.INT().getText())

    def visitFloat(self, ctx: languageParser.FloatContext):
        return float(ctx.FLOAT().getText())

    def visitBool(self, ctx: languageParser.BoolContext):
        return bool(ctx.BOOL().getText())

    def visitString(self, ctx: languageParser.StringContext):
        return ctx.STRING().getText()
