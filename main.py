import sys
from pprint import pprint

from antlr4 import *
from antlr4.tree.Trees import Trees

from errors import Errors
from languageLexer import languageLexer
from languageParser import languageParser
from outputVisitor import OutputVisitor
from typecheck_visitor import TypeCheckingVisitor


def main(argv):
    input_stream = FileStream("test1.txt")
    lexer = languageLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = languageParser(stream)

    # Error listeners
    # parser.removeErrorListeners()  # Remove default error listeners
    # parser.addErrorListener(VerboseErrorListener())
    # parser.addErrorListener(StopParsingListener())

    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        print("Grammar is Ok")

        typecheck_visitor = TypeCheckingVisitor()
        typecheck_visitor.visit(tree)

        # pprint(visitor.symbol_table.memory)

        if Errors.number_of_errors():
            Errors.print_and_clear_errors()
            return
        else:
            print("Type Checking is Ok")
            print("OutputVisitor:")
            output_visitor = OutputVisitor(typecheck_visitor.symbol_table)
            output = output_visitor.visit(tree)
            output_str = "\n".join(output)
            print(output_str)

            with open("output.txt", "w") as file:
                file.write(output_str)


if __name__ == "__main__":
    main(sys.argv)