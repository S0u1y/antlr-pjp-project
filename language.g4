grammar language;

options {
    language = Python3;
}

prog: expression+ EOF ;

expression:  assignment ';';

assignment: IDENTIFIER '=' NUMBER
            | IDENTIFIER '=' IDENTIFIER;

IDENTIFIER: [a-z]+;

NUMBER: [0-9]+;

WS: [\t\n\r]+ -> skip;
