grammar language;

options {
    language = Python3;
}

fragment CHARACTER: [a-zA-Z] ;
INT: [1-9][0-9]* | '0';
FLOAT: [0-9]+'.'[0-9]+ | '.'[1-9]+ ;
BOOL: 'true' | 'false' ;
ONE_LINE_COMMENT: '//' ~[\r\n]* -> skip ;
STRING: '"' ~["\\\r\n]* '"' ;
IDENTIFIER: [a-zA-Z] ([a-zA-Z] | [0-9])* ;
WS: [\t\n\r]+ -> skip ;

MUL: '*' ;
DIV: '/' ;
ADD: '+' ;
SUB: '-' ;
MOD: '%' ;
CONCAT: '.' ;

prog: statement+ EOF ;

statement:  ';'
            | declaration
            | expression ';'
            | read
            | write
            | block
            | condition
            | while_loop
            | ONE_LINE_COMMENT ;

expression: prefix='-' expression
          | prefix='+' expression
          | left=expression op=(MUL | DIV | MOD) right=expression
          | left=expression op=(ADD | SUB | CONCAT) right=expression
          | left=expression op=('<' | '>') right=expression
          | left=expression op=('==' | '!=') right=expression
          | left=expression op='&&' right=expression
          | left=expression op='||' right=expression
          | parantheses
          | assignment
          | IDENTIFIER
          | literal ;

parantheses: '(' expression ')' ;

declaration: type ' '+ IDENTIFIER (',' ' '* IDENTIFIER)* ';' ;

read: 'read' ' '+ IDENTIFIER (',' IDENTIFIER)* ';' ;
write: 'write' ' '+ expression (',' expression)* ';' ;

block: '{' statement* '}' ;

condition: 'if' '(' expression ')' statement ('else' statement)? ;
while_loop: 'while' '(' expression ')' statement ;

assignment: <assoc=right> IDENTIFIER ' '* '=' ' '* expression ;

type: 'int' | 'float' | 'bool' | 'string' ;

literal: INT # int
       | FLOAT # float
       | BOOL # bool
       | STRING # string ;