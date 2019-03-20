# $ANTLR 3.5.2 Java.g 2019-03-19 17:13:02

import sys
from antlr3 import *
from antlr3.compat import set, frozenset



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
ABSTRACT=4
AND=5
AND_ASSIGN=6
ANNOTATION_INIT_ARRAY_ELEMENT=7
ANNOTATION_INIT_BLOCK=8
ANNOTATION_INIT_DEFAULT_KEY=9
ANNOTATION_INIT_KEY_LIST=10
ANNOTATION_LIST=11
ANNOTATION_METHOD_DECL=12
ANNOTATION_SCOPE=13
ANNOTATION_TOP_LEVEL_SCOPE=14
ARGUMENT_LIST=15
ARRAY_DECLARATOR=16
ARRAY_DECLARATOR_LIST=17
ARRAY_ELEMENT_ACCESS=18
ARRAY_INITIALIZER=19
ASSERT=20
ASSIGN=21
AT=22
BIT_SHIFT_RIGHT=23
BIT_SHIFT_RIGHT_ASSIGN=24
BLOCK_SCOPE=25
BOOLEAN=26
BREAK=27
BYTE=28
CASE=29
CAST_EXPR=30
CATCH=31
CATCH_CLAUSE_LIST=32
CHAR=33
CHARACTER_LITERAL=34
CLASS=35
CLASS_CONSTRUCTOR_CALL=36
CLASS_INSTANCE_INITIALIZER=37
CLASS_STATIC_INITIALIZER=38
CLASS_TOP_LEVEL_SCOPE=39
COLON=40
COMMA=41
COMMENT=42
CONSTRUCTOR_DECL=43
CONTINUE=44
DEC=45
DECIMAL_LITERAL=46
DEFAULT=47
DIV=48
DIV_ASSIGN=49
DO=50
DOT=51
DOTSTAR=52
DOUBLE=53
ELLIPSIS=54
ELSE=55
ENUM=56
ENUM_TOP_LEVEL_SCOPE=57
EQUAL=58
ESCAPE_SEQUENCE=59
EXPONENT=60
EXPR=61
EXTENDS=62
EXTENDS_BOUND_LIST=63
EXTENDS_CLAUSE=64
FALSE=65
FINAL=66
FINALLY=67
FLOAT=68
FLOATING_POINT_LITERAL=69
FLOAT_TYPE_SUFFIX=70
FOR=71
FORMAL_PARAM_LIST=72
FORMAL_PARAM_STD_DECL=73
FORMAL_PARAM_VARARG_DECL=74
FOR_CONDITION=75
FOR_EACH=76
FOR_INIT=77
FOR_UPDATE=78
FUNCTION_METHOD_DECL=79
GENERIC_TYPE_ARG_LIST=80
GENERIC_TYPE_PARAM_LIST=81
GREATER_OR_EQUAL=82
GREATER_THAN=83
HEX_DIGIT=84
HEX_LITERAL=85
IDENT=86
IF=87
IMPLEMENTS=88
IMPLEMENTS_CLAUSE=89
IMPORT=90
INC=91
INSTANCEOF=92
INT=93
INTEGER_TYPE_SUFFIX=94
INTERFACE=95
INTERFACE_TOP_LEVEL_SCOPE=96
JAVADOC_COMMENT=97
JAVA_ID_PART=98
JAVA_ID_START=99
JAVA_SOURCE=100
LABELED_STATEMENT=101
LBRACK=102
LCURLY=103
LESS_OR_EQUAL=104
LESS_THAN=105
LINE_COMMENT=106
LOCAL_MODIFIER_LIST=107
LOGICAL_AND=108
LOGICAL_NOT=109
LOGICAL_OR=110
LONG=111
LPAREN=112
METHOD_CALL=113
MINUS=114
MINUS_ASSIGN=115
MOD=116
MODIFIER_LIST=117
MOD_ASSIGN=118
NATIVE=119
NEW=120
NOT=121
NOT_EQUAL=122
NULL=123
OCTAL_ESCAPE=124
OCTAL_LITERAL=125
OR=126
OR_ASSIGN=127
PACKAGE=128
PARENTESIZED_EXPR=129
PLUS=130
PLUS_ASSIGN=131
POST_DEC=132
POST_INC=133
PRE_DEC=134
PRE_INC=135
PRIVATE=136
PROTECTED=137
PUBLIC=138
QUALIFIED_TYPE_IDENT=139
QUESTION=140
RBRACK=141
RCURLY=142
RETURN=143
RPAREN=144
SEMI=145
SHIFT_LEFT=146
SHIFT_LEFT_ASSIGN=147
SHIFT_RIGHT=148
SHIFT_RIGHT_ASSIGN=149
SHORT=150
STAR=151
STAR_ASSIGN=152
STATIC=153
STATIC_ARRAY_CREATOR=154
STRICTFP=155
STRING_LITERAL=156
SUPER=157
SUPER_CONSTRUCTOR_CALL=158
SWITCH=159
SWITCH_BLOCK_LABEL_LIST=160
SYNCHRONIZED=161
THIS=162
THIS_CONSTRUCTOR_CALL=163
THROW=164
THROWS=165
THROWS_CLAUSE=166
TRANSIENT=167
TRUE=168
TRY=169
TYPE=170
UNARY_MINUS=171
UNARY_PLUS=172
UNICODE_ESCAPE=173
VAR_DECLARATION=174
VAR_DECLARATOR=175
VAR_DECLARATOR_LIST=176
VOID=177
VOID_METHOD_DECL=178
VOLATILE=179
WHILE=180
WS=181
XOR=182
XOR_ASSIGN=183


