import sys

from antlr4 import *
from antlr4.tree.Trees import Trees

from languageLexer import languageLexer
from languageParser import languageParser
from visitorImpl import visitorImpl

#skupina B
#do while
# do statement
# while (expression);

if __name__ == '__main__':
    argv = sys.argv
    input_stream = FileStream('test1.txt')
    lexer = languageLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = languageParser(stream)

    tree = parser.prog()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        visitor = visitorImpl()
        visitor.visit(tree)



    pass