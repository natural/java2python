grammar Selector;


options {
    backtrack=true;
    memoize=true;
    language=Python;
    output=AST;
    ASTLabelType=CommonTree;
}

tokens {
COMMA   = ',' ;
DQUOTE  = '"' ;
EQ      = '=' ;
GT      = '>' ;
LSQUARE = '[' ;
PLUS    = '+' ;
RSQUARE = ']' ;
STAR    = '*' ;


NTH;
MATCH;
MATCH_CHILD;
MATCH_DESCEND;
MATCH_NTH;
MATCH_OP;
MATCH_SIBLING;
MATCH_STAR;
MATCH_TEXT;
MATCH_TYPE;
OP;
SELECTOR;
TEXT;
}


selector
    : expression+
      -> ^(SELECTOR expression+)
    ;


expression
    : primary
      -> ^(primary)
    | primary optail
      -> ^(MATCH_OP primary optail)
    | primary subtail
      -> ^(MATCH_NTH primary subtail)
    ;


primary
    : STAR -> ^(MATCH_STAR[$STAR])
    | TYPE -> ^(MATCH_TYPE[$TYPE])
    ;


optail
    : (GT expression*)
      -> ^(OP['>'] expression*)
    | (PLUS expression*)
      -> ^(OP['+'] expression*)
    ;


subtail
    : LSQUARE index RSQUARE expression*
      -> ^(NTH[$index.text] expression*)
    | LSQUARE text  RSQUARE expression*
      -> ^(TEXT[$text.text] expression*)
    ;


index    : INDEX;
text     : LITERAL;


// lexer


LLETTERS : ('a'..'z');
ULETTERS : ('A'..'Z');
HASH     : '#';
USCORE   : '_';


fragment TYPE_START  : ULETTERS+    ;
fragment TYPE_PART   : TYPE_START | USCORE ;
TYPE : TYPE_START (TYPE_PART)*  ;
LITERAL :  '"' ( ESCAPE_SEQUENCE | ~('\\'|'"') )* '"'   ;

fragment
ESCAPE_SEQUENCE
    :   '\\' ('b'|'t'|'n'|'f'|'r'|'\"'|'\''|'\\')
    |   UNICODE_ESCAPE
    |   OCTAL_ESCAPE
    ;

fragment
OCTAL_ESCAPE
    :   '\\' ('0'..'3') ('0'..'7') ('0'..'7')
    |   '\\' ('0'..'7') ('0'..'7')
    |   '\\' ('0'..'7')
    ;

fragment UNICODE_ESCAPE : '\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT ;
fragment HEX_DIGIT : ('0'..'9'|'a'..'f'|'A'..'F') ;
INDEX : ('0' | '1'..'9' '0'..'9'*);
WS    : (' '|'\r'|'\t'|'\u000C'|'\n') { $channel = HIDDEN };