class JavaLexer(Lexer):

    grammarFileName = "Java.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(JavaLexer, self).__init__(input, state)

        self.delegates = []

        self.dfa29 = self.DFA29(
            self, 29,
            eot = self.DFA29_eot,
            eof = self.DFA29_eof,
            min = self.DFA29_min,
            max = self.DFA29_max,
            accept = self.DFA29_accept,
            special = self.DFA29_special,
            transition = self.DFA29_transition
            )






    # $ANTLR start "ABSTRACT"
    def mABSTRACT(self, ):
        try:
            _type = ABSTRACT
            _channel = DEFAULT_CHANNEL

            # Java.g:7:10: ( 'abstract' )
            # Java.g:7:12: 'abstract'
            pass 
            self.match("abstract")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ABSTRACT"



    # $ANTLR start "AND"
    def mAND(self, ):
        try:
            _type = AND
            _channel = DEFAULT_CHANNEL

            # Java.g:8:5: ( '&' )
            # Java.g:8:7: '&'
            pass 
            self.match(38)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AND"



    # $ANTLR start "AND_ASSIGN"
    def mAND_ASSIGN(self, ):
        try:
            _type = AND_ASSIGN
            _channel = DEFAULT_CHANNEL

            # Java.g:9:12: ( '&=' )
            # Java.g:9:14: '&='
            pass 
            self.match("&=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AND_ASSIGN"



    # $ANTLR start "ASSERT"
    def mASSERT(self, ):
        try:
            _type = ASSERT
            _channel = DEFAULT_CHANNEL

            # Java.g:10:8: ( 'assert' )
            # Java.g:10:10: 'assert'
            pass 
            self.match("assert")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ASSERT"



    # $ANTLR start "ASSIGN"
    def mASSIGN(self, ):
        try:
            _type = ASSIGN
            _channel = DEFAULT_CHANNEL

            # Java.g:11:8: ( '=' )
            # Java.g:11:10: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ASSIGN"



    # $ANTLR start "AT"
    def mAT(self, ):
        try:
            _type = AT
            _channel = DEFAULT_CHANNEL

            # Java.g:12:4: ( '@' )
            # Java.g:12:6: '@'
            pass 
            self.match(64)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AT"



    # $ANTLR start "BIT_SHIFT_RIGHT"
    def mBIT_SHIFT_RIGHT(self, ):
        try:
            _type = BIT_SHIFT_RIGHT
            _channel = DEFAULT_CHANNEL

            # Java.g:13:17: ( '>>>' )
            # Java.g:13:19: '>>>'
            pass 
            self.match(">>>")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "BIT_SHIFT_RIGHT"



    # $ANTLR start "BIT_SHIFT_RIGHT_ASSIGN"
    def mBIT_SHIFT_RIGHT_ASSIGN(self, ):
        try:
            _type = BIT_SHIFT_RIGHT_ASSIGN
            _channel = DEFAULT_CHANNEL

            # Java.g:14:24: ( '>>>=' )
            # Java.g:14:26: '>>>='
            pass 
            self.match(">>>=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "BIT_SHIFT_RIGHT_ASSIGN"



    # $ANTLR start "BOOLEAN"
    def mBOOLEAN(self, ):
        try:
            _type = BOOLEAN
            _channel = DEFAULT_CHANNEL

            # Java.g:15:9: ( 'boolean' )
            # Java.g:15:11: 'boolean'
            pass 
            self.match("boolean")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "BOOLEAN"



    # $ANTLR start "BREAK"
    def mBREAK(self, ):
        try:
            _type = BREAK
            _channel = DEFAULT_CHANNEL

            # Java.g:16:7: ( 'break' )
            # Java.g:16:9: 'break'
            pass 
            self.match("break")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "BREAK"



    # $ANTLR start "BYTE"
    def mBYTE(self, ):
        try:
            _type = BYTE
            _channel = DEFAULT_CHANNEL

            # Java.g:17:6: ( 'byte' )
            # Java.g:17:8: 'byte'
            pass 
            self.match("byte")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "BYTE"



    # $ANTLR start "CASE"
    def mCASE(self, ):
        try:
            _type = CASE
            _channel = DEFAULT_CHANNEL

            # Java.g:18:6: ( 'case' )
            # Java.g:18:8: 'case'
            pass 
            self.match("case")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CASE"



    # $ANTLR start "CATCH"
    def mCATCH(self, ):
        try:
            _type = CATCH
            _channel = DEFAULT_CHANNEL

            # Java.g:19:7: ( 'catch' )
            # Java.g:19:9: 'catch'
            pass 
            self.match("catch")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CATCH"



    # $ANTLR start "CHAR"
    def mCHAR(self, ):
        try:
            _type = CHAR
            _channel = DEFAULT_CHANNEL

            # Java.g:20:6: ( 'char' )
            # Java.g:20:8: 'char'
            pass 
            self.match("char")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CHAR"



    # $ANTLR start "CLASS"
    def mCLASS(self, ):
        try:
            _type = CLASS
            _channel = DEFAULT_CHANNEL

            # Java.g:21:7: ( 'class' )
            # Java.g:21:9: 'class'
            pass 
            self.match("class")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CLASS"



    # $ANTLR start "COLON"
    def mCOLON(self, ):
        try:
            _type = COLON
            _channel = DEFAULT_CHANNEL

            # Java.g:22:7: ( ':' )
            # Java.g:22:9: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COLON"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):
        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # Java.g:23:7: ( ',' )
            # Java.g:23:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "CONTINUE"
    def mCONTINUE(self, ):
        try:
            _type = CONTINUE
            _channel = DEFAULT_CHANNEL

            # Java.g:24:10: ( 'continue' )
            # Java.g:24:12: 'continue'
            pass 
            self.match("continue")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CONTINUE"



    # $ANTLR start "DEC"
    def mDEC(self, ):
        try:
            _type = DEC
            _channel = DEFAULT_CHANNEL

            # Java.g:25:5: ( '--' )
            # Java.g:25:7: '--'
            pass 
            self.match("--")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DEC"



    # $ANTLR start "DEFAULT"
    def mDEFAULT(self, ):
        try:
            _type = DEFAULT
            _channel = DEFAULT_CHANNEL

            # Java.g:26:9: ( 'default' )
            # Java.g:26:11: 'default'
            pass 
            self.match("default")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DEFAULT"



    # $ANTLR start "DIV"
    def mDIV(self, ):
        try:
            _type = DIV
            _channel = DEFAULT_CHANNEL

            # Java.g:27:5: ( '/' )
            # Java.g:27:7: '/'
            pass 
            self.match(47)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DIV"



    # $ANTLR start "DIV_ASSIGN"
    def mDIV_ASSIGN(self, ):
        try:
            _type = DIV_ASSIGN
            _channel = DEFAULT_CHANNEL

            # Java.g:28:12: ( '/=' )
            # Java.g:28:14: '/='
            pass 
            self.match("/=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DIV_ASSIGN"



    # $ANTLR start "DO"
    def mDO(self, ):
        try:
            _type = DO
            _channel = DEFAULT_CHANNEL

            # Java.g:29:4: ( 'do' )
            # Java.g:29:6: 'do'
            pass 
            self.match("do")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DO"



    # $ANTLR start "DOT"
    def mDOT(self, ):
        try:
            _type = DOT
            _channel = DEFAULT_CHANNEL

            # Java.g:30:5: ( '.' )
            # Java.g:30:7: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DOT"



    # $ANTLR start "DOTSTAR"
    def mDOTSTAR(self, ):
        try:
            _type = DOTSTAR
            _channel = DEFAULT_CHANNEL

            # Java.g:31:9: ( '.*' )
            # Java.g:31:11: '.*'
            pass 
            self.match(".*")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DOTSTAR"



    # $ANTLR start "DOUBLE"
    def mDOUBLE(self, ):
        try:
            _type = DOUBLE
            _channel = DEFAULT_CHANNEL

            # Java.g:32:8: ( 'double' )
            # Java.g:32:10: 'double'
            pass 
            self.match("double")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DOUBLE"



    # $ANTLR start "ELLIPSIS"
    def mELLIPSIS(self, ):
        try:
            _type = ELLIPSIS
            _channel = DEFAULT_CHANNEL

            # Java.g:33:10: ( '...' )
            # Java.g:33:12: '...'
            pass 
            self.match("...")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ELLIPSIS"



    # $ANTLR start "ELSE"
    def mELSE(self, ):
        try:
            _type = ELSE
            _channel = DEFAULT_CHANNEL

            # Java.g:34:6: ( 'else' )
            # Java.g:34:8: 'else'
            pass 
            self.match("else")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ELSE"



    # $ANTLR start "ENUM"
    def mENUM(self, ):
        try:
            _type = ENUM
            _channel = DEFAULT_CHANNEL

            # Java.g:35:6: ( 'enum' )
            # Java.g:35:8: 'enum'
            pass 
            self.match("enum")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ENUM"



    # $ANTLR start "EQUAL"
    def mEQUAL(self, ):
        try:
            _type = EQUAL
            _channel = DEFAULT_CHANNEL

            # Java.g:36:7: ( '==' )
            # Java.g:36:9: '=='
            pass 
            self.match("==")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EQUAL"



    # $ANTLR start "EXTENDS"
    def mEXTENDS(self, ):
        try:
            _type = EXTENDS
            _channel = DEFAULT_CHANNEL

            # Java.g:37:9: ( 'extends' )
            # Java.g:37:11: 'extends'
            pass 
            self.match("extends")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EXTENDS"



    # $ANTLR start "FALSE"
    def mFALSE(self, ):
        try:
            _type = FALSE
            _channel = DEFAULT_CHANNEL

            # Java.g:38:7: ( 'false' )
            # Java.g:38:9: 'false'
            pass 
            self.match("false")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FALSE"



    # $ANTLR start "FINAL"
    def mFINAL(self, ):
        try:
            _type = FINAL
            _channel = DEFAULT_CHANNEL

            # Java.g:39:7: ( 'final' )
            # Java.g:39:9: 'final'
            pass 
            self.match("final")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FINAL"



    # $ANTLR start "FINALLY"
    def mFINALLY(self, ):
        try:
            _type = FINALLY
            _channel = DEFAULT_CHANNEL

            # Java.g:40:9: ( 'finally' )
            # Java.g:40:11: 'finally'
            pass 
            self.match("finally")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FINALLY"



    # $ANTLR start "FLOAT"
    def mFLOAT(self, ):
        try:
            _type = FLOAT
            _channel = DEFAULT_CHANNEL

            # Java.g:41:7: ( 'float' )
            # Java.g:41:9: 'float'
            pass 
            self.match("float")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FLOAT"



    # $ANTLR start "FOR"
    def mFOR(self, ):
        try:
            _type = FOR
            _channel = DEFAULT_CHANNEL

            # Java.g:42:5: ( 'for' )
            # Java.g:42:7: 'for'
            pass 
            self.match("for")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FOR"



    # $ANTLR start "GREATER_OR_EQUAL"
    def mGREATER_OR_EQUAL(self, ):
        try:
            _type = GREATER_OR_EQUAL
            _channel = DEFAULT_CHANNEL

            # Java.g:43:18: ( '>=' )
            # Java.g:43:20: '>='
            pass 
            self.match(">=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GREATER_OR_EQUAL"



    # $ANTLR start "GREATER_THAN"
    def mGREATER_THAN(self, ):
        try:
            _type = GREATER_THAN
            _channel = DEFAULT_CHANNEL

            # Java.g:44:14: ( '>' )
            # Java.g:44:16: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GREATER_THAN"



    # $ANTLR start "IF"
    def mIF(self, ):
        try:
            _type = IF
            _channel = DEFAULT_CHANNEL

            # Java.g:45:4: ( 'if' )
            # Java.g:45:6: 'if'
            pass 
            self.match("if")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IF"



    # $ANTLR start "IMPLEMENTS"
    def mIMPLEMENTS(self, ):
        try:
            _type = IMPLEMENTS
            _channel = DEFAULT_CHANNEL

            # Java.g:46:12: ( 'implements' )
            # Java.g:46:14: 'implements'
            pass 
            self.match("implements")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IMPLEMENTS"



    # $ANTLR start "IMPORT"
    def mIMPORT(self, ):
        try:
            _type = IMPORT
            _channel = DEFAULT_CHANNEL

            # Java.g:47:8: ( 'import' )
            # Java.g:47:10: 'import'
            pass 
            self.match("import")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IMPORT"



    # $ANTLR start "INC"
    def mINC(self, ):
        try:
            _type = INC
            _channel = DEFAULT_CHANNEL

            # Java.g:48:5: ( '++' )
            # Java.g:48:7: '++'
            pass 
            self.match("++")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "INC"



    # $ANTLR start "INSTANCEOF"
    def mINSTANCEOF(self, ):
        try:
            _type = INSTANCEOF
            _channel = DEFAULT_CHANNEL

            # Java.g:49:12: ( 'instanceof' )
            # Java.g:49:14: 'instanceof'
            pass 
            self.match("instanceof")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "INSTANCEOF"



    # $ANTLR start "INT"
    def mINT(self, ):
        try:
            _type = INT
            _channel = DEFAULT_CHANNEL

            # Java.g:50:5: ( 'int' )
            # Java.g:50:7: 'int'
            pass 
            self.match("int")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "INT"



    # $ANTLR start "INTERFACE"
    def mINTERFACE(self, ):
        try:
            _type = INTERFACE
            _channel = DEFAULT_CHANNEL

            # Java.g:51:11: ( 'interface' )
            # Java.g:51:13: 'interface'
            pass 
            self.match("interface")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "INTERFACE"



    # $ANTLR start "LBRACK"
    def mLBRACK(self, ):
        try:
            _type = LBRACK
            _channel = DEFAULT_CHANNEL

            # Java.g:52:8: ( '[' )
            # Java.g:52:10: '['
            pass 
            self.match(91)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LBRACK"



    # $ANTLR start "LCURLY"
    def mLCURLY(self, ):
        try:
            _type = LCURLY
            _channel = DEFAULT_CHANNEL

            # Java.g:53:8: ( '{' )
            # Java.g:53:10: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LCURLY"



    # $ANTLR start "LESS_OR_EQUAL"
    def mLESS_OR_EQUAL(self, ):
        try:
            _type = LESS_OR_EQUAL
            _channel = DEFAULT_CHANNEL

            # Java.g:54:15: ( '<=' )
            # Java.g:54:17: '<='
            pass 
            self.match("<=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LESS_OR_EQUAL"



    # $ANTLR start "LESS_THAN"
    def mLESS_THAN(self, ):
        try:
            _type = LESS_THAN
            _channel = DEFAULT_CHANNEL

            # Java.g:55:11: ( '<' )
            # Java.g:55:13: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LESS_THAN"



    # $ANTLR start "LOGICAL_AND"
    def mLOGICAL_AND(self, ):
        try:
            _type = LOGICAL_AND
            _channel = DEFAULT_CHANNEL

            # Java.g:56:13: ( '&&' )
            # Java.g:56:15: '&&'
            pass 
            self.match("&&")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LOGICAL_AND"



    # $ANTLR start "LOGICAL_NOT"
    def mLOGICAL_NOT(self, ):
        try:
            _type = LOGICAL_NOT
            _channel = DEFAULT_CHANNEL

            # Java.g:57:13: ( '!' )
            # Java.g:57:15: '!'
            pass 
            self.match(33)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LOGICAL_NOT"



    # $ANTLR start "LOGICAL_OR"
    def mLOGICAL_OR(self, ):
        try:
            _type = LOGICAL_OR
            _channel = DEFAULT_CHANNEL

            # Java.g:58:12: ( '||' )
            # Java.g:58:14: '||'
            pass 
            self.match("||")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LOGICAL_OR"



    # $ANTLR start "LONG"
    def mLONG(self, ):
        try:
            _type = LONG
            _channel = DEFAULT_CHANNEL

            # Java.g:59:6: ( 'long' )
            # Java.g:59:8: 'long'
            pass 
            self.match("long")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LONG"



    # $ANTLR start "LPAREN"
    def mLPAREN(self, ):
        try:
            _type = LPAREN
            _channel = DEFAULT_CHANNEL

            # Java.g:60:8: ( '(' )
            # Java.g:60:10: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LPAREN"



    # $ANTLR start "MINUS"
    def mMINUS(self, ):
        try:
            _type = MINUS
            _channel = DEFAULT_CHANNEL

            # Java.g:61:7: ( '-' )
            # Java.g:61:9: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MINUS"



    # $ANTLR start "MINUS_ASSIGN"
    def mMINUS_ASSIGN(self, ):
        try:
            _type = MINUS_ASSIGN
            _channel = DEFAULT_CHANNEL

            # Java.g:62:14: ( '-=' )
            # Java.g:62:16: '-='
            pass 
            self.match("-=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MINUS_ASSIGN"



    # $ANTLR start "MOD"
    def mMOD(self, ):
        try:
            _type = MOD
            _channel = DEFAULT_CHANNEL

            # Java.g:63:5: ( '%' )
            # Java.g:63:7: '%'
            pass 
            self.match(37)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MOD"



    # $ANTLR start "MOD_ASSIGN"
    def mMOD_ASSIGN(self, ):
        try:
            _type = MOD_ASSIGN
            _channel = DEFAULT_CHANNEL

            # Java.g:64:12: ( '%=' )
            # Java.g:64:14: '%='
            pass 
            self.match("%=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MOD_ASSIGN"



    # $ANTLR start "NATIVE"
    def mNATIVE(self, ):
        try:
            _type = NATIVE
            _channel = DEFAULT_CHANNEL

            # Java.g:65:8: ( 'native' )
            # Java.g:65:10: 'native'
            pass 
            self.match("native")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NATIVE"



    # $ANTLR start "NEW"
    def mNEW(self, ):
        try:
            _type = NEW
            _channel = DEFAULT_CHANNEL

            # Java.g:66:5: ( 'new' )
            # Java.g:66:7: 'new'
            pass 
            self.match("new")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NEW"



    # $ANTLR start "NOT"
    def mNOT(self, ):
        try:
            _type = NOT
            _channel = DEFAULT_CHANNEL

            # Java.g:67:5: ( '~' )
            # Java.g:67:7: '~'
            pass 
            self.match(126)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NOT"



    # $ANTLR start "NOT_EQUAL"
    def mNOT_EQUAL(self, ):
        try:
            _type = NOT_EQUAL
            _channel = DEFAULT_CHANNEL

            # Java.g:68:11: ( '!=' )
            # Java.g:68:13: '!='
            pass 
            self.match("!=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NOT_EQUAL"



    # $ANTLR start "NULL"
    def mNULL(self, ):
        try:
            _type = NULL
            _channel = DEFAULT_CHANNEL

            # Java.g:69:6: ( 'null' )
            # Java.g:69:8: 'null'
            pass 
            self.match("null")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NULL"



    # $ANTLR start "OR"
    def mOR(self, ):
        try:
            _type = OR
            _channel = DEFAULT_CHANNEL

            # Java.g:70:4: ( '|' )
            # Java.g:70:6: '|'
            pass 
            self.match(124)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OR"



    # $ANTLR start "OR_ASSIGN"
    def mOR_ASSIGN(self, ):
        try:
            _type = OR_ASSIGN
            _channel = DEFAULT_CHANNEL

            # Java.g:71:11: ( '|=' )
            # Java.g:71:13: '|='
            pass 
            self.match("|=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OR_ASSIGN"



    # $ANTLR start "PACKAGE"
    def mPACKAGE(self, ):
        try:
            _type = PACKAGE
            _channel = DEFAULT_CHANNEL

            # Java.g:72:9: ( 'package' )
            # Java.g:72:11: 'package'
            pass 
            self.match("package")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PACKAGE"



    # $ANTLR start "PLUS"
    def mPLUS(self, ):
        try:
            _type = PLUS
            _channel = DEFAULT_CHANNEL

            # Java.g:73:6: ( '+' )
            # Java.g:73:8: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PLUS"



    # $ANTLR start "PLUS_ASSIGN"
    def mPLUS_ASSIGN(self, ):
        try:
            _type = PLUS_ASSIGN
            _channel = DEFAULT_CHANNEL

            # Java.g:74:13: ( '+=' )
            # Java.g:74:15: '+='
            pass 
            self.match("+=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PLUS_ASSIGN"



    # $ANTLR start "PRIVATE"
    def mPRIVATE(self, ):
        try:
            _type = PRIVATE
            _channel = DEFAULT_CHANNEL

            # Java.g:75:9: ( 'private' )
            # Java.g:75:11: 'private'
            pass 
            self.match("private")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PRIVATE"



    # $ANTLR start "PROTECTED"
    def mPROTECTED(self, ):
        try:
            _type = PROTECTED
            _channel = DEFAULT_CHANNEL

            # Java.g:76:11: ( 'protected' )
            # Java.g:76:13: 'protected'
            pass 
            self.match("protected")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PROTECTED"



    # $ANTLR start "PUBLIC"
    def mPUBLIC(self, ):
        try:
            _type = PUBLIC
            _channel = DEFAULT_CHANNEL

            # Java.g:77:8: ( 'public' )
            # Java.g:77:10: 'public'
            pass 
            self.match("public")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PUBLIC"



    # $ANTLR start "QUESTION"
    def mQUESTION(self, ):
        try:
            _type = QUESTION
            _channel = DEFAULT_CHANNEL

            # Java.g:78:10: ( '?' )
            # Java.g:78:12: '?'
            pass 
            self.match(63)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "QUESTION"



    # $ANTLR start "RBRACK"
    def mRBRACK(self, ):
        try:
            _type = RBRACK
            _channel = DEFAULT_CHANNEL

            # Java.g:79:8: ( ']' )
            # Java.g:79:10: ']'
            pass 
            self.match(93)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RBRACK"



    # $ANTLR start "RCURLY"
    def mRCURLY(self, ):
        try:
            _type = RCURLY
            _channel = DEFAULT_CHANNEL

            # Java.g:80:8: ( '}' )
            # Java.g:80:10: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RCURLY"



    # $ANTLR start "RETURN"
    def mRETURN(self, ):
        try:
            _type = RETURN
            _channel = DEFAULT_CHANNEL

            # Java.g:81:8: ( 'return' )
            # Java.g:81:10: 'return'
            pass 
            self.match("return")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RETURN"



    # $ANTLR start "RPAREN"
    def mRPAREN(self, ):
        try:
            _type = RPAREN
            _channel = DEFAULT_CHANNEL

            # Java.g:82:8: ( ')' )
            # Java.g:82:10: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RPAREN"



    # $ANTLR start "SEMI"
    def mSEMI(self, ):
        try:
            _type = SEMI
            _channel = DEFAULT_CHANNEL

            # Java.g:83:6: ( ';' )
            # Java.g:83:8: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SEMI"



    # $ANTLR start "SHIFT_LEFT"
    def mSHIFT_LEFT(self, ):
        try:
            _type = SHIFT_LEFT
            _channel = DEFAULT_CHANNEL

            # Java.g:84:12: ( '<<' )
            # Java.g:84:14: '<<'
            pass 
            self.match("<<")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SHIFT_LEFT"



    # $ANTLR start "SHIFT_LEFT_ASSIGN"
    def mSHIFT_LEFT_ASSIGN(self, ):
        try:
            _type = SHIFT_LEFT_ASSIGN
            _channel = DEFAULT_CHANNEL

            # Java.g:85:19: ( '<<=' )
            # Java.g:85:21: '<<='
            pass 
            self.match("<<=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SHIFT_LEFT_ASSIGN"



    # $ANTLR start "SHIFT_RIGHT"
    def mSHIFT_RIGHT(self, ):
        try:
            _type = SHIFT_RIGHT
            _channel = DEFAULT_CHANNEL

            # Java.g:86:13: ( '>>' )
            # Java.g:86:15: '>>'
            pass 
            self.match(">>")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SHIFT_RIGHT"



    # $ANTLR start "SHIFT_RIGHT_ASSIGN"
    def mSHIFT_RIGHT_ASSIGN(self, ):
        try:
            _type = SHIFT_RIGHT_ASSIGN
            _channel = DEFAULT_CHANNEL

            # Java.g:87:20: ( '>>=' )
            # Java.g:87:22: '>>='
            pass 
            self.match(">>=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SHIFT_RIGHT_ASSIGN"



    # $ANTLR start "SHORT"
    def mSHORT(self, ):
        try:
            _type = SHORT
            _channel = DEFAULT_CHANNEL

            # Java.g:88:7: ( 'short' )
            # Java.g:88:9: 'short'
            pass 
            self.match("short")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SHORT"



    # $ANTLR start "STAR"
    def mSTAR(self, ):
        try:
            _type = STAR
            _channel = DEFAULT_CHANNEL

            # Java.g:89:6: ( '*' )
            # Java.g:89:8: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STAR"



    # $ANTLR start "STAR_ASSIGN"
    def mSTAR_ASSIGN(self, ):
        try:
            _type = STAR_ASSIGN
            _channel = DEFAULT_CHANNEL

            # Java.g:90:13: ( '*=' )
            # Java.g:90:15: '*='
            pass 
            self.match("*=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STAR_ASSIGN"



    # $ANTLR start "STATIC"
    def mSTATIC(self, ):
        try:
            _type = STATIC
            _channel = DEFAULT_CHANNEL

            # Java.g:91:8: ( 'static' )
            # Java.g:91:10: 'static'
            pass 
            self.match("static")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STATIC"



    # $ANTLR start "STRICTFP"
    def mSTRICTFP(self, ):
        try:
            _type = STRICTFP
            _channel = DEFAULT_CHANNEL

            # Java.g:92:10: ( 'strictfp' )
            # Java.g:92:12: 'strictfp'
            pass 
            self.match("strictfp")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STRICTFP"



    # $ANTLR start "SUPER"
    def mSUPER(self, ):
        try:
            _type = SUPER
            _channel = DEFAULT_CHANNEL

            # Java.g:93:7: ( 'super' )
            # Java.g:93:9: 'super'
            pass 
            self.match("super")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SUPER"



    # $ANTLR start "SWITCH"
    def mSWITCH(self, ):
        try:
            _type = SWITCH
            _channel = DEFAULT_CHANNEL

            # Java.g:94:8: ( 'switch' )
            # Java.g:94:10: 'switch'
            pass 
            self.match("switch")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SWITCH"



    # $ANTLR start "SYNCHRONIZED"
    def mSYNCHRONIZED(self, ):
        try:
            _type = SYNCHRONIZED
            _channel = DEFAULT_CHANNEL

            # Java.g:95:14: ( 'synchronized' )
            # Java.g:95:16: 'synchronized'
            pass 
            self.match("synchronized")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SYNCHRONIZED"



    # $ANTLR start "THIS"
    def mTHIS(self, ):
        try:
            _type = THIS
            _channel = DEFAULT_CHANNEL

            # Java.g:96:6: ( 'this' )
            # Java.g:96:8: 'this'
            pass 
            self.match("this")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "THIS"



    # $ANTLR start "THROW"
    def mTHROW(self, ):
        try:
            _type = THROW
            _channel = DEFAULT_CHANNEL

            # Java.g:97:7: ( 'throw' )
            # Java.g:97:9: 'throw'
            pass 
            self.match("throw")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "THROW"



    # $ANTLR start "THROWS"
    def mTHROWS(self, ):
        try:
            _type = THROWS
            _channel = DEFAULT_CHANNEL

            # Java.g:98:8: ( 'throws' )
            # Java.g:98:10: 'throws'
            pass 
            self.match("throws")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "THROWS"



    # $ANTLR start "TRANSIENT"
    def mTRANSIENT(self, ):
        try:
            _type = TRANSIENT
            _channel = DEFAULT_CHANNEL

            # Java.g:99:11: ( 'transient' )
            # Java.g:99:13: 'transient'
            pass 
            self.match("transient")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TRANSIENT"



    # $ANTLR start "TRUE"
    def mTRUE(self, ):
        try:
            _type = TRUE
            _channel = DEFAULT_CHANNEL

            # Java.g:100:6: ( 'true' )
            # Java.g:100:8: 'true'
            pass 
            self.match("true")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TRUE"



    # $ANTLR start "TRY"
    def mTRY(self, ):
        try:
            _type = TRY
            _channel = DEFAULT_CHANNEL

            # Java.g:101:5: ( 'try' )
            # Java.g:101:7: 'try'
            pass 
            self.match("try")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TRY"



    # $ANTLR start "VOID"
    def mVOID(self, ):
        try:
            _type = VOID
            _channel = DEFAULT_CHANNEL

            # Java.g:102:6: ( 'void' )
            # Java.g:102:8: 'void'
            pass 
            self.match("void")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "VOID"



    # $ANTLR start "VOLATILE"
    def mVOLATILE(self, ):
        try:
            _type = VOLATILE
            _channel = DEFAULT_CHANNEL

            # Java.g:103:10: ( 'volatile' )
            # Java.g:103:12: 'volatile'
            pass 
            self.match("volatile")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "VOLATILE"



    # $ANTLR start "WHILE"
    def mWHILE(self, ):
        try:
            _type = WHILE
            _channel = DEFAULT_CHANNEL

            # Java.g:104:7: ( 'while' )
            # Java.g:104:9: 'while'
            pass 
            self.match("while")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WHILE"



    # $ANTLR start "XOR"
    def mXOR(self, ):
        try:
            _type = XOR
            _channel = DEFAULT_CHANNEL

            # Java.g:105:5: ( '^' )
            # Java.g:105:7: '^'
            pass 
            self.match(94)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "XOR"



    # $ANTLR start "XOR_ASSIGN"
    def mXOR_ASSIGN(self, ):
        try:
            _type = XOR_ASSIGN
            _channel = DEFAULT_CHANNEL

            # Java.g:106:12: ( '^=' )
            # Java.g:106:14: '^='
            pass 
            self.match("^=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "XOR_ASSIGN"



    # $ANTLR start "HEX_LITERAL"
    def mHEX_LITERAL(self, ):
        try:
            _type = HEX_LITERAL
            _channel = DEFAULT_CHANNEL

            # Java.g:985:13: ( '0' ( 'x' | 'X' ) ( HEX_DIGIT )+ ( INTEGER_TYPE_SUFFIX )? )
            # Java.g:985:15: '0' ( 'x' | 'X' ) ( HEX_DIGIT )+ ( INTEGER_TYPE_SUFFIX )?
            pass 
            self.match(48)

            if self.input.LA(1) == 88 or self.input.LA(1) == 120:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # Java.g:985:29: ( HEX_DIGIT )+
            cnt1 = 0
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((48 <= LA1_0 <= 57) or (65 <= LA1_0 <= 70) or (97 <= LA1_0 <= 102)) :
                    alt1 = 1


                if alt1 == 1:
                    # Java.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70) or (97 <= self.input.LA(1) <= 102):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt1 >= 1:
                        break #loop1

                    eee = EarlyExitException(1, self.input)
                    raise eee

                cnt1 += 1


            # Java.g:985:40: ( INTEGER_TYPE_SUFFIX )?
            alt2 = 2
            LA2_0 = self.input.LA(1)

            if (LA2_0 == 76 or LA2_0 == 108) :
                alt2 = 1
            if alt2 == 1:
                # Java.g:
                pass 
                if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse








            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "HEX_LITERAL"



    # $ANTLR start "DECIMAL_LITERAL"
    def mDECIMAL_LITERAL(self, ):
        try:
            _type = DECIMAL_LITERAL
            _channel = DEFAULT_CHANNEL

            # Java.g:987:17: ( ( '0' | '1' .. '9' ( '0' .. '9' )* ) ( INTEGER_TYPE_SUFFIX )? )
            # Java.g:987:19: ( '0' | '1' .. '9' ( '0' .. '9' )* ) ( INTEGER_TYPE_SUFFIX )?
            pass 
            # Java.g:987:19: ( '0' | '1' .. '9' ( '0' .. '9' )* )
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if (LA4_0 == 48) :
                alt4 = 1
            elif ((49 <= LA4_0 <= 57)) :
                alt4 = 2
            else:
                nvae = NoViableAltException("", 4, 0, self.input)

                raise nvae


            if alt4 == 1:
                # Java.g:987:20: '0'
                pass 
                self.match(48)


            elif alt4 == 2:
                # Java.g:987:26: '1' .. '9' ( '0' .. '9' )*
                pass 
                self.matchRange(49, 57)

                # Java.g:987:35: ( '0' .. '9' )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if ((48 <= LA3_0 <= 57)) :
                        alt3 = 1


                    if alt3 == 1:
                        # Java.g:
                        pass 
                        if (48 <= self.input.LA(1) <= 57):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop3





            # Java.g:987:46: ( INTEGER_TYPE_SUFFIX )?
            alt5 = 2
            LA5_0 = self.input.LA(1)

            if (LA5_0 == 76 or LA5_0 == 108) :
                alt5 = 1
            if alt5 == 1:
                # Java.g:
                pass 
                if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse








            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DECIMAL_LITERAL"



    # $ANTLR start "OCTAL_LITERAL"
    def mOCTAL_LITERAL(self, ):
        try:
            _type = OCTAL_LITERAL
            _channel = DEFAULT_CHANNEL

            # Java.g:989:15: ( '0' ( '0' .. '7' )+ ( INTEGER_TYPE_SUFFIX )? )
            # Java.g:989:17: '0' ( '0' .. '7' )+ ( INTEGER_TYPE_SUFFIX )?
            pass 
            self.match(48)

            # Java.g:989:21: ( '0' .. '7' )+
            cnt6 = 0
            while True: #loop6
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if ((48 <= LA6_0 <= 55)) :
                    alt6 = 1


                if alt6 == 1:
                    # Java.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 55):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt6 >= 1:
                        break #loop6

                    eee = EarlyExitException(6, self.input)
                    raise eee

                cnt6 += 1


            # Java.g:989:33: ( INTEGER_TYPE_SUFFIX )?
            alt7 = 2
            LA7_0 = self.input.LA(1)

            if (LA7_0 == 76 or LA7_0 == 108) :
                alt7 = 1
            if alt7 == 1:
                # Java.g:
                pass 
                if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse








            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OCTAL_LITERAL"



    # $ANTLR start "HEX_DIGIT"
    def mHEX_DIGIT(self, ):
        try:
            # Java.g:993:11: ( ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' ) )
            # Java.g:
            pass 
            if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70) or (97 <= self.input.LA(1) <= 102):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "HEX_DIGIT"



    # $ANTLR start "INTEGER_TYPE_SUFFIX"
    def mINTEGER_TYPE_SUFFIX(self, ):
        try:
            # Java.g:996:21: ( ( 'l' | 'L' ) )
            # Java.g:
            pass 
            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "INTEGER_TYPE_SUFFIX"



    # $ANTLR start "FLOATING_POINT_LITERAL"
    def mFLOATING_POINT_LITERAL(self, ):
        try:
            _type = FLOATING_POINT_LITERAL
            _channel = DEFAULT_CHANNEL

            # Java.g:998:5: ( ( '0' .. '9' )+ ( DOT ( '0' .. '9' )* ( EXPONENT )? ( FLOAT_TYPE_SUFFIX )? | EXPONENT ( FLOAT_TYPE_SUFFIX )? | FLOAT_TYPE_SUFFIX ) | DOT ( '0' .. '9' )+ ( EXPONENT )? ( FLOAT_TYPE_SUFFIX )? )
            alt17 = 2
            LA17_0 = self.input.LA(1)

            if ((48 <= LA17_0 <= 57)) :
                alt17 = 1
            elif (LA17_0 == 46) :
                alt17 = 2
            else:
                nvae = NoViableAltException("", 17, 0, self.input)

                raise nvae


            if alt17 == 1:
                # Java.g:998:9: ( '0' .. '9' )+ ( DOT ( '0' .. '9' )* ( EXPONENT )? ( FLOAT_TYPE_SUFFIX )? | EXPONENT ( FLOAT_TYPE_SUFFIX )? | FLOAT_TYPE_SUFFIX )
                pass 
                # Java.g:998:9: ( '0' .. '9' )+
                cnt8 = 0
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if ((48 <= LA8_0 <= 57)) :
                        alt8 = 1


                    if alt8 == 1:
                        # Java.g:
                        pass 
                        if (48 <= self.input.LA(1) <= 57):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        if cnt8 >= 1:
                            break #loop8

                        eee = EarlyExitException(8, self.input)
                        raise eee

                    cnt8 += 1


                # Java.g:999:9: ( DOT ( '0' .. '9' )* ( EXPONENT )? ( FLOAT_TYPE_SUFFIX )? | EXPONENT ( FLOAT_TYPE_SUFFIX )? | FLOAT_TYPE_SUFFIX )
                alt13 = 3
                LA13 = self.input.LA(1)
                if LA13 == 46:
                    alt13 = 1
                elif LA13 == 69 or LA13 == 101:
                    alt13 = 2
                elif LA13 == 68 or LA13 == 70 or LA13 == 100 or LA13 == 102:
                    alt13 = 3
                else:
                    nvae = NoViableAltException("", 13, 0, self.input)

                    raise nvae


                if alt13 == 1:
                    # Java.g:1000:13: DOT ( '0' .. '9' )* ( EXPONENT )? ( FLOAT_TYPE_SUFFIX )?
                    pass 
                    self.mDOT()


                    # Java.g:1000:17: ( '0' .. '9' )*
                    while True: #loop9
                        alt9 = 2
                        LA9_0 = self.input.LA(1)

                        if ((48 <= LA9_0 <= 57)) :
                            alt9 = 1


                        if alt9 == 1:
                            # Java.g:
                            pass 
                            if (48 <= self.input.LA(1) <= 57):
                                self.input.consume()
                            else:
                                mse = MismatchedSetException(None, self.input)
                                self.recover(mse)
                                raise mse




                        else:
                            break #loop9


                    # Java.g:1000:29: ( EXPONENT )?
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == 69 or LA10_0 == 101) :
                        alt10 = 1
                    if alt10 == 1:
                        # Java.g:1000:29: EXPONENT
                        pass 
                        self.mEXPONENT()





                    # Java.g:1000:39: ( FLOAT_TYPE_SUFFIX )?
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == 68 or LA11_0 == 70 or LA11_0 == 100 or LA11_0 == 102) :
                        alt11 = 1
                    if alt11 == 1:
                        # Java.g:
                        pass 
                        if self.input.LA(1) == 68 or self.input.LA(1) == 70 or self.input.LA(1) == 100 or self.input.LA(1) == 102:
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse







                elif alt13 == 2:
                    # Java.g:1001:13: EXPONENT ( FLOAT_TYPE_SUFFIX )?
                    pass 
                    self.mEXPONENT()


                    # Java.g:1001:22: ( FLOAT_TYPE_SUFFIX )?
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == 68 or LA12_0 == 70 or LA12_0 == 100 or LA12_0 == 102) :
                        alt12 = 1
                    if alt12 == 1:
                        # Java.g:
                        pass 
                        if self.input.LA(1) == 68 or self.input.LA(1) == 70 or self.input.LA(1) == 100 or self.input.LA(1) == 102:
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse







                elif alt13 == 3:
                    # Java.g:1002:13: FLOAT_TYPE_SUFFIX
                    pass 
                    self.mFLOAT_TYPE_SUFFIX()






            elif alt17 == 2:
                # Java.g:1004:9: DOT ( '0' .. '9' )+ ( EXPONENT )? ( FLOAT_TYPE_SUFFIX )?
                pass 
                self.mDOT()


                # Java.g:1004:13: ( '0' .. '9' )+
                cnt14 = 0
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if ((48 <= LA14_0 <= 57)) :
                        alt14 = 1


                    if alt14 == 1:
                        # Java.g:
                        pass 
                        if (48 <= self.input.LA(1) <= 57):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        if cnt14 >= 1:
                            break #loop14

                        eee = EarlyExitException(14, self.input)
                        raise eee

                    cnt14 += 1


                # Java.g:1004:25: ( EXPONENT )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == 69 or LA15_0 == 101) :
                    alt15 = 1
                if alt15 == 1:
                    # Java.g:1004:25: EXPONENT
                    pass 
                    self.mEXPONENT()





                # Java.g:1004:35: ( FLOAT_TYPE_SUFFIX )?
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == 68 or LA16_0 == 70 or LA16_0 == 100 or LA16_0 == 102) :
                    alt16 = 1
                if alt16 == 1:
                    # Java.g:
                    pass 
                    if self.input.LA(1) == 68 or self.input.LA(1) == 70 or self.input.LA(1) == 100 or self.input.LA(1) == 102:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse







            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FLOATING_POINT_LITERAL"



    # $ANTLR start "EXPONENT"
    def mEXPONENT(self, ):
        try:
            # Java.g:1009:10: ( ( 'e' | 'E' ) ( '+' | '-' )? ( '0' .. '9' )+ )
            # Java.g:1009:12: ( 'e' | 'E' ) ( '+' | '-' )? ( '0' .. '9' )+
            pass 
            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # Java.g:1009:22: ( '+' | '-' )?
            alt18 = 2
            LA18_0 = self.input.LA(1)

            if (LA18_0 == 43 or LA18_0 == 45) :
                alt18 = 1
            if alt18 == 1:
                # Java.g:
                pass 
                if self.input.LA(1) == 43 or self.input.LA(1) == 45:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse






            # Java.g:1009:33: ( '0' .. '9' )+
            cnt19 = 0
            while True: #loop19
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if ((48 <= LA19_0 <= 57)) :
                    alt19 = 1


                if alt19 == 1:
                    # Java.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt19 >= 1:
                        break #loop19

                    eee = EarlyExitException(19, self.input)
                    raise eee

                cnt19 += 1





        finally:
            pass

    # $ANTLR end "EXPONENT"



    # $ANTLR start "FLOAT_TYPE_SUFFIX"
    def mFLOAT_TYPE_SUFFIX(self, ):
        try:
            # Java.g:1012:19: ( ( 'f' | 'F' | 'd' | 'D' ) )
            # Java.g:
            pass 
            if self.input.LA(1) == 68 or self.input.LA(1) == 70 or self.input.LA(1) == 100 or self.input.LA(1) == 102:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "FLOAT_TYPE_SUFFIX"



    # $ANTLR start "CHARACTER_LITERAL"
    def mCHARACTER_LITERAL(self, ):
        try:
            _type = CHARACTER_LITERAL
            _channel = DEFAULT_CHANNEL

            # Java.g:1014:5: ( '\\'' ( ESCAPE_SEQUENCE |~ ( '\\'' | '\\\\' ) ) '\\'' )
            # Java.g:1014:9: '\\'' ( ESCAPE_SEQUENCE |~ ( '\\'' | '\\\\' ) ) '\\''
            pass 
            self.match(39)

            # Java.g:1014:14: ( ESCAPE_SEQUENCE |~ ( '\\'' | '\\\\' ) )
            alt20 = 2
            LA20_0 = self.input.LA(1)

            if (LA20_0 == 92) :
                alt20 = 1
            elif ((0 <= LA20_0 <= 38) or (40 <= LA20_0 <= 91) or (93 <= LA20_0 <= 65535)) :
                alt20 = 2
            else:
                nvae = NoViableAltException("", 20, 0, self.input)

                raise nvae


            if alt20 == 1:
                # Java.g:1014:16: ESCAPE_SEQUENCE
                pass 
                self.mESCAPE_SEQUENCE()



            elif alt20 == 2:
                # Java.g:1014:34: ~ ( '\\'' | '\\\\' )
                pass 
                if (0 <= self.input.LA(1) <= 38) or (40 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse






            self.match(39)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CHARACTER_LITERAL"



    # $ANTLR start "STRING_LITERAL"
    def mSTRING_LITERAL(self, ):
        try:
            _type = STRING_LITERAL
            _channel = DEFAULT_CHANNEL

            # Java.g:1018:5: ( '\"' ( ESCAPE_SEQUENCE |~ ( '\\\\' | '\"' ) )* '\"' )
            # Java.g:1018:8: '\"' ( ESCAPE_SEQUENCE |~ ( '\\\\' | '\"' ) )* '\"'
            pass 
            self.match(34)

            # Java.g:1018:12: ( ESCAPE_SEQUENCE |~ ( '\\\\' | '\"' ) )*
            while True: #loop21
                alt21 = 3
                LA21_0 = self.input.LA(1)

                if (LA21_0 == 92) :
                    alt21 = 1
                elif ((0 <= LA21_0 <= 33) or (35 <= LA21_0 <= 91) or (93 <= LA21_0 <= 65535)) :
                    alt21 = 2


                if alt21 == 1:
                    # Java.g:1018:14: ESCAPE_SEQUENCE
                    pass 
                    self.mESCAPE_SEQUENCE()



                elif alt21 == 2:
                    # Java.g:1018:32: ~ ( '\\\\' | '\"' )
                    pass 
                    if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop21


            self.match(34)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STRING_LITERAL"



    # $ANTLR start "ESCAPE_SEQUENCE"
    def mESCAPE_SEQUENCE(self, ):
        try:
            # Java.g:1024:5: ( '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' ) | UNICODE_ESCAPE | OCTAL_ESCAPE )
            alt22 = 3
            LA22_0 = self.input.LA(1)

            if (LA22_0 == 92) :
                LA22 = self.input.LA(2)
                if LA22 == 34 or LA22 == 39 or LA22 == 92 or LA22 == 98 or LA22 == 102 or LA22 == 110 or LA22 == 114 or LA22 == 116:
                    alt22 = 1
                elif LA22 == 117:
                    alt22 = 2
                elif LA22 == 48 or LA22 == 49 or LA22 == 50 or LA22 == 51 or LA22 == 52 or LA22 == 53 or LA22 == 54 or LA22 == 55:
                    alt22 = 3
                else:
                    nvae = NoViableAltException("", 22, 1, self.input)

                    raise nvae


            else:
                nvae = NoViableAltException("", 22, 0, self.input)

                raise nvae


            if alt22 == 1:
                # Java.g:1024:9: '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' )
                pass 
                self.match(92)

                if self.input.LA(1) == 34 or self.input.LA(1) == 39 or self.input.LA(1) == 92 or self.input.LA(1) == 98 or self.input.LA(1) == 102 or self.input.LA(1) == 110 or self.input.LA(1) == 114 or self.input.LA(1) == 116:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            elif alt22 == 2:
                # Java.g:1025:9: UNICODE_ESCAPE
                pass 
                self.mUNICODE_ESCAPE()



            elif alt22 == 3:
                # Java.g:1026:9: OCTAL_ESCAPE
                pass 
                self.mOCTAL_ESCAPE()




        finally:
            pass

    # $ANTLR end "ESCAPE_SEQUENCE"



    # $ANTLR start "OCTAL_ESCAPE"
    def mOCTAL_ESCAPE(self, ):
        try:
            # Java.g:1031:5: ( '\\\\' ( '0' .. '3' ) ( '0' .. '7' ) ( '0' .. '7' ) | '\\\\' ( '0' .. '7' ) ( '0' .. '7' ) | '\\\\' ( '0' .. '7' ) )
            alt23 = 3
            LA23_0 = self.input.LA(1)

            if (LA23_0 == 92) :
                LA23_1 = self.input.LA(2)

                if ((48 <= LA23_1 <= 51)) :
                    LA23_2 = self.input.LA(3)

                    if ((48 <= LA23_2 <= 55)) :
                        LA23_4 = self.input.LA(4)

                        if ((48 <= LA23_4 <= 55)) :
                            alt23 = 1
                        else:
                            alt23 = 2

                    else:
                        alt23 = 3

                elif ((52 <= LA23_1 <= 55)) :
                    LA23_3 = self.input.LA(3)

                    if ((48 <= LA23_3 <= 55)) :
                        alt23 = 2
                    else:
                        alt23 = 3

                else:
                    nvae = NoViableAltException("", 23, 1, self.input)

                    raise nvae


            else:
                nvae = NoViableAltException("", 23, 0, self.input)

                raise nvae


            if alt23 == 1:
                # Java.g:1031:9: '\\\\' ( '0' .. '3' ) ( '0' .. '7' ) ( '0' .. '7' )
                pass 
                self.match(92)

                if (48 <= self.input.LA(1) <= 51):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



                if (48 <= self.input.LA(1) <= 55):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



                if (48 <= self.input.LA(1) <= 55):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            elif alt23 == 2:
                # Java.g:1032:9: '\\\\' ( '0' .. '7' ) ( '0' .. '7' )
                pass 
                self.match(92)

                if (48 <= self.input.LA(1) <= 55):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



                if (48 <= self.input.LA(1) <= 55):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            elif alt23 == 3:
                # Java.g:1033:9: '\\\\' ( '0' .. '7' )
                pass 
                self.match(92)

                if (48 <= self.input.LA(1) <= 55):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse





        finally:
            pass

    # $ANTLR end "OCTAL_ESCAPE"



    # $ANTLR start "UNICODE_ESCAPE"
    def mUNICODE_ESCAPE(self, ):
        try:
            # Java.g:1038:5: ( '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT )
            # Java.g:1038:9: '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
            pass 
            self.match(92)

            self.match(117)

            self.mHEX_DIGIT()


            self.mHEX_DIGIT()


            self.mHEX_DIGIT()


            self.mHEX_DIGIT()





        finally:
            pass

    # $ANTLR end "UNICODE_ESCAPE"



    # $ANTLR start "IDENT"
    def mIDENT(self, ):
        try:
            _type = IDENT
            _channel = DEFAULT_CHANNEL

            # Java.g:1041:5: ( JAVA_ID_START ( JAVA_ID_PART )* )
            # Java.g:1041:9: JAVA_ID_START ( JAVA_ID_PART )*
            pass 
            self.mJAVA_ID_START()


            # Java.g:1041:23: ( JAVA_ID_PART )*
            while True: #loop24
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if (LA24_0 == 36 or (48 <= LA24_0 <= 57) or (65 <= LA24_0 <= 90) or LA24_0 == 95 or (97 <= LA24_0 <= 122) or (192 <= LA24_0 <= 214) or (216 <= LA24_0 <= 246) or (248 <= LA24_0 <= 8191) or (12352 <= LA24_0 <= 12687) or (13056 <= LA24_0 <= 13183) or (13312 <= LA24_0 <= 15661) or (19968 <= LA24_0 <= 40959) or (63744 <= LA24_0 <= 64255)) :
                    alt24 = 1


                if alt24 == 1:
                    # Java.g:
                    pass 
                    if self.input.LA(1) == 36 or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122) or (192 <= self.input.LA(1) <= 214) or (216 <= self.input.LA(1) <= 246) or (248 <= self.input.LA(1) <= 8191) or (12352 <= self.input.LA(1) <= 12687) or (13056 <= self.input.LA(1) <= 13183) or (13312 <= self.input.LA(1) <= 15661) or (19968 <= self.input.LA(1) <= 40959) or (63744 <= self.input.LA(1) <= 64255):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop24




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IDENT"



    # $ANTLR start "JAVA_ID_START"
    def mJAVA_ID_START(self, ):
        try:
            # Java.g:1047:5: ( '\\u0024' | '\\u0041' .. '\\u005a' | '\\u005f' | '\\u0061' .. '\\u007a' | '\\u00c0' .. '\\u00d6' | '\\u00d8' .. '\\u00f6' | '\\u00f8' .. '\\u00ff' | '\\u0100' .. '\\u1fff' | '\\u3040' .. '\\u318f' | '\\u3300' .. '\\u337f' | '\\u3400' .. '\\u3d2d' | '\\u4e00' .. '\\u9fff' | '\\uf900' .. '\\ufaff' )
            # Java.g:
            pass 
            if self.input.LA(1) == 36 or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122) or (192 <= self.input.LA(1) <= 214) or (216 <= self.input.LA(1) <= 246) or (248 <= self.input.LA(1) <= 8191) or (12352 <= self.input.LA(1) <= 12687) or (13056 <= self.input.LA(1) <= 13183) or (13312 <= self.input.LA(1) <= 15661) or (19968 <= self.input.LA(1) <= 40959) or (63744 <= self.input.LA(1) <= 64255):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "JAVA_ID_START"



    # $ANTLR start "JAVA_ID_PART"
    def mJAVA_ID_PART(self, ):
        try:
            # Java.g:1064:5: ( JAVA_ID_START | '\\u0030' .. '\\u0039' )
            # Java.g:
            pass 
            if self.input.LA(1) == 36 or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122) or (192 <= self.input.LA(1) <= 214) or (216 <= self.input.LA(1) <= 246) or (248 <= self.input.LA(1) <= 8191) or (12352 <= self.input.LA(1) <= 12687) or (13056 <= self.input.LA(1) <= 13183) or (13312 <= self.input.LA(1) <= 15661) or (19968 <= self.input.LA(1) <= 40959) or (63744 <= self.input.LA(1) <= 64255):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "JAVA_ID_PART"



    # $ANTLR start "WS"
    def mWS(self, ):
        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # Java.g:1067:5: ( ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' ) )
            # Java.g:1067:8: ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' )
            pass 
            if (9 <= self.input.LA(1) <= 10) or (12 <= self.input.LA(1) <= 13) or self.input.LA(1) == 32:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            #action start
                
            _channel = HIDDEN
                
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WS"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):
        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # Java.g:1074:5: ( '/*' ~ ( '*' ) ( options {greedy=false; } : . )* '*/' )
            # Java.g:1074:9: '/*' ~ ( '*' ) ( options {greedy=false; } : . )* '*/'
            pass 
            self.match("/*")


            if (0 <= self.input.LA(1) <= 41) or (43 <= self.input.LA(1) <= 65535):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # Java.g:1074:21: ( options {greedy=false; } : . )*
            while True: #loop25
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if (LA25_0 == 42) :
                    LA25_1 = self.input.LA(2)

                    if (LA25_1 == 47) :
                        alt25 = 2
                    elif ((0 <= LA25_1 <= 46) or (48 <= LA25_1 <= 65535)) :
                        alt25 = 1


                elif ((0 <= LA25_0 <= 41) or (43 <= LA25_0 <= 65535)) :
                    alt25 = 1


                if alt25 == 1:
                    # Java.g:1074:49: .
                    pass 
                    self.matchAny()


                else:
                    break #loop25


            self.match("*/")


            #action start
                
            _channel = HIDDEN
                
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "LINE_COMMENT"
    def mLINE_COMMENT(self, ):
        try:
            _type = LINE_COMMENT
            _channel = DEFAULT_CHANNEL

            # Java.g:1081:5: ( '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' )
            # Java.g:1081:7: '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
            pass 
            self.match("//")


            # Java.g:1081:12: (~ ( '\\n' | '\\r' ) )*
            while True: #loop26
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if ((0 <= LA26_0 <= 9) or (11 <= LA26_0 <= 12) or (14 <= LA26_0 <= 65535)) :
                    alt26 = 1


                if alt26 == 1:
                    # Java.g:
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop26


            # Java.g:1081:26: ( '\\r' )?
            alt27 = 2
            LA27_0 = self.input.LA(1)

            if (LA27_0 == 13) :
                alt27 = 1
            if alt27 == 1:
                # Java.g:1081:26: '\\r'
                pass 
                self.match(13)




            self.match(10)

            #action start
                
            _channel = HIDDEN
                
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LINE_COMMENT"



    # $ANTLR start "JAVADOC_COMMENT"
    def mJAVADOC_COMMENT(self, ):
        try:
            _type = JAVADOC_COMMENT
            _channel = DEFAULT_CHANNEL

            # Java.g:1088:5: ( '/**' ( options {greedy=false; } : . )* '*/' )
            # Java.g:1088:9: '/**' ( options {greedy=false; } : . )* '*/'
            pass 
            self.match("/**")


            # Java.g:1088:15: ( options {greedy=false; } : . )*
            while True: #loop28
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if (LA28_0 == 42) :
                    LA28_1 = self.input.LA(2)

                    if (LA28_1 == 47) :
                        alt28 = 2
                    elif ((0 <= LA28_1 <= 46) or (48 <= LA28_1 <= 65535)) :
                        alt28 = 1


                elif ((0 <= LA28_0 <= 41) or (43 <= LA28_0 <= 65535)) :
                    alt28 = 1


                if alt28 == 1:
                    # Java.g:1088:43: .
                    pass 
                    self.matchAny()


                else:
                    break #loop28


            self.match("*/")


            #action start
                
            _channel = HIDDEN
                
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "JAVADOC_COMMENT"



    def mTokens(self):
        # Java.g:1:8: ( ABSTRACT | AND | AND_ASSIGN | ASSERT | ASSIGN | AT | BIT_SHIFT_RIGHT | BIT_SHIFT_RIGHT_ASSIGN | BOOLEAN | BREAK | BYTE | CASE | CATCH | CHAR | CLASS | COLON | COMMA | CONTINUE | DEC | DEFAULT | DIV | DIV_ASSIGN | DO | DOT | DOTSTAR | DOUBLE | ELLIPSIS | ELSE | ENUM | EQUAL | EXTENDS | FALSE | FINAL | FINALLY | FLOAT | FOR | GREATER_OR_EQUAL | GREATER_THAN | IF | IMPLEMENTS | IMPORT | INC | INSTANCEOF | INT | INTERFACE | LBRACK | LCURLY | LESS_OR_EQUAL | LESS_THAN | LOGICAL_AND | LOGICAL_NOT | LOGICAL_OR | LONG | LPAREN | MINUS | MINUS_ASSIGN | MOD | MOD_ASSIGN | NATIVE | NEW | NOT | NOT_EQUAL | NULL | OR | OR_ASSIGN | PACKAGE | PLUS | PLUS_ASSIGN | PRIVATE | PROTECTED | PUBLIC | QUESTION | RBRACK | RCURLY | RETURN | RPAREN | SEMI | SHIFT_LEFT | SHIFT_LEFT_ASSIGN | SHIFT_RIGHT | SHIFT_RIGHT_ASSIGN | SHORT | STAR | STAR_ASSIGN | STATIC | STRICTFP | SUPER | SWITCH | SYNCHRONIZED | THIS | THROW | THROWS | TRANSIENT | TRUE | TRY | VOID | VOLATILE | WHILE | XOR | XOR_ASSIGN | HEX_LITERAL | DECIMAL_LITERAL | OCTAL_LITERAL | FLOATING_POINT_LITERAL | CHARACTER_LITERAL | STRING_LITERAL | IDENT | WS | COMMENT | LINE_COMMENT | JAVADOC_COMMENT )
        alt29 = 111
        alt29 = self.dfa29.predict(self.input)
        if alt29 == 1:
            # Java.g:1:10: ABSTRACT
            pass 
            self.mABSTRACT()



        elif alt29 == 2:
            # Java.g:1:19: AND
            pass 
            self.mAND()



        elif alt29 == 3:
            # Java.g:1:23: AND_ASSIGN
            pass 
            self.mAND_ASSIGN()



        elif alt29 == 4:
            # Java.g:1:34: ASSERT
            pass 
            self.mASSERT()



        elif alt29 == 5:
            # Java.g:1:41: ASSIGN
            pass 
            self.mASSIGN()



        elif alt29 == 6:
            # Java.g:1:48: AT
            pass 
            self.mAT()



        elif alt29 == 7:
            # Java.g:1:51: BIT_SHIFT_RIGHT
            pass 
            self.mBIT_SHIFT_RIGHT()



        elif alt29 == 8:
            # Java.g:1:67: BIT_SHIFT_RIGHT_ASSIGN
            pass 
            self.mBIT_SHIFT_RIGHT_ASSIGN()



        elif alt29 == 9:
            # Java.g:1:90: BOOLEAN
            pass 
            self.mBOOLEAN()



        elif alt29 == 10:
            # Java.g:1:98: BREAK
            pass 
            self.mBREAK()



        elif alt29 == 11:
            # Java.g:1:104: BYTE
            pass 
            self.mBYTE()



        elif alt29 == 12:
            # Java.g:1:109: CASE
            pass 
            self.mCASE()



        elif alt29 == 13:
            # Java.g:1:114: CATCH
            pass 
            self.mCATCH()



        elif alt29 == 14:
            # Java.g:1:120: CHAR
            pass 
            self.mCHAR()



        elif alt29 == 15:
            # Java.g:1:125: CLASS
            pass 
            self.mCLASS()



        elif alt29 == 16:
            # Java.g:1:131: COLON
            pass 
            self.mCOLON()



        elif alt29 == 17:
            # Java.g:1:137: COMMA
            pass 
            self.mCOMMA()



        elif alt29 == 18:
            # Java.g:1:143: CONTINUE
            pass 
            self.mCONTINUE()



        elif alt29 == 19:
            # Java.g:1:152: DEC
            pass 
            self.mDEC()



        elif alt29 == 20:
            # Java.g:1:156: DEFAULT
            pass 
            self.mDEFAULT()



        elif alt29 == 21:
            # Java.g:1:164: DIV
            pass 
            self.mDIV()



        elif alt29 == 22:
            # Java.g:1:168: DIV_ASSIGN
            pass 
            self.mDIV_ASSIGN()



        elif alt29 == 23:
            # Java.g:1:179: DO
            pass 
            self.mDO()



        elif alt29 == 24:
            # Java.g:1:182: DOT
            pass 
            self.mDOT()



        elif alt29 == 25:
            # Java.g:1:186: DOTSTAR
            pass 
            self.mDOTSTAR()



        elif alt29 == 26:
            # Java.g:1:194: DOUBLE
            pass 
            self.mDOUBLE()



        elif alt29 == 27:
            # Java.g:1:201: ELLIPSIS
            pass 
            self.mELLIPSIS()



        elif alt29 == 28:
            # Java.g:1:210: ELSE
            pass 
            self.mELSE()



        elif alt29 == 29:
            # Java.g:1:215: ENUM
            pass 
            self.mENUM()



        elif alt29 == 30:
            # Java.g:1:220: EQUAL
            pass 
            self.mEQUAL()



        elif alt29 == 31:
            # Java.g:1:226: EXTENDS
            pass 
            self.mEXTENDS()



        elif alt29 == 32:
            # Java.g:1:234: FALSE
            pass 
            self.mFALSE()



        elif alt29 == 33:
            # Java.g:1:240: FINAL
            pass 
            self.mFINAL()



        elif alt29 == 34:
            # Java.g:1:246: FINALLY
            pass 
            self.mFINALLY()



        elif alt29 == 35:
            # Java.g:1:254: FLOAT
            pass 
            self.mFLOAT()



        elif alt29 == 36:
            # Java.g:1:260: FOR
            pass 
            self.mFOR()



        elif alt29 == 37:
            # Java.g:1:264: GREATER_OR_EQUAL
            pass 
            self.mGREATER_OR_EQUAL()



        elif alt29 == 38:
            # Java.g:1:281: GREATER_THAN
            pass 
            self.mGREATER_THAN()



        elif alt29 == 39:
            # Java.g:1:294: IF
            pass 
            self.mIF()



        elif alt29 == 40:
            # Java.g:1:297: IMPLEMENTS
            pass 
            self.mIMPLEMENTS()



        elif alt29 == 41:
            # Java.g:1:308: IMPORT
            pass 
            self.mIMPORT()



        elif alt29 == 42:
            # Java.g:1:315: INC
            pass 
            self.mINC()



        elif alt29 == 43:
            # Java.g:1:319: INSTANCEOF
            pass 
            self.mINSTANCEOF()



        elif alt29 == 44:
            # Java.g:1:330: INT
            pass 
            self.mINT()



        elif alt29 == 45:
            # Java.g:1:334: INTERFACE
            pass 
            self.mINTERFACE()



        elif alt29 == 46:
            # Java.g:1:344: LBRACK
            pass 
            self.mLBRACK()



        elif alt29 == 47:
            # Java.g:1:351: LCURLY
            pass 
            self.mLCURLY()



        elif alt29 == 48:
            # Java.g:1:358: LESS_OR_EQUAL
            pass 
            self.mLESS_OR_EQUAL()



        elif alt29 == 49:
            # Java.g:1:372: LESS_THAN
            pass 
            self.mLESS_THAN()



        elif alt29 == 50:
            # Java.g:1:382: LOGICAL_AND
            pass 
            self.mLOGICAL_AND()



        elif alt29 == 51:
            # Java.g:1:394: LOGICAL_NOT
            pass 
            self.mLOGICAL_NOT()



        elif alt29 == 52:
            # Java.g:1:406: LOGICAL_OR
            pass 
            self.mLOGICAL_OR()



        elif alt29 == 53:
            # Java.g:1:417: LONG
            pass 
            self.mLONG()



        elif alt29 == 54:
            # Java.g:1:422: LPAREN
            pass 
            self.mLPAREN()



        elif alt29 == 55:
            # Java.g:1:429: MINUS
            pass 
            self.mMINUS()



        elif alt29 == 56:
            # Java.g:1:435: MINUS_ASSIGN
            pass 
            self.mMINUS_ASSIGN()



        elif alt29 == 57:
            # Java.g:1:448: MOD
            pass 
            self.mMOD()



        elif alt29 == 58:
            # Java.g:1:452: MOD_ASSIGN
            pass 
            self.mMOD_ASSIGN()



        elif alt29 == 59:
            # Java.g:1:463: NATIVE
            pass 
            self.mNATIVE()



        elif alt29 == 60:
            # Java.g:1:470: NEW
            pass 
            self.mNEW()



        elif alt29 == 61:
            # Java.g:1:474: NOT
            pass 
            self.mNOT()



        elif alt29 == 62:
            # Java.g:1:478: NOT_EQUAL
            pass 
            self.mNOT_EQUAL()



        elif alt29 == 63:
            # Java.g:1:488: NULL
            pass 
            self.mNULL()



        elif alt29 == 64:
            # Java.g:1:493: OR
            pass 
            self.mOR()



        elif alt29 == 65:
            # Java.g:1:496: OR_ASSIGN
            pass 
            self.mOR_ASSIGN()



        elif alt29 == 66:
            # Java.g:1:506: PACKAGE
            pass 
            self.mPACKAGE()



        elif alt29 == 67:
            # Java.g:1:514: PLUS
            pass 
            self.mPLUS()



        elif alt29 == 68:
            # Java.g:1:519: PLUS_ASSIGN
            pass 
            self.mPLUS_ASSIGN()



        elif alt29 == 69:
            # Java.g:1:531: PRIVATE
            pass 
            self.mPRIVATE()



        elif alt29 == 70:
            # Java.g:1:539: PROTECTED
            pass 
            self.mPROTECTED()



        elif alt29 == 71:
            # Java.g:1:549: PUBLIC
            pass 
            self.mPUBLIC()



        elif alt29 == 72:
            # Java.g:1:556: QUESTION
            pass 
            self.mQUESTION()



        elif alt29 == 73:
            # Java.g:1:565: RBRACK
            pass 
            self.mRBRACK()



        elif alt29 == 74:
            # Java.g:1:572: RCURLY
            pass 
            self.mRCURLY()



        elif alt29 == 75:
            # Java.g:1:579: RETURN
            pass 
            self.mRETURN()



        elif alt29 == 76:
            # Java.g:1:586: RPAREN
            pass 
            self.mRPAREN()



        elif alt29 == 77:
            # Java.g:1:593: SEMI
            pass 
            self.mSEMI()



        elif alt29 == 78:
            # Java.g:1:598: SHIFT_LEFT
            pass 
            self.mSHIFT_LEFT()



        elif alt29 == 79:
            # Java.g:1:609: SHIFT_LEFT_ASSIGN
            pass 
            self.mSHIFT_LEFT_ASSIGN()



        elif alt29 == 80:
            # Java.g:1:627: SHIFT_RIGHT
            pass 
            self.mSHIFT_RIGHT()



        elif alt29 == 81:
            # Java.g:1:639: SHIFT_RIGHT_ASSIGN
            pass 
            self.mSHIFT_RIGHT_ASSIGN()



        elif alt29 == 82:
            # Java.g:1:658: SHORT
            pass 
            self.mSHORT()



        elif alt29 == 83:
            # Java.g:1:664: STAR
            pass 
            self.mSTAR()



        elif alt29 == 84:
            # Java.g:1:669: STAR_ASSIGN
            pass 
            self.mSTAR_ASSIGN()



        elif alt29 == 85:
            # Java.g:1:681: STATIC
            pass 
            self.mSTATIC()



        elif alt29 == 86:
            # Java.g:1:688: STRICTFP
            pass 
            self.mSTRICTFP()



        elif alt29 == 87:
            # Java.g:1:697: SUPER
            pass 
            self.mSUPER()



        elif alt29 == 88:
            # Java.g:1:703: SWITCH
            pass 
            self.mSWITCH()



        elif alt29 == 89:
            # Java.g:1:710: SYNCHRONIZED
            pass 
            self.mSYNCHRONIZED()



        elif alt29 == 90:
            # Java.g:1:723: THIS
            pass 
            self.mTHIS()



        elif alt29 == 91:
            # Java.g:1:728: THROW
            pass 
            self.mTHROW()



        elif alt29 == 92:
            # Java.g:1:734: THROWS
            pass 
            self.mTHROWS()



        elif alt29 == 93:
            # Java.g:1:741: TRANSIENT
            pass 
            self.mTRANSIENT()



        elif alt29 == 94:
            # Java.g:1:751: TRUE
            pass 
            self.mTRUE()



        elif alt29 == 95:
            # Java.g:1:756: TRY
            pass 
            self.mTRY()



        elif alt29 == 96:
            # Java.g:1:760: VOID
            pass 
            self.mVOID()



        elif alt29 == 97:
            # Java.g:1:765: VOLATILE
            pass 
            self.mVOLATILE()



        elif alt29 == 98:
            # Java.g:1:774: WHILE
            pass 
            self.mWHILE()



        elif alt29 == 99:
            # Java.g:1:780: XOR
            pass 
            self.mXOR()



        elif alt29 == 100:
            # Java.g:1:784: XOR_ASSIGN
            pass 
            self.mXOR_ASSIGN()



        elif alt29 == 101:
            # Java.g:1:795: HEX_LITERAL
            pass 
            self.mHEX_LITERAL()



        elif alt29 == 102:
            # Java.g:1:807: DECIMAL_LITERAL
            pass 
            self.mDECIMAL_LITERAL()



        elif alt29 == 103:
            # Java.g:1:823: OCTAL_LITERAL
            pass 
            self.mOCTAL_LITERAL()



        elif alt29 == 104:
            # Java.g:1:837: FLOATING_POINT_LITERAL
            pass 
            self.mFLOATING_POINT_LITERAL()



        elif alt29 == 105:
            # Java.g:1:860: CHARACTER_LITERAL
            pass 
            self.mCHARACTER_LITERAL()



        elif alt29 == 106:
            # Java.g:1:878: STRING_LITERAL
            pass 
            self.mSTRING_LITERAL()



        elif alt29 == 107:
            # Java.g:1:893: IDENT
            pass 
            self.mIDENT()



        elif alt29 == 108:
            # Java.g:1:899: WS
            pass 
            self.mWS()



        elif alt29 == 109:
            # Java.g:1:902: COMMENT
            pass 
            self.mCOMMENT()



        elif alt29 == 110:
            # Java.g:1:910: LINE_COMMENT
            pass 
            self.mLINE_COMMENT()



        elif alt29 == 111:
            # Java.g:1:923: JAVADOC_COMMENT
            pass 
            self.mJAVADOC_COMMENT()








    # lookup tables for DFA #29

    DFA29_eot = DFA.unpack(
        "\1\uffff\1\55\1\63\1\65\1\uffff\1\70\2\55\2\uffff\1\102\1\55\1"
        "\110\1\113\3\55\1\131\2\uffff\1\134\1\136\1\141\1\55\1\uffff\1"
        "\144\1\55\1\uffff\1\55\3\uffff\1\55\2\uffff\1\55\1\162\3\55\1\170"
        "\2\172\4\uffff\2\55\5\uffff\1\u0081\2\uffff\7\55\3\uffff\1\55\1"
        "\u008c\10\uffff\7\55\1\u0096\2\55\4\uffff\1\u009b\6\uffff\1\55"
        "\2\uffff\14\55\2\uffff\4\55\4\uffff\1\u00b3\1\172\2\55\1\u00b7"
        "\2\uffff\12\55\3\uffff\6\55\1\u00c8\1\uffff\2\55\1\u00cd\2\uffff"
        "\2\55\1\u00d0\20\55\1\u00e1\3\55\1\uffff\2\55\2\uffff\2\55\1\u00e9"
        "\1\u00ea\1\55\1\u00ec\4\55\1\u00f1\1\u00f2\4\55\1\uffff\4\55\1"
        "\uffff\1\u00fb\1\55\1\uffff\1\u00fd\13\55\1\u0109\2\55\1\u010c"
        "\1\uffff\1\u010d\5\55\1\u0113\2\uffff\1\u0114\1\uffff\1\u0115\3"
        "\55\2\uffff\1\55\1\u011a\1\u011c\1\u011d\4\55\1\uffff\1\55\1\uffff"
        "\5\55\1\u0128\2\55\1\u012b\2\55\1\uffff\1\u012f\1\55\2\uffff\1"
        "\55\1\u0132\1\55\1\u0134\1\55\3\uffff\2\55\1\u0138\1\55\1\uffff"
        "\1\55\2\uffff\1\55\1\u013c\2\55\1\u013f\3\55\1\u0143\1\u0144\1"
        "\uffff\1\u0145\1\55\1\uffff\1\u0147\1\55\1\u0149\1\uffff\2\55\1"
        "\uffff\1\55\1\uffff\1\u014d\1\55\1\u014f\1\uffff\1\u0150\1\u0151"
        "\1\55\1\uffff\2\55\1\uffff\1\u0155\1\u0156\1\55\3\uffff\1\55\1"
        "\uffff\1\55\1\uffff\2\55\1\u015c\1\uffff\1\u015d\3\uffff\3\55\2"
        "\uffff\1\55\1\u0162\2\55\1\u0165\2\uffff\2\55\1\u0168\1\u0169\1"
        "\uffff\1\55\1\u016b\1\uffff\1\u016c\1\u016d\2\uffff\1\55\3\uffff"
        "\1\55\1\u0170\1\uffff"
        )

    DFA29_eof = DFA.unpack(
        "\u0171\uffff"
        )

    DFA29_min = DFA.unpack(
        "\1\11\1\142\1\46\1\75\1\uffff\1\75\1\157\1\141\2\uffff\1\55\1\145"
        "\2\52\1\154\1\141\1\146\1\53\2\uffff\1\74\2\75\1\157\1\uffff\1"
        "\75\1\141\1\uffff\1\141\3\uffff\1\145\2\uffff\1\150\1\75\1\150"
        "\1\157\1\150\1\75\2\56\4\uffff\2\163\5\uffff\1\75\2\uffff\1\157"
        "\1\145\1\164\1\163\2\141\1\156\3\uffff\1\146\1\44\1\uffff\1\0\6"
        "\uffff\1\163\1\165\1\164\1\154\1\156\1\157\1\162\1\44\1\160\1\163"
        "\4\uffff\1\75\6\uffff\1\156\2\uffff\1\164\1\167\1\154\1\143\1\151"
        "\1\142\1\164\1\157\1\141\1\160\1\151\1\156\2\uffff\1\151\1\141"
        "\2\151\4\uffff\2\56\1\164\1\145\1\75\2\uffff\1\154\1\141\2\145"
        "\1\143\1\162\1\163\1\164\1\141\1\142\3\uffff\1\145\1\155\1\145"
        "\1\163\2\141\1\44\1\uffff\1\154\1\164\1\44\2\uffff\1\147\1\151"
        "\1\44\1\154\1\153\1\166\1\164\1\154\1\165\1\162\1\164\1\151\1\145"
        "\1\164\1\143\1\163\1\157\1\156\1\145\1\44\1\144\1\141\1\154\1\uffff"
        "\2\162\2\uffff\1\145\1\153\2\44\1\150\1\44\1\163\1\151\1\165\1"
        "\154\2\44\1\156\1\145\1\154\1\164\1\uffff\1\145\1\162\1\141\1\162"
        "\1\uffff\1\44\1\166\1\uffff\1\44\2\141\1\145\1\151\1\162\1\164"
        "\1\151\1\143\1\162\1\143\1\150\1\44\1\167\1\163\1\44\1\uffff\1"
        "\44\1\164\1\145\1\141\1\164\1\141\1\44\2\uffff\1\44\1\uffff\1\44"
        "\1\156\1\154\1\145\2\uffff\1\144\3\44\1\155\1\164\1\156\1\146\1"
        "\uffff\1\145\1\uffff\1\147\1\164\2\143\1\156\1\44\1\143\1\164\1"
        "\44\1\150\1\162\1\uffff\1\44\1\151\2\uffff\1\151\1\44\1\143\1\44"
        "\1\156\3\uffff\1\165\1\164\1\44\1\163\1\uffff\1\171\2\uffff\1\145"
        "\1\44\1\143\1\141\1\44\2\145\1\164\2\44\1\uffff\1\44\1\146\1\uffff"
        "\1\44\1\157\1\44\1\uffff\1\145\1\154\1\uffff\1\164\1\uffff\1\44"
        "\1\145\1\44\1\uffff\2\44\1\156\1\uffff\1\145\1\143\1\uffff\2\44"
        "\1\145\3\uffff\1\160\1\uffff\1\156\1\uffff\1\156\1\145\1\44\1\uffff"
        "\1\44\3\uffff\1\164\1\157\1\145\2\uffff\1\144\1\44\1\151\1\164"
        "\1\44\2\uffff\1\163\1\146\2\44\1\uffff\1\172\1\44\1\uffff\2\44"
        "\2\uffff\1\145\3\uffff\1\144\1\44\1\uffff"
        )

    DFA29_max = DFA.unpack(
        "\1\ufaff\1\163\2\75\1\uffff\1\76\1\171\1\157\2\uffff\1\75\1\157"
        "\1\75\1\71\1\170\1\157\1\156\1\75\2\uffff\2\75\1\174\1\157\1\uffff"
        "\1\75\1\165\1\uffff\1\165\3\uffff\1\145\2\uffff\1\171\1\75\1\162"
        "\1\157\1\150\1\75\1\170\1\146\4\uffff\2\163\5\uffff\1\76\2\uffff"
        "\1\157\1\145\2\164\2\141\1\156\3\uffff\1\146\1\ufaff\1\uffff\1"
        "\uffff\6\uffff\1\163\1\165\1\164\1\154\1\156\1\157\1\162\1\ufaff"
        "\1\160\1\164\4\uffff\1\75\6\uffff\1\156\2\uffff\1\164\1\167\1\154"
        "\1\143\1\157\1\142\1\164\1\157\1\162\1\160\1\151\1\156\2\uffff"
        "\1\162\1\171\1\154\1\151\4\uffff\2\146\1\164\1\145\1\75\2\uffff"
        "\1\154\1\141\2\145\1\143\1\162\1\163\1\164\1\141\1\142\3\uffff"
        "\1\145\1\155\1\145\1\163\2\141\1\ufaff\1\uffff\1\157\1\164\1\ufaff"
        "\2\uffff\1\147\1\151\1\ufaff\1\154\1\153\1\166\1\164\1\154\1\165"
        "\1\162\1\164\1\151\1\145\1\164\1\143\1\163\1\157\1\156\1\145\1"
        "\ufaff\1\144\1\141\1\154\1\uffff\2\162\2\uffff\1\145\1\153\2\ufaff"
        "\1\150\1\ufaff\1\163\1\151\1\165\1\154\2\ufaff\1\156\1\145\1\154"
        "\1\164\1\uffff\1\145\1\162\1\141\1\162\1\uffff\1\ufaff\1\166\1"
        "\uffff\1\ufaff\2\141\1\145\1\151\1\162\1\164\1\151\1\143\1\162"
        "\1\143\1\150\1\ufaff\1\167\1\163\1\ufaff\1\uffff\1\ufaff\1\164"
        "\1\145\1\141\1\164\1\141\1\ufaff\2\uffff\1\ufaff\1\uffff\1\ufaff"
        "\1\156\1\154\1\145\2\uffff\1\144\3\ufaff\1\155\1\164\1\156\1\146"
        "\1\uffff\1\145\1\uffff\1\147\1\164\2\143\1\156\1\ufaff\1\143\1"
        "\164\1\ufaff\1\150\1\162\1\uffff\1\ufaff\1\151\2\uffff\1\151\1"
        "\ufaff\1\143\1\ufaff\1\156\3\uffff\1\165\1\164\1\ufaff\1\163\1"
        "\uffff\1\171\2\uffff\1\145\1\ufaff\1\143\1\141\1\ufaff\2\145\1"
        "\164\2\ufaff\1\uffff\1\ufaff\1\146\1\uffff\1\ufaff\1\157\1\ufaff"
        "\1\uffff\1\145\1\154\1\uffff\1\164\1\uffff\1\ufaff\1\145\1\ufaff"
        "\1\uffff\2\ufaff\1\156\1\uffff\1\145\1\143\1\uffff\2\ufaff\1\145"
        "\3\uffff\1\160\1\uffff\1\156\1\uffff\1\156\1\145\1\ufaff\1\uffff"
        "\1\ufaff\3\uffff\1\164\1\157\1\145\2\uffff\1\144\1\ufaff\1\151"
        "\1\164\1\ufaff\2\uffff\1\163\1\146\2\ufaff\1\uffff\1\172\1\ufaff"
        "\1\uffff\2\ufaff\2\uffff\1\145\3\uffff\1\144\1\ufaff\1\uffff"
        )

    DFA29_accept = DFA.unpack(
        "\4\uffff\1\6\3\uffff\1\20\1\21\10\uffff\1\56\1\57\4\uffff\1\66"
        "\2\uffff\1\75\1\uffff\1\110\1\111\1\112\1\uffff\1\114\1\115\10"
        "\uffff\1\151\1\152\1\153\1\154\2\uffff\1\3\1\62\1\2\1\36\1\5\1"
        "\uffff\1\45\1\46\7\uffff\1\23\1\70\1\67\2\uffff\1\26\1\uffff\1"
        "\156\1\25\1\31\1\33\1\30\1\150\12\uffff\1\52\1\104\1\103\1\60\1"
        "\uffff\1\61\1\76\1\63\1\64\1\101\1\100\1\uffff\1\72\1\71\14\uffff"
        "\1\124\1\123\4\uffff\1\144\1\143\1\145\1\146\5\uffff\1\121\1\120"
        "\12\uffff\1\27\1\155\1\157\7\uffff\1\47\3\uffff\1\117\1\116\27"
        "\uffff\1\147\2\uffff\1\10\1\7\20\uffff\1\44\4\uffff\1\54\2\uffff"
        "\1\74\20\uffff\1\137\7\uffff\1\13\1\14\1\uffff\1\16\4\uffff\1\34"
        "\1\35\10\uffff\1\65\1\uffff\1\77\13\uffff\1\132\2\uffff\1\136\1"
        "\140\5\uffff\1\12\1\15\1\17\4\uffff\1\40\1\uffff\1\41\1\43\12\uffff"
        "\1\122\2\uffff\1\127\3\uffff\1\133\2\uffff\1\142\1\uffff\1\4\3"
        "\uffff\1\32\3\uffff\1\51\2\uffff\1\73\3\uffff\1\107\1\113\1\125"
        "\1\uffff\1\130\1\uffff\1\134\3\uffff\1\11\1\uffff\1\24\1\37\1\42"
        "\3\uffff\1\102\1\105\5\uffff\1\1\1\22\4\uffff\1\126\2\uffff\1\141"
        "\2\uffff\1\55\1\106\1\uffff\1\135\1\50\1\53\2\uffff\1\131"
        )

    DFA29_special = DFA.unpack(
        "\106\uffff\1\0\u012a\uffff"
        )


    DFA29_transition = [
        DFA.unpack("\2\56\1\uffff\2\56\22\uffff\1\56\1\25\1\54\1\uffff\1"
        "\55\1\31\1\2\1\53\1\30\1\41\1\44\1\21\1\11\1\12\1\15\1\14\1\51"
        "\11\52\1\10\1\42\1\24\1\3\1\5\1\35\1\4\32\55\1\22\1\uffff\1\36"
        "\1\50\1\55\1\uffff\1\1\1\6\1\7\1\13\1\16\1\17\2\55\1\20\2\55\1"
        "\27\1\55\1\32\1\55\1\34\1\55\1\40\1\43\1\45\1\55\1\46\1\47\3\55"
        "\1\23\1\26\1\37\1\33\101\uffff\27\55\1\uffff\37\55\1\uffff\u1f08"
        "\55\u1040\uffff\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e"
        "\55\u10d2\uffff\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\57\20\uffff\1\60"),
        DFA.unpack("\1\62\26\uffff\1\61"),
        DFA.unpack("\1\64"),
        DFA.unpack(""),
        DFA.unpack("\1\67\1\66"),
        DFA.unpack("\1\71\2\uffff\1\72\6\uffff\1\73"),
        DFA.unpack("\1\74\6\uffff\1\75\3\uffff\1\76\2\uffff\1\77"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\100\17\uffff\1\101"),
        DFA.unpack("\1\103\11\uffff\1\104"),
        DFA.unpack("\1\106\4\uffff\1\107\15\uffff\1\105"),
        DFA.unpack("\1\111\3\uffff\1\112\1\uffff\12\114"),
        DFA.unpack("\1\115\1\uffff\1\116\11\uffff\1\117"),
        DFA.unpack("\1\120\7\uffff\1\121\2\uffff\1\122\2\uffff\1\123"),
        DFA.unpack("\1\124\6\uffff\1\125\1\126"),
        DFA.unpack("\1\127\21\uffff\1\130"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\133\1\132"),
        DFA.unpack("\1\135"),
        DFA.unpack("\1\140\76\uffff\1\137"),
        DFA.unpack("\1\142"),
        DFA.unpack(""),
        DFA.unpack("\1\143"),
        DFA.unpack("\1\145\3\uffff\1\146\17\uffff\1\147"),
        DFA.unpack(""),
        DFA.unpack("\1\150\20\uffff\1\151\2\uffff\1\152"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\153"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\154\13\uffff\1\155\1\156\1\uffff\1\157\1\uffff\1"
        "\160"),
        DFA.unpack("\1\161"),
        DFA.unpack("\1\163\11\uffff\1\164"),
        DFA.unpack("\1\165"),
        DFA.unpack("\1\166"),
        DFA.unpack("\1\167"),
        DFA.unpack("\1\114\1\uffff\10\173\2\114\12\uffff\3\114\21\uffff"
        "\1\171\13\uffff\3\114\21\uffff\1\171"),
        DFA.unpack("\1\114\1\uffff\12\174\12\uffff\3\114\35\uffff\3\114"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\175"),
        DFA.unpack("\1\176"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0080\1\177"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0082"),
        DFA.unpack("\1\u0083"),
        DFA.unpack("\1\u0084"),
        DFA.unpack("\1\u0085\1\u0086"),
        DFA.unpack("\1\u0087"),
        DFA.unpack("\1\u0088"),
        DFA.unpack("\1\u0089"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u008a"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\24\55\1\u008b\5\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08"
        "\55\u1040\uffff\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e"
        "\55\u10d2\uffff\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack(""),
        DFA.unpack("\52\u008d\1\u008e\uffd5\u008d"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u008f"),
        DFA.unpack("\1\u0090"),
        DFA.unpack("\1\u0091"),
        DFA.unpack("\1\u0092"),
        DFA.unpack("\1\u0093"),
        DFA.unpack("\1\u0094"),
        DFA.unpack("\1\u0095"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\u0097"),
        DFA.unpack("\1\u0098\1\u0099"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u009a"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u009c"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u009d"),
        DFA.unpack("\1\u009e"),
        DFA.unpack("\1\u009f"),
        DFA.unpack("\1\u00a0"),
        DFA.unpack("\1\u00a1\5\uffff\1\u00a2"),
        DFA.unpack("\1\u00a3"),
        DFA.unpack("\1\u00a4"),
        DFA.unpack("\1\u00a5"),
        DFA.unpack("\1\u00a6\20\uffff\1\u00a7"),
        DFA.unpack("\1\u00a8"),
        DFA.unpack("\1\u00a9"),
        DFA.unpack("\1\u00aa"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00ab\10\uffff\1\u00ac"),
        DFA.unpack("\1\u00ad\23\uffff\1\u00ae\3\uffff\1\u00af"),
        DFA.unpack("\1\u00b0\2\uffff\1\u00b1"),
        DFA.unpack("\1\u00b2"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\114\1\uffff\10\173\2\114\12\uffff\3\114\35\uffff"
        "\3\114"),
        DFA.unpack("\1\114\1\uffff\12\174\12\uffff\3\114\35\uffff\3\114"),
        DFA.unpack("\1\u00b4"),
        DFA.unpack("\1\u00b5"),
        DFA.unpack("\1\u00b6"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00b8"),
        DFA.unpack("\1\u00b9"),
        DFA.unpack("\1\u00ba"),
        DFA.unpack("\1\u00bb"),
        DFA.unpack("\1\u00bc"),
        DFA.unpack("\1\u00bd"),
        DFA.unpack("\1\u00be"),
        DFA.unpack("\1\u00bf"),
        DFA.unpack("\1\u00c0"),
        DFA.unpack("\1\u00c1"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00c2"),
        DFA.unpack("\1\u00c3"),
        DFA.unpack("\1\u00c4"),
        DFA.unpack("\1\u00c5"),
        DFA.unpack("\1\u00c6"),
        DFA.unpack("\1\u00c7"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack(""),
        DFA.unpack("\1\u00c9\2\uffff\1\u00ca"),
        DFA.unpack("\1\u00cb"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\4\55\1\u00cc\25\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08"
        "\55\u1040\uffff\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e"
        "\55\u10d2\uffff\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00ce"),
        DFA.unpack("\1\u00cf"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\u00d1"),
        DFA.unpack("\1\u00d2"),
        DFA.unpack("\1\u00d3"),
        DFA.unpack("\1\u00d4"),
        DFA.unpack("\1\u00d5"),
        DFA.unpack("\1\u00d6"),
        DFA.unpack("\1\u00d7"),
        DFA.unpack("\1\u00d8"),
        DFA.unpack("\1\u00d9"),
        DFA.unpack("\1\u00da"),
        DFA.unpack("\1\u00db"),
        DFA.unpack("\1\u00dc"),
        DFA.unpack("\1\u00dd"),
        DFA.unpack("\1\u00de"),
        DFA.unpack("\1\u00df"),
        DFA.unpack("\1\u00e0"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\u00e2"),
        DFA.unpack("\1\u00e3"),
        DFA.unpack("\1\u00e4"),
        DFA.unpack(""),
        DFA.unpack("\1\u00e5"),
        DFA.unpack("\1\u00e6"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00e7"),
        DFA.unpack("\1\u00e8"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\u00eb"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\u00ed"),
        DFA.unpack("\1\u00ee"),
        DFA.unpack("\1\u00ef"),
        DFA.unpack("\1\u00f0"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\u00f3"),
        DFA.unpack("\1\u00f4"),
        DFA.unpack("\1\u00f5"),
        DFA.unpack("\1\u00f6"),
        DFA.unpack(""),
        DFA.unpack("\1\u00f7"),
        DFA.unpack("\1\u00f8"),
        DFA.unpack("\1\u00f9"),
        DFA.unpack("\1\u00fa"),
        DFA.unpack(""),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\u00fc"),
        DFA.unpack(""),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\u00fe"),
        DFA.unpack("\1\u00ff"),
        DFA.unpack("\1\u0100"),
        DFA.unpack("\1\u0101"),
        DFA.unpack("\1\u0102"),
        DFA.unpack("\1\u0103"),
        DFA.unpack("\1\u0104"),
        DFA.unpack("\1\u0105"),
        DFA.unpack("\1\u0106"),
        DFA.unpack("\1\u0107"),
        DFA.unpack("\1\u0108"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\u010a"),
        DFA.unpack("\1\u010b"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack(""),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\u010e"),
        DFA.unpack("\1\u010f"),
        DFA.unpack("\1\u0110"),
        DFA.unpack("\1\u0111"),
        DFA.unpack("\1\u0112"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack(""),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\u0116"),
        DFA.unpack("\1\u0117"),
        DFA.unpack("\1\u0118"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0119"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\13\55\1\u011b\16\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08"
        "\55\u1040\uffff\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e"
        "\55\u10d2\uffff\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\u011e"),
        DFA.unpack("\1\u011f"),
        DFA.unpack("\1\u0120"),
        DFA.unpack("\1\u0121"),
        DFA.unpack(""),
        DFA.unpack("\1\u0122"),
        DFA.unpack(""),
        DFA.unpack("\1\u0123"),
        DFA.unpack("\1\u0124"),
        DFA.unpack("\1\u0125"),
        DFA.unpack("\1\u0126"),
        DFA.unpack("\1\u0127"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\u0129"),
        DFA.unpack("\1\u012a"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\u012c"),
        DFA.unpack("\1\u012d"),
        DFA.unpack(""),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\22\55\1\u012e\7\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08"
        "\55\u1040\uffff\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e"
        "\55\u10d2\uffff\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\u0130"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0131"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\u0133"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\u0135"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0136"),
        DFA.unpack("\1\u0137"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\u0139"),
        DFA.unpack(""),
        DFA.unpack("\1\u013a"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u013b"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\u013d"),
        DFA.unpack("\1\u013e"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\u0140"),
        DFA.unpack("\1\u0141"),
        DFA.unpack("\1\u0142"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack(""),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\u0146"),
        DFA.unpack(""),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\u0148"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack(""),
        DFA.unpack("\1\u014a"),
        DFA.unpack("\1\u014b"),
        DFA.unpack(""),
        DFA.unpack("\1\u014c"),
        DFA.unpack(""),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\u014e"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack(""),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\u0152"),
        DFA.unpack(""),
        DFA.unpack("\1\u0153"),
        DFA.unpack("\1\u0154"),
        DFA.unpack(""),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\u0157"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0158"),
        DFA.unpack(""),
        DFA.unpack("\1\u0159"),
        DFA.unpack(""),
        DFA.unpack("\1\u015a"),
        DFA.unpack("\1\u015b"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack(""),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u015e"),
        DFA.unpack("\1\u015f"),
        DFA.unpack("\1\u0160"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0161"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\u0163"),
        DFA.unpack("\1\u0164"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0166"),
        DFA.unpack("\1\u0167"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack(""),
        DFA.unpack("\1\u016a"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack(""),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u016e"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u016f"),
        DFA.unpack("\1\55\13\uffff\12\55\7\uffff\32\55\4\uffff\1\55\1\uffff"
        "\32\55\105\uffff\27\55\1\uffff\37\55\1\uffff\u1f08\55\u1040\uffff"
        "\u0150\55\u0170\uffff\u0080\55\u0080\uffff\u092e\55\u10d2\uffff"
        "\u5200\55\u5900\uffff\u0200\55"),
        DFA.unpack("")
    ]

    # class definition for DFA #29

    class DFA29(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA29_70 = input.LA(1)

                s = -1
                if ((0 <= LA29_70 <= 41) or (43 <= LA29_70 <= 65535)):
                    s = 141

                elif (LA29_70 == 42):
                    s = 142

                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 29, _s, input)
            self_.error(nvae)
            raise nvae

 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(JavaLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
