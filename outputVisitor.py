from antlr4.tree.Tree import TerminalNodeImpl

from languageParser import languageParser, ParserRuleContext
from languageVisitor import languageVisitor
from symbol_table import SymbolTable
from type_enum import Type


class OutputVisitor(languageVisitor):
    def __init__(self, symbol_table: SymbolTable, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.symbol_table = symbol_table
        self.output_list = []
        self.type_single_letter_dir: dict[Type, str] = {
            Type.Int: "I",
            Type.Float: "F",
            Type.Bool: "B",
            Type.String: "S",
        }
        self.jump_idx = -1

    def new_jump_idx(self):
        self.jump_idx += 1
        return self.jump_idx

    def resolve_itof_binary_op(self, left: ParserRuleContext, right: ParserRuleContext):
        if isinstance(left, languageParser.IntLiteralContext) and isinstance(
                right, languageParser.FloatLiteralContext
        ):
            self.output_list.append("itof")
            return True

    def resolve_left_right_itof(self, ctx):
        resolved = []
        left = ctx.expression()[0]
        right = ctx.expression()[1]

        l = self.visit(left)
        # resolved.append(self.resolve_itof_binary_op(left, right))

        r = self.visit(right)
        # resolved.append(self.resolve_itof_binary_op(right, left))
        # print("lr", l, r)
        if l[0] == "I" and (r[0] == "F" or r == "F"):
            if self.output_list[-1].startswith("push"):
                self.output_list.insert(-1, "itof")
            else:
                self.output_list.append("itof")
            return "F"
            pass
        elif l[0] == "F" and (r[0] == "I" or r == "I"):
            # self.output_list.insert(-1, "itof")
            self.output_list.append("itof")
            return "F"
            pass
        return l[0]

        pass

    def visitIntLiteral(self, ctx: languageParser.IntLiteralContext):
        self.output_list.append(f"push I {ctx.INT_LITERAL().getText()}")
        return "I", ctx.INT_LITERAL().getText()

    def visitFloatLiteral(self, ctx: languageParser.FloatLiteralContext):
        self.output_list.append(f"push F {ctx.FLOAT_LITERAL().getText()}")
        return "F", ctx.FLOAT_LITERAL().getText()

    def visitBoolLiteral(self, ctx: languageParser.BoolLiteralContext):
        self.output_list.append(f"push B {ctx.BOOL_LITERAL().getText()}")
        return "B", ctx.BOOL_LITERAL().getText()

    def visitStringLiteral(self, ctx: languageParser.StringLiteralContext):
        self.output_list.append(f"push S {ctx.STRING_LITERAL().getText()}")
        return "S", ctx.STRING_LITERAL().getText()

    def visitParentheses(self, ctx: languageParser.ParenthesesContext):
        v = self.visit(ctx.expression())
        return v

    def visitWrite_statement(self, ctx: languageParser.Write_statementContext):
        for expression in ctx.expression():
            self.visit(expression)

        self.output_list.append(f"print {len(ctx.expression())}")

    def visitRead_statement(self, ctx: languageParser.Read_statementContext):
        for identifier in ctx.IDENTIFIER():
            identifier: TerminalNodeImpl
            type_single_letter = self.type_single_letter_dir[
                self.symbol_table[identifier.symbol]
            ]
            self.output_list.append(f"read {type_single_letter}")
            self.output_list.append(f"save {identifier.getText()}")

    def visitUnaryMinus(self, ctx: languageParser.UnaryMinusContext):
        self.visit(ctx.expression())
        self.output_list.append(f"uminus")

    def visitProgram(self, ctx: languageParser.ProgramContext):
        for statement in ctx.statement():
            statement: ParserRuleContext
            self.visit(statement)

        return self.output_list

    def visitType_keyword(self, ctx: languageParser.Type_keywordContext):
        match ctx.getText():
            case "int":
                self.output_list.append("push I 0")
            case "float":
                self.output_list.append("push F 0.0")
            case "string":
                self.output_list.append('push S ""')
            case "bool":
                self.output_list.append("push B true")

    def visitId(self, ctx: languageParser.IdContext):
        self.output_list.append(f"load {ctx.IDENTIFIER().getText()}")

    def visitMulDivMod(self, ctx: languageParser.MulDivModContext):
        ret = self.resolve_left_right_itof(ctx)

        match ctx.op.type:
            case languageParser.MUL:
                self.output_list.append("mul")
            case languageParser.DIV:
                self.output_list.append("div")
            case languageParser.MOD:
                self.output_list.append("mod")

        return ret

    def visitAddSubConcat(self, ctx: languageParser.MulDivModContext):
        ret = self.resolve_left_right_itof(ctx)

        match ctx.op.type:
            case languageParser.ADD:
                self.output_list.append("add")
            case languageParser.SUB:
                self.output_list.append("sub")
            case languageParser.CONCAT:
                self.output_list.append("concat")

        return ret

    def visitLesserGreater(self, ctx: languageParser.MulDivModContext):
        ret = self.resolve_left_right_itof(ctx)

        match ctx.op.type:
            case languageParser.LT:
                self.output_list.append("lt " + ret[0])
            case languageParser.GT:
                self.output_list.append("gt " + ret[0])

    def visitEqualNotEqual(self, ctx: languageParser.MulDivModContext):
        left = ctx.expression()[0]
        right = ctx.expression()[1]
        l = self.visit(left)
        r = self.visit(right)

        match ctx.op.type:
            case languageParser.EQUAL:
                self.output_list.append("eq " + l[0])
            case languageParser.NOTEQUAL:
                self.output_list.append("eq " + l[0])
                self.output_list.append("not " + l[0])

    def visitLogicalAnd(self, ctx: languageParser.MulDivModContext):
        left = ctx.expression()[0]
        right = ctx.expression()[1]
        self.visit(left)
        self.visit(right)

        self.output_list.append("and")

    def visitLogicalOr(self, ctx: languageParser.MulDivModContext):
        left = ctx.expression()[0]
        right = ctx.expression()[1]
        self.visit(left)
        self.visit(right)

        self.output_list.append("or")

    def visitLogicalNot(self, ctx: languageParser.MulDivModContext):
        self.visit(ctx.expression())

        self.output_list.append("not")

    def visitDeclaration(self, ctx: languageParser.DeclarationContext):
        for identifier in ctx.IDENTIFIER():
            identifier: TerminalNodeImpl
            self.visit(ctx.type_keyword())
            self.output_list.append(f"save {identifier.getText()}")

    def visitConditional(self, ctx: languageParser.ConditionalContext):
        self.visit(ctx.condition)
        fjmp = self.new_jump_idx()
        jmp = self.new_jump_idx()

        self.output_list.append(f"fjmp {fjmp}")
        self.visit(ctx.if_body)

        self.output_list.append(f"jmp {jmp}")
        self.output_list.append(f"label {fjmp}")
        if ctx.else_body:
            self.visit(ctx.else_body)
        self.output_list.append(f"label {jmp}")

    def visitWhile_loop(self, ctx: languageParser.While_loopContext):
        jmp = self.new_jump_idx()
        fjmp = self.new_jump_idx()

        self.output_list.append(f"label {jmp}")
        self.visit(ctx.condition)
        self.output_list.append(f"fjmp {fjmp}")
        self.visit(ctx.statement())
        self.output_list.append(f"jmp {jmp}")
        self.output_list.append(f"label {fjmp}")

    def visitAssignment(self, ctx: languageParser.AssignmentContext):
        self.visit(ctx.expression())

        # itof
        if self.symbol_table[ctx.IDENTIFIER().symbol] == Type.Float and isinstance(
                ctx.expression(), languageParser.IntLiteralContext
        ):
            self.output_list.append("itof")

        self.output_list.append(f"save {ctx.IDENTIFIER().getText()}")
        self.output_list.append(f"load {ctx.IDENTIFIER().getText()}")

        if not isinstance(ctx.parentCtx, languageParser.AssignmentContext):
            self.output_list.append(f"pop")

        return ctx.expression()

    def visitStatement(self, ctx: languageParser.StatementContext):
        # expr: languageParser.ExpressionContext = ctx.expression()

        if ctx.expression() is not None:
            ret = self.visit(ctx.expression())

            if ret is not None and type(ret) in (list, tuple):
                self.output_list.append(f"push {ret[0]} {ret[1]}")
                self.output_list.append(f"push {ret[0]} {ret[2]}")
                self.output_list.append(f"{ret[-1]} {ret[0]}")
            else:
                # return super().visitStatement(ctx)
                pass
        else:
            return super().visitStatement(ctx)
