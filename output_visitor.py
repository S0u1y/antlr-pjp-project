from antlr4.tree.Tree import TerminalNodeImpl

from languageParser import languageParser, ParserRuleContext
from languageVisitor import languageVisitor

from symbol_table import SymbolTable


class OutputVisitor(languageVisitor):
    def __init__(self, symbol_table, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.symbol_table = symbol_table
        self.output_list = []
        self.type_single_letter_dir = {
            int: "I",
            float: "F",
            bool: "B",
            str: "S"
        }
        self.jump_idx = -1

    def add_jump_idx(self):
        self.jump_idx += 1
        return self.jump_idx

    def resolve_itof_binary_op(self, left, right):
        if isinstance(left, languageParser.IntContext) and isinstance(right, languageParser.FloatContext):
            self.output_list.append("itof")

    def visitAssignment(self, ctx: languageParser.AssignmentContext):
        self.visit(ctx.expression())
        # itof
        if self.symbol_table[ctx.IDENTIFIER().symbol] == float and isinstance(ctx.expression(),
                                                                              languageParser.IntContext):
            self.output_list.append("itof")
        self.output_list.append(f"save {ctx.IDENTIFIER().getText()}")
        self.output_list.append(f"load {ctx.IDENTIFIER().getText()}")

        if not isinstance(ctx.parentCtx, languageParser.AssignmentContext):
            self.output_list.append("pop")

        return ctx.expression()

    def visitWhile_loop(self, ctx: languageParser.While_loopContext):
        jmp = self.add_jump_idx()
        fjmp = self.add_jump_idx()

        self.output_list.append(f"label {jmp}")
        self.visit(ctx.expression())
        self.output_list.append(f"fjmp {fjmp}")
        self.visit(ctx.statement())
        self.output_list.append(f"jmp {jmp}")
        self.output_list.append(f"label {fjmp}")

    def visitDeclaration(self, ctx: languageParser.DeclarationContext):
        for identifier in ctx.IDENTIFIER():
            identifier: TerminalNodeImpl
            self.visit(ctx.type_())
            self.output_list.append(f"save {identifier.getText()}")

    def visitType(self, ctx: languageParser.TypeContext):
        match ctx.getText():
            case "int":
                self.output_list.append("push I 0")
            case "float":
                self.output_list.append("push F 0.0")
            case "string":
                self.output_list.append('push S ""')
            case "bool":
                self.output_list.append("push B true")

    def visitInt(self, ctx: languageParser.IntContext):
        self.output_list.append(f"push I {ctx.INT().getText()}")

    def visitFloat(self, ctx: languageParser.FloatContext):
        self.output_list.append(f"push F {ctx.FLOAT().getText()}")

    def visitBool(self, ctx: languageParser.BoolContext):
        self.output_list.append(f"push B {ctx.BOOL().getText()}")

    def visitString(self, ctx: languageParser.StringContext):
        self.output_list.append(f"push S {ctx.STRING().getText()}")

    def visitParantheses(self, ctx: languageParser.ParanthesesContext):
        return self.visit(ctx.expression())

    def visitRead(self, ctx: languageParser.ReadContext):
        for identifier in ctx.IDENTIFIER():
            identifier: TerminalNodeImpl
            type_single_letter = self.type_single_letter_dir[
                self.symbol_table[identifier.symbol]
            ]
            self.output_list.append(f"read {type_single_letter}")
            self.output_list.append(f"save {identifier.getText()}")

    def visitWrite(self, ctx: languageParser.WriteContext):
        for expression in ctx.expression():
            self.visit(expression)

        self.output_list.append(f"print {len(ctx.expression())}")

    def visitExpression(self, ctx: languageParser.ExpressionContext):
        left = ctx.left
        right = ctx.right
        self.visit(left)
        self.visit(right)
        operator = ctx.op.text
        _resolve_expression(left, operator, right)



def _resolve_expression(left, operator, right):
    match operator:
        case '/':
            #             TODO
            return None
        case '*':
            #             TODO
            return None
        case '+':
            #             TODO
            return None
        case '-':
            #             TODO
            return None
        case "==":
            return bool, left == right
        case "&&":
            #             TODO
            return None
        case "||":
            #             TODO
            return None
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
            
            return bool, left < right
        case ">":
            if type(left) not in (int, float) or type(right) not in (int, float):
                print(f"Relation operator signature error. ")
                return "error", 0
            return bool, left > right
