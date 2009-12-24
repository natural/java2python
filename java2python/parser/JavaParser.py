# $ANTLR 3.1.1 Java.g 2009-12-23 14:35:12

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *

         
# placeholder




# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
PACKAGE=84
EXPONENT=173
STAR=49
WHILE=103
MOD=32
MOD_ASSIGN=33
CASE=58
CHAR=60
NEW=82
DO=64
GENERIC_TYPE_PARAM_LIST=138
CLASS_INSTANCE_INITIALIZER=121
ARRAY_ELEMENT_ACCESS=115
FOR_CONDITION=129
NOT=34
VAR_DECLARATION=160
ANNOTATION_METHOD_DECL=109
EOF=-1
DIV_ASSIGN=14
LOGICAL_AND=26
BREAK=56
UNARY_PLUS=159
BIT_SHIFT_RIGHT_ASSIGN=9
TYPE=157
RPAREN=43
INC=21
FINAL=70
IMPORT=78
STRING_LITERAL=170
FOR_UPDATE=132
FLOATING_POINT_LITERAL=168
CAST_EXPR=118
NOT_EQUAL=35
VOID_METHOD_DECL=163
THIS=95
RETURN=88
DOUBLE=65
ENUM_TOP_LEVEL_SCOPE=125
VOID=101
SUPER=92
COMMENT=181
ANNOTATION_INIT_KEY_LIST=107
JAVA_ID_START=178
FLOAT_TYPE_SUFFIX=174
PRE_DEC=149
RBRACK=41
IMPLEMENTS_CLAUSE=140
SWITCH_BLOCK_LABEL_LIST=154
LINE_COMMENT=182
PRIVATE=85
STATIC=90
BLOCK_SCOPE=117
ANNOTATION_INIT_DEFAULT_KEY=106
SWITCH=93
NULL=83
VAR_DECLARATOR=161
MINUS_ASSIGN=31
ELSE=66
STRICTFP=91
CHARACTER_LITERAL=169
PRE_INC=150
ANNOTATION_LIST=108
ELLIPSIS=17
NATIVE=81
OCTAL_ESCAPE=177
UNARY_MINUS=158
THROWS=97
LCURLY=23
INT=79
FORMAL_PARAM_VARARG_DECL=135
METHOD_CALL=144
ASSERT=54
TRY=100
INTERFACE_TOP_LEVEL_SCOPE=139
SHIFT_LEFT=45
WS=180
SHIFT_RIGHT=47
FORMAL_PARAM_STD_DECL=134
LOCAL_MODIFIER_LIST=142
OR=36
LESS_THAN=25
SHIFT_RIGHT_ASSIGN=48
EXTENDS_BOUND_LIST=127
JAVA_SOURCE=143
CATCH=59
FALSE=69
INTEGER_TYPE_SUFFIX=172
DECIMAL_LITERAL=167
THROW=96
FOR_INIT=131
DEC=12
PROTECTED=86
CLASS=61
LBRACK=22
BIT_SHIFT_RIGHT=8
THROWS_CLAUSE=156
GREATER_OR_EQUAL=19
FOR=73
THIS_CONSTRUCTOR_CALL=155
LOGICAL_NOT=27
FLOAT=72
ABSTRACT=53
AND=4
POST_DEC=147
AND_ASSIGN=5
STATIC_ARRAY_CREATOR=152
MODIFIER_LIST=145
ANNOTATION_SCOPE=110
LPAREN=29
IF=74
AT=7
ESCAPE_SEQUENCE=175
CONSTRUCTOR_DECL=124
LABELED_STATEMENT=141
UNICODE_ESCAPE=176
EXPR=126
SYNCHRONIZED=94
BOOLEAN=55
CLASS_TOP_LEVEL_SCOPE=123
IMPLEMENTS=75
CONTINUE=62
COMMA=11
TRANSIENT=98
EQUAL=18
XOR_ASSIGN=52
LOGICAL_OR=28
IDENT=164
QUALIFIED_TYPE_IDENT=151
ARGUMENT_LIST=112
PLUS=38
HEX_LITERAL=165
ANNOTATION_INIT_BLOCK=105
DOT=15
SHIFT_LEFT_ASSIGN=46
FORMAL_PARAM_LIST=133
GENERIC_TYPE_ARG_LIST=137
ANNOTATION_TOP_LEVEL_SCOPE=111
DOTSTAR=16
BYTE=57
XOR=51
JAVA_ID_PART=179
GREATER_THAN=20
VOLATILE=102
PARENTESIZED_EXPR=146
CLASS_STATIC_INITIALIZER=122
ARRAY_DECLARATOR_LIST=114
LESS_OR_EQUAL=24
DEFAULT=63
OCTAL_LITERAL=166
HEX_DIGIT=171
SHORT=89
INSTANCEOF=76
MINUS=30
EXTENDS_CLAUSE=128
TRUE=99
SEMI=44
STAR_ASSIGN=50
VAR_DECLARATOR_LIST=162
ARRAY_DECLARATOR=113
COLON=10
OR_ASSIGN=37
ENUM=67
QUESTION=40
FINALLY=71
RCURLY=42
PLUS_ASSIGN=39
ASSIGN=6
ANNOTATION_INIT_ARRAY_ELEMENT=104
FUNCTION_METHOD_DECL=136
INTERFACE=77
POST_INC=148
DIV=13
CLASS_CONSTRUCTOR_CALL=120
LONG=80
FOR_EACH=130
EXTENDS=68
PUBLIC=87
ARRAY_INITIALIZER=116
CATCH_CLAUSE_LIST=119
SUPER_CONSTRUCTOR_CALL=153

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "AND", "AND_ASSIGN", "ASSIGN", "AT", "BIT_SHIFT_RIGHT", "BIT_SHIFT_RIGHT_ASSIGN", 
    "COLON", "COMMA", "DEC", "DIV", "DIV_ASSIGN", "DOT", "DOTSTAR", "ELLIPSIS", 
    "EQUAL", "GREATER_OR_EQUAL", "GREATER_THAN", "INC", "LBRACK", "LCURLY", 
    "LESS_OR_EQUAL", "LESS_THAN", "LOGICAL_AND", "LOGICAL_NOT", "LOGICAL_OR", 
    "LPAREN", "MINUS", "MINUS_ASSIGN", "MOD", "MOD_ASSIGN", "NOT", "NOT_EQUAL", 
    "OR", "OR_ASSIGN", "PLUS", "PLUS_ASSIGN", "QUESTION", "RBRACK", "RCURLY", 
    "RPAREN", "SEMI", "SHIFT_LEFT", "SHIFT_LEFT_ASSIGN", "SHIFT_RIGHT", 
    "SHIFT_RIGHT_ASSIGN", "STAR", "STAR_ASSIGN", "XOR", "XOR_ASSIGN", "ABSTRACT", 
    "ASSERT", "BOOLEAN", "BREAK", "BYTE", "CASE", "CATCH", "CHAR", "CLASS", 
    "CONTINUE", "DEFAULT", "DO", "DOUBLE", "ELSE", "ENUM", "EXTENDS", "FALSE", 
    "FINAL", "FINALLY", "FLOAT", "FOR", "IF", "IMPLEMENTS", "INSTANCEOF", 
    "INTERFACE", "IMPORT", "INT", "LONG", "NATIVE", "NEW", "NULL", "PACKAGE", 
    "PRIVATE", "PROTECTED", "PUBLIC", "RETURN", "SHORT", "STATIC", "STRICTFP", 
    "SUPER", "SWITCH", "SYNCHRONIZED", "THIS", "THROW", "THROWS", "TRANSIENT", 
    "TRUE", "TRY", "VOID", "VOLATILE", "WHILE", "ANNOTATION_INIT_ARRAY_ELEMENT", 
    "ANNOTATION_INIT_BLOCK", "ANNOTATION_INIT_DEFAULT_KEY", "ANNOTATION_INIT_KEY_LIST", 
    "ANNOTATION_LIST", "ANNOTATION_METHOD_DECL", "ANNOTATION_SCOPE", "ANNOTATION_TOP_LEVEL_SCOPE", 
    "ARGUMENT_LIST", "ARRAY_DECLARATOR", "ARRAY_DECLARATOR_LIST", "ARRAY_ELEMENT_ACCESS", 
    "ARRAY_INITIALIZER", "BLOCK_SCOPE", "CAST_EXPR", "CATCH_CLAUSE_LIST", 
    "CLASS_CONSTRUCTOR_CALL", "CLASS_INSTANCE_INITIALIZER", "CLASS_STATIC_INITIALIZER", 
    "CLASS_TOP_LEVEL_SCOPE", "CONSTRUCTOR_DECL", "ENUM_TOP_LEVEL_SCOPE", 
    "EXPR", "EXTENDS_BOUND_LIST", "EXTENDS_CLAUSE", "FOR_CONDITION", "FOR_EACH", 
    "FOR_INIT", "FOR_UPDATE", "FORMAL_PARAM_LIST", "FORMAL_PARAM_STD_DECL", 
    "FORMAL_PARAM_VARARG_DECL", "FUNCTION_METHOD_DECL", "GENERIC_TYPE_ARG_LIST", 
    "GENERIC_TYPE_PARAM_LIST", "INTERFACE_TOP_LEVEL_SCOPE", "IMPLEMENTS_CLAUSE", 
    "LABELED_STATEMENT", "LOCAL_MODIFIER_LIST", "JAVA_SOURCE", "METHOD_CALL", 
    "MODIFIER_LIST", "PARENTESIZED_EXPR", "POST_DEC", "POST_INC", "PRE_DEC", 
    "PRE_INC", "QUALIFIED_TYPE_IDENT", "STATIC_ARRAY_CREATOR", "SUPER_CONSTRUCTOR_CALL", 
    "SWITCH_BLOCK_LABEL_LIST", "THIS_CONSTRUCTOR_CALL", "THROWS_CLAUSE", 
    "TYPE", "UNARY_MINUS", "UNARY_PLUS", "VAR_DECLARATION", "VAR_DECLARATOR", 
    "VAR_DECLARATOR_LIST", "VOID_METHOD_DECL", "IDENT", "HEX_LITERAL", "OCTAL_LITERAL", 
    "DECIMAL_LITERAL", "FLOATING_POINT_LITERAL", "CHARACTER_LITERAL", "STRING_LITERAL", 
    "HEX_DIGIT", "INTEGER_TYPE_SUFFIX", "EXPONENT", "FLOAT_TYPE_SUFFIX", 
    "ESCAPE_SEQUENCE", "UNICODE_ESCAPE", "OCTAL_ESCAPE", "JAVA_ID_START", 
    "JAVA_ID_PART", "WS", "COMMENT", "LINE_COMMENT"
]




class JavaParser(Parser):
    grammarFileName = "Java.g"
    antlr_version = version_str_to_tuple("3.1.1")
    antlr_version_str = "3.1.1"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        Parser.__init__(self, input, state)

        self._state.ruleMemo = {}

        self.dfa36 = self.DFA36(
            self, 36,
            eot = self.DFA36_eot,
            eof = self.DFA36_eof,
            min = self.DFA36_min,
            max = self.DFA36_max,
            accept = self.DFA36_accept,
            special = self.DFA36_special,
            transition = self.DFA36_transition
            )

        self.dfa43 = self.DFA43(
            self, 43,
            eot = self.DFA43_eot,
            eof = self.DFA43_eof,
            min = self.DFA43_min,
            max = self.DFA43_max,
            accept = self.DFA43_accept,
            special = self.DFA43_special,
            transition = self.DFA43_transition
            )

        self.dfa86 = self.DFA86(
            self, 86,
            eot = self.DFA86_eot,
            eof = self.DFA86_eof,
            min = self.DFA86_min,
            max = self.DFA86_max,
            accept = self.DFA86_accept,
            special = self.DFA86_special,
            transition = self.DFA86_transition
            )

        self.dfa88 = self.DFA88(
            self, 88,
            eot = self.DFA88_eot,
            eof = self.DFA88_eof,
            min = self.DFA88_min,
            max = self.DFA88_max,
            accept = self.DFA88_accept,
            special = self.DFA88_special,
            transition = self.DFA88_transition
            )

        self.dfa97 = self.DFA97(
            self, 97,
            eot = self.DFA97_eot,
            eof = self.DFA97_eof,
            min = self.DFA97_min,
            max = self.DFA97_max,
            accept = self.DFA97_accept,
            special = self.DFA97_special,
            transition = self.DFA97_transition
            )

        self.dfa91 = self.DFA91(
            self, 91,
            eot = self.DFA91_eot,
            eof = self.DFA91_eof,
            min = self.DFA91_min,
            max = self.DFA91_max,
            accept = self.DFA91_accept,
            special = self.DFA91_special,
            transition = self.DFA91_transition
            )

        self.dfa103 = self.DFA103(
            self, 103,
            eot = self.DFA103_eot,
            eof = self.DFA103_eof,
            min = self.DFA103_min,
            max = self.DFA103_max,
            accept = self.DFA103_accept,
            special = self.DFA103_special,
            transition = self.DFA103_transition
            )

        self.dfa127 = self.DFA127(
            self, 127,
            eot = self.DFA127_eot,
            eof = self.DFA127_eof,
            min = self.DFA127_min,
            max = self.DFA127_max,
            accept = self.DFA127_accept,
            special = self.DFA127_special,
            transition = self.DFA127_transition
            )

        self.dfa139 = self.DFA139(
            self, 139,
            eot = self.DFA139_eot,
            eof = self.DFA139_eof,
            min = self.DFA139_min,
            max = self.DFA139_max,
            accept = self.DFA139_accept,
            special = self.DFA139_special,
            transition = self.DFA139_transition
            )

        self.dfa143 = self.DFA143(
            self, 143,
            eot = self.DFA143_eot,
            eof = self.DFA143_eof,
            min = self.DFA143_min,
            max = self.DFA143_max,
            accept = self.DFA143_accept,
            special = self.DFA143_special,
            transition = self.DFA143_transition
            )

        self.dfa150 = self.DFA150(
            self, 150,
            eot = self.DFA150_eot,
            eof = self.DFA150_eof,
            min = self.DFA150_min,
            max = self.DFA150_max,
            accept = self.DFA150_accept,
            special = self.DFA150_special,
            transition = self.DFA150_transition
            )






                
        self._adaptor = CommonTreeAdaptor()


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)

              
    @staticmethod
    def tokenMap():
        src = globals().items()
        return dict([(v, k) for k, v in src if isinstance(v, int)])


    class javaSource_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "javaSource"
    # Java.g:260:1: javaSource : compilationUnit -> ^( JAVA_SOURCE compilationUnit ) ;
    def javaSource(self, ):

        retval = self.javaSource_return()
        retval.start = self.input.LT(1)
        javaSource_StartIndex = self.input.index()
        root_0 = None

        compilationUnit1 = None


        stream_compilationUnit = RewriteRuleSubtreeStream(self._adaptor, "rule compilationUnit")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 1):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:261:5: ( compilationUnit -> ^( JAVA_SOURCE compilationUnit ) )
                # Java.g:261:9: compilationUnit
                pass 
                self._state.following.append(self.FOLLOW_compilationUnit_in_javaSource4499)
                compilationUnit1 = self.compilationUnit()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_compilationUnit.add(compilationUnit1.tree)

                # AST Rewrite
                # elements: compilationUnit
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 262:9: -> ^( JAVA_SOURCE compilationUnit )
                    # Java.g:262:13: ^( JAVA_SOURCE compilationUnit )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(JAVA_SOURCE, "JAVA_SOURCE"), root_1)

                    self._adaptor.addChild(root_1, stream_compilationUnit.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 1, javaSource_StartIndex, success)

            pass

        return retval

    # $ANTLR end "javaSource"

    class compilationUnit_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "compilationUnit"
    # Java.g:265:1: compilationUnit : annotationList ( packageDeclaration )? ( importDeclaration )* ( typeDecls )* ;
    def compilationUnit(self, ):

        retval = self.compilationUnit_return()
        retval.start = self.input.LT(1)
        compilationUnit_StartIndex = self.input.index()
        root_0 = None

        annotationList2 = None

        packageDeclaration3 = None

        importDeclaration4 = None

        typeDecls5 = None



        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 2):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:266:5: ( annotationList ( packageDeclaration )? ( importDeclaration )* ( typeDecls )* )
                # Java.g:266:9: annotationList ( packageDeclaration )? ( importDeclaration )* ( typeDecls )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_annotationList_in_compilationUnit4535)
                annotationList2 = self.annotationList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, annotationList2.tree)
                # Java.g:267:9: ( packageDeclaration )?
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == PACKAGE) :
                    alt1 = 1
                if alt1 == 1:
                    # Java.g:0:0: packageDeclaration
                    pass 
                    self._state.following.append(self.FOLLOW_packageDeclaration_in_compilationUnit4545)
                    packageDeclaration3 = self.packageDeclaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, packageDeclaration3.tree)



                # Java.g:268:9: ( importDeclaration )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == IMPORT) :
                        alt2 = 1


                    if alt2 == 1:
                        # Java.g:0:0: importDeclaration
                        pass 
                        self._state.following.append(self.FOLLOW_importDeclaration_in_compilationUnit4556)
                        importDeclaration4 = self.importDeclaration()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, importDeclaration4.tree)


                    else:
                        break #loop2


                # Java.g:269:9: ( typeDecls )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == AT or LA3_0 == LESS_THAN or LA3_0 == SEMI or LA3_0 == ABSTRACT or LA3_0 == BOOLEAN or LA3_0 == BYTE or (CHAR <= LA3_0 <= CLASS) or LA3_0 == DOUBLE or LA3_0 == ENUM or LA3_0 == FINAL or LA3_0 == FLOAT or LA3_0 == INTERFACE or (INT <= LA3_0 <= NATIVE) or (PRIVATE <= LA3_0 <= PUBLIC) or (SHORT <= LA3_0 <= STRICTFP) or LA3_0 == SYNCHRONIZED or LA3_0 == TRANSIENT or (VOID <= LA3_0 <= VOLATILE) or LA3_0 == IDENT) :
                        alt3 = 1


                    if alt3 == 1:
                        # Java.g:0:0: typeDecls
                        pass 
                        self._state.following.append(self.FOLLOW_typeDecls_in_compilationUnit4567)
                        typeDecls5 = self.typeDecls()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, typeDecls5.tree)


                    else:
                        break #loop3





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 2, compilationUnit_StartIndex, success)

            pass

        return retval

    # $ANTLR end "compilationUnit"

    class typeDecls_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "typeDecls"
    # Java.g:272:1: typeDecls : ( typeDeclaration | SEMI );
    def typeDecls(self, ):

        retval = self.typeDecls_return()
        retval.start = self.input.LT(1)
        typeDecls_StartIndex = self.input.index()
        root_0 = None

        SEMI7 = None
        typeDeclaration6 = None


        SEMI7_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 3):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:273:5: ( typeDeclaration | SEMI )
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == AT or LA4_0 == LESS_THAN or LA4_0 == ABSTRACT or LA4_0 == BOOLEAN or LA4_0 == BYTE or (CHAR <= LA4_0 <= CLASS) or LA4_0 == DOUBLE or LA4_0 == ENUM or LA4_0 == FINAL or LA4_0 == FLOAT or LA4_0 == INTERFACE or (INT <= LA4_0 <= NATIVE) or (PRIVATE <= LA4_0 <= PUBLIC) or (SHORT <= LA4_0 <= STRICTFP) or LA4_0 == SYNCHRONIZED or LA4_0 == TRANSIENT or (VOID <= LA4_0 <= VOLATILE) or LA4_0 == IDENT) :
                    alt4 = 1
                elif (LA4_0 == SEMI) :
                    alt4 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae

                if alt4 == 1:
                    # Java.g:273:9: typeDeclaration
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_typeDeclaration_in_typeDecls4587)
                    typeDeclaration6 = self.typeDeclaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, typeDeclaration6.tree)


                elif alt4 == 2:
                    # Java.g:274:9: SEMI
                    pass 
                    root_0 = self._adaptor.nil()

                    SEMI7=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_typeDecls4597)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 3, typeDecls_StartIndex, success)

            pass

        return retval

    # $ANTLR end "typeDecls"

    class packageDeclaration_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "packageDeclaration"
    # Java.g:277:1: packageDeclaration : PACKAGE qualifiedIdentifier SEMI ;
    def packageDeclaration(self, ):

        retval = self.packageDeclaration_return()
        retval.start = self.input.LT(1)
        packageDeclaration_StartIndex = self.input.index()
        root_0 = None

        PACKAGE8 = None
        SEMI10 = None
        qualifiedIdentifier9 = None


        PACKAGE8_tree = None
        SEMI10_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 4):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:278:5: ( PACKAGE qualifiedIdentifier SEMI )
                # Java.g:278:9: PACKAGE qualifiedIdentifier SEMI
                pass 
                root_0 = self._adaptor.nil()

                PACKAGE8=self.match(self.input, PACKAGE, self.FOLLOW_PACKAGE_in_packageDeclaration4617)
                if self._state.backtracking == 0:

                    PACKAGE8_tree = self._adaptor.createWithPayload(PACKAGE8)
                    root_0 = self._adaptor.becomeRoot(PACKAGE8_tree, root_0)

                self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_packageDeclaration4620)
                qualifiedIdentifier9 = self.qualifiedIdentifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, qualifiedIdentifier9.tree)
                SEMI10=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_packageDeclaration4622)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 4, packageDeclaration_StartIndex, success)

            pass

        return retval

    # $ANTLR end "packageDeclaration"

    class importDeclaration_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "importDeclaration"
    # Java.g:281:1: importDeclaration : IMPORT ( STATIC )? qualifiedIdentifier ( DOTSTAR )? SEMI ;
    def importDeclaration(self, ):

        retval = self.importDeclaration_return()
        retval.start = self.input.LT(1)
        importDeclaration_StartIndex = self.input.index()
        root_0 = None

        IMPORT11 = None
        STATIC12 = None
        DOTSTAR14 = None
        SEMI15 = None
        qualifiedIdentifier13 = None


        IMPORT11_tree = None
        STATIC12_tree = None
        DOTSTAR14_tree = None
        SEMI15_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 5):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:282:5: ( IMPORT ( STATIC )? qualifiedIdentifier ( DOTSTAR )? SEMI )
                # Java.g:282:9: IMPORT ( STATIC )? qualifiedIdentifier ( DOTSTAR )? SEMI
                pass 
                root_0 = self._adaptor.nil()

                IMPORT11=self.match(self.input, IMPORT, self.FOLLOW_IMPORT_in_importDeclaration4642)
                if self._state.backtracking == 0:

                    IMPORT11_tree = self._adaptor.createWithPayload(IMPORT11)
                    root_0 = self._adaptor.becomeRoot(IMPORT11_tree, root_0)

                # Java.g:282:17: ( STATIC )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == STATIC) :
                    alt5 = 1
                if alt5 == 1:
                    # Java.g:0:0: STATIC
                    pass 
                    STATIC12=self.match(self.input, STATIC, self.FOLLOW_STATIC_in_importDeclaration4645)
                    if self._state.backtracking == 0:

                        STATIC12_tree = self._adaptor.createWithPayload(STATIC12)
                        self._adaptor.addChild(root_0, STATIC12_tree)




                self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_importDeclaration4648)
                qualifiedIdentifier13 = self.qualifiedIdentifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, qualifiedIdentifier13.tree)
                # Java.g:282:45: ( DOTSTAR )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == DOTSTAR) :
                    alt6 = 1
                if alt6 == 1:
                    # Java.g:0:0: DOTSTAR
                    pass 
                    DOTSTAR14=self.match(self.input, DOTSTAR, self.FOLLOW_DOTSTAR_in_importDeclaration4650)
                    if self._state.backtracking == 0:

                        DOTSTAR14_tree = self._adaptor.createWithPayload(DOTSTAR14)
                        self._adaptor.addChild(root_0, DOTSTAR14_tree)




                SEMI15=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_importDeclaration4653)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 5, importDeclaration_StartIndex, success)

            pass

        return retval

    # $ANTLR end "importDeclaration"

    class typeDeclaration_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "typeDeclaration"
    # Java.g:285:1: typeDeclaration : modifierList ( classTypeDeclaration[$modifierList.tree] | interfaceTypeDeclaration[$modifierList.tree] | enumTypeDeclaration[$modifierList.tree] | annotationTypeDeclaration[$modifierList.tree] ) ;
    def typeDeclaration(self, ):

        retval = self.typeDeclaration_return()
        retval.start = self.input.LT(1)
        typeDeclaration_StartIndex = self.input.index()
        root_0 = None

        modifierList16 = None

        classTypeDeclaration17 = None

        interfaceTypeDeclaration18 = None

        enumTypeDeclaration19 = None

        annotationTypeDeclaration20 = None



        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 6):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:286:5: ( modifierList ( classTypeDeclaration[$modifierList.tree] | interfaceTypeDeclaration[$modifierList.tree] | enumTypeDeclaration[$modifierList.tree] | annotationTypeDeclaration[$modifierList.tree] ) )
                # Java.g:286:9: modifierList ( classTypeDeclaration[$modifierList.tree] | interfaceTypeDeclaration[$modifierList.tree] | enumTypeDeclaration[$modifierList.tree] | annotationTypeDeclaration[$modifierList.tree] )
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_modifierList_in_typeDeclaration4673)
                modifierList16 = self.modifierList()

                self._state.following.pop()
                # Java.g:287:9: ( classTypeDeclaration[$modifierList.tree] | interfaceTypeDeclaration[$modifierList.tree] | enumTypeDeclaration[$modifierList.tree] | annotationTypeDeclaration[$modifierList.tree] )
                alt7 = 4
                LA7 = self.input.LA(1)
                if LA7 == CLASS:
                    alt7 = 1
                elif LA7 == INTERFACE:
                    alt7 = 2
                elif LA7 == ENUM:
                    alt7 = 3
                elif LA7 == AT:
                    alt7 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae

                if alt7 == 1:
                    # Java.g:287:13: classTypeDeclaration[$modifierList.tree]
                    pass 
                    self._state.following.append(self.FOLLOW_classTypeDeclaration_in_typeDeclaration4688)
                    classTypeDeclaration17 = self.classTypeDeclaration(modifierList16.tree)

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, classTypeDeclaration17.tree)


                elif alt7 == 2:
                    # Java.g:288:13: interfaceTypeDeclaration[$modifierList.tree]
                    pass 
                    self._state.following.append(self.FOLLOW_interfaceTypeDeclaration_in_typeDeclaration4703)
                    interfaceTypeDeclaration18 = self.interfaceTypeDeclaration(modifierList16.tree)

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, interfaceTypeDeclaration18.tree)


                elif alt7 == 3:
                    # Java.g:289:13: enumTypeDeclaration[$modifierList.tree]
                    pass 
                    self._state.following.append(self.FOLLOW_enumTypeDeclaration_in_typeDeclaration4718)
                    enumTypeDeclaration19 = self.enumTypeDeclaration(modifierList16.tree)

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, enumTypeDeclaration19.tree)


                elif alt7 == 4:
                    # Java.g:290:13: annotationTypeDeclaration[$modifierList.tree]
                    pass 
                    self._state.following.append(self.FOLLOW_annotationTypeDeclaration_in_typeDeclaration4733)
                    annotationTypeDeclaration20 = self.annotationTypeDeclaration(modifierList16.tree)

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, annotationTypeDeclaration20.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 6, typeDeclaration_StartIndex, success)

            pass

        return retval

    # $ANTLR end "typeDeclaration"

    class classTypeDeclaration_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "classTypeDeclaration"
    # Java.g:294:1: classTypeDeclaration[modifiers] : CLASS IDENT ( genericTypeParameterList )? ( classExtendsClause )? ( implementsClause )? classBody -> ^( CLASS IDENT ( genericTypeParameterList )? ( classExtendsClause )? ( implementsClause )? classBody ) ;
    def classTypeDeclaration(self, modifiers):

        retval = self.classTypeDeclaration_return()
        retval.start = self.input.LT(1)
        classTypeDeclaration_StartIndex = self.input.index()
        root_0 = None

        CLASS21 = None
        IDENT22 = None
        genericTypeParameterList23 = None

        classExtendsClause24 = None

        implementsClause25 = None

        classBody26 = None


        CLASS21_tree = None
        IDENT22_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_CLASS = RewriteRuleTokenStream(self._adaptor, "token CLASS")
        stream_genericTypeParameterList = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeParameterList")
        stream_classExtendsClause = RewriteRuleSubtreeStream(self._adaptor, "rule classExtendsClause")
        stream_implementsClause = RewriteRuleSubtreeStream(self._adaptor, "rule implementsClause")
        stream_classBody = RewriteRuleSubtreeStream(self._adaptor, "rule classBody")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 7):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:295:5: ( CLASS IDENT ( genericTypeParameterList )? ( classExtendsClause )? ( implementsClause )? classBody -> ^( CLASS IDENT ( genericTypeParameterList )? ( classExtendsClause )? ( implementsClause )? classBody ) )
                # Java.g:295:9: CLASS IDENT ( genericTypeParameterList )? ( classExtendsClause )? ( implementsClause )? classBody
                pass 
                CLASS21=self.match(self.input, CLASS, self.FOLLOW_CLASS_in_classTypeDeclaration4764) 
                if self._state.backtracking == 0:
                    stream_CLASS.add(CLASS21)
                IDENT22=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_classTypeDeclaration4766) 
                if self._state.backtracking == 0:
                    stream_IDENT.add(IDENT22)
                # Java.g:295:21: ( genericTypeParameterList )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == LESS_THAN) :
                    alt8 = 1
                if alt8 == 1:
                    # Java.g:0:0: genericTypeParameterList
                    pass 
                    self._state.following.append(self.FOLLOW_genericTypeParameterList_in_classTypeDeclaration4768)
                    genericTypeParameterList23 = self.genericTypeParameterList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_genericTypeParameterList.add(genericTypeParameterList23.tree)



                # Java.g:295:47: ( classExtendsClause )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == EXTENDS) :
                    alt9 = 1
                if alt9 == 1:
                    # Java.g:0:0: classExtendsClause
                    pass 
                    self._state.following.append(self.FOLLOW_classExtendsClause_in_classTypeDeclaration4771)
                    classExtendsClause24 = self.classExtendsClause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_classExtendsClause.add(classExtendsClause24.tree)



                # Java.g:295:67: ( implementsClause )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == IMPLEMENTS) :
                    alt10 = 1
                if alt10 == 1:
                    # Java.g:0:0: implementsClause
                    pass 
                    self._state.following.append(self.FOLLOW_implementsClause_in_classTypeDeclaration4774)
                    implementsClause25 = self.implementsClause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_implementsClause.add(implementsClause25.tree)



                self._state.following.append(self.FOLLOW_classBody_in_classTypeDeclaration4777)
                classBody26 = self.classBody()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_classBody.add(classBody26.tree)

                # AST Rewrite
                # elements: implementsClause, IDENT, classExtendsClause, genericTypeParameterList, CLASS, classBody
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 296:9: -> ^( CLASS IDENT ( genericTypeParameterList )? ( classExtendsClause )? ( implementsClause )? classBody )
                    # Java.g:296:13: ^( CLASS IDENT ( genericTypeParameterList )? ( classExtendsClause )? ( implementsClause )? classBody )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_CLASS.nextNode(), root_1)

                    self._adaptor.addChild(root_1, modifiers)
                    self._adaptor.addChild(root_1, stream_IDENT.nextNode())
                    # Java.g:296:40: ( genericTypeParameterList )?
                    if stream_genericTypeParameterList.hasNext():
                        self._adaptor.addChild(root_1, stream_genericTypeParameterList.nextTree())


                    stream_genericTypeParameterList.reset();
                    # Java.g:296:66: ( classExtendsClause )?
                    if stream_classExtendsClause.hasNext():
                        self._adaptor.addChild(root_1, stream_classExtendsClause.nextTree())


                    stream_classExtendsClause.reset();
                    # Java.g:296:86: ( implementsClause )?
                    if stream_implementsClause.hasNext():
                        self._adaptor.addChild(root_1, stream_implementsClause.nextTree())


                    stream_implementsClause.reset();
                    self._adaptor.addChild(root_1, stream_classBody.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 7, classTypeDeclaration_StartIndex, success)

            pass

        return retval

    # $ANTLR end "classTypeDeclaration"

    class classExtendsClause_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "classExtendsClause"
    # Java.g:299:1: classExtendsClause : EXTENDS type -> ^( EXTENDS_CLAUSE[$EXTENDS, \"EXTENDS_CLAUSE\"] type ) ;
    def classExtendsClause(self, ):

        retval = self.classExtendsClause_return()
        retval.start = self.input.LT(1)
        classExtendsClause_StartIndex = self.input.index()
        root_0 = None

        EXTENDS27 = None
        type28 = None


        EXTENDS27_tree = None
        stream_EXTENDS = RewriteRuleTokenStream(self._adaptor, "token EXTENDS")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 8):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:300:5: ( EXTENDS type -> ^( EXTENDS_CLAUSE[$EXTENDS, \"EXTENDS_CLAUSE\"] type ) )
                # Java.g:300:9: EXTENDS type
                pass 
                EXTENDS27=self.match(self.input, EXTENDS, self.FOLLOW_EXTENDS_in_classExtendsClause4826) 
                if self._state.backtracking == 0:
                    stream_EXTENDS.add(EXTENDS27)
                self._state.following.append(self.FOLLOW_type_in_classExtendsClause4828)
                type28 = self.type()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_type.add(type28.tree)

                # AST Rewrite
                # elements: type
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 301:9: -> ^( EXTENDS_CLAUSE[$EXTENDS, \"EXTENDS_CLAUSE\"] type )
                    # Java.g:301:13: ^( EXTENDS_CLAUSE[$EXTENDS, \"EXTENDS_CLAUSE\"] type )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.create(EXTENDS_CLAUSE, EXTENDS27, "EXTENDS_CLAUSE"), root_1)

                    self._adaptor.addChild(root_1, stream_type.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 8, classExtendsClause_StartIndex, success)

            pass

        return retval

    # $ANTLR end "classExtendsClause"

    class interfaceExtendsClause_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "interfaceExtendsClause"
    # Java.g:304:1: interfaceExtendsClause : EXTENDS typeList -> ^( EXTENDS_CLAUSE[$EXTENDS, \"EXTENDS_CLAUSE\"] typeList ) ;
    def interfaceExtendsClause(self, ):

        retval = self.interfaceExtendsClause_return()
        retval.start = self.input.LT(1)
        interfaceExtendsClause_StartIndex = self.input.index()
        root_0 = None

        EXTENDS29 = None
        typeList30 = None


        EXTENDS29_tree = None
        stream_EXTENDS = RewriteRuleTokenStream(self._adaptor, "token EXTENDS")
        stream_typeList = RewriteRuleSubtreeStream(self._adaptor, "rule typeList")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 9):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:305:5: ( EXTENDS typeList -> ^( EXTENDS_CLAUSE[$EXTENDS, \"EXTENDS_CLAUSE\"] typeList ) )
                # Java.g:305:9: EXTENDS typeList
                pass 
                EXTENDS29=self.match(self.input, EXTENDS, self.FOLLOW_EXTENDS_in_interfaceExtendsClause4865) 
                if self._state.backtracking == 0:
                    stream_EXTENDS.add(EXTENDS29)
                self._state.following.append(self.FOLLOW_typeList_in_interfaceExtendsClause4867)
                typeList30 = self.typeList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_typeList.add(typeList30.tree)

                # AST Rewrite
                # elements: typeList
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 306:9: -> ^( EXTENDS_CLAUSE[$EXTENDS, \"EXTENDS_CLAUSE\"] typeList )
                    # Java.g:306:13: ^( EXTENDS_CLAUSE[$EXTENDS, \"EXTENDS_CLAUSE\"] typeList )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.create(EXTENDS_CLAUSE, EXTENDS29, "EXTENDS_CLAUSE"), root_1)

                    self._adaptor.addChild(root_1, stream_typeList.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 9, interfaceExtendsClause_StartIndex, success)

            pass

        return retval

    # $ANTLR end "interfaceExtendsClause"

    class implementsClause_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "implementsClause"
    # Java.g:309:1: implementsClause : IMPLEMENTS typeList -> ^( IMPLEMENTS_CLAUSE[$IMPLEMENTS, \"IMPLEMENTS_CLAUSE\"] typeList ) ;
    def implementsClause(self, ):

        retval = self.implementsClause_return()
        retval.start = self.input.LT(1)
        implementsClause_StartIndex = self.input.index()
        root_0 = None

        IMPLEMENTS31 = None
        typeList32 = None


        IMPLEMENTS31_tree = None
        stream_IMPLEMENTS = RewriteRuleTokenStream(self._adaptor, "token IMPLEMENTS")
        stream_typeList = RewriteRuleSubtreeStream(self._adaptor, "rule typeList")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 10):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:310:5: ( IMPLEMENTS typeList -> ^( IMPLEMENTS_CLAUSE[$IMPLEMENTS, \"IMPLEMENTS_CLAUSE\"] typeList ) )
                # Java.g:310:9: IMPLEMENTS typeList
                pass 
                IMPLEMENTS31=self.match(self.input, IMPLEMENTS, self.FOLLOW_IMPLEMENTS_in_implementsClause4904) 
                if self._state.backtracking == 0:
                    stream_IMPLEMENTS.add(IMPLEMENTS31)
                self._state.following.append(self.FOLLOW_typeList_in_implementsClause4906)
                typeList32 = self.typeList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_typeList.add(typeList32.tree)

                # AST Rewrite
                # elements: typeList
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 311:9: -> ^( IMPLEMENTS_CLAUSE[$IMPLEMENTS, \"IMPLEMENTS_CLAUSE\"] typeList )
                    # Java.g:311:13: ^( IMPLEMENTS_CLAUSE[$IMPLEMENTS, \"IMPLEMENTS_CLAUSE\"] typeList )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.create(IMPLEMENTS_CLAUSE, IMPLEMENTS31, "IMPLEMENTS_CLAUSE"), root_1)

                    self._adaptor.addChild(root_1, stream_typeList.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 10, implementsClause_StartIndex, success)

            pass

        return retval

    # $ANTLR end "implementsClause"

    class genericTypeParameterList_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "genericTypeParameterList"
    # Java.g:314:1: genericTypeParameterList : LESS_THAN genericTypeParameter ( COMMA genericTypeParameter )* genericTypeListClosing -> ^( GENERIC_TYPE_PARAM_LIST[$LESS_THAN, \"GENERIC_TYPE_PARAM_LIST\"] ( genericTypeParameter )+ ) ;
    def genericTypeParameterList(self, ):

        retval = self.genericTypeParameterList_return()
        retval.start = self.input.LT(1)
        genericTypeParameterList_StartIndex = self.input.index()
        root_0 = None

        LESS_THAN33 = None
        COMMA35 = None
        genericTypeParameter34 = None

        genericTypeParameter36 = None

        genericTypeListClosing37 = None


        LESS_THAN33_tree = None
        COMMA35_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LESS_THAN = RewriteRuleTokenStream(self._adaptor, "token LESS_THAN")
        stream_genericTypeParameter = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeParameter")
        stream_genericTypeListClosing = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeListClosing")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 11):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:315:5: ( LESS_THAN genericTypeParameter ( COMMA genericTypeParameter )* genericTypeListClosing -> ^( GENERIC_TYPE_PARAM_LIST[$LESS_THAN, \"GENERIC_TYPE_PARAM_LIST\"] ( genericTypeParameter )+ ) )
                # Java.g:315:9: LESS_THAN genericTypeParameter ( COMMA genericTypeParameter )* genericTypeListClosing
                pass 
                LESS_THAN33=self.match(self.input, LESS_THAN, self.FOLLOW_LESS_THAN_in_genericTypeParameterList4943) 
                if self._state.backtracking == 0:
                    stream_LESS_THAN.add(LESS_THAN33)
                self._state.following.append(self.FOLLOW_genericTypeParameter_in_genericTypeParameterList4945)
                genericTypeParameter34 = self.genericTypeParameter()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_genericTypeParameter.add(genericTypeParameter34.tree)
                # Java.g:315:40: ( COMMA genericTypeParameter )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == COMMA) :
                        alt11 = 1


                    if alt11 == 1:
                        # Java.g:315:41: COMMA genericTypeParameter
                        pass 
                        COMMA35=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_genericTypeParameterList4948) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA35)
                        self._state.following.append(self.FOLLOW_genericTypeParameter_in_genericTypeParameterList4950)
                        genericTypeParameter36 = self.genericTypeParameter()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_genericTypeParameter.add(genericTypeParameter36.tree)


                    else:
                        break #loop11


                self._state.following.append(self.FOLLOW_genericTypeListClosing_in_genericTypeParameterList4954)
                genericTypeListClosing37 = self.genericTypeListClosing()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_genericTypeListClosing.add(genericTypeListClosing37.tree)

                # AST Rewrite
                # elements: genericTypeParameter
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 316:9: -> ^( GENERIC_TYPE_PARAM_LIST[$LESS_THAN, \"GENERIC_TYPE_PARAM_LIST\"] ( genericTypeParameter )+ )
                    # Java.g:316:13: ^( GENERIC_TYPE_PARAM_LIST[$LESS_THAN, \"GENERIC_TYPE_PARAM_LIST\"] ( genericTypeParameter )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.create(GENERIC_TYPE_PARAM_LIST, LESS_THAN33, "GENERIC_TYPE_PARAM_LIST"), root_1)

                    # Java.g:316:78: ( genericTypeParameter )+
                    if not (stream_genericTypeParameter.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_genericTypeParameter.hasNext():
                        self._adaptor.addChild(root_1, stream_genericTypeParameter.nextTree())


                    stream_genericTypeParameter.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 11, genericTypeParameterList_StartIndex, success)

            pass

        return retval

    # $ANTLR end "genericTypeParameterList"

    class genericTypeListClosing_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "genericTypeListClosing"
    # Java.g:319:1: genericTypeListClosing : ( GREATER_THAN | SHIFT_RIGHT | BIT_SHIFT_RIGHT | );
    def genericTypeListClosing(self, ):

        retval = self.genericTypeListClosing_return()
        retval.start = self.input.LT(1)
        genericTypeListClosing_StartIndex = self.input.index()
        root_0 = None

        GREATER_THAN38 = None
        SHIFT_RIGHT39 = None
        BIT_SHIFT_RIGHT40 = None

        GREATER_THAN38_tree = None
        SHIFT_RIGHT39_tree = None
        BIT_SHIFT_RIGHT40_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 12):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:323:5: ( GREATER_THAN | SHIFT_RIGHT | BIT_SHIFT_RIGHT | )
                alt12 = 4
                LA12 = self.input.LA(1)
                if LA12 == GREATER_THAN:
                    LA12_1 = self.input.LA(2)

                    if (self.synpred14_Java()) :
                        alt12 = 1
                    elif (True) :
                        alt12 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 12, 1, self.input)

                        raise nvae

                elif LA12 == SHIFT_RIGHT:
                    LA12_2 = self.input.LA(2)

                    if (self.synpred15_Java()) :
                        alt12 = 2
                    elif (True) :
                        alt12 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 12, 2, self.input)

                        raise nvae

                elif LA12 == BIT_SHIFT_RIGHT:
                    LA12_3 = self.input.LA(2)

                    if (self.synpred16_Java()) :
                        alt12 = 3
                    elif (True) :
                        alt12 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 12, 3, self.input)

                        raise nvae

                elif LA12 == EOF or LA12 == AND or LA12 == AND_ASSIGN or LA12 == ASSIGN or LA12 == BIT_SHIFT_RIGHT_ASSIGN or LA12 == COLON or LA12 == COMMA or LA12 == DIV_ASSIGN or LA12 == DOT or LA12 == ELLIPSIS or LA12 == EQUAL or LA12 == LBRACK or LA12 == LCURLY or LA12 == LOGICAL_AND or LA12 == LOGICAL_OR or LA12 == LPAREN or LA12 == MINUS_ASSIGN or LA12 == MOD_ASSIGN or LA12 == NOT_EQUAL or LA12 == OR or LA12 == OR_ASSIGN or LA12 == PLUS_ASSIGN or LA12 == QUESTION or LA12 == RBRACK or LA12 == RCURLY or LA12 == RPAREN or LA12 == SEMI or LA12 == SHIFT_LEFT_ASSIGN or LA12 == SHIFT_RIGHT_ASSIGN or LA12 == STAR_ASSIGN or LA12 == XOR or LA12 == XOR_ASSIGN or LA12 == BOOLEAN or LA12 == BYTE or LA12 == CHAR or LA12 == DOUBLE or LA12 == EXTENDS or LA12 == FLOAT or LA12 == IMPLEMENTS or LA12 == INT or LA12 == LONG or LA12 == SHORT or LA12 == SUPER or LA12 == THIS or LA12 == VOID or LA12 == IDENT:
                    alt12 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 12, 0, self.input)

                    raise nvae

                if alt12 == 1:
                    # Java.g:323:9: GREATER_THAN
                    pass 
                    root_0 = self._adaptor.nil()

                    GREATER_THAN38=self.match(self.input, GREATER_THAN, self.FOLLOW_GREATER_THAN_in_genericTypeListClosing5069)
                    if self._state.backtracking == 0:

                        GREATER_THAN38_tree = self._adaptor.createWithPayload(GREATER_THAN38)
                        self._adaptor.addChild(root_0, GREATER_THAN38_tree)



                elif alt12 == 2:
                    # Java.g:324:9: SHIFT_RIGHT
                    pass 
                    root_0 = self._adaptor.nil()

                    SHIFT_RIGHT39=self.match(self.input, SHIFT_RIGHT, self.FOLLOW_SHIFT_RIGHT_in_genericTypeListClosing5079)
                    if self._state.backtracking == 0:

                        SHIFT_RIGHT39_tree = self._adaptor.createWithPayload(SHIFT_RIGHT39)
                        self._adaptor.addChild(root_0, SHIFT_RIGHT39_tree)



                elif alt12 == 3:
                    # Java.g:325:9: BIT_SHIFT_RIGHT
                    pass 
                    root_0 = self._adaptor.nil()

                    BIT_SHIFT_RIGHT40=self.match(self.input, BIT_SHIFT_RIGHT, self.FOLLOW_BIT_SHIFT_RIGHT_in_genericTypeListClosing5089)
                    if self._state.backtracking == 0:

                        BIT_SHIFT_RIGHT40_tree = self._adaptor.createWithPayload(BIT_SHIFT_RIGHT40)
                        self._adaptor.addChild(root_0, BIT_SHIFT_RIGHT40_tree)



                elif alt12 == 4:
                    # Java.g:327:5: 
                    pass 
                    root_0 = self._adaptor.nil()


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 12, genericTypeListClosing_StartIndex, success)

            pass

        return retval

    # $ANTLR end "genericTypeListClosing"

    class genericTypeParameter_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "genericTypeParameter"
    # Java.g:329:1: genericTypeParameter : IDENT ( bound )? -> ^( IDENT ( bound )? ) ;
    def genericTypeParameter(self, ):

        retval = self.genericTypeParameter_return()
        retval.start = self.input.LT(1)
        genericTypeParameter_StartIndex = self.input.index()
        root_0 = None

        IDENT41 = None
        bound42 = None


        IDENT41_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_bound = RewriteRuleSubtreeStream(self._adaptor, "rule bound")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 13):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:330:5: ( IDENT ( bound )? -> ^( IDENT ( bound )? ) )
                # Java.g:330:9: IDENT ( bound )?
                pass 
                IDENT41=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_genericTypeParameter5117) 
                if self._state.backtracking == 0:
                    stream_IDENT.add(IDENT41)
                # Java.g:330:15: ( bound )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == EXTENDS) :
                    LA13_1 = self.input.LA(2)

                    if (LA13_1 == BOOLEAN or LA13_1 == BYTE or LA13_1 == CHAR or LA13_1 == DOUBLE or LA13_1 == FLOAT or (INT <= LA13_1 <= LONG) or LA13_1 == SHORT) :
                        LA13_3 = self.input.LA(3)

                        if (self.synpred17_Java()) :
                            alt13 = 1
                    elif (LA13_1 == IDENT) :
                        LA13_4 = self.input.LA(3)

                        if (self.synpred17_Java()) :
                            alt13 = 1
                if alt13 == 1:
                    # Java.g:0:0: bound
                    pass 
                    self._state.following.append(self.FOLLOW_bound_in_genericTypeParameter5119)
                    bound42 = self.bound()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_bound.add(bound42.tree)




                # AST Rewrite
                # elements: bound, IDENT
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 331:9: -> ^( IDENT ( bound )? )
                    # Java.g:331:13: ^( IDENT ( bound )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_IDENT.nextNode(), root_1)

                    # Java.g:331:21: ( bound )?
                    if stream_bound.hasNext():
                        self._adaptor.addChild(root_1, stream_bound.nextTree())


                    stream_bound.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 13, genericTypeParameter_StartIndex, success)

            pass

        return retval

    # $ANTLR end "genericTypeParameter"

    class bound_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "bound"
    # Java.g:334:1: bound : EXTENDS type ( AND type )* -> ^( EXTENDS_BOUND_LIST[$EXTENDS, \"EXTENDS_BOUND_LIST\"] ( type )+ ) ;
    def bound(self, ):

        retval = self.bound_return()
        retval.start = self.input.LT(1)
        bound_StartIndex = self.input.index()
        root_0 = None

        EXTENDS43 = None
        AND45 = None
        type44 = None

        type46 = None


        EXTENDS43_tree = None
        AND45_tree = None
        stream_AND = RewriteRuleTokenStream(self._adaptor, "token AND")
        stream_EXTENDS = RewriteRuleTokenStream(self._adaptor, "token EXTENDS")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 14):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:335:5: ( EXTENDS type ( AND type )* -> ^( EXTENDS_BOUND_LIST[$EXTENDS, \"EXTENDS_BOUND_LIST\"] ( type )+ ) )
                # Java.g:335:9: EXTENDS type ( AND type )*
                pass 
                EXTENDS43=self.match(self.input, EXTENDS, self.FOLLOW_EXTENDS_in_bound5157) 
                if self._state.backtracking == 0:
                    stream_EXTENDS.add(EXTENDS43)
                self._state.following.append(self.FOLLOW_type_in_bound5159)
                type44 = self.type()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_type.add(type44.tree)
                # Java.g:335:22: ( AND type )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == AND) :
                        alt14 = 1


                    if alt14 == 1:
                        # Java.g:335:23: AND type
                        pass 
                        AND45=self.match(self.input, AND, self.FOLLOW_AND_in_bound5162) 
                        if self._state.backtracking == 0:
                            stream_AND.add(AND45)
                        self._state.following.append(self.FOLLOW_type_in_bound5164)
                        type46 = self.type()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_type.add(type46.tree)


                    else:
                        break #loop14



                # AST Rewrite
                # elements: type
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 336:9: -> ^( EXTENDS_BOUND_LIST[$EXTENDS, \"EXTENDS_BOUND_LIST\"] ( type )+ )
                    # Java.g:336:13: ^( EXTENDS_BOUND_LIST[$EXTENDS, \"EXTENDS_BOUND_LIST\"] ( type )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.create(EXTENDS_BOUND_LIST, EXTENDS43, "EXTENDS_BOUND_LIST"), root_1)

                    # Java.g:336:66: ( type )+
                    if not (stream_type.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_type.hasNext():
                        self._adaptor.addChild(root_1, stream_type.nextTree())


                    stream_type.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 14, bound_StartIndex, success)

            pass

        return retval

    # $ANTLR end "bound"

    class enumTypeDeclaration_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "enumTypeDeclaration"
    # Java.g:339:1: enumTypeDeclaration[modifiers] : ENUM IDENT ( implementsClause )? enumBody -> ^( ENUM IDENT ( implementsClause )? enumBody ) ;
    def enumTypeDeclaration(self, modifiers):

        retval = self.enumTypeDeclaration_return()
        retval.start = self.input.LT(1)
        enumTypeDeclaration_StartIndex = self.input.index()
        root_0 = None

        ENUM47 = None
        IDENT48 = None
        implementsClause49 = None

        enumBody50 = None


        ENUM47_tree = None
        IDENT48_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_ENUM = RewriteRuleTokenStream(self._adaptor, "token ENUM")
        stream_implementsClause = RewriteRuleSubtreeStream(self._adaptor, "rule implementsClause")
        stream_enumBody = RewriteRuleSubtreeStream(self._adaptor, "rule enumBody")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 15):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:340:5: ( ENUM IDENT ( implementsClause )? enumBody -> ^( ENUM IDENT ( implementsClause )? enumBody ) )
                # Java.g:340:9: ENUM IDENT ( implementsClause )? enumBody
                pass 
                ENUM47=self.match(self.input, ENUM, self.FOLLOW_ENUM_in_enumTypeDeclaration5205) 
                if self._state.backtracking == 0:
                    stream_ENUM.add(ENUM47)
                IDENT48=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_enumTypeDeclaration5207) 
                if self._state.backtracking == 0:
                    stream_IDENT.add(IDENT48)
                # Java.g:340:20: ( implementsClause )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == IMPLEMENTS) :
                    alt15 = 1
                if alt15 == 1:
                    # Java.g:0:0: implementsClause
                    pass 
                    self._state.following.append(self.FOLLOW_implementsClause_in_enumTypeDeclaration5209)
                    implementsClause49 = self.implementsClause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_implementsClause.add(implementsClause49.tree)



                self._state.following.append(self.FOLLOW_enumBody_in_enumTypeDeclaration5212)
                enumBody50 = self.enumBody()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_enumBody.add(enumBody50.tree)

                # AST Rewrite
                # elements: ENUM, implementsClause, enumBody, IDENT
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 341:9: -> ^( ENUM IDENT ( implementsClause )? enumBody )
                    # Java.g:341:13: ^( ENUM IDENT ( implementsClause )? enumBody )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_ENUM.nextNode(), root_1)

                    self._adaptor.addChild(root_1, modifiers)
                    self._adaptor.addChild(root_1, stream_IDENT.nextNode())
                    # Java.g:341:39: ( implementsClause )?
                    if stream_implementsClause.hasNext():
                        self._adaptor.addChild(root_1, stream_implementsClause.nextTree())


                    stream_implementsClause.reset();
                    self._adaptor.addChild(root_1, stream_enumBody.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 15, enumTypeDeclaration_StartIndex, success)

            pass

        return retval

    # $ANTLR end "enumTypeDeclaration"

    class enumBody_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "enumBody"
    # Java.g:344:1: enumBody : LCURLY enumScopeDeclarations RCURLY -> ^( ENUM_TOP_LEVEL_SCOPE[$LCURLY, \"ENUM_TOP_LEVEL_SCOPE\"] enumScopeDeclarations ) ;
    def enumBody(self, ):

        retval = self.enumBody_return()
        retval.start = self.input.LT(1)
        enumBody_StartIndex = self.input.index()
        root_0 = None

        LCURLY51 = None
        RCURLY53 = None
        enumScopeDeclarations52 = None


        LCURLY51_tree = None
        RCURLY53_tree = None
        stream_LCURLY = RewriteRuleTokenStream(self._adaptor, "token LCURLY")
        stream_RCURLY = RewriteRuleTokenStream(self._adaptor, "token RCURLY")
        stream_enumScopeDeclarations = RewriteRuleSubtreeStream(self._adaptor, "rule enumScopeDeclarations")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 16):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:345:5: ( LCURLY enumScopeDeclarations RCURLY -> ^( ENUM_TOP_LEVEL_SCOPE[$LCURLY, \"ENUM_TOP_LEVEL_SCOPE\"] enumScopeDeclarations ) )
                # Java.g:345:9: LCURLY enumScopeDeclarations RCURLY
                pass 
                LCURLY51=self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_enumBody5255) 
                if self._state.backtracking == 0:
                    stream_LCURLY.add(LCURLY51)
                self._state.following.append(self.FOLLOW_enumScopeDeclarations_in_enumBody5257)
                enumScopeDeclarations52 = self.enumScopeDeclarations()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_enumScopeDeclarations.add(enumScopeDeclarations52.tree)
                RCURLY53=self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_enumBody5259) 
                if self._state.backtracking == 0:
                    stream_RCURLY.add(RCURLY53)

                # AST Rewrite
                # elements: enumScopeDeclarations
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 346:9: -> ^( ENUM_TOP_LEVEL_SCOPE[$LCURLY, \"ENUM_TOP_LEVEL_SCOPE\"] enumScopeDeclarations )
                    # Java.g:346:13: ^( ENUM_TOP_LEVEL_SCOPE[$LCURLY, \"ENUM_TOP_LEVEL_SCOPE\"] enumScopeDeclarations )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.create(ENUM_TOP_LEVEL_SCOPE, LCURLY51, "ENUM_TOP_LEVEL_SCOPE"), root_1)

                    self._adaptor.addChild(root_1, stream_enumScopeDeclarations.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 16, enumBody_StartIndex, success)

            pass

        return retval

    # $ANTLR end "enumBody"

    class enumScopeDeclarations_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "enumScopeDeclarations"
    # Java.g:349:1: enumScopeDeclarations : enumConstants ( COMMA )? ( enumClassScopeDeclarations )? ;
    def enumScopeDeclarations(self, ):

        retval = self.enumScopeDeclarations_return()
        retval.start = self.input.LT(1)
        enumScopeDeclarations_StartIndex = self.input.index()
        root_0 = None

        COMMA55 = None
        enumConstants54 = None

        enumClassScopeDeclarations56 = None


        COMMA55_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 17):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:350:5: ( enumConstants ( COMMA )? ( enumClassScopeDeclarations )? )
                # Java.g:350:9: enumConstants ( COMMA )? ( enumClassScopeDeclarations )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_enumConstants_in_enumScopeDeclarations5296)
                enumConstants54 = self.enumConstants()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, enumConstants54.tree)
                # Java.g:350:23: ( COMMA )?
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == COMMA) :
                    alt16 = 1
                if alt16 == 1:
                    # Java.g:350:24: COMMA
                    pass 
                    COMMA55=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_enumScopeDeclarations5299)



                # Java.g:350:33: ( enumClassScopeDeclarations )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == SEMI) :
                    alt17 = 1
                if alt17 == 1:
                    # Java.g:0:0: enumClassScopeDeclarations
                    pass 
                    self._state.following.append(self.FOLLOW_enumClassScopeDeclarations_in_enumScopeDeclarations5304)
                    enumClassScopeDeclarations56 = self.enumClassScopeDeclarations()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, enumClassScopeDeclarations56.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 17, enumScopeDeclarations_StartIndex, success)

            pass

        return retval

    # $ANTLR end "enumScopeDeclarations"

    class enumClassScopeDeclarations_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "enumClassScopeDeclarations"
    # Java.g:353:1: enumClassScopeDeclarations : SEMI ( classScopeDeclarations )* -> ^( CLASS_TOP_LEVEL_SCOPE[$SEMI, \"CLASS_TOP_LEVEL_SCOPE\"] ( classScopeDeclarations )* ) ;
    def enumClassScopeDeclarations(self, ):

        retval = self.enumClassScopeDeclarations_return()
        retval.start = self.input.LT(1)
        enumClassScopeDeclarations_StartIndex = self.input.index()
        root_0 = None

        SEMI57 = None
        classScopeDeclarations58 = None


        SEMI57_tree = None
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_classScopeDeclarations = RewriteRuleSubtreeStream(self._adaptor, "rule classScopeDeclarations")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 18):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:354:5: ( SEMI ( classScopeDeclarations )* -> ^( CLASS_TOP_LEVEL_SCOPE[$SEMI, \"CLASS_TOP_LEVEL_SCOPE\"] ( classScopeDeclarations )* ) )
                # Java.g:354:9: SEMI ( classScopeDeclarations )*
                pass 
                SEMI57=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_enumClassScopeDeclarations5324) 
                if self._state.backtracking == 0:
                    stream_SEMI.add(SEMI57)
                # Java.g:354:14: ( classScopeDeclarations )*
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == AT or LA18_0 == LCURLY or LA18_0 == LESS_THAN or LA18_0 == SEMI or LA18_0 == ABSTRACT or LA18_0 == BOOLEAN or LA18_0 == BYTE or (CHAR <= LA18_0 <= CLASS) or LA18_0 == DOUBLE or LA18_0 == ENUM or LA18_0 == FINAL or LA18_0 == FLOAT or LA18_0 == INTERFACE or (INT <= LA18_0 <= NATIVE) or (PRIVATE <= LA18_0 <= PUBLIC) or (SHORT <= LA18_0 <= STRICTFP) or LA18_0 == SYNCHRONIZED or LA18_0 == TRANSIENT or (VOID <= LA18_0 <= VOLATILE) or LA18_0 == IDENT) :
                        alt18 = 1


                    if alt18 == 1:
                        # Java.g:0:0: classScopeDeclarations
                        pass 
                        self._state.following.append(self.FOLLOW_classScopeDeclarations_in_enumClassScopeDeclarations5326)
                        classScopeDeclarations58 = self.classScopeDeclarations()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_classScopeDeclarations.add(classScopeDeclarations58.tree)


                    else:
                        break #loop18



                # AST Rewrite
                # elements: classScopeDeclarations
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 355:9: -> ^( CLASS_TOP_LEVEL_SCOPE[$SEMI, \"CLASS_TOP_LEVEL_SCOPE\"] ( classScopeDeclarations )* )
                    # Java.g:355:13: ^( CLASS_TOP_LEVEL_SCOPE[$SEMI, \"CLASS_TOP_LEVEL_SCOPE\"] ( classScopeDeclarations )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.create(CLASS_TOP_LEVEL_SCOPE, SEMI57, "CLASS_TOP_LEVEL_SCOPE"), root_1)

                    # Java.g:355:69: ( classScopeDeclarations )*
                    while stream_classScopeDeclarations.hasNext():
                        self._adaptor.addChild(root_1, stream_classScopeDeclarations.nextTree())


                    stream_classScopeDeclarations.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 18, enumClassScopeDeclarations_StartIndex, success)

            pass

        return retval

    # $ANTLR end "enumClassScopeDeclarations"

    class enumConstants_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "enumConstants"
    # Java.g:358:1: enumConstants : enumConstant ( COMMA enumConstant )* ;
    def enumConstants(self, ):

        retval = self.enumConstants_return()
        retval.start = self.input.LT(1)
        enumConstants_StartIndex = self.input.index()
        root_0 = None

        COMMA60 = None
        enumConstant59 = None

        enumConstant61 = None


        COMMA60_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 19):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:359:5: ( enumConstant ( COMMA enumConstant )* )
                # Java.g:359:9: enumConstant ( COMMA enumConstant )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_enumConstant_in_enumConstants5365)
                enumConstant59 = self.enumConstant()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, enumConstant59.tree)
                # Java.g:359:22: ( COMMA enumConstant )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == COMMA) :
                        LA19_1 = self.input.LA(2)

                        if (LA19_1 == AT or LA19_1 == IDENT) :
                            alt19 = 1




                    if alt19 == 1:
                        # Java.g:359:23: COMMA enumConstant
                        pass 
                        COMMA60=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_enumConstants5368)
                        self._state.following.append(self.FOLLOW_enumConstant_in_enumConstants5371)
                        enumConstant61 = self.enumConstant()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, enumConstant61.tree)


                    else:
                        break #loop19





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 19, enumConstants_StartIndex, success)

            pass

        return retval

    # $ANTLR end "enumConstants"

    class enumConstant_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "enumConstant"
    # Java.g:362:1: enumConstant : annotationList IDENT ( arguments )? ( classBody )? ;
    def enumConstant(self, ):

        retval = self.enumConstant_return()
        retval.start = self.input.LT(1)
        enumConstant_StartIndex = self.input.index()
        root_0 = None

        IDENT63 = None
        annotationList62 = None

        arguments64 = None

        classBody65 = None


        IDENT63_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 20):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:363:5: ( annotationList IDENT ( arguments )? ( classBody )? )
                # Java.g:363:9: annotationList IDENT ( arguments )? ( classBody )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_annotationList_in_enumConstant5392)
                annotationList62 = self.annotationList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, annotationList62.tree)
                IDENT63=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_enumConstant5394)
                if self._state.backtracking == 0:

                    IDENT63_tree = self._adaptor.createWithPayload(IDENT63)
                    root_0 = self._adaptor.becomeRoot(IDENT63_tree, root_0)

                # Java.g:363:31: ( arguments )?
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == LPAREN) :
                    alt20 = 1
                if alt20 == 1:
                    # Java.g:0:0: arguments
                    pass 
                    self._state.following.append(self.FOLLOW_arguments_in_enumConstant5397)
                    arguments64 = self.arguments()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, arguments64.tree)



                # Java.g:363:42: ( classBody )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == LCURLY) :
                    alt21 = 1
                if alt21 == 1:
                    # Java.g:0:0: classBody
                    pass 
                    self._state.following.append(self.FOLLOW_classBody_in_enumConstant5400)
                    classBody65 = self.classBody()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, classBody65.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 20, enumConstant_StartIndex, success)

            pass

        return retval

    # $ANTLR end "enumConstant"

    class interfaceTypeDeclaration_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "interfaceTypeDeclaration"
    # Java.g:366:1: interfaceTypeDeclaration[modifiers] : INTERFACE IDENT ( genericTypeParameterList )? ( interfaceExtendsClause )? interfaceBody -> ^( INTERFACE IDENT ( genericTypeParameterList )? ( interfaceExtendsClause )? interfaceBody ) ;
    def interfaceTypeDeclaration(self, modifiers):

        retval = self.interfaceTypeDeclaration_return()
        retval.start = self.input.LT(1)
        interfaceTypeDeclaration_StartIndex = self.input.index()
        root_0 = None

        INTERFACE66 = None
        IDENT67 = None
        genericTypeParameterList68 = None

        interfaceExtendsClause69 = None

        interfaceBody70 = None


        INTERFACE66_tree = None
        IDENT67_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_INTERFACE = RewriteRuleTokenStream(self._adaptor, "token INTERFACE")
        stream_genericTypeParameterList = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeParameterList")
        stream_interfaceBody = RewriteRuleSubtreeStream(self._adaptor, "rule interfaceBody")
        stream_interfaceExtendsClause = RewriteRuleSubtreeStream(self._adaptor, "rule interfaceExtendsClause")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 21):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:367:5: ( INTERFACE IDENT ( genericTypeParameterList )? ( interfaceExtendsClause )? interfaceBody -> ^( INTERFACE IDENT ( genericTypeParameterList )? ( interfaceExtendsClause )? interfaceBody ) )
                # Java.g:367:9: INTERFACE IDENT ( genericTypeParameterList )? ( interfaceExtendsClause )? interfaceBody
                pass 
                INTERFACE66=self.match(self.input, INTERFACE, self.FOLLOW_INTERFACE_in_interfaceTypeDeclaration5421) 
                if self._state.backtracking == 0:
                    stream_INTERFACE.add(INTERFACE66)
                IDENT67=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_interfaceTypeDeclaration5423) 
                if self._state.backtracking == 0:
                    stream_IDENT.add(IDENT67)
                # Java.g:367:25: ( genericTypeParameterList )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == LESS_THAN) :
                    alt22 = 1
                if alt22 == 1:
                    # Java.g:0:0: genericTypeParameterList
                    pass 
                    self._state.following.append(self.FOLLOW_genericTypeParameterList_in_interfaceTypeDeclaration5425)
                    genericTypeParameterList68 = self.genericTypeParameterList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_genericTypeParameterList.add(genericTypeParameterList68.tree)



                # Java.g:367:51: ( interfaceExtendsClause )?
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == EXTENDS) :
                    alt23 = 1
                if alt23 == 1:
                    # Java.g:0:0: interfaceExtendsClause
                    pass 
                    self._state.following.append(self.FOLLOW_interfaceExtendsClause_in_interfaceTypeDeclaration5428)
                    interfaceExtendsClause69 = self.interfaceExtendsClause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_interfaceExtendsClause.add(interfaceExtendsClause69.tree)



                self._state.following.append(self.FOLLOW_interfaceBody_in_interfaceTypeDeclaration5431)
                interfaceBody70 = self.interfaceBody()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_interfaceBody.add(interfaceBody70.tree)

                # AST Rewrite
                # elements: INTERFACE, genericTypeParameterList, IDENT, interfaceBody, interfaceExtendsClause
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 368:9: -> ^( INTERFACE IDENT ( genericTypeParameterList )? ( interfaceExtendsClause )? interfaceBody )
                    # Java.g:368:13: ^( INTERFACE IDENT ( genericTypeParameterList )? ( interfaceExtendsClause )? interfaceBody )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_INTERFACE.nextNode(), root_1)

                    self._adaptor.addChild(root_1, modifiers)
                    self._adaptor.addChild(root_1, stream_IDENT.nextNode())
                    # Java.g:368:44: ( genericTypeParameterList )?
                    if stream_genericTypeParameterList.hasNext():
                        self._adaptor.addChild(root_1, stream_genericTypeParameterList.nextTree())


                    stream_genericTypeParameterList.reset();
                    # Java.g:368:70: ( interfaceExtendsClause )?
                    if stream_interfaceExtendsClause.hasNext():
                        self._adaptor.addChild(root_1, stream_interfaceExtendsClause.nextTree())


                    stream_interfaceExtendsClause.reset();
                    self._adaptor.addChild(root_1, stream_interfaceBody.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 21, interfaceTypeDeclaration_StartIndex, success)

            pass

        return retval

    # $ANTLR end "interfaceTypeDeclaration"

    class typeList_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "typeList"
    # Java.g:371:1: typeList : type ( COMMA type )* ;
    def typeList(self, ):

        retval = self.typeList_return()
        retval.start = self.input.LT(1)
        typeList_StartIndex = self.input.index()
        root_0 = None

        COMMA72 = None
        type71 = None

        type73 = None


        COMMA72_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 22):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:372:5: ( type ( COMMA type )* )
                # Java.g:372:9: type ( COMMA type )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_type_in_typeList5477)
                type71 = self.type()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, type71.tree)
                # Java.g:372:14: ( COMMA type )*
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == COMMA) :
                        alt24 = 1


                    if alt24 == 1:
                        # Java.g:372:15: COMMA type
                        pass 
                        COMMA72=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_typeList5480)
                        self._state.following.append(self.FOLLOW_type_in_typeList5483)
                        type73 = self.type()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, type73.tree)


                    else:
                        break #loop24





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 22, typeList_StartIndex, success)

            pass

        return retval

    # $ANTLR end "typeList"

    class classBody_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "classBody"
    # Java.g:375:1: classBody : LCURLY ( classScopeDeclarations )* RCURLY -> ^( CLASS_TOP_LEVEL_SCOPE[$LCURLY, \"CLASS_TOP_LEVEL_SCOPE\"] ( classScopeDeclarations )* ) ;
    def classBody(self, ):

        retval = self.classBody_return()
        retval.start = self.input.LT(1)
        classBody_StartIndex = self.input.index()
        root_0 = None

        LCURLY74 = None
        RCURLY76 = None
        classScopeDeclarations75 = None


        LCURLY74_tree = None
        RCURLY76_tree = None
        stream_LCURLY = RewriteRuleTokenStream(self._adaptor, "token LCURLY")
        stream_RCURLY = RewriteRuleTokenStream(self._adaptor, "token RCURLY")
        stream_classScopeDeclarations = RewriteRuleSubtreeStream(self._adaptor, "rule classScopeDeclarations")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 23):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:376:5: ( LCURLY ( classScopeDeclarations )* RCURLY -> ^( CLASS_TOP_LEVEL_SCOPE[$LCURLY, \"CLASS_TOP_LEVEL_SCOPE\"] ( classScopeDeclarations )* ) )
                # Java.g:376:9: LCURLY ( classScopeDeclarations )* RCURLY
                pass 
                LCURLY74=self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_classBody5504) 
                if self._state.backtracking == 0:
                    stream_LCURLY.add(LCURLY74)
                # Java.g:376:16: ( classScopeDeclarations )*
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == AT or LA25_0 == LCURLY or LA25_0 == LESS_THAN or LA25_0 == SEMI or LA25_0 == ABSTRACT or LA25_0 == BOOLEAN or LA25_0 == BYTE or (CHAR <= LA25_0 <= CLASS) or LA25_0 == DOUBLE or LA25_0 == ENUM or LA25_0 == FINAL or LA25_0 == FLOAT or LA25_0 == INTERFACE or (INT <= LA25_0 <= NATIVE) or (PRIVATE <= LA25_0 <= PUBLIC) or (SHORT <= LA25_0 <= STRICTFP) or LA25_0 == SYNCHRONIZED or LA25_0 == TRANSIENT or (VOID <= LA25_0 <= VOLATILE) or LA25_0 == IDENT) :
                        alt25 = 1


                    if alt25 == 1:
                        # Java.g:0:0: classScopeDeclarations
                        pass 
                        self._state.following.append(self.FOLLOW_classScopeDeclarations_in_classBody5506)
                        classScopeDeclarations75 = self.classScopeDeclarations()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_classScopeDeclarations.add(classScopeDeclarations75.tree)


                    else:
                        break #loop25


                RCURLY76=self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_classBody5509) 
                if self._state.backtracking == 0:
                    stream_RCURLY.add(RCURLY76)

                # AST Rewrite
                # elements: classScopeDeclarations
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 377:9: -> ^( CLASS_TOP_LEVEL_SCOPE[$LCURLY, \"CLASS_TOP_LEVEL_SCOPE\"] ( classScopeDeclarations )* )
                    # Java.g:377:13: ^( CLASS_TOP_LEVEL_SCOPE[$LCURLY, \"CLASS_TOP_LEVEL_SCOPE\"] ( classScopeDeclarations )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.create(CLASS_TOP_LEVEL_SCOPE, LCURLY74, "CLASS_TOP_LEVEL_SCOPE"), root_1)

                    # Java.g:377:71: ( classScopeDeclarations )*
                    while stream_classScopeDeclarations.hasNext():
                        self._adaptor.addChild(root_1, stream_classScopeDeclarations.nextTree())


                    stream_classScopeDeclarations.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 23, classBody_StartIndex, success)

            pass

        return retval

    # $ANTLR end "classBody"

    class interfaceBody_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "interfaceBody"
    # Java.g:380:1: interfaceBody : LCURLY ( interfaceScopeDeclarations )* RCURLY -> ^( INTERFACE_TOP_LEVEL_SCOPE[$LCURLY, \"CLASS_TOP_LEVEL_SCOPE\"] ( interfaceScopeDeclarations )* ) ;
    def interfaceBody(self, ):

        retval = self.interfaceBody_return()
        retval.start = self.input.LT(1)
        interfaceBody_StartIndex = self.input.index()
        root_0 = None

        LCURLY77 = None
        RCURLY79 = None
        interfaceScopeDeclarations78 = None


        LCURLY77_tree = None
        RCURLY79_tree = None
        stream_LCURLY = RewriteRuleTokenStream(self._adaptor, "token LCURLY")
        stream_RCURLY = RewriteRuleTokenStream(self._adaptor, "token RCURLY")
        stream_interfaceScopeDeclarations = RewriteRuleSubtreeStream(self._adaptor, "rule interfaceScopeDeclarations")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 24):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:381:5: ( LCURLY ( interfaceScopeDeclarations )* RCURLY -> ^( INTERFACE_TOP_LEVEL_SCOPE[$LCURLY, \"CLASS_TOP_LEVEL_SCOPE\"] ( interfaceScopeDeclarations )* ) )
                # Java.g:381:9: LCURLY ( interfaceScopeDeclarations )* RCURLY
                pass 
                LCURLY77=self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_interfaceBody5547) 
                if self._state.backtracking == 0:
                    stream_LCURLY.add(LCURLY77)
                # Java.g:381:16: ( interfaceScopeDeclarations )*
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == AT or LA26_0 == LESS_THAN or LA26_0 == SEMI or LA26_0 == ABSTRACT or LA26_0 == BOOLEAN or LA26_0 == BYTE or (CHAR <= LA26_0 <= CLASS) or LA26_0 == DOUBLE or LA26_0 == ENUM or LA26_0 == FINAL or LA26_0 == FLOAT or LA26_0 == INTERFACE or (INT <= LA26_0 <= NATIVE) or (PRIVATE <= LA26_0 <= PUBLIC) or (SHORT <= LA26_0 <= STRICTFP) or LA26_0 == SYNCHRONIZED or LA26_0 == TRANSIENT or (VOID <= LA26_0 <= VOLATILE) or LA26_0 == IDENT) :
                        alt26 = 1


                    if alt26 == 1:
                        # Java.g:0:0: interfaceScopeDeclarations
                        pass 
                        self._state.following.append(self.FOLLOW_interfaceScopeDeclarations_in_interfaceBody5549)
                        interfaceScopeDeclarations78 = self.interfaceScopeDeclarations()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_interfaceScopeDeclarations.add(interfaceScopeDeclarations78.tree)


                    else:
                        break #loop26


                RCURLY79=self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_interfaceBody5552) 
                if self._state.backtracking == 0:
                    stream_RCURLY.add(RCURLY79)

                # AST Rewrite
                # elements: interfaceScopeDeclarations
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 382:9: -> ^( INTERFACE_TOP_LEVEL_SCOPE[$LCURLY, \"CLASS_TOP_LEVEL_SCOPE\"] ( interfaceScopeDeclarations )* )
                    # Java.g:382:13: ^( INTERFACE_TOP_LEVEL_SCOPE[$LCURLY, \"CLASS_TOP_LEVEL_SCOPE\"] ( interfaceScopeDeclarations )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.create(INTERFACE_TOP_LEVEL_SCOPE, LCURLY77, "CLASS_TOP_LEVEL_SCOPE"), root_1)

                    # Java.g:382:75: ( interfaceScopeDeclarations )*
                    while stream_interfaceScopeDeclarations.hasNext():
                        self._adaptor.addChild(root_1, stream_interfaceScopeDeclarations.nextTree())


                    stream_interfaceScopeDeclarations.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 24, interfaceBody_StartIndex, success)

            pass

        return retval

    # $ANTLR end "interfaceBody"

    class classScopeDeclarations_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "classScopeDeclarations"
    # Java.g:385:1: classScopeDeclarations : ( block -> ^( CLASS_INSTANCE_INITIALIZER block ) | STATIC block -> ^( CLASS_STATIC_INITIALIZER[$STATIC, \"CLASS_STATIC_INITIALIZER\"] block ) | modifierList ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block )? ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ( block )? ) | ident= IDENT formalParameterList ( throwsClause )? block -> ^( CONSTRUCTOR_DECL[$ident, \"CONSTRUCTOR_DECL\"] modifierList ( genericTypeParameterList )? formalParameterList ( throwsClause )? block ) ) | type classFieldDeclaratorList SEMI -> ^( VAR_DECLARATION modifierList type classFieldDeclaratorList ) ) | typeDeclaration | SEMI );
    def classScopeDeclarations(self, ):

        retval = self.classScopeDeclarations_return()
        retval.start = self.input.LT(1)
        classScopeDeclarations_StartIndex = self.input.index()
        root_0 = None

        ident = None
        STATIC81 = None
        IDENT86 = None
        SEMI91 = None
        VOID92 = None
        IDENT93 = None
        SEMI97 = None
        SEMI103 = None
        SEMI105 = None
        block80 = None

        block82 = None

        modifierList83 = None

        genericTypeParameterList84 = None

        type85 = None

        formalParameterList87 = None

        arrayDeclaratorList88 = None

        throwsClause89 = None

        block90 = None

        formalParameterList94 = None

        throwsClause95 = None

        block96 = None

        formalParameterList98 = None

        throwsClause99 = None

        block100 = None

        type101 = None

        classFieldDeclaratorList102 = None

        typeDeclaration104 = None


        ident_tree = None
        STATIC81_tree = None
        IDENT86_tree = None
        SEMI91_tree = None
        VOID92_tree = None
        IDENT93_tree = None
        SEMI97_tree = None
        SEMI103_tree = None
        SEMI105_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_VOID = RewriteRuleTokenStream(self._adaptor, "token VOID")
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_STATIC = RewriteRuleTokenStream(self._adaptor, "token STATIC")
        stream_arrayDeclaratorList = RewriteRuleSubtreeStream(self._adaptor, "rule arrayDeclaratorList")
        stream_throwsClause = RewriteRuleSubtreeStream(self._adaptor, "rule throwsClause")
        stream_modifierList = RewriteRuleSubtreeStream(self._adaptor, "rule modifierList")
        stream_genericTypeParameterList = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeParameterList")
        stream_block = RewriteRuleSubtreeStream(self._adaptor, "rule block")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        stream_classFieldDeclaratorList = RewriteRuleSubtreeStream(self._adaptor, "rule classFieldDeclaratorList")
        stream_formalParameterList = RewriteRuleSubtreeStream(self._adaptor, "rule formalParameterList")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 25):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:386:5: ( block -> ^( CLASS_INSTANCE_INITIALIZER block ) | STATIC block -> ^( CLASS_STATIC_INITIALIZER[$STATIC, \"CLASS_STATIC_INITIALIZER\"] block ) | modifierList ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block )? ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ( block )? ) | ident= IDENT formalParameterList ( throwsClause )? block -> ^( CONSTRUCTOR_DECL[$ident, \"CONSTRUCTOR_DECL\"] modifierList ( genericTypeParameterList )? formalParameterList ( throwsClause )? block ) ) | type classFieldDeclaratorList SEMI -> ^( VAR_DECLARATION modifierList type classFieldDeclaratorList ) ) | typeDeclaration | SEMI )
                alt36 = 5
                alt36 = self.dfa36.predict(self.input)
                if alt36 == 1:
                    # Java.g:386:9: block
                    pass 
                    self._state.following.append(self.FOLLOW_block_in_classScopeDeclarations5590)
                    block80 = self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_block.add(block80.tree)

                    # AST Rewrite
                    # elements: block
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 386:25: -> ^( CLASS_INSTANCE_INITIALIZER block )
                        # Java.g:386:29: ^( CLASS_INSTANCE_INITIALIZER block )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CLASS_INSTANCE_INITIALIZER, "CLASS_INSTANCE_INITIALIZER"), root_1)

                        self._adaptor.addChild(root_1, stream_block.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt36 == 2:
                    # Java.g:387:9: STATIC block
                    pass 
                    STATIC81=self.match(self.input, STATIC, self.FOLLOW_STATIC_in_classScopeDeclarations5619) 
                    if self._state.backtracking == 0:
                        stream_STATIC.add(STATIC81)
                    self._state.following.append(self.FOLLOW_block_in_classScopeDeclarations5621)
                    block82 = self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_block.add(block82.tree)

                    # AST Rewrite
                    # elements: block
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 387:25: -> ^( CLASS_STATIC_INITIALIZER[$STATIC, \"CLASS_STATIC_INITIALIZER\"] block )
                        # Java.g:387:29: ^( CLASS_STATIC_INITIALIZER[$STATIC, \"CLASS_STATIC_INITIALIZER\"] block )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.create(CLASS_STATIC_INITIALIZER, STATIC81, "CLASS_STATIC_INITIALIZER"), root_1)

                        self._adaptor.addChild(root_1, stream_block.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt36 == 3:
                    # Java.g:388:9: modifierList ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block )? ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ( block )? ) | ident= IDENT formalParameterList ( throwsClause )? block -> ^( CONSTRUCTOR_DECL[$ident, \"CONSTRUCTOR_DECL\"] modifierList ( genericTypeParameterList )? formalParameterList ( throwsClause )? block ) ) | type classFieldDeclaratorList SEMI -> ^( VAR_DECLARATION modifierList type classFieldDeclaratorList ) )
                    pass 
                    self._state.following.append(self.FOLLOW_modifierList_in_classScopeDeclarations5644)
                    modifierList83 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_modifierList.add(modifierList83.tree)
                    # Java.g:389:9: ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block )? ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ( block )? ) | ident= IDENT formalParameterList ( throwsClause )? block -> ^( CONSTRUCTOR_DECL[$ident, \"CONSTRUCTOR_DECL\"] modifierList ( genericTypeParameterList )? formalParameterList ( throwsClause )? block ) ) | type classFieldDeclaratorList SEMI -> ^( VAR_DECLARATION modifierList type classFieldDeclaratorList ) )
                    alt35 = 2
                    LA35 = self.input.LA(1)
                    if LA35 == LESS_THAN or LA35 == VOID:
                        alt35 = 1
                    elif LA35 == BOOLEAN or LA35 == BYTE or LA35 == CHAR or LA35 == DOUBLE or LA35 == FLOAT or LA35 == INT or LA35 == LONG or LA35 == SHORT:
                        LA35_2 = self.input.LA(2)

                        if (self.synpred42_Java()) :
                            alt35 = 1
                        elif (True) :
                            alt35 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 35, 2, self.input)

                            raise nvae

                    elif LA35 == IDENT:
                        LA35_3 = self.input.LA(2)

                        if (self.synpred42_Java()) :
                            alt35 = 1
                        elif (True) :
                            alt35 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 35, 3, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 35, 0, self.input)

                        raise nvae

                    if alt35 == 1:
                        # Java.g:389:13: ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block )? ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ( block )? ) | ident= IDENT formalParameterList ( throwsClause )? block -> ^( CONSTRUCTOR_DECL[$ident, \"CONSTRUCTOR_DECL\"] modifierList ( genericTypeParameterList )? formalParameterList ( throwsClause )? block ) )
                        pass 
                        # Java.g:389:13: ( genericTypeParameterList )?
                        alt27 = 2
                        LA27_0 = self.input.LA(1)

                        if (LA27_0 == LESS_THAN) :
                            alt27 = 1
                        if alt27 == 1:
                            # Java.g:0:0: genericTypeParameterList
                            pass 
                            self._state.following.append(self.FOLLOW_genericTypeParameterList_in_classScopeDeclarations5658)
                            genericTypeParameterList84 = self.genericTypeParameterList()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_genericTypeParameterList.add(genericTypeParameterList84.tree)



                        # Java.g:390:13: ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block )? ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ( block )? ) | ident= IDENT formalParameterList ( throwsClause )? block -> ^( CONSTRUCTOR_DECL[$ident, \"CONSTRUCTOR_DECL\"] modifierList ( genericTypeParameterList )? formalParameterList ( throwsClause )? block ) )
                        alt34 = 3
                        LA34 = self.input.LA(1)
                        if LA34 == BOOLEAN or LA34 == BYTE or LA34 == CHAR or LA34 == DOUBLE or LA34 == FLOAT or LA34 == INT or LA34 == LONG or LA34 == SHORT:
                            alt34 = 1
                        elif LA34 == IDENT:
                            LA34_2 = self.input.LA(2)

                            if (LA34_2 == DOT or LA34_2 == LBRACK or LA34_2 == LESS_THAN or LA34_2 == IDENT) :
                                alt34 = 1
                            elif (LA34_2 == LPAREN) :
                                alt34 = 3
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                nvae = NoViableAltException("", 34, 2, self.input)

                                raise nvae

                        elif LA34 == VOID:
                            alt34 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 34, 0, self.input)

                            raise nvae

                        if alt34 == 1:
                            # Java.g:390:17: type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI )
                            pass 
                            self._state.following.append(self.FOLLOW_type_in_classScopeDeclarations5677)
                            type85 = self.type()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_type.add(type85.tree)
                            IDENT86=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_classScopeDeclarations5679) 
                            if self._state.backtracking == 0:
                                stream_IDENT.add(IDENT86)
                            self._state.following.append(self.FOLLOW_formalParameterList_in_classScopeDeclarations5681)
                            formalParameterList87 = self.formalParameterList()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_formalParameterList.add(formalParameterList87.tree)
                            # Java.g:390:48: ( arrayDeclaratorList )?
                            alt28 = 2
                            LA28_0 = self.input.LA(1)

                            if (LA28_0 == LBRACK) :
                                alt28 = 1
                            if alt28 == 1:
                                # Java.g:0:0: arrayDeclaratorList
                                pass 
                                self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_classScopeDeclarations5683)
                                arrayDeclaratorList88 = self.arrayDeclaratorList()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    stream_arrayDeclaratorList.add(arrayDeclaratorList88.tree)



                            # Java.g:390:69: ( throwsClause )?
                            alt29 = 2
                            LA29_0 = self.input.LA(1)

                            if (LA29_0 == THROWS) :
                                alt29 = 1
                            if alt29 == 1:
                                # Java.g:0:0: throwsClause
                                pass 
                                self._state.following.append(self.FOLLOW_throwsClause_in_classScopeDeclarations5686)
                                throwsClause89 = self.throwsClause()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    stream_throwsClause.add(throwsClause89.tree)



                            # Java.g:390:83: ( block | SEMI )
                            alt30 = 2
                            LA30_0 = self.input.LA(1)

                            if (LA30_0 == LCURLY) :
                                alt30 = 1
                            elif (LA30_0 == SEMI) :
                                alt30 = 2
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                nvae = NoViableAltException("", 30, 0, self.input)

                                raise nvae

                            if alt30 == 1:
                                # Java.g:390:84: block
                                pass 
                                self._state.following.append(self.FOLLOW_block_in_classScopeDeclarations5690)
                                block90 = self.block()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    stream_block.add(block90.tree)


                            elif alt30 == 2:
                                # Java.g:390:92: SEMI
                                pass 
                                SEMI91=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_classScopeDeclarations5694) 
                                if self._state.backtracking == 0:
                                    stream_SEMI.add(SEMI91)




                            # AST Rewrite
                            # elements: arrayDeclaratorList, block, throwsClause, type, genericTypeParameterList, modifierList, formalParameterList, IDENT
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            if self._state.backtracking == 0:

                                retval.tree = root_0

                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 391:17: -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block )? )
                                # Java.g:391:21: ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block )? )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FUNCTION_METHOD_DECL, "FUNCTION_METHOD_DECL"), root_1)

                                self._adaptor.addChild(root_1, stream_modifierList.nextTree())
                                # Java.g:391:57: ( genericTypeParameterList )?
                                if stream_genericTypeParameterList.hasNext():
                                    self._adaptor.addChild(root_1, stream_genericTypeParameterList.nextTree())


                                stream_genericTypeParameterList.reset();
                                self._adaptor.addChild(root_1, stream_type.nextTree())
                                self._adaptor.addChild(root_1, stream_IDENT.nextNode())
                                self._adaptor.addChild(root_1, stream_formalParameterList.nextTree())
                                # Java.g:391:114: ( arrayDeclaratorList )?
                                if stream_arrayDeclaratorList.hasNext():
                                    self._adaptor.addChild(root_1, stream_arrayDeclaratorList.nextTree())


                                stream_arrayDeclaratorList.reset();
                                # Java.g:391:135: ( throwsClause )?
                                if stream_throwsClause.hasNext():
                                    self._adaptor.addChild(root_1, stream_throwsClause.nextTree())


                                stream_throwsClause.reset();
                                # Java.g:391:149: ( block )?
                                if stream_block.hasNext():
                                    self._adaptor.addChild(root_1, stream_block.nextTree())


                                stream_block.reset();

                                self._adaptor.addChild(root_0, root_1)



                                retval.tree = root_0


                        elif alt34 == 2:
                            # Java.g:392:17: VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI )
                            pass 
                            VOID92=self.match(self.input, VOID, self.FOLLOW_VOID_in_classScopeDeclarations5756) 
                            if self._state.backtracking == 0:
                                stream_VOID.add(VOID92)
                            IDENT93=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_classScopeDeclarations5758) 
                            if self._state.backtracking == 0:
                                stream_IDENT.add(IDENT93)
                            self._state.following.append(self.FOLLOW_formalParameterList_in_classScopeDeclarations5760)
                            formalParameterList94 = self.formalParameterList()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_formalParameterList.add(formalParameterList94.tree)
                            # Java.g:392:48: ( throwsClause )?
                            alt31 = 2
                            LA31_0 = self.input.LA(1)

                            if (LA31_0 == THROWS) :
                                alt31 = 1
                            if alt31 == 1:
                                # Java.g:0:0: throwsClause
                                pass 
                                self._state.following.append(self.FOLLOW_throwsClause_in_classScopeDeclarations5762)
                                throwsClause95 = self.throwsClause()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    stream_throwsClause.add(throwsClause95.tree)



                            # Java.g:392:62: ( block | SEMI )
                            alt32 = 2
                            LA32_0 = self.input.LA(1)

                            if (LA32_0 == LCURLY) :
                                alt32 = 1
                            elif (LA32_0 == SEMI) :
                                alt32 = 2
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                nvae = NoViableAltException("", 32, 0, self.input)

                                raise nvae

                            if alt32 == 1:
                                # Java.g:392:63: block
                                pass 
                                self._state.following.append(self.FOLLOW_block_in_classScopeDeclarations5766)
                                block96 = self.block()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    stream_block.add(block96.tree)


                            elif alt32 == 2:
                                # Java.g:392:71: SEMI
                                pass 
                                SEMI97=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_classScopeDeclarations5770) 
                                if self._state.backtracking == 0:
                                    stream_SEMI.add(SEMI97)




                            # AST Rewrite
                            # elements: block, IDENT, throwsClause, genericTypeParameterList, modifierList, formalParameterList
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            if self._state.backtracking == 0:

                                retval.tree = root_0

                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 393:17: -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ( block )? )
                                # Java.g:393:21: ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ( block )? )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VOID_METHOD_DECL, "VOID_METHOD_DECL"), root_1)

                                self._adaptor.addChild(root_1, stream_modifierList.nextTree())
                                # Java.g:393:53: ( genericTypeParameterList )?
                                if stream_genericTypeParameterList.hasNext():
                                    self._adaptor.addChild(root_1, stream_genericTypeParameterList.nextTree())


                                stream_genericTypeParameterList.reset();
                                self._adaptor.addChild(root_1, stream_IDENT.nextNode())
                                self._adaptor.addChild(root_1, stream_formalParameterList.nextTree())
                                # Java.g:393:105: ( throwsClause )?
                                if stream_throwsClause.hasNext():
                                    self._adaptor.addChild(root_1, stream_throwsClause.nextTree())


                                stream_throwsClause.reset();
                                # Java.g:393:119: ( block )?
                                if stream_block.hasNext():
                                    self._adaptor.addChild(root_1, stream_block.nextTree())


                                stream_block.reset();

                                self._adaptor.addChild(root_0, root_1)



                                retval.tree = root_0


                        elif alt34 == 3:
                            # Java.g:394:17: ident= IDENT formalParameterList ( throwsClause )? block
                            pass 
                            ident=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_classScopeDeclarations5829) 
                            if self._state.backtracking == 0:
                                stream_IDENT.add(ident)
                            self._state.following.append(self.FOLLOW_formalParameterList_in_classScopeDeclarations5831)
                            formalParameterList98 = self.formalParameterList()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_formalParameterList.add(formalParameterList98.tree)
                            # Java.g:394:49: ( throwsClause )?
                            alt33 = 2
                            LA33_0 = self.input.LA(1)

                            if (LA33_0 == THROWS) :
                                alt33 = 1
                            if alt33 == 1:
                                # Java.g:0:0: throwsClause
                                pass 
                                self._state.following.append(self.FOLLOW_throwsClause_in_classScopeDeclarations5833)
                                throwsClause99 = self.throwsClause()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    stream_throwsClause.add(throwsClause99.tree)



                            self._state.following.append(self.FOLLOW_block_in_classScopeDeclarations5836)
                            block100 = self.block()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_block.add(block100.tree)

                            # AST Rewrite
                            # elements: throwsClause, block, formalParameterList, genericTypeParameterList, modifierList
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            if self._state.backtracking == 0:

                                retval.tree = root_0

                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 395:17: -> ^( CONSTRUCTOR_DECL[$ident, \"CONSTRUCTOR_DECL\"] modifierList ( genericTypeParameterList )? formalParameterList ( throwsClause )? block )
                                # Java.g:395:21: ^( CONSTRUCTOR_DECL[$ident, \"CONSTRUCTOR_DECL\"] modifierList ( genericTypeParameterList )? formalParameterList ( throwsClause )? block )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(self._adaptor.create(CONSTRUCTOR_DECL, ident, "CONSTRUCTOR_DECL"), root_1)

                                self._adaptor.addChild(root_1, stream_modifierList.nextTree())
                                # Java.g:395:81: ( genericTypeParameterList )?
                                if stream_genericTypeParameterList.hasNext():
                                    self._adaptor.addChild(root_1, stream_genericTypeParameterList.nextTree())


                                stream_genericTypeParameterList.reset();
                                self._adaptor.addChild(root_1, stream_formalParameterList.nextTree())
                                # Java.g:395:127: ( throwsClause )?
                                if stream_throwsClause.hasNext():
                                    self._adaptor.addChild(root_1, stream_throwsClause.nextTree())


                                stream_throwsClause.reset();
                                self._adaptor.addChild(root_1, stream_block.nextTree())

                                self._adaptor.addChild(root_0, root_1)



                                retval.tree = root_0





                    elif alt35 == 2:
                        # Java.g:397:13: type classFieldDeclaratorList SEMI
                        pass 
                        self._state.following.append(self.FOLLOW_type_in_classScopeDeclarations5900)
                        type101 = self.type()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_type.add(type101.tree)
                        self._state.following.append(self.FOLLOW_classFieldDeclaratorList_in_classScopeDeclarations5902)
                        classFieldDeclaratorList102 = self.classFieldDeclaratorList()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_classFieldDeclaratorList.add(classFieldDeclaratorList102.tree)
                        SEMI103=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_classScopeDeclarations5904) 
                        if self._state.backtracking == 0:
                            stream_SEMI.add(SEMI103)

                        # AST Rewrite
                        # elements: modifierList, type, classFieldDeclaratorList
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 398:13: -> ^( VAR_DECLARATION modifierList type classFieldDeclaratorList )
                            # Java.g:398:17: ^( VAR_DECLARATION modifierList type classFieldDeclaratorList )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAR_DECLARATION, "VAR_DECLARATION"), root_1)

                            self._adaptor.addChild(root_1, stream_modifierList.nextTree())
                            self._adaptor.addChild(root_1, stream_type.nextTree())
                            self._adaptor.addChild(root_1, stream_classFieldDeclaratorList.nextTree())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0





                elif alt36 == 4:
                    # Java.g:400:9: typeDeclaration
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_typeDeclaration_in_classScopeDeclarations5949)
                    typeDeclaration104 = self.typeDeclaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, typeDeclaration104.tree)


                elif alt36 == 5:
                    # Java.g:401:9: SEMI
                    pass 
                    root_0 = self._adaptor.nil()

                    SEMI105=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_classScopeDeclarations5959)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 25, classScopeDeclarations_StartIndex, success)

            pass

        return retval

    # $ANTLR end "classScopeDeclarations"

    class interfaceScopeDeclarations_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "interfaceScopeDeclarations"
    # Java.g:404:1: interfaceScopeDeclarations : ( modifierList ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ) | VOID IDENT formalParameterList ( throwsClause )? SEMI -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ) ) | type interfaceFieldDeclaratorList SEMI -> ^( VAR_DECLARATION modifierList type interfaceFieldDeclaratorList ) ) | typeDeclaration | SEMI );
    def interfaceScopeDeclarations(self, ):

        retval = self.interfaceScopeDeclarations_return()
        retval.start = self.input.LT(1)
        interfaceScopeDeclarations_StartIndex = self.input.index()
        root_0 = None

        IDENT109 = None
        SEMI113 = None
        VOID114 = None
        IDENT115 = None
        SEMI118 = None
        SEMI121 = None
        SEMI123 = None
        modifierList106 = None

        genericTypeParameterList107 = None

        type108 = None

        formalParameterList110 = None

        arrayDeclaratorList111 = None

        throwsClause112 = None

        formalParameterList116 = None

        throwsClause117 = None

        type119 = None

        interfaceFieldDeclaratorList120 = None

        typeDeclaration122 = None


        IDENT109_tree = None
        SEMI113_tree = None
        VOID114_tree = None
        IDENT115_tree = None
        SEMI118_tree = None
        SEMI121_tree = None
        SEMI123_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_VOID = RewriteRuleTokenStream(self._adaptor, "token VOID")
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_arrayDeclaratorList = RewriteRuleSubtreeStream(self._adaptor, "rule arrayDeclaratorList")
        stream_throwsClause = RewriteRuleSubtreeStream(self._adaptor, "rule throwsClause")
        stream_modifierList = RewriteRuleSubtreeStream(self._adaptor, "rule modifierList")
        stream_genericTypeParameterList = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeParameterList")
        stream_interfaceFieldDeclaratorList = RewriteRuleSubtreeStream(self._adaptor, "rule interfaceFieldDeclaratorList")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        stream_formalParameterList = RewriteRuleSubtreeStream(self._adaptor, "rule formalParameterList")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 26):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:405:5: ( modifierList ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ) | VOID IDENT formalParameterList ( throwsClause )? SEMI -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ) ) | type interfaceFieldDeclaratorList SEMI -> ^( VAR_DECLARATION modifierList type interfaceFieldDeclaratorList ) ) | typeDeclaration | SEMI )
                alt43 = 3
                alt43 = self.dfa43.predict(self.input)
                if alt43 == 1:
                    # Java.g:405:9: modifierList ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ) | VOID IDENT formalParameterList ( throwsClause )? SEMI -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ) ) | type interfaceFieldDeclaratorList SEMI -> ^( VAR_DECLARATION modifierList type interfaceFieldDeclaratorList ) )
                    pass 
                    self._state.following.append(self.FOLLOW_modifierList_in_interfaceScopeDeclarations5979)
                    modifierList106 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_modifierList.add(modifierList106.tree)
                    # Java.g:406:9: ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ) | VOID IDENT formalParameterList ( throwsClause )? SEMI -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ) ) | type interfaceFieldDeclaratorList SEMI -> ^( VAR_DECLARATION modifierList type interfaceFieldDeclaratorList ) )
                    alt42 = 2
                    LA42 = self.input.LA(1)
                    if LA42 == LESS_THAN or LA42 == VOID:
                        alt42 = 1
                    elif LA42 == BOOLEAN or LA42 == BYTE or LA42 == CHAR or LA42 == DOUBLE or LA42 == FLOAT or LA42 == INT or LA42 == LONG or LA42 == SHORT:
                        LA42_2 = self.input.LA(2)

                        if (self.synpred50_Java()) :
                            alt42 = 1
                        elif (True) :
                            alt42 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 42, 2, self.input)

                            raise nvae

                    elif LA42 == IDENT:
                        LA42_3 = self.input.LA(2)

                        if (self.synpred50_Java()) :
                            alt42 = 1
                        elif (True) :
                            alt42 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 42, 3, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 42, 0, self.input)

                        raise nvae

                    if alt42 == 1:
                        # Java.g:406:13: ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ) | VOID IDENT formalParameterList ( throwsClause )? SEMI -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ) )
                        pass 
                        # Java.g:406:13: ( genericTypeParameterList )?
                        alt37 = 2
                        LA37_0 = self.input.LA(1)

                        if (LA37_0 == LESS_THAN) :
                            alt37 = 1
                        if alt37 == 1:
                            # Java.g:0:0: genericTypeParameterList
                            pass 
                            self._state.following.append(self.FOLLOW_genericTypeParameterList_in_interfaceScopeDeclarations5993)
                            genericTypeParameterList107 = self.genericTypeParameterList()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_genericTypeParameterList.add(genericTypeParameterList107.tree)



                        # Java.g:407:13: ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ) | VOID IDENT formalParameterList ( throwsClause )? SEMI -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ) )
                        alt41 = 2
                        LA41_0 = self.input.LA(1)

                        if (LA41_0 == BOOLEAN or LA41_0 == BYTE or LA41_0 == CHAR or LA41_0 == DOUBLE or LA41_0 == FLOAT or (INT <= LA41_0 <= LONG) or LA41_0 == SHORT or LA41_0 == IDENT) :
                            alt41 = 1
                        elif (LA41_0 == VOID) :
                            alt41 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 41, 0, self.input)

                            raise nvae

                        if alt41 == 1:
                            # Java.g:407:17: type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI
                            pass 
                            self._state.following.append(self.FOLLOW_type_in_interfaceScopeDeclarations6012)
                            type108 = self.type()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_type.add(type108.tree)
                            IDENT109=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_interfaceScopeDeclarations6014) 
                            if self._state.backtracking == 0:
                                stream_IDENT.add(IDENT109)
                            self._state.following.append(self.FOLLOW_formalParameterList_in_interfaceScopeDeclarations6016)
                            formalParameterList110 = self.formalParameterList()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_formalParameterList.add(formalParameterList110.tree)
                            # Java.g:407:48: ( arrayDeclaratorList )?
                            alt38 = 2
                            LA38_0 = self.input.LA(1)

                            if (LA38_0 == LBRACK) :
                                alt38 = 1
                            if alt38 == 1:
                                # Java.g:0:0: arrayDeclaratorList
                                pass 
                                self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_interfaceScopeDeclarations6018)
                                arrayDeclaratorList111 = self.arrayDeclaratorList()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    stream_arrayDeclaratorList.add(arrayDeclaratorList111.tree)



                            # Java.g:407:69: ( throwsClause )?
                            alt39 = 2
                            LA39_0 = self.input.LA(1)

                            if (LA39_0 == THROWS) :
                                alt39 = 1
                            if alt39 == 1:
                                # Java.g:0:0: throwsClause
                                pass 
                                self._state.following.append(self.FOLLOW_throwsClause_in_interfaceScopeDeclarations6021)
                                throwsClause112 = self.throwsClause()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    stream_throwsClause.add(throwsClause112.tree)



                            SEMI113=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_interfaceScopeDeclarations6024) 
                            if self._state.backtracking == 0:
                                stream_SEMI.add(SEMI113)

                            # AST Rewrite
                            # elements: genericTypeParameterList, throwsClause, type, IDENT, formalParameterList, modifierList, arrayDeclaratorList
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            if self._state.backtracking == 0:

                                retval.tree = root_0

                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 408:17: -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? )
                                # Java.g:408:21: ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FUNCTION_METHOD_DECL, "FUNCTION_METHOD_DECL"), root_1)

                                self._adaptor.addChild(root_1, stream_modifierList.nextTree())
                                # Java.g:408:57: ( genericTypeParameterList )?
                                if stream_genericTypeParameterList.hasNext():
                                    self._adaptor.addChild(root_1, stream_genericTypeParameterList.nextTree())


                                stream_genericTypeParameterList.reset();
                                self._adaptor.addChild(root_1, stream_type.nextTree())
                                self._adaptor.addChild(root_1, stream_IDENT.nextNode())
                                self._adaptor.addChild(root_1, stream_formalParameterList.nextTree())
                                # Java.g:408:114: ( arrayDeclaratorList )?
                                if stream_arrayDeclaratorList.hasNext():
                                    self._adaptor.addChild(root_1, stream_arrayDeclaratorList.nextTree())


                                stream_arrayDeclaratorList.reset();
                                # Java.g:408:135: ( throwsClause )?
                                if stream_throwsClause.hasNext():
                                    self._adaptor.addChild(root_1, stream_throwsClause.nextTree())


                                stream_throwsClause.reset();

                                self._adaptor.addChild(root_0, root_1)



                                retval.tree = root_0


                        elif alt41 == 2:
                            # Java.g:409:17: VOID IDENT formalParameterList ( throwsClause )? SEMI
                            pass 
                            VOID114=self.match(self.input, VOID, self.FOLLOW_VOID_in_interfaceScopeDeclarations6082) 
                            if self._state.backtracking == 0:
                                stream_VOID.add(VOID114)
                            IDENT115=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_interfaceScopeDeclarations6084) 
                            if self._state.backtracking == 0:
                                stream_IDENT.add(IDENT115)
                            self._state.following.append(self.FOLLOW_formalParameterList_in_interfaceScopeDeclarations6086)
                            formalParameterList116 = self.formalParameterList()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_formalParameterList.add(formalParameterList116.tree)
                            # Java.g:409:48: ( throwsClause )?
                            alt40 = 2
                            LA40_0 = self.input.LA(1)

                            if (LA40_0 == THROWS) :
                                alt40 = 1
                            if alt40 == 1:
                                # Java.g:0:0: throwsClause
                                pass 
                                self._state.following.append(self.FOLLOW_throwsClause_in_interfaceScopeDeclarations6088)
                                throwsClause117 = self.throwsClause()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    stream_throwsClause.add(throwsClause117.tree)



                            SEMI118=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_interfaceScopeDeclarations6091) 
                            if self._state.backtracking == 0:
                                stream_SEMI.add(SEMI118)

                            # AST Rewrite
                            # elements: IDENT, genericTypeParameterList, throwsClause, formalParameterList, modifierList
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            if self._state.backtracking == 0:

                                retval.tree = root_0

                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 410:17: -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? )
                                # Java.g:410:21: ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VOID_METHOD_DECL, "VOID_METHOD_DECL"), root_1)

                                self._adaptor.addChild(root_1, stream_modifierList.nextTree())
                                # Java.g:410:53: ( genericTypeParameterList )?
                                if stream_genericTypeParameterList.hasNext():
                                    self._adaptor.addChild(root_1, stream_genericTypeParameterList.nextTree())


                                stream_genericTypeParameterList.reset();
                                self._adaptor.addChild(root_1, stream_IDENT.nextNode())
                                self._adaptor.addChild(root_1, stream_formalParameterList.nextTree())
                                # Java.g:410:105: ( throwsClause )?
                                if stream_throwsClause.hasNext():
                                    self._adaptor.addChild(root_1, stream_throwsClause.nextTree())


                                stream_throwsClause.reset();

                                self._adaptor.addChild(root_0, root_1)



                                retval.tree = root_0





                    elif alt42 == 2:
                        # Java.g:412:13: type interfaceFieldDeclaratorList SEMI
                        pass 
                        self._state.following.append(self.FOLLOW_type_in_interfaceScopeDeclarations6154)
                        type119 = self.type()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_type.add(type119.tree)
                        self._state.following.append(self.FOLLOW_interfaceFieldDeclaratorList_in_interfaceScopeDeclarations6156)
                        interfaceFieldDeclaratorList120 = self.interfaceFieldDeclaratorList()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_interfaceFieldDeclaratorList.add(interfaceFieldDeclaratorList120.tree)
                        SEMI121=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_interfaceScopeDeclarations6158) 
                        if self._state.backtracking == 0:
                            stream_SEMI.add(SEMI121)

                        # AST Rewrite
                        # elements: type, interfaceFieldDeclaratorList, modifierList
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 413:13: -> ^( VAR_DECLARATION modifierList type interfaceFieldDeclaratorList )
                            # Java.g:413:17: ^( VAR_DECLARATION modifierList type interfaceFieldDeclaratorList )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAR_DECLARATION, "VAR_DECLARATION"), root_1)

                            self._adaptor.addChild(root_1, stream_modifierList.nextTree())
                            self._adaptor.addChild(root_1, stream_type.nextTree())
                            self._adaptor.addChild(root_1, stream_interfaceFieldDeclaratorList.nextTree())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0





                elif alt43 == 2:
                    # Java.g:415:9: typeDeclaration
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_typeDeclaration_in_interfaceScopeDeclarations6203)
                    typeDeclaration122 = self.typeDeclaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, typeDeclaration122.tree)


                elif alt43 == 3:
                    # Java.g:416:9: SEMI
                    pass 
                    root_0 = self._adaptor.nil()

                    SEMI123=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_interfaceScopeDeclarations6213)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 26, interfaceScopeDeclarations_StartIndex, success)

            pass

        return retval

    # $ANTLR end "interfaceScopeDeclarations"

    class classFieldDeclaratorList_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "classFieldDeclaratorList"
    # Java.g:419:1: classFieldDeclaratorList : classFieldDeclarator ( COMMA classFieldDeclarator )* -> ^( VAR_DECLARATOR_LIST ( classFieldDeclarator )+ ) ;
    def classFieldDeclaratorList(self, ):

        retval = self.classFieldDeclaratorList_return()
        retval.start = self.input.LT(1)
        classFieldDeclaratorList_StartIndex = self.input.index()
        root_0 = None

        COMMA125 = None
        classFieldDeclarator124 = None

        classFieldDeclarator126 = None


        COMMA125_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_classFieldDeclarator = RewriteRuleSubtreeStream(self._adaptor, "rule classFieldDeclarator")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 27):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:420:5: ( classFieldDeclarator ( COMMA classFieldDeclarator )* -> ^( VAR_DECLARATOR_LIST ( classFieldDeclarator )+ ) )
                # Java.g:420:9: classFieldDeclarator ( COMMA classFieldDeclarator )*
                pass 
                self._state.following.append(self.FOLLOW_classFieldDeclarator_in_classFieldDeclaratorList6233)
                classFieldDeclarator124 = self.classFieldDeclarator()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_classFieldDeclarator.add(classFieldDeclarator124.tree)
                # Java.g:420:30: ( COMMA classFieldDeclarator )*
                while True: #loop44
                    alt44 = 2
                    LA44_0 = self.input.LA(1)

                    if (LA44_0 == COMMA) :
                        alt44 = 1


                    if alt44 == 1:
                        # Java.g:420:31: COMMA classFieldDeclarator
                        pass 
                        COMMA125=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_classFieldDeclaratorList6236) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA125)
                        self._state.following.append(self.FOLLOW_classFieldDeclarator_in_classFieldDeclaratorList6238)
                        classFieldDeclarator126 = self.classFieldDeclarator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_classFieldDeclarator.add(classFieldDeclarator126.tree)


                    else:
                        break #loop44



                # AST Rewrite
                # elements: classFieldDeclarator
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 421:9: -> ^( VAR_DECLARATOR_LIST ( classFieldDeclarator )+ )
                    # Java.g:421:13: ^( VAR_DECLARATOR_LIST ( classFieldDeclarator )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAR_DECLARATOR_LIST, "VAR_DECLARATOR_LIST"), root_1)

                    # Java.g:421:35: ( classFieldDeclarator )+
                    if not (stream_classFieldDeclarator.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_classFieldDeclarator.hasNext():
                        self._adaptor.addChild(root_1, stream_classFieldDeclarator.nextTree())


                    stream_classFieldDeclarator.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 27, classFieldDeclaratorList_StartIndex, success)

            pass

        return retval

    # $ANTLR end "classFieldDeclaratorList"

    class classFieldDeclarator_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "classFieldDeclarator"
    # Java.g:424:1: classFieldDeclarator : variableDeclaratorId ( ASSIGN variableInitializer )? -> ^( VAR_DECLARATOR variableDeclaratorId ( variableInitializer )? ) ;
    def classFieldDeclarator(self, ):

        retval = self.classFieldDeclarator_return()
        retval.start = self.input.LT(1)
        classFieldDeclarator_StartIndex = self.input.index()
        root_0 = None

        ASSIGN128 = None
        variableDeclaratorId127 = None

        variableInitializer129 = None


        ASSIGN128_tree = None
        stream_ASSIGN = RewriteRuleTokenStream(self._adaptor, "token ASSIGN")
        stream_variableDeclaratorId = RewriteRuleSubtreeStream(self._adaptor, "rule variableDeclaratorId")
        stream_variableInitializer = RewriteRuleSubtreeStream(self._adaptor, "rule variableInitializer")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 28):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:425:5: ( variableDeclaratorId ( ASSIGN variableInitializer )? -> ^( VAR_DECLARATOR variableDeclaratorId ( variableInitializer )? ) )
                # Java.g:425:9: variableDeclaratorId ( ASSIGN variableInitializer )?
                pass 
                self._state.following.append(self.FOLLOW_variableDeclaratorId_in_classFieldDeclarator6277)
                variableDeclaratorId127 = self.variableDeclaratorId()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_variableDeclaratorId.add(variableDeclaratorId127.tree)
                # Java.g:425:30: ( ASSIGN variableInitializer )?
                alt45 = 2
                LA45_0 = self.input.LA(1)

                if (LA45_0 == ASSIGN) :
                    alt45 = 1
                if alt45 == 1:
                    # Java.g:425:31: ASSIGN variableInitializer
                    pass 
                    ASSIGN128=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_classFieldDeclarator6280) 
                    if self._state.backtracking == 0:
                        stream_ASSIGN.add(ASSIGN128)
                    self._state.following.append(self.FOLLOW_variableInitializer_in_classFieldDeclarator6282)
                    variableInitializer129 = self.variableInitializer()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_variableInitializer.add(variableInitializer129.tree)




                # AST Rewrite
                # elements: variableDeclaratorId, variableInitializer
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 426:9: -> ^( VAR_DECLARATOR variableDeclaratorId ( variableInitializer )? )
                    # Java.g:426:13: ^( VAR_DECLARATOR variableDeclaratorId ( variableInitializer )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAR_DECLARATOR, "VAR_DECLARATOR"), root_1)

                    self._adaptor.addChild(root_1, stream_variableDeclaratorId.nextTree())
                    # Java.g:426:51: ( variableInitializer )?
                    if stream_variableInitializer.hasNext():
                        self._adaptor.addChild(root_1, stream_variableInitializer.nextTree())


                    stream_variableInitializer.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 28, classFieldDeclarator_StartIndex, success)

            pass

        return retval

    # $ANTLR end "classFieldDeclarator"

    class interfaceFieldDeclaratorList_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "interfaceFieldDeclaratorList"
    # Java.g:429:1: interfaceFieldDeclaratorList : interfaceFieldDeclarator ( COMMA interfaceFieldDeclarator )* -> ^( VAR_DECLARATOR_LIST ( interfaceFieldDeclarator )+ ) ;
    def interfaceFieldDeclaratorList(self, ):

        retval = self.interfaceFieldDeclaratorList_return()
        retval.start = self.input.LT(1)
        interfaceFieldDeclaratorList_StartIndex = self.input.index()
        root_0 = None

        COMMA131 = None
        interfaceFieldDeclarator130 = None

        interfaceFieldDeclarator132 = None


        COMMA131_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_interfaceFieldDeclarator = RewriteRuleSubtreeStream(self._adaptor, "rule interfaceFieldDeclarator")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 29):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:430:5: ( interfaceFieldDeclarator ( COMMA interfaceFieldDeclarator )* -> ^( VAR_DECLARATOR_LIST ( interfaceFieldDeclarator )+ ) )
                # Java.g:430:9: interfaceFieldDeclarator ( COMMA interfaceFieldDeclarator )*
                pass 
                self._state.following.append(self.FOLLOW_interfaceFieldDeclarator_in_interfaceFieldDeclaratorList6323)
                interfaceFieldDeclarator130 = self.interfaceFieldDeclarator()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_interfaceFieldDeclarator.add(interfaceFieldDeclarator130.tree)
                # Java.g:430:34: ( COMMA interfaceFieldDeclarator )*
                while True: #loop46
                    alt46 = 2
                    LA46_0 = self.input.LA(1)

                    if (LA46_0 == COMMA) :
                        alt46 = 1


                    if alt46 == 1:
                        # Java.g:430:35: COMMA interfaceFieldDeclarator
                        pass 
                        COMMA131=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_interfaceFieldDeclaratorList6326) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA131)
                        self._state.following.append(self.FOLLOW_interfaceFieldDeclarator_in_interfaceFieldDeclaratorList6328)
                        interfaceFieldDeclarator132 = self.interfaceFieldDeclarator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_interfaceFieldDeclarator.add(interfaceFieldDeclarator132.tree)


                    else:
                        break #loop46



                # AST Rewrite
                # elements: interfaceFieldDeclarator
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 431:9: -> ^( VAR_DECLARATOR_LIST ( interfaceFieldDeclarator )+ )
                    # Java.g:431:13: ^( VAR_DECLARATOR_LIST ( interfaceFieldDeclarator )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAR_DECLARATOR_LIST, "VAR_DECLARATOR_LIST"), root_1)

                    # Java.g:431:35: ( interfaceFieldDeclarator )+
                    if not (stream_interfaceFieldDeclarator.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_interfaceFieldDeclarator.hasNext():
                        self._adaptor.addChild(root_1, stream_interfaceFieldDeclarator.nextTree())


                    stream_interfaceFieldDeclarator.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 29, interfaceFieldDeclaratorList_StartIndex, success)

            pass

        return retval

    # $ANTLR end "interfaceFieldDeclaratorList"

    class interfaceFieldDeclarator_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "interfaceFieldDeclarator"
    # Java.g:434:1: interfaceFieldDeclarator : variableDeclaratorId ASSIGN variableInitializer -> ^( VAR_DECLARATOR variableDeclaratorId variableInitializer ) ;
    def interfaceFieldDeclarator(self, ):

        retval = self.interfaceFieldDeclarator_return()
        retval.start = self.input.LT(1)
        interfaceFieldDeclarator_StartIndex = self.input.index()
        root_0 = None

        ASSIGN134 = None
        variableDeclaratorId133 = None

        variableInitializer135 = None


        ASSIGN134_tree = None
        stream_ASSIGN = RewriteRuleTokenStream(self._adaptor, "token ASSIGN")
        stream_variableDeclaratorId = RewriteRuleSubtreeStream(self._adaptor, "rule variableDeclaratorId")
        stream_variableInitializer = RewriteRuleSubtreeStream(self._adaptor, "rule variableInitializer")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 30):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:435:5: ( variableDeclaratorId ASSIGN variableInitializer -> ^( VAR_DECLARATOR variableDeclaratorId variableInitializer ) )
                # Java.g:435:9: variableDeclaratorId ASSIGN variableInitializer
                pass 
                self._state.following.append(self.FOLLOW_variableDeclaratorId_in_interfaceFieldDeclarator6367)
                variableDeclaratorId133 = self.variableDeclaratorId()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_variableDeclaratorId.add(variableDeclaratorId133.tree)
                ASSIGN134=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_interfaceFieldDeclarator6369) 
                if self._state.backtracking == 0:
                    stream_ASSIGN.add(ASSIGN134)
                self._state.following.append(self.FOLLOW_variableInitializer_in_interfaceFieldDeclarator6371)
                variableInitializer135 = self.variableInitializer()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_variableInitializer.add(variableInitializer135.tree)

                # AST Rewrite
                # elements: variableDeclaratorId, variableInitializer
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 436:9: -> ^( VAR_DECLARATOR variableDeclaratorId variableInitializer )
                    # Java.g:436:13: ^( VAR_DECLARATOR variableDeclaratorId variableInitializer )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAR_DECLARATOR, "VAR_DECLARATOR"), root_1)

                    self._adaptor.addChild(root_1, stream_variableDeclaratorId.nextTree())
                    self._adaptor.addChild(root_1, stream_variableInitializer.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 30, interfaceFieldDeclarator_StartIndex, success)

            pass

        return retval

    # $ANTLR end "interfaceFieldDeclarator"

    class variableDeclaratorId_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "variableDeclaratorId"
    # Java.g:439:1: variableDeclaratorId : IDENT ( arrayDeclaratorList )? ;
    def variableDeclaratorId(self, ):

        retval = self.variableDeclaratorId_return()
        retval.start = self.input.LT(1)
        variableDeclaratorId_StartIndex = self.input.index()
        root_0 = None

        IDENT136 = None
        arrayDeclaratorList137 = None


        IDENT136_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 31):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:440:5: ( IDENT ( arrayDeclaratorList )? )
                # Java.g:440:9: IDENT ( arrayDeclaratorList )?
                pass 
                root_0 = self._adaptor.nil()

                IDENT136=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_variableDeclaratorId6409)
                if self._state.backtracking == 0:

                    IDENT136_tree = self._adaptor.createWithPayload(IDENT136)
                    root_0 = self._adaptor.becomeRoot(IDENT136_tree, root_0)

                # Java.g:440:16: ( arrayDeclaratorList )?
                alt47 = 2
                LA47_0 = self.input.LA(1)

                if (LA47_0 == LBRACK) :
                    alt47 = 1
                if alt47 == 1:
                    # Java.g:0:0: arrayDeclaratorList
                    pass 
                    self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_variableDeclaratorId6412)
                    arrayDeclaratorList137 = self.arrayDeclaratorList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, arrayDeclaratorList137.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 31, variableDeclaratorId_StartIndex, success)

            pass

        return retval

    # $ANTLR end "variableDeclaratorId"

    class variableInitializer_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "variableInitializer"
    # Java.g:443:1: variableInitializer : ( arrayInitializer | expression );
    def variableInitializer(self, ):

        retval = self.variableInitializer_return()
        retval.start = self.input.LT(1)
        variableInitializer_StartIndex = self.input.index()
        root_0 = None

        arrayInitializer138 = None

        expression139 = None



        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 32):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:444:5: ( arrayInitializer | expression )
                alt48 = 2
                LA48_0 = self.input.LA(1)

                if (LA48_0 == LCURLY) :
                    alt48 = 1
                elif (LA48_0 == DEC or LA48_0 == INC or LA48_0 == LESS_THAN or LA48_0 == LOGICAL_NOT or (LPAREN <= LA48_0 <= MINUS) or LA48_0 == NOT or LA48_0 == PLUS or LA48_0 == BOOLEAN or LA48_0 == BYTE or LA48_0 == CHAR or LA48_0 == DOUBLE or LA48_0 == FALSE or LA48_0 == FLOAT or (INT <= LA48_0 <= LONG) or (NEW <= LA48_0 <= NULL) or LA48_0 == SHORT or LA48_0 == SUPER or LA48_0 == THIS or LA48_0 == TRUE or LA48_0 == VOID or (IDENT <= LA48_0 <= STRING_LITERAL)) :
                    alt48 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 48, 0, self.input)

                    raise nvae

                if alt48 == 1:
                    # Java.g:444:9: arrayInitializer
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_arrayInitializer_in_variableInitializer6432)
                    arrayInitializer138 = self.arrayInitializer()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, arrayInitializer138.tree)


                elif alt48 == 2:
                    # Java.g:445:9: expression
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_expression_in_variableInitializer6442)
                    expression139 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression139.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 32, variableInitializer_StartIndex, success)

            pass

        return retval

    # $ANTLR end "variableInitializer"

    class arrayDeclarator_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "arrayDeclarator"
    # Java.g:448:1: arrayDeclarator : LBRACK RBRACK -> ^( ARRAY_DECLARATOR ) ;
    def arrayDeclarator(self, ):

        retval = self.arrayDeclarator_return()
        retval.start = self.input.LT(1)
        arrayDeclarator_StartIndex = self.input.index()
        root_0 = None

        LBRACK140 = None
        RBRACK141 = None

        LBRACK140_tree = None
        RBRACK141_tree = None
        stream_RBRACK = RewriteRuleTokenStream(self._adaptor, "token RBRACK")
        stream_LBRACK = RewriteRuleTokenStream(self._adaptor, "token LBRACK")

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 33):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:449:5: ( LBRACK RBRACK -> ^( ARRAY_DECLARATOR ) )
                # Java.g:449:9: LBRACK RBRACK
                pass 
                LBRACK140=self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_arrayDeclarator6461) 
                if self._state.backtracking == 0:
                    stream_LBRACK.add(LBRACK140)
                RBRACK141=self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_arrayDeclarator6463) 
                if self._state.backtracking == 0:
                    stream_RBRACK.add(RBRACK141)

                # AST Rewrite
                # elements: 
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 450:9: -> ^( ARRAY_DECLARATOR )
                    # Java.g:450:13: ^( ARRAY_DECLARATOR )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ARRAY_DECLARATOR, "ARRAY_DECLARATOR"), root_1)

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 33, arrayDeclarator_StartIndex, success)

            pass

        return retval

    # $ANTLR end "arrayDeclarator"

    class arrayDeclaratorList_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "arrayDeclaratorList"
    # Java.g:453:1: arrayDeclaratorList : ( arrayDeclarator )+ -> ^( ARRAY_DECLARATOR_LIST ( arrayDeclarator )+ ) ;
    def arrayDeclaratorList(self, ):

        retval = self.arrayDeclaratorList_return()
        retval.start = self.input.LT(1)
        arrayDeclaratorList_StartIndex = self.input.index()
        root_0 = None

        arrayDeclarator142 = None


        stream_arrayDeclarator = RewriteRuleSubtreeStream(self._adaptor, "rule arrayDeclarator")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 34):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:454:5: ( ( arrayDeclarator )+ -> ^( ARRAY_DECLARATOR_LIST ( arrayDeclarator )+ ) )
                # Java.g:454:9: ( arrayDeclarator )+
                pass 
                # Java.g:454:9: ( arrayDeclarator )+
                cnt49 = 0
                while True: #loop49
                    alt49 = 2
                    LA49_0 = self.input.LA(1)

                    if (LA49_0 == LBRACK) :
                        LA49_2 = self.input.LA(2)

                        if (self.synpred58_Java()) :
                            alt49 = 1




                    if alt49 == 1:
                        # Java.g:0:0: arrayDeclarator
                        pass 
                        self._state.following.append(self.FOLLOW_arrayDeclarator_in_arrayDeclaratorList6497)
                        arrayDeclarator142 = self.arrayDeclarator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_arrayDeclarator.add(arrayDeclarator142.tree)


                    else:
                        if cnt49 >= 1:
                            break #loop49

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(49, self.input)
                        raise eee

                    cnt49 += 1



                # AST Rewrite
                # elements: arrayDeclarator
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 455:9: -> ^( ARRAY_DECLARATOR_LIST ( arrayDeclarator )+ )
                    # Java.g:455:13: ^( ARRAY_DECLARATOR_LIST ( arrayDeclarator )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ARRAY_DECLARATOR_LIST, "ARRAY_DECLARATOR_LIST"), root_1)

                    # Java.g:455:37: ( arrayDeclarator )+
                    if not (stream_arrayDeclarator.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arrayDeclarator.hasNext():
                        self._adaptor.addChild(root_1, stream_arrayDeclarator.nextTree())


                    stream_arrayDeclarator.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 34, arrayDeclaratorList_StartIndex, success)

            pass

        return retval

    # $ANTLR end "arrayDeclaratorList"

    class arrayInitializer_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "arrayInitializer"
    # Java.g:458:1: arrayInitializer : LCURLY ( variableInitializer ( COMMA variableInitializer )* ( COMMA )? )? RCURLY -> ^( ARRAY_INITIALIZER[$LCURLY, \"ARRAY_INITIALIZER\"] ( variableInitializer )* ) ;
    def arrayInitializer(self, ):

        retval = self.arrayInitializer_return()
        retval.start = self.input.LT(1)
        arrayInitializer_StartIndex = self.input.index()
        root_0 = None

        LCURLY143 = None
        COMMA145 = None
        COMMA147 = None
        RCURLY148 = None
        variableInitializer144 = None

        variableInitializer146 = None


        LCURLY143_tree = None
        COMMA145_tree = None
        COMMA147_tree = None
        RCURLY148_tree = None
        stream_LCURLY = RewriteRuleTokenStream(self._adaptor, "token LCURLY")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_RCURLY = RewriteRuleTokenStream(self._adaptor, "token RCURLY")
        stream_variableInitializer = RewriteRuleSubtreeStream(self._adaptor, "rule variableInitializer")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 35):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:459:5: ( LCURLY ( variableInitializer ( COMMA variableInitializer )* ( COMMA )? )? RCURLY -> ^( ARRAY_INITIALIZER[$LCURLY, \"ARRAY_INITIALIZER\"] ( variableInitializer )* ) )
                # Java.g:459:9: LCURLY ( variableInitializer ( COMMA variableInitializer )* ( COMMA )? )? RCURLY
                pass 
                LCURLY143=self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_arrayInitializer6535) 
                if self._state.backtracking == 0:
                    stream_LCURLY.add(LCURLY143)
                # Java.g:459:16: ( variableInitializer ( COMMA variableInitializer )* ( COMMA )? )?
                alt52 = 2
                LA52_0 = self.input.LA(1)

                if (LA52_0 == DEC or LA52_0 == INC or LA52_0 == LCURLY or LA52_0 == LESS_THAN or LA52_0 == LOGICAL_NOT or (LPAREN <= LA52_0 <= MINUS) or LA52_0 == NOT or LA52_0 == PLUS or LA52_0 == BOOLEAN or LA52_0 == BYTE or LA52_0 == CHAR or LA52_0 == DOUBLE or LA52_0 == FALSE or LA52_0 == FLOAT or (INT <= LA52_0 <= LONG) or (NEW <= LA52_0 <= NULL) or LA52_0 == SHORT or LA52_0 == SUPER or LA52_0 == THIS or LA52_0 == TRUE or LA52_0 == VOID or (IDENT <= LA52_0 <= STRING_LITERAL)) :
                    alt52 = 1
                if alt52 == 1:
                    # Java.g:459:17: variableInitializer ( COMMA variableInitializer )* ( COMMA )?
                    pass 
                    self._state.following.append(self.FOLLOW_variableInitializer_in_arrayInitializer6538)
                    variableInitializer144 = self.variableInitializer()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_variableInitializer.add(variableInitializer144.tree)
                    # Java.g:459:37: ( COMMA variableInitializer )*
                    while True: #loop50
                        alt50 = 2
                        LA50_0 = self.input.LA(1)

                        if (LA50_0 == COMMA) :
                            LA50_1 = self.input.LA(2)

                            if (LA50_1 == DEC or LA50_1 == INC or LA50_1 == LCURLY or LA50_1 == LESS_THAN or LA50_1 == LOGICAL_NOT or (LPAREN <= LA50_1 <= MINUS) or LA50_1 == NOT or LA50_1 == PLUS or LA50_1 == BOOLEAN or LA50_1 == BYTE or LA50_1 == CHAR or LA50_1 == DOUBLE or LA50_1 == FALSE or LA50_1 == FLOAT or (INT <= LA50_1 <= LONG) or (NEW <= LA50_1 <= NULL) or LA50_1 == SHORT or LA50_1 == SUPER or LA50_1 == THIS or LA50_1 == TRUE or LA50_1 == VOID or (IDENT <= LA50_1 <= STRING_LITERAL)) :
                                alt50 = 1




                        if alt50 == 1:
                            # Java.g:459:38: COMMA variableInitializer
                            pass 
                            COMMA145=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_arrayInitializer6541) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA145)
                            self._state.following.append(self.FOLLOW_variableInitializer_in_arrayInitializer6543)
                            variableInitializer146 = self.variableInitializer()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_variableInitializer.add(variableInitializer146.tree)


                        else:
                            break #loop50


                    # Java.g:459:66: ( COMMA )?
                    alt51 = 2
                    LA51_0 = self.input.LA(1)

                    if (LA51_0 == COMMA) :
                        alt51 = 1
                    if alt51 == 1:
                        # Java.g:0:0: COMMA
                        pass 
                        COMMA147=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_arrayInitializer6547) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA147)






                RCURLY148=self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_arrayInitializer6552) 
                if self._state.backtracking == 0:
                    stream_RCURLY.add(RCURLY148)

                # AST Rewrite
                # elements: variableInitializer
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 460:9: -> ^( ARRAY_INITIALIZER[$LCURLY, \"ARRAY_INITIALIZER\"] ( variableInitializer )* )
                    # Java.g:460:13: ^( ARRAY_INITIALIZER[$LCURLY, \"ARRAY_INITIALIZER\"] ( variableInitializer )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.create(ARRAY_INITIALIZER, LCURLY143, "ARRAY_INITIALIZER"), root_1)

                    # Java.g:460:63: ( variableInitializer )*
                    while stream_variableInitializer.hasNext():
                        self._adaptor.addChild(root_1, stream_variableInitializer.nextTree())


                    stream_variableInitializer.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 35, arrayInitializer_StartIndex, success)

            pass

        return retval

    # $ANTLR end "arrayInitializer"

    class throwsClause_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "throwsClause"
    # Java.g:463:1: throwsClause : THROWS qualifiedIdentList -> ^( THROWS_CLAUSE[$THROWS, \"THROWS_CLAUSE\"] qualifiedIdentList ) ;
    def throwsClause(self, ):

        retval = self.throwsClause_return()
        retval.start = self.input.LT(1)
        throwsClause_StartIndex = self.input.index()
        root_0 = None

        THROWS149 = None
        qualifiedIdentList150 = None


        THROWS149_tree = None
        stream_THROWS = RewriteRuleTokenStream(self._adaptor, "token THROWS")
        stream_qualifiedIdentList = RewriteRuleSubtreeStream(self._adaptor, "rule qualifiedIdentList")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 36):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:464:5: ( THROWS qualifiedIdentList -> ^( THROWS_CLAUSE[$THROWS, \"THROWS_CLAUSE\"] qualifiedIdentList ) )
                # Java.g:464:9: THROWS qualifiedIdentList
                pass 
                THROWS149=self.match(self.input, THROWS, self.FOLLOW_THROWS_in_throwsClause6590) 
                if self._state.backtracking == 0:
                    stream_THROWS.add(THROWS149)
                self._state.following.append(self.FOLLOW_qualifiedIdentList_in_throwsClause6592)
                qualifiedIdentList150 = self.qualifiedIdentList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_qualifiedIdentList.add(qualifiedIdentList150.tree)

                # AST Rewrite
                # elements: qualifiedIdentList
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 465:9: -> ^( THROWS_CLAUSE[$THROWS, \"THROWS_CLAUSE\"] qualifiedIdentList )
                    # Java.g:465:13: ^( THROWS_CLAUSE[$THROWS, \"THROWS_CLAUSE\"] qualifiedIdentList )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.create(THROWS_CLAUSE, THROWS149, "THROWS_CLAUSE"), root_1)

                    self._adaptor.addChild(root_1, stream_qualifiedIdentList.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 36, throwsClause_StartIndex, success)

            pass

        return retval

    # $ANTLR end "throwsClause"

    class modifierList_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "modifierList"
    # Java.g:468:1: modifierList : ( modifier )* -> ^( MODIFIER_LIST ( modifier )* ) ;
    def modifierList(self, ):

        retval = self.modifierList_return()
        retval.start = self.input.LT(1)
        modifierList_StartIndex = self.input.index()
        root_0 = None

        modifier151 = None


        stream_modifier = RewriteRuleSubtreeStream(self._adaptor, "rule modifier")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 37):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:469:5: ( ( modifier )* -> ^( MODIFIER_LIST ( modifier )* ) )
                # Java.g:469:9: ( modifier )*
                pass 
                # Java.g:469:9: ( modifier )*
                while True: #loop53
                    alt53 = 2
                    LA53_0 = self.input.LA(1)

                    if (LA53_0 == AT) :
                        LA53_2 = self.input.LA(2)

                        if (LA53_2 == IDENT) :
                            alt53 = 1


                    elif (LA53_0 == ABSTRACT or LA53_0 == FINAL or LA53_0 == NATIVE or (PRIVATE <= LA53_0 <= PUBLIC) or (STATIC <= LA53_0 <= STRICTFP) or LA53_0 == SYNCHRONIZED or LA53_0 == TRANSIENT or LA53_0 == VOLATILE) :
                        alt53 = 1


                    if alt53 == 1:
                        # Java.g:0:0: modifier
                        pass 
                        self._state.following.append(self.FOLLOW_modifier_in_modifierList6629)
                        modifier151 = self.modifier()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_modifier.add(modifier151.tree)


                    else:
                        break #loop53



                # AST Rewrite
                # elements: modifier
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 470:9: -> ^( MODIFIER_LIST ( modifier )* )
                    # Java.g:470:13: ^( MODIFIER_LIST ( modifier )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(MODIFIER_LIST, "MODIFIER_LIST"), root_1)

                    # Java.g:470:29: ( modifier )*
                    while stream_modifier.hasNext():
                        self._adaptor.addChild(root_1, stream_modifier.nextTree())


                    stream_modifier.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 37, modifierList_StartIndex, success)

            pass

        return retval

    # $ANTLR end "modifierList"

    class modifier_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "modifier"
    # Java.g:473:1: modifier : ( PUBLIC | PROTECTED | PRIVATE | STATIC | ABSTRACT | NATIVE | SYNCHRONIZED | TRANSIENT | VOLATILE | STRICTFP | localModifier );
    def modifier(self, ):

        retval = self.modifier_return()
        retval.start = self.input.LT(1)
        modifier_StartIndex = self.input.index()
        root_0 = None

        PUBLIC152 = None
        PROTECTED153 = None
        PRIVATE154 = None
        STATIC155 = None
        ABSTRACT156 = None
        NATIVE157 = None
        SYNCHRONIZED158 = None
        TRANSIENT159 = None
        VOLATILE160 = None
        STRICTFP161 = None
        localModifier162 = None


        PUBLIC152_tree = None
        PROTECTED153_tree = None
        PRIVATE154_tree = None
        STATIC155_tree = None
        ABSTRACT156_tree = None
        NATIVE157_tree = None
        SYNCHRONIZED158_tree = None
        TRANSIENT159_tree = None
        VOLATILE160_tree = None
        STRICTFP161_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 38):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:474:5: ( PUBLIC | PROTECTED | PRIVATE | STATIC | ABSTRACT | NATIVE | SYNCHRONIZED | TRANSIENT | VOLATILE | STRICTFP | localModifier )
                alt54 = 11
                LA54 = self.input.LA(1)
                if LA54 == PUBLIC:
                    alt54 = 1
                elif LA54 == PROTECTED:
                    alt54 = 2
                elif LA54 == PRIVATE:
                    alt54 = 3
                elif LA54 == STATIC:
                    alt54 = 4
                elif LA54 == ABSTRACT:
                    alt54 = 5
                elif LA54 == NATIVE:
                    alt54 = 6
                elif LA54 == SYNCHRONIZED:
                    alt54 = 7
                elif LA54 == TRANSIENT:
                    alt54 = 8
                elif LA54 == VOLATILE:
                    alt54 = 9
                elif LA54 == STRICTFP:
                    alt54 = 10
                elif LA54 == AT or LA54 == FINAL:
                    alt54 = 11
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 54, 0, self.input)

                    raise nvae

                if alt54 == 1:
                    # Java.g:474:9: PUBLIC
                    pass 
                    root_0 = self._adaptor.nil()

                    PUBLIC152=self.match(self.input, PUBLIC, self.FOLLOW_PUBLIC_in_modifier6667)
                    if self._state.backtracking == 0:

                        PUBLIC152_tree = self._adaptor.createWithPayload(PUBLIC152)
                        self._adaptor.addChild(root_0, PUBLIC152_tree)



                elif alt54 == 2:
                    # Java.g:475:9: PROTECTED
                    pass 
                    root_0 = self._adaptor.nil()

                    PROTECTED153=self.match(self.input, PROTECTED, self.FOLLOW_PROTECTED_in_modifier6677)
                    if self._state.backtracking == 0:

                        PROTECTED153_tree = self._adaptor.createWithPayload(PROTECTED153)
                        self._adaptor.addChild(root_0, PROTECTED153_tree)



                elif alt54 == 3:
                    # Java.g:476:9: PRIVATE
                    pass 
                    root_0 = self._adaptor.nil()

                    PRIVATE154=self.match(self.input, PRIVATE, self.FOLLOW_PRIVATE_in_modifier6687)
                    if self._state.backtracking == 0:

                        PRIVATE154_tree = self._adaptor.createWithPayload(PRIVATE154)
                        self._adaptor.addChild(root_0, PRIVATE154_tree)



                elif alt54 == 4:
                    # Java.g:477:9: STATIC
                    pass 
                    root_0 = self._adaptor.nil()

                    STATIC155=self.match(self.input, STATIC, self.FOLLOW_STATIC_in_modifier6697)
                    if self._state.backtracking == 0:

                        STATIC155_tree = self._adaptor.createWithPayload(STATIC155)
                        self._adaptor.addChild(root_0, STATIC155_tree)



                elif alt54 == 5:
                    # Java.g:478:9: ABSTRACT
                    pass 
                    root_0 = self._adaptor.nil()

                    ABSTRACT156=self.match(self.input, ABSTRACT, self.FOLLOW_ABSTRACT_in_modifier6707)
                    if self._state.backtracking == 0:

                        ABSTRACT156_tree = self._adaptor.createWithPayload(ABSTRACT156)
                        self._adaptor.addChild(root_0, ABSTRACT156_tree)



                elif alt54 == 6:
                    # Java.g:479:9: NATIVE
                    pass 
                    root_0 = self._adaptor.nil()

                    NATIVE157=self.match(self.input, NATIVE, self.FOLLOW_NATIVE_in_modifier6717)
                    if self._state.backtracking == 0:

                        NATIVE157_tree = self._adaptor.createWithPayload(NATIVE157)
                        self._adaptor.addChild(root_0, NATIVE157_tree)



                elif alt54 == 7:
                    # Java.g:480:9: SYNCHRONIZED
                    pass 
                    root_0 = self._adaptor.nil()

                    SYNCHRONIZED158=self.match(self.input, SYNCHRONIZED, self.FOLLOW_SYNCHRONIZED_in_modifier6727)
                    if self._state.backtracking == 0:

                        SYNCHRONIZED158_tree = self._adaptor.createWithPayload(SYNCHRONIZED158)
                        self._adaptor.addChild(root_0, SYNCHRONIZED158_tree)



                elif alt54 == 8:
                    # Java.g:481:9: TRANSIENT
                    pass 
                    root_0 = self._adaptor.nil()

                    TRANSIENT159=self.match(self.input, TRANSIENT, self.FOLLOW_TRANSIENT_in_modifier6737)
                    if self._state.backtracking == 0:

                        TRANSIENT159_tree = self._adaptor.createWithPayload(TRANSIENT159)
                        self._adaptor.addChild(root_0, TRANSIENT159_tree)



                elif alt54 == 9:
                    # Java.g:482:9: VOLATILE
                    pass 
                    root_0 = self._adaptor.nil()

                    VOLATILE160=self.match(self.input, VOLATILE, self.FOLLOW_VOLATILE_in_modifier6747)
                    if self._state.backtracking == 0:

                        VOLATILE160_tree = self._adaptor.createWithPayload(VOLATILE160)
                        self._adaptor.addChild(root_0, VOLATILE160_tree)



                elif alt54 == 10:
                    # Java.g:483:9: STRICTFP
                    pass 
                    root_0 = self._adaptor.nil()

                    STRICTFP161=self.match(self.input, STRICTFP, self.FOLLOW_STRICTFP_in_modifier6757)
                    if self._state.backtracking == 0:

                        STRICTFP161_tree = self._adaptor.createWithPayload(STRICTFP161)
                        self._adaptor.addChild(root_0, STRICTFP161_tree)



                elif alt54 == 11:
                    # Java.g:484:9: localModifier
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_localModifier_in_modifier6767)
                    localModifier162 = self.localModifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, localModifier162.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 38, modifier_StartIndex, success)

            pass

        return retval

    # $ANTLR end "modifier"

    class localModifierList_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "localModifierList"
    # Java.g:487:1: localModifierList : ( localModifier )* -> ^( LOCAL_MODIFIER_LIST ( localModifier )* ) ;
    def localModifierList(self, ):

        retval = self.localModifierList_return()
        retval.start = self.input.LT(1)
        localModifierList_StartIndex = self.input.index()
        root_0 = None

        localModifier163 = None


        stream_localModifier = RewriteRuleSubtreeStream(self._adaptor, "rule localModifier")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 39):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:488:5: ( ( localModifier )* -> ^( LOCAL_MODIFIER_LIST ( localModifier )* ) )
                # Java.g:488:9: ( localModifier )*
                pass 
                # Java.g:488:9: ( localModifier )*
                while True: #loop55
                    alt55 = 2
                    LA55_0 = self.input.LA(1)

                    if (LA55_0 == AT or LA55_0 == FINAL) :
                        alt55 = 1


                    if alt55 == 1:
                        # Java.g:0:0: localModifier
                        pass 
                        self._state.following.append(self.FOLLOW_localModifier_in_localModifierList6786)
                        localModifier163 = self.localModifier()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_localModifier.add(localModifier163.tree)


                    else:
                        break #loop55



                # AST Rewrite
                # elements: localModifier
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 489:9: -> ^( LOCAL_MODIFIER_LIST ( localModifier )* )
                    # Java.g:489:12: ^( LOCAL_MODIFIER_LIST ( localModifier )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LOCAL_MODIFIER_LIST, "LOCAL_MODIFIER_LIST"), root_1)

                    # Java.g:489:34: ( localModifier )*
                    while stream_localModifier.hasNext():
                        self._adaptor.addChild(root_1, stream_localModifier.nextTree())


                    stream_localModifier.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 39, localModifierList_StartIndex, success)

            pass

        return retval

    # $ANTLR end "localModifierList"

    class localModifier_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "localModifier"
    # Java.g:492:1: localModifier : ( FINAL | annotation );
    def localModifier(self, ):

        retval = self.localModifier_return()
        retval.start = self.input.LT(1)
        localModifier_StartIndex = self.input.index()
        root_0 = None

        FINAL164 = None
        annotation165 = None


        FINAL164_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 40):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:493:5: ( FINAL | annotation )
                alt56 = 2
                LA56_0 = self.input.LA(1)

                if (LA56_0 == FINAL) :
                    alt56 = 1
                elif (LA56_0 == AT) :
                    alt56 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 56, 0, self.input)

                    raise nvae

                if alt56 == 1:
                    # Java.g:493:9: FINAL
                    pass 
                    root_0 = self._adaptor.nil()

                    FINAL164=self.match(self.input, FINAL, self.FOLLOW_FINAL_in_localModifier6823)
                    if self._state.backtracking == 0:

                        FINAL164_tree = self._adaptor.createWithPayload(FINAL164)
                        self._adaptor.addChild(root_0, FINAL164_tree)



                elif alt56 == 2:
                    # Java.g:494:9: annotation
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_annotation_in_localModifier6833)
                    annotation165 = self.annotation()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, annotation165.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 40, localModifier_StartIndex, success)

            pass

        return retval

    # $ANTLR end "localModifier"

    class type_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "type"
    # Java.g:497:1: type : ( simpleType | objectType );
    def type(self, ):

        retval = self.type_return()
        retval.start = self.input.LT(1)
        type_StartIndex = self.input.index()
        root_0 = None

        simpleType166 = None

        objectType167 = None



        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 41):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:498:5: ( simpleType | objectType )
                alt57 = 2
                LA57_0 = self.input.LA(1)

                if (LA57_0 == BOOLEAN or LA57_0 == BYTE or LA57_0 == CHAR or LA57_0 == DOUBLE or LA57_0 == FLOAT or (INT <= LA57_0 <= LONG) or LA57_0 == SHORT) :
                    alt57 = 1
                elif (LA57_0 == IDENT) :
                    alt57 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 57, 0, self.input)

                    raise nvae

                if alt57 == 1:
                    # Java.g:498:9: simpleType
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_simpleType_in_type6852)
                    simpleType166 = self.simpleType()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, simpleType166.tree)


                elif alt57 == 2:
                    # Java.g:499:9: objectType
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_objectType_in_type6862)
                    objectType167 = self.objectType()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, objectType167.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 41, type_StartIndex, success)

            pass

        return retval

    # $ANTLR end "type"

    class simpleType_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "simpleType"
    # Java.g:502:1: simpleType : primitiveType ( arrayDeclaratorList )? -> ^( TYPE primitiveType ( arrayDeclaratorList )? ) ;
    def simpleType(self, ):

        retval = self.simpleType_return()
        retval.start = self.input.LT(1)
        simpleType_StartIndex = self.input.index()
        root_0 = None

        primitiveType168 = None

        arrayDeclaratorList169 = None


        stream_arrayDeclaratorList = RewriteRuleSubtreeStream(self._adaptor, "rule arrayDeclaratorList")
        stream_primitiveType = RewriteRuleSubtreeStream(self._adaptor, "rule primitiveType")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 42):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:503:5: ( primitiveType ( arrayDeclaratorList )? -> ^( TYPE primitiveType ( arrayDeclaratorList )? ) )
                # Java.g:503:9: primitiveType ( arrayDeclaratorList )?
                pass 
                self._state.following.append(self.FOLLOW_primitiveType_in_simpleType6882)
                primitiveType168 = self.primitiveType()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_primitiveType.add(primitiveType168.tree)
                # Java.g:503:23: ( arrayDeclaratorList )?
                alt58 = 2
                LA58_0 = self.input.LA(1)

                if (LA58_0 == LBRACK) :
                    LA58_1 = self.input.LA(2)

                    if (LA58_1 == RBRACK) :
                        LA58_3 = self.input.LA(3)

                        if (self.synpred76_Java()) :
                            alt58 = 1
                if alt58 == 1:
                    # Java.g:0:0: arrayDeclaratorList
                    pass 
                    self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_simpleType6884)
                    arrayDeclaratorList169 = self.arrayDeclaratorList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_arrayDeclaratorList.add(arrayDeclaratorList169.tree)




                # AST Rewrite
                # elements: arrayDeclaratorList, primitiveType
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 504:9: -> ^( TYPE primitiveType ( arrayDeclaratorList )? )
                    # Java.g:504:13: ^( TYPE primitiveType ( arrayDeclaratorList )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TYPE, "TYPE"), root_1)

                    self._adaptor.addChild(root_1, stream_primitiveType.nextTree())
                    # Java.g:504:34: ( arrayDeclaratorList )?
                    if stream_arrayDeclaratorList.hasNext():
                        self._adaptor.addChild(root_1, stream_arrayDeclaratorList.nextTree())


                    stream_arrayDeclaratorList.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 42, simpleType_StartIndex, success)

            pass

        return retval

    # $ANTLR end "simpleType"

    class objectType_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "objectType"
    # Java.g:507:1: objectType : qualifiedTypeIdent ( arrayDeclaratorList )? -> ^( TYPE qualifiedTypeIdent ( arrayDeclaratorList )? ) ;
    def objectType(self, ):

        retval = self.objectType_return()
        retval.start = self.input.LT(1)
        objectType_StartIndex = self.input.index()
        root_0 = None

        qualifiedTypeIdent170 = None

        arrayDeclaratorList171 = None


        stream_arrayDeclaratorList = RewriteRuleSubtreeStream(self._adaptor, "rule arrayDeclaratorList")
        stream_qualifiedTypeIdent = RewriteRuleSubtreeStream(self._adaptor, "rule qualifiedTypeIdent")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 43):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:508:5: ( qualifiedTypeIdent ( arrayDeclaratorList )? -> ^( TYPE qualifiedTypeIdent ( arrayDeclaratorList )? ) )
                # Java.g:508:9: qualifiedTypeIdent ( arrayDeclaratorList )?
                pass 
                self._state.following.append(self.FOLLOW_qualifiedTypeIdent_in_objectType6925)
                qualifiedTypeIdent170 = self.qualifiedTypeIdent()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_qualifiedTypeIdent.add(qualifiedTypeIdent170.tree)
                # Java.g:508:28: ( arrayDeclaratorList )?
                alt59 = 2
                LA59_0 = self.input.LA(1)

                if (LA59_0 == LBRACK) :
                    LA59_1 = self.input.LA(2)

                    if (self.synpred77_Java()) :
                        alt59 = 1
                if alt59 == 1:
                    # Java.g:0:0: arrayDeclaratorList
                    pass 
                    self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_objectType6927)
                    arrayDeclaratorList171 = self.arrayDeclaratorList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_arrayDeclaratorList.add(arrayDeclaratorList171.tree)




                # AST Rewrite
                # elements: qualifiedTypeIdent, arrayDeclaratorList
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 509:9: -> ^( TYPE qualifiedTypeIdent ( arrayDeclaratorList )? )
                    # Java.g:509:13: ^( TYPE qualifiedTypeIdent ( arrayDeclaratorList )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TYPE, "TYPE"), root_1)

                    self._adaptor.addChild(root_1, stream_qualifiedTypeIdent.nextTree())
                    # Java.g:509:39: ( arrayDeclaratorList )?
                    if stream_arrayDeclaratorList.hasNext():
                        self._adaptor.addChild(root_1, stream_arrayDeclaratorList.nextTree())


                    stream_arrayDeclaratorList.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 43, objectType_StartIndex, success)

            pass

        return retval

    # $ANTLR end "objectType"

    class objectTypeSimplified_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "objectTypeSimplified"
    # Java.g:512:1: objectTypeSimplified : qualifiedTypeIdentSimplified ( arrayDeclaratorList )? -> ^( TYPE qualifiedTypeIdentSimplified ( arrayDeclaratorList )? ) ;
    def objectTypeSimplified(self, ):

        retval = self.objectTypeSimplified_return()
        retval.start = self.input.LT(1)
        objectTypeSimplified_StartIndex = self.input.index()
        root_0 = None

        qualifiedTypeIdentSimplified172 = None

        arrayDeclaratorList173 = None


        stream_arrayDeclaratorList = RewriteRuleSubtreeStream(self._adaptor, "rule arrayDeclaratorList")
        stream_qualifiedTypeIdentSimplified = RewriteRuleSubtreeStream(self._adaptor, "rule qualifiedTypeIdentSimplified")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 44):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:513:5: ( qualifiedTypeIdentSimplified ( arrayDeclaratorList )? -> ^( TYPE qualifiedTypeIdentSimplified ( arrayDeclaratorList )? ) )
                # Java.g:513:9: qualifiedTypeIdentSimplified ( arrayDeclaratorList )?
                pass 
                self._state.following.append(self.FOLLOW_qualifiedTypeIdentSimplified_in_objectTypeSimplified6967)
                qualifiedTypeIdentSimplified172 = self.qualifiedTypeIdentSimplified()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_qualifiedTypeIdentSimplified.add(qualifiedTypeIdentSimplified172.tree)
                # Java.g:513:38: ( arrayDeclaratorList )?
                alt60 = 2
                LA60_0 = self.input.LA(1)

                if (LA60_0 == LBRACK) :
                    alt60 = 1
                if alt60 == 1:
                    # Java.g:0:0: arrayDeclaratorList
                    pass 
                    self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_objectTypeSimplified6969)
                    arrayDeclaratorList173 = self.arrayDeclaratorList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_arrayDeclaratorList.add(arrayDeclaratorList173.tree)




                # AST Rewrite
                # elements: qualifiedTypeIdentSimplified, arrayDeclaratorList
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 514:9: -> ^( TYPE qualifiedTypeIdentSimplified ( arrayDeclaratorList )? )
                    # Java.g:514:13: ^( TYPE qualifiedTypeIdentSimplified ( arrayDeclaratorList )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TYPE, "TYPE"), root_1)

                    self._adaptor.addChild(root_1, stream_qualifiedTypeIdentSimplified.nextTree())
                    # Java.g:514:49: ( arrayDeclaratorList )?
                    if stream_arrayDeclaratorList.hasNext():
                        self._adaptor.addChild(root_1, stream_arrayDeclaratorList.nextTree())


                    stream_arrayDeclaratorList.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 44, objectTypeSimplified_StartIndex, success)

            pass

        return retval

    # $ANTLR end "objectTypeSimplified"

    class qualifiedTypeIdent_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "qualifiedTypeIdent"
    # Java.g:517:1: qualifiedTypeIdent : typeIdent ( DOT typeIdent )* -> ^( QUALIFIED_TYPE_IDENT ( typeIdent )+ ) ;
    def qualifiedTypeIdent(self, ):

        retval = self.qualifiedTypeIdent_return()
        retval.start = self.input.LT(1)
        qualifiedTypeIdent_StartIndex = self.input.index()
        root_0 = None

        DOT175 = None
        typeIdent174 = None

        typeIdent176 = None


        DOT175_tree = None
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_typeIdent = RewriteRuleSubtreeStream(self._adaptor, "rule typeIdent")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 45):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:518:5: ( typeIdent ( DOT typeIdent )* -> ^( QUALIFIED_TYPE_IDENT ( typeIdent )+ ) )
                # Java.g:518:9: typeIdent ( DOT typeIdent )*
                pass 
                self._state.following.append(self.FOLLOW_typeIdent_in_qualifiedTypeIdent7009)
                typeIdent174 = self.typeIdent()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_typeIdent.add(typeIdent174.tree)
                # Java.g:518:19: ( DOT typeIdent )*
                while True: #loop61
                    alt61 = 2
                    LA61_0 = self.input.LA(1)

                    if (LA61_0 == DOT) :
                        LA61_2 = self.input.LA(2)

                        if (self.synpred79_Java()) :
                            alt61 = 1




                    if alt61 == 1:
                        # Java.g:518:20: DOT typeIdent
                        pass 
                        DOT175=self.match(self.input, DOT, self.FOLLOW_DOT_in_qualifiedTypeIdent7012) 
                        if self._state.backtracking == 0:
                            stream_DOT.add(DOT175)
                        self._state.following.append(self.FOLLOW_typeIdent_in_qualifiedTypeIdent7014)
                        typeIdent176 = self.typeIdent()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_typeIdent.add(typeIdent176.tree)


                    else:
                        break #loop61



                # AST Rewrite
                # elements: typeIdent
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 519:9: -> ^( QUALIFIED_TYPE_IDENT ( typeIdent )+ )
                    # Java.g:519:13: ^( QUALIFIED_TYPE_IDENT ( typeIdent )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(QUALIFIED_TYPE_IDENT, "QUALIFIED_TYPE_IDENT"), root_1)

                    # Java.g:519:36: ( typeIdent )+
                    if not (stream_typeIdent.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_typeIdent.hasNext():
                        self._adaptor.addChild(root_1, stream_typeIdent.nextTree())


                    stream_typeIdent.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 45, qualifiedTypeIdent_StartIndex, success)

            pass

        return retval

    # $ANTLR end "qualifiedTypeIdent"

    class qualifiedTypeIdentSimplified_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "qualifiedTypeIdentSimplified"
    # Java.g:522:1: qualifiedTypeIdentSimplified : typeIdentSimplified ( DOT typeIdentSimplified )* -> ^( QUALIFIED_TYPE_IDENT ( typeIdentSimplified )+ ) ;
    def qualifiedTypeIdentSimplified(self, ):

        retval = self.qualifiedTypeIdentSimplified_return()
        retval.start = self.input.LT(1)
        qualifiedTypeIdentSimplified_StartIndex = self.input.index()
        root_0 = None

        DOT178 = None
        typeIdentSimplified177 = None

        typeIdentSimplified179 = None


        DOT178_tree = None
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_typeIdentSimplified = RewriteRuleSubtreeStream(self._adaptor, "rule typeIdentSimplified")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 46):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:523:5: ( typeIdentSimplified ( DOT typeIdentSimplified )* -> ^( QUALIFIED_TYPE_IDENT ( typeIdentSimplified )+ ) )
                # Java.g:523:9: typeIdentSimplified ( DOT typeIdentSimplified )*
                pass 
                self._state.following.append(self.FOLLOW_typeIdentSimplified_in_qualifiedTypeIdentSimplified7053)
                typeIdentSimplified177 = self.typeIdentSimplified()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_typeIdentSimplified.add(typeIdentSimplified177.tree)
                # Java.g:523:29: ( DOT typeIdentSimplified )*
                while True: #loop62
                    alt62 = 2
                    LA62_0 = self.input.LA(1)

                    if (LA62_0 == DOT) :
                        alt62 = 1


                    if alt62 == 1:
                        # Java.g:523:30: DOT typeIdentSimplified
                        pass 
                        DOT178=self.match(self.input, DOT, self.FOLLOW_DOT_in_qualifiedTypeIdentSimplified7056) 
                        if self._state.backtracking == 0:
                            stream_DOT.add(DOT178)
                        self._state.following.append(self.FOLLOW_typeIdentSimplified_in_qualifiedTypeIdentSimplified7058)
                        typeIdentSimplified179 = self.typeIdentSimplified()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_typeIdentSimplified.add(typeIdentSimplified179.tree)


                    else:
                        break #loop62



                # AST Rewrite
                # elements: typeIdentSimplified
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 524:9: -> ^( QUALIFIED_TYPE_IDENT ( typeIdentSimplified )+ )
                    # Java.g:524:13: ^( QUALIFIED_TYPE_IDENT ( typeIdentSimplified )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(QUALIFIED_TYPE_IDENT, "QUALIFIED_TYPE_IDENT"), root_1)

                    # Java.g:524:36: ( typeIdentSimplified )+
                    if not (stream_typeIdentSimplified.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_typeIdentSimplified.hasNext():
                        self._adaptor.addChild(root_1, stream_typeIdentSimplified.nextTree())


                    stream_typeIdentSimplified.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 46, qualifiedTypeIdentSimplified_StartIndex, success)

            pass

        return retval

    # $ANTLR end "qualifiedTypeIdentSimplified"

    class typeIdent_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "typeIdent"
    # Java.g:527:1: typeIdent : IDENT ( genericTypeArgumentList )? ;
    def typeIdent(self, ):

        retval = self.typeIdent_return()
        retval.start = self.input.LT(1)
        typeIdent_StartIndex = self.input.index()
        root_0 = None

        IDENT180 = None
        genericTypeArgumentList181 = None


        IDENT180_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 47):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:528:5: ( IDENT ( genericTypeArgumentList )? )
                # Java.g:528:9: IDENT ( genericTypeArgumentList )?
                pass 
                root_0 = self._adaptor.nil()

                IDENT180=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_typeIdent7097)
                if self._state.backtracking == 0:

                    IDENT180_tree = self._adaptor.createWithPayload(IDENT180)
                    root_0 = self._adaptor.becomeRoot(IDENT180_tree, root_0)

                # Java.g:528:16: ( genericTypeArgumentList )?
                alt63 = 2
                LA63_0 = self.input.LA(1)

                if (LA63_0 == LESS_THAN) :
                    alt63 = 1
                if alt63 == 1:
                    # Java.g:0:0: genericTypeArgumentList
                    pass 
                    self._state.following.append(self.FOLLOW_genericTypeArgumentList_in_typeIdent7100)
                    genericTypeArgumentList181 = self.genericTypeArgumentList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, genericTypeArgumentList181.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 47, typeIdent_StartIndex, success)

            pass

        return retval

    # $ANTLR end "typeIdent"

    class typeIdentSimplified_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "typeIdentSimplified"
    # Java.g:531:1: typeIdentSimplified : IDENT ( genericTypeArgumentListSimplified )? ;
    def typeIdentSimplified(self, ):

        retval = self.typeIdentSimplified_return()
        retval.start = self.input.LT(1)
        typeIdentSimplified_StartIndex = self.input.index()
        root_0 = None

        IDENT182 = None
        genericTypeArgumentListSimplified183 = None


        IDENT182_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 48):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:532:5: ( IDENT ( genericTypeArgumentListSimplified )? )
                # Java.g:532:9: IDENT ( genericTypeArgumentListSimplified )?
                pass 
                root_0 = self._adaptor.nil()

                IDENT182=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_typeIdentSimplified7120)
                if self._state.backtracking == 0:

                    IDENT182_tree = self._adaptor.createWithPayload(IDENT182)
                    root_0 = self._adaptor.becomeRoot(IDENT182_tree, root_0)

                # Java.g:532:16: ( genericTypeArgumentListSimplified )?
                alt64 = 2
                LA64_0 = self.input.LA(1)

                if (LA64_0 == LESS_THAN) :
                    alt64 = 1
                if alt64 == 1:
                    # Java.g:0:0: genericTypeArgumentListSimplified
                    pass 
                    self._state.following.append(self.FOLLOW_genericTypeArgumentListSimplified_in_typeIdentSimplified7123)
                    genericTypeArgumentListSimplified183 = self.genericTypeArgumentListSimplified()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, genericTypeArgumentListSimplified183.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 48, typeIdentSimplified_StartIndex, success)

            pass

        return retval

    # $ANTLR end "typeIdentSimplified"

    class primitiveType_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "primitiveType"
    # Java.g:535:1: primitiveType : ( BOOLEAN | CHAR | BYTE | SHORT | INT | LONG | FLOAT | DOUBLE );
    def primitiveType(self, ):

        retval = self.primitiveType_return()
        retval.start = self.input.LT(1)
        primitiveType_StartIndex = self.input.index()
        root_0 = None

        set184 = None

        set184_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 49):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:536:5: ( BOOLEAN | CHAR | BYTE | SHORT | INT | LONG | FLOAT | DOUBLE )
                # Java.g:
                pass 
                root_0 = self._adaptor.nil()

                set184 = self.input.LT(1)
                if self.input.LA(1) == BOOLEAN or self.input.LA(1) == BYTE or self.input.LA(1) == CHAR or self.input.LA(1) == DOUBLE or self.input.LA(1) == FLOAT or (INT <= self.input.LA(1) <= LONG) or self.input.LA(1) == SHORT:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set184))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 49, primitiveType_StartIndex, success)

            pass

        return retval

    # $ANTLR end "primitiveType"

    class genericTypeArgumentList_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "genericTypeArgumentList"
    # Java.g:546:1: genericTypeArgumentList : LESS_THAN genericTypeArgument ( COMMA genericTypeArgument )* genericTypeListClosing -> ^( GENERIC_TYPE_ARG_LIST[$LESS_THAN, \"GENERIC_TYPE_ARG_LIST\"] ( genericTypeArgument )+ ) ;
    def genericTypeArgumentList(self, ):

        retval = self.genericTypeArgumentList_return()
        retval.start = self.input.LT(1)
        genericTypeArgumentList_StartIndex = self.input.index()
        root_0 = None

        LESS_THAN185 = None
        COMMA187 = None
        genericTypeArgument186 = None

        genericTypeArgument188 = None

        genericTypeListClosing189 = None


        LESS_THAN185_tree = None
        COMMA187_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LESS_THAN = RewriteRuleTokenStream(self._adaptor, "token LESS_THAN")
        stream_genericTypeArgument = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeArgument")
        stream_genericTypeListClosing = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeListClosing")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 50):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:547:5: ( LESS_THAN genericTypeArgument ( COMMA genericTypeArgument )* genericTypeListClosing -> ^( GENERIC_TYPE_ARG_LIST[$LESS_THAN, \"GENERIC_TYPE_ARG_LIST\"] ( genericTypeArgument )+ ) )
                # Java.g:547:9: LESS_THAN genericTypeArgument ( COMMA genericTypeArgument )* genericTypeListClosing
                pass 
                LESS_THAN185=self.match(self.input, LESS_THAN, self.FOLLOW_LESS_THAN_in_genericTypeArgumentList7232) 
                if self._state.backtracking == 0:
                    stream_LESS_THAN.add(LESS_THAN185)
                self._state.following.append(self.FOLLOW_genericTypeArgument_in_genericTypeArgumentList7234)
                genericTypeArgument186 = self.genericTypeArgument()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_genericTypeArgument.add(genericTypeArgument186.tree)
                # Java.g:547:39: ( COMMA genericTypeArgument )*
                while True: #loop65
                    alt65 = 2
                    LA65_0 = self.input.LA(1)

                    if (LA65_0 == COMMA) :
                        LA65_2 = self.input.LA(2)

                        if (self.synpred90_Java()) :
                            alt65 = 1




                    if alt65 == 1:
                        # Java.g:547:40: COMMA genericTypeArgument
                        pass 
                        COMMA187=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_genericTypeArgumentList7237) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA187)
                        self._state.following.append(self.FOLLOW_genericTypeArgument_in_genericTypeArgumentList7239)
                        genericTypeArgument188 = self.genericTypeArgument()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_genericTypeArgument.add(genericTypeArgument188.tree)


                    else:
                        break #loop65


                self._state.following.append(self.FOLLOW_genericTypeListClosing_in_genericTypeArgumentList7243)
                genericTypeListClosing189 = self.genericTypeListClosing()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_genericTypeListClosing.add(genericTypeListClosing189.tree)

                # AST Rewrite
                # elements: genericTypeArgument
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 548:9: -> ^( GENERIC_TYPE_ARG_LIST[$LESS_THAN, \"GENERIC_TYPE_ARG_LIST\"] ( genericTypeArgument )+ )
                    # Java.g:548:13: ^( GENERIC_TYPE_ARG_LIST[$LESS_THAN, \"GENERIC_TYPE_ARG_LIST\"] ( genericTypeArgument )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.create(GENERIC_TYPE_ARG_LIST, LESS_THAN185, "GENERIC_TYPE_ARG_LIST"), root_1)

                    # Java.g:548:74: ( genericTypeArgument )+
                    if not (stream_genericTypeArgument.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_genericTypeArgument.hasNext():
                        self._adaptor.addChild(root_1, stream_genericTypeArgument.nextTree())


                    stream_genericTypeArgument.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 50, genericTypeArgumentList_StartIndex, success)

            pass

        return retval

    # $ANTLR end "genericTypeArgumentList"

    class genericTypeArgument_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "genericTypeArgument"
    # Java.g:551:1: genericTypeArgument : ( type | QUESTION ( genericWildcardBoundType )? -> ^( QUESTION ( genericWildcardBoundType )? ) );
    def genericTypeArgument(self, ):

        retval = self.genericTypeArgument_return()
        retval.start = self.input.LT(1)
        genericTypeArgument_StartIndex = self.input.index()
        root_0 = None

        QUESTION191 = None
        type190 = None

        genericWildcardBoundType192 = None


        QUESTION191_tree = None
        stream_QUESTION = RewriteRuleTokenStream(self._adaptor, "token QUESTION")
        stream_genericWildcardBoundType = RewriteRuleSubtreeStream(self._adaptor, "rule genericWildcardBoundType")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 51):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:552:5: ( type | QUESTION ( genericWildcardBoundType )? -> ^( QUESTION ( genericWildcardBoundType )? ) )
                alt67 = 2
                LA67_0 = self.input.LA(1)

                if (LA67_0 == BOOLEAN or LA67_0 == BYTE or LA67_0 == CHAR or LA67_0 == DOUBLE or LA67_0 == FLOAT or (INT <= LA67_0 <= LONG) or LA67_0 == SHORT or LA67_0 == IDENT) :
                    alt67 = 1
                elif (LA67_0 == QUESTION) :
                    alt67 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 67, 0, self.input)

                    raise nvae

                if alt67 == 1:
                    # Java.g:552:9: type
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_type_in_genericTypeArgument7281)
                    type190 = self.type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, type190.tree)


                elif alt67 == 2:
                    # Java.g:553:9: QUESTION ( genericWildcardBoundType )?
                    pass 
                    QUESTION191=self.match(self.input, QUESTION, self.FOLLOW_QUESTION_in_genericTypeArgument7291) 
                    if self._state.backtracking == 0:
                        stream_QUESTION.add(QUESTION191)
                    # Java.g:553:18: ( genericWildcardBoundType )?
                    alt66 = 2
                    LA66_0 = self.input.LA(1)

                    if (LA66_0 == EXTENDS) :
                        LA66_1 = self.input.LA(2)

                        if (LA66_1 == BOOLEAN or LA66_1 == BYTE or LA66_1 == CHAR or LA66_1 == DOUBLE or LA66_1 == FLOAT or (INT <= LA66_1 <= LONG) or LA66_1 == SHORT) :
                            LA66_4 = self.input.LA(3)

                            if (self.synpred92_Java()) :
                                alt66 = 1
                        elif (LA66_1 == IDENT) :
                            LA66_5 = self.input.LA(3)

                            if (self.synpred92_Java()) :
                                alt66 = 1
                    elif (LA66_0 == SUPER) :
                        LA66_3 = self.input.LA(2)

                        if (LA66_3 == BOOLEAN or LA66_3 == BYTE or LA66_3 == CHAR or LA66_3 == DOUBLE or LA66_3 == FLOAT or (INT <= LA66_3 <= LONG) or LA66_3 == SHORT or LA66_3 == IDENT) :
                            alt66 = 1
                    if alt66 == 1:
                        # Java.g:0:0: genericWildcardBoundType
                        pass 
                        self._state.following.append(self.FOLLOW_genericWildcardBoundType_in_genericTypeArgument7293)
                        genericWildcardBoundType192 = self.genericWildcardBoundType()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_genericWildcardBoundType.add(genericWildcardBoundType192.tree)




                    # AST Rewrite
                    # elements: genericWildcardBoundType, QUESTION
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 554:9: -> ^( QUESTION ( genericWildcardBoundType )? )
                        # Java.g:554:13: ^( QUESTION ( genericWildcardBoundType )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_QUESTION.nextNode(), root_1)

                        # Java.g:554:24: ( genericWildcardBoundType )?
                        if stream_genericWildcardBoundType.hasNext():
                            self._adaptor.addChild(root_1, stream_genericWildcardBoundType.nextTree())


                        stream_genericWildcardBoundType.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 51, genericTypeArgument_StartIndex, success)

            pass

        return retval

    # $ANTLR end "genericTypeArgument"

    class genericWildcardBoundType_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "genericWildcardBoundType"
    # Java.g:557:1: genericWildcardBoundType : ( EXTENDS | SUPER ) type ;
    def genericWildcardBoundType(self, ):

        retval = self.genericWildcardBoundType_return()
        retval.start = self.input.LT(1)
        genericWildcardBoundType_StartIndex = self.input.index()
        root_0 = None

        set193 = None
        type194 = None


        set193_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 52):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:558:5: ( ( EXTENDS | SUPER ) type )
                # Java.g:558:9: ( EXTENDS | SUPER ) type
                pass 
                root_0 = self._adaptor.nil()

                set193 = self.input.LT(1)
                set193 = self.input.LT(1)
                if self.input.LA(1) == EXTENDS or self.input.LA(1) == SUPER:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set193), root_0)
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse


                self._state.following.append(self.FOLLOW_type_in_genericWildcardBoundType7340)
                type194 = self.type()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, type194.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 52, genericWildcardBoundType_StartIndex, success)

            pass

        return retval

    # $ANTLR end "genericWildcardBoundType"

    class genericTypeArgumentListSimplified_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "genericTypeArgumentListSimplified"
    # Java.g:561:1: genericTypeArgumentListSimplified : LESS_THAN genericTypeArgumentSimplified ( COMMA genericTypeArgumentSimplified )* genericTypeListClosing -> ^( GENERIC_TYPE_ARG_LIST[$LESS_THAN, \"GENERIC_TYPE_ARG_LIST\"] ( genericTypeArgumentSimplified )+ ) ;
    def genericTypeArgumentListSimplified(self, ):

        retval = self.genericTypeArgumentListSimplified_return()
        retval.start = self.input.LT(1)
        genericTypeArgumentListSimplified_StartIndex = self.input.index()
        root_0 = None

        LESS_THAN195 = None
        COMMA197 = None
        genericTypeArgumentSimplified196 = None

        genericTypeArgumentSimplified198 = None

        genericTypeListClosing199 = None


        LESS_THAN195_tree = None
        COMMA197_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LESS_THAN = RewriteRuleTokenStream(self._adaptor, "token LESS_THAN")
        stream_genericTypeArgumentSimplified = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeArgumentSimplified")
        stream_genericTypeListClosing = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeListClosing")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 53):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:562:5: ( LESS_THAN genericTypeArgumentSimplified ( COMMA genericTypeArgumentSimplified )* genericTypeListClosing -> ^( GENERIC_TYPE_ARG_LIST[$LESS_THAN, \"GENERIC_TYPE_ARG_LIST\"] ( genericTypeArgumentSimplified )+ ) )
                # Java.g:562:9: LESS_THAN genericTypeArgumentSimplified ( COMMA genericTypeArgumentSimplified )* genericTypeListClosing
                pass 
                LESS_THAN195=self.match(self.input, LESS_THAN, self.FOLLOW_LESS_THAN_in_genericTypeArgumentListSimplified7359) 
                if self._state.backtracking == 0:
                    stream_LESS_THAN.add(LESS_THAN195)
                self._state.following.append(self.FOLLOW_genericTypeArgumentSimplified_in_genericTypeArgumentListSimplified7361)
                genericTypeArgumentSimplified196 = self.genericTypeArgumentSimplified()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_genericTypeArgumentSimplified.add(genericTypeArgumentSimplified196.tree)
                # Java.g:562:49: ( COMMA genericTypeArgumentSimplified )*
                while True: #loop68
                    alt68 = 2
                    LA68_0 = self.input.LA(1)

                    if (LA68_0 == COMMA) :
                        alt68 = 1


                    if alt68 == 1:
                        # Java.g:562:50: COMMA genericTypeArgumentSimplified
                        pass 
                        COMMA197=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_genericTypeArgumentListSimplified7364) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA197)
                        self._state.following.append(self.FOLLOW_genericTypeArgumentSimplified_in_genericTypeArgumentListSimplified7366)
                        genericTypeArgumentSimplified198 = self.genericTypeArgumentSimplified()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_genericTypeArgumentSimplified.add(genericTypeArgumentSimplified198.tree)


                    else:
                        break #loop68


                self._state.following.append(self.FOLLOW_genericTypeListClosing_in_genericTypeArgumentListSimplified7370)
                genericTypeListClosing199 = self.genericTypeListClosing()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_genericTypeListClosing.add(genericTypeListClosing199.tree)

                # AST Rewrite
                # elements: genericTypeArgumentSimplified
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 563:9: -> ^( GENERIC_TYPE_ARG_LIST[$LESS_THAN, \"GENERIC_TYPE_ARG_LIST\"] ( genericTypeArgumentSimplified )+ )
                    # Java.g:563:13: ^( GENERIC_TYPE_ARG_LIST[$LESS_THAN, \"GENERIC_TYPE_ARG_LIST\"] ( genericTypeArgumentSimplified )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.create(GENERIC_TYPE_ARG_LIST, LESS_THAN195, "GENERIC_TYPE_ARG_LIST"), root_1)

                    # Java.g:563:74: ( genericTypeArgumentSimplified )+
                    if not (stream_genericTypeArgumentSimplified.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_genericTypeArgumentSimplified.hasNext():
                        self._adaptor.addChild(root_1, stream_genericTypeArgumentSimplified.nextTree())


                    stream_genericTypeArgumentSimplified.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 53, genericTypeArgumentListSimplified_StartIndex, success)

            pass

        return retval

    # $ANTLR end "genericTypeArgumentListSimplified"

    class genericTypeArgumentSimplified_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "genericTypeArgumentSimplified"
    # Java.g:566:1: genericTypeArgumentSimplified : ( type | QUESTION );
    def genericTypeArgumentSimplified(self, ):

        retval = self.genericTypeArgumentSimplified_return()
        retval.start = self.input.LT(1)
        genericTypeArgumentSimplified_StartIndex = self.input.index()
        root_0 = None

        QUESTION201 = None
        type200 = None


        QUESTION201_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 54):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:567:5: ( type | QUESTION )
                alt69 = 2
                LA69_0 = self.input.LA(1)

                if (LA69_0 == BOOLEAN or LA69_0 == BYTE or LA69_0 == CHAR or LA69_0 == DOUBLE or LA69_0 == FLOAT or (INT <= LA69_0 <= LONG) or LA69_0 == SHORT or LA69_0 == IDENT) :
                    alt69 = 1
                elif (LA69_0 == QUESTION) :
                    alt69 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 69, 0, self.input)

                    raise nvae

                if alt69 == 1:
                    # Java.g:567:9: type
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_type_in_genericTypeArgumentSimplified7408)
                    type200 = self.type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, type200.tree)


                elif alt69 == 2:
                    # Java.g:568:9: QUESTION
                    pass 
                    root_0 = self._adaptor.nil()

                    QUESTION201=self.match(self.input, QUESTION, self.FOLLOW_QUESTION_in_genericTypeArgumentSimplified7418)
                    if self._state.backtracking == 0:

                        QUESTION201_tree = self._adaptor.createWithPayload(QUESTION201)
                        self._adaptor.addChild(root_0, QUESTION201_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 54, genericTypeArgumentSimplified_StartIndex, success)

            pass

        return retval

    # $ANTLR end "genericTypeArgumentSimplified"

    class qualifiedIdentList_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "qualifiedIdentList"
    # Java.g:571:1: qualifiedIdentList : qualifiedIdentifier ( COMMA qualifiedIdentifier )* ;
    def qualifiedIdentList(self, ):

        retval = self.qualifiedIdentList_return()
        retval.start = self.input.LT(1)
        qualifiedIdentList_StartIndex = self.input.index()
        root_0 = None

        COMMA203 = None
        qualifiedIdentifier202 = None

        qualifiedIdentifier204 = None


        COMMA203_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 55):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:572:5: ( qualifiedIdentifier ( COMMA qualifiedIdentifier )* )
                # Java.g:572:9: qualifiedIdentifier ( COMMA qualifiedIdentifier )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_qualifiedIdentList7437)
                qualifiedIdentifier202 = self.qualifiedIdentifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, qualifiedIdentifier202.tree)
                # Java.g:572:29: ( COMMA qualifiedIdentifier )*
                while True: #loop70
                    alt70 = 2
                    LA70_0 = self.input.LA(1)

                    if (LA70_0 == COMMA) :
                        alt70 = 1


                    if alt70 == 1:
                        # Java.g:572:30: COMMA qualifiedIdentifier
                        pass 
                        COMMA203=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_qualifiedIdentList7440)
                        self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_qualifiedIdentList7443)
                        qualifiedIdentifier204 = self.qualifiedIdentifier()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, qualifiedIdentifier204.tree)


                    else:
                        break #loop70





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 55, qualifiedIdentList_StartIndex, success)

            pass

        return retval

    # $ANTLR end "qualifiedIdentList"

    class formalParameterList_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "formalParameterList"
    # Java.g:575:1: formalParameterList : LPAREN ( formalParameterStandardDecl ( COMMA formalParameterStandardDecl )* ( COMMA formalParameterVarArgDecl )? -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] ( formalParameterStandardDecl )+ ( formalParameterVarArgDecl )? ) | formalParameterVarArgDecl -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] formalParameterVarArgDecl ) | -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] ) ) RPAREN ;
    def formalParameterList(self, ):

        retval = self.formalParameterList_return()
        retval.start = self.input.LT(1)
        formalParameterList_StartIndex = self.input.index()
        root_0 = None

        LPAREN205 = None
        COMMA207 = None
        COMMA209 = None
        RPAREN212 = None
        formalParameterStandardDecl206 = None

        formalParameterStandardDecl208 = None

        formalParameterVarArgDecl210 = None

        formalParameterVarArgDecl211 = None


        LPAREN205_tree = None
        COMMA207_tree = None
        COMMA209_tree = None
        RPAREN212_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_formalParameterVarArgDecl = RewriteRuleSubtreeStream(self._adaptor, "rule formalParameterVarArgDecl")
        stream_formalParameterStandardDecl = RewriteRuleSubtreeStream(self._adaptor, "rule formalParameterStandardDecl")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 56):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:576:5: ( LPAREN ( formalParameterStandardDecl ( COMMA formalParameterStandardDecl )* ( COMMA formalParameterVarArgDecl )? -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] ( formalParameterStandardDecl )+ ( formalParameterVarArgDecl )? ) | formalParameterVarArgDecl -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] formalParameterVarArgDecl ) | -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] ) ) RPAREN )
                # Java.g:576:9: LPAREN ( formalParameterStandardDecl ( COMMA formalParameterStandardDecl )* ( COMMA formalParameterVarArgDecl )? -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] ( formalParameterStandardDecl )+ ( formalParameterVarArgDecl )? ) | formalParameterVarArgDecl -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] formalParameterVarArgDecl ) | -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] ) ) RPAREN
                pass 
                LPAREN205=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_formalParameterList7464) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(LPAREN205)
                # Java.g:577:9: ( formalParameterStandardDecl ( COMMA formalParameterStandardDecl )* ( COMMA formalParameterVarArgDecl )? -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] ( formalParameterStandardDecl )+ ( formalParameterVarArgDecl )? ) | formalParameterVarArgDecl -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] formalParameterVarArgDecl ) | -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] ) )
                alt73 = 3
                LA73 = self.input.LA(1)
                if LA73 == FINAL:
                    LA73_1 = self.input.LA(2)

                    if (self.synpred99_Java()) :
                        alt73 = 1
                    elif (self.synpred100_Java()) :
                        alt73 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 73, 1, self.input)

                        raise nvae

                elif LA73 == AT:
                    LA73_2 = self.input.LA(2)

                    if (self.synpred99_Java()) :
                        alt73 = 1
                    elif (self.synpred100_Java()) :
                        alt73 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 73, 2, self.input)

                        raise nvae

                elif LA73 == BOOLEAN or LA73 == BYTE or LA73 == CHAR or LA73 == DOUBLE or LA73 == FLOAT or LA73 == INT or LA73 == LONG or LA73 == SHORT:
                    LA73_3 = self.input.LA(2)

                    if (self.synpred99_Java()) :
                        alt73 = 1
                    elif (self.synpred100_Java()) :
                        alt73 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 73, 3, self.input)

                        raise nvae

                elif LA73 == IDENT:
                    LA73_4 = self.input.LA(2)

                    if (self.synpred99_Java()) :
                        alt73 = 1
                    elif (self.synpred100_Java()) :
                        alt73 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 73, 4, self.input)

                        raise nvae

                elif LA73 == RPAREN:
                    alt73 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 73, 0, self.input)

                    raise nvae

                if alt73 == 1:
                    # Java.g:578:13: formalParameterStandardDecl ( COMMA formalParameterStandardDecl )* ( COMMA formalParameterVarArgDecl )?
                    pass 
                    self._state.following.append(self.FOLLOW_formalParameterStandardDecl_in_formalParameterList7491)
                    formalParameterStandardDecl206 = self.formalParameterStandardDecl()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_formalParameterStandardDecl.add(formalParameterStandardDecl206.tree)
                    # Java.g:578:41: ( COMMA formalParameterStandardDecl )*
                    while True: #loop71
                        alt71 = 2
                        LA71_0 = self.input.LA(1)

                        if (LA71_0 == COMMA) :
                            LA71_1 = self.input.LA(2)

                            if (self.synpred97_Java()) :
                                alt71 = 1




                        if alt71 == 1:
                            # Java.g:578:42: COMMA formalParameterStandardDecl
                            pass 
                            COMMA207=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_formalParameterList7494) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA207)
                            self._state.following.append(self.FOLLOW_formalParameterStandardDecl_in_formalParameterList7496)
                            formalParameterStandardDecl208 = self.formalParameterStandardDecl()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_formalParameterStandardDecl.add(formalParameterStandardDecl208.tree)


                        else:
                            break #loop71


                    # Java.g:578:78: ( COMMA formalParameterVarArgDecl )?
                    alt72 = 2
                    LA72_0 = self.input.LA(1)

                    if (LA72_0 == COMMA) :
                        alt72 = 1
                    if alt72 == 1:
                        # Java.g:578:79: COMMA formalParameterVarArgDecl
                        pass 
                        COMMA209=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_formalParameterList7501) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA209)
                        self._state.following.append(self.FOLLOW_formalParameterVarArgDecl_in_formalParameterList7503)
                        formalParameterVarArgDecl210 = self.formalParameterVarArgDecl()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_formalParameterVarArgDecl.add(formalParameterVarArgDecl210.tree)




                    # AST Rewrite
                    # elements: formalParameterStandardDecl, formalParameterVarArgDecl
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 579:13: -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] ( formalParameterStandardDecl )+ ( formalParameterVarArgDecl )? )
                        # Java.g:579:17: ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] ( formalParameterStandardDecl )+ ( formalParameterVarArgDecl )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.create(FORMAL_PARAM_LIST, LPAREN205, "FORMAL_PARAM_LIST"), root_1)

                        # Java.g:579:67: ( formalParameterStandardDecl )+
                        if not (stream_formalParameterStandardDecl.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_formalParameterStandardDecl.hasNext():
                            self._adaptor.addChild(root_1, stream_formalParameterStandardDecl.nextTree())


                        stream_formalParameterStandardDecl.reset()
                        # Java.g:579:96: ( formalParameterVarArgDecl )?
                        if stream_formalParameterVarArgDecl.hasNext():
                            self._adaptor.addChild(root_1, stream_formalParameterVarArgDecl.nextTree())


                        stream_formalParameterVarArgDecl.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt73 == 2:
                    # Java.g:581:13: formalParameterVarArgDecl
                    pass 
                    self._state.following.append(self.FOLLOW_formalParameterVarArgDecl_in_formalParameterList7558)
                    formalParameterVarArgDecl211 = self.formalParameterVarArgDecl()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_formalParameterVarArgDecl.add(formalParameterVarArgDecl211.tree)

                    # AST Rewrite
                    # elements: formalParameterVarArgDecl
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 582:13: -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] formalParameterVarArgDecl )
                        # Java.g:582:17: ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] formalParameterVarArgDecl )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.create(FORMAL_PARAM_LIST, LPAREN205, "FORMAL_PARAM_LIST"), root_1)

                        self._adaptor.addChild(root_1, stream_formalParameterVarArgDecl.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt73 == 3:
                    # Java.g:584:13: 
                    pass 
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 584:13: -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] )
                        # Java.g:584:17: ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.create(FORMAL_PARAM_LIST, LPAREN205, "FORMAL_PARAM_LIST"), root_1)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0



                RPAREN212=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_formalParameterList7633) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(RPAREN212)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 56, formalParameterList_StartIndex, success)

            pass

        return retval

    # $ANTLR end "formalParameterList"

    class formalParameterStandardDecl_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "formalParameterStandardDecl"
    # Java.g:589:1: formalParameterStandardDecl : localModifierList type variableDeclaratorId -> ^( FORMAL_PARAM_STD_DECL localModifierList type variableDeclaratorId ) ;
    def formalParameterStandardDecl(self, ):

        retval = self.formalParameterStandardDecl_return()
        retval.start = self.input.LT(1)
        formalParameterStandardDecl_StartIndex = self.input.index()
        root_0 = None

        localModifierList213 = None

        type214 = None

        variableDeclaratorId215 = None


        stream_variableDeclaratorId = RewriteRuleSubtreeStream(self._adaptor, "rule variableDeclaratorId")
        stream_localModifierList = RewriteRuleSubtreeStream(self._adaptor, "rule localModifierList")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 57):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:590:5: ( localModifierList type variableDeclaratorId -> ^( FORMAL_PARAM_STD_DECL localModifierList type variableDeclaratorId ) )
                # Java.g:590:9: localModifierList type variableDeclaratorId
                pass 
                self._state.following.append(self.FOLLOW_localModifierList_in_formalParameterStandardDecl7652)
                localModifierList213 = self.localModifierList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_localModifierList.add(localModifierList213.tree)
                self._state.following.append(self.FOLLOW_type_in_formalParameterStandardDecl7654)
                type214 = self.type()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_type.add(type214.tree)
                self._state.following.append(self.FOLLOW_variableDeclaratorId_in_formalParameterStandardDecl7656)
                variableDeclaratorId215 = self.variableDeclaratorId()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_variableDeclaratorId.add(variableDeclaratorId215.tree)

                # AST Rewrite
                # elements: type, localModifierList, variableDeclaratorId
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 591:9: -> ^( FORMAL_PARAM_STD_DECL localModifierList type variableDeclaratorId )
                    # Java.g:591:13: ^( FORMAL_PARAM_STD_DECL localModifierList type variableDeclaratorId )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FORMAL_PARAM_STD_DECL, "FORMAL_PARAM_STD_DECL"), root_1)

                    self._adaptor.addChild(root_1, stream_localModifierList.nextTree())
                    self._adaptor.addChild(root_1, stream_type.nextTree())
                    self._adaptor.addChild(root_1, stream_variableDeclaratorId.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 57, formalParameterStandardDecl_StartIndex, success)

            pass

        return retval

    # $ANTLR end "formalParameterStandardDecl"

    class formalParameterVarArgDecl_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "formalParameterVarArgDecl"
    # Java.g:594:1: formalParameterVarArgDecl : localModifierList type ELLIPSIS variableDeclaratorId -> ^( FORMAL_PARAM_VARARG_DECL localModifierList type variableDeclaratorId ) ;
    def formalParameterVarArgDecl(self, ):

        retval = self.formalParameterVarArgDecl_return()
        retval.start = self.input.LT(1)
        formalParameterVarArgDecl_StartIndex = self.input.index()
        root_0 = None

        ELLIPSIS218 = None
        localModifierList216 = None

        type217 = None

        variableDeclaratorId219 = None


        ELLIPSIS218_tree = None
        stream_ELLIPSIS = RewriteRuleTokenStream(self._adaptor, "token ELLIPSIS")
        stream_variableDeclaratorId = RewriteRuleSubtreeStream(self._adaptor, "rule variableDeclaratorId")
        stream_localModifierList = RewriteRuleSubtreeStream(self._adaptor, "rule localModifierList")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 58):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:595:5: ( localModifierList type ELLIPSIS variableDeclaratorId -> ^( FORMAL_PARAM_VARARG_DECL localModifierList type variableDeclaratorId ) )
                # Java.g:595:9: localModifierList type ELLIPSIS variableDeclaratorId
                pass 
                self._state.following.append(self.FOLLOW_localModifierList_in_formalParameterVarArgDecl7696)
                localModifierList216 = self.localModifierList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_localModifierList.add(localModifierList216.tree)
                self._state.following.append(self.FOLLOW_type_in_formalParameterVarArgDecl7698)
                type217 = self.type()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_type.add(type217.tree)
                ELLIPSIS218=self.match(self.input, ELLIPSIS, self.FOLLOW_ELLIPSIS_in_formalParameterVarArgDecl7700) 
                if self._state.backtracking == 0:
                    stream_ELLIPSIS.add(ELLIPSIS218)
                self._state.following.append(self.FOLLOW_variableDeclaratorId_in_formalParameterVarArgDecl7702)
                variableDeclaratorId219 = self.variableDeclaratorId()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_variableDeclaratorId.add(variableDeclaratorId219.tree)

                # AST Rewrite
                # elements: type, variableDeclaratorId, localModifierList
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 596:9: -> ^( FORMAL_PARAM_VARARG_DECL localModifierList type variableDeclaratorId )
                    # Java.g:596:13: ^( FORMAL_PARAM_VARARG_DECL localModifierList type variableDeclaratorId )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FORMAL_PARAM_VARARG_DECL, "FORMAL_PARAM_VARARG_DECL"), root_1)

                    self._adaptor.addChild(root_1, stream_localModifierList.nextTree())
                    self._adaptor.addChild(root_1, stream_type.nextTree())
                    self._adaptor.addChild(root_1, stream_variableDeclaratorId.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 58, formalParameterVarArgDecl_StartIndex, success)

            pass

        return retval

    # $ANTLR end "formalParameterVarArgDecl"

    class qualifiedIdentifier_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "qualifiedIdentifier"
    # Java.g:599:1: qualifiedIdentifier : ( IDENT -> IDENT ) ( DOT ident= IDENT -> ^( DOT $qualifiedIdentifier $ident) )* ;
    def qualifiedIdentifier(self, ):

        retval = self.qualifiedIdentifier_return()
        retval.start = self.input.LT(1)
        qualifiedIdentifier_StartIndex = self.input.index()
        root_0 = None

        ident = None
        IDENT220 = None
        DOT221 = None

        ident_tree = None
        IDENT220_tree = None
        DOT221_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 59):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:600:5: ( ( IDENT -> IDENT ) ( DOT ident= IDENT -> ^( DOT $qualifiedIdentifier $ident) )* )
                # Java.g:600:9: ( IDENT -> IDENT ) ( DOT ident= IDENT -> ^( DOT $qualifiedIdentifier $ident) )*
                pass 
                # Java.g:600:9: ( IDENT -> IDENT )
                # Java.g:600:13: IDENT
                pass 
                IDENT220=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_qualifiedIdentifier7746) 
                if self._state.backtracking == 0:
                    stream_IDENT.add(IDENT220)

                # AST Rewrite
                # elements: IDENT
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 600:33: -> IDENT
                    self._adaptor.addChild(root_0, stream_IDENT.nextNode())



                    retval.tree = root_0



                # Java.g:602:9: ( DOT ident= IDENT -> ^( DOT $qualifiedIdentifier $ident) )*
                while True: #loop74
                    alt74 = 2
                    LA74_0 = self.input.LA(1)

                    if (LA74_0 == DOT) :
                        LA74_2 = self.input.LA(2)

                        if (LA74_2 == IDENT) :
                            LA74_3 = self.input.LA(3)

                            if (self.synpred101_Java()) :
                                alt74 = 1






                    if alt74 == 1:
                        # Java.g:602:13: DOT ident= IDENT
                        pass 
                        DOT221=self.match(self.input, DOT, self.FOLLOW_DOT_in_qualifiedIdentifier7789) 
                        if self._state.backtracking == 0:
                            stream_DOT.add(DOT221)
                        ident=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_qualifiedIdentifier7793) 
                        if self._state.backtracking == 0:
                            stream_IDENT.add(ident)

                        # AST Rewrite
                        # elements: qualifiedIdentifier, ident, DOT
                        # token labels: ident
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0
                            stream_ident = RewriteRuleTokenStream(self._adaptor, "token ident", ident)

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 602:33: -> ^( DOT $qualifiedIdentifier $ident)
                            # Java.g:602:37: ^( DOT $qualifiedIdentifier $ident)
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(stream_DOT.nextNode(), root_1)

                            self._adaptor.addChild(root_1, stream_retval.nextTree())
                            self._adaptor.addChild(root_1, stream_ident.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    else:
                        break #loop74





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 59, qualifiedIdentifier_StartIndex, success)

            pass

        return retval

    # $ANTLR end "qualifiedIdentifier"

    class annotationList_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "annotationList"
    # Java.g:608:1: annotationList : ( annotation )* -> ^( ANNOTATION_LIST ( annotation )* ) ;
    def annotationList(self, ):

        retval = self.annotationList_return()
        retval.start = self.input.LT(1)
        annotationList_StartIndex = self.input.index()
        root_0 = None

        annotation222 = None


        stream_annotation = RewriteRuleSubtreeStream(self._adaptor, "rule annotation")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 60):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:609:5: ( ( annotation )* -> ^( ANNOTATION_LIST ( annotation )* ) )
                # Java.g:609:9: ( annotation )*
                pass 
                # Java.g:609:9: ( annotation )*
                while True: #loop75
                    alt75 = 2
                    LA75_0 = self.input.LA(1)

                    if (LA75_0 == AT) :
                        LA75_2 = self.input.LA(2)

                        if (LA75_2 == IDENT) :
                            LA75_3 = self.input.LA(3)

                            if (self.synpred102_Java()) :
                                alt75 = 1






                    if alt75 == 1:
                        # Java.g:0:0: annotation
                        pass 
                        self._state.following.append(self.FOLLOW_annotation_in_annotationList7842)
                        annotation222 = self.annotation()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_annotation.add(annotation222.tree)


                    else:
                        break #loop75



                # AST Rewrite
                # elements: annotation
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 610:9: -> ^( ANNOTATION_LIST ( annotation )* )
                    # Java.g:610:13: ^( ANNOTATION_LIST ( annotation )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ANNOTATION_LIST, "ANNOTATION_LIST"), root_1)

                    # Java.g:610:31: ( annotation )*
                    while stream_annotation.hasNext():
                        self._adaptor.addChild(root_1, stream_annotation.nextTree())


                    stream_annotation.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 60, annotationList_StartIndex, success)

            pass

        return retval

    # $ANTLR end "annotationList"

    class annotation_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "annotation"
    # Java.g:613:1: annotation : AT qualifiedIdentifier ( annotationInit )? ;
    def annotation(self, ):

        retval = self.annotation_return()
        retval.start = self.input.LT(1)
        annotation_StartIndex = self.input.index()
        root_0 = None

        AT223 = None
        qualifiedIdentifier224 = None

        annotationInit225 = None


        AT223_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 61):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:614:5: ( AT qualifiedIdentifier ( annotationInit )? )
                # Java.g:614:9: AT qualifiedIdentifier ( annotationInit )?
                pass 
                root_0 = self._adaptor.nil()

                AT223=self.match(self.input, AT, self.FOLLOW_AT_in_annotation7880)
                if self._state.backtracking == 0:

                    AT223_tree = self._adaptor.createWithPayload(AT223)
                    root_0 = self._adaptor.becomeRoot(AT223_tree, root_0)

                self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_annotation7883)
                qualifiedIdentifier224 = self.qualifiedIdentifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, qualifiedIdentifier224.tree)
                # Java.g:614:33: ( annotationInit )?
                alt76 = 2
                LA76_0 = self.input.LA(1)

                if (LA76_0 == LPAREN) :
                    alt76 = 1
                if alt76 == 1:
                    # Java.g:0:0: annotationInit
                    pass 
                    self._state.following.append(self.FOLLOW_annotationInit_in_annotation7885)
                    annotationInit225 = self.annotationInit()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, annotationInit225.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 61, annotation_StartIndex, success)

            pass

        return retval

    # $ANTLR end "annotation"

    class annotationInit_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "annotationInit"
    # Java.g:617:1: annotationInit : LPAREN annotationInitializers RPAREN -> ^( ANNOTATION_INIT_BLOCK[$LPAREN, \"ANNOTATION_INIT_BLOCK\"] annotationInitializers ) ;
    def annotationInit(self, ):

        retval = self.annotationInit_return()
        retval.start = self.input.LT(1)
        annotationInit_StartIndex = self.input.index()
        root_0 = None

        LPAREN226 = None
        RPAREN228 = None
        annotationInitializers227 = None


        LPAREN226_tree = None
        RPAREN228_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_annotationInitializers = RewriteRuleSubtreeStream(self._adaptor, "rule annotationInitializers")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 62):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:618:5: ( LPAREN annotationInitializers RPAREN -> ^( ANNOTATION_INIT_BLOCK[$LPAREN, \"ANNOTATION_INIT_BLOCK\"] annotationInitializers ) )
                # Java.g:618:9: LPAREN annotationInitializers RPAREN
                pass 
                LPAREN226=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_annotationInit7905) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(LPAREN226)
                self._state.following.append(self.FOLLOW_annotationInitializers_in_annotationInit7907)
                annotationInitializers227 = self.annotationInitializers()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_annotationInitializers.add(annotationInitializers227.tree)
                RPAREN228=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_annotationInit7909) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(RPAREN228)

                # AST Rewrite
                # elements: annotationInitializers
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 619:9: -> ^( ANNOTATION_INIT_BLOCK[$LPAREN, \"ANNOTATION_INIT_BLOCK\"] annotationInitializers )
                    # Java.g:619:13: ^( ANNOTATION_INIT_BLOCK[$LPAREN, \"ANNOTATION_INIT_BLOCK\"] annotationInitializers )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.create(ANNOTATION_INIT_BLOCK, LPAREN226, "ANNOTATION_INIT_BLOCK"), root_1)

                    self._adaptor.addChild(root_1, stream_annotationInitializers.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 62, annotationInit_StartIndex, success)

            pass

        return retval

    # $ANTLR end "annotationInit"

    class annotationInitializers_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "annotationInitializers"
    # Java.g:622:1: annotationInitializers : ( annotationInitializer ( COMMA annotationInitializer )* -> ^( ANNOTATION_INIT_KEY_LIST ( annotationInitializer )+ ) | annotationElementValue -> ^( ANNOTATION_INIT_DEFAULT_KEY annotationElementValue ) );
    def annotationInitializers(self, ):

        retval = self.annotationInitializers_return()
        retval.start = self.input.LT(1)
        annotationInitializers_StartIndex = self.input.index()
        root_0 = None

        COMMA230 = None
        annotationInitializer229 = None

        annotationInitializer231 = None

        annotationElementValue232 = None


        COMMA230_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_annotationElementValue = RewriteRuleSubtreeStream(self._adaptor, "rule annotationElementValue")
        stream_annotationInitializer = RewriteRuleSubtreeStream(self._adaptor, "rule annotationInitializer")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 63):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:623:5: ( annotationInitializer ( COMMA annotationInitializer )* -> ^( ANNOTATION_INIT_KEY_LIST ( annotationInitializer )+ ) | annotationElementValue -> ^( ANNOTATION_INIT_DEFAULT_KEY annotationElementValue ) )
                alt78 = 2
                LA78_0 = self.input.LA(1)

                if (LA78_0 == IDENT) :
                    LA78_1 = self.input.LA(2)

                    if (LA78_1 == ASSIGN) :
                        alt78 = 1
                    elif (LA78_1 == AND or LA78_1 == BIT_SHIFT_RIGHT or (DEC <= LA78_1 <= DIV) or LA78_1 == DOT or (EQUAL <= LA78_1 <= LBRACK) or (LESS_OR_EQUAL <= LA78_1 <= LOGICAL_AND) or (LOGICAL_OR <= LA78_1 <= MINUS) or LA78_1 == MOD or (NOT_EQUAL <= LA78_1 <= OR) or LA78_1 == PLUS or LA78_1 == QUESTION or LA78_1 == RPAREN or LA78_1 == SHIFT_LEFT or LA78_1 == SHIFT_RIGHT or LA78_1 == STAR or LA78_1 == XOR or LA78_1 == INSTANCEOF) :
                        alt78 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 78, 1, self.input)

                        raise nvae

                elif (LA78_0 == AT or LA78_0 == DEC or LA78_0 == INC or LA78_0 == LCURLY or LA78_0 == LESS_THAN or LA78_0 == LOGICAL_NOT or (LPAREN <= LA78_0 <= MINUS) or LA78_0 == NOT or LA78_0 == PLUS or LA78_0 == BOOLEAN or LA78_0 == BYTE or LA78_0 == CHAR or LA78_0 == DOUBLE or LA78_0 == FALSE or LA78_0 == FLOAT or (INT <= LA78_0 <= LONG) or (NEW <= LA78_0 <= NULL) or LA78_0 == SHORT or LA78_0 == SUPER or LA78_0 == THIS or LA78_0 == TRUE or LA78_0 == VOID or (HEX_LITERAL <= LA78_0 <= STRING_LITERAL)) :
                    alt78 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 78, 0, self.input)

                    raise nvae

                if alt78 == 1:
                    # Java.g:623:9: annotationInitializer ( COMMA annotationInitializer )*
                    pass 
                    self._state.following.append(self.FOLLOW_annotationInitializer_in_annotationInitializers7946)
                    annotationInitializer229 = self.annotationInitializer()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_annotationInitializer.add(annotationInitializer229.tree)
                    # Java.g:623:31: ( COMMA annotationInitializer )*
                    while True: #loop77
                        alt77 = 2
                        LA77_0 = self.input.LA(1)

                        if (LA77_0 == COMMA) :
                            alt77 = 1


                        if alt77 == 1:
                            # Java.g:623:32: COMMA annotationInitializer
                            pass 
                            COMMA230=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_annotationInitializers7949) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA230)
                            self._state.following.append(self.FOLLOW_annotationInitializer_in_annotationInitializers7951)
                            annotationInitializer231 = self.annotationInitializer()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_annotationInitializer.add(annotationInitializer231.tree)


                        else:
                            break #loop77



                    # AST Rewrite
                    # elements: annotationInitializer
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 624:9: -> ^( ANNOTATION_INIT_KEY_LIST ( annotationInitializer )+ )
                        # Java.g:624:13: ^( ANNOTATION_INIT_KEY_LIST ( annotationInitializer )+ )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ANNOTATION_INIT_KEY_LIST, "ANNOTATION_INIT_KEY_LIST"), root_1)

                        # Java.g:624:40: ( annotationInitializer )+
                        if not (stream_annotationInitializer.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_annotationInitializer.hasNext():
                            self._adaptor.addChild(root_1, stream_annotationInitializer.nextTree())


                        stream_annotationInitializer.reset()

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt78 == 2:
                    # Java.g:625:9: annotationElementValue
                    pass 
                    self._state.following.append(self.FOLLOW_annotationElementValue_in_annotationInitializers7981)
                    annotationElementValue232 = self.annotationElementValue()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_annotationElementValue.add(annotationElementValue232.tree)

                    # AST Rewrite
                    # elements: annotationElementValue
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 626:9: -> ^( ANNOTATION_INIT_DEFAULT_KEY annotationElementValue )
                        # Java.g:626:13: ^( ANNOTATION_INIT_DEFAULT_KEY annotationElementValue )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ANNOTATION_INIT_DEFAULT_KEY, "ANNOTATION_INIT_DEFAULT_KEY"), root_1)

                        self._adaptor.addChild(root_1, stream_annotationElementValue.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 63, annotationInitializers_StartIndex, success)

            pass

        return retval

    # $ANTLR end "annotationInitializers"

    class annotationInitializer_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "annotationInitializer"
    # Java.g:629:1: annotationInitializer : IDENT ASSIGN annotationElementValue ;
    def annotationInitializer(self, ):

        retval = self.annotationInitializer_return()
        retval.start = self.input.LT(1)
        annotationInitializer_StartIndex = self.input.index()
        root_0 = None

        IDENT233 = None
        ASSIGN234 = None
        annotationElementValue235 = None


        IDENT233_tree = None
        ASSIGN234_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 64):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:630:5: ( IDENT ASSIGN annotationElementValue )
                # Java.g:630:9: IDENT ASSIGN annotationElementValue
                pass 
                root_0 = self._adaptor.nil()

                IDENT233=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_annotationInitializer8018)
                if self._state.backtracking == 0:

                    IDENT233_tree = self._adaptor.createWithPayload(IDENT233)
                    root_0 = self._adaptor.becomeRoot(IDENT233_tree, root_0)

                ASSIGN234=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_annotationInitializer8021)
                self._state.following.append(self.FOLLOW_annotationElementValue_in_annotationInitializer8024)
                annotationElementValue235 = self.annotationElementValue()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, annotationElementValue235.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 64, annotationInitializer_StartIndex, success)

            pass

        return retval

    # $ANTLR end "annotationInitializer"

    class annotationElementValue_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "annotationElementValue"
    # Java.g:633:1: annotationElementValue : ( annotationElementValueExpression | annotation | annotationElementValueArrayInitializer );
    def annotationElementValue(self, ):

        retval = self.annotationElementValue_return()
        retval.start = self.input.LT(1)
        annotationElementValue_StartIndex = self.input.index()
        root_0 = None

        annotationElementValueExpression236 = None

        annotation237 = None

        annotationElementValueArrayInitializer238 = None



        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 65):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:634:5: ( annotationElementValueExpression | annotation | annotationElementValueArrayInitializer )
                alt79 = 3
                LA79 = self.input.LA(1)
                if LA79 == DEC or LA79 == INC or LA79 == LESS_THAN or LA79 == LOGICAL_NOT or LA79 == LPAREN or LA79 == MINUS or LA79 == NOT or LA79 == PLUS or LA79 == BOOLEAN or LA79 == BYTE or LA79 == CHAR or LA79 == DOUBLE or LA79 == FALSE or LA79 == FLOAT or LA79 == INT or LA79 == LONG or LA79 == NEW or LA79 == NULL or LA79 == SHORT or LA79 == SUPER or LA79 == THIS or LA79 == TRUE or LA79 == VOID or LA79 == IDENT or LA79 == HEX_LITERAL or LA79 == OCTAL_LITERAL or LA79 == DECIMAL_LITERAL or LA79 == FLOATING_POINT_LITERAL or LA79 == CHARACTER_LITERAL or LA79 == STRING_LITERAL:
                    alt79 = 1
                elif LA79 == AT:
                    alt79 = 2
                elif LA79 == LCURLY:
                    alt79 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 79, 0, self.input)

                    raise nvae

                if alt79 == 1:
                    # Java.g:634:9: annotationElementValueExpression
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_annotationElementValueExpression_in_annotationElementValue8043)
                    annotationElementValueExpression236 = self.annotationElementValueExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, annotationElementValueExpression236.tree)


                elif alt79 == 2:
                    # Java.g:635:9: annotation
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_annotation_in_annotationElementValue8053)
                    annotation237 = self.annotation()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, annotation237.tree)


                elif alt79 == 3:
                    # Java.g:636:9: annotationElementValueArrayInitializer
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_annotationElementValueArrayInitializer_in_annotationElementValue8063)
                    annotationElementValueArrayInitializer238 = self.annotationElementValueArrayInitializer()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, annotationElementValueArrayInitializer238.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 65, annotationElementValue_StartIndex, success)

            pass

        return retval

    # $ANTLR end "annotationElementValue"

    class annotationElementValueExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "annotationElementValueExpression"
    # Java.g:639:1: annotationElementValueExpression : conditionalExpression -> ^( EXPR conditionalExpression ) ;
    def annotationElementValueExpression(self, ):

        retval = self.annotationElementValueExpression_return()
        retval.start = self.input.LT(1)
        annotationElementValueExpression_StartIndex = self.input.index()
        root_0 = None

        conditionalExpression239 = None


        stream_conditionalExpression = RewriteRuleSubtreeStream(self._adaptor, "rule conditionalExpression")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 66):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:640:5: ( conditionalExpression -> ^( EXPR conditionalExpression ) )
                # Java.g:640:9: conditionalExpression
                pass 
                self._state.following.append(self.FOLLOW_conditionalExpression_in_annotationElementValueExpression8082)
                conditionalExpression239 = self.conditionalExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_conditionalExpression.add(conditionalExpression239.tree)

                # AST Rewrite
                # elements: conditionalExpression
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 641:9: -> ^( EXPR conditionalExpression )
                    # Java.g:641:13: ^( EXPR conditionalExpression )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EXPR, "EXPR"), root_1)

                    self._adaptor.addChild(root_1, stream_conditionalExpression.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 66, annotationElementValueExpression_StartIndex, success)

            pass

        return retval

    # $ANTLR end "annotationElementValueExpression"

    class annotationElementValueArrayInitializer_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "annotationElementValueArrayInitializer"
    # Java.g:644:1: annotationElementValueArrayInitializer : LCURLY ( annotationElementValue ( COMMA annotationElementValue )* )? ( COMMA )? RCURLY -> ^( ANNOTATION_INIT_ARRAY_ELEMENT[$LCURLY, \"ANNOTATION_ELEM_VALUE_ARRAY_INIT\"] ( annotationElementValue )* ) ;
    def annotationElementValueArrayInitializer(self, ):

        retval = self.annotationElementValueArrayInitializer_return()
        retval.start = self.input.LT(1)
        annotationElementValueArrayInitializer_StartIndex = self.input.index()
        root_0 = None

        LCURLY240 = None
        COMMA242 = None
        COMMA244 = None
        RCURLY245 = None
        annotationElementValue241 = None

        annotationElementValue243 = None


        LCURLY240_tree = None
        COMMA242_tree = None
        COMMA244_tree = None
        RCURLY245_tree = None
        stream_LCURLY = RewriteRuleTokenStream(self._adaptor, "token LCURLY")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_RCURLY = RewriteRuleTokenStream(self._adaptor, "token RCURLY")
        stream_annotationElementValue = RewriteRuleSubtreeStream(self._adaptor, "rule annotationElementValue")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 67):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:645:5: ( LCURLY ( annotationElementValue ( COMMA annotationElementValue )* )? ( COMMA )? RCURLY -> ^( ANNOTATION_INIT_ARRAY_ELEMENT[$LCURLY, \"ANNOTATION_ELEM_VALUE_ARRAY_INIT\"] ( annotationElementValue )* ) )
                # Java.g:645:9: LCURLY ( annotationElementValue ( COMMA annotationElementValue )* )? ( COMMA )? RCURLY
                pass 
                LCURLY240=self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_annotationElementValueArrayInitializer8118) 
                if self._state.backtracking == 0:
                    stream_LCURLY.add(LCURLY240)
                # Java.g:645:16: ( annotationElementValue ( COMMA annotationElementValue )* )?
                alt81 = 2
                LA81_0 = self.input.LA(1)

                if (LA81_0 == AT or LA81_0 == DEC or LA81_0 == INC or LA81_0 == LCURLY or LA81_0 == LESS_THAN or LA81_0 == LOGICAL_NOT or (LPAREN <= LA81_0 <= MINUS) or LA81_0 == NOT or LA81_0 == PLUS or LA81_0 == BOOLEAN or LA81_0 == BYTE or LA81_0 == CHAR or LA81_0 == DOUBLE or LA81_0 == FALSE or LA81_0 == FLOAT or (INT <= LA81_0 <= LONG) or (NEW <= LA81_0 <= NULL) or LA81_0 == SHORT or LA81_0 == SUPER or LA81_0 == THIS or LA81_0 == TRUE or LA81_0 == VOID or (IDENT <= LA81_0 <= STRING_LITERAL)) :
                    alt81 = 1
                if alt81 == 1:
                    # Java.g:645:17: annotationElementValue ( COMMA annotationElementValue )*
                    pass 
                    self._state.following.append(self.FOLLOW_annotationElementValue_in_annotationElementValueArrayInitializer8121)
                    annotationElementValue241 = self.annotationElementValue()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_annotationElementValue.add(annotationElementValue241.tree)
                    # Java.g:645:40: ( COMMA annotationElementValue )*
                    while True: #loop80
                        alt80 = 2
                        LA80_0 = self.input.LA(1)

                        if (LA80_0 == COMMA) :
                            LA80_1 = self.input.LA(2)

                            if (LA80_1 == AT or LA80_1 == DEC or LA80_1 == INC or LA80_1 == LCURLY or LA80_1 == LESS_THAN or LA80_1 == LOGICAL_NOT or (LPAREN <= LA80_1 <= MINUS) or LA80_1 == NOT or LA80_1 == PLUS or LA80_1 == BOOLEAN or LA80_1 == BYTE or LA80_1 == CHAR or LA80_1 == DOUBLE or LA80_1 == FALSE or LA80_1 == FLOAT or (INT <= LA80_1 <= LONG) or (NEW <= LA80_1 <= NULL) or LA80_1 == SHORT or LA80_1 == SUPER or LA80_1 == THIS or LA80_1 == TRUE or LA80_1 == VOID or (IDENT <= LA80_1 <= STRING_LITERAL)) :
                                alt80 = 1




                        if alt80 == 1:
                            # Java.g:645:41: COMMA annotationElementValue
                            pass 
                            COMMA242=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_annotationElementValueArrayInitializer8124) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA242)
                            self._state.following.append(self.FOLLOW_annotationElementValue_in_annotationElementValueArrayInitializer8126)
                            annotationElementValue243 = self.annotationElementValue()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_annotationElementValue.add(annotationElementValue243.tree)


                        else:
                            break #loop80





                # Java.g:645:74: ( COMMA )?
                alt82 = 2
                LA82_0 = self.input.LA(1)

                if (LA82_0 == COMMA) :
                    alt82 = 1
                if alt82 == 1:
                    # Java.g:645:75: COMMA
                    pass 
                    COMMA244=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_annotationElementValueArrayInitializer8133) 
                    if self._state.backtracking == 0:
                        stream_COMMA.add(COMMA244)



                RCURLY245=self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_annotationElementValueArrayInitializer8137) 
                if self._state.backtracking == 0:
                    stream_RCURLY.add(RCURLY245)

                # AST Rewrite
                # elements: annotationElementValue
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 646:9: -> ^( ANNOTATION_INIT_ARRAY_ELEMENT[$LCURLY, \"ANNOTATION_ELEM_VALUE_ARRAY_INIT\"] ( annotationElementValue )* )
                    # Java.g:646:13: ^( ANNOTATION_INIT_ARRAY_ELEMENT[$LCURLY, \"ANNOTATION_ELEM_VALUE_ARRAY_INIT\"] ( annotationElementValue )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.create(ANNOTATION_INIT_ARRAY_ELEMENT, LCURLY240, "ANNOTATION_ELEM_VALUE_ARRAY_INIT"), root_1)

                    # Java.g:646:90: ( annotationElementValue )*
                    while stream_annotationElementValue.hasNext():
                        self._adaptor.addChild(root_1, stream_annotationElementValue.nextTree())


                    stream_annotationElementValue.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 67, annotationElementValueArrayInitializer_StartIndex, success)

            pass

        return retval

    # $ANTLR end "annotationElementValueArrayInitializer"

    class annotationTypeDeclaration_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "annotationTypeDeclaration"
    # Java.g:649:1: annotationTypeDeclaration[modifiers] : AT INTERFACE IDENT annotationBody -> ^( AT IDENT annotationBody ) ;
    def annotationTypeDeclaration(self, modifiers):

        retval = self.annotationTypeDeclaration_return()
        retval.start = self.input.LT(1)
        annotationTypeDeclaration_StartIndex = self.input.index()
        root_0 = None

        AT246 = None
        INTERFACE247 = None
        IDENT248 = None
        annotationBody249 = None


        AT246_tree = None
        INTERFACE247_tree = None
        IDENT248_tree = None
        stream_AT = RewriteRuleTokenStream(self._adaptor, "token AT")
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_INTERFACE = RewriteRuleTokenStream(self._adaptor, "token INTERFACE")
        stream_annotationBody = RewriteRuleSubtreeStream(self._adaptor, "rule annotationBody")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 68):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:650:5: ( AT INTERFACE IDENT annotationBody -> ^( AT IDENT annotationBody ) )
                # Java.g:650:9: AT INTERFACE IDENT annotationBody
                pass 
                AT246=self.match(self.input, AT, self.FOLLOW_AT_in_annotationTypeDeclaration8176) 
                if self._state.backtracking == 0:
                    stream_AT.add(AT246)
                INTERFACE247=self.match(self.input, INTERFACE, self.FOLLOW_INTERFACE_in_annotationTypeDeclaration8178) 
                if self._state.backtracking == 0:
                    stream_INTERFACE.add(INTERFACE247)
                IDENT248=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_annotationTypeDeclaration8180) 
                if self._state.backtracking == 0:
                    stream_IDENT.add(IDENT248)
                self._state.following.append(self.FOLLOW_annotationBody_in_annotationTypeDeclaration8182)
                annotationBody249 = self.annotationBody()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_annotationBody.add(annotationBody249.tree)

                # AST Rewrite
                # elements: annotationBody, AT, IDENT
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 651:9: -> ^( AT IDENT annotationBody )
                    # Java.g:651:12: ^( AT IDENT annotationBody )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_AT.nextNode(), root_1)

                    self._adaptor.addChild(root_1, modifiers)
                    self._adaptor.addChild(root_1, stream_IDENT.nextNode())
                    self._adaptor.addChild(root_1, stream_annotationBody.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 68, annotationTypeDeclaration_StartIndex, success)

            pass

        return retval

    # $ANTLR end "annotationTypeDeclaration"

    class annotationBody_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "annotationBody"
    # Java.g:654:1: annotationBody : LCURLY ( annotationScopeDeclarations )* RCURLY -> ^( ANNOTATION_TOP_LEVEL_SCOPE[$LCURLY, \"CLASS_TOP_LEVEL_SCOPE\"] ( annotationScopeDeclarations )* ) ;
    def annotationBody(self, ):

        retval = self.annotationBody_return()
        retval.start = self.input.LT(1)
        annotationBody_StartIndex = self.input.index()
        root_0 = None

        LCURLY250 = None
        RCURLY252 = None
        annotationScopeDeclarations251 = None


        LCURLY250_tree = None
        RCURLY252_tree = None
        stream_LCURLY = RewriteRuleTokenStream(self._adaptor, "token LCURLY")
        stream_RCURLY = RewriteRuleTokenStream(self._adaptor, "token RCURLY")
        stream_annotationScopeDeclarations = RewriteRuleSubtreeStream(self._adaptor, "rule annotationScopeDeclarations")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 69):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:655:5: ( LCURLY ( annotationScopeDeclarations )* RCURLY -> ^( ANNOTATION_TOP_LEVEL_SCOPE[$LCURLY, \"CLASS_TOP_LEVEL_SCOPE\"] ( annotationScopeDeclarations )* ) )
                # Java.g:655:9: LCURLY ( annotationScopeDeclarations )* RCURLY
                pass 
                LCURLY250=self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_annotationBody8221) 
                if self._state.backtracking == 0:
                    stream_LCURLY.add(LCURLY250)
                # Java.g:655:16: ( annotationScopeDeclarations )*
                while True: #loop83
                    alt83 = 2
                    LA83_0 = self.input.LA(1)

                    if (LA83_0 == AT or LA83_0 == LESS_THAN or LA83_0 == ABSTRACT or LA83_0 == BOOLEAN or LA83_0 == BYTE or (CHAR <= LA83_0 <= CLASS) or LA83_0 == DOUBLE or LA83_0 == ENUM or LA83_0 == FINAL or LA83_0 == FLOAT or LA83_0 == INTERFACE or (INT <= LA83_0 <= NATIVE) or (PRIVATE <= LA83_0 <= PUBLIC) or (SHORT <= LA83_0 <= STRICTFP) or LA83_0 == SYNCHRONIZED or LA83_0 == TRANSIENT or (VOID <= LA83_0 <= VOLATILE) or LA83_0 == IDENT) :
                        alt83 = 1


                    if alt83 == 1:
                        # Java.g:0:0: annotationScopeDeclarations
                        pass 
                        self._state.following.append(self.FOLLOW_annotationScopeDeclarations_in_annotationBody8223)
                        annotationScopeDeclarations251 = self.annotationScopeDeclarations()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_annotationScopeDeclarations.add(annotationScopeDeclarations251.tree)


                    else:
                        break #loop83


                RCURLY252=self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_annotationBody8226) 
                if self._state.backtracking == 0:
                    stream_RCURLY.add(RCURLY252)

                # AST Rewrite
                # elements: annotationScopeDeclarations
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 656:9: -> ^( ANNOTATION_TOP_LEVEL_SCOPE[$LCURLY, \"CLASS_TOP_LEVEL_SCOPE\"] ( annotationScopeDeclarations )* )
                    # Java.g:656:13: ^( ANNOTATION_TOP_LEVEL_SCOPE[$LCURLY, \"CLASS_TOP_LEVEL_SCOPE\"] ( annotationScopeDeclarations )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.create(ANNOTATION_TOP_LEVEL_SCOPE, LCURLY250, "CLASS_TOP_LEVEL_SCOPE"), root_1)

                    # Java.g:656:76: ( annotationScopeDeclarations )*
                    while stream_annotationScopeDeclarations.hasNext():
                        self._adaptor.addChild(root_1, stream_annotationScopeDeclarations.nextTree())


                    stream_annotationScopeDeclarations.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 69, annotationBody_StartIndex, success)

            pass

        return retval

    # $ANTLR end "annotationBody"

    class annotationScopeDeclarations_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "annotationScopeDeclarations"
    # Java.g:659:1: annotationScopeDeclarations : ( modifierList type ( IDENT LPAREN RPAREN ( annotationDefaultValue )? SEMI -> ^( ANNOTATION_METHOD_DECL modifierList type IDENT ( annotationDefaultValue )? ) | classFieldDeclaratorList SEMI -> ^( VAR_DECLARATION modifierList type classFieldDeclaratorList ) ) | typeDeclaration );
    def annotationScopeDeclarations(self, ):

        retval = self.annotationScopeDeclarations_return()
        retval.start = self.input.LT(1)
        annotationScopeDeclarations_StartIndex = self.input.index()
        root_0 = None

        IDENT255 = None
        LPAREN256 = None
        RPAREN257 = None
        SEMI259 = None
        SEMI261 = None
        modifierList253 = None

        type254 = None

        annotationDefaultValue258 = None

        classFieldDeclaratorList260 = None

        typeDeclaration262 = None


        IDENT255_tree = None
        LPAREN256_tree = None
        RPAREN257_tree = None
        SEMI259_tree = None
        SEMI261_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_modifierList = RewriteRuleSubtreeStream(self._adaptor, "rule modifierList")
        stream_annotationDefaultValue = RewriteRuleSubtreeStream(self._adaptor, "rule annotationDefaultValue")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        stream_classFieldDeclaratorList = RewriteRuleSubtreeStream(self._adaptor, "rule classFieldDeclaratorList")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 70):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:660:5: ( modifierList type ( IDENT LPAREN RPAREN ( annotationDefaultValue )? SEMI -> ^( ANNOTATION_METHOD_DECL modifierList type IDENT ( annotationDefaultValue )? ) | classFieldDeclaratorList SEMI -> ^( VAR_DECLARATION modifierList type classFieldDeclaratorList ) ) | typeDeclaration )
                alt86 = 2
                alt86 = self.dfa86.predict(self.input)
                if alt86 == 1:
                    # Java.g:660:9: modifierList type ( IDENT LPAREN RPAREN ( annotationDefaultValue )? SEMI -> ^( ANNOTATION_METHOD_DECL modifierList type IDENT ( annotationDefaultValue )? ) | classFieldDeclaratorList SEMI -> ^( VAR_DECLARATION modifierList type classFieldDeclaratorList ) )
                    pass 
                    self._state.following.append(self.FOLLOW_modifierList_in_annotationScopeDeclarations8264)
                    modifierList253 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_modifierList.add(modifierList253.tree)
                    self._state.following.append(self.FOLLOW_type_in_annotationScopeDeclarations8266)
                    type254 = self.type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_type.add(type254.tree)
                    # Java.g:661:9: ( IDENT LPAREN RPAREN ( annotationDefaultValue )? SEMI -> ^( ANNOTATION_METHOD_DECL modifierList type IDENT ( annotationDefaultValue )? ) | classFieldDeclaratorList SEMI -> ^( VAR_DECLARATION modifierList type classFieldDeclaratorList ) )
                    alt85 = 2
                    LA85_0 = self.input.LA(1)

                    if (LA85_0 == IDENT) :
                        LA85_1 = self.input.LA(2)

                        if (LA85_1 == LPAREN) :
                            alt85 = 1
                        elif (LA85_1 == ASSIGN or LA85_1 == COMMA or LA85_1 == LBRACK or LA85_1 == SEMI) :
                            alt85 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 85, 1, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 85, 0, self.input)

                        raise nvae

                    if alt85 == 1:
                        # Java.g:661:13: IDENT LPAREN RPAREN ( annotationDefaultValue )? SEMI
                        pass 
                        IDENT255=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_annotationScopeDeclarations8280) 
                        if self._state.backtracking == 0:
                            stream_IDENT.add(IDENT255)
                        LPAREN256=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_annotationScopeDeclarations8282) 
                        if self._state.backtracking == 0:
                            stream_LPAREN.add(LPAREN256)
                        RPAREN257=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_annotationScopeDeclarations8284) 
                        if self._state.backtracking == 0:
                            stream_RPAREN.add(RPAREN257)
                        # Java.g:661:33: ( annotationDefaultValue )?
                        alt84 = 2
                        LA84_0 = self.input.LA(1)

                        if (LA84_0 == DEFAULT) :
                            alt84 = 1
                        if alt84 == 1:
                            # Java.g:0:0: annotationDefaultValue
                            pass 
                            self._state.following.append(self.FOLLOW_annotationDefaultValue_in_annotationScopeDeclarations8286)
                            annotationDefaultValue258 = self.annotationDefaultValue()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_annotationDefaultValue.add(annotationDefaultValue258.tree)



                        SEMI259=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_annotationScopeDeclarations8289) 
                        if self._state.backtracking == 0:
                            stream_SEMI.add(SEMI259)

                        # AST Rewrite
                        # elements: annotationDefaultValue, modifierList, IDENT, type
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 662:13: -> ^( ANNOTATION_METHOD_DECL modifierList type IDENT ( annotationDefaultValue )? )
                            # Java.g:662:17: ^( ANNOTATION_METHOD_DECL modifierList type IDENT ( annotationDefaultValue )? )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ANNOTATION_METHOD_DECL, "ANNOTATION_METHOD_DECL"), root_1)

                            self._adaptor.addChild(root_1, stream_modifierList.nextTree())
                            self._adaptor.addChild(root_1, stream_type.nextTree())
                            self._adaptor.addChild(root_1, stream_IDENT.nextNode())
                            # Java.g:662:66: ( annotationDefaultValue )?
                            if stream_annotationDefaultValue.hasNext():
                                self._adaptor.addChild(root_1, stream_annotationDefaultValue.nextTree())


                            stream_annotationDefaultValue.reset();

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt85 == 2:
                        # Java.g:663:13: classFieldDeclaratorList SEMI
                        pass 
                        self._state.following.append(self.FOLLOW_classFieldDeclaratorList_in_annotationScopeDeclarations8331)
                        classFieldDeclaratorList260 = self.classFieldDeclaratorList()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_classFieldDeclaratorList.add(classFieldDeclaratorList260.tree)
                        SEMI261=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_annotationScopeDeclarations8333) 
                        if self._state.backtracking == 0:
                            stream_SEMI.add(SEMI261)

                        # AST Rewrite
                        # elements: type, modifierList, classFieldDeclaratorList
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 664:13: -> ^( VAR_DECLARATION modifierList type classFieldDeclaratorList )
                            # Java.g:664:17: ^( VAR_DECLARATION modifierList type classFieldDeclaratorList )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAR_DECLARATION, "VAR_DECLARATION"), root_1)

                            self._adaptor.addChild(root_1, stream_modifierList.nextTree())
                            self._adaptor.addChild(root_1, stream_type.nextTree())
                            self._adaptor.addChild(root_1, stream_classFieldDeclaratorList.nextTree())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0





                elif alt86 == 2:
                    # Java.g:666:9: typeDeclaration
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_typeDeclaration_in_annotationScopeDeclarations8378)
                    typeDeclaration262 = self.typeDeclaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, typeDeclaration262.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 70, annotationScopeDeclarations_StartIndex, success)

            pass

        return retval

    # $ANTLR end "annotationScopeDeclarations"

    class annotationDefaultValue_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "annotationDefaultValue"
    # Java.g:669:1: annotationDefaultValue : DEFAULT annotationElementValue ;
    def annotationDefaultValue(self, ):

        retval = self.annotationDefaultValue_return()
        retval.start = self.input.LT(1)
        annotationDefaultValue_StartIndex = self.input.index()
        root_0 = None

        DEFAULT263 = None
        annotationElementValue264 = None


        DEFAULT263_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 71):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:670:5: ( DEFAULT annotationElementValue )
                # Java.g:670:9: DEFAULT annotationElementValue
                pass 
                root_0 = self._adaptor.nil()

                DEFAULT263=self.match(self.input, DEFAULT, self.FOLLOW_DEFAULT_in_annotationDefaultValue8397)
                if self._state.backtracking == 0:

                    DEFAULT263_tree = self._adaptor.createWithPayload(DEFAULT263)
                    root_0 = self._adaptor.becomeRoot(DEFAULT263_tree, root_0)

                self._state.following.append(self.FOLLOW_annotationElementValue_in_annotationDefaultValue8400)
                annotationElementValue264 = self.annotationElementValue()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, annotationElementValue264.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 71, annotationDefaultValue_StartIndex, success)

            pass

        return retval

    # $ANTLR end "annotationDefaultValue"

    class block_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "block"
    # Java.g:675:1: block : LCURLY ( blockStatement )* RCURLY -> ^( BLOCK_SCOPE[$LCURLY, \"BLOCK_SCOPE\"] ( blockStatement )* ) ;
    def block(self, ):

        retval = self.block_return()
        retval.start = self.input.LT(1)
        block_StartIndex = self.input.index()
        root_0 = None

        LCURLY265 = None
        RCURLY267 = None
        blockStatement266 = None


        LCURLY265_tree = None
        RCURLY267_tree = None
        stream_LCURLY = RewriteRuleTokenStream(self._adaptor, "token LCURLY")
        stream_RCURLY = RewriteRuleTokenStream(self._adaptor, "token RCURLY")
        stream_blockStatement = RewriteRuleSubtreeStream(self._adaptor, "rule blockStatement")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 72):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:676:5: ( LCURLY ( blockStatement )* RCURLY -> ^( BLOCK_SCOPE[$LCURLY, \"BLOCK_SCOPE\"] ( blockStatement )* ) )
                # Java.g:676:9: LCURLY ( blockStatement )* RCURLY
                pass 
                LCURLY265=self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_block8421) 
                if self._state.backtracking == 0:
                    stream_LCURLY.add(LCURLY265)
                # Java.g:676:16: ( blockStatement )*
                while True: #loop87
                    alt87 = 2
                    LA87_0 = self.input.LA(1)

                    if (LA87_0 == AT or LA87_0 == DEC or LA87_0 == INC or LA87_0 == LCURLY or LA87_0 == LESS_THAN or LA87_0 == LOGICAL_NOT or (LPAREN <= LA87_0 <= MINUS) or LA87_0 == NOT or LA87_0 == PLUS or LA87_0 == SEMI or (ABSTRACT <= LA87_0 <= BYTE) or (CHAR <= LA87_0 <= CONTINUE) or (DO <= LA87_0 <= DOUBLE) or LA87_0 == ENUM or (FALSE <= LA87_0 <= FINAL) or (FLOAT <= LA87_0 <= IF) or LA87_0 == INTERFACE or (INT <= LA87_0 <= NULL) or (PRIVATE <= LA87_0 <= THROW) or (TRANSIENT <= LA87_0 <= WHILE) or (IDENT <= LA87_0 <= STRING_LITERAL)) :
                        alt87 = 1


                    if alt87 == 1:
                        # Java.g:0:0: blockStatement
                        pass 
                        self._state.following.append(self.FOLLOW_blockStatement_in_block8423)
                        blockStatement266 = self.blockStatement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_blockStatement.add(blockStatement266.tree)


                    else:
                        break #loop87


                RCURLY267=self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_block8426) 
                if self._state.backtracking == 0:
                    stream_RCURLY.add(RCURLY267)

                # AST Rewrite
                # elements: blockStatement
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 677:9: -> ^( BLOCK_SCOPE[$LCURLY, \"BLOCK_SCOPE\"] ( blockStatement )* )
                    # Java.g:677:13: ^( BLOCK_SCOPE[$LCURLY, \"BLOCK_SCOPE\"] ( blockStatement )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.create(BLOCK_SCOPE, LCURLY265, "BLOCK_SCOPE"), root_1)

                    # Java.g:677:51: ( blockStatement )*
                    while stream_blockStatement.hasNext():
                        self._adaptor.addChild(root_1, stream_blockStatement.nextTree())


                    stream_blockStatement.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 72, block_StartIndex, success)

            pass

        return retval

    # $ANTLR end "block"

    class blockStatement_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "blockStatement"
    # Java.g:680:1: blockStatement : ( localVariableDeclaration SEMI | typeDeclaration | statement );
    def blockStatement(self, ):

        retval = self.blockStatement_return()
        retval.start = self.input.LT(1)
        blockStatement_StartIndex = self.input.index()
        root_0 = None

        SEMI269 = None
        localVariableDeclaration268 = None

        typeDeclaration270 = None

        statement271 = None


        SEMI269_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 73):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:681:5: ( localVariableDeclaration SEMI | typeDeclaration | statement )
                alt88 = 3
                alt88 = self.dfa88.predict(self.input)
                if alt88 == 1:
                    # Java.g:681:9: localVariableDeclaration SEMI
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_localVariableDeclaration_in_blockStatement8464)
                    localVariableDeclaration268 = self.localVariableDeclaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, localVariableDeclaration268.tree)
                    SEMI269=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_blockStatement8466)


                elif alt88 == 2:
                    # Java.g:682:9: typeDeclaration
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_typeDeclaration_in_blockStatement8477)
                    typeDeclaration270 = self.typeDeclaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, typeDeclaration270.tree)


                elif alt88 == 3:
                    # Java.g:683:9: statement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_statement_in_blockStatement8487)
                    statement271 = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statement271.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 73, blockStatement_StartIndex, success)

            pass

        return retval

    # $ANTLR end "blockStatement"

    class localVariableDeclaration_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "localVariableDeclaration"
    # Java.g:686:1: localVariableDeclaration : localModifierList type classFieldDeclaratorList -> ^( VAR_DECLARATION localModifierList type classFieldDeclaratorList ) ;
    def localVariableDeclaration(self, ):

        retval = self.localVariableDeclaration_return()
        retval.start = self.input.LT(1)
        localVariableDeclaration_StartIndex = self.input.index()
        root_0 = None

        localModifierList272 = None

        type273 = None

        classFieldDeclaratorList274 = None


        stream_localModifierList = RewriteRuleSubtreeStream(self._adaptor, "rule localModifierList")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        stream_classFieldDeclaratorList = RewriteRuleSubtreeStream(self._adaptor, "rule classFieldDeclaratorList")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 74):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:687:5: ( localModifierList type classFieldDeclaratorList -> ^( VAR_DECLARATION localModifierList type classFieldDeclaratorList ) )
                # Java.g:687:9: localModifierList type classFieldDeclaratorList
                pass 
                self._state.following.append(self.FOLLOW_localModifierList_in_localVariableDeclaration8506)
                localModifierList272 = self.localModifierList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_localModifierList.add(localModifierList272.tree)
                self._state.following.append(self.FOLLOW_type_in_localVariableDeclaration8508)
                type273 = self.type()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_type.add(type273.tree)
                self._state.following.append(self.FOLLOW_classFieldDeclaratorList_in_localVariableDeclaration8510)
                classFieldDeclaratorList274 = self.classFieldDeclaratorList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_classFieldDeclaratorList.add(classFieldDeclaratorList274.tree)

                # AST Rewrite
                # elements: classFieldDeclaratorList, type, localModifierList
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 688:9: -> ^( VAR_DECLARATION localModifierList type classFieldDeclaratorList )
                    # Java.g:688:13: ^( VAR_DECLARATION localModifierList type classFieldDeclaratorList )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAR_DECLARATION, "VAR_DECLARATION"), root_1)

                    self._adaptor.addChild(root_1, stream_localModifierList.nextTree())
                    self._adaptor.addChild(root_1, stream_type.nextTree())
                    self._adaptor.addChild(root_1, stream_classFieldDeclaratorList.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 74, localVariableDeclaration_StartIndex, success)

            pass

        return retval

    # $ANTLR end "localVariableDeclaration"

    class statement_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "statement"
    # Java.g:692:1: statement : ( block | ASSERT expr1= expression ( COLON expr2= expression SEMI -> ^( ASSERT $expr1 $expr2) | SEMI -> ^( ASSERT $expr1) ) | IF parenthesizedExpression ifStat= statement ( ELSE elseStat= statement -> ^( IF parenthesizedExpression $ifStat $elseStat) | -> ^( IF parenthesizedExpression $ifStat) ) | FOR LPAREN ( forInit SEMI forCondition SEMI forUpdater RPAREN statement -> ^( FOR forInit forCondition forUpdater statement ) | localModifierList type IDENT COLON expression RPAREN statement -> ^( FOR_EACH[$FOR, \"FOR_EACH\"] localModifierList type IDENT expression statement ) ) | WHILE parenthesizedExpression statement -> ^( WHILE parenthesizedExpression statement ) | DO statement WHILE parenthesizedExpression SEMI -> ^( DO statement parenthesizedExpression ) | TRY block ( catches ( finallyClause )? | finallyClause ) -> ^( TRY block ( catches )? ( finallyClause )? ) | SWITCH parenthesizedExpression LCURLY switchBlockLabels RCURLY -> ^( SWITCH parenthesizedExpression switchBlockLabels ) | SYNCHRONIZED parenthesizedExpression block -> ^( SYNCHRONIZED parenthesizedExpression block ) | RETURN ( expression )? SEMI -> ^( RETURN ( expression )? ) | THROW expression SEMI -> ^( THROW expression ) | BREAK ( IDENT )? SEMI -> ^( BREAK ( IDENT )? ) | CONTINUE ( IDENT )? SEMI -> ^( CONTINUE ( IDENT )? ) | IDENT COLON statement -> ^( LABELED_STATEMENT IDENT statement ) | expression SEMI | SEMI );
    def statement(self, ):

        retval = self.statement_return()
        retval.start = self.input.LT(1)
        statement_StartIndex = self.input.index()
        root_0 = None

        ASSERT276 = None
        COLON277 = None
        SEMI278 = None
        SEMI279 = None
        IF280 = None
        ELSE282 = None
        FOR283 = None
        LPAREN284 = None
        SEMI286 = None
        SEMI288 = None
        RPAREN290 = None
        IDENT294 = None
        COLON295 = None
        RPAREN297 = None
        WHILE299 = None
        DO302 = None
        WHILE304 = None
        SEMI306 = None
        TRY307 = None
        SWITCH312 = None
        LCURLY314 = None
        RCURLY316 = None
        SYNCHRONIZED317 = None
        RETURN320 = None
        SEMI322 = None
        THROW323 = None
        SEMI325 = None
        BREAK326 = None
        IDENT327 = None
        SEMI328 = None
        CONTINUE329 = None
        IDENT330 = None
        SEMI331 = None
        IDENT332 = None
        COLON333 = None
        SEMI336 = None
        SEMI337 = None
        expr1 = None

        expr2 = None

        ifStat = None

        elseStat = None

        block275 = None

        parenthesizedExpression281 = None

        forInit285 = None

        forCondition287 = None

        forUpdater289 = None

        statement291 = None

        localModifierList292 = None

        type293 = None

        expression296 = None

        statement298 = None

        parenthesizedExpression300 = None

        statement301 = None

        statement303 = None

        parenthesizedExpression305 = None

        block308 = None

        catches309 = None

        finallyClause310 = None

        finallyClause311 = None

        parenthesizedExpression313 = None

        switchBlockLabels315 = None

        parenthesizedExpression318 = None

        block319 = None

        expression321 = None

        expression324 = None

        statement334 = None

        expression335 = None


        ASSERT276_tree = None
        COLON277_tree = None
        SEMI278_tree = None
        SEMI279_tree = None
        IF280_tree = None
        ELSE282_tree = None
        FOR283_tree = None
        LPAREN284_tree = None
        SEMI286_tree = None
        SEMI288_tree = None
        RPAREN290_tree = None
        IDENT294_tree = None
        COLON295_tree = None
        RPAREN297_tree = None
        WHILE299_tree = None
        DO302_tree = None
        WHILE304_tree = None
        SEMI306_tree = None
        TRY307_tree = None
        SWITCH312_tree = None
        LCURLY314_tree = None
        RCURLY316_tree = None
        SYNCHRONIZED317_tree = None
        RETURN320_tree = None
        SEMI322_tree = None
        THROW323_tree = None
        SEMI325_tree = None
        BREAK326_tree = None
        IDENT327_tree = None
        SEMI328_tree = None
        CONTINUE329_tree = None
        IDENT330_tree = None
        SEMI331_tree = None
        IDENT332_tree = None
        COLON333_tree = None
        SEMI336_tree = None
        SEMI337_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_SYNCHRONIZED = RewriteRuleTokenStream(self._adaptor, "token SYNCHRONIZED")
        stream_WHILE = RewriteRuleTokenStream(self._adaptor, "token WHILE")
        stream_CONTINUE = RewriteRuleTokenStream(self._adaptor, "token CONTINUE")
        stream_SWITCH = RewriteRuleTokenStream(self._adaptor, "token SWITCH")
        stream_RCURLY = RewriteRuleTokenStream(self._adaptor, "token RCURLY")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_RETURN = RewriteRuleTokenStream(self._adaptor, "token RETURN")
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_FOR = RewriteRuleTokenStream(self._adaptor, "token FOR")
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_LCURLY = RewriteRuleTokenStream(self._adaptor, "token LCURLY")
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_ASSERT = RewriteRuleTokenStream(self._adaptor, "token ASSERT")
        stream_BREAK = RewriteRuleTokenStream(self._adaptor, "token BREAK")
        stream_THROW = RewriteRuleTokenStream(self._adaptor, "token THROW")
        stream_TRY = RewriteRuleTokenStream(self._adaptor, "token TRY")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        stream_finallyClause = RewriteRuleSubtreeStream(self._adaptor, "rule finallyClause")
        stream_catches = RewriteRuleSubtreeStream(self._adaptor, "rule catches")
        stream_forUpdater = RewriteRuleSubtreeStream(self._adaptor, "rule forUpdater")
        stream_block = RewriteRuleSubtreeStream(self._adaptor, "rule block")
        stream_forCondition = RewriteRuleSubtreeStream(self._adaptor, "rule forCondition")
        stream_localModifierList = RewriteRuleSubtreeStream(self._adaptor, "rule localModifierList")
        stream_forInit = RewriteRuleSubtreeStream(self._adaptor, "rule forInit")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        stream_switchBlockLabels = RewriteRuleSubtreeStream(self._adaptor, "rule switchBlockLabels")
        stream_parenthesizedExpression = RewriteRuleSubtreeStream(self._adaptor, "rule parenthesizedExpression")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 75):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:693:5: ( block | ASSERT expr1= expression ( COLON expr2= expression SEMI -> ^( ASSERT $expr1 $expr2) | SEMI -> ^( ASSERT $expr1) ) | IF parenthesizedExpression ifStat= statement ( ELSE elseStat= statement -> ^( IF parenthesizedExpression $ifStat $elseStat) | -> ^( IF parenthesizedExpression $ifStat) ) | FOR LPAREN ( forInit SEMI forCondition SEMI forUpdater RPAREN statement -> ^( FOR forInit forCondition forUpdater statement ) | localModifierList type IDENT COLON expression RPAREN statement -> ^( FOR_EACH[$FOR, \"FOR_EACH\"] localModifierList type IDENT expression statement ) ) | WHILE parenthesizedExpression statement -> ^( WHILE parenthesizedExpression statement ) | DO statement WHILE parenthesizedExpression SEMI -> ^( DO statement parenthesizedExpression ) | TRY block ( catches ( finallyClause )? | finallyClause ) -> ^( TRY block ( catches )? ( finallyClause )? ) | SWITCH parenthesizedExpression LCURLY switchBlockLabels RCURLY -> ^( SWITCH parenthesizedExpression switchBlockLabels ) | SYNCHRONIZED parenthesizedExpression block -> ^( SYNCHRONIZED parenthesizedExpression block ) | RETURN ( expression )? SEMI -> ^( RETURN ( expression )? ) | THROW expression SEMI -> ^( THROW expression ) | BREAK ( IDENT )? SEMI -> ^( BREAK ( IDENT )? ) | CONTINUE ( IDENT )? SEMI -> ^( CONTINUE ( IDENT )? ) | IDENT COLON statement -> ^( LABELED_STATEMENT IDENT statement ) | expression SEMI | SEMI )
                alt97 = 16
                alt97 = self.dfa97.predict(self.input)
                if alt97 == 1:
                    # Java.g:693:9: block
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_block_in_statement8551)
                    block275 = self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, block275.tree)


                elif alt97 == 2:
                    # Java.g:694:9: ASSERT expr1= expression ( COLON expr2= expression SEMI -> ^( ASSERT $expr1 $expr2) | SEMI -> ^( ASSERT $expr1) )
                    pass 
                    ASSERT276=self.match(self.input, ASSERT, self.FOLLOW_ASSERT_in_statement8561) 
                    if self._state.backtracking == 0:
                        stream_ASSERT.add(ASSERT276)
                    self._state.following.append(self.FOLLOW_expression_in_statement8565)
                    expr1 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expr1.tree)
                    # Java.g:695:9: ( COLON expr2= expression SEMI -> ^( ASSERT $expr1 $expr2) | SEMI -> ^( ASSERT $expr1) )
                    alt89 = 2
                    LA89_0 = self.input.LA(1)

                    if (LA89_0 == COLON) :
                        alt89 = 1
                    elif (LA89_0 == SEMI) :
                        alt89 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 89, 0, self.input)

                        raise nvae

                    if alt89 == 1:
                        # Java.g:695:13: COLON expr2= expression SEMI
                        pass 
                        COLON277=self.match(self.input, COLON, self.FOLLOW_COLON_in_statement8579) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(COLON277)
                        self._state.following.append(self.FOLLOW_expression_in_statement8583)
                        expr2 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_expression.add(expr2.tree)
                        SEMI278=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement8585) 
                        if self._state.backtracking == 0:
                            stream_SEMI.add(SEMI278)

                        # AST Rewrite
                        # elements: expr2, expr1, ASSERT
                        # token labels: 
                        # rule labels: retval, expr1, expr2
                        # token list labels: 
                        # rule list labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            if expr1 is not None:
                                stream_expr1 = RewriteRuleSubtreeStream(self._adaptor, "token expr1", expr1.tree)
                            else:
                                stream_expr1 = RewriteRuleSubtreeStream(self._adaptor, "token expr1", None)


                            if expr2 is not None:
                                stream_expr2 = RewriteRuleSubtreeStream(self._adaptor, "token expr2", expr2.tree)
                            else:
                                stream_expr2 = RewriteRuleSubtreeStream(self._adaptor, "token expr2", None)


                            root_0 = self._adaptor.nil()
                            # 695:77: -> ^( ASSERT $expr1 $expr2)
                            # Java.g:695:81: ^( ASSERT $expr1 $expr2)
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(stream_ASSERT.nextNode(), root_1)

                            self._adaptor.addChild(root_1, stream_expr1.nextTree())
                            self._adaptor.addChild(root_1, stream_expr2.nextTree())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt89 == 2:
                        # Java.g:696:13: SEMI
                        pass 
                        SEMI279=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement8648) 
                        if self._state.backtracking == 0:
                            stream_SEMI.add(SEMI279)

                        # AST Rewrite
                        # elements: ASSERT, expr1
                        # token labels: 
                        # rule labels: retval, expr1
                        # token list labels: 
                        # rule list labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            if expr1 is not None:
                                stream_expr1 = RewriteRuleSubtreeStream(self._adaptor, "token expr1", expr1.tree)
                            else:
                                stream_expr1 = RewriteRuleSubtreeStream(self._adaptor, "token expr1", None)


                            root_0 = self._adaptor.nil()
                            # 696:77: -> ^( ASSERT $expr1)
                            # Java.g:696:81: ^( ASSERT $expr1)
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(stream_ASSERT.nextNode(), root_1)

                            self._adaptor.addChild(root_1, stream_expr1.nextTree())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0





                elif alt97 == 3:
                    # Java.g:698:9: IF parenthesizedExpression ifStat= statement ( ELSE elseStat= statement -> ^( IF parenthesizedExpression $ifStat $elseStat) | -> ^( IF parenthesizedExpression $ifStat) )
                    pass 
                    IF280=self.match(self.input, IF, self.FOLLOW_IF_in_statement8737) 
                    if self._state.backtracking == 0:
                        stream_IF.add(IF280)
                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_statement8739)
                    parenthesizedExpression281 = self.parenthesizedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parenthesizedExpression.add(parenthesizedExpression281.tree)
                    self._state.following.append(self.FOLLOW_statement_in_statement8743)
                    ifStat = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_statement.add(ifStat.tree)
                    # Java.g:699:9: ( ELSE elseStat= statement -> ^( IF parenthesizedExpression $ifStat $elseStat) | -> ^( IF parenthesizedExpression $ifStat) )
                    alt90 = 2
                    LA90_0 = self.input.LA(1)

                    if (LA90_0 == ELSE) :
                        LA90_1 = self.input.LA(2)

                        if (self.synpred121_Java()) :
                            alt90 = 1
                        elif (True) :
                            alt90 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 90, 1, self.input)

                            raise nvae

                    elif (LA90_0 == EOF or LA90_0 == AT or LA90_0 == DEC or LA90_0 == INC or LA90_0 == LCURLY or LA90_0 == LESS_THAN or LA90_0 == LOGICAL_NOT or (LPAREN <= LA90_0 <= MINUS) or LA90_0 == NOT or LA90_0 == PLUS or LA90_0 == RCURLY or LA90_0 == SEMI or (ABSTRACT <= LA90_0 <= CASE) or (CHAR <= LA90_0 <= DOUBLE) or LA90_0 == ENUM or (FALSE <= LA90_0 <= FINAL) or (FLOAT <= LA90_0 <= IF) or LA90_0 == INTERFACE or (INT <= LA90_0 <= NULL) or (PRIVATE <= LA90_0 <= THROW) or (TRANSIENT <= LA90_0 <= WHILE) or (IDENT <= LA90_0 <= STRING_LITERAL)) :
                        alt90 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 90, 0, self.input)

                        raise nvae

                    if alt90 == 1:
                        # Java.g:699:13: ELSE elseStat= statement
                        pass 
                        ELSE282=self.match(self.input, ELSE, self.FOLLOW_ELSE_in_statement8757) 
                        if self._state.backtracking == 0:
                            stream_ELSE.add(ELSE282)
                        self._state.following.append(self.FOLLOW_statement_in_statement8761)
                        elseStat = self.statement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_statement.add(elseStat.tree)

                        # AST Rewrite
                        # elements: ifStat, IF, elseStat, parenthesizedExpression
                        # token labels: 
                        # rule labels: retval, ifStat, elseStat
                        # token list labels: 
                        # rule list labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            if ifStat is not None:
                                stream_ifStat = RewriteRuleSubtreeStream(self._adaptor, "token ifStat", ifStat.tree)
                            else:
                                stream_ifStat = RewriteRuleSubtreeStream(self._adaptor, "token ifStat", None)


                            if elseStat is not None:
                                stream_elseStat = RewriteRuleSubtreeStream(self._adaptor, "token elseStat", elseStat.tree)
                            else:
                                stream_elseStat = RewriteRuleSubtreeStream(self._adaptor, "token elseStat", None)


                            root_0 = self._adaptor.nil()
                            # 699:77: -> ^( IF parenthesizedExpression $ifStat $elseStat)
                            # Java.g:699:81: ^( IF parenthesizedExpression $ifStat $elseStat)
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(stream_IF.nextNode(), root_1)

                            self._adaptor.addChild(root_1, stream_parenthesizedExpression.nextTree())
                            self._adaptor.addChild(root_1, stream_ifStat.nextTree())
                            self._adaptor.addChild(root_1, stream_elseStat.nextTree())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt90 == 2:
                        # Java.g:700:77: 
                        pass 
                        # AST Rewrite
                        # elements: parenthesizedExpression, IF, ifStat
                        # token labels: 
                        # rule labels: retval, ifStat
                        # token list labels: 
                        # rule list labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            if ifStat is not None:
                                stream_ifStat = RewriteRuleSubtreeStream(self._adaptor, "token ifStat", ifStat.tree)
                            else:
                                stream_ifStat = RewriteRuleSubtreeStream(self._adaptor, "token ifStat", None)


                            root_0 = self._adaptor.nil()
                            # 700:77: -> ^( IF parenthesizedExpression $ifStat)
                            # Java.g:700:81: ^( IF parenthesizedExpression $ifStat)
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(stream_IF.nextNode(), root_1)

                            self._adaptor.addChild(root_1, stream_parenthesizedExpression.nextTree())
                            self._adaptor.addChild(root_1, stream_ifStat.nextTree())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0





                elif alt97 == 4:
                    # Java.g:702:9: FOR LPAREN ( forInit SEMI forCondition SEMI forUpdater RPAREN statement -> ^( FOR forInit forCondition forUpdater statement ) | localModifierList type IDENT COLON expression RPAREN statement -> ^( FOR_EACH[$FOR, \"FOR_EACH\"] localModifierList type IDENT expression statement ) )
                    pass 
                    FOR283=self.match(self.input, FOR, self.FOLLOW_FOR_in_statement8924) 
                    if self._state.backtracking == 0:
                        stream_FOR.add(FOR283)
                    LPAREN284=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_statement8926) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN284)
                    # Java.g:703:9: ( forInit SEMI forCondition SEMI forUpdater RPAREN statement -> ^( FOR forInit forCondition forUpdater statement ) | localModifierList type IDENT COLON expression RPAREN statement -> ^( FOR_EACH[$FOR, \"FOR_EACH\"] localModifierList type IDENT expression statement ) )
                    alt91 = 2
                    alt91 = self.dfa91.predict(self.input)
                    if alt91 == 1:
                        # Java.g:703:13: forInit SEMI forCondition SEMI forUpdater RPAREN statement
                        pass 
                        self._state.following.append(self.FOLLOW_forInit_in_statement8940)
                        forInit285 = self.forInit()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_forInit.add(forInit285.tree)
                        SEMI286=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement8942) 
                        if self._state.backtracking == 0:
                            stream_SEMI.add(SEMI286)
                        self._state.following.append(self.FOLLOW_forCondition_in_statement8944)
                        forCondition287 = self.forCondition()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_forCondition.add(forCondition287.tree)
                        SEMI288=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement8946) 
                        if self._state.backtracking == 0:
                            stream_SEMI.add(SEMI288)
                        self._state.following.append(self.FOLLOW_forUpdater_in_statement8948)
                        forUpdater289 = self.forUpdater()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_forUpdater.add(forUpdater289.tree)
                        RPAREN290=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_statement8950) 
                        if self._state.backtracking == 0:
                            stream_RPAREN.add(RPAREN290)
                        self._state.following.append(self.FOLLOW_statement_in_statement8952)
                        statement291 = self.statement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_statement.add(statement291.tree)

                        # AST Rewrite
                        # elements: forCondition, statement, FOR, forInit, forUpdater
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 703:77: -> ^( FOR forInit forCondition forUpdater statement )
                            # Java.g:703:81: ^( FOR forInit forCondition forUpdater statement )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(stream_FOR.nextNode(), root_1)

                            self._adaptor.addChild(root_1, stream_forInit.nextTree())
                            self._adaptor.addChild(root_1, stream_forCondition.nextTree())
                            self._adaptor.addChild(root_1, stream_forUpdater.nextTree())
                            self._adaptor.addChild(root_1, stream_statement.nextTree())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt91 == 2:
                        # Java.g:704:13: localModifierList type IDENT COLON expression RPAREN statement
                        pass 
                        self._state.following.append(self.FOLLOW_localModifierList_in_statement8986)
                        localModifierList292 = self.localModifierList()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_localModifierList.add(localModifierList292.tree)
                        self._state.following.append(self.FOLLOW_type_in_statement8988)
                        type293 = self.type()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_type.add(type293.tree)
                        IDENT294=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_statement8990) 
                        if self._state.backtracking == 0:
                            stream_IDENT.add(IDENT294)
                        COLON295=self.match(self.input, COLON, self.FOLLOW_COLON_in_statement8992) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(COLON295)
                        self._state.following.append(self.FOLLOW_expression_in_statement8994)
                        expression296 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_expression.add(expression296.tree)
                        RPAREN297=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_statement8996) 
                        if self._state.backtracking == 0:
                            stream_RPAREN.add(RPAREN297)
                        self._state.following.append(self.FOLLOW_statement_in_statement8998)
                        statement298 = self.statement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_statement.add(statement298.tree)

                        # AST Rewrite
                        # elements: statement, type, IDENT, expression, localModifierList
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 705:77: -> ^( FOR_EACH[$FOR, \"FOR_EACH\"] localModifierList type IDENT expression statement )
                            # Java.g:705:81: ^( FOR_EACH[$FOR, \"FOR_EACH\"] localModifierList type IDENT expression statement )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.create(FOR_EACH, FOR283, "FOR_EACH"), root_1)

                            self._adaptor.addChild(root_1, stream_localModifierList.nextTree())
                            self._adaptor.addChild(root_1, stream_type.nextTree())
                            self._adaptor.addChild(root_1, stream_IDENT.nextNode())
                            self._adaptor.addChild(root_1, stream_expression.nextTree())
                            self._adaptor.addChild(root_1, stream_statement.nextTree())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0





                elif alt97 == 5:
                    # Java.g:707:9: WHILE parenthesizedExpression statement
                    pass 
                    WHILE299=self.match(self.input, WHILE, self.FOLLOW_WHILE_in_statement9112) 
                    if self._state.backtracking == 0:
                        stream_WHILE.add(WHILE299)
                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_statement9114)
                    parenthesizedExpression300 = self.parenthesizedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parenthesizedExpression.add(parenthesizedExpression300.tree)
                    self._state.following.append(self.FOLLOW_statement_in_statement9116)
                    statement301 = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_statement.add(statement301.tree)

                    # AST Rewrite
                    # elements: WHILE, statement, parenthesizedExpression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 707:77: -> ^( WHILE parenthesizedExpression statement )
                        # Java.g:707:81: ^( WHILE parenthesizedExpression statement )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_WHILE.nextNode(), root_1)

                        self._adaptor.addChild(root_1, stream_parenthesizedExpression.nextTree())
                        self._adaptor.addChild(root_1, stream_statement.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt97 == 6:
                    # Java.g:708:9: DO statement WHILE parenthesizedExpression SEMI
                    pass 
                    DO302=self.match(self.input, DO, self.FOLLOW_DO_in_statement9165) 
                    if self._state.backtracking == 0:
                        stream_DO.add(DO302)
                    self._state.following.append(self.FOLLOW_statement_in_statement9167)
                    statement303 = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_statement.add(statement303.tree)
                    WHILE304=self.match(self.input, WHILE, self.FOLLOW_WHILE_in_statement9169) 
                    if self._state.backtracking == 0:
                        stream_WHILE.add(WHILE304)
                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_statement9171)
                    parenthesizedExpression305 = self.parenthesizedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parenthesizedExpression.add(parenthesizedExpression305.tree)
                    SEMI306=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement9173) 
                    if self._state.backtracking == 0:
                        stream_SEMI.add(SEMI306)

                    # AST Rewrite
                    # elements: statement, parenthesizedExpression, DO
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 708:77: -> ^( DO statement parenthesizedExpression )
                        # Java.g:708:81: ^( DO statement parenthesizedExpression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_DO.nextNode(), root_1)

                        self._adaptor.addChild(root_1, stream_statement.nextTree())
                        self._adaptor.addChild(root_1, stream_parenthesizedExpression.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt97 == 7:
                    # Java.g:709:9: TRY block ( catches ( finallyClause )? | finallyClause )
                    pass 
                    TRY307=self.match(self.input, TRY, self.FOLLOW_TRY_in_statement9214) 
                    if self._state.backtracking == 0:
                        stream_TRY.add(TRY307)
                    self._state.following.append(self.FOLLOW_block_in_statement9216)
                    block308 = self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_block.add(block308.tree)
                    # Java.g:709:19: ( catches ( finallyClause )? | finallyClause )
                    alt93 = 2
                    LA93_0 = self.input.LA(1)

                    if (LA93_0 == CATCH) :
                        alt93 = 1
                    elif (LA93_0 == FINALLY) :
                        alt93 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 93, 0, self.input)

                        raise nvae

                    if alt93 == 1:
                        # Java.g:709:20: catches ( finallyClause )?
                        pass 
                        self._state.following.append(self.FOLLOW_catches_in_statement9219)
                        catches309 = self.catches()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_catches.add(catches309.tree)
                        # Java.g:709:28: ( finallyClause )?
                        alt92 = 2
                        LA92_0 = self.input.LA(1)

                        if (LA92_0 == FINALLY) :
                            alt92 = 1
                        if alt92 == 1:
                            # Java.g:0:0: finallyClause
                            pass 
                            self._state.following.append(self.FOLLOW_finallyClause_in_statement9221)
                            finallyClause310 = self.finallyClause()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_finallyClause.add(finallyClause310.tree)





                    elif alt93 == 2:
                        # Java.g:709:45: finallyClause
                        pass 
                        self._state.following.append(self.FOLLOW_finallyClause_in_statement9226)
                        finallyClause311 = self.finallyClause()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_finallyClause.add(finallyClause311.tree)




                    # AST Rewrite
                    # elements: finallyClause, catches, TRY, block
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 709:77: -> ^( TRY block ( catches )? ( finallyClause )? )
                        # Java.g:709:81: ^( TRY block ( catches )? ( finallyClause )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_TRY.nextNode(), root_1)

                        self._adaptor.addChild(root_1, stream_block.nextTree())
                        # Java.g:709:93: ( catches )?
                        if stream_catches.hasNext():
                            self._adaptor.addChild(root_1, stream_catches.nextTree())


                        stream_catches.reset();
                        # Java.g:709:102: ( finallyClause )?
                        if stream_finallyClause.hasNext():
                            self._adaptor.addChild(root_1, stream_finallyClause.nextTree())


                        stream_finallyClause.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt97 == 8:
                    # Java.g:710:9: SWITCH parenthesizedExpression LCURLY switchBlockLabels RCURLY
                    pass 
                    SWITCH312=self.match(self.input, SWITCH, self.FOLLOW_SWITCH_in_statement9269) 
                    if self._state.backtracking == 0:
                        stream_SWITCH.add(SWITCH312)
                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_statement9271)
                    parenthesizedExpression313 = self.parenthesizedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parenthesizedExpression.add(parenthesizedExpression313.tree)
                    LCURLY314=self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_statement9273) 
                    if self._state.backtracking == 0:
                        stream_LCURLY.add(LCURLY314)
                    self._state.following.append(self.FOLLOW_switchBlockLabels_in_statement9275)
                    switchBlockLabels315 = self.switchBlockLabels()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_switchBlockLabels.add(switchBlockLabels315.tree)
                    RCURLY316=self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_statement9277) 
                    if self._state.backtracking == 0:
                        stream_RCURLY.add(RCURLY316)

                    # AST Rewrite
                    # elements: parenthesizedExpression, SWITCH, switchBlockLabels
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 710:77: -> ^( SWITCH parenthesizedExpression switchBlockLabels )
                        # Java.g:710:81: ^( SWITCH parenthesizedExpression switchBlockLabels )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_SWITCH.nextNode(), root_1)

                        self._adaptor.addChild(root_1, stream_parenthesizedExpression.nextTree())
                        self._adaptor.addChild(root_1, stream_switchBlockLabels.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt97 == 9:
                    # Java.g:711:9: SYNCHRONIZED parenthesizedExpression block
                    pass 
                    SYNCHRONIZED317=self.match(self.input, SYNCHRONIZED, self.FOLLOW_SYNCHRONIZED_in_statement9303) 
                    if self._state.backtracking == 0:
                        stream_SYNCHRONIZED.add(SYNCHRONIZED317)
                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_statement9305)
                    parenthesizedExpression318 = self.parenthesizedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parenthesizedExpression.add(parenthesizedExpression318.tree)
                    self._state.following.append(self.FOLLOW_block_in_statement9307)
                    block319 = self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_block.add(block319.tree)

                    # AST Rewrite
                    # elements: parenthesizedExpression, SYNCHRONIZED, block
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 711:77: -> ^( SYNCHRONIZED parenthesizedExpression block )
                        # Java.g:711:81: ^( SYNCHRONIZED parenthesizedExpression block )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_SYNCHRONIZED.nextNode(), root_1)

                        self._adaptor.addChild(root_1, stream_parenthesizedExpression.nextTree())
                        self._adaptor.addChild(root_1, stream_block.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt97 == 10:
                    # Java.g:712:9: RETURN ( expression )? SEMI
                    pass 
                    RETURN320=self.match(self.input, RETURN, self.FOLLOW_RETURN_in_statement9353) 
                    if self._state.backtracking == 0:
                        stream_RETURN.add(RETURN320)
                    # Java.g:712:16: ( expression )?
                    alt94 = 2
                    LA94_0 = self.input.LA(1)

                    if (LA94_0 == DEC or LA94_0 == INC or LA94_0 == LESS_THAN or LA94_0 == LOGICAL_NOT or (LPAREN <= LA94_0 <= MINUS) or LA94_0 == NOT or LA94_0 == PLUS or LA94_0 == BOOLEAN or LA94_0 == BYTE or LA94_0 == CHAR or LA94_0 == DOUBLE or LA94_0 == FALSE or LA94_0 == FLOAT or (INT <= LA94_0 <= LONG) or (NEW <= LA94_0 <= NULL) or LA94_0 == SHORT or LA94_0 == SUPER or LA94_0 == THIS or LA94_0 == TRUE or LA94_0 == VOID or (IDENT <= LA94_0 <= STRING_LITERAL)) :
                        alt94 = 1
                    if alt94 == 1:
                        # Java.g:0:0: expression
                        pass 
                        self._state.following.append(self.FOLLOW_expression_in_statement9355)
                        expression321 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_expression.add(expression321.tree)



                    SEMI322=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement9358) 
                    if self._state.backtracking == 0:
                        stream_SEMI.add(SEMI322)

                    # AST Rewrite
                    # elements: expression, RETURN
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 712:77: -> ^( RETURN ( expression )? )
                        # Java.g:712:81: ^( RETURN ( expression )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_RETURN.nextNode(), root_1)

                        # Java.g:712:90: ( expression )?
                        if stream_expression.hasNext():
                            self._adaptor.addChild(root_1, stream_expression.nextTree())


                        stream_expression.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt97 == 11:
                    # Java.g:713:9: THROW expression SEMI
                    pass 
                    THROW323=self.match(self.input, THROW, self.FOLLOW_THROW_in_statement9422) 
                    if self._state.backtracking == 0:
                        stream_THROW.add(THROW323)
                    self._state.following.append(self.FOLLOW_expression_in_statement9424)
                    expression324 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression324.tree)
                    SEMI325=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement9426) 
                    if self._state.backtracking == 0:
                        stream_SEMI.add(SEMI325)

                    # AST Rewrite
                    # elements: expression, THROW
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 713:77: -> ^( THROW expression )
                        # Java.g:713:81: ^( THROW expression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_THROW.nextNode(), root_1)

                        self._adaptor.addChild(root_1, stream_expression.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt97 == 12:
                    # Java.g:714:9: BREAK ( IDENT )? SEMI
                    pass 
                    BREAK326=self.match(self.input, BREAK, self.FOLLOW_BREAK_in_statement9491) 
                    if self._state.backtracking == 0:
                        stream_BREAK.add(BREAK326)
                    # Java.g:714:15: ( IDENT )?
                    alt95 = 2
                    LA95_0 = self.input.LA(1)

                    if (LA95_0 == IDENT) :
                        alt95 = 1
                    if alt95 == 1:
                        # Java.g:0:0: IDENT
                        pass 
                        IDENT327=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_statement9493) 
                        if self._state.backtracking == 0:
                            stream_IDENT.add(IDENT327)



                    SEMI328=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement9496) 
                    if self._state.backtracking == 0:
                        stream_SEMI.add(SEMI328)

                    # AST Rewrite
                    # elements: BREAK, IDENT
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 714:77: -> ^( BREAK ( IDENT )? )
                        # Java.g:714:81: ^( BREAK ( IDENT )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_BREAK.nextNode(), root_1)

                        # Java.g:714:89: ( IDENT )?
                        if stream_IDENT.hasNext():
                            self._adaptor.addChild(root_1, stream_IDENT.nextNode())


                        stream_IDENT.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt97 == 13:
                    # Java.g:715:9: CONTINUE ( IDENT )? SEMI
                    pass 
                    CONTINUE329=self.match(self.input, CONTINUE, self.FOLLOW_CONTINUE_in_statement9566) 
                    if self._state.backtracking == 0:
                        stream_CONTINUE.add(CONTINUE329)
                    # Java.g:715:18: ( IDENT )?
                    alt96 = 2
                    LA96_0 = self.input.LA(1)

                    if (LA96_0 == IDENT) :
                        alt96 = 1
                    if alt96 == 1:
                        # Java.g:0:0: IDENT
                        pass 
                        IDENT330=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_statement9568) 
                        if self._state.backtracking == 0:
                            stream_IDENT.add(IDENT330)



                    SEMI331=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement9571) 
                    if self._state.backtracking == 0:
                        stream_SEMI.add(SEMI331)

                    # AST Rewrite
                    # elements: IDENT, CONTINUE
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 715:77: -> ^( CONTINUE ( IDENT )? )
                        # Java.g:715:81: ^( CONTINUE ( IDENT )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_CONTINUE.nextNode(), root_1)

                        # Java.g:715:92: ( IDENT )?
                        if stream_IDENT.hasNext():
                            self._adaptor.addChild(root_1, stream_IDENT.nextNode())


                        stream_IDENT.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt97 == 14:
                    # Java.g:716:9: IDENT COLON statement
                    pass 
                    IDENT332=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_statement9638) 
                    if self._state.backtracking == 0:
                        stream_IDENT.add(IDENT332)
                    COLON333=self.match(self.input, COLON, self.FOLLOW_COLON_in_statement9640) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON333)
                    self._state.following.append(self.FOLLOW_statement_in_statement9642)
                    statement334 = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_statement.add(statement334.tree)

                    # AST Rewrite
                    # elements: IDENT, statement
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 716:77: -> ^( LABELED_STATEMENT IDENT statement )
                        # Java.g:716:81: ^( LABELED_STATEMENT IDENT statement )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LABELED_STATEMENT, "LABELED_STATEMENT"), root_1)

                        self._adaptor.addChild(root_1, stream_IDENT.nextNode())
                        self._adaptor.addChild(root_1, stream_statement.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt97 == 15:
                    # Java.g:717:9: expression SEMI
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_expression_in_statement9709)
                    expression335 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression335.tree)
                    SEMI336=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement9711)


                elif alt97 == 16:
                    # Java.g:718:9: SEMI
                    pass 
                    root_0 = self._adaptor.nil()

                    SEMI337=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement9722)
                    if self._state.backtracking == 0:

                        SEMI337_tree = self._adaptor.createWithPayload(SEMI337)
                        self._adaptor.addChild(root_0, SEMI337_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 75, statement_StartIndex, success)

            pass

        return retval

    # $ANTLR end "statement"

    class catches_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "catches"
    # Java.g:721:1: catches : ( catchClause )+ -> ^( CATCH_CLAUSE_LIST ( catchClause )+ ) ;
    def catches(self, ):

        retval = self.catches_return()
        retval.start = self.input.LT(1)
        catches_StartIndex = self.input.index()
        root_0 = None

        catchClause338 = None


        stream_catchClause = RewriteRuleSubtreeStream(self._adaptor, "rule catchClause")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 76):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:722:5: ( ( catchClause )+ -> ^( CATCH_CLAUSE_LIST ( catchClause )+ ) )
                # Java.g:722:9: ( catchClause )+
                pass 
                # Java.g:722:9: ( catchClause )+
                cnt98 = 0
                while True: #loop98
                    alt98 = 2
                    LA98_0 = self.input.LA(1)

                    if (LA98_0 == CATCH) :
                        alt98 = 1


                    if alt98 == 1:
                        # Java.g:0:0: catchClause
                        pass 
                        self._state.following.append(self.FOLLOW_catchClause_in_catches9742)
                        catchClause338 = self.catchClause()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_catchClause.add(catchClause338.tree)


                    else:
                        if cnt98 >= 1:
                            break #loop98

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(98, self.input)
                        raise eee

                    cnt98 += 1



                # AST Rewrite
                # elements: catchClause
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 723:9: -> ^( CATCH_CLAUSE_LIST ( catchClause )+ )
                    # Java.g:723:13: ^( CATCH_CLAUSE_LIST ( catchClause )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CATCH_CLAUSE_LIST, "CATCH_CLAUSE_LIST"), root_1)

                    # Java.g:723:33: ( catchClause )+
                    if not (stream_catchClause.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_catchClause.hasNext():
                        self._adaptor.addChild(root_1, stream_catchClause.nextTree())


                    stream_catchClause.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 76, catches_StartIndex, success)

            pass

        return retval

    # $ANTLR end "catches"

    class catchClause_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "catchClause"
    # Java.g:726:1: catchClause : CATCH LPAREN formalParameterStandardDecl RPAREN block ;
    def catchClause(self, ):

        retval = self.catchClause_return()
        retval.start = self.input.LT(1)
        catchClause_StartIndex = self.input.index()
        root_0 = None

        CATCH339 = None
        LPAREN340 = None
        RPAREN342 = None
        formalParameterStandardDecl341 = None

        block343 = None


        CATCH339_tree = None
        LPAREN340_tree = None
        RPAREN342_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 77):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:727:5: ( CATCH LPAREN formalParameterStandardDecl RPAREN block )
                # Java.g:727:9: CATCH LPAREN formalParameterStandardDecl RPAREN block
                pass 
                root_0 = self._adaptor.nil()

                CATCH339=self.match(self.input, CATCH, self.FOLLOW_CATCH_in_catchClause9780)
                if self._state.backtracking == 0:

                    CATCH339_tree = self._adaptor.createWithPayload(CATCH339)
                    root_0 = self._adaptor.becomeRoot(CATCH339_tree, root_0)

                LPAREN340=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_catchClause9783)
                self._state.following.append(self.FOLLOW_formalParameterStandardDecl_in_catchClause9786)
                formalParameterStandardDecl341 = self.formalParameterStandardDecl()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, formalParameterStandardDecl341.tree)
                RPAREN342=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_catchClause9788)
                self._state.following.append(self.FOLLOW_block_in_catchClause9791)
                block343 = self.block()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, block343.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 77, catchClause_StartIndex, success)

            pass

        return retval

    # $ANTLR end "catchClause"

    class finallyClause_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "finallyClause"
    # Java.g:730:1: finallyClause : FINALLY block -> block ;
    def finallyClause(self, ):

        retval = self.finallyClause_return()
        retval.start = self.input.LT(1)
        finallyClause_StartIndex = self.input.index()
        root_0 = None

        FINALLY344 = None
        block345 = None


        FINALLY344_tree = None
        stream_FINALLY = RewriteRuleTokenStream(self._adaptor, "token FINALLY")
        stream_block = RewriteRuleSubtreeStream(self._adaptor, "rule block")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 78):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:731:5: ( FINALLY block -> block )
                # Java.g:731:9: FINALLY block
                pass 
                FINALLY344=self.match(self.input, FINALLY, self.FOLLOW_FINALLY_in_finallyClause9810) 
                if self._state.backtracking == 0:
                    stream_FINALLY.add(FINALLY344)
                self._state.following.append(self.FOLLOW_block_in_finallyClause9812)
                block345 = self.block()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_block.add(block345.tree)

                # AST Rewrite
                # elements: block
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 732:9: -> block
                    self._adaptor.addChild(root_0, stream_block.nextTree())



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 78, finallyClause_StartIndex, success)

            pass

        return retval

    # $ANTLR end "finallyClause"

    class switchBlockLabels_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "switchBlockLabels"
    # Java.g:735:1: switchBlockLabels : switchCaseLabels ( switchDefaultLabel )? -> ^( SWITCH_BLOCK_LABEL_LIST switchCaseLabels ( switchDefaultLabel )? ) ;
    def switchBlockLabels(self, ):

        retval = self.switchBlockLabels_return()
        retval.start = self.input.LT(1)
        switchBlockLabels_StartIndex = self.input.index()
        root_0 = None

        switchCaseLabels346 = None

        switchDefaultLabel347 = None


        stream_switchDefaultLabel = RewriteRuleSubtreeStream(self._adaptor, "rule switchDefaultLabel")
        stream_switchCaseLabels = RewriteRuleSubtreeStream(self._adaptor, "rule switchCaseLabels")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 79):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:739:5: ( switchCaseLabels ( switchDefaultLabel )? -> ^( SWITCH_BLOCK_LABEL_LIST switchCaseLabels ( switchDefaultLabel )? ) )
                # Java.g:739:9: switchCaseLabels ( switchDefaultLabel )?
                pass 
                self._state.following.append(self.FOLLOW_switchCaseLabels_in_switchBlockLabels9847)
                switchCaseLabels346 = self.switchCaseLabels()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_switchCaseLabels.add(switchCaseLabels346.tree)
                # Java.g:739:26: ( switchDefaultLabel )?
                alt99 = 2
                LA99_0 = self.input.LA(1)

                if (LA99_0 == DEFAULT) :
                    alt99 = 1
                if alt99 == 1:
                    # Java.g:0:0: switchDefaultLabel
                    pass 
                    self._state.following.append(self.FOLLOW_switchDefaultLabel_in_switchBlockLabels9849)
                    switchDefaultLabel347 = self.switchDefaultLabel()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_switchDefaultLabel.add(switchDefaultLabel347.tree)




                # AST Rewrite
                # elements: switchCaseLabels, switchDefaultLabel
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 740:9: -> ^( SWITCH_BLOCK_LABEL_LIST switchCaseLabels ( switchDefaultLabel )? )
                    # Java.g:740:13: ^( SWITCH_BLOCK_LABEL_LIST switchCaseLabels ( switchDefaultLabel )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(SWITCH_BLOCK_LABEL_LIST, "SWITCH_BLOCK_LABEL_LIST"), root_1)

                    self._adaptor.addChild(root_1, stream_switchCaseLabels.nextTree())
                    # Java.g:740:56: ( switchDefaultLabel )?
                    if stream_switchDefaultLabel.hasNext():
                        self._adaptor.addChild(root_1, stream_switchDefaultLabel.nextTree())


                    stream_switchDefaultLabel.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 79, switchBlockLabels_StartIndex, success)

            pass

        return retval

    # $ANTLR end "switchBlockLabels"

    class switchCaseLabels_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "switchCaseLabels"
    # Java.g:743:1: switchCaseLabels : ( switchCaseLabel )* ;
    def switchCaseLabels(self, ):

        retval = self.switchCaseLabels_return()
        retval.start = self.input.LT(1)
        switchCaseLabels_StartIndex = self.input.index()
        root_0 = None

        switchCaseLabel348 = None



        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 80):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:744:5: ( ( switchCaseLabel )* )
                # Java.g:744:9: ( switchCaseLabel )*
                pass 
                root_0 = self._adaptor.nil()

                # Java.g:744:9: ( switchCaseLabel )*
                while True: #loop100
                    alt100 = 2
                    LA100_0 = self.input.LA(1)

                    if (LA100_0 == CASE) :
                        alt100 = 1


                    if alt100 == 1:
                        # Java.g:0:0: switchCaseLabel
                        pass 
                        self._state.following.append(self.FOLLOW_switchCaseLabel_in_switchCaseLabels9890)
                        switchCaseLabel348 = self.switchCaseLabel()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, switchCaseLabel348.tree)


                    else:
                        break #loop100





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 80, switchCaseLabels_StartIndex, success)

            pass

        return retval

    # $ANTLR end "switchCaseLabels"

    class switchCaseLabel_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "switchCaseLabel"
    # Java.g:747:1: switchCaseLabel : CASE expression COLON ( blockStatement )* ;
    def switchCaseLabel(self, ):

        retval = self.switchCaseLabel_return()
        retval.start = self.input.LT(1)
        switchCaseLabel_StartIndex = self.input.index()
        root_0 = None

        CASE349 = None
        COLON351 = None
        expression350 = None

        blockStatement352 = None


        CASE349_tree = None
        COLON351_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 81):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:748:5: ( CASE expression COLON ( blockStatement )* )
                # Java.g:748:9: CASE expression COLON ( blockStatement )*
                pass 
                root_0 = self._adaptor.nil()

                CASE349=self.match(self.input, CASE, self.FOLLOW_CASE_in_switchCaseLabel9910)
                if self._state.backtracking == 0:

                    CASE349_tree = self._adaptor.createWithPayload(CASE349)
                    root_0 = self._adaptor.becomeRoot(CASE349_tree, root_0)

                self._state.following.append(self.FOLLOW_expression_in_switchCaseLabel9913)
                expression350 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression350.tree)
                COLON351=self.match(self.input, COLON, self.FOLLOW_COLON_in_switchCaseLabel9915)
                # Java.g:748:33: ( blockStatement )*
                while True: #loop101
                    alt101 = 2
                    LA101_0 = self.input.LA(1)

                    if (LA101_0 == AT or LA101_0 == DEC or LA101_0 == INC or LA101_0 == LCURLY or LA101_0 == LESS_THAN or LA101_0 == LOGICAL_NOT or (LPAREN <= LA101_0 <= MINUS) or LA101_0 == NOT or LA101_0 == PLUS or LA101_0 == SEMI or (ABSTRACT <= LA101_0 <= BYTE) or (CHAR <= LA101_0 <= CONTINUE) or (DO <= LA101_0 <= DOUBLE) or LA101_0 == ENUM or (FALSE <= LA101_0 <= FINAL) or (FLOAT <= LA101_0 <= IF) or LA101_0 == INTERFACE or (INT <= LA101_0 <= NULL) or (PRIVATE <= LA101_0 <= THROW) or (TRANSIENT <= LA101_0 <= WHILE) or (IDENT <= LA101_0 <= STRING_LITERAL)) :
                        alt101 = 1


                    if alt101 == 1:
                        # Java.g:0:0: blockStatement
                        pass 
                        self._state.following.append(self.FOLLOW_blockStatement_in_switchCaseLabel9918)
                        blockStatement352 = self.blockStatement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, blockStatement352.tree)


                    else:
                        break #loop101





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 81, switchCaseLabel_StartIndex, success)

            pass

        return retval

    # $ANTLR end "switchCaseLabel"

    class switchDefaultLabel_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "switchDefaultLabel"
    # Java.g:751:1: switchDefaultLabel : DEFAULT COLON ( blockStatement )* ;
    def switchDefaultLabel(self, ):

        retval = self.switchDefaultLabel_return()
        retval.start = self.input.LT(1)
        switchDefaultLabel_StartIndex = self.input.index()
        root_0 = None

        DEFAULT353 = None
        COLON354 = None
        blockStatement355 = None


        DEFAULT353_tree = None
        COLON354_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 82):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:752:5: ( DEFAULT COLON ( blockStatement )* )
                # Java.g:752:9: DEFAULT COLON ( blockStatement )*
                pass 
                root_0 = self._adaptor.nil()

                DEFAULT353=self.match(self.input, DEFAULT, self.FOLLOW_DEFAULT_in_switchDefaultLabel9938)
                if self._state.backtracking == 0:

                    DEFAULT353_tree = self._adaptor.createWithPayload(DEFAULT353)
                    root_0 = self._adaptor.becomeRoot(DEFAULT353_tree, root_0)

                COLON354=self.match(self.input, COLON, self.FOLLOW_COLON_in_switchDefaultLabel9941)
                # Java.g:752:25: ( blockStatement )*
                while True: #loop102
                    alt102 = 2
                    LA102_0 = self.input.LA(1)

                    if (LA102_0 == AT or LA102_0 == DEC or LA102_0 == INC or LA102_0 == LCURLY or LA102_0 == LESS_THAN or LA102_0 == LOGICAL_NOT or (LPAREN <= LA102_0 <= MINUS) or LA102_0 == NOT or LA102_0 == PLUS or LA102_0 == SEMI or (ABSTRACT <= LA102_0 <= BYTE) or (CHAR <= LA102_0 <= CONTINUE) or (DO <= LA102_0 <= DOUBLE) or LA102_0 == ENUM or (FALSE <= LA102_0 <= FINAL) or (FLOAT <= LA102_0 <= IF) or LA102_0 == INTERFACE or (INT <= LA102_0 <= NULL) or (PRIVATE <= LA102_0 <= THROW) or (TRANSIENT <= LA102_0 <= WHILE) or (IDENT <= LA102_0 <= STRING_LITERAL)) :
                        alt102 = 1


                    if alt102 == 1:
                        # Java.g:0:0: blockStatement
                        pass 
                        self._state.following.append(self.FOLLOW_blockStatement_in_switchDefaultLabel9944)
                        blockStatement355 = self.blockStatement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, blockStatement355.tree)


                    else:
                        break #loop102





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 82, switchDefaultLabel_StartIndex, success)

            pass

        return retval

    # $ANTLR end "switchDefaultLabel"

    class forInit_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "forInit"
    # Java.g:755:1: forInit : ( localVariableDeclaration -> ^( FOR_INIT localVariableDeclaration ) | expressionList -> ^( FOR_INIT expressionList ) | -> ^( FOR_INIT ) );
    def forInit(self, ):

        retval = self.forInit_return()
        retval.start = self.input.LT(1)
        forInit_StartIndex = self.input.index()
        root_0 = None

        localVariableDeclaration356 = None

        expressionList357 = None


        stream_expressionList = RewriteRuleSubtreeStream(self._adaptor, "rule expressionList")
        stream_localVariableDeclaration = RewriteRuleSubtreeStream(self._adaptor, "rule localVariableDeclaration")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 83):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:756:5: ( localVariableDeclaration -> ^( FOR_INIT localVariableDeclaration ) | expressionList -> ^( FOR_INIT expressionList ) | -> ^( FOR_INIT ) )
                alt103 = 3
                alt103 = self.dfa103.predict(self.input)
                if alt103 == 1:
                    # Java.g:756:9: localVariableDeclaration
                    pass 
                    self._state.following.append(self.FOLLOW_localVariableDeclaration_in_forInit9964)
                    localVariableDeclaration356 = self.localVariableDeclaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_localVariableDeclaration.add(localVariableDeclaration356.tree)

                    # AST Rewrite
                    # elements: localVariableDeclaration
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 756:37: -> ^( FOR_INIT localVariableDeclaration )
                        # Java.g:756:41: ^( FOR_INIT localVariableDeclaration )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FOR_INIT, "FOR_INIT"), root_1)

                        self._adaptor.addChild(root_1, stream_localVariableDeclaration.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt103 == 2:
                    # Java.g:757:9: expressionList
                    pass 
                    self._state.following.append(self.FOLLOW_expressionList_in_forInit9986)
                    expressionList357 = self.expressionList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expressionList.add(expressionList357.tree)

                    # AST Rewrite
                    # elements: expressionList
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 757:37: -> ^( FOR_INIT expressionList )
                        # Java.g:757:41: ^( FOR_INIT expressionList )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FOR_INIT, "FOR_INIT"), root_1)

                        self._adaptor.addChild(root_1, stream_expressionList.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt103 == 3:
                    # Java.g:758:37: 
                    pass 
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 758:37: -> ^( FOR_INIT )
                        # Java.g:758:41: ^( FOR_INIT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FOR_INIT, "FOR_INIT"), root_1)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 83, forInit_StartIndex, success)

            pass

        return retval

    # $ANTLR end "forInit"

    class forCondition_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "forCondition"
    # Java.g:761:1: forCondition : ( expression )? -> ^( FOR_CONDITION ( expression )? ) ;
    def forCondition(self, ):

        retval = self.forCondition_return()
        retval.start = self.input.LT(1)
        forCondition_StartIndex = self.input.index()
        root_0 = None

        expression358 = None


        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 84):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:762:5: ( ( expression )? -> ^( FOR_CONDITION ( expression )? ) )
                # Java.g:762:9: ( expression )?
                pass 
                # Java.g:762:9: ( expression )?
                alt104 = 2
                LA104_0 = self.input.LA(1)

                if (LA104_0 == DEC or LA104_0 == INC or LA104_0 == LESS_THAN or LA104_0 == LOGICAL_NOT or (LPAREN <= LA104_0 <= MINUS) or LA104_0 == NOT or LA104_0 == PLUS or LA104_0 == BOOLEAN or LA104_0 == BYTE or LA104_0 == CHAR or LA104_0 == DOUBLE or LA104_0 == FALSE or LA104_0 == FLOAT or (INT <= LA104_0 <= LONG) or (NEW <= LA104_0 <= NULL) or LA104_0 == SHORT or LA104_0 == SUPER or LA104_0 == THIS or LA104_0 == TRUE or LA104_0 == VOID or (IDENT <= LA104_0 <= STRING_LITERAL)) :
                    alt104 = 1
                if alt104 == 1:
                    # Java.g:0:0: expression
                    pass 
                    self._state.following.append(self.FOLLOW_expression_in_forCondition10070)
                    expression358 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression358.tree)




                # AST Rewrite
                # elements: expression
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 763:9: -> ^( FOR_CONDITION ( expression )? )
                    # Java.g:763:13: ^( FOR_CONDITION ( expression )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FOR_CONDITION, "FOR_CONDITION"), root_1)

                    # Java.g:763:29: ( expression )?
                    if stream_expression.hasNext():
                        self._adaptor.addChild(root_1, stream_expression.nextTree())


                    stream_expression.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 84, forCondition_StartIndex, success)

            pass

        return retval

    # $ANTLR end "forCondition"

    class forUpdater_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "forUpdater"
    # Java.g:766:1: forUpdater : ( expressionList )? -> ^( FOR_UPDATE ( expressionList )? ) ;
    def forUpdater(self, ):

        retval = self.forUpdater_return()
        retval.start = self.input.LT(1)
        forUpdater_StartIndex = self.input.index()
        root_0 = None

        expressionList359 = None


        stream_expressionList = RewriteRuleSubtreeStream(self._adaptor, "rule expressionList")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 85):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:767:5: ( ( expressionList )? -> ^( FOR_UPDATE ( expressionList )? ) )
                # Java.g:767:9: ( expressionList )?
                pass 
                # Java.g:767:9: ( expressionList )?
                alt105 = 2
                LA105_0 = self.input.LA(1)

                if (LA105_0 == DEC or LA105_0 == INC or LA105_0 == LESS_THAN or LA105_0 == LOGICAL_NOT or (LPAREN <= LA105_0 <= MINUS) or LA105_0 == NOT or LA105_0 == PLUS or LA105_0 == BOOLEAN or LA105_0 == BYTE or LA105_0 == CHAR or LA105_0 == DOUBLE or LA105_0 == FALSE or LA105_0 == FLOAT or (INT <= LA105_0 <= LONG) or (NEW <= LA105_0 <= NULL) or LA105_0 == SHORT or LA105_0 == SUPER or LA105_0 == THIS or LA105_0 == TRUE or LA105_0 == VOID or (IDENT <= LA105_0 <= STRING_LITERAL)) :
                    alt105 = 1
                if alt105 == 1:
                    # Java.g:0:0: expressionList
                    pass 
                    self._state.following.append(self.FOLLOW_expressionList_in_forUpdater10108)
                    expressionList359 = self.expressionList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expressionList.add(expressionList359.tree)




                # AST Rewrite
                # elements: expressionList
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 768:9: -> ^( FOR_UPDATE ( expressionList )? )
                    # Java.g:768:13: ^( FOR_UPDATE ( expressionList )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FOR_UPDATE, "FOR_UPDATE"), root_1)

                    # Java.g:768:26: ( expressionList )?
                    if stream_expressionList.hasNext():
                        self._adaptor.addChild(root_1, stream_expressionList.nextTree())


                    stream_expressionList.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 85, forUpdater_StartIndex, success)

            pass

        return retval

    # $ANTLR end "forUpdater"

    class parenthesizedExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "parenthesizedExpression"
    # Java.g:773:1: parenthesizedExpression : LPAREN expression RPAREN -> ^( PARENTESIZED_EXPR[$LPAREN, \"PARENTESIZED_EXPR\"] expression ) ;
    def parenthesizedExpression(self, ):

        retval = self.parenthesizedExpression_return()
        retval.start = self.input.LT(1)
        parenthesizedExpression_StartIndex = self.input.index()
        root_0 = None

        LPAREN360 = None
        RPAREN362 = None
        expression361 = None


        LPAREN360_tree = None
        RPAREN362_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 86):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:774:5: ( LPAREN expression RPAREN -> ^( PARENTESIZED_EXPR[$LPAREN, \"PARENTESIZED_EXPR\"] expression ) )
                # Java.g:774:9: LPAREN expression RPAREN
                pass 
                LPAREN360=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_parenthesizedExpression10148) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(LPAREN360)
                self._state.following.append(self.FOLLOW_expression_in_parenthesizedExpression10150)
                expression361 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(expression361.tree)
                RPAREN362=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_parenthesizedExpression10152) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(RPAREN362)

                # AST Rewrite
                # elements: expression
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 775:9: -> ^( PARENTESIZED_EXPR[$LPAREN, \"PARENTESIZED_EXPR\"] expression )
                    # Java.g:775:13: ^( PARENTESIZED_EXPR[$LPAREN, \"PARENTESIZED_EXPR\"] expression )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.create(PARENTESIZED_EXPR, LPAREN360, "PARENTESIZED_EXPR"), root_1)

                    self._adaptor.addChild(root_1, stream_expression.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 86, parenthesizedExpression_StartIndex, success)

            pass

        return retval

    # $ANTLR end "parenthesizedExpression"

    class expressionList_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "expressionList"
    # Java.g:778:1: expressionList : expression ( COMMA expression )* ;
    def expressionList(self, ):

        retval = self.expressionList_return()
        retval.start = self.input.LT(1)
        expressionList_StartIndex = self.input.index()
        root_0 = None

        COMMA364 = None
        expression363 = None

        expression365 = None


        COMMA364_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 87):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:779:5: ( expression ( COMMA expression )* )
                # Java.g:779:9: expression ( COMMA expression )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_expression_in_expressionList10189)
                expression363 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression363.tree)
                # Java.g:779:20: ( COMMA expression )*
                while True: #loop106
                    alt106 = 2
                    LA106_0 = self.input.LA(1)

                    if (LA106_0 == COMMA) :
                        alt106 = 1


                    if alt106 == 1:
                        # Java.g:779:21: COMMA expression
                        pass 
                        COMMA364=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_expressionList10192)
                        self._state.following.append(self.FOLLOW_expression_in_expressionList10195)
                        expression365 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression365.tree)


                    else:
                        break #loop106





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 87, expressionList_StartIndex, success)

            pass

        return retval

    # $ANTLR end "expressionList"

    class expression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "expression"
    # Java.g:782:1: expression : assignmentExpression -> ^( EXPR assignmentExpression ) ;
    def expression(self, ):

        retval = self.expression_return()
        retval.start = self.input.LT(1)
        expression_StartIndex = self.input.index()
        root_0 = None

        assignmentExpression366 = None


        stream_assignmentExpression = RewriteRuleSubtreeStream(self._adaptor, "rule assignmentExpression")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 88):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:783:5: ( assignmentExpression -> ^( EXPR assignmentExpression ) )
                # Java.g:783:9: assignmentExpression
                pass 
                self._state.following.append(self.FOLLOW_assignmentExpression_in_expression10216)
                assignmentExpression366 = self.assignmentExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_assignmentExpression.add(assignmentExpression366.tree)

                # AST Rewrite
                # elements: assignmentExpression
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 784:9: -> ^( EXPR assignmentExpression )
                    # Java.g:784:13: ^( EXPR assignmentExpression )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EXPR, "EXPR"), root_1)

                    self._adaptor.addChild(root_1, stream_assignmentExpression.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 88, expression_StartIndex, success)

            pass

        return retval

    # $ANTLR end "expression"

    class assignmentExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "assignmentExpression"
    # Java.g:787:1: assignmentExpression : conditionalExpression ( ( ASSIGN | PLUS_ASSIGN | MINUS_ASSIGN | STAR_ASSIGN | DIV_ASSIGN | AND_ASSIGN | OR_ASSIGN | XOR_ASSIGN | MOD_ASSIGN | SHIFT_LEFT_ASSIGN | SHIFT_RIGHT_ASSIGN | BIT_SHIFT_RIGHT_ASSIGN ) assignmentExpression )? ;
    def assignmentExpression(self, ):

        retval = self.assignmentExpression_return()
        retval.start = self.input.LT(1)
        assignmentExpression_StartIndex = self.input.index()
        root_0 = None

        ASSIGN368 = None
        PLUS_ASSIGN369 = None
        MINUS_ASSIGN370 = None
        STAR_ASSIGN371 = None
        DIV_ASSIGN372 = None
        AND_ASSIGN373 = None
        OR_ASSIGN374 = None
        XOR_ASSIGN375 = None
        MOD_ASSIGN376 = None
        SHIFT_LEFT_ASSIGN377 = None
        SHIFT_RIGHT_ASSIGN378 = None
        BIT_SHIFT_RIGHT_ASSIGN379 = None
        conditionalExpression367 = None

        assignmentExpression380 = None


        ASSIGN368_tree = None
        PLUS_ASSIGN369_tree = None
        MINUS_ASSIGN370_tree = None
        STAR_ASSIGN371_tree = None
        DIV_ASSIGN372_tree = None
        AND_ASSIGN373_tree = None
        OR_ASSIGN374_tree = None
        XOR_ASSIGN375_tree = None
        MOD_ASSIGN376_tree = None
        SHIFT_LEFT_ASSIGN377_tree = None
        SHIFT_RIGHT_ASSIGN378_tree = None
        BIT_SHIFT_RIGHT_ASSIGN379_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 89):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:788:5: ( conditionalExpression ( ( ASSIGN | PLUS_ASSIGN | MINUS_ASSIGN | STAR_ASSIGN | DIV_ASSIGN | AND_ASSIGN | OR_ASSIGN | XOR_ASSIGN | MOD_ASSIGN | SHIFT_LEFT_ASSIGN | SHIFT_RIGHT_ASSIGN | BIT_SHIFT_RIGHT_ASSIGN ) assignmentExpression )? )
                # Java.g:788:9: conditionalExpression ( ( ASSIGN | PLUS_ASSIGN | MINUS_ASSIGN | STAR_ASSIGN | DIV_ASSIGN | AND_ASSIGN | OR_ASSIGN | XOR_ASSIGN | MOD_ASSIGN | SHIFT_LEFT_ASSIGN | SHIFT_RIGHT_ASSIGN | BIT_SHIFT_RIGHT_ASSIGN ) assignmentExpression )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_conditionalExpression_in_assignmentExpression10252)
                conditionalExpression367 = self.conditionalExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, conditionalExpression367.tree)
                # Java.g:789:9: ( ( ASSIGN | PLUS_ASSIGN | MINUS_ASSIGN | STAR_ASSIGN | DIV_ASSIGN | AND_ASSIGN | OR_ASSIGN | XOR_ASSIGN | MOD_ASSIGN | SHIFT_LEFT_ASSIGN | SHIFT_RIGHT_ASSIGN | BIT_SHIFT_RIGHT_ASSIGN ) assignmentExpression )?
                alt108 = 2
                LA108_0 = self.input.LA(1)

                if ((AND_ASSIGN <= LA108_0 <= ASSIGN) or LA108_0 == BIT_SHIFT_RIGHT_ASSIGN or LA108_0 == DIV_ASSIGN or LA108_0 == MINUS_ASSIGN or LA108_0 == MOD_ASSIGN or LA108_0 == OR_ASSIGN or LA108_0 == PLUS_ASSIGN or LA108_0 == SHIFT_LEFT_ASSIGN or LA108_0 == SHIFT_RIGHT_ASSIGN or LA108_0 == STAR_ASSIGN or LA108_0 == XOR_ASSIGN) :
                    alt108 = 1
                if alt108 == 1:
                    # Java.g:789:13: ( ASSIGN | PLUS_ASSIGN | MINUS_ASSIGN | STAR_ASSIGN | DIV_ASSIGN | AND_ASSIGN | OR_ASSIGN | XOR_ASSIGN | MOD_ASSIGN | SHIFT_LEFT_ASSIGN | SHIFT_RIGHT_ASSIGN | BIT_SHIFT_RIGHT_ASSIGN ) assignmentExpression
                    pass 
                    # Java.g:789:13: ( ASSIGN | PLUS_ASSIGN | MINUS_ASSIGN | STAR_ASSIGN | DIV_ASSIGN | AND_ASSIGN | OR_ASSIGN | XOR_ASSIGN | MOD_ASSIGN | SHIFT_LEFT_ASSIGN | SHIFT_RIGHT_ASSIGN | BIT_SHIFT_RIGHT_ASSIGN )
                    alt107 = 12
                    LA107 = self.input.LA(1)
                    if LA107 == ASSIGN:
                        alt107 = 1
                    elif LA107 == PLUS_ASSIGN:
                        alt107 = 2
                    elif LA107 == MINUS_ASSIGN:
                        alt107 = 3
                    elif LA107 == STAR_ASSIGN:
                        alt107 = 4
                    elif LA107 == DIV_ASSIGN:
                        alt107 = 5
                    elif LA107 == AND_ASSIGN:
                        alt107 = 6
                    elif LA107 == OR_ASSIGN:
                        alt107 = 7
                    elif LA107 == XOR_ASSIGN:
                        alt107 = 8
                    elif LA107 == MOD_ASSIGN:
                        alt107 = 9
                    elif LA107 == SHIFT_LEFT_ASSIGN:
                        alt107 = 10
                    elif LA107 == SHIFT_RIGHT_ASSIGN:
                        alt107 = 11
                    elif LA107 == BIT_SHIFT_RIGHT_ASSIGN:
                        alt107 = 12
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 107, 0, self.input)

                        raise nvae

                    if alt107 == 1:
                        # Java.g:789:17: ASSIGN
                        pass 
                        ASSIGN368=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_assignmentExpression10270)
                        if self._state.backtracking == 0:

                            ASSIGN368_tree = self._adaptor.createWithPayload(ASSIGN368)
                            root_0 = self._adaptor.becomeRoot(ASSIGN368_tree, root_0)



                    elif alt107 == 2:
                        # Java.g:790:17: PLUS_ASSIGN
                        pass 
                        PLUS_ASSIGN369=self.match(self.input, PLUS_ASSIGN, self.FOLLOW_PLUS_ASSIGN_in_assignmentExpression10289)
                        if self._state.backtracking == 0:

                            PLUS_ASSIGN369_tree = self._adaptor.createWithPayload(PLUS_ASSIGN369)
                            root_0 = self._adaptor.becomeRoot(PLUS_ASSIGN369_tree, root_0)



                    elif alt107 == 3:
                        # Java.g:791:17: MINUS_ASSIGN
                        pass 
                        MINUS_ASSIGN370=self.match(self.input, MINUS_ASSIGN, self.FOLLOW_MINUS_ASSIGN_in_assignmentExpression10308)
                        if self._state.backtracking == 0:

                            MINUS_ASSIGN370_tree = self._adaptor.createWithPayload(MINUS_ASSIGN370)
                            root_0 = self._adaptor.becomeRoot(MINUS_ASSIGN370_tree, root_0)



                    elif alt107 == 4:
                        # Java.g:792:17: STAR_ASSIGN
                        pass 
                        STAR_ASSIGN371=self.match(self.input, STAR_ASSIGN, self.FOLLOW_STAR_ASSIGN_in_assignmentExpression10327)
                        if self._state.backtracking == 0:

                            STAR_ASSIGN371_tree = self._adaptor.createWithPayload(STAR_ASSIGN371)
                            root_0 = self._adaptor.becomeRoot(STAR_ASSIGN371_tree, root_0)



                    elif alt107 == 5:
                        # Java.g:793:17: DIV_ASSIGN
                        pass 
                        DIV_ASSIGN372=self.match(self.input, DIV_ASSIGN, self.FOLLOW_DIV_ASSIGN_in_assignmentExpression10346)
                        if self._state.backtracking == 0:

                            DIV_ASSIGN372_tree = self._adaptor.createWithPayload(DIV_ASSIGN372)
                            root_0 = self._adaptor.becomeRoot(DIV_ASSIGN372_tree, root_0)



                    elif alt107 == 6:
                        # Java.g:794:17: AND_ASSIGN
                        pass 
                        AND_ASSIGN373=self.match(self.input, AND_ASSIGN, self.FOLLOW_AND_ASSIGN_in_assignmentExpression10365)
                        if self._state.backtracking == 0:

                            AND_ASSIGN373_tree = self._adaptor.createWithPayload(AND_ASSIGN373)
                            root_0 = self._adaptor.becomeRoot(AND_ASSIGN373_tree, root_0)



                    elif alt107 == 7:
                        # Java.g:795:17: OR_ASSIGN
                        pass 
                        OR_ASSIGN374=self.match(self.input, OR_ASSIGN, self.FOLLOW_OR_ASSIGN_in_assignmentExpression10384)
                        if self._state.backtracking == 0:

                            OR_ASSIGN374_tree = self._adaptor.createWithPayload(OR_ASSIGN374)
                            root_0 = self._adaptor.becomeRoot(OR_ASSIGN374_tree, root_0)



                    elif alt107 == 8:
                        # Java.g:796:17: XOR_ASSIGN
                        pass 
                        XOR_ASSIGN375=self.match(self.input, XOR_ASSIGN, self.FOLLOW_XOR_ASSIGN_in_assignmentExpression10403)
                        if self._state.backtracking == 0:

                            XOR_ASSIGN375_tree = self._adaptor.createWithPayload(XOR_ASSIGN375)
                            root_0 = self._adaptor.becomeRoot(XOR_ASSIGN375_tree, root_0)



                    elif alt107 == 9:
                        # Java.g:797:17: MOD_ASSIGN
                        pass 
                        MOD_ASSIGN376=self.match(self.input, MOD_ASSIGN, self.FOLLOW_MOD_ASSIGN_in_assignmentExpression10422)
                        if self._state.backtracking == 0:

                            MOD_ASSIGN376_tree = self._adaptor.createWithPayload(MOD_ASSIGN376)
                            root_0 = self._adaptor.becomeRoot(MOD_ASSIGN376_tree, root_0)



                    elif alt107 == 10:
                        # Java.g:798:17: SHIFT_LEFT_ASSIGN
                        pass 
                        SHIFT_LEFT_ASSIGN377=self.match(self.input, SHIFT_LEFT_ASSIGN, self.FOLLOW_SHIFT_LEFT_ASSIGN_in_assignmentExpression10441)
                        if self._state.backtracking == 0:

                            SHIFT_LEFT_ASSIGN377_tree = self._adaptor.createWithPayload(SHIFT_LEFT_ASSIGN377)
                            root_0 = self._adaptor.becomeRoot(SHIFT_LEFT_ASSIGN377_tree, root_0)



                    elif alt107 == 11:
                        # Java.g:799:17: SHIFT_RIGHT_ASSIGN
                        pass 
                        SHIFT_RIGHT_ASSIGN378=self.match(self.input, SHIFT_RIGHT_ASSIGN, self.FOLLOW_SHIFT_RIGHT_ASSIGN_in_assignmentExpression10460)
                        if self._state.backtracking == 0:

                            SHIFT_RIGHT_ASSIGN378_tree = self._adaptor.createWithPayload(SHIFT_RIGHT_ASSIGN378)
                            root_0 = self._adaptor.becomeRoot(SHIFT_RIGHT_ASSIGN378_tree, root_0)



                    elif alt107 == 12:
                        # Java.g:800:17: BIT_SHIFT_RIGHT_ASSIGN
                        pass 
                        BIT_SHIFT_RIGHT_ASSIGN379=self.match(self.input, BIT_SHIFT_RIGHT_ASSIGN, self.FOLLOW_BIT_SHIFT_RIGHT_ASSIGN_in_assignmentExpression10479)
                        if self._state.backtracking == 0:

                            BIT_SHIFT_RIGHT_ASSIGN379_tree = self._adaptor.createWithPayload(BIT_SHIFT_RIGHT_ASSIGN379)
                            root_0 = self._adaptor.becomeRoot(BIT_SHIFT_RIGHT_ASSIGN379_tree, root_0)




                    self._state.following.append(self.FOLLOW_assignmentExpression_in_assignmentExpression10500)
                    assignmentExpression380 = self.assignmentExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assignmentExpression380.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 89, assignmentExpression_StartIndex, success)

            pass

        return retval

    # $ANTLR end "assignmentExpression"

    class conditionalExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "conditionalExpression"
    # Java.g:805:1: conditionalExpression : logicalOrExpression ( QUESTION assignmentExpression COLON conditionalExpression )? ;
    def conditionalExpression(self, ):

        retval = self.conditionalExpression_return()
        retval.start = self.input.LT(1)
        conditionalExpression_StartIndex = self.input.index()
        root_0 = None

        QUESTION382 = None
        COLON384 = None
        logicalOrExpression381 = None

        assignmentExpression383 = None

        conditionalExpression385 = None


        QUESTION382_tree = None
        COLON384_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 90):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:806:5: ( logicalOrExpression ( QUESTION assignmentExpression COLON conditionalExpression )? )
                # Java.g:806:9: logicalOrExpression ( QUESTION assignmentExpression COLON conditionalExpression )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_logicalOrExpression_in_conditionalExpression10521)
                logicalOrExpression381 = self.logicalOrExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, logicalOrExpression381.tree)
                # Java.g:806:29: ( QUESTION assignmentExpression COLON conditionalExpression )?
                alt109 = 2
                LA109_0 = self.input.LA(1)

                if (LA109_0 == QUESTION) :
                    alt109 = 1
                if alt109 == 1:
                    # Java.g:806:30: QUESTION assignmentExpression COLON conditionalExpression
                    pass 
                    QUESTION382=self.match(self.input, QUESTION, self.FOLLOW_QUESTION_in_conditionalExpression10524)
                    if self._state.backtracking == 0:

                        QUESTION382_tree = self._adaptor.createWithPayload(QUESTION382)
                        root_0 = self._adaptor.becomeRoot(QUESTION382_tree, root_0)

                    self._state.following.append(self.FOLLOW_assignmentExpression_in_conditionalExpression10527)
                    assignmentExpression383 = self.assignmentExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assignmentExpression383.tree)
                    COLON384=self.match(self.input, COLON, self.FOLLOW_COLON_in_conditionalExpression10529)
                    self._state.following.append(self.FOLLOW_conditionalExpression_in_conditionalExpression10532)
                    conditionalExpression385 = self.conditionalExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, conditionalExpression385.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 90, conditionalExpression_StartIndex, success)

            pass

        return retval

    # $ANTLR end "conditionalExpression"

    class logicalOrExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "logicalOrExpression"
    # Java.g:809:1: logicalOrExpression : logicalAndExpression ( LOGICAL_OR logicalAndExpression )* ;
    def logicalOrExpression(self, ):

        retval = self.logicalOrExpression_return()
        retval.start = self.input.LT(1)
        logicalOrExpression_StartIndex = self.input.index()
        root_0 = None

        LOGICAL_OR387 = None
        logicalAndExpression386 = None

        logicalAndExpression388 = None


        LOGICAL_OR387_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 91):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:810:5: ( logicalAndExpression ( LOGICAL_OR logicalAndExpression )* )
                # Java.g:810:9: logicalAndExpression ( LOGICAL_OR logicalAndExpression )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_logicalAndExpression_in_logicalOrExpression10553)
                logicalAndExpression386 = self.logicalAndExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, logicalAndExpression386.tree)
                # Java.g:810:30: ( LOGICAL_OR logicalAndExpression )*
                while True: #loop110
                    alt110 = 2
                    LA110_0 = self.input.LA(1)

                    if (LA110_0 == LOGICAL_OR) :
                        alt110 = 1


                    if alt110 == 1:
                        # Java.g:810:31: LOGICAL_OR logicalAndExpression
                        pass 
                        LOGICAL_OR387=self.match(self.input, LOGICAL_OR, self.FOLLOW_LOGICAL_OR_in_logicalOrExpression10556)
                        if self._state.backtracking == 0:

                            LOGICAL_OR387_tree = self._adaptor.createWithPayload(LOGICAL_OR387)
                            root_0 = self._adaptor.becomeRoot(LOGICAL_OR387_tree, root_0)

                        self._state.following.append(self.FOLLOW_logicalAndExpression_in_logicalOrExpression10559)
                        logicalAndExpression388 = self.logicalAndExpression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, logicalAndExpression388.tree)


                    else:
                        break #loop110





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 91, logicalOrExpression_StartIndex, success)

            pass

        return retval

    # $ANTLR end "logicalOrExpression"

    class logicalAndExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "logicalAndExpression"
    # Java.g:813:1: logicalAndExpression : inclusiveOrExpression ( LOGICAL_AND inclusiveOrExpression )* ;
    def logicalAndExpression(self, ):

        retval = self.logicalAndExpression_return()
        retval.start = self.input.LT(1)
        logicalAndExpression_StartIndex = self.input.index()
        root_0 = None

        LOGICAL_AND390 = None
        inclusiveOrExpression389 = None

        inclusiveOrExpression391 = None


        LOGICAL_AND390_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 92):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:814:5: ( inclusiveOrExpression ( LOGICAL_AND inclusiveOrExpression )* )
                # Java.g:814:9: inclusiveOrExpression ( LOGICAL_AND inclusiveOrExpression )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_inclusiveOrExpression_in_logicalAndExpression10580)
                inclusiveOrExpression389 = self.inclusiveOrExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, inclusiveOrExpression389.tree)
                # Java.g:814:31: ( LOGICAL_AND inclusiveOrExpression )*
                while True: #loop111
                    alt111 = 2
                    LA111_0 = self.input.LA(1)

                    if (LA111_0 == LOGICAL_AND) :
                        alt111 = 1


                    if alt111 == 1:
                        # Java.g:814:32: LOGICAL_AND inclusiveOrExpression
                        pass 
                        LOGICAL_AND390=self.match(self.input, LOGICAL_AND, self.FOLLOW_LOGICAL_AND_in_logicalAndExpression10583)
                        if self._state.backtracking == 0:

                            LOGICAL_AND390_tree = self._adaptor.createWithPayload(LOGICAL_AND390)
                            root_0 = self._adaptor.becomeRoot(LOGICAL_AND390_tree, root_0)

                        self._state.following.append(self.FOLLOW_inclusiveOrExpression_in_logicalAndExpression10586)
                        inclusiveOrExpression391 = self.inclusiveOrExpression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, inclusiveOrExpression391.tree)


                    else:
                        break #loop111





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 92, logicalAndExpression_StartIndex, success)

            pass

        return retval

    # $ANTLR end "logicalAndExpression"

    class inclusiveOrExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "inclusiveOrExpression"
    # Java.g:817:1: inclusiveOrExpression : exclusiveOrExpression ( OR exclusiveOrExpression )* ;
    def inclusiveOrExpression(self, ):

        retval = self.inclusiveOrExpression_return()
        retval.start = self.input.LT(1)
        inclusiveOrExpression_StartIndex = self.input.index()
        root_0 = None

        OR393 = None
        exclusiveOrExpression392 = None

        exclusiveOrExpression394 = None


        OR393_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 93):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:818:5: ( exclusiveOrExpression ( OR exclusiveOrExpression )* )
                # Java.g:818:9: exclusiveOrExpression ( OR exclusiveOrExpression )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_exclusiveOrExpression_in_inclusiveOrExpression10607)
                exclusiveOrExpression392 = self.exclusiveOrExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, exclusiveOrExpression392.tree)
                # Java.g:818:31: ( OR exclusiveOrExpression )*
                while True: #loop112
                    alt112 = 2
                    LA112_0 = self.input.LA(1)

                    if (LA112_0 == OR) :
                        alt112 = 1


                    if alt112 == 1:
                        # Java.g:818:32: OR exclusiveOrExpression
                        pass 
                        OR393=self.match(self.input, OR, self.FOLLOW_OR_in_inclusiveOrExpression10610)
                        if self._state.backtracking == 0:

                            OR393_tree = self._adaptor.createWithPayload(OR393)
                            root_0 = self._adaptor.becomeRoot(OR393_tree, root_0)

                        self._state.following.append(self.FOLLOW_exclusiveOrExpression_in_inclusiveOrExpression10613)
                        exclusiveOrExpression394 = self.exclusiveOrExpression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, exclusiveOrExpression394.tree)


                    else:
                        break #loop112





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 93, inclusiveOrExpression_StartIndex, success)

            pass

        return retval

    # $ANTLR end "inclusiveOrExpression"

    class exclusiveOrExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "exclusiveOrExpression"
    # Java.g:821:1: exclusiveOrExpression : andExpression ( XOR andExpression )* ;
    def exclusiveOrExpression(self, ):

        retval = self.exclusiveOrExpression_return()
        retval.start = self.input.LT(1)
        exclusiveOrExpression_StartIndex = self.input.index()
        root_0 = None

        XOR396 = None
        andExpression395 = None

        andExpression397 = None


        XOR396_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 94):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:822:5: ( andExpression ( XOR andExpression )* )
                # Java.g:822:9: andExpression ( XOR andExpression )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_andExpression_in_exclusiveOrExpression10634)
                andExpression395 = self.andExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, andExpression395.tree)
                # Java.g:822:23: ( XOR andExpression )*
                while True: #loop113
                    alt113 = 2
                    LA113_0 = self.input.LA(1)

                    if (LA113_0 == XOR) :
                        alt113 = 1


                    if alt113 == 1:
                        # Java.g:822:24: XOR andExpression
                        pass 
                        XOR396=self.match(self.input, XOR, self.FOLLOW_XOR_in_exclusiveOrExpression10637)
                        if self._state.backtracking == 0:

                            XOR396_tree = self._adaptor.createWithPayload(XOR396)
                            root_0 = self._adaptor.becomeRoot(XOR396_tree, root_0)

                        self._state.following.append(self.FOLLOW_andExpression_in_exclusiveOrExpression10640)
                        andExpression397 = self.andExpression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, andExpression397.tree)


                    else:
                        break #loop113





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 94, exclusiveOrExpression_StartIndex, success)

            pass

        return retval

    # $ANTLR end "exclusiveOrExpression"

    class andExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "andExpression"
    # Java.g:825:1: andExpression : equalityExpression ( AND equalityExpression )* ;
    def andExpression(self, ):

        retval = self.andExpression_return()
        retval.start = self.input.LT(1)
        andExpression_StartIndex = self.input.index()
        root_0 = None

        AND399 = None
        equalityExpression398 = None

        equalityExpression400 = None


        AND399_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 95):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:826:5: ( equalityExpression ( AND equalityExpression )* )
                # Java.g:826:9: equalityExpression ( AND equalityExpression )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_equalityExpression_in_andExpression10661)
                equalityExpression398 = self.equalityExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, equalityExpression398.tree)
                # Java.g:826:28: ( AND equalityExpression )*
                while True: #loop114
                    alt114 = 2
                    LA114_0 = self.input.LA(1)

                    if (LA114_0 == AND) :
                        alt114 = 1


                    if alt114 == 1:
                        # Java.g:826:29: AND equalityExpression
                        pass 
                        AND399=self.match(self.input, AND, self.FOLLOW_AND_in_andExpression10664)
                        if self._state.backtracking == 0:

                            AND399_tree = self._adaptor.createWithPayload(AND399)
                            root_0 = self._adaptor.becomeRoot(AND399_tree, root_0)

                        self._state.following.append(self.FOLLOW_equalityExpression_in_andExpression10667)
                        equalityExpression400 = self.equalityExpression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, equalityExpression400.tree)


                    else:
                        break #loop114





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 95, andExpression_StartIndex, success)

            pass

        return retval

    # $ANTLR end "andExpression"

    class equalityExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "equalityExpression"
    # Java.g:829:1: equalityExpression : instanceOfExpression ( ( EQUAL | NOT_EQUAL ) instanceOfExpression )* ;
    def equalityExpression(self, ):

        retval = self.equalityExpression_return()
        retval.start = self.input.LT(1)
        equalityExpression_StartIndex = self.input.index()
        root_0 = None

        EQUAL402 = None
        NOT_EQUAL403 = None
        instanceOfExpression401 = None

        instanceOfExpression404 = None


        EQUAL402_tree = None
        NOT_EQUAL403_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 96):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:830:5: ( instanceOfExpression ( ( EQUAL | NOT_EQUAL ) instanceOfExpression )* )
                # Java.g:830:9: instanceOfExpression ( ( EQUAL | NOT_EQUAL ) instanceOfExpression )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_instanceOfExpression_in_equalityExpression10688)
                instanceOfExpression401 = self.instanceOfExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, instanceOfExpression401.tree)
                # Java.g:831:9: ( ( EQUAL | NOT_EQUAL ) instanceOfExpression )*
                while True: #loop116
                    alt116 = 2
                    LA116_0 = self.input.LA(1)

                    if (LA116_0 == EQUAL or LA116_0 == NOT_EQUAL) :
                        alt116 = 1


                    if alt116 == 1:
                        # Java.g:831:13: ( EQUAL | NOT_EQUAL ) instanceOfExpression
                        pass 
                        # Java.g:831:13: ( EQUAL | NOT_EQUAL )
                        alt115 = 2
                        LA115_0 = self.input.LA(1)

                        if (LA115_0 == EQUAL) :
                            alt115 = 1
                        elif (LA115_0 == NOT_EQUAL) :
                            alt115 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 115, 0, self.input)

                            raise nvae

                        if alt115 == 1:
                            # Java.g:831:17: EQUAL
                            pass 
                            EQUAL402=self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_equalityExpression10706)
                            if self._state.backtracking == 0:

                                EQUAL402_tree = self._adaptor.createWithPayload(EQUAL402)
                                root_0 = self._adaptor.becomeRoot(EQUAL402_tree, root_0)



                        elif alt115 == 2:
                            # Java.g:832:17: NOT_EQUAL
                            pass 
                            NOT_EQUAL403=self.match(self.input, NOT_EQUAL, self.FOLLOW_NOT_EQUAL_in_equalityExpression10725)
                            if self._state.backtracking == 0:

                                NOT_EQUAL403_tree = self._adaptor.createWithPayload(NOT_EQUAL403)
                                root_0 = self._adaptor.becomeRoot(NOT_EQUAL403_tree, root_0)




                        self._state.following.append(self.FOLLOW_instanceOfExpression_in_equalityExpression10754)
                        instanceOfExpression404 = self.instanceOfExpression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, instanceOfExpression404.tree)


                    else:
                        break #loop116





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 96, equalityExpression_StartIndex, success)

            pass

        return retval

    # $ANTLR end "equalityExpression"

    class instanceOfExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "instanceOfExpression"
    # Java.g:838:1: instanceOfExpression : relationalExpression ( INSTANCEOF type )? ;
    def instanceOfExpression(self, ):

        retval = self.instanceOfExpression_return()
        retval.start = self.input.LT(1)
        instanceOfExpression_StartIndex = self.input.index()
        root_0 = None

        INSTANCEOF406 = None
        relationalExpression405 = None

        type407 = None


        INSTANCEOF406_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 97):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:839:5: ( relationalExpression ( INSTANCEOF type )? )
                # Java.g:839:9: relationalExpression ( INSTANCEOF type )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_relationalExpression_in_instanceOfExpression10784)
                relationalExpression405 = self.relationalExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, relationalExpression405.tree)
                # Java.g:839:30: ( INSTANCEOF type )?
                alt117 = 2
                LA117_0 = self.input.LA(1)

                if (LA117_0 == INSTANCEOF) :
                    alt117 = 1
                if alt117 == 1:
                    # Java.g:839:31: INSTANCEOF type
                    pass 
                    INSTANCEOF406=self.match(self.input, INSTANCEOF, self.FOLLOW_INSTANCEOF_in_instanceOfExpression10787)
                    if self._state.backtracking == 0:

                        INSTANCEOF406_tree = self._adaptor.createWithPayload(INSTANCEOF406)
                        root_0 = self._adaptor.becomeRoot(INSTANCEOF406_tree, root_0)

                    self._state.following.append(self.FOLLOW_type_in_instanceOfExpression10790)
                    type407 = self.type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, type407.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 97, instanceOfExpression_StartIndex, success)

            pass

        return retval

    # $ANTLR end "instanceOfExpression"

    class relationalExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "relationalExpression"
    # Java.g:842:1: relationalExpression : shiftExpression ( ( LESS_OR_EQUAL | GREATER_OR_EQUAL | LESS_THAN | GREATER_THAN ) shiftExpression )* ;
    def relationalExpression(self, ):

        retval = self.relationalExpression_return()
        retval.start = self.input.LT(1)
        relationalExpression_StartIndex = self.input.index()
        root_0 = None

        LESS_OR_EQUAL409 = None
        GREATER_OR_EQUAL410 = None
        LESS_THAN411 = None
        GREATER_THAN412 = None
        shiftExpression408 = None

        shiftExpression413 = None


        LESS_OR_EQUAL409_tree = None
        GREATER_OR_EQUAL410_tree = None
        LESS_THAN411_tree = None
        GREATER_THAN412_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 98):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:843:5: ( shiftExpression ( ( LESS_OR_EQUAL | GREATER_OR_EQUAL | LESS_THAN | GREATER_THAN ) shiftExpression )* )
                # Java.g:843:9: shiftExpression ( ( LESS_OR_EQUAL | GREATER_OR_EQUAL | LESS_THAN | GREATER_THAN ) shiftExpression )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_shiftExpression_in_relationalExpression10811)
                shiftExpression408 = self.shiftExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, shiftExpression408.tree)
                # Java.g:844:9: ( ( LESS_OR_EQUAL | GREATER_OR_EQUAL | LESS_THAN | GREATER_THAN ) shiftExpression )*
                while True: #loop119
                    alt119 = 2
                    LA119_0 = self.input.LA(1)

                    if ((GREATER_OR_EQUAL <= LA119_0 <= GREATER_THAN) or (LESS_OR_EQUAL <= LA119_0 <= LESS_THAN)) :
                        alt119 = 1


                    if alt119 == 1:
                        # Java.g:844:13: ( LESS_OR_EQUAL | GREATER_OR_EQUAL | LESS_THAN | GREATER_THAN ) shiftExpression
                        pass 
                        # Java.g:844:13: ( LESS_OR_EQUAL | GREATER_OR_EQUAL | LESS_THAN | GREATER_THAN )
                        alt118 = 4
                        LA118 = self.input.LA(1)
                        if LA118 == LESS_OR_EQUAL:
                            alt118 = 1
                        elif LA118 == GREATER_OR_EQUAL:
                            alt118 = 2
                        elif LA118 == LESS_THAN:
                            alt118 = 3
                        elif LA118 == GREATER_THAN:
                            alt118 = 4
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 118, 0, self.input)

                            raise nvae

                        if alt118 == 1:
                            # Java.g:844:17: LESS_OR_EQUAL
                            pass 
                            LESS_OR_EQUAL409=self.match(self.input, LESS_OR_EQUAL, self.FOLLOW_LESS_OR_EQUAL_in_relationalExpression10829)
                            if self._state.backtracking == 0:

                                LESS_OR_EQUAL409_tree = self._adaptor.createWithPayload(LESS_OR_EQUAL409)
                                root_0 = self._adaptor.becomeRoot(LESS_OR_EQUAL409_tree, root_0)



                        elif alt118 == 2:
                            # Java.g:845:17: GREATER_OR_EQUAL
                            pass 
                            GREATER_OR_EQUAL410=self.match(self.input, GREATER_OR_EQUAL, self.FOLLOW_GREATER_OR_EQUAL_in_relationalExpression10848)
                            if self._state.backtracking == 0:

                                GREATER_OR_EQUAL410_tree = self._adaptor.createWithPayload(GREATER_OR_EQUAL410)
                                root_0 = self._adaptor.becomeRoot(GREATER_OR_EQUAL410_tree, root_0)



                        elif alt118 == 3:
                            # Java.g:846:17: LESS_THAN
                            pass 
                            LESS_THAN411=self.match(self.input, LESS_THAN, self.FOLLOW_LESS_THAN_in_relationalExpression10867)
                            if self._state.backtracking == 0:

                                LESS_THAN411_tree = self._adaptor.createWithPayload(LESS_THAN411)
                                root_0 = self._adaptor.becomeRoot(LESS_THAN411_tree, root_0)



                        elif alt118 == 4:
                            # Java.g:847:17: GREATER_THAN
                            pass 
                            GREATER_THAN412=self.match(self.input, GREATER_THAN, self.FOLLOW_GREATER_THAN_in_relationalExpression10886)
                            if self._state.backtracking == 0:

                                GREATER_THAN412_tree = self._adaptor.createWithPayload(GREATER_THAN412)
                                root_0 = self._adaptor.becomeRoot(GREATER_THAN412_tree, root_0)




                        self._state.following.append(self.FOLLOW_shiftExpression_in_relationalExpression10915)
                        shiftExpression413 = self.shiftExpression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, shiftExpression413.tree)


                    else:
                        break #loop119





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 98, relationalExpression_StartIndex, success)

            pass

        return retval

    # $ANTLR end "relationalExpression"

    class shiftExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "shiftExpression"
    # Java.g:853:1: shiftExpression : additiveExpression ( ( BIT_SHIFT_RIGHT | SHIFT_RIGHT | SHIFT_LEFT ) additiveExpression )* ;
    def shiftExpression(self, ):

        retval = self.shiftExpression_return()
        retval.start = self.input.LT(1)
        shiftExpression_StartIndex = self.input.index()
        root_0 = None

        BIT_SHIFT_RIGHT415 = None
        SHIFT_RIGHT416 = None
        SHIFT_LEFT417 = None
        additiveExpression414 = None

        additiveExpression418 = None


        BIT_SHIFT_RIGHT415_tree = None
        SHIFT_RIGHT416_tree = None
        SHIFT_LEFT417_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 99):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:854:5: ( additiveExpression ( ( BIT_SHIFT_RIGHT | SHIFT_RIGHT | SHIFT_LEFT ) additiveExpression )* )
                # Java.g:854:9: additiveExpression ( ( BIT_SHIFT_RIGHT | SHIFT_RIGHT | SHIFT_LEFT ) additiveExpression )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_additiveExpression_in_shiftExpression10945)
                additiveExpression414 = self.additiveExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, additiveExpression414.tree)
                # Java.g:855:9: ( ( BIT_SHIFT_RIGHT | SHIFT_RIGHT | SHIFT_LEFT ) additiveExpression )*
                while True: #loop121
                    alt121 = 2
                    LA121_0 = self.input.LA(1)

                    if (LA121_0 == BIT_SHIFT_RIGHT or LA121_0 == SHIFT_LEFT or LA121_0 == SHIFT_RIGHT) :
                        alt121 = 1


                    if alt121 == 1:
                        # Java.g:855:13: ( BIT_SHIFT_RIGHT | SHIFT_RIGHT | SHIFT_LEFT ) additiveExpression
                        pass 
                        # Java.g:855:13: ( BIT_SHIFT_RIGHT | SHIFT_RIGHT | SHIFT_LEFT )
                        alt120 = 3
                        LA120 = self.input.LA(1)
                        if LA120 == BIT_SHIFT_RIGHT:
                            alt120 = 1
                        elif LA120 == SHIFT_RIGHT:
                            alt120 = 2
                        elif LA120 == SHIFT_LEFT:
                            alt120 = 3
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 120, 0, self.input)

                            raise nvae

                        if alt120 == 1:
                            # Java.g:855:17: BIT_SHIFT_RIGHT
                            pass 
                            BIT_SHIFT_RIGHT415=self.match(self.input, BIT_SHIFT_RIGHT, self.FOLLOW_BIT_SHIFT_RIGHT_in_shiftExpression10963)
                            if self._state.backtracking == 0:

                                BIT_SHIFT_RIGHT415_tree = self._adaptor.createWithPayload(BIT_SHIFT_RIGHT415)
                                root_0 = self._adaptor.becomeRoot(BIT_SHIFT_RIGHT415_tree, root_0)



                        elif alt120 == 2:
                            # Java.g:856:17: SHIFT_RIGHT
                            pass 
                            SHIFT_RIGHT416=self.match(self.input, SHIFT_RIGHT, self.FOLLOW_SHIFT_RIGHT_in_shiftExpression10982)
                            if self._state.backtracking == 0:

                                SHIFT_RIGHT416_tree = self._adaptor.createWithPayload(SHIFT_RIGHT416)
                                root_0 = self._adaptor.becomeRoot(SHIFT_RIGHT416_tree, root_0)



                        elif alt120 == 3:
                            # Java.g:857:17: SHIFT_LEFT
                            pass 
                            SHIFT_LEFT417=self.match(self.input, SHIFT_LEFT, self.FOLLOW_SHIFT_LEFT_in_shiftExpression11001)
                            if self._state.backtracking == 0:

                                SHIFT_LEFT417_tree = self._adaptor.createWithPayload(SHIFT_LEFT417)
                                root_0 = self._adaptor.becomeRoot(SHIFT_LEFT417_tree, root_0)




                        self._state.following.append(self.FOLLOW_additiveExpression_in_shiftExpression11030)
                        additiveExpression418 = self.additiveExpression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, additiveExpression418.tree)


                    else:
                        break #loop121





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 99, shiftExpression_StartIndex, success)

            pass

        return retval

    # $ANTLR end "shiftExpression"

    class additiveExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "additiveExpression"
    # Java.g:863:1: additiveExpression : multiplicativeExpression ( ( PLUS | MINUS ) multiplicativeExpression )* ;
    def additiveExpression(self, ):

        retval = self.additiveExpression_return()
        retval.start = self.input.LT(1)
        additiveExpression_StartIndex = self.input.index()
        root_0 = None

        PLUS420 = None
        MINUS421 = None
        multiplicativeExpression419 = None

        multiplicativeExpression422 = None


        PLUS420_tree = None
        MINUS421_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 100):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:864:5: ( multiplicativeExpression ( ( PLUS | MINUS ) multiplicativeExpression )* )
                # Java.g:864:9: multiplicativeExpression ( ( PLUS | MINUS ) multiplicativeExpression )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_multiplicativeExpression_in_additiveExpression11060)
                multiplicativeExpression419 = self.multiplicativeExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, multiplicativeExpression419.tree)
                # Java.g:865:9: ( ( PLUS | MINUS ) multiplicativeExpression )*
                while True: #loop123
                    alt123 = 2
                    LA123_0 = self.input.LA(1)

                    if (LA123_0 == MINUS or LA123_0 == PLUS) :
                        alt123 = 1


                    if alt123 == 1:
                        # Java.g:865:13: ( PLUS | MINUS ) multiplicativeExpression
                        pass 
                        # Java.g:865:13: ( PLUS | MINUS )
                        alt122 = 2
                        LA122_0 = self.input.LA(1)

                        if (LA122_0 == PLUS) :
                            alt122 = 1
                        elif (LA122_0 == MINUS) :
                            alt122 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 122, 0, self.input)

                            raise nvae

                        if alt122 == 1:
                            # Java.g:865:17: PLUS
                            pass 
                            PLUS420=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_additiveExpression11078)
                            if self._state.backtracking == 0:

                                PLUS420_tree = self._adaptor.createWithPayload(PLUS420)
                                root_0 = self._adaptor.becomeRoot(PLUS420_tree, root_0)



                        elif alt122 == 2:
                            # Java.g:866:17: MINUS
                            pass 
                            MINUS421=self.match(self.input, MINUS, self.FOLLOW_MINUS_in_additiveExpression11097)
                            if self._state.backtracking == 0:

                                MINUS421_tree = self._adaptor.createWithPayload(MINUS421)
                                root_0 = self._adaptor.becomeRoot(MINUS421_tree, root_0)




                        self._state.following.append(self.FOLLOW_multiplicativeExpression_in_additiveExpression11126)
                        multiplicativeExpression422 = self.multiplicativeExpression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, multiplicativeExpression422.tree)


                    else:
                        break #loop123





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 100, additiveExpression_StartIndex, success)

            pass

        return retval

    # $ANTLR end "additiveExpression"

    class multiplicativeExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "multiplicativeExpression"
    # Java.g:872:1: multiplicativeExpression : unaryExpression ( ( STAR | DIV | MOD ) unaryExpression )* ;
    def multiplicativeExpression(self, ):

        retval = self.multiplicativeExpression_return()
        retval.start = self.input.LT(1)
        multiplicativeExpression_StartIndex = self.input.index()
        root_0 = None

        STAR424 = None
        DIV425 = None
        MOD426 = None
        unaryExpression423 = None

        unaryExpression427 = None


        STAR424_tree = None
        DIV425_tree = None
        MOD426_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 101):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:873:5: ( unaryExpression ( ( STAR | DIV | MOD ) unaryExpression )* )
                # Java.g:873:9: unaryExpression ( ( STAR | DIV | MOD ) unaryExpression )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_unaryExpression_in_multiplicativeExpression11156)
                unaryExpression423 = self.unaryExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, unaryExpression423.tree)
                # Java.g:874:9: ( ( STAR | DIV | MOD ) unaryExpression )*
                while True: #loop125
                    alt125 = 2
                    LA125_0 = self.input.LA(1)

                    if (LA125_0 == DIV or LA125_0 == MOD or LA125_0 == STAR) :
                        alt125 = 1


                    if alt125 == 1:
                        # Java.g:874:13: ( STAR | DIV | MOD ) unaryExpression
                        pass 
                        # Java.g:874:13: ( STAR | DIV | MOD )
                        alt124 = 3
                        LA124 = self.input.LA(1)
                        if LA124 == STAR:
                            alt124 = 1
                        elif LA124 == DIV:
                            alt124 = 2
                        elif LA124 == MOD:
                            alt124 = 3
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 124, 0, self.input)

                            raise nvae

                        if alt124 == 1:
                            # Java.g:874:17: STAR
                            pass 
                            STAR424=self.match(self.input, STAR, self.FOLLOW_STAR_in_multiplicativeExpression11174)
                            if self._state.backtracking == 0:

                                STAR424_tree = self._adaptor.createWithPayload(STAR424)
                                root_0 = self._adaptor.becomeRoot(STAR424_tree, root_0)



                        elif alt124 == 2:
                            # Java.g:875:17: DIV
                            pass 
                            DIV425=self.match(self.input, DIV, self.FOLLOW_DIV_in_multiplicativeExpression11193)
                            if self._state.backtracking == 0:

                                DIV425_tree = self._adaptor.createWithPayload(DIV425)
                                root_0 = self._adaptor.becomeRoot(DIV425_tree, root_0)



                        elif alt124 == 3:
                            # Java.g:876:17: MOD
                            pass 
                            MOD426=self.match(self.input, MOD, self.FOLLOW_MOD_in_multiplicativeExpression11212)
                            if self._state.backtracking == 0:

                                MOD426_tree = self._adaptor.createWithPayload(MOD426)
                                root_0 = self._adaptor.becomeRoot(MOD426_tree, root_0)




                        self._state.following.append(self.FOLLOW_unaryExpression_in_multiplicativeExpression11241)
                        unaryExpression427 = self.unaryExpression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, unaryExpression427.tree)


                    else:
                        break #loop125





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 101, multiplicativeExpression_StartIndex, success)

            pass

        return retval

    # $ANTLR end "multiplicativeExpression"

    class unaryExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "unaryExpression"
    # Java.g:882:1: unaryExpression : ( PLUS unaryExpression -> ^( UNARY_PLUS[$PLUS, \"UNARY_PLUS\"] unaryExpression ) | MINUS unaryExpression -> ^( UNARY_MINUS[$MINUS, \"UNARY_MINUS\"] unaryExpression ) | INC postfixedExpression -> ^( PRE_INC[$INC, \"PRE_INC\"] postfixedExpression ) | DEC postfixedExpression -> ^( PRE_DEC[$DEC, \"PRE_DEC\"] postfixedExpression ) | unaryExpressionNotPlusMinus );
    def unaryExpression(self, ):

        retval = self.unaryExpression_return()
        retval.start = self.input.LT(1)
        unaryExpression_StartIndex = self.input.index()
        root_0 = None

        PLUS428 = None
        MINUS430 = None
        INC432 = None
        DEC434 = None
        unaryExpression429 = None

        unaryExpression431 = None

        postfixedExpression433 = None

        postfixedExpression435 = None

        unaryExpressionNotPlusMinus436 = None


        PLUS428_tree = None
        MINUS430_tree = None
        INC432_tree = None
        DEC434_tree = None
        stream_DEC = RewriteRuleTokenStream(self._adaptor, "token DEC")
        stream_INC = RewriteRuleTokenStream(self._adaptor, "token INC")
        stream_PLUS = RewriteRuleTokenStream(self._adaptor, "token PLUS")
        stream_MINUS = RewriteRuleTokenStream(self._adaptor, "token MINUS")
        stream_postfixedExpression = RewriteRuleSubtreeStream(self._adaptor, "rule postfixedExpression")
        stream_unaryExpression = RewriteRuleSubtreeStream(self._adaptor, "rule unaryExpression")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 102):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:883:5: ( PLUS unaryExpression -> ^( UNARY_PLUS[$PLUS, \"UNARY_PLUS\"] unaryExpression ) | MINUS unaryExpression -> ^( UNARY_MINUS[$MINUS, \"UNARY_MINUS\"] unaryExpression ) | INC postfixedExpression -> ^( PRE_INC[$INC, \"PRE_INC\"] postfixedExpression ) | DEC postfixedExpression -> ^( PRE_DEC[$DEC, \"PRE_DEC\"] postfixedExpression ) | unaryExpressionNotPlusMinus )
                alt126 = 5
                LA126 = self.input.LA(1)
                if LA126 == PLUS:
                    alt126 = 1
                elif LA126 == MINUS:
                    alt126 = 2
                elif LA126 == INC:
                    alt126 = 3
                elif LA126 == DEC:
                    alt126 = 4
                elif LA126 == LESS_THAN or LA126 == LOGICAL_NOT or LA126 == LPAREN or LA126 == NOT or LA126 == BOOLEAN or LA126 == BYTE or LA126 == CHAR or LA126 == DOUBLE or LA126 == FALSE or LA126 == FLOAT or LA126 == INT or LA126 == LONG or LA126 == NEW or LA126 == NULL or LA126 == SHORT or LA126 == SUPER or LA126 == THIS or LA126 == TRUE or LA126 == VOID or LA126 == IDENT or LA126 == HEX_LITERAL or LA126 == OCTAL_LITERAL or LA126 == DECIMAL_LITERAL or LA126 == FLOATING_POINT_LITERAL or LA126 == CHARACTER_LITERAL or LA126 == STRING_LITERAL:
                    alt126 = 5
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 126, 0, self.input)

                    raise nvae

                if alt126 == 1:
                    # Java.g:883:9: PLUS unaryExpression
                    pass 
                    PLUS428=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_unaryExpression11271) 
                    if self._state.backtracking == 0:
                        stream_PLUS.add(PLUS428)
                    self._state.following.append(self.FOLLOW_unaryExpression_in_unaryExpression11273)
                    unaryExpression429 = self.unaryExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_unaryExpression.add(unaryExpression429.tree)

                    # AST Rewrite
                    # elements: unaryExpression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 883:37: -> ^( UNARY_PLUS[$PLUS, \"UNARY_PLUS\"] unaryExpression )
                        # Java.g:883:41: ^( UNARY_PLUS[$PLUS, \"UNARY_PLUS\"] unaryExpression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.create(UNARY_PLUS, PLUS428, "UNARY_PLUS"), root_1)

                        self._adaptor.addChild(root_1, stream_unaryExpression.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt126 == 2:
                    # Java.g:884:9: MINUS unaryExpression
                    pass 
                    MINUS430=self.match(self.input, MINUS, self.FOLLOW_MINUS_in_unaryExpression11300) 
                    if self._state.backtracking == 0:
                        stream_MINUS.add(MINUS430)
                    self._state.following.append(self.FOLLOW_unaryExpression_in_unaryExpression11302)
                    unaryExpression431 = self.unaryExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_unaryExpression.add(unaryExpression431.tree)

                    # AST Rewrite
                    # elements: unaryExpression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 884:37: -> ^( UNARY_MINUS[$MINUS, \"UNARY_MINUS\"] unaryExpression )
                        # Java.g:884:41: ^( UNARY_MINUS[$MINUS, \"UNARY_MINUS\"] unaryExpression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.create(UNARY_MINUS, MINUS430, "UNARY_MINUS"), root_1)

                        self._adaptor.addChild(root_1, stream_unaryExpression.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt126 == 3:
                    # Java.g:885:9: INC postfixedExpression
                    pass 
                    INC432=self.match(self.input, INC, self.FOLLOW_INC_in_unaryExpression11328) 
                    if self._state.backtracking == 0:
                        stream_INC.add(INC432)
                    self._state.following.append(self.FOLLOW_postfixedExpression_in_unaryExpression11330)
                    postfixedExpression433 = self.postfixedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_postfixedExpression.add(postfixedExpression433.tree)

                    # AST Rewrite
                    # elements: postfixedExpression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 885:37: -> ^( PRE_INC[$INC, \"PRE_INC\"] postfixedExpression )
                        # Java.g:885:41: ^( PRE_INC[$INC, \"PRE_INC\"] postfixedExpression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.create(PRE_INC, INC432, "PRE_INC"), root_1)

                        self._adaptor.addChild(root_1, stream_postfixedExpression.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt126 == 4:
                    # Java.g:886:9: DEC postfixedExpression
                    pass 
                    DEC434=self.match(self.input, DEC, self.FOLLOW_DEC_in_unaryExpression11354) 
                    if self._state.backtracking == 0:
                        stream_DEC.add(DEC434)
                    self._state.following.append(self.FOLLOW_postfixedExpression_in_unaryExpression11356)
                    postfixedExpression435 = self.postfixedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_postfixedExpression.add(postfixedExpression435.tree)

                    # AST Rewrite
                    # elements: postfixedExpression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 886:37: -> ^( PRE_DEC[$DEC, \"PRE_DEC\"] postfixedExpression )
                        # Java.g:886:41: ^( PRE_DEC[$DEC, \"PRE_DEC\"] postfixedExpression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.create(PRE_DEC, DEC434, "PRE_DEC"), root_1)

                        self._adaptor.addChild(root_1, stream_postfixedExpression.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt126 == 5:
                    # Java.g:887:9: unaryExpressionNotPlusMinus
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_unaryExpressionNotPlusMinus_in_unaryExpression11380)
                    unaryExpressionNotPlusMinus436 = self.unaryExpressionNotPlusMinus()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, unaryExpressionNotPlusMinus436.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 102, unaryExpression_StartIndex, success)

            pass

        return retval

    # $ANTLR end "unaryExpression"

    class unaryExpressionNotPlusMinus_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "unaryExpressionNotPlusMinus"
    # Java.g:890:1: unaryExpressionNotPlusMinus : ( NOT unaryExpression -> ^( NOT unaryExpression ) | LOGICAL_NOT unaryExpression -> ^( LOGICAL_NOT unaryExpression ) | LPAREN type RPAREN unaryExpression -> ^( CAST_EXPR[$LPAREN, \"CAST_EXPR\"] type unaryExpression ) | postfixedExpression );
    def unaryExpressionNotPlusMinus(self, ):

        retval = self.unaryExpressionNotPlusMinus_return()
        retval.start = self.input.LT(1)
        unaryExpressionNotPlusMinus_StartIndex = self.input.index()
        root_0 = None

        NOT437 = None
        LOGICAL_NOT439 = None
        LPAREN441 = None
        RPAREN443 = None
        unaryExpression438 = None

        unaryExpression440 = None

        type442 = None

        unaryExpression444 = None

        postfixedExpression445 = None


        NOT437_tree = None
        LOGICAL_NOT439_tree = None
        LPAREN441_tree = None
        RPAREN443_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_LOGICAL_NOT = RewriteRuleTokenStream(self._adaptor, "token LOGICAL_NOT")
        stream_NOT = RewriteRuleTokenStream(self._adaptor, "token NOT")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_unaryExpression = RewriteRuleSubtreeStream(self._adaptor, "rule unaryExpression")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 103):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:891:5: ( NOT unaryExpression -> ^( NOT unaryExpression ) | LOGICAL_NOT unaryExpression -> ^( LOGICAL_NOT unaryExpression ) | LPAREN type RPAREN unaryExpression -> ^( CAST_EXPR[$LPAREN, \"CAST_EXPR\"] type unaryExpression ) | postfixedExpression )
                alt127 = 4
                alt127 = self.dfa127.predict(self.input)
                if alt127 == 1:
                    # Java.g:891:9: NOT unaryExpression
                    pass 
                    NOT437=self.match(self.input, NOT, self.FOLLOW_NOT_in_unaryExpressionNotPlusMinus11399) 
                    if self._state.backtracking == 0:
                        stream_NOT.add(NOT437)
                    self._state.following.append(self.FOLLOW_unaryExpression_in_unaryExpressionNotPlusMinus11401)
                    unaryExpression438 = self.unaryExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_unaryExpression.add(unaryExpression438.tree)

                    # AST Rewrite
                    # elements: NOT, unaryExpression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 891:57: -> ^( NOT unaryExpression )
                        # Java.g:891:61: ^( NOT unaryExpression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_NOT.nextNode(), root_1)

                        self._adaptor.addChild(root_1, stream_unaryExpression.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt127 == 2:
                    # Java.g:892:9: LOGICAL_NOT unaryExpression
                    pass 
                    LOGICAL_NOT439=self.match(self.input, LOGICAL_NOT, self.FOLLOW_LOGICAL_NOT_in_unaryExpressionNotPlusMinus11448) 
                    if self._state.backtracking == 0:
                        stream_LOGICAL_NOT.add(LOGICAL_NOT439)
                    self._state.following.append(self.FOLLOW_unaryExpression_in_unaryExpressionNotPlusMinus11450)
                    unaryExpression440 = self.unaryExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_unaryExpression.add(unaryExpression440.tree)

                    # AST Rewrite
                    # elements: LOGICAL_NOT, unaryExpression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 892:57: -> ^( LOGICAL_NOT unaryExpression )
                        # Java.g:892:61: ^( LOGICAL_NOT unaryExpression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_LOGICAL_NOT.nextNode(), root_1)

                        self._adaptor.addChild(root_1, stream_unaryExpression.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt127 == 3:
                    # Java.g:893:9: LPAREN type RPAREN unaryExpression
                    pass 
                    LPAREN441=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_unaryExpressionNotPlusMinus11489) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN441)
                    self._state.following.append(self.FOLLOW_type_in_unaryExpressionNotPlusMinus11491)
                    type442 = self.type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_type.add(type442.tree)
                    RPAREN443=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_unaryExpressionNotPlusMinus11493) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN443)
                    self._state.following.append(self.FOLLOW_unaryExpression_in_unaryExpressionNotPlusMinus11495)
                    unaryExpression444 = self.unaryExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_unaryExpression.add(unaryExpression444.tree)

                    # AST Rewrite
                    # elements: unaryExpression, type
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 893:57: -> ^( CAST_EXPR[$LPAREN, \"CAST_EXPR\"] type unaryExpression )
                        # Java.g:893:61: ^( CAST_EXPR[$LPAREN, \"CAST_EXPR\"] type unaryExpression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.create(CAST_EXPR, LPAREN441, "CAST_EXPR"), root_1)

                        self._adaptor.addChild(root_1, stream_type.nextTree())
                        self._adaptor.addChild(root_1, stream_unaryExpression.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt127 == 4:
                    # Java.g:894:9: postfixedExpression
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_postfixedExpression_in_unaryExpressionNotPlusMinus11530)
                    postfixedExpression445 = self.postfixedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, postfixedExpression445.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 103, unaryExpressionNotPlusMinus_StartIndex, success)

            pass

        return retval

    # $ANTLR end "unaryExpressionNotPlusMinus"

    class postfixedExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "postfixedExpression"
    # Java.g:897:1: postfixedExpression : ( primaryExpression -> primaryExpression ) (outerDot= DOT ( ( ( genericTypeArgumentListSimplified )? IDENT -> ^( DOT $postfixedExpression IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression ( genericTypeArgumentListSimplified )? arguments ) )? | THIS -> ^( DOT $postfixedExpression THIS ) | Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] $postfixedExpression arguments ) | ( SUPER innerDot= DOT IDENT -> ^( $innerDot ^( $outerDot $postfixedExpression SUPER ) IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression arguments ) )? | innerNewExpression -> ^( DOT $postfixedExpression innerNewExpression ) ) | LBRACK expression RBRACK -> ^( ARRAY_ELEMENT_ACCESS $postfixedExpression expression ) )* ( INC -> ^( POST_INC[$INC, \"POST_INC\"] $postfixedExpression) | DEC -> ^( POST_DEC[$DEC, \"POST_DEC\"] $postfixedExpression) )? ;
    def postfixedExpression(self, ):

        retval = self.postfixedExpression_return()
        retval.start = self.input.LT(1)
        postfixedExpression_StartIndex = self.input.index()
        root_0 = None

        outerDot = None
        Super = None
        innerDot = None
        IDENT448 = None
        THIS450 = None
        SUPER452 = None
        IDENT453 = None
        LBRACK456 = None
        RBRACK458 = None
        INC459 = None
        DEC460 = None
        primaryExpression446 = None

        genericTypeArgumentListSimplified447 = None

        arguments449 = None

        arguments451 = None

        arguments454 = None

        innerNewExpression455 = None

        expression457 = None


        outerDot_tree = None
        Super_tree = None
        innerDot_tree = None
        IDENT448_tree = None
        THIS450_tree = None
        SUPER452_tree = None
        IDENT453_tree = None
        LBRACK456_tree = None
        RBRACK458_tree = None
        INC459_tree = None
        DEC460_tree = None
        stream_RBRACK = RewriteRuleTokenStream(self._adaptor, "token RBRACK")
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_INC = RewriteRuleTokenStream(self._adaptor, "token INC")
        stream_DEC = RewriteRuleTokenStream(self._adaptor, "token DEC")
        stream_LBRACK = RewriteRuleTokenStream(self._adaptor, "token LBRACK")
        stream_SUPER = RewriteRuleTokenStream(self._adaptor, "token SUPER")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_THIS = RewriteRuleTokenStream(self._adaptor, "token THIS")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        stream_arguments = RewriteRuleSubtreeStream(self._adaptor, "rule arguments")
        stream_primaryExpression = RewriteRuleSubtreeStream(self._adaptor, "rule primaryExpression")
        stream_genericTypeArgumentListSimplified = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeArgumentListSimplified")
        stream_innerNewExpression = RewriteRuleSubtreeStream(self._adaptor, "rule innerNewExpression")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 104):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:899:5: ( ( primaryExpression -> primaryExpression ) (outerDot= DOT ( ( ( genericTypeArgumentListSimplified )? IDENT -> ^( DOT $postfixedExpression IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression ( genericTypeArgumentListSimplified )? arguments ) )? | THIS -> ^( DOT $postfixedExpression THIS ) | Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] $postfixedExpression arguments ) | ( SUPER innerDot= DOT IDENT -> ^( $innerDot ^( $outerDot $postfixedExpression SUPER ) IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression arguments ) )? | innerNewExpression -> ^( DOT $postfixedExpression innerNewExpression ) ) | LBRACK expression RBRACK -> ^( ARRAY_ELEMENT_ACCESS $postfixedExpression expression ) )* ( INC -> ^( POST_INC[$INC, \"POST_INC\"] $postfixedExpression) | DEC -> ^( POST_DEC[$DEC, \"POST_DEC\"] $postfixedExpression) )? )
                # Java.g:899:9: ( primaryExpression -> primaryExpression ) (outerDot= DOT ( ( ( genericTypeArgumentListSimplified )? IDENT -> ^( DOT $postfixedExpression IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression ( genericTypeArgumentListSimplified )? arguments ) )? | THIS -> ^( DOT $postfixedExpression THIS ) | Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] $postfixedExpression arguments ) | ( SUPER innerDot= DOT IDENT -> ^( $innerDot ^( $outerDot $postfixedExpression SUPER ) IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression arguments ) )? | innerNewExpression -> ^( DOT $postfixedExpression innerNewExpression ) ) | LBRACK expression RBRACK -> ^( ARRAY_ELEMENT_ACCESS $postfixedExpression expression ) )* ( INC -> ^( POST_INC[$INC, \"POST_INC\"] $postfixedExpression) | DEC -> ^( POST_DEC[$DEC, \"POST_DEC\"] $postfixedExpression) )?
                pass 
                # Java.g:899:9: ( primaryExpression -> primaryExpression )
                # Java.g:899:13: primaryExpression
                pass 
                self._state.following.append(self.FOLLOW_primaryExpression_in_postfixedExpression11562)
                primaryExpression446 = self.primaryExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_primaryExpression.add(primaryExpression446.tree)

                # AST Rewrite
                # elements: primaryExpression
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 899:53: -> primaryExpression
                    self._adaptor.addChild(root_0, stream_primaryExpression.nextTree())



                    retval.tree = root_0



                # Java.g:902:9: (outerDot= DOT ( ( ( genericTypeArgumentListSimplified )? IDENT -> ^( DOT $postfixedExpression IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression ( genericTypeArgumentListSimplified )? arguments ) )? | THIS -> ^( DOT $postfixedExpression THIS ) | Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] $postfixedExpression arguments ) | ( SUPER innerDot= DOT IDENT -> ^( $innerDot ^( $outerDot $postfixedExpression SUPER ) IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression arguments ) )? | innerNewExpression -> ^( DOT $postfixedExpression innerNewExpression ) ) | LBRACK expression RBRACK -> ^( ARRAY_ELEMENT_ACCESS $postfixedExpression expression ) )*
                while True: #loop132
                    alt132 = 3
                    LA132_0 = self.input.LA(1)

                    if (LA132_0 == DOT) :
                        alt132 = 1
                    elif (LA132_0 == LBRACK) :
                        alt132 = 2


                    if alt132 == 1:
                        # Java.g:902:13: outerDot= DOT ( ( ( genericTypeArgumentListSimplified )? IDENT -> ^( DOT $postfixedExpression IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression ( genericTypeArgumentListSimplified )? arguments ) )? | THIS -> ^( DOT $postfixedExpression THIS ) | Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] $postfixedExpression arguments ) | ( SUPER innerDot= DOT IDENT -> ^( $innerDot ^( $outerDot $postfixedExpression SUPER ) IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression arguments ) )? | innerNewExpression -> ^( DOT $postfixedExpression innerNewExpression ) )
                        pass 
                        outerDot=self.match(self.input, DOT, self.FOLLOW_DOT_in_postfixedExpression11624) 
                        if self._state.backtracking == 0:
                            stream_DOT.add(outerDot)
                        # Java.g:903:13: ( ( ( genericTypeArgumentListSimplified )? IDENT -> ^( DOT $postfixedExpression IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression ( genericTypeArgumentListSimplified )? arguments ) )? | THIS -> ^( DOT $postfixedExpression THIS ) | Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] $postfixedExpression arguments ) | ( SUPER innerDot= DOT IDENT -> ^( $innerDot ^( $outerDot $postfixedExpression SUPER ) IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression arguments ) )? | innerNewExpression -> ^( DOT $postfixedExpression innerNewExpression ) )
                        alt131 = 5
                        LA131 = self.input.LA(1)
                        if LA131 == LESS_THAN or LA131 == IDENT:
                            alt131 = 1
                        elif LA131 == THIS:
                            alt131 = 2
                        elif LA131 == SUPER:
                            LA131_3 = self.input.LA(2)

                            if (LA131_3 == DOT) :
                                alt131 = 4
                            elif (LA131_3 == LPAREN) :
                                alt131 = 3
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                nvae = NoViableAltException("", 131, 3, self.input)

                                raise nvae

                        elif LA131 == NEW:
                            alt131 = 5
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 131, 0, self.input)

                            raise nvae

                        if alt131 == 1:
                            # Java.g:903:17: ( ( genericTypeArgumentListSimplified )? IDENT -> ^( DOT $postfixedExpression IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression ( genericTypeArgumentListSimplified )? arguments ) )?
                            pass 
                            # Java.g:903:17: ( ( genericTypeArgumentListSimplified )? IDENT -> ^( DOT $postfixedExpression IDENT ) )
                            # Java.g:903:21: ( genericTypeArgumentListSimplified )? IDENT
                            pass 
                            # Java.g:903:21: ( genericTypeArgumentListSimplified )?
                            alt128 = 2
                            LA128_0 = self.input.LA(1)

                            if (LA128_0 == LESS_THAN) :
                                alt128 = 1
                            if alt128 == 1:
                                # Java.g:0:0: genericTypeArgumentListSimplified
                                pass 
                                self._state.following.append(self.FOLLOW_genericTypeArgumentListSimplified_in_postfixedExpression11646)
                                genericTypeArgumentListSimplified447 = self.genericTypeArgumentListSimplified()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    stream_genericTypeArgumentListSimplified.add(genericTypeArgumentListSimplified447.tree)



                            IDENT448=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_postfixedExpression11728) 
                            if self._state.backtracking == 0:
                                stream_IDENT.add(IDENT448)

                            # AST Rewrite
                            # elements: IDENT, DOT, postfixedExpression
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            if self._state.backtracking == 0:

                                retval.tree = root_0

                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 905:53: -> ^( DOT $postfixedExpression IDENT )
                                # Java.g:905:57: ^( DOT $postfixedExpression IDENT )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(stream_DOT.nextNode(), root_1)

                                self._adaptor.addChild(root_1, stream_retval.nextTree())
                                self._adaptor.addChild(root_1, stream_IDENT.nextNode())

                                self._adaptor.addChild(root_0, root_1)



                                retval.tree = root_0



                            # Java.g:907:17: ( arguments -> ^( METHOD_CALL $postfixedExpression ( genericTypeArgumentListSimplified )? arguments ) )?
                            alt129 = 2
                            LA129_0 = self.input.LA(1)

                            if (LA129_0 == LPAREN) :
                                alt129 = 1
                            if alt129 == 1:
                                # Java.g:907:21: arguments
                                pass 
                                self._state.following.append(self.FOLLOW_arguments_in_postfixedExpression11806)
                                arguments449 = self.arguments()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    stream_arguments.add(arguments449.tree)

                                # AST Rewrite
                                # elements: postfixedExpression, arguments, genericTypeArgumentListSimplified
                                # token labels: 
                                # rule labels: retval
                                # token list labels: 
                                # rule list labels: 
                                if self._state.backtracking == 0:

                                    retval.tree = root_0

                                    if retval is not None:
                                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                                    else:
                                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                    root_0 = self._adaptor.nil()
                                    # 907:53: -> ^( METHOD_CALL $postfixedExpression ( genericTypeArgumentListSimplified )? arguments )
                                    # Java.g:907:57: ^( METHOD_CALL $postfixedExpression ( genericTypeArgumentListSimplified )? arguments )
                                    root_1 = self._adaptor.nil()
                                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(METHOD_CALL, "METHOD_CALL"), root_1)

                                    self._adaptor.addChild(root_1, stream_retval.nextTree())
                                    # Java.g:907:92: ( genericTypeArgumentListSimplified )?
                                    if stream_genericTypeArgumentListSimplified.hasNext():
                                        self._adaptor.addChild(root_1, stream_genericTypeArgumentListSimplified.nextTree())


                                    stream_genericTypeArgumentListSimplified.reset();
                                    self._adaptor.addChild(root_1, stream_arguments.nextTree())

                                    self._adaptor.addChild(root_0, root_1)



                                    retval.tree = root_0





                        elif alt131 == 2:
                            # Java.g:909:17: THIS
                            pass 
                            THIS450=self.match(self.input, THIS, self.FOLLOW_THIS_in_postfixedExpression11880) 
                            if self._state.backtracking == 0:
                                stream_THIS.add(THIS450)

                            # AST Rewrite
                            # elements: postfixedExpression, DOT, THIS
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            if self._state.backtracking == 0:

                                retval.tree = root_0

                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 909:53: -> ^( DOT $postfixedExpression THIS )
                                # Java.g:909:57: ^( DOT $postfixedExpression THIS )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(stream_DOT.nextNode(), root_1)

                                self._adaptor.addChild(root_1, stream_retval.nextTree())
                                self._adaptor.addChild(root_1, stream_THIS.nextNode())

                                self._adaptor.addChild(root_0, root_1)



                                retval.tree = root_0


                        elif alt131 == 3:
                            # Java.g:910:17: Super= SUPER arguments
                            pass 
                            Super=self.match(self.input, SUPER, self.FOLLOW_SUPER_in_postfixedExpression11943) 
                            if self._state.backtracking == 0:
                                stream_SUPER.add(Super)
                            self._state.following.append(self.FOLLOW_arguments_in_postfixedExpression11945)
                            arguments451 = self.arguments()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_arguments.add(arguments451.tree)

                            # AST Rewrite
                            # elements: arguments, postfixedExpression
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            if self._state.backtracking == 0:

                                retval.tree = root_0

                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 910:57: -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] $postfixedExpression arguments )
                                # Java.g:910:61: ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] $postfixedExpression arguments )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(self._adaptor.create(SUPER_CONSTRUCTOR_CALL, Super, "SUPER_CONSTRUCTOR_CALL"), root_1)

                                self._adaptor.addChild(root_1, stream_retval.nextTree())
                                self._adaptor.addChild(root_1, stream_arguments.nextTree())

                                self._adaptor.addChild(root_0, root_1)



                                retval.tree = root_0


                        elif alt131 == 4:
                            # Java.g:911:17: ( SUPER innerDot= DOT IDENT -> ^( $innerDot ^( $outerDot $postfixedExpression SUPER ) IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression arguments ) )?
                            pass 
                            # Java.g:911:17: ( SUPER innerDot= DOT IDENT -> ^( $innerDot ^( $outerDot $postfixedExpression SUPER ) IDENT ) )
                            # Java.g:911:21: SUPER innerDot= DOT IDENT
                            pass 
                            SUPER452=self.match(self.input, SUPER, self.FOLLOW_SUPER_in_postfixedExpression11998) 
                            if self._state.backtracking == 0:
                                stream_SUPER.add(SUPER452)
                            innerDot=self.match(self.input, DOT, self.FOLLOW_DOT_in_postfixedExpression12002) 
                            if self._state.backtracking == 0:
                                stream_DOT.add(innerDot)
                            IDENT453=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_postfixedExpression12004) 
                            if self._state.backtracking == 0:
                                stream_IDENT.add(IDENT453)

                            # AST Rewrite
                            # elements: innerDot, postfixedExpression, outerDot, SUPER, IDENT
                            # token labels: outerDot, innerDot
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            if self._state.backtracking == 0:

                                retval.tree = root_0
                                stream_outerDot = RewriteRuleTokenStream(self._adaptor, "token outerDot", outerDot)
                                stream_innerDot = RewriteRuleTokenStream(self._adaptor, "token innerDot", innerDot)

                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 911:53: -> ^( $innerDot ^( $outerDot $postfixedExpression SUPER ) IDENT )
                                # Java.g:911:57: ^( $innerDot ^( $outerDot $postfixedExpression SUPER ) IDENT )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(stream_innerDot.nextNode(), root_1)

                                # Java.g:911:69: ^( $outerDot $postfixedExpression SUPER )
                                root_2 = self._adaptor.nil()
                                root_2 = self._adaptor.becomeRoot(stream_outerDot.nextNode(), root_2)

                                self._adaptor.addChild(root_2, stream_retval.nextTree())
                                self._adaptor.addChild(root_2, stream_SUPER.nextNode())

                                self._adaptor.addChild(root_1, root_2)
                                self._adaptor.addChild(root_1, stream_IDENT.nextNode())

                                self._adaptor.addChild(root_0, root_1)



                                retval.tree = root_0



                            # Java.g:913:17: ( arguments -> ^( METHOD_CALL $postfixedExpression arguments ) )?
                            alt130 = 2
                            LA130_0 = self.input.LA(1)

                            if (LA130_0 == LPAREN) :
                                alt130 = 1
                            if alt130 == 1:
                                # Java.g:913:21: arguments
                                pass 
                                self._state.following.append(self.FOLLOW_arguments_in_postfixedExpression12071)
                                arguments454 = self.arguments()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    stream_arguments.add(arguments454.tree)

                                # AST Rewrite
                                # elements: postfixedExpression, arguments
                                # token labels: 
                                # rule labels: retval
                                # token list labels: 
                                # rule list labels: 
                                if self._state.backtracking == 0:

                                    retval.tree = root_0

                                    if retval is not None:
                                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                                    else:
                                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                    root_0 = self._adaptor.nil()
                                    # 913:53: -> ^( METHOD_CALL $postfixedExpression arguments )
                                    # Java.g:913:57: ^( METHOD_CALL $postfixedExpression arguments )
                                    root_1 = self._adaptor.nil()
                                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(METHOD_CALL, "METHOD_CALL"), root_1)

                                    self._adaptor.addChild(root_1, stream_retval.nextTree())
                                    self._adaptor.addChild(root_1, stream_arguments.nextTree())

                                    self._adaptor.addChild(root_0, root_1)



                                    retval.tree = root_0





                        elif alt131 == 5:
                            # Java.g:915:17: innerNewExpression
                            pass 
                            self._state.following.append(self.FOLLOW_innerNewExpression_in_postfixedExpression12142)
                            innerNewExpression455 = self.innerNewExpression()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_innerNewExpression.add(innerNewExpression455.tree)

                            # AST Rewrite
                            # elements: DOT, postfixedExpression, innerNewExpression
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            if self._state.backtracking == 0:

                                retval.tree = root_0

                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 915:53: -> ^( DOT $postfixedExpression innerNewExpression )
                                # Java.g:915:57: ^( DOT $postfixedExpression innerNewExpression )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(stream_DOT.nextNode(), root_1)

                                self._adaptor.addChild(root_1, stream_retval.nextTree())
                                self._adaptor.addChild(root_1, stream_innerNewExpression.nextTree())

                                self._adaptor.addChild(root_0, root_1)



                                retval.tree = root_0





                    elif alt132 == 2:
                        # Java.g:917:13: LBRACK expression RBRACK
                        pass 
                        LBRACK456=self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_postfixedExpression12199) 
                        if self._state.backtracking == 0:
                            stream_LBRACK.add(LBRACK456)
                        self._state.following.append(self.FOLLOW_expression_in_postfixedExpression12201)
                        expression457 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_expression.add(expression457.tree)
                        RBRACK458=self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_postfixedExpression12203) 
                        if self._state.backtracking == 0:
                            stream_RBRACK.add(RBRACK458)

                        # AST Rewrite
                        # elements: expression, postfixedExpression
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 917:53: -> ^( ARRAY_ELEMENT_ACCESS $postfixedExpression expression )
                            # Java.g:917:57: ^( ARRAY_ELEMENT_ACCESS $postfixedExpression expression )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ARRAY_ELEMENT_ACCESS, "ARRAY_ELEMENT_ACCESS"), root_1)

                            self._adaptor.addChild(root_1, stream_retval.nextTree())
                            self._adaptor.addChild(root_1, stream_expression.nextTree())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    else:
                        break #loop132


                # Java.g:920:9: ( INC -> ^( POST_INC[$INC, \"POST_INC\"] $postfixedExpression) | DEC -> ^( POST_DEC[$DEC, \"POST_DEC\"] $postfixedExpression) )?
                alt133 = 3
                LA133_0 = self.input.LA(1)

                if (LA133_0 == INC) :
                    alt133 = 1
                elif (LA133_0 == DEC) :
                    alt133 = 2
                if alt133 == 1:
                    # Java.g:920:13: INC
                    pass 
                    INC459=self.match(self.input, INC, self.FOLLOW_INC_in_postfixedExpression12264) 
                    if self._state.backtracking == 0:
                        stream_INC.add(INC459)

                    # AST Rewrite
                    # elements: postfixedExpression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 920:17: -> ^( POST_INC[$INC, \"POST_INC\"] $postfixedExpression)
                        # Java.g:920:20: ^( POST_INC[$INC, \"POST_INC\"] $postfixedExpression)
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.create(POST_INC, INC459, "POST_INC"), root_1)

                        self._adaptor.addChild(root_1, stream_retval.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt133 == 2:
                    # Java.g:921:13: DEC
                    pass 
                    DEC460=self.match(self.input, DEC, self.FOLLOW_DEC_in_postfixedExpression12288) 
                    if self._state.backtracking == 0:
                        stream_DEC.add(DEC460)

                    # AST Rewrite
                    # elements: postfixedExpression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 921:17: -> ^( POST_DEC[$DEC, \"POST_DEC\"] $postfixedExpression)
                        # Java.g:921:20: ^( POST_DEC[$DEC, \"POST_DEC\"] $postfixedExpression)
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.create(POST_DEC, DEC460, "POST_DEC"), root_1)

                        self._adaptor.addChild(root_1, stream_retval.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 104, postfixedExpression_StartIndex, success)

            pass

        return retval

    # $ANTLR end "postfixedExpression"

    class primaryExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "primaryExpression"
    # Java.g:925:1: primaryExpression : ( parenthesizedExpression | literal | newExpression | qualifiedIdentExpression | genericTypeArgumentListSimplified ( SUPER ( arguments -> ^( SUPER_CONSTRUCTOR_CALL[$SUPER, \"SUPER_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments ) | DOT IDENT arguments -> ^( METHOD_CALL ^( DOT SUPER IDENT ) genericTypeArgumentListSimplified arguments ) ) | IDENT arguments -> ^( METHOD_CALL IDENT genericTypeArgumentListSimplified arguments ) | THIS arguments -> ^( THIS_CONSTRUCTOR_CALL[$THIS, \"THIS_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments ) ) | ( THIS -> THIS ) ( arguments -> ^( THIS_CONSTRUCTOR_CALL[$THIS, \"THIS_CONSTRUCTOR_CALL\"] arguments ) )? | SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$SUPER, \"SUPER_CONSTRUCTOR_CALL\"] arguments ) | ( SUPER DOT IDENT ) ( arguments -> ^( METHOD_CALL ^( DOT SUPER IDENT ) arguments ) | -> ^( DOT SUPER IDENT ) ) | ( primitiveType -> primitiveType ) ( arrayDeclarator -> ^( arrayDeclarator $primaryExpression) )* DOT CLASS -> ^( DOT $primaryExpression CLASS ) | VOID DOT CLASS -> ^( DOT VOID CLASS ) );
    def primaryExpression(self, ):

        retval = self.primaryExpression_return()
        retval.start = self.input.LT(1)
        primaryExpression_StartIndex = self.input.index()
        root_0 = None

        SUPER466 = None
        DOT468 = None
        IDENT469 = None
        IDENT471 = None
        THIS473 = None
        THIS475 = None
        SUPER477 = None
        SUPER479 = None
        DOT480 = None
        IDENT481 = None
        DOT485 = None
        CLASS486 = None
        VOID487 = None
        DOT488 = None
        CLASS489 = None
        parenthesizedExpression461 = None

        literal462 = None

        newExpression463 = None

        qualifiedIdentExpression464 = None

        genericTypeArgumentListSimplified465 = None

        arguments467 = None

        arguments470 = None

        arguments472 = None

        arguments474 = None

        arguments476 = None

        arguments478 = None

        arguments482 = None

        primitiveType483 = None

        arrayDeclarator484 = None


        SUPER466_tree = None
        DOT468_tree = None
        IDENT469_tree = None
        IDENT471_tree = None
        THIS473_tree = None
        THIS475_tree = None
        SUPER477_tree = None
        SUPER479_tree = None
        DOT480_tree = None
        IDENT481_tree = None
        DOT485_tree = None
        CLASS486_tree = None
        VOID487_tree = None
        DOT488_tree = None
        CLASS489_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_CLASS = RewriteRuleTokenStream(self._adaptor, "token CLASS")
        stream_VOID = RewriteRuleTokenStream(self._adaptor, "token VOID")
        stream_SUPER = RewriteRuleTokenStream(self._adaptor, "token SUPER")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_THIS = RewriteRuleTokenStream(self._adaptor, "token THIS")
        stream_arrayDeclarator = RewriteRuleSubtreeStream(self._adaptor, "rule arrayDeclarator")
        stream_arguments = RewriteRuleSubtreeStream(self._adaptor, "rule arguments")
        stream_primitiveType = RewriteRuleSubtreeStream(self._adaptor, "rule primitiveType")
        stream_genericTypeArgumentListSimplified = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeArgumentListSimplified")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 105):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:926:5: ( parenthesizedExpression | literal | newExpression | qualifiedIdentExpression | genericTypeArgumentListSimplified ( SUPER ( arguments -> ^( SUPER_CONSTRUCTOR_CALL[$SUPER, \"SUPER_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments ) | DOT IDENT arguments -> ^( METHOD_CALL ^( DOT SUPER IDENT ) genericTypeArgumentListSimplified arguments ) ) | IDENT arguments -> ^( METHOD_CALL IDENT genericTypeArgumentListSimplified arguments ) | THIS arguments -> ^( THIS_CONSTRUCTOR_CALL[$THIS, \"THIS_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments ) ) | ( THIS -> THIS ) ( arguments -> ^( THIS_CONSTRUCTOR_CALL[$THIS, \"THIS_CONSTRUCTOR_CALL\"] arguments ) )? | SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$SUPER, \"SUPER_CONSTRUCTOR_CALL\"] arguments ) | ( SUPER DOT IDENT ) ( arguments -> ^( METHOD_CALL ^( DOT SUPER IDENT ) arguments ) | -> ^( DOT SUPER IDENT ) ) | ( primitiveType -> primitiveType ) ( arrayDeclarator -> ^( arrayDeclarator $primaryExpression) )* DOT CLASS -> ^( DOT $primaryExpression CLASS ) | VOID DOT CLASS -> ^( DOT VOID CLASS ) )
                alt139 = 10
                alt139 = self.dfa139.predict(self.input)
                if alt139 == 1:
                    # Java.g:926:9: parenthesizedExpression
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_primaryExpression12328)
                    parenthesizedExpression461 = self.parenthesizedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, parenthesizedExpression461.tree)


                elif alt139 == 2:
                    # Java.g:927:9: literal
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_literal_in_primaryExpression12338)
                    literal462 = self.literal()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, literal462.tree)


                elif alt139 == 3:
                    # Java.g:928:9: newExpression
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_newExpression_in_primaryExpression12348)
                    newExpression463 = self.newExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, newExpression463.tree)


                elif alt139 == 4:
                    # Java.g:929:9: qualifiedIdentExpression
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_qualifiedIdentExpression_in_primaryExpression12358)
                    qualifiedIdentExpression464 = self.qualifiedIdentExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, qualifiedIdentExpression464.tree)


                elif alt139 == 5:
                    # Java.g:930:9: genericTypeArgumentListSimplified ( SUPER ( arguments -> ^( SUPER_CONSTRUCTOR_CALL[$SUPER, \"SUPER_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments ) | DOT IDENT arguments -> ^( METHOD_CALL ^( DOT SUPER IDENT ) genericTypeArgumentListSimplified arguments ) ) | IDENT arguments -> ^( METHOD_CALL IDENT genericTypeArgumentListSimplified arguments ) | THIS arguments -> ^( THIS_CONSTRUCTOR_CALL[$THIS, \"THIS_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments ) )
                    pass 
                    self._state.following.append(self.FOLLOW_genericTypeArgumentListSimplified_in_primaryExpression12368)
                    genericTypeArgumentListSimplified465 = self.genericTypeArgumentListSimplified()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_genericTypeArgumentListSimplified.add(genericTypeArgumentListSimplified465.tree)
                    # Java.g:931:9: ( SUPER ( arguments -> ^( SUPER_CONSTRUCTOR_CALL[$SUPER, \"SUPER_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments ) | DOT IDENT arguments -> ^( METHOD_CALL ^( DOT SUPER IDENT ) genericTypeArgumentListSimplified arguments ) ) | IDENT arguments -> ^( METHOD_CALL IDENT genericTypeArgumentListSimplified arguments ) | THIS arguments -> ^( THIS_CONSTRUCTOR_CALL[$THIS, \"THIS_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments ) )
                    alt135 = 3
                    LA135 = self.input.LA(1)
                    if LA135 == SUPER:
                        alt135 = 1
                    elif LA135 == IDENT:
                        alt135 = 2
                    elif LA135 == THIS:
                        alt135 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 135, 0, self.input)

                        raise nvae

                    if alt135 == 1:
                        # Java.g:931:13: SUPER ( arguments -> ^( SUPER_CONSTRUCTOR_CALL[$SUPER, \"SUPER_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments ) | DOT IDENT arguments -> ^( METHOD_CALL ^( DOT SUPER IDENT ) genericTypeArgumentListSimplified arguments ) )
                        pass 
                        SUPER466=self.match(self.input, SUPER, self.FOLLOW_SUPER_in_primaryExpression12382) 
                        if self._state.backtracking == 0:
                            stream_SUPER.add(SUPER466)
                        # Java.g:932:13: ( arguments -> ^( SUPER_CONSTRUCTOR_CALL[$SUPER, \"SUPER_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments ) | DOT IDENT arguments -> ^( METHOD_CALL ^( DOT SUPER IDENT ) genericTypeArgumentListSimplified arguments ) )
                        alt134 = 2
                        LA134_0 = self.input.LA(1)

                        if (LA134_0 == LPAREN) :
                            alt134 = 1
                        elif (LA134_0 == DOT) :
                            alt134 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 134, 0, self.input)

                            raise nvae

                        if alt134 == 1:
                            # Java.g:932:17: arguments
                            pass 
                            self._state.following.append(self.FOLLOW_arguments_in_primaryExpression12400)
                            arguments467 = self.arguments()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_arguments.add(arguments467.tree)

                            # AST Rewrite
                            # elements: genericTypeArgumentListSimplified, arguments
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            if self._state.backtracking == 0:

                                retval.tree = root_0

                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 932:57: -> ^( SUPER_CONSTRUCTOR_CALL[$SUPER, \"SUPER_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments )
                                # Java.g:932:61: ^( SUPER_CONSTRUCTOR_CALL[$SUPER, \"SUPER_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(self._adaptor.create(SUPER_CONSTRUCTOR_CALL, SUPER466, "SUPER_CONSTRUCTOR_CALL"), root_1)

                                self._adaptor.addChild(root_1, stream_genericTypeArgumentListSimplified.nextTree())
                                self._adaptor.addChild(root_1, stream_arguments.nextTree())

                                self._adaptor.addChild(root_0, root_1)



                                retval.tree = root_0


                        elif alt134 == 2:
                            # Java.g:933:17: DOT IDENT arguments
                            pass 
                            DOT468=self.match(self.input, DOT, self.FOLLOW_DOT_in_primaryExpression12460) 
                            if self._state.backtracking == 0:
                                stream_DOT.add(DOT468)
                            IDENT469=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_primaryExpression12462) 
                            if self._state.backtracking == 0:
                                stream_IDENT.add(IDENT469)
                            self._state.following.append(self.FOLLOW_arguments_in_primaryExpression12464)
                            arguments470 = self.arguments()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_arguments.add(arguments470.tree)

                            # AST Rewrite
                            # elements: SUPER, IDENT, arguments, genericTypeArgumentListSimplified, DOT
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            if self._state.backtracking == 0:

                                retval.tree = root_0

                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 933:57: -> ^( METHOD_CALL ^( DOT SUPER IDENT ) genericTypeArgumentListSimplified arguments )
                                # Java.g:933:61: ^( METHOD_CALL ^( DOT SUPER IDENT ) genericTypeArgumentListSimplified arguments )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(METHOD_CALL, "METHOD_CALL"), root_1)

                                # Java.g:933:75: ^( DOT SUPER IDENT )
                                root_2 = self._adaptor.nil()
                                root_2 = self._adaptor.becomeRoot(stream_DOT.nextNode(), root_2)

                                self._adaptor.addChild(root_2, stream_SUPER.nextNode())
                                self._adaptor.addChild(root_2, stream_IDENT.nextNode())

                                self._adaptor.addChild(root_1, root_2)
                                self._adaptor.addChild(root_1, stream_genericTypeArgumentListSimplified.nextTree())
                                self._adaptor.addChild(root_1, stream_arguments.nextTree())

                                self._adaptor.addChild(root_0, root_1)



                                retval.tree = root_0





                    elif alt135 == 2:
                        # Java.g:935:13: IDENT arguments
                        pass 
                        IDENT471=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_primaryExpression12531) 
                        if self._state.backtracking == 0:
                            stream_IDENT.add(IDENT471)
                        self._state.following.append(self.FOLLOW_arguments_in_primaryExpression12533)
                        arguments472 = self.arguments()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_arguments.add(arguments472.tree)

                        # AST Rewrite
                        # elements: arguments, IDENT, genericTypeArgumentListSimplified
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 935:57: -> ^( METHOD_CALL IDENT genericTypeArgumentListSimplified arguments )
                            # Java.g:935:61: ^( METHOD_CALL IDENT genericTypeArgumentListSimplified arguments )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(METHOD_CALL, "METHOD_CALL"), root_1)

                            self._adaptor.addChild(root_1, stream_IDENT.nextNode())
                            self._adaptor.addChild(root_1, stream_genericTypeArgumentListSimplified.nextTree())
                            self._adaptor.addChild(root_1, stream_arguments.nextTree())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt135 == 3:
                        # Java.g:936:13: THIS arguments
                        pass 
                        THIS473=self.match(self.input, THIS, self.FOLLOW_THIS_in_primaryExpression12588) 
                        if self._state.backtracking == 0:
                            stream_THIS.add(THIS473)
                        self._state.following.append(self.FOLLOW_arguments_in_primaryExpression12590)
                        arguments474 = self.arguments()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_arguments.add(arguments474.tree)

                        # AST Rewrite
                        # elements: arguments, genericTypeArgumentListSimplified
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 936:57: -> ^( THIS_CONSTRUCTOR_CALL[$THIS, \"THIS_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments )
                            # Java.g:936:61: ^( THIS_CONSTRUCTOR_CALL[$THIS, \"THIS_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.create(THIS_CONSTRUCTOR_CALL, THIS473, "THIS_CONSTRUCTOR_CALL"), root_1)

                            self._adaptor.addChild(root_1, stream_genericTypeArgumentListSimplified.nextTree())
                            self._adaptor.addChild(root_1, stream_arguments.nextTree())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0





                elif alt139 == 6:
                    # Java.g:938:9: ( THIS -> THIS ) ( arguments -> ^( THIS_CONSTRUCTOR_CALL[$THIS, \"THIS_CONSTRUCTOR_CALL\"] arguments ) )?
                    pass 
                    # Java.g:938:9: ( THIS -> THIS )
                    # Java.g:938:13: THIS
                    pass 
                    THIS475=self.match(self.input, THIS, self.FOLLOW_THIS_in_primaryExpression12655) 
                    if self._state.backtracking == 0:
                        stream_THIS.add(THIS475)

                    # AST Rewrite
                    # elements: THIS
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 938:57: -> THIS
                        self._adaptor.addChild(root_0, stream_THIS.nextNode())



                        retval.tree = root_0



                    # Java.g:940:9: ( arguments -> ^( THIS_CONSTRUCTOR_CALL[$THIS, \"THIS_CONSTRUCTOR_CALL\"] arguments ) )?
                    alt136 = 2
                    LA136_0 = self.input.LA(1)

                    if (LA136_0 == LPAREN) :
                        alt136 = 1
                    if alt136 == 1:
                        # Java.g:940:13: arguments
                        pass 
                        self._state.following.append(self.FOLLOW_arguments_in_primaryExpression12723)
                        arguments476 = self.arguments()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_arguments.add(arguments476.tree)

                        # AST Rewrite
                        # elements: arguments
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 940:57: -> ^( THIS_CONSTRUCTOR_CALL[$THIS, \"THIS_CONSTRUCTOR_CALL\"] arguments )
                            # Java.g:940:61: ^( THIS_CONSTRUCTOR_CALL[$THIS, \"THIS_CONSTRUCTOR_CALL\"] arguments )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.create(THIS_CONSTRUCTOR_CALL, THIS475, "THIS_CONSTRUCTOR_CALL"), root_1)

                            self._adaptor.addChild(root_1, stream_arguments.nextTree())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0





                elif alt139 == 7:
                    # Java.g:942:9: SUPER arguments
                    pass 
                    SUPER477=self.match(self.input, SUPER, self.FOLLOW_SUPER_in_primaryExpression12788) 
                    if self._state.backtracking == 0:
                        stream_SUPER.add(SUPER477)
                    self._state.following.append(self.FOLLOW_arguments_in_primaryExpression12790)
                    arguments478 = self.arguments()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_arguments.add(arguments478.tree)

                    # AST Rewrite
                    # elements: arguments
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 942:57: -> ^( SUPER_CONSTRUCTOR_CALL[$SUPER, \"SUPER_CONSTRUCTOR_CALL\"] arguments )
                        # Java.g:942:61: ^( SUPER_CONSTRUCTOR_CALL[$SUPER, \"SUPER_CONSTRUCTOR_CALL\"] arguments )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.create(SUPER_CONSTRUCTOR_CALL, SUPER477, "SUPER_CONSTRUCTOR_CALL"), root_1)

                        self._adaptor.addChild(root_1, stream_arguments.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt139 == 8:
                    # Java.g:943:9: ( SUPER DOT IDENT ) ( arguments -> ^( METHOD_CALL ^( DOT SUPER IDENT ) arguments ) | -> ^( DOT SUPER IDENT ) )
                    pass 
                    # Java.g:943:9: ( SUPER DOT IDENT )
                    # Java.g:943:13: SUPER DOT IDENT
                    pass 
                    SUPER479=self.match(self.input, SUPER, self.FOLLOW_SUPER_in_primaryExpression12846) 
                    if self._state.backtracking == 0:
                        stream_SUPER.add(SUPER479)
                    DOT480=self.match(self.input, DOT, self.FOLLOW_DOT_in_primaryExpression12848) 
                    if self._state.backtracking == 0:
                        stream_DOT.add(DOT480)
                    IDENT481=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_primaryExpression12850) 
                    if self._state.backtracking == 0:
                        stream_IDENT.add(IDENT481)



                    # Java.g:945:9: ( arguments -> ^( METHOD_CALL ^( DOT SUPER IDENT ) arguments ) | -> ^( DOT SUPER IDENT ) )
                    alt137 = 2
                    LA137_0 = self.input.LA(1)

                    if (LA137_0 == LPAREN) :
                        alt137 = 1
                    elif (LA137_0 == EOF or (AND <= LA137_0 <= ASSIGN) or (BIT_SHIFT_RIGHT <= LA137_0 <= DOT) or (EQUAL <= LA137_0 <= LBRACK) or (LESS_OR_EQUAL <= LA137_0 <= LOGICAL_AND) or LA137_0 == LOGICAL_OR or (MINUS <= LA137_0 <= MOD_ASSIGN) or (NOT_EQUAL <= LA137_0 <= XOR_ASSIGN) or LA137_0 == INSTANCEOF) :
                        alt137 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 137, 0, self.input)

                        raise nvae

                    if alt137 == 1:
                        # Java.g:945:13: arguments
                        pass 
                        self._state.following.append(self.FOLLOW_arguments_in_primaryExpression12874)
                        arguments482 = self.arguments()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_arguments.add(arguments482.tree)

                        # AST Rewrite
                        # elements: arguments, DOT, SUPER, IDENT
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 945:57: -> ^( METHOD_CALL ^( DOT SUPER IDENT ) arguments )
                            # Java.g:945:61: ^( METHOD_CALL ^( DOT SUPER IDENT ) arguments )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(METHOD_CALL, "METHOD_CALL"), root_1)

                            # Java.g:945:75: ^( DOT SUPER IDENT )
                            root_2 = self._adaptor.nil()
                            root_2 = self._adaptor.becomeRoot(stream_DOT.nextNode(), root_2)

                            self._adaptor.addChild(root_2, stream_SUPER.nextNode())
                            self._adaptor.addChild(root_2, stream_IDENT.nextNode())

                            self._adaptor.addChild(root_1, root_2)
                            self._adaptor.addChild(root_1, stream_arguments.nextTree())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt137 == 2:
                        # Java.g:946:57: 
                        pass 
                        # AST Rewrite
                        # elements: SUPER, DOT, IDENT
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 946:57: -> ^( DOT SUPER IDENT )
                            # Java.g:946:61: ^( DOT SUPER IDENT )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(stream_DOT.nextNode(), root_1)

                            self._adaptor.addChild(root_1, stream_SUPER.nextNode())
                            self._adaptor.addChild(root_1, stream_IDENT.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0





                elif alt139 == 9:
                    # Java.g:948:9: ( primitiveType -> primitiveType ) ( arrayDeclarator -> ^( arrayDeclarator $primaryExpression) )* DOT CLASS
                    pass 
                    # Java.g:948:9: ( primitiveType -> primitiveType )
                    # Java.g:948:13: primitiveType
                    pass 
                    self._state.following.append(self.FOLLOW_primitiveType_in_primaryExpression13016)
                    primitiveType483 = self.primitiveType()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_primitiveType.add(primitiveType483.tree)

                    # AST Rewrite
                    # elements: primitiveType
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 948:57: -> primitiveType
                        self._adaptor.addChild(root_0, stream_primitiveType.nextTree())



                        retval.tree = root_0



                    # Java.g:950:9: ( arrayDeclarator -> ^( arrayDeclarator $primaryExpression) )*
                    while True: #loop138
                        alt138 = 2
                        LA138_0 = self.input.LA(1)

                        if (LA138_0 == LBRACK) :
                            alt138 = 1


                        if alt138 == 1:
                            # Java.g:950:13: arrayDeclarator
                            pass 
                            self._state.following.append(self.FOLLOW_arrayDeclarator_in_primaryExpression13075)
                            arrayDeclarator484 = self.arrayDeclarator()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_arrayDeclarator.add(arrayDeclarator484.tree)

                            # AST Rewrite
                            # elements: arrayDeclarator, primaryExpression
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            if self._state.backtracking == 0:

                                retval.tree = root_0

                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 950:57: -> ^( arrayDeclarator $primaryExpression)
                                # Java.g:950:61: ^( arrayDeclarator $primaryExpression)
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(stream_arrayDeclarator.nextNode(), root_1)

                                self._adaptor.addChild(root_1, stream_retval.nextTree())

                                self._adaptor.addChild(root_0, root_1)



                                retval.tree = root_0


                        else:
                            break #loop138


                    DOT485=self.match(self.input, DOT, self.FOLLOW_DOT_in_primaryExpression13134) 
                    if self._state.backtracking == 0:
                        stream_DOT.add(DOT485)
                    CLASS486=self.match(self.input, CLASS, self.FOLLOW_CLASS_in_primaryExpression13136) 
                    if self._state.backtracking == 0:
                        stream_CLASS.add(CLASS486)

                    # AST Rewrite
                    # elements: DOT, CLASS, primaryExpression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 952:57: -> ^( DOT $primaryExpression CLASS )
                        # Java.g:952:61: ^( DOT $primaryExpression CLASS )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_DOT.nextNode(), root_1)

                        self._adaptor.addChild(root_1, stream_retval.nextTree())
                        self._adaptor.addChild(root_1, stream_CLASS.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt139 == 10:
                    # Java.g:953:9: VOID DOT CLASS
                    pass 
                    VOID487=self.match(self.input, VOID, self.FOLLOW_VOID_in_primaryExpression13196) 
                    if self._state.backtracking == 0:
                        stream_VOID.add(VOID487)
                    DOT488=self.match(self.input, DOT, self.FOLLOW_DOT_in_primaryExpression13198) 
                    if self._state.backtracking == 0:
                        stream_DOT.add(DOT488)
                    CLASS489=self.match(self.input, CLASS, self.FOLLOW_CLASS_in_primaryExpression13200) 
                    if self._state.backtracking == 0:
                        stream_CLASS.add(CLASS489)

                    # AST Rewrite
                    # elements: DOT, CLASS, VOID
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 953:57: -> ^( DOT VOID CLASS )
                        # Java.g:953:61: ^( DOT VOID CLASS )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_DOT.nextNode(), root_1)

                        self._adaptor.addChild(root_1, stream_VOID.nextNode())
                        self._adaptor.addChild(root_1, stream_CLASS.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 105, primaryExpression_StartIndex, success)

            pass

        return retval

    # $ANTLR end "primaryExpression"

    class qualifiedIdentExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "qualifiedIdentExpression"
    # Java.g:956:1: qualifiedIdentExpression : ( qualifiedIdentifier -> qualifiedIdentifier ) ( ( arrayDeclarator -> ^( arrayDeclarator $qualifiedIdentExpression) )+ ( DOT CLASS -> ^( DOT $qualifiedIdentExpression CLASS ) ) | arguments -> ^( METHOD_CALL qualifiedIdentifier arguments ) | outerDot= DOT ( CLASS -> ^( DOT qualifiedIdentifier CLASS ) | genericTypeArgumentListSimplified (Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier genericTypeArgumentListSimplified arguments ) | SUPER innerDot= DOT IDENT arguments -> ^( METHOD_CALL ^( $innerDot ^( $outerDot qualifiedIdentifier SUPER ) IDENT ) genericTypeArgumentListSimplified arguments ) | IDENT arguments -> ^( METHOD_CALL ^( DOT qualifiedIdentifier IDENT ) genericTypeArgumentListSimplified arguments ) ) | THIS -> ^( DOT qualifiedIdentifier THIS ) | Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier arguments ) | innerNewExpression -> ^( DOT qualifiedIdentifier innerNewExpression ) ) )? ;
    def qualifiedIdentExpression(self, ):

        retval = self.qualifiedIdentExpression_return()
        retval.start = self.input.LT(1)
        qualifiedIdentExpression_StartIndex = self.input.index()
        root_0 = None

        outerDot = None
        Super = None
        innerDot = None
        DOT492 = None
        CLASS493 = None
        CLASS495 = None
        SUPER498 = None
        IDENT499 = None
        IDENT501 = None
        THIS503 = None
        qualifiedIdentifier490 = None

        arrayDeclarator491 = None

        arguments494 = None

        genericTypeArgumentListSimplified496 = None

        arguments497 = None

        arguments500 = None

        arguments502 = None

        arguments504 = None

        innerNewExpression505 = None


        outerDot_tree = None
        Super_tree = None
        innerDot_tree = None
        DOT492_tree = None
        CLASS493_tree = None
        CLASS495_tree = None
        SUPER498_tree = None
        IDENT499_tree = None
        IDENT501_tree = None
        THIS503_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_CLASS = RewriteRuleTokenStream(self._adaptor, "token CLASS")
        stream_SUPER = RewriteRuleTokenStream(self._adaptor, "token SUPER")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_THIS = RewriteRuleTokenStream(self._adaptor, "token THIS")
        stream_arrayDeclarator = RewriteRuleSubtreeStream(self._adaptor, "rule arrayDeclarator")
        stream_arguments = RewriteRuleSubtreeStream(self._adaptor, "rule arguments")
        stream_qualifiedIdentifier = RewriteRuleSubtreeStream(self._adaptor, "rule qualifiedIdentifier")
        stream_genericTypeArgumentListSimplified = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeArgumentListSimplified")
        stream_innerNewExpression = RewriteRuleSubtreeStream(self._adaptor, "rule innerNewExpression")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 106):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:958:5: ( ( qualifiedIdentifier -> qualifiedIdentifier ) ( ( arrayDeclarator -> ^( arrayDeclarator $qualifiedIdentExpression) )+ ( DOT CLASS -> ^( DOT $qualifiedIdentExpression CLASS ) ) | arguments -> ^( METHOD_CALL qualifiedIdentifier arguments ) | outerDot= DOT ( CLASS -> ^( DOT qualifiedIdentifier CLASS ) | genericTypeArgumentListSimplified (Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier genericTypeArgumentListSimplified arguments ) | SUPER innerDot= DOT IDENT arguments -> ^( METHOD_CALL ^( $innerDot ^( $outerDot qualifiedIdentifier SUPER ) IDENT ) genericTypeArgumentListSimplified arguments ) | IDENT arguments -> ^( METHOD_CALL ^( DOT qualifiedIdentifier IDENT ) genericTypeArgumentListSimplified arguments ) ) | THIS -> ^( DOT qualifiedIdentifier THIS ) | Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier arguments ) | innerNewExpression -> ^( DOT qualifiedIdentifier innerNewExpression ) ) )? )
                # Java.g:958:9: ( qualifiedIdentifier -> qualifiedIdentifier ) ( ( arrayDeclarator -> ^( arrayDeclarator $qualifiedIdentExpression) )+ ( DOT CLASS -> ^( DOT $qualifiedIdentExpression CLASS ) ) | arguments -> ^( METHOD_CALL qualifiedIdentifier arguments ) | outerDot= DOT ( CLASS -> ^( DOT qualifiedIdentifier CLASS ) | genericTypeArgumentListSimplified (Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier genericTypeArgumentListSimplified arguments ) | SUPER innerDot= DOT IDENT arguments -> ^( METHOD_CALL ^( $innerDot ^( $outerDot qualifiedIdentifier SUPER ) IDENT ) genericTypeArgumentListSimplified arguments ) | IDENT arguments -> ^( METHOD_CALL ^( DOT qualifiedIdentifier IDENT ) genericTypeArgumentListSimplified arguments ) ) | THIS -> ^( DOT qualifiedIdentifier THIS ) | Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier arguments ) | innerNewExpression -> ^( DOT qualifiedIdentifier innerNewExpression ) ) )?
                pass 
                # Java.g:958:9: ( qualifiedIdentifier -> qualifiedIdentifier )
                # Java.g:958:13: qualifiedIdentifier
                pass 
                self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_qualifiedIdentExpression13276)
                qualifiedIdentifier490 = self.qualifiedIdentifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_qualifiedIdentifier.add(qualifiedIdentifier490.tree)

                # AST Rewrite
                # elements: qualifiedIdentifier
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 958:61: -> qualifiedIdentifier
                    self._adaptor.addChild(root_0, stream_qualifiedIdentifier.nextTree())



                    retval.tree = root_0



                # Java.g:961:9: ( ( arrayDeclarator -> ^( arrayDeclarator $qualifiedIdentExpression) )+ ( DOT CLASS -> ^( DOT $qualifiedIdentExpression CLASS ) ) | arguments -> ^( METHOD_CALL qualifiedIdentifier arguments ) | outerDot= DOT ( CLASS -> ^( DOT qualifiedIdentifier CLASS ) | genericTypeArgumentListSimplified (Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier genericTypeArgumentListSimplified arguments ) | SUPER innerDot= DOT IDENT arguments -> ^( METHOD_CALL ^( $innerDot ^( $outerDot qualifiedIdentifier SUPER ) IDENT ) genericTypeArgumentListSimplified arguments ) | IDENT arguments -> ^( METHOD_CALL ^( DOT qualifiedIdentifier IDENT ) genericTypeArgumentListSimplified arguments ) ) | THIS -> ^( DOT qualifiedIdentifier THIS ) | Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier arguments ) | innerNewExpression -> ^( DOT qualifiedIdentifier innerNewExpression ) ) )?
                alt143 = 4
                alt143 = self.dfa143.predict(self.input)
                if alt143 == 1:
                    # Java.g:961:13: ( arrayDeclarator -> ^( arrayDeclarator $qualifiedIdentExpression) )+ ( DOT CLASS -> ^( DOT $qualifiedIdentExpression CLASS ) )
                    pass 
                    # Java.g:961:13: ( arrayDeclarator -> ^( arrayDeclarator $qualifiedIdentExpression) )+
                    cnt140 = 0
                    while True: #loop140
                        alt140 = 2
                        LA140_0 = self.input.LA(1)

                        if (LA140_0 == LBRACK) :
                            alt140 = 1


                        if alt140 == 1:
                            # Java.g:961:17: arrayDeclarator
                            pass 
                            self._state.following.append(self.FOLLOW_arrayDeclarator_in_qualifiedIdentExpression13346)
                            arrayDeclarator491 = self.arrayDeclarator()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_arrayDeclarator.add(arrayDeclarator491.tree)

                            # AST Rewrite
                            # elements: arrayDeclarator, qualifiedIdentExpression
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            if self._state.backtracking == 0:

                                retval.tree = root_0

                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 961:57: -> ^( arrayDeclarator $qualifiedIdentExpression)
                                # Java.g:961:61: ^( arrayDeclarator $qualifiedIdentExpression)
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(stream_arrayDeclarator.nextNode(), root_1)

                                self._adaptor.addChild(root_1, stream_retval.nextTree())

                                self._adaptor.addChild(root_0, root_1)



                                retval.tree = root_0


                        else:
                            if cnt140 >= 1:
                                break #loop140

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(140, self.input)
                            raise eee

                        cnt140 += 1


                    # Java.g:963:13: ( DOT CLASS -> ^( DOT $qualifiedIdentExpression CLASS ) )
                    # Java.g:963:17: DOT CLASS
                    pass 
                    DOT492=self.match(self.input, DOT, self.FOLLOW_DOT_in_qualifiedIdentExpression13413) 
                    if self._state.backtracking == 0:
                        stream_DOT.add(DOT492)
                    CLASS493=self.match(self.input, CLASS, self.FOLLOW_CLASS_in_qualifiedIdentExpression13415) 
                    if self._state.backtracking == 0:
                        stream_CLASS.add(CLASS493)

                    # AST Rewrite
                    # elements: qualifiedIdentExpression, DOT, CLASS
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 963:57: -> ^( DOT $qualifiedIdentExpression CLASS )
                        # Java.g:963:61: ^( DOT $qualifiedIdentExpression CLASS )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_DOT.nextNode(), root_1)

                        self._adaptor.addChild(root_1, stream_retval.nextTree())
                        self._adaptor.addChild(root_1, stream_CLASS.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0





                elif alt143 == 2:
                    # Java.g:965:13: arguments
                    pass 
                    self._state.following.append(self.FOLLOW_arguments_in_qualifiedIdentExpression13485)
                    arguments494 = self.arguments()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_arguments.add(arguments494.tree)

                    # AST Rewrite
                    # elements: qualifiedIdentifier, arguments
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 965:57: -> ^( METHOD_CALL qualifiedIdentifier arguments )
                        # Java.g:965:61: ^( METHOD_CALL qualifiedIdentifier arguments )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(METHOD_CALL, "METHOD_CALL"), root_1)

                        self._adaptor.addChild(root_1, stream_qualifiedIdentifier.nextTree())
                        self._adaptor.addChild(root_1, stream_arguments.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt143 == 3:
                    # Java.g:966:13: outerDot= DOT ( CLASS -> ^( DOT qualifiedIdentifier CLASS ) | genericTypeArgumentListSimplified (Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier genericTypeArgumentListSimplified arguments ) | SUPER innerDot= DOT IDENT arguments -> ^( METHOD_CALL ^( $innerDot ^( $outerDot qualifiedIdentifier SUPER ) IDENT ) genericTypeArgumentListSimplified arguments ) | IDENT arguments -> ^( METHOD_CALL ^( DOT qualifiedIdentifier IDENT ) genericTypeArgumentListSimplified arguments ) ) | THIS -> ^( DOT qualifiedIdentifier THIS ) | Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier arguments ) | innerNewExpression -> ^( DOT qualifiedIdentifier innerNewExpression ) )
                    pass 
                    outerDot=self.match(self.input, DOT, self.FOLLOW_DOT_in_qualifiedIdentExpression13546) 
                    if self._state.backtracking == 0:
                        stream_DOT.add(outerDot)
                    # Java.g:967:13: ( CLASS -> ^( DOT qualifiedIdentifier CLASS ) | genericTypeArgumentListSimplified (Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier genericTypeArgumentListSimplified arguments ) | SUPER innerDot= DOT IDENT arguments -> ^( METHOD_CALL ^( $innerDot ^( $outerDot qualifiedIdentifier SUPER ) IDENT ) genericTypeArgumentListSimplified arguments ) | IDENT arguments -> ^( METHOD_CALL ^( DOT qualifiedIdentifier IDENT ) genericTypeArgumentListSimplified arguments ) ) | THIS -> ^( DOT qualifiedIdentifier THIS ) | Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier arguments ) | innerNewExpression -> ^( DOT qualifiedIdentifier innerNewExpression ) )
                    alt142 = 5
                    LA142 = self.input.LA(1)
                    if LA142 == CLASS:
                        alt142 = 1
                    elif LA142 == LESS_THAN:
                        alt142 = 2
                    elif LA142 == THIS:
                        alt142 = 3
                    elif LA142 == SUPER:
                        alt142 = 4
                    elif LA142 == NEW:
                        alt142 = 5
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 142, 0, self.input)

                        raise nvae

                    if alt142 == 1:
                        # Java.g:967:17: CLASS
                        pass 
                        CLASS495=self.match(self.input, CLASS, self.FOLLOW_CLASS_in_qualifiedIdentExpression13564) 
                        if self._state.backtracking == 0:
                            stream_CLASS.add(CLASS495)

                        # AST Rewrite
                        # elements: CLASS, qualifiedIdentifier, DOT
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 967:57: -> ^( DOT qualifiedIdentifier CLASS )
                            # Java.g:967:61: ^( DOT qualifiedIdentifier CLASS )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(stream_DOT.nextNode(), root_1)

                            self._adaptor.addChild(root_1, stream_qualifiedIdentifier.nextTree())
                            self._adaptor.addChild(root_1, stream_CLASS.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt142 == 2:
                        # Java.g:968:17: genericTypeArgumentListSimplified (Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier genericTypeArgumentListSimplified arguments ) | SUPER innerDot= DOT IDENT arguments -> ^( METHOD_CALL ^( $innerDot ^( $outerDot qualifiedIdentifier SUPER ) IDENT ) genericTypeArgumentListSimplified arguments ) | IDENT arguments -> ^( METHOD_CALL ^( DOT qualifiedIdentifier IDENT ) genericTypeArgumentListSimplified arguments ) )
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeArgumentListSimplified_in_qualifiedIdentExpression13627)
                        genericTypeArgumentListSimplified496 = self.genericTypeArgumentListSimplified()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_genericTypeArgumentListSimplified.add(genericTypeArgumentListSimplified496.tree)
                        # Java.g:969:17: (Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier genericTypeArgumentListSimplified arguments ) | SUPER innerDot= DOT IDENT arguments -> ^( METHOD_CALL ^( $innerDot ^( $outerDot qualifiedIdentifier SUPER ) IDENT ) genericTypeArgumentListSimplified arguments ) | IDENT arguments -> ^( METHOD_CALL ^( DOT qualifiedIdentifier IDENT ) genericTypeArgumentListSimplified arguments ) )
                        alt141 = 3
                        LA141_0 = self.input.LA(1)

                        if (LA141_0 == SUPER) :
                            LA141_1 = self.input.LA(2)

                            if (LA141_1 == DOT) :
                                alt141 = 2
                            elif (LA141_1 == LPAREN) :
                                alt141 = 1
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                nvae = NoViableAltException("", 141, 1, self.input)

                                raise nvae

                        elif (LA141_0 == IDENT) :
                            alt141 = 3
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 141, 0, self.input)

                            raise nvae

                        if alt141 == 1:
                            # Java.g:969:21: Super= SUPER arguments
                            pass 
                            Super=self.match(self.input, SUPER, self.FOLLOW_SUPER_in_qualifiedIdentExpression13651) 
                            if self._state.backtracking == 0:
                                stream_SUPER.add(Super)
                            self._state.following.append(self.FOLLOW_arguments_in_qualifiedIdentExpression13653)
                            arguments497 = self.arguments()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_arguments.add(arguments497.tree)

                            # AST Rewrite
                            # elements: qualifiedIdentifier, arguments, genericTypeArgumentListSimplified
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            if self._state.backtracking == 0:

                                retval.tree = root_0

                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 969:57: -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier genericTypeArgumentListSimplified arguments )
                                # Java.g:969:61: ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier genericTypeArgumentListSimplified arguments )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(self._adaptor.create(SUPER_CONSTRUCTOR_CALL, Super, "SUPER_CONSTRUCTOR_CALL"), root_1)

                                self._adaptor.addChild(root_1, stream_qualifiedIdentifier.nextTree())
                                self._adaptor.addChild(root_1, stream_genericTypeArgumentListSimplified.nextTree())
                                self._adaptor.addChild(root_1, stream_arguments.nextTree())

                                self._adaptor.addChild(root_0, root_1)



                                retval.tree = root_0


                        elif alt141 == 2:
                            # Java.g:970:21: SUPER innerDot= DOT IDENT arguments
                            pass 
                            SUPER498=self.match(self.input, SUPER, self.FOLLOW_SUPER_in_qualifiedIdentExpression13703) 
                            if self._state.backtracking == 0:
                                stream_SUPER.add(SUPER498)
                            innerDot=self.match(self.input, DOT, self.FOLLOW_DOT_in_qualifiedIdentExpression13707) 
                            if self._state.backtracking == 0:
                                stream_DOT.add(innerDot)
                            IDENT499=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_qualifiedIdentExpression13709) 
                            if self._state.backtracking == 0:
                                stream_IDENT.add(IDENT499)
                            self._state.following.append(self.FOLLOW_arguments_in_qualifiedIdentExpression13711)
                            arguments500 = self.arguments()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_arguments.add(arguments500.tree)

                            # AST Rewrite
                            # elements: qualifiedIdentifier, outerDot, arguments, IDENT, genericTypeArgumentListSimplified, SUPER, innerDot
                            # token labels: outerDot, innerDot
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            if self._state.backtracking == 0:

                                retval.tree = root_0
                                stream_outerDot = RewriteRuleTokenStream(self._adaptor, "token outerDot", outerDot)
                                stream_innerDot = RewriteRuleTokenStream(self._adaptor, "token innerDot", innerDot)

                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 970:57: -> ^( METHOD_CALL ^( $innerDot ^( $outerDot qualifiedIdentifier SUPER ) IDENT ) genericTypeArgumentListSimplified arguments )
                                # Java.g:970:61: ^( METHOD_CALL ^( $innerDot ^( $outerDot qualifiedIdentifier SUPER ) IDENT ) genericTypeArgumentListSimplified arguments )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(METHOD_CALL, "METHOD_CALL"), root_1)

                                # Java.g:970:75: ^( $innerDot ^( $outerDot qualifiedIdentifier SUPER ) IDENT )
                                root_2 = self._adaptor.nil()
                                root_2 = self._adaptor.becomeRoot(stream_innerDot.nextNode(), root_2)

                                # Java.g:970:87: ^( $outerDot qualifiedIdentifier SUPER )
                                root_3 = self._adaptor.nil()
                                root_3 = self._adaptor.becomeRoot(stream_outerDot.nextNode(), root_3)

                                self._adaptor.addChild(root_3, stream_qualifiedIdentifier.nextTree())
                                self._adaptor.addChild(root_3, stream_SUPER.nextNode())

                                self._adaptor.addChild(root_2, root_3)
                                self._adaptor.addChild(root_2, stream_IDENT.nextNode())

                                self._adaptor.addChild(root_1, root_2)
                                self._adaptor.addChild(root_1, stream_genericTypeArgumentListSimplified.nextTree())
                                self._adaptor.addChild(root_1, stream_arguments.nextTree())

                                self._adaptor.addChild(root_0, root_1)



                                retval.tree = root_0


                        elif alt141 == 3:
                            # Java.g:971:21: IDENT arguments
                            pass 
                            IDENT501=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_qualifiedIdentExpression13761) 
                            if self._state.backtracking == 0:
                                stream_IDENT.add(IDENT501)
                            self._state.following.append(self.FOLLOW_arguments_in_qualifiedIdentExpression13763)
                            arguments502 = self.arguments()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_arguments.add(arguments502.tree)

                            # AST Rewrite
                            # elements: qualifiedIdentifier, genericTypeArgumentListSimplified, arguments, IDENT, DOT
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            if self._state.backtracking == 0:

                                retval.tree = root_0

                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 971:57: -> ^( METHOD_CALL ^( DOT qualifiedIdentifier IDENT ) genericTypeArgumentListSimplified arguments )
                                # Java.g:971:61: ^( METHOD_CALL ^( DOT qualifiedIdentifier IDENT ) genericTypeArgumentListSimplified arguments )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(METHOD_CALL, "METHOD_CALL"), root_1)

                                # Java.g:971:75: ^( DOT qualifiedIdentifier IDENT )
                                root_2 = self._adaptor.nil()
                                root_2 = self._adaptor.becomeRoot(stream_DOT.nextNode(), root_2)

                                self._adaptor.addChild(root_2, stream_qualifiedIdentifier.nextTree())
                                self._adaptor.addChild(root_2, stream_IDENT.nextNode())

                                self._adaptor.addChild(root_1, root_2)
                                self._adaptor.addChild(root_1, stream_genericTypeArgumentListSimplified.nextTree())
                                self._adaptor.addChild(root_1, stream_arguments.nextTree())

                                self._adaptor.addChild(root_0, root_1)



                                retval.tree = root_0





                    elif alt142 == 3:
                        # Java.g:973:17: THIS
                        pass 
                        THIS503=self.match(self.input, THIS, self.FOLLOW_THIS_in_qualifiedIdentExpression13838) 
                        if self._state.backtracking == 0:
                            stream_THIS.add(THIS503)

                        # AST Rewrite
                        # elements: DOT, qualifiedIdentifier, THIS
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 973:57: -> ^( DOT qualifiedIdentifier THIS )
                            # Java.g:973:61: ^( DOT qualifiedIdentifier THIS )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(stream_DOT.nextNode(), root_1)

                            self._adaptor.addChild(root_1, stream_qualifiedIdentifier.nextTree())
                            self._adaptor.addChild(root_1, stream_THIS.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt142 == 4:
                        # Java.g:974:17: Super= SUPER arguments
                        pass 
                        Super=self.match(self.input, SUPER, self.FOLLOW_SUPER_in_qualifiedIdentExpression13904) 
                        if self._state.backtracking == 0:
                            stream_SUPER.add(Super)
                        self._state.following.append(self.FOLLOW_arguments_in_qualifiedIdentExpression13906)
                        arguments504 = self.arguments()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_arguments.add(arguments504.tree)

                        # AST Rewrite
                        # elements: qualifiedIdentifier, arguments
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 974:57: -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier arguments )
                            # Java.g:974:61: ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier arguments )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.create(SUPER_CONSTRUCTOR_CALL, Super, "SUPER_CONSTRUCTOR_CALL"), root_1)

                            self._adaptor.addChild(root_1, stream_qualifiedIdentifier.nextTree())
                            self._adaptor.addChild(root_1, stream_arguments.nextTree())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt142 == 5:
                        # Java.g:975:17: innerNewExpression
                        pass 
                        self._state.following.append(self.FOLLOW_innerNewExpression_in_qualifiedIdentExpression13954)
                        innerNewExpression505 = self.innerNewExpression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_innerNewExpression.add(innerNewExpression505.tree)

                        # AST Rewrite
                        # elements: innerNewExpression, DOT, qualifiedIdentifier
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 975:57: -> ^( DOT qualifiedIdentifier innerNewExpression )
                            # Java.g:975:61: ^( DOT qualifiedIdentifier innerNewExpression )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(stream_DOT.nextNode(), root_1)

                            self._adaptor.addChild(root_1, stream_qualifiedIdentifier.nextTree())
                            self._adaptor.addChild(root_1, stream_innerNewExpression.nextTree())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0









                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 106, qualifiedIdentExpression_StartIndex, success)

            pass

        return retval

    # $ANTLR end "qualifiedIdentExpression"

    class newExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "newExpression"
    # Java.g:980:1: newExpression : NEW ( primitiveType newArrayConstruction -> ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] primitiveType newArrayConstruction ) | ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified ( newArrayConstruction -> ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified newArrayConstruction ) | arguments ( classBody )? -> ^( CLASS_CONSTRUCTOR_CALL[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified arguments ( classBody )? ) ) ) ;
    def newExpression(self, ):

        retval = self.newExpression_return()
        retval.start = self.input.LT(1)
        newExpression_StartIndex = self.input.index()
        root_0 = None

        NEW506 = None
        primitiveType507 = None

        newArrayConstruction508 = None

        genericTypeArgumentListSimplified509 = None

        qualifiedTypeIdentSimplified510 = None

        newArrayConstruction511 = None

        arguments512 = None

        classBody513 = None


        NEW506_tree = None
        stream_NEW = RewriteRuleTokenStream(self._adaptor, "token NEW")
        stream_newArrayConstruction = RewriteRuleSubtreeStream(self._adaptor, "rule newArrayConstruction")
        stream_arguments = RewriteRuleSubtreeStream(self._adaptor, "rule arguments")
        stream_qualifiedTypeIdentSimplified = RewriteRuleSubtreeStream(self._adaptor, "rule qualifiedTypeIdentSimplified")
        stream_primitiveType = RewriteRuleSubtreeStream(self._adaptor, "rule primitiveType")
        stream_classBody = RewriteRuleSubtreeStream(self._adaptor, "rule classBody")
        stream_genericTypeArgumentListSimplified = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeArgumentListSimplified")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 107):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:981:5: ( NEW ( primitiveType newArrayConstruction -> ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] primitiveType newArrayConstruction ) | ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified ( newArrayConstruction -> ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified newArrayConstruction ) | arguments ( classBody )? -> ^( CLASS_CONSTRUCTOR_CALL[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified arguments ( classBody )? ) ) ) )
                # Java.g:981:9: NEW ( primitiveType newArrayConstruction -> ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] primitiveType newArrayConstruction ) | ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified ( newArrayConstruction -> ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified newArrayConstruction ) | arguments ( classBody )? -> ^( CLASS_CONSTRUCTOR_CALL[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified arguments ( classBody )? ) ) )
                pass 
                NEW506=self.match(self.input, NEW, self.FOLLOW_NEW_in_newExpression14030) 
                if self._state.backtracking == 0:
                    stream_NEW.add(NEW506)
                # Java.g:982:9: ( primitiveType newArrayConstruction -> ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] primitiveType newArrayConstruction ) | ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified ( newArrayConstruction -> ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified newArrayConstruction ) | arguments ( classBody )? -> ^( CLASS_CONSTRUCTOR_CALL[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified arguments ( classBody )? ) ) )
                alt147 = 2
                LA147_0 = self.input.LA(1)

                if (LA147_0 == BOOLEAN or LA147_0 == BYTE or LA147_0 == CHAR or LA147_0 == DOUBLE or LA147_0 == FLOAT or (INT <= LA147_0 <= LONG) or LA147_0 == SHORT) :
                    alt147 = 1
                elif (LA147_0 == LESS_THAN or LA147_0 == IDENT) :
                    alt147 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 147, 0, self.input)

                    raise nvae

                if alt147 == 1:
                    # Java.g:982:13: primitiveType newArrayConstruction
                    pass 
                    self._state.following.append(self.FOLLOW_primitiveType_in_newExpression14044)
                    primitiveType507 = self.primitiveType()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_primitiveType.add(primitiveType507.tree)
                    self._state.following.append(self.FOLLOW_newArrayConstruction_in_newExpression14046)
                    newArrayConstruction508 = self.newArrayConstruction()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_newArrayConstruction.add(newArrayConstruction508.tree)

                    # AST Rewrite
                    # elements: primitiveType, newArrayConstruction
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 983:13: -> ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] primitiveType newArrayConstruction )
                        # Java.g:983:17: ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] primitiveType newArrayConstruction )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.create(STATIC_ARRAY_CREATOR, NEW506, "STATIC_ARRAY_CREATOR"), root_1)

                        self._adaptor.addChild(root_1, stream_primitiveType.nextTree())
                        self._adaptor.addChild(root_1, stream_newArrayConstruction.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt147 == 2:
                    # Java.g:984:13: ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified ( newArrayConstruction -> ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified newArrayConstruction ) | arguments ( classBody )? -> ^( CLASS_CONSTRUCTOR_CALL[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified arguments ( classBody )? ) )
                    pass 
                    # Java.g:984:13: ( genericTypeArgumentListSimplified )?
                    alt144 = 2
                    LA144_0 = self.input.LA(1)

                    if (LA144_0 == LESS_THAN) :
                        alt144 = 1
                    if alt144 == 1:
                        # Java.g:0:0: genericTypeArgumentListSimplified
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeArgumentListSimplified_in_newExpression14090)
                        genericTypeArgumentListSimplified509 = self.genericTypeArgumentListSimplified()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_genericTypeArgumentListSimplified.add(genericTypeArgumentListSimplified509.tree)



                    self._state.following.append(self.FOLLOW_qualifiedTypeIdentSimplified_in_newExpression14093)
                    qualifiedTypeIdentSimplified510 = self.qualifiedTypeIdentSimplified()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_qualifiedTypeIdentSimplified.add(qualifiedTypeIdentSimplified510.tree)
                    # Java.g:985:13: ( newArrayConstruction -> ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified newArrayConstruction ) | arguments ( classBody )? -> ^( CLASS_CONSTRUCTOR_CALL[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified arguments ( classBody )? ) )
                    alt146 = 2
                    LA146_0 = self.input.LA(1)

                    if (LA146_0 == LBRACK) :
                        alt146 = 1
                    elif (LA146_0 == LPAREN) :
                        alt146 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 146, 0, self.input)

                        raise nvae

                    if alt146 == 1:
                        # Java.g:985:17: newArrayConstruction
                        pass 
                        self._state.following.append(self.FOLLOW_newArrayConstruction_in_newExpression14111)
                        newArrayConstruction511 = self.newArrayConstruction()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_newArrayConstruction.add(newArrayConstruction511.tree)

                        # AST Rewrite
                        # elements: genericTypeArgumentListSimplified, newArrayConstruction, qualifiedTypeIdentSimplified
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 986:17: -> ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified newArrayConstruction )
                            # Java.g:986:21: ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified newArrayConstruction )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.create(STATIC_ARRAY_CREATOR, NEW506, "STATIC_ARRAY_CREATOR"), root_1)

                            # Java.g:986:74: ( genericTypeArgumentListSimplified )?
                            if stream_genericTypeArgumentListSimplified.hasNext():
                                self._adaptor.addChild(root_1, stream_genericTypeArgumentListSimplified.nextTree())


                            stream_genericTypeArgumentListSimplified.reset();
                            self._adaptor.addChild(root_1, stream_qualifiedTypeIdentSimplified.nextTree())
                            self._adaptor.addChild(root_1, stream_newArrayConstruction.nextTree())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt146 == 2:
                        # Java.g:987:17: arguments ( classBody )?
                        pass 
                        self._state.following.append(self.FOLLOW_arguments_in_newExpression14176)
                        arguments512 = self.arguments()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_arguments.add(arguments512.tree)
                        # Java.g:987:27: ( classBody )?
                        alt145 = 2
                        LA145_0 = self.input.LA(1)

                        if (LA145_0 == LCURLY) :
                            alt145 = 1
                        if alt145 == 1:
                            # Java.g:0:0: classBody
                            pass 
                            self._state.following.append(self.FOLLOW_classBody_in_newExpression14178)
                            classBody513 = self.classBody()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_classBody.add(classBody513.tree)




                        # AST Rewrite
                        # elements: arguments, qualifiedTypeIdentSimplified, genericTypeArgumentListSimplified, classBody
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 988:17: -> ^( CLASS_CONSTRUCTOR_CALL[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified arguments ( classBody )? )
                            # Java.g:988:21: ^( CLASS_CONSTRUCTOR_CALL[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified arguments ( classBody )? )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.create(CLASS_CONSTRUCTOR_CALL, NEW506, "STATIC_ARRAY_CREATOR"), root_1)

                            # Java.g:988:76: ( genericTypeArgumentListSimplified )?
                            if stream_genericTypeArgumentListSimplified.hasNext():
                                self._adaptor.addChild(root_1, stream_genericTypeArgumentListSimplified.nextTree())


                            stream_genericTypeArgumentListSimplified.reset();
                            self._adaptor.addChild(root_1, stream_qualifiedTypeIdentSimplified.nextTree())
                            self._adaptor.addChild(root_1, stream_arguments.nextTree())
                            # Java.g:988:150: ( classBody )?
                            if stream_classBody.hasNext():
                                self._adaptor.addChild(root_1, stream_classBody.nextTree())


                            stream_classBody.reset();

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0









                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 107, newExpression_StartIndex, success)

            pass

        return retval

    # $ANTLR end "newExpression"

    class innerNewExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "innerNewExpression"
    # Java.g:993:1: innerNewExpression : NEW ( genericTypeArgumentListSimplified )? IDENT arguments ( classBody )? -> ^( CLASS_CONSTRUCTOR_CALL[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? IDENT arguments ( classBody )? ) ;
    def innerNewExpression(self, ):

        retval = self.innerNewExpression_return()
        retval.start = self.input.LT(1)
        innerNewExpression_StartIndex = self.input.index()
        root_0 = None

        NEW514 = None
        IDENT516 = None
        genericTypeArgumentListSimplified515 = None

        arguments517 = None

        classBody518 = None


        NEW514_tree = None
        IDENT516_tree = None
        stream_NEW = RewriteRuleTokenStream(self._adaptor, "token NEW")
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_arguments = RewriteRuleSubtreeStream(self._adaptor, "rule arguments")
        stream_classBody = RewriteRuleSubtreeStream(self._adaptor, "rule classBody")
        stream_genericTypeArgumentListSimplified = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeArgumentListSimplified")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 108):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:994:5: ( NEW ( genericTypeArgumentListSimplified )? IDENT arguments ( classBody )? -> ^( CLASS_CONSTRUCTOR_CALL[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? IDENT arguments ( classBody )? ) )
                # Java.g:994:9: NEW ( genericTypeArgumentListSimplified )? IDENT arguments ( classBody )?
                pass 
                NEW514=self.match(self.input, NEW, self.FOLLOW_NEW_in_innerNewExpression14273) 
                if self._state.backtracking == 0:
                    stream_NEW.add(NEW514)
                # Java.g:994:13: ( genericTypeArgumentListSimplified )?
                alt148 = 2
                LA148_0 = self.input.LA(1)

                if (LA148_0 == LESS_THAN) :
                    alt148 = 1
                if alt148 == 1:
                    # Java.g:0:0: genericTypeArgumentListSimplified
                    pass 
                    self._state.following.append(self.FOLLOW_genericTypeArgumentListSimplified_in_innerNewExpression14275)
                    genericTypeArgumentListSimplified515 = self.genericTypeArgumentListSimplified()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_genericTypeArgumentListSimplified.add(genericTypeArgumentListSimplified515.tree)



                IDENT516=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_innerNewExpression14278) 
                if self._state.backtracking == 0:
                    stream_IDENT.add(IDENT516)
                self._state.following.append(self.FOLLOW_arguments_in_innerNewExpression14280)
                arguments517 = self.arguments()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_arguments.add(arguments517.tree)
                # Java.g:994:64: ( classBody )?
                alt149 = 2
                LA149_0 = self.input.LA(1)

                if (LA149_0 == LCURLY) :
                    alt149 = 1
                if alt149 == 1:
                    # Java.g:0:0: classBody
                    pass 
                    self._state.following.append(self.FOLLOW_classBody_in_innerNewExpression14282)
                    classBody518 = self.classBody()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_classBody.add(classBody518.tree)




                # AST Rewrite
                # elements: arguments, genericTypeArgumentListSimplified, IDENT, classBody
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 995:9: -> ^( CLASS_CONSTRUCTOR_CALL[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? IDENT arguments ( classBody )? )
                    # Java.g:995:13: ^( CLASS_CONSTRUCTOR_CALL[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? IDENT arguments ( classBody )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.create(CLASS_CONSTRUCTOR_CALL, NEW514, "STATIC_ARRAY_CREATOR"), root_1)

                    # Java.g:995:68: ( genericTypeArgumentListSimplified )?
                    if stream_genericTypeArgumentListSimplified.hasNext():
                        self._adaptor.addChild(root_1, stream_genericTypeArgumentListSimplified.nextTree())


                    stream_genericTypeArgumentListSimplified.reset();
                    self._adaptor.addChild(root_1, stream_IDENT.nextNode())
                    self._adaptor.addChild(root_1, stream_arguments.nextTree())
                    # Java.g:995:119: ( classBody )?
                    if stream_classBody.hasNext():
                        self._adaptor.addChild(root_1, stream_classBody.nextTree())


                    stream_classBody.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 108, innerNewExpression_StartIndex, success)

            pass

        return retval

    # $ANTLR end "innerNewExpression"

    class newArrayConstruction_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "newArrayConstruction"
    # Java.g:998:1: newArrayConstruction : ( arrayDeclaratorList arrayInitializer | LBRACK expression RBRACK ( LBRACK expression RBRACK )* ( arrayDeclaratorList )? );
    def newArrayConstruction(self, ):

        retval = self.newArrayConstruction_return()
        retval.start = self.input.LT(1)
        newArrayConstruction_StartIndex = self.input.index()
        root_0 = None

        LBRACK521 = None
        RBRACK523 = None
        LBRACK524 = None
        RBRACK526 = None
        arrayDeclaratorList519 = None

        arrayInitializer520 = None

        expression522 = None

        expression525 = None

        arrayDeclaratorList527 = None


        LBRACK521_tree = None
        RBRACK523_tree = None
        LBRACK524_tree = None
        RBRACK526_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 109):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:999:5: ( arrayDeclaratorList arrayInitializer | LBRACK expression RBRACK ( LBRACK expression RBRACK )* ( arrayDeclaratorList )? )
                alt152 = 2
                LA152_0 = self.input.LA(1)

                if (LA152_0 == LBRACK) :
                    LA152_1 = self.input.LA(2)

                    if (LA152_1 == RBRACK) :
                        alt152 = 1
                    elif (LA152_1 == DEC or LA152_1 == INC or LA152_1 == LESS_THAN or LA152_1 == LOGICAL_NOT or (LPAREN <= LA152_1 <= MINUS) or LA152_1 == NOT or LA152_1 == PLUS or LA152_1 == BOOLEAN or LA152_1 == BYTE or LA152_1 == CHAR or LA152_1 == DOUBLE or LA152_1 == FALSE or LA152_1 == FLOAT or (INT <= LA152_1 <= LONG) or (NEW <= LA152_1 <= NULL) or LA152_1 == SHORT or LA152_1 == SUPER or LA152_1 == THIS or LA152_1 == TRUE or LA152_1 == VOID or (IDENT <= LA152_1 <= STRING_LITERAL)) :
                        alt152 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 152, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 152, 0, self.input)

                    raise nvae

                if alt152 == 1:
                    # Java.g:999:9: arrayDeclaratorList arrayInitializer
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_newArrayConstruction14328)
                    arrayDeclaratorList519 = self.arrayDeclaratorList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, arrayDeclaratorList519.tree)
                    self._state.following.append(self.FOLLOW_arrayInitializer_in_newArrayConstruction14330)
                    arrayInitializer520 = self.arrayInitializer()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, arrayInitializer520.tree)


                elif alt152 == 2:
                    # Java.g:1000:9: LBRACK expression RBRACK ( LBRACK expression RBRACK )* ( arrayDeclaratorList )?
                    pass 
                    root_0 = self._adaptor.nil()

                    LBRACK521=self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_newArrayConstruction14340)
                    self._state.following.append(self.FOLLOW_expression_in_newArrayConstruction14343)
                    expression522 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression522.tree)
                    RBRACK523=self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_newArrayConstruction14345)
                    # Java.g:1000:36: ( LBRACK expression RBRACK )*
                    while True: #loop150
                        alt150 = 2
                        alt150 = self.dfa150.predict(self.input)
                        if alt150 == 1:
                            # Java.g:1000:37: LBRACK expression RBRACK
                            pass 
                            LBRACK524=self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_newArrayConstruction14349)
                            self._state.following.append(self.FOLLOW_expression_in_newArrayConstruction14352)
                            expression525 = self.expression()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, expression525.tree)
                            RBRACK526=self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_newArrayConstruction14354)


                        else:
                            break #loop150


                    # Java.g:1000:66: ( arrayDeclaratorList )?
                    alt151 = 2
                    LA151_0 = self.input.LA(1)

                    if (LA151_0 == LBRACK) :
                        LA151_1 = self.input.LA(2)

                        if (LA151_1 == RBRACK) :
                            alt151 = 1
                    if alt151 == 1:
                        # Java.g:0:0: arrayDeclaratorList
                        pass 
                        self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_newArrayConstruction14359)
                        arrayDeclaratorList527 = self.arrayDeclaratorList()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arrayDeclaratorList527.tree)





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 109, newArrayConstruction_StartIndex, success)

            pass

        return retval

    # $ANTLR end "newArrayConstruction"

    class arguments_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "arguments"
    # Java.g:1003:1: arguments : LPAREN ( expressionList )? RPAREN -> ^( ARGUMENT_LIST[$LPAREN, \"ARGUMENT_LIST\"] ( expressionList )? ) ;
    def arguments(self, ):

        retval = self.arguments_return()
        retval.start = self.input.LT(1)
        arguments_StartIndex = self.input.index()
        root_0 = None

        LPAREN528 = None
        RPAREN530 = None
        expressionList529 = None


        LPAREN528_tree = None
        RPAREN530_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_expressionList = RewriteRuleSubtreeStream(self._adaptor, "rule expressionList")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 110):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:1004:5: ( LPAREN ( expressionList )? RPAREN -> ^( ARGUMENT_LIST[$LPAREN, \"ARGUMENT_LIST\"] ( expressionList )? ) )
                # Java.g:1004:9: LPAREN ( expressionList )? RPAREN
                pass 
                LPAREN528=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_arguments14379) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(LPAREN528)
                # Java.g:1004:16: ( expressionList )?
                alt153 = 2
                LA153_0 = self.input.LA(1)

                if (LA153_0 == DEC or LA153_0 == INC or LA153_0 == LESS_THAN or LA153_0 == LOGICAL_NOT or (LPAREN <= LA153_0 <= MINUS) or LA153_0 == NOT or LA153_0 == PLUS or LA153_0 == BOOLEAN or LA153_0 == BYTE or LA153_0 == CHAR or LA153_0 == DOUBLE or LA153_0 == FALSE or LA153_0 == FLOAT or (INT <= LA153_0 <= LONG) or (NEW <= LA153_0 <= NULL) or LA153_0 == SHORT or LA153_0 == SUPER or LA153_0 == THIS or LA153_0 == TRUE or LA153_0 == VOID or (IDENT <= LA153_0 <= STRING_LITERAL)) :
                    alt153 = 1
                if alt153 == 1:
                    # Java.g:0:0: expressionList
                    pass 
                    self._state.following.append(self.FOLLOW_expressionList_in_arguments14381)
                    expressionList529 = self.expressionList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expressionList.add(expressionList529.tree)



                RPAREN530=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_arguments14384) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(RPAREN530)

                # AST Rewrite
                # elements: expressionList
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 1005:9: -> ^( ARGUMENT_LIST[$LPAREN, \"ARGUMENT_LIST\"] ( expressionList )? )
                    # Java.g:1005:13: ^( ARGUMENT_LIST[$LPAREN, \"ARGUMENT_LIST\"] ( expressionList )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.create(ARGUMENT_LIST, LPAREN528, "ARGUMENT_LIST"), root_1)

                    # Java.g:1005:55: ( expressionList )?
                    if stream_expressionList.hasNext():
                        self._adaptor.addChild(root_1, stream_expressionList.nextTree())


                    stream_expressionList.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 110, arguments_StartIndex, success)

            pass

        return retval

    # $ANTLR end "arguments"

    class literal_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "literal"
    # Java.g:1008:1: literal : ( HEX_LITERAL | OCTAL_LITERAL | DECIMAL_LITERAL | FLOATING_POINT_LITERAL | CHARACTER_LITERAL | STRING_LITERAL | TRUE | FALSE | NULL );
    def literal(self, ):

        retval = self.literal_return()
        retval.start = self.input.LT(1)
        literal_StartIndex = self.input.index()
        root_0 = None

        set531 = None

        set531_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 111):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # Java.g:1009:5: ( HEX_LITERAL | OCTAL_LITERAL | DECIMAL_LITERAL | FLOATING_POINT_LITERAL | CHARACTER_LITERAL | STRING_LITERAL | TRUE | FALSE | NULL )
                # Java.g:
                pass 
                root_0 = self._adaptor.nil()

                set531 = self.input.LT(1)
                if self.input.LA(1) == FALSE or self.input.LA(1) == NULL or self.input.LA(1) == TRUE or (HEX_LITERAL <= self.input.LA(1) <= STRING_LITERAL):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set531))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 111, literal_StartIndex, success)

            pass

        return retval

    # $ANTLR end "literal"

    # $ANTLR start "synpred14_Java"
    def synpred14_Java_fragment(self, ):
        # Java.g:323:9: ( GREATER_THAN )
        # Java.g:323:9: GREATER_THAN
        pass 
        self.match(self.input, GREATER_THAN, self.FOLLOW_GREATER_THAN_in_synpred14_Java5069)


    # $ANTLR end "synpred14_Java"



    # $ANTLR start "synpred15_Java"
    def synpred15_Java_fragment(self, ):
        # Java.g:324:9: ( SHIFT_RIGHT )
        # Java.g:324:9: SHIFT_RIGHT
        pass 
        self.match(self.input, SHIFT_RIGHT, self.FOLLOW_SHIFT_RIGHT_in_synpred15_Java5079)


    # $ANTLR end "synpred15_Java"



    # $ANTLR start "synpred16_Java"
    def synpred16_Java_fragment(self, ):
        # Java.g:325:9: ( BIT_SHIFT_RIGHT )
        # Java.g:325:9: BIT_SHIFT_RIGHT
        pass 
        self.match(self.input, BIT_SHIFT_RIGHT, self.FOLLOW_BIT_SHIFT_RIGHT_in_synpred16_Java5089)


    # $ANTLR end "synpred16_Java"



    # $ANTLR start "synpred17_Java"
    def synpred17_Java_fragment(self, ):
        # Java.g:330:15: ( bound )
        # Java.g:330:15: bound
        pass 
        self._state.following.append(self.FOLLOW_bound_in_synpred17_Java5119)
        self.bound()

        self._state.following.pop()


    # $ANTLR end "synpred17_Java"



    # $ANTLR start "synpred32_Java"
    def synpred32_Java_fragment(self, ):
        # Java.g:387:9: ( STATIC block )
        # Java.g:387:9: STATIC block
        pass 
        self.match(self.input, STATIC, self.FOLLOW_STATIC_in_synpred32_Java5619)
        self._state.following.append(self.FOLLOW_block_in_synpred32_Java5621)
        self.block()

        self._state.following.pop()


    # $ANTLR end "synpred32_Java"



    # $ANTLR start "synpred42_Java"
    def synpred42_Java_fragment(self, ):
        # Java.g:389:13: ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) | ident= IDENT formalParameterList ( throwsClause )? block ) )
        # Java.g:389:13: ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) | ident= IDENT formalParameterList ( throwsClause )? block )
        pass 
        # Java.g:389:13: ( genericTypeParameterList )?
        alt159 = 2
        LA159_0 = self.input.LA(1)

        if (LA159_0 == LESS_THAN) :
            alt159 = 1
        if alt159 == 1:
            # Java.g:0:0: genericTypeParameterList
            pass 
            self._state.following.append(self.FOLLOW_genericTypeParameterList_in_synpred42_Java5658)
            self.genericTypeParameterList()

            self._state.following.pop()



        # Java.g:390:13: ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) | ident= IDENT formalParameterList ( throwsClause )? block )
        alt166 = 3
        LA166 = self.input.LA(1)
        if LA166 == BOOLEAN or LA166 == BYTE or LA166 == CHAR or LA166 == DOUBLE or LA166 == FLOAT or LA166 == INT or LA166 == LONG or LA166 == SHORT:
            alt166 = 1
        elif LA166 == IDENT:
            LA166_2 = self.input.LA(2)

            if (LA166_2 == LPAREN) :
                alt166 = 3
            elif (LA166_2 == DOT or LA166_2 == LBRACK or LA166_2 == LESS_THAN or LA166_2 == IDENT) :
                alt166 = 1
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 166, 2, self.input)

                raise nvae

        elif LA166 == VOID:
            alt166 = 2
        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            nvae = NoViableAltException("", 166, 0, self.input)

            raise nvae

        if alt166 == 1:
            # Java.g:390:17: type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI )
            pass 
            self._state.following.append(self.FOLLOW_type_in_synpred42_Java5677)
            self.type()

            self._state.following.pop()
            self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred42_Java5679)
            self._state.following.append(self.FOLLOW_formalParameterList_in_synpred42_Java5681)
            self.formalParameterList()

            self._state.following.pop()
            # Java.g:390:48: ( arrayDeclaratorList )?
            alt160 = 2
            LA160_0 = self.input.LA(1)

            if (LA160_0 == LBRACK) :
                alt160 = 1
            if alt160 == 1:
                # Java.g:0:0: arrayDeclaratorList
                pass 
                self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_synpred42_Java5683)
                self.arrayDeclaratorList()

                self._state.following.pop()



            # Java.g:390:69: ( throwsClause )?
            alt161 = 2
            LA161_0 = self.input.LA(1)

            if (LA161_0 == THROWS) :
                alt161 = 1
            if alt161 == 1:
                # Java.g:0:0: throwsClause
                pass 
                self._state.following.append(self.FOLLOW_throwsClause_in_synpred42_Java5686)
                self.throwsClause()

                self._state.following.pop()



            # Java.g:390:83: ( block | SEMI )
            alt162 = 2
            LA162_0 = self.input.LA(1)

            if (LA162_0 == LCURLY) :
                alt162 = 1
            elif (LA162_0 == SEMI) :
                alt162 = 2
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 162, 0, self.input)

                raise nvae

            if alt162 == 1:
                # Java.g:390:84: block
                pass 
                self._state.following.append(self.FOLLOW_block_in_synpred42_Java5690)
                self.block()

                self._state.following.pop()


            elif alt162 == 2:
                # Java.g:390:92: SEMI
                pass 
                self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred42_Java5694)





        elif alt166 == 2:
            # Java.g:392:17: VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI )
            pass 
            self.match(self.input, VOID, self.FOLLOW_VOID_in_synpred42_Java5756)
            self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred42_Java5758)
            self._state.following.append(self.FOLLOW_formalParameterList_in_synpred42_Java5760)
            self.formalParameterList()

            self._state.following.pop()
            # Java.g:392:48: ( throwsClause )?
            alt163 = 2
            LA163_0 = self.input.LA(1)

            if (LA163_0 == THROWS) :
                alt163 = 1
            if alt163 == 1:
                # Java.g:0:0: throwsClause
                pass 
                self._state.following.append(self.FOLLOW_throwsClause_in_synpred42_Java5762)
                self.throwsClause()

                self._state.following.pop()



            # Java.g:392:62: ( block | SEMI )
            alt164 = 2
            LA164_0 = self.input.LA(1)

            if (LA164_0 == LCURLY) :
                alt164 = 1
            elif (LA164_0 == SEMI) :
                alt164 = 2
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 164, 0, self.input)

                raise nvae

            if alt164 == 1:
                # Java.g:392:63: block
                pass 
                self._state.following.append(self.FOLLOW_block_in_synpred42_Java5766)
                self.block()

                self._state.following.pop()


            elif alt164 == 2:
                # Java.g:392:71: SEMI
                pass 
                self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred42_Java5770)





        elif alt166 == 3:
            # Java.g:394:17: ident= IDENT formalParameterList ( throwsClause )? block
            pass 
            ident=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred42_Java5829)
            self._state.following.append(self.FOLLOW_formalParameterList_in_synpred42_Java5831)
            self.formalParameterList()

            self._state.following.pop()
            # Java.g:394:49: ( throwsClause )?
            alt165 = 2
            LA165_0 = self.input.LA(1)

            if (LA165_0 == THROWS) :
                alt165 = 1
            if alt165 == 1:
                # Java.g:0:0: throwsClause
                pass 
                self._state.following.append(self.FOLLOW_throwsClause_in_synpred42_Java5833)
                self.throwsClause()

                self._state.following.pop()



            self._state.following.append(self.FOLLOW_block_in_synpred42_Java5836)
            self.block()

            self._state.following.pop()





    # $ANTLR end "synpred42_Java"



    # $ANTLR start "synpred43_Java"
    def synpred43_Java_fragment(self, ):
        # Java.g:388:9: ( modifierList ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) | ident= IDENT formalParameterList ( throwsClause )? block ) | type classFieldDeclaratorList SEMI ) )
        # Java.g:388:9: modifierList ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) | ident= IDENT formalParameterList ( throwsClause )? block ) | type classFieldDeclaratorList SEMI )
        pass 
        self._state.following.append(self.FOLLOW_modifierList_in_synpred43_Java5644)
        self.modifierList()

        self._state.following.pop()
        # Java.g:389:9: ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) | ident= IDENT formalParameterList ( throwsClause )? block ) | type classFieldDeclaratorList SEMI )
        alt175 = 2
        LA175 = self.input.LA(1)
        if LA175 == LESS_THAN or LA175 == VOID:
            alt175 = 1
        elif LA175 == BOOLEAN or LA175 == BYTE or LA175 == CHAR or LA175 == DOUBLE or LA175 == FLOAT or LA175 == INT or LA175 == LONG or LA175 == SHORT:
            LA175_2 = self.input.LA(2)

            if (self.synpred42_Java()) :
                alt175 = 1
            elif (True) :
                alt175 = 2
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 175, 2, self.input)

                raise nvae

        elif LA175 == IDENT:
            LA175_3 = self.input.LA(2)

            if (self.synpred42_Java()) :
                alt175 = 1
            elif (True) :
                alt175 = 2
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 175, 3, self.input)

                raise nvae

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            nvae = NoViableAltException("", 175, 0, self.input)

            raise nvae

        if alt175 == 1:
            # Java.g:389:13: ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) | ident= IDENT formalParameterList ( throwsClause )? block )
            pass 
            # Java.g:389:13: ( genericTypeParameterList )?
            alt167 = 2
            LA167_0 = self.input.LA(1)

            if (LA167_0 == LESS_THAN) :
                alt167 = 1
            if alt167 == 1:
                # Java.g:0:0: genericTypeParameterList
                pass 
                self._state.following.append(self.FOLLOW_genericTypeParameterList_in_synpred43_Java5658)
                self.genericTypeParameterList()

                self._state.following.pop()



            # Java.g:390:13: ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) | ident= IDENT formalParameterList ( throwsClause )? block )
            alt174 = 3
            LA174 = self.input.LA(1)
            if LA174 == BOOLEAN or LA174 == BYTE or LA174 == CHAR or LA174 == DOUBLE or LA174 == FLOAT or LA174 == INT or LA174 == LONG or LA174 == SHORT:
                alt174 = 1
            elif LA174 == IDENT:
                LA174_2 = self.input.LA(2)

                if (LA174_2 == DOT or LA174_2 == LBRACK or LA174_2 == LESS_THAN or LA174_2 == IDENT) :
                    alt174 = 1
                elif (LA174_2 == LPAREN) :
                    alt174 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 174, 2, self.input)

                    raise nvae

            elif LA174 == VOID:
                alt174 = 2
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 174, 0, self.input)

                raise nvae

            if alt174 == 1:
                # Java.g:390:17: type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI )
                pass 
                self._state.following.append(self.FOLLOW_type_in_synpred43_Java5677)
                self.type()

                self._state.following.pop()
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred43_Java5679)
                self._state.following.append(self.FOLLOW_formalParameterList_in_synpred43_Java5681)
                self.formalParameterList()

                self._state.following.pop()
                # Java.g:390:48: ( arrayDeclaratorList )?
                alt168 = 2
                LA168_0 = self.input.LA(1)

                if (LA168_0 == LBRACK) :
                    alt168 = 1
                if alt168 == 1:
                    # Java.g:0:0: arrayDeclaratorList
                    pass 
                    self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_synpred43_Java5683)
                    self.arrayDeclaratorList()

                    self._state.following.pop()



                # Java.g:390:69: ( throwsClause )?
                alt169 = 2
                LA169_0 = self.input.LA(1)

                if (LA169_0 == THROWS) :
                    alt169 = 1
                if alt169 == 1:
                    # Java.g:0:0: throwsClause
                    pass 
                    self._state.following.append(self.FOLLOW_throwsClause_in_synpred43_Java5686)
                    self.throwsClause()

                    self._state.following.pop()



                # Java.g:390:83: ( block | SEMI )
                alt170 = 2
                LA170_0 = self.input.LA(1)

                if (LA170_0 == LCURLY) :
                    alt170 = 1
                elif (LA170_0 == SEMI) :
                    alt170 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 170, 0, self.input)

                    raise nvae

                if alt170 == 1:
                    # Java.g:390:84: block
                    pass 
                    self._state.following.append(self.FOLLOW_block_in_synpred43_Java5690)
                    self.block()

                    self._state.following.pop()


                elif alt170 == 2:
                    # Java.g:390:92: SEMI
                    pass 
                    self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred43_Java5694)





            elif alt174 == 2:
                # Java.g:392:17: VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI )
                pass 
                self.match(self.input, VOID, self.FOLLOW_VOID_in_synpred43_Java5756)
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred43_Java5758)
                self._state.following.append(self.FOLLOW_formalParameterList_in_synpred43_Java5760)
                self.formalParameterList()

                self._state.following.pop()
                # Java.g:392:48: ( throwsClause )?
                alt171 = 2
                LA171_0 = self.input.LA(1)

                if (LA171_0 == THROWS) :
                    alt171 = 1
                if alt171 == 1:
                    # Java.g:0:0: throwsClause
                    pass 
                    self._state.following.append(self.FOLLOW_throwsClause_in_synpred43_Java5762)
                    self.throwsClause()

                    self._state.following.pop()



                # Java.g:392:62: ( block | SEMI )
                alt172 = 2
                LA172_0 = self.input.LA(1)

                if (LA172_0 == LCURLY) :
                    alt172 = 1
                elif (LA172_0 == SEMI) :
                    alt172 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 172, 0, self.input)

                    raise nvae

                if alt172 == 1:
                    # Java.g:392:63: block
                    pass 
                    self._state.following.append(self.FOLLOW_block_in_synpred43_Java5766)
                    self.block()

                    self._state.following.pop()


                elif alt172 == 2:
                    # Java.g:392:71: SEMI
                    pass 
                    self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred43_Java5770)





            elif alt174 == 3:
                # Java.g:394:17: ident= IDENT formalParameterList ( throwsClause )? block
                pass 
                ident=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred43_Java5829)
                self._state.following.append(self.FOLLOW_formalParameterList_in_synpred43_Java5831)
                self.formalParameterList()

                self._state.following.pop()
                # Java.g:394:49: ( throwsClause )?
                alt173 = 2
                LA173_0 = self.input.LA(1)

                if (LA173_0 == THROWS) :
                    alt173 = 1
                if alt173 == 1:
                    # Java.g:0:0: throwsClause
                    pass 
                    self._state.following.append(self.FOLLOW_throwsClause_in_synpred43_Java5833)
                    self.throwsClause()

                    self._state.following.pop()



                self._state.following.append(self.FOLLOW_block_in_synpred43_Java5836)
                self.block()

                self._state.following.pop()





        elif alt175 == 2:
            # Java.g:397:13: type classFieldDeclaratorList SEMI
            pass 
            self._state.following.append(self.FOLLOW_type_in_synpred43_Java5900)
            self.type()

            self._state.following.pop()
            self._state.following.append(self.FOLLOW_classFieldDeclaratorList_in_synpred43_Java5902)
            self.classFieldDeclaratorList()

            self._state.following.pop()
            self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred43_Java5904)





    # $ANTLR end "synpred43_Java"



    # $ANTLR start "synpred44_Java"
    def synpred44_Java_fragment(self, ):
        # Java.g:400:9: ( typeDeclaration )
        # Java.g:400:9: typeDeclaration
        pass 
        self._state.following.append(self.FOLLOW_typeDeclaration_in_synpred44_Java5949)
        self.typeDeclaration()

        self._state.following.pop()


    # $ANTLR end "synpred44_Java"



    # $ANTLR start "synpred50_Java"
    def synpred50_Java_fragment(self, ):
        # Java.g:406:13: ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI | VOID IDENT formalParameterList ( throwsClause )? SEMI ) )
        # Java.g:406:13: ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI | VOID IDENT formalParameterList ( throwsClause )? SEMI )
        pass 
        # Java.g:406:13: ( genericTypeParameterList )?
        alt178 = 2
        LA178_0 = self.input.LA(1)

        if (LA178_0 == LESS_THAN) :
            alt178 = 1
        if alt178 == 1:
            # Java.g:0:0: genericTypeParameterList
            pass 
            self._state.following.append(self.FOLLOW_genericTypeParameterList_in_synpred50_Java5993)
            self.genericTypeParameterList()

            self._state.following.pop()



        # Java.g:407:13: ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI | VOID IDENT formalParameterList ( throwsClause )? SEMI )
        alt182 = 2
        LA182_0 = self.input.LA(1)

        if (LA182_0 == BOOLEAN or LA182_0 == BYTE or LA182_0 == CHAR or LA182_0 == DOUBLE or LA182_0 == FLOAT or (INT <= LA182_0 <= LONG) or LA182_0 == SHORT or LA182_0 == IDENT) :
            alt182 = 1
        elif (LA182_0 == VOID) :
            alt182 = 2
        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            nvae = NoViableAltException("", 182, 0, self.input)

            raise nvae

        if alt182 == 1:
            # Java.g:407:17: type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI
            pass 
            self._state.following.append(self.FOLLOW_type_in_synpred50_Java6012)
            self.type()

            self._state.following.pop()
            self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred50_Java6014)
            self._state.following.append(self.FOLLOW_formalParameterList_in_synpred50_Java6016)
            self.formalParameterList()

            self._state.following.pop()
            # Java.g:407:48: ( arrayDeclaratorList )?
            alt179 = 2
            LA179_0 = self.input.LA(1)

            if (LA179_0 == LBRACK) :
                alt179 = 1
            if alt179 == 1:
                # Java.g:0:0: arrayDeclaratorList
                pass 
                self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_synpred50_Java6018)
                self.arrayDeclaratorList()

                self._state.following.pop()



            # Java.g:407:69: ( throwsClause )?
            alt180 = 2
            LA180_0 = self.input.LA(1)

            if (LA180_0 == THROWS) :
                alt180 = 1
            if alt180 == 1:
                # Java.g:0:0: throwsClause
                pass 
                self._state.following.append(self.FOLLOW_throwsClause_in_synpred50_Java6021)
                self.throwsClause()

                self._state.following.pop()



            self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred50_Java6024)


        elif alt182 == 2:
            # Java.g:409:17: VOID IDENT formalParameterList ( throwsClause )? SEMI
            pass 
            self.match(self.input, VOID, self.FOLLOW_VOID_in_synpred50_Java6082)
            self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred50_Java6084)
            self._state.following.append(self.FOLLOW_formalParameterList_in_synpred50_Java6086)
            self.formalParameterList()

            self._state.following.pop()
            # Java.g:409:48: ( throwsClause )?
            alt181 = 2
            LA181_0 = self.input.LA(1)

            if (LA181_0 == THROWS) :
                alt181 = 1
            if alt181 == 1:
                # Java.g:0:0: throwsClause
                pass 
                self._state.following.append(self.FOLLOW_throwsClause_in_synpred50_Java6088)
                self.throwsClause()

                self._state.following.pop()



            self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred50_Java6091)





    # $ANTLR end "synpred50_Java"



    # $ANTLR start "synpred51_Java"
    def synpred51_Java_fragment(self, ):
        # Java.g:405:9: ( modifierList ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI | VOID IDENT formalParameterList ( throwsClause )? SEMI ) | type interfaceFieldDeclaratorList SEMI ) )
        # Java.g:405:9: modifierList ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI | VOID IDENT formalParameterList ( throwsClause )? SEMI ) | type interfaceFieldDeclaratorList SEMI )
        pass 
        self._state.following.append(self.FOLLOW_modifierList_in_synpred51_Java5979)
        self.modifierList()

        self._state.following.pop()
        # Java.g:406:9: ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI | VOID IDENT formalParameterList ( throwsClause )? SEMI ) | type interfaceFieldDeclaratorList SEMI )
        alt188 = 2
        LA188 = self.input.LA(1)
        if LA188 == LESS_THAN or LA188 == VOID:
            alt188 = 1
        elif LA188 == BOOLEAN or LA188 == BYTE or LA188 == CHAR or LA188 == DOUBLE or LA188 == FLOAT or LA188 == INT or LA188 == LONG or LA188 == SHORT:
            LA188_2 = self.input.LA(2)

            if (self.synpred50_Java()) :
                alt188 = 1
            elif (True) :
                alt188 = 2
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 188, 2, self.input)

                raise nvae

        elif LA188 == IDENT:
            LA188_3 = self.input.LA(2)

            if (self.synpred50_Java()) :
                alt188 = 1
            elif (True) :
                alt188 = 2
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 188, 3, self.input)

                raise nvae

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            nvae = NoViableAltException("", 188, 0, self.input)

            raise nvae

        if alt188 == 1:
            # Java.g:406:13: ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI | VOID IDENT formalParameterList ( throwsClause )? SEMI )
            pass 
            # Java.g:406:13: ( genericTypeParameterList )?
            alt183 = 2
            LA183_0 = self.input.LA(1)

            if (LA183_0 == LESS_THAN) :
                alt183 = 1
            if alt183 == 1:
                # Java.g:0:0: genericTypeParameterList
                pass 
                self._state.following.append(self.FOLLOW_genericTypeParameterList_in_synpred51_Java5993)
                self.genericTypeParameterList()

                self._state.following.pop()



            # Java.g:407:13: ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI | VOID IDENT formalParameterList ( throwsClause )? SEMI )
            alt187 = 2
            LA187_0 = self.input.LA(1)

            if (LA187_0 == BOOLEAN or LA187_0 == BYTE or LA187_0 == CHAR or LA187_0 == DOUBLE or LA187_0 == FLOAT or (INT <= LA187_0 <= LONG) or LA187_0 == SHORT or LA187_0 == IDENT) :
                alt187 = 1
            elif (LA187_0 == VOID) :
                alt187 = 2
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 187, 0, self.input)

                raise nvae

            if alt187 == 1:
                # Java.g:407:17: type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI
                pass 
                self._state.following.append(self.FOLLOW_type_in_synpred51_Java6012)
                self.type()

                self._state.following.pop()
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred51_Java6014)
                self._state.following.append(self.FOLLOW_formalParameterList_in_synpred51_Java6016)
                self.formalParameterList()

                self._state.following.pop()
                # Java.g:407:48: ( arrayDeclaratorList )?
                alt184 = 2
                LA184_0 = self.input.LA(1)

                if (LA184_0 == LBRACK) :
                    alt184 = 1
                if alt184 == 1:
                    # Java.g:0:0: arrayDeclaratorList
                    pass 
                    self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_synpred51_Java6018)
                    self.arrayDeclaratorList()

                    self._state.following.pop()



                # Java.g:407:69: ( throwsClause )?
                alt185 = 2
                LA185_0 = self.input.LA(1)

                if (LA185_0 == THROWS) :
                    alt185 = 1
                if alt185 == 1:
                    # Java.g:0:0: throwsClause
                    pass 
                    self._state.following.append(self.FOLLOW_throwsClause_in_synpred51_Java6021)
                    self.throwsClause()

                    self._state.following.pop()



                self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred51_Java6024)


            elif alt187 == 2:
                # Java.g:409:17: VOID IDENT formalParameterList ( throwsClause )? SEMI
                pass 
                self.match(self.input, VOID, self.FOLLOW_VOID_in_synpred51_Java6082)
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred51_Java6084)
                self._state.following.append(self.FOLLOW_formalParameterList_in_synpred51_Java6086)
                self.formalParameterList()

                self._state.following.pop()
                # Java.g:409:48: ( throwsClause )?
                alt186 = 2
                LA186_0 = self.input.LA(1)

                if (LA186_0 == THROWS) :
                    alt186 = 1
                if alt186 == 1:
                    # Java.g:0:0: throwsClause
                    pass 
                    self._state.following.append(self.FOLLOW_throwsClause_in_synpred51_Java6088)
                    self.throwsClause()

                    self._state.following.pop()



                self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred51_Java6091)





        elif alt188 == 2:
            # Java.g:412:13: type interfaceFieldDeclaratorList SEMI
            pass 
            self._state.following.append(self.FOLLOW_type_in_synpred51_Java6154)
            self.type()

            self._state.following.pop()
            self._state.following.append(self.FOLLOW_interfaceFieldDeclaratorList_in_synpred51_Java6156)
            self.interfaceFieldDeclaratorList()

            self._state.following.pop()
            self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred51_Java6158)





    # $ANTLR end "synpred51_Java"



    # $ANTLR start "synpred52_Java"
    def synpred52_Java_fragment(self, ):
        # Java.g:415:9: ( typeDeclaration )
        # Java.g:415:9: typeDeclaration
        pass 
        self._state.following.append(self.FOLLOW_typeDeclaration_in_synpred52_Java6203)
        self.typeDeclaration()

        self._state.following.pop()


    # $ANTLR end "synpred52_Java"



    # $ANTLR start "synpred58_Java"
    def synpred58_Java_fragment(self, ):
        # Java.g:454:9: ( arrayDeclarator )
        # Java.g:454:9: arrayDeclarator
        pass 
        self._state.following.append(self.FOLLOW_arrayDeclarator_in_synpred58_Java6497)
        self.arrayDeclarator()

        self._state.following.pop()


    # $ANTLR end "synpred58_Java"



    # $ANTLR start "synpred76_Java"
    def synpred76_Java_fragment(self, ):
        # Java.g:503:23: ( arrayDeclaratorList )
        # Java.g:503:23: arrayDeclaratorList
        pass 
        self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_synpred76_Java6884)
        self.arrayDeclaratorList()

        self._state.following.pop()


    # $ANTLR end "synpred76_Java"



    # $ANTLR start "synpred77_Java"
    def synpred77_Java_fragment(self, ):
        # Java.g:508:28: ( arrayDeclaratorList )
        # Java.g:508:28: arrayDeclaratorList
        pass 
        self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_synpred77_Java6927)
        self.arrayDeclaratorList()

        self._state.following.pop()


    # $ANTLR end "synpred77_Java"



    # $ANTLR start "synpred79_Java"
    def synpred79_Java_fragment(self, ):
        # Java.g:518:20: ( DOT typeIdent )
        # Java.g:518:20: DOT typeIdent
        pass 
        self.match(self.input, DOT, self.FOLLOW_DOT_in_synpred79_Java7012)
        self._state.following.append(self.FOLLOW_typeIdent_in_synpred79_Java7014)
        self.typeIdent()

        self._state.following.pop()


    # $ANTLR end "synpred79_Java"



    # $ANTLR start "synpred90_Java"
    def synpred90_Java_fragment(self, ):
        # Java.g:547:40: ( COMMA genericTypeArgument )
        # Java.g:547:40: COMMA genericTypeArgument
        pass 
        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_synpred90_Java7237)
        self._state.following.append(self.FOLLOW_genericTypeArgument_in_synpred90_Java7239)
        self.genericTypeArgument()

        self._state.following.pop()


    # $ANTLR end "synpred90_Java"



    # $ANTLR start "synpred92_Java"
    def synpred92_Java_fragment(self, ):
        # Java.g:553:18: ( genericWildcardBoundType )
        # Java.g:553:18: genericWildcardBoundType
        pass 
        self._state.following.append(self.FOLLOW_genericWildcardBoundType_in_synpred92_Java7293)
        self.genericWildcardBoundType()

        self._state.following.pop()


    # $ANTLR end "synpred92_Java"



    # $ANTLR start "synpred97_Java"
    def synpred97_Java_fragment(self, ):
        # Java.g:578:42: ( COMMA formalParameterStandardDecl )
        # Java.g:578:42: COMMA formalParameterStandardDecl
        pass 
        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_synpred97_Java7494)
        self._state.following.append(self.FOLLOW_formalParameterStandardDecl_in_synpred97_Java7496)
        self.formalParameterStandardDecl()

        self._state.following.pop()


    # $ANTLR end "synpred97_Java"



    # $ANTLR start "synpred99_Java"
    def synpred99_Java_fragment(self, ):
        # Java.g:578:13: ( formalParameterStandardDecl ( COMMA formalParameterStandardDecl )* ( COMMA formalParameterVarArgDecl )? )
        # Java.g:578:13: formalParameterStandardDecl ( COMMA formalParameterStandardDecl )* ( COMMA formalParameterVarArgDecl )?
        pass 
        self._state.following.append(self.FOLLOW_formalParameterStandardDecl_in_synpred99_Java7491)
        self.formalParameterStandardDecl()

        self._state.following.pop()
        # Java.g:578:41: ( COMMA formalParameterStandardDecl )*
        while True: #loop191
            alt191 = 2
            LA191_0 = self.input.LA(1)

            if (LA191_0 == COMMA) :
                LA191_1 = self.input.LA(2)

                if (self.synpred97_Java()) :
                    alt191 = 1




            if alt191 == 1:
                # Java.g:578:42: COMMA formalParameterStandardDecl
                pass 
                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_synpred99_Java7494)
                self._state.following.append(self.FOLLOW_formalParameterStandardDecl_in_synpred99_Java7496)
                self.formalParameterStandardDecl()

                self._state.following.pop()


            else:
                break #loop191


        # Java.g:578:78: ( COMMA formalParameterVarArgDecl )?
        alt192 = 2
        LA192_0 = self.input.LA(1)

        if (LA192_0 == COMMA) :
            alt192 = 1
        if alt192 == 1:
            # Java.g:578:79: COMMA formalParameterVarArgDecl
            pass 
            self.match(self.input, COMMA, self.FOLLOW_COMMA_in_synpred99_Java7501)
            self._state.following.append(self.FOLLOW_formalParameterVarArgDecl_in_synpred99_Java7503)
            self.formalParameterVarArgDecl()

            self._state.following.pop()





    # $ANTLR end "synpred99_Java"



    # $ANTLR start "synpred100_Java"
    def synpred100_Java_fragment(self, ):
        # Java.g:581:13: ( formalParameterVarArgDecl )
        # Java.g:581:13: formalParameterVarArgDecl
        pass 
        self._state.following.append(self.FOLLOW_formalParameterVarArgDecl_in_synpred100_Java7558)
        self.formalParameterVarArgDecl()

        self._state.following.pop()


    # $ANTLR end "synpred100_Java"



    # $ANTLR start "synpred101_Java"
    def synpred101_Java_fragment(self, ):
        # Java.g:602:13: ( DOT ident= IDENT )
        # Java.g:602:13: DOT ident= IDENT
        pass 
        self.match(self.input, DOT, self.FOLLOW_DOT_in_synpred101_Java7789)
        ident=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred101_Java7793)


    # $ANTLR end "synpred101_Java"



    # $ANTLR start "synpred102_Java"
    def synpred102_Java_fragment(self, ):
        # Java.g:609:9: ( annotation )
        # Java.g:609:9: annotation
        pass 
        self._state.following.append(self.FOLLOW_annotation_in_synpred102_Java7842)
        self.annotation()

        self._state.following.pop()


    # $ANTLR end "synpred102_Java"



    # $ANTLR start "synpred114_Java"
    def synpred114_Java_fragment(self, ):
        # Java.g:660:9: ( modifierList type ( IDENT LPAREN RPAREN ( annotationDefaultValue )? SEMI | classFieldDeclaratorList SEMI ) )
        # Java.g:660:9: modifierList type ( IDENT LPAREN RPAREN ( annotationDefaultValue )? SEMI | classFieldDeclaratorList SEMI )
        pass 
        self._state.following.append(self.FOLLOW_modifierList_in_synpred114_Java8264)
        self.modifierList()

        self._state.following.pop()
        self._state.following.append(self.FOLLOW_type_in_synpred114_Java8266)
        self.type()

        self._state.following.pop()
        # Java.g:661:9: ( IDENT LPAREN RPAREN ( annotationDefaultValue )? SEMI | classFieldDeclaratorList SEMI )
        alt197 = 2
        LA197_0 = self.input.LA(1)

        if (LA197_0 == IDENT) :
            LA197_1 = self.input.LA(2)

            if (LA197_1 == LPAREN) :
                alt197 = 1
            elif (LA197_1 == ASSIGN or LA197_1 == COMMA or LA197_1 == LBRACK or LA197_1 == SEMI) :
                alt197 = 2
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 197, 1, self.input)

                raise nvae

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            nvae = NoViableAltException("", 197, 0, self.input)

            raise nvae

        if alt197 == 1:
            # Java.g:661:13: IDENT LPAREN RPAREN ( annotationDefaultValue )? SEMI
            pass 
            self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred114_Java8280)
            self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_synpred114_Java8282)
            self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_synpred114_Java8284)
            # Java.g:661:33: ( annotationDefaultValue )?
            alt196 = 2
            LA196_0 = self.input.LA(1)

            if (LA196_0 == DEFAULT) :
                alt196 = 1
            if alt196 == 1:
                # Java.g:0:0: annotationDefaultValue
                pass 
                self._state.following.append(self.FOLLOW_annotationDefaultValue_in_synpred114_Java8286)
                self.annotationDefaultValue()

                self._state.following.pop()



            self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred114_Java8289)


        elif alt197 == 2:
            # Java.g:663:13: classFieldDeclaratorList SEMI
            pass 
            self._state.following.append(self.FOLLOW_classFieldDeclaratorList_in_synpred114_Java8331)
            self.classFieldDeclaratorList()

            self._state.following.pop()
            self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred114_Java8333)





    # $ANTLR end "synpred114_Java"



    # $ANTLR start "synpred116_Java"
    def synpred116_Java_fragment(self, ):
        # Java.g:681:9: ( localVariableDeclaration SEMI )
        # Java.g:681:9: localVariableDeclaration SEMI
        pass 
        self._state.following.append(self.FOLLOW_localVariableDeclaration_in_synpred116_Java8464)
        self.localVariableDeclaration()

        self._state.following.pop()
        self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred116_Java8466)


    # $ANTLR end "synpred116_Java"



    # $ANTLR start "synpred117_Java"
    def synpred117_Java_fragment(self, ):
        # Java.g:682:9: ( typeDeclaration )
        # Java.g:682:9: typeDeclaration
        pass 
        self._state.following.append(self.FOLLOW_typeDeclaration_in_synpred117_Java8477)
        self.typeDeclaration()

        self._state.following.pop()


    # $ANTLR end "synpred117_Java"



    # $ANTLR start "synpred121_Java"
    def synpred121_Java_fragment(self, ):
        # Java.g:699:13: ( ELSE elseStat= statement )
        # Java.g:699:13: ELSE elseStat= statement
        pass 
        self.match(self.input, ELSE, self.FOLLOW_ELSE_in_synpred121_Java8757)
        self._state.following.append(self.FOLLOW_statement_in_synpred121_Java8761)
        elseStat = self.statement()

        self._state.following.pop()


    # $ANTLR end "synpred121_Java"



    # $ANTLR start "synpred123_Java"
    def synpred123_Java_fragment(self, ):
        # Java.g:703:13: ( forInit SEMI forCondition SEMI forUpdater RPAREN statement )
        # Java.g:703:13: forInit SEMI forCondition SEMI forUpdater RPAREN statement
        pass 
        self._state.following.append(self.FOLLOW_forInit_in_synpred123_Java8940)
        self.forInit()

        self._state.following.pop()
        self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred123_Java8942)
        self._state.following.append(self.FOLLOW_forCondition_in_synpred123_Java8944)
        self.forCondition()

        self._state.following.pop()
        self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred123_Java8946)
        self._state.following.append(self.FOLLOW_forUpdater_in_synpred123_Java8948)
        self.forUpdater()

        self._state.following.pop()
        self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_synpred123_Java8950)
        self._state.following.append(self.FOLLOW_statement_in_synpred123_Java8952)
        self.statement()

        self._state.following.pop()


    # $ANTLR end "synpred123_Java"



    # $ANTLR start "synpred146_Java"
    def synpred146_Java_fragment(self, ):
        # Java.g:756:9: ( localVariableDeclaration )
        # Java.g:756:9: localVariableDeclaration
        pass 
        self._state.following.append(self.FOLLOW_localVariableDeclaration_in_synpred146_Java9964)
        self.localVariableDeclaration()

        self._state.following.pop()


    # $ANTLR end "synpred146_Java"



    # $ANTLR start "synpred147_Java"
    def synpred147_Java_fragment(self, ):
        # Java.g:757:9: ( expressionList )
        # Java.g:757:9: expressionList
        pass 
        self._state.following.append(self.FOLLOW_expressionList_in_synpred147_Java9986)
        self.expressionList()

        self._state.following.pop()


    # $ANTLR end "synpred147_Java"



    # $ANTLR start "synpred190_Java"
    def synpred190_Java_fragment(self, ):
        # Java.g:893:9: ( LPAREN type RPAREN unaryExpression )
        # Java.g:893:9: LPAREN type RPAREN unaryExpression
        pass 
        self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_synpred190_Java11489)
        self._state.following.append(self.FOLLOW_type_in_synpred190_Java11491)
        self.type()

        self._state.following.pop()
        self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_synpred190_Java11493)
        self._state.following.append(self.FOLLOW_unaryExpression_in_synpred190_Java11495)
        self.unaryExpression()

        self._state.following.pop()


    # $ANTLR end "synpred190_Java"



    # $ANTLR start "synpred218_Java"
    def synpred218_Java_fragment(self, ):
        # Java.g:961:13: ( ( arrayDeclarator )+ ( DOT CLASS ) )
        # Java.g:961:13: ( arrayDeclarator )+ ( DOT CLASS )
        pass 
        # Java.g:961:13: ( arrayDeclarator )+
        cnt220 = 0
        while True: #loop220
            alt220 = 2
            LA220_0 = self.input.LA(1)

            if (LA220_0 == LBRACK) :
                alt220 = 1


            if alt220 == 1:
                # Java.g:961:17: arrayDeclarator
                pass 
                self._state.following.append(self.FOLLOW_arrayDeclarator_in_synpred218_Java13346)
                self.arrayDeclarator()

                self._state.following.pop()


            else:
                if cnt220 >= 1:
                    break #loop220

                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                eee = EarlyExitException(220, self.input)
                raise eee

            cnt220 += 1


        # Java.g:963:13: ( DOT CLASS )
        # Java.g:963:17: DOT CLASS
        pass 
        self.match(self.input, DOT, self.FOLLOW_DOT_in_synpred218_Java13413)
        self.match(self.input, CLASS, self.FOLLOW_CLASS_in_synpred218_Java13415)





    # $ANTLR end "synpred218_Java"



    # $ANTLR start "synpred226_Java"
    def synpred226_Java_fragment(self, ):
        # Java.g:966:13: (outerDot= DOT ( CLASS | genericTypeArgumentListSimplified (Super= SUPER arguments | SUPER innerDot= DOT IDENT arguments | IDENT arguments ) | THIS | Super= SUPER arguments | innerNewExpression ) )
        # Java.g:966:13: outerDot= DOT ( CLASS | genericTypeArgumentListSimplified (Super= SUPER arguments | SUPER innerDot= DOT IDENT arguments | IDENT arguments ) | THIS | Super= SUPER arguments | innerNewExpression )
        pass 
        outerDot=self.match(self.input, DOT, self.FOLLOW_DOT_in_synpred226_Java13546)
        # Java.g:967:13: ( CLASS | genericTypeArgumentListSimplified (Super= SUPER arguments | SUPER innerDot= DOT IDENT arguments | IDENT arguments ) | THIS | Super= SUPER arguments | innerNewExpression )
        alt223 = 5
        LA223 = self.input.LA(1)
        if LA223 == CLASS:
            alt223 = 1
        elif LA223 == LESS_THAN:
            alt223 = 2
        elif LA223 == THIS:
            alt223 = 3
        elif LA223 == SUPER:
            alt223 = 4
        elif LA223 == NEW:
            alt223 = 5
        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            nvae = NoViableAltException("", 223, 0, self.input)

            raise nvae

        if alt223 == 1:
            # Java.g:967:17: CLASS
            pass 
            self.match(self.input, CLASS, self.FOLLOW_CLASS_in_synpred226_Java13564)


        elif alt223 == 2:
            # Java.g:968:17: genericTypeArgumentListSimplified (Super= SUPER arguments | SUPER innerDot= DOT IDENT arguments | IDENT arguments )
            pass 
            self._state.following.append(self.FOLLOW_genericTypeArgumentListSimplified_in_synpred226_Java13627)
            self.genericTypeArgumentListSimplified()

            self._state.following.pop()
            # Java.g:969:17: (Super= SUPER arguments | SUPER innerDot= DOT IDENT arguments | IDENT arguments )
            alt222 = 3
            LA222_0 = self.input.LA(1)

            if (LA222_0 == SUPER) :
                LA222_1 = self.input.LA(2)

                if (LA222_1 == DOT) :
                    alt222 = 2
                elif (LA222_1 == LPAREN) :
                    alt222 = 1
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 222, 1, self.input)

                    raise nvae

            elif (LA222_0 == IDENT) :
                alt222 = 3
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 222, 0, self.input)

                raise nvae

            if alt222 == 1:
                # Java.g:969:21: Super= SUPER arguments
                pass 
                Super=self.match(self.input, SUPER, self.FOLLOW_SUPER_in_synpred226_Java13651)
                self._state.following.append(self.FOLLOW_arguments_in_synpred226_Java13653)
                self.arguments()

                self._state.following.pop()


            elif alt222 == 2:
                # Java.g:970:21: SUPER innerDot= DOT IDENT arguments
                pass 
                self.match(self.input, SUPER, self.FOLLOW_SUPER_in_synpred226_Java13703)
                innerDot=self.match(self.input, DOT, self.FOLLOW_DOT_in_synpred226_Java13707)
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred226_Java13709)
                self._state.following.append(self.FOLLOW_arguments_in_synpred226_Java13711)
                self.arguments()

                self._state.following.pop()


            elif alt222 == 3:
                # Java.g:971:21: IDENT arguments
                pass 
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred226_Java13761)
                self._state.following.append(self.FOLLOW_arguments_in_synpred226_Java13763)
                self.arguments()

                self._state.following.pop()





        elif alt223 == 3:
            # Java.g:973:17: THIS
            pass 
            self.match(self.input, THIS, self.FOLLOW_THIS_in_synpred226_Java13838)


        elif alt223 == 4:
            # Java.g:974:17: Super= SUPER arguments
            pass 
            Super=self.match(self.input, SUPER, self.FOLLOW_SUPER_in_synpred226_Java13904)
            self._state.following.append(self.FOLLOW_arguments_in_synpred226_Java13906)
            self.arguments()

            self._state.following.pop()


        elif alt223 == 5:
            # Java.g:975:17: innerNewExpression
            pass 
            self._state.following.append(self.FOLLOW_innerNewExpression_in_synpred226_Java13954)
            self.innerNewExpression()

            self._state.following.pop()





    # $ANTLR end "synpred226_Java"



    # $ANTLR start "synpred234_Java"
    def synpred234_Java_fragment(self, ):
        # Java.g:1000:37: ( LBRACK expression RBRACK )
        # Java.g:1000:37: LBRACK expression RBRACK
        pass 
        self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_synpred234_Java14349)
        self._state.following.append(self.FOLLOW_expression_in_synpred234_Java14352)
        self.expression()

        self._state.following.pop()
        self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_synpred234_Java14354)


    # $ANTLR end "synpred234_Java"




    # Delegated rules

    def synpred226_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred226_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred43_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred43_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred121_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred121_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred76_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred76_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred114_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred114_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred116_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred116_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred97_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred97_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred102_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred102_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred218_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred218_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred117_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred117_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred79_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred79_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred101_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred101_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred16_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred16_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred147_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred147_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred42_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred42_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred190_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred190_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred77_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred77_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred51_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred51_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred100_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred100_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred52_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred52_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred15_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred15_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred123_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred123_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred32_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred32_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred17_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred17_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred92_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred92_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred90_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred90_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred58_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred58_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred50_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred50_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred14_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred14_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred99_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred99_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred234_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred234_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred146_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred146_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred44_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred44_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



    # lookup tables for DFA #36

    DFA36_eot = DFA.unpack(
        u"\27\uffff"
        )

    DFA36_eof = DFA.unpack(
        u"\27\uffff"
        )

    DFA36_min = DFA.unpack(
        u"\1\7\1\uffff\14\0\11\uffff"
        )

    DFA36_max = DFA.unpack(
        u"\1\u00a4\1\uffff\14\0\11\uffff"
        )

    DFA36_accept = DFA.unpack(
        u"\1\uffff\1\1\14\uffff\1\3\3\uffff\1\4\2\uffff\1\5\1\2"
        )

    DFA36_special = DFA.unpack(
        u"\2\uffff\1\0\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\11\1\12\1\13\11"
        u"\uffff"
        )

            
    DFA36_transition = [
        DFA.unpack(u"\1\15\17\uffff\1\1\1\uffff\1\16\22\uffff\1\25\10\uffff"
        u"\1\6\1\uffff\1\16\1\uffff\1\16\2\uffff\1\16\1\22\3\uffff\1\16\1"
        u"\uffff\1\22\2\uffff\1\14\1\uffff\1\16\4\uffff\1\22\1\uffff\2\16"
        u"\1\7\3\uffff\1\5\1\4\1\3\1\uffff\1\16\1\2\1\13\2\uffff\1\10\3\uffff"
        u"\1\11\2\uffff\1\16\1\12\75\uffff\1\16"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #36

    class DFA36(DFA):
        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA36_2 = input.LA(1)

                 
                index36_2 = input.index()
                input.rewind()
                s = -1
                if (self.synpred32_Java()):
                    s = 22

                elif (self.synpred43_Java()):
                    s = 14

                elif (self.synpred44_Java()):
                    s = 18

                 
                input.seek(index36_2)
                if s >= 0:
                    return s
            elif s == 1: 
                LA36_3 = input.LA(1)

                 
                index36_3 = input.index()
                input.rewind()
                s = -1
                if (self.synpred43_Java()):
                    s = 14

                elif (self.synpred44_Java()):
                    s = 18

                 
                input.seek(index36_3)
                if s >= 0:
                    return s
            elif s == 2: 
                LA36_4 = input.LA(1)

                 
                index36_4 = input.index()
                input.rewind()
                s = -1
                if (self.synpred43_Java()):
                    s = 14

                elif (self.synpred44_Java()):
                    s = 18

                 
                input.seek(index36_4)
                if s >= 0:
                    return s
            elif s == 3: 
                LA36_5 = input.LA(1)

                 
                index36_5 = input.index()
                input.rewind()
                s = -1
                if (self.synpred43_Java()):
                    s = 14

                elif (self.synpred44_Java()):
                    s = 18

                 
                input.seek(index36_5)
                if s >= 0:
                    return s
            elif s == 4: 
                LA36_6 = input.LA(1)

                 
                index36_6 = input.index()
                input.rewind()
                s = -1
                if (self.synpred43_Java()):
                    s = 14

                elif (self.synpred44_Java()):
                    s = 18

                 
                input.seek(index36_6)
                if s >= 0:
                    return s
            elif s == 5: 
                LA36_7 = input.LA(1)

                 
                index36_7 = input.index()
                input.rewind()
                s = -1
                if (self.synpred43_Java()):
                    s = 14

                elif (self.synpred44_Java()):
                    s = 18

                 
                input.seek(index36_7)
                if s >= 0:
                    return s
            elif s == 6: 
                LA36_8 = input.LA(1)

                 
                index36_8 = input.index()
                input.rewind()
                s = -1
                if (self.synpred43_Java()):
                    s = 14

                elif (self.synpred44_Java()):
                    s = 18

                 
                input.seek(index36_8)
                if s >= 0:
                    return s
            elif s == 7: 
                LA36_9 = input.LA(1)

                 
                index36_9 = input.index()
                input.rewind()
                s = -1
                if (self.synpred43_Java()):
                    s = 14

                elif (self.synpred44_Java()):
                    s = 18

                 
                input.seek(index36_9)
                if s >= 0:
                    return s
            elif s == 8: 
                LA36_10 = input.LA(1)

                 
                index36_10 = input.index()
                input.rewind()
                s = -1
                if (self.synpred43_Java()):
                    s = 14

                elif (self.synpred44_Java()):
                    s = 18

                 
                input.seek(index36_10)
                if s >= 0:
                    return s
            elif s == 9: 
                LA36_11 = input.LA(1)

                 
                index36_11 = input.index()
                input.rewind()
                s = -1
                if (self.synpred43_Java()):
                    s = 14

                elif (self.synpred44_Java()):
                    s = 18

                 
                input.seek(index36_11)
                if s >= 0:
                    return s
            elif s == 10: 
                LA36_12 = input.LA(1)

                 
                index36_12 = input.index()
                input.rewind()
                s = -1
                if (self.synpred43_Java()):
                    s = 14

                elif (self.synpred44_Java()):
                    s = 18

                 
                input.seek(index36_12)
                if s >= 0:
                    return s
            elif s == 11: 
                LA36_13 = input.LA(1)

                 
                index36_13 = input.index()
                input.rewind()
                s = -1
                if (self.synpred43_Java()):
                    s = 14

                elif (self.synpred44_Java()):
                    s = 18

                 
                input.seek(index36_13)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 36, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #43

    DFA43_eot = DFA.unpack(
        u"\25\uffff"
        )

    DFA43_eof = DFA.unpack(
        u"\25\uffff"
        )

    DFA43_min = DFA.unpack(
        u"\1\7\14\0\10\uffff"
        )

    DFA43_max = DFA.unpack(
        u"\1\u00a4\14\0\10\uffff"
        )

    DFA43_accept = DFA.unpack(
        u"\15\uffff\1\1\3\uffff\1\2\2\uffff\1\3"
        )

    DFA43_special = DFA.unpack(
        u"\1\uffff\1\0\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\11\1\12\1\13\10"
        u"\uffff"
        )

            
    DFA43_transition = [
        DFA.unpack(u"\1\14\21\uffff\1\15\22\uffff\1\24\10\uffff\1\5\1\uffff"
        u"\1\15\1\uffff\1\15\2\uffff\1\15\1\21\3\uffff\1\15\1\uffff\1\21"
        u"\2\uffff\1\13\1\uffff\1\15\4\uffff\1\21\1\uffff\2\15\1\6\3\uffff"
        u"\1\3\1\2\1\1\1\uffff\1\15\1\4\1\12\2\uffff\1\7\3\uffff\1\10\2\uffff"
        u"\1\15\1\11\75\uffff\1\15"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #43

    class DFA43(DFA):
        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA43_1 = input.LA(1)

                 
                index43_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred51_Java()):
                    s = 13

                elif (self.synpred52_Java()):
                    s = 17

                 
                input.seek(index43_1)
                if s >= 0:
                    return s
            elif s == 1: 
                LA43_2 = input.LA(1)

                 
                index43_2 = input.index()
                input.rewind()
                s = -1
                if (self.synpred51_Java()):
                    s = 13

                elif (self.synpred52_Java()):
                    s = 17

                 
                input.seek(index43_2)
                if s >= 0:
                    return s
            elif s == 2: 
                LA43_3 = input.LA(1)

                 
                index43_3 = input.index()
                input.rewind()
                s = -1
                if (self.synpred51_Java()):
                    s = 13

                elif (self.synpred52_Java()):
                    s = 17

                 
                input.seek(index43_3)
                if s >= 0:
                    return s
            elif s == 3: 
                LA43_4 = input.LA(1)

                 
                index43_4 = input.index()
                input.rewind()
                s = -1
                if (self.synpred51_Java()):
                    s = 13

                elif (self.synpred52_Java()):
                    s = 17

                 
                input.seek(index43_4)
                if s >= 0:
                    return s
            elif s == 4: 
                LA43_5 = input.LA(1)

                 
                index43_5 = input.index()
                input.rewind()
                s = -1
                if (self.synpred51_Java()):
                    s = 13

                elif (self.synpred52_Java()):
                    s = 17

                 
                input.seek(index43_5)
                if s >= 0:
                    return s
            elif s == 5: 
                LA43_6 = input.LA(1)

                 
                index43_6 = input.index()
                input.rewind()
                s = -1
                if (self.synpred51_Java()):
                    s = 13

                elif (self.synpred52_Java()):
                    s = 17

                 
                input.seek(index43_6)
                if s >= 0:
                    return s
            elif s == 6: 
                LA43_7 = input.LA(1)

                 
                index43_7 = input.index()
                input.rewind()
                s = -1
                if (self.synpred51_Java()):
                    s = 13

                elif (self.synpred52_Java()):
                    s = 17

                 
                input.seek(index43_7)
                if s >= 0:
                    return s
            elif s == 7: 
                LA43_8 = input.LA(1)

                 
                index43_8 = input.index()
                input.rewind()
                s = -1
                if (self.synpred51_Java()):
                    s = 13

                elif (self.synpred52_Java()):
                    s = 17

                 
                input.seek(index43_8)
                if s >= 0:
                    return s
            elif s == 8: 
                LA43_9 = input.LA(1)

                 
                index43_9 = input.index()
                input.rewind()
                s = -1
                if (self.synpred51_Java()):
                    s = 13

                elif (self.synpred52_Java()):
                    s = 17

                 
                input.seek(index43_9)
                if s >= 0:
                    return s
            elif s == 9: 
                LA43_10 = input.LA(1)

                 
                index43_10 = input.index()
                input.rewind()
                s = -1
                if (self.synpred51_Java()):
                    s = 13

                elif (self.synpred52_Java()):
                    s = 17

                 
                input.seek(index43_10)
                if s >= 0:
                    return s
            elif s == 10: 
                LA43_11 = input.LA(1)

                 
                index43_11 = input.index()
                input.rewind()
                s = -1
                if (self.synpred51_Java()):
                    s = 13

                elif (self.synpred52_Java()):
                    s = 17

                 
                input.seek(index43_11)
                if s >= 0:
                    return s
            elif s == 11: 
                LA43_12 = input.LA(1)

                 
                index43_12 = input.index()
                input.rewind()
                s = -1
                if (self.synpred51_Java()):
                    s = 13

                elif (self.synpred52_Java()):
                    s = 17

                 
                input.seek(index43_12)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 43, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #86

    DFA86_eot = DFA.unpack(
        u"\22\uffff"
        )

    DFA86_eof = DFA.unpack(
        u"\22\uffff"
        )

    DFA86_min = DFA.unpack(
        u"\1\7\14\0\5\uffff"
        )

    DFA86_max = DFA.unpack(
        u"\1\u00a4\14\0\5\uffff"
        )

    DFA86_accept = DFA.unpack(
        u"\15\uffff\1\1\1\uffff\1\2\2\uffff"
        )

    DFA86_special = DFA.unpack(
        u"\1\uffff\1\0\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\11\1\12\1\13\5"
        u"\uffff"
        )

            
    DFA86_transition = [
        DFA.unpack(u"\1\14\55\uffff\1\5\1\uffff\1\15\1\uffff\1\15\2\uffff"
        u"\1\15\1\17\3\uffff\1\15\1\uffff\1\17\2\uffff\1\13\1\uffff\1\15"
        u"\4\uffff\1\17\1\uffff\2\15\1\6\3\uffff\1\3\1\2\1\1\1\uffff\1\15"
        u"\1\4\1\12\2\uffff\1\7\3\uffff\1\10\3\uffff\1\11\75\uffff\1\15"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #86

    class DFA86(DFA):
        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA86_1 = input.LA(1)

                 
                index86_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred114_Java()):
                    s = 13

                elif (True):
                    s = 15

                 
                input.seek(index86_1)
                if s >= 0:
                    return s
            elif s == 1: 
                LA86_2 = input.LA(1)

                 
                index86_2 = input.index()
                input.rewind()
                s = -1
                if (self.synpred114_Java()):
                    s = 13

                elif (True):
                    s = 15

                 
                input.seek(index86_2)
                if s >= 0:
                    return s
            elif s == 2: 
                LA86_3 = input.LA(1)

                 
                index86_3 = input.index()
                input.rewind()
                s = -1
                if (self.synpred114_Java()):
                    s = 13

                elif (True):
                    s = 15

                 
                input.seek(index86_3)
                if s >= 0:
                    return s
            elif s == 3: 
                LA86_4 = input.LA(1)

                 
                index86_4 = input.index()
                input.rewind()
                s = -1
                if (self.synpred114_Java()):
                    s = 13

                elif (True):
                    s = 15

                 
                input.seek(index86_4)
                if s >= 0:
                    return s
            elif s == 4: 
                LA86_5 = input.LA(1)

                 
                index86_5 = input.index()
                input.rewind()
                s = -1
                if (self.synpred114_Java()):
                    s = 13

                elif (True):
                    s = 15

                 
                input.seek(index86_5)
                if s >= 0:
                    return s
            elif s == 5: 
                LA86_6 = input.LA(1)

                 
                index86_6 = input.index()
                input.rewind()
                s = -1
                if (self.synpred114_Java()):
                    s = 13

                elif (True):
                    s = 15

                 
                input.seek(index86_6)
                if s >= 0:
                    return s
            elif s == 6: 
                LA86_7 = input.LA(1)

                 
                index86_7 = input.index()
                input.rewind()
                s = -1
                if (self.synpred114_Java()):
                    s = 13

                elif (True):
                    s = 15

                 
                input.seek(index86_7)
                if s >= 0:
                    return s
            elif s == 7: 
                LA86_8 = input.LA(1)

                 
                index86_8 = input.index()
                input.rewind()
                s = -1
                if (self.synpred114_Java()):
                    s = 13

                elif (True):
                    s = 15

                 
                input.seek(index86_8)
                if s >= 0:
                    return s
            elif s == 8: 
                LA86_9 = input.LA(1)

                 
                index86_9 = input.index()
                input.rewind()
                s = -1
                if (self.synpred114_Java()):
                    s = 13

                elif (True):
                    s = 15

                 
                input.seek(index86_9)
                if s >= 0:
                    return s
            elif s == 9: 
                LA86_10 = input.LA(1)

                 
                index86_10 = input.index()
                input.rewind()
                s = -1
                if (self.synpred114_Java()):
                    s = 13

                elif (True):
                    s = 15

                 
                input.seek(index86_10)
                if s >= 0:
                    return s
            elif s == 10: 
                LA86_11 = input.LA(1)

                 
                index86_11 = input.index()
                input.rewind()
                s = -1
                if (self.synpred114_Java()):
                    s = 13

                elif (True):
                    s = 15

                 
                input.seek(index86_11)
                if s >= 0:
                    return s
            elif s == 11: 
                LA86_12 = input.LA(1)

                 
                index86_12 = input.index()
                input.rewind()
                s = -1
                if (self.synpred114_Java()):
                    s = 13

                elif (True):
                    s = 15

                 
                input.seek(index86_12)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 86, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #88

    DFA88_eot = DFA.unpack(
        u"\55\uffff"
        )

    DFA88_eof = DFA.unpack(
        u"\55\uffff"
        )

    DFA88_min = DFA.unpack(
        u"\1\7\4\0\6\uffff\1\0\41\uffff"
        )

    DFA88_max = DFA.unpack(
        u"\1\u00aa\4\0\6\uffff\1\0\41\uffff"
        )

    DFA88_accept = DFA.unpack(
        u"\5\uffff\1\2\14\uffff\1\3\31\uffff\1\1"
        )

    DFA88_special = DFA.unpack(
        u"\1\uffff\1\0\1\1\1\2\1\3\6\uffff\1\4\41\uffff"
        )

            
    DFA88_transition = [
        DFA.unpack(u"\1\2\4\uffff\1\22\10\uffff\1\22\1\uffff\1\22\1\uffff"
        u"\1\22\1\uffff\1\22\1\uffff\2\22\3\uffff\1\22\3\uffff\1\22\5\uffff"
        u"\1\22\10\uffff\1\5\1\22\1\3\1\22\1\3\2\uffff\1\3\1\5\1\22\1\uffff"
        u"\1\22\1\3\1\uffff\1\5\1\uffff\1\22\1\1\1\uffff\1\3\2\22\2\uffff"
        u"\1\5\1\uffff\2\3\1\5\2\22\1\uffff\3\5\1\22\1\3\2\5\2\22\1\13\2"
        u"\22\1\uffff\1\5\3\22\1\5\1\22\74\uffff\1\4\6\22"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #88

    class DFA88(DFA):
        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA88_1 = input.LA(1)

                 
                index88_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred116_Java()):
                    s = 44

                elif (self.synpred117_Java()):
                    s = 5

                 
                input.seek(index88_1)
                if s >= 0:
                    return s
            elif s == 1: 
                LA88_2 = input.LA(1)

                 
                index88_2 = input.index()
                input.rewind()
                s = -1
                if (self.synpred116_Java()):
                    s = 44

                elif (self.synpred117_Java()):
                    s = 5

                 
                input.seek(index88_2)
                if s >= 0:
                    return s
            elif s == 2: 
                LA88_3 = input.LA(1)

                 
                index88_3 = input.index()
                input.rewind()
                s = -1
                if (self.synpred116_Java()):
                    s = 44

                elif (True):
                    s = 18

                 
                input.seek(index88_3)
                if s >= 0:
                    return s
            elif s == 3: 
                LA88_4 = input.LA(1)

                 
                index88_4 = input.index()
                input.rewind()
                s = -1
                if (self.synpred116_Java()):
                    s = 44

                elif (True):
                    s = 18

                 
                input.seek(index88_4)
                if s >= 0:
                    return s
            elif s == 4: 
                LA88_11 = input.LA(1)

                 
                index88_11 = input.index()
                input.rewind()
                s = -1
                if (self.synpred117_Java()):
                    s = 5

                elif (True):
                    s = 18

                 
                input.seek(index88_11)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 88, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #97

    DFA97_eot = DFA.unpack(
        u"\22\uffff"
        )

    DFA97_eof = DFA.unpack(
        u"\22\uffff"
        )

    DFA97_min = DFA.unpack(
        u"\1\14\15\uffff\1\4\3\uffff"
        )

    DFA97_max = DFA.unpack(
        u"\1\u00aa\15\uffff\1\114\3\uffff"
        )

    DFA97_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\11\1\12\1\13\1\14\1"
        u"\15\1\uffff\1\17\1\20\1\16"
        )

    DFA97_special = DFA.unpack(
        u"\22\uffff"
        )

            
    DFA97_transition = [
        DFA.unpack(u"\1\17\10\uffff\1\17\1\uffff\1\1\1\uffff\1\17\1\uffff"
        u"\1\17\1\uffff\2\17\3\uffff\1\17\3\uffff\1\17\5\uffff\1\20\11\uffff"
        u"\1\2\1\17\1\14\1\17\2\uffff\1\17\1\uffff\1\15\1\uffff\1\6\1\17"
        u"\3\uffff\1\17\2\uffff\1\17\1\4\1\3\4\uffff\2\17\1\uffff\2\17\4"
        u"\uffff\1\12\1\17\2\uffff\1\17\1\10\1\11\1\17\1\13\2\uffff\1\17"
        u"\1\7\1\17\1\uffff\1\5\74\uffff\1\16\6\17"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\3\17\1\uffff\2\17\1\21\1\uffff\4\17\2\uffff\5\17\1"
        u"\uffff\3\17\1\uffff\6\17\1\uffff\6\17\3\uffff\11\17\27\uffff\1"
        u"\17"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #97

    DFA97 = DFA
    # lookup tables for DFA #91

    DFA91_eot = DFA.unpack(
        u"\24\uffff"
        )

    DFA91_eof = DFA.unpack(
        u"\24\uffff"
        )

    DFA91_min = DFA.unpack(
        u"\1\7\4\0\17\uffff"
        )

    DFA91_max = DFA.unpack(
        u"\1\u00aa\4\0\17\uffff"
        )

    DFA91_accept = DFA.unpack(
        u"\5\uffff\1\1\15\uffff\1\2"
        )

    DFA91_special = DFA.unpack(
        u"\1\uffff\1\0\1\1\1\2\1\3\17\uffff"
        )

            
    DFA91_transition = [
        DFA.unpack(u"\1\2\4\uffff\1\5\10\uffff\1\5\3\uffff\1\5\1\uffff\1"
        u"\5\1\uffff\2\5\3\uffff\1\5\3\uffff\1\5\5\uffff\1\5\12\uffff\1\3"
        u"\1\uffff\1\3\2\uffff\1\3\4\uffff\1\3\3\uffff\1\5\1\1\1\uffff\1"
        u"\3\6\uffff\2\3\1\uffff\2\5\5\uffff\1\3\2\uffff\1\5\2\uffff\1\5"
        u"\3\uffff\1\5\1\uffff\1\5\76\uffff\1\4\6\5"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #91

    class DFA91(DFA):
        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA91_1 = input.LA(1)

                 
                index91_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred123_Java()):
                    s = 5

                elif (True):
                    s = 19

                 
                input.seek(index91_1)
                if s >= 0:
                    return s
            elif s == 1: 
                LA91_2 = input.LA(1)

                 
                index91_2 = input.index()
                input.rewind()
                s = -1
                if (self.synpred123_Java()):
                    s = 5

                elif (True):
                    s = 19

                 
                input.seek(index91_2)
                if s >= 0:
                    return s
            elif s == 2: 
                LA91_3 = input.LA(1)

                 
                index91_3 = input.index()
                input.rewind()
                s = -1
                if (self.synpred123_Java()):
                    s = 5

                elif (True):
                    s = 19

                 
                input.seek(index91_3)
                if s >= 0:
                    return s
            elif s == 3: 
                LA91_4 = input.LA(1)

                 
                index91_4 = input.index()
                input.rewind()
                s = -1
                if (self.synpred123_Java()):
                    s = 5

                elif (True):
                    s = 19

                 
                input.seek(index91_4)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 91, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #103

    DFA103_eot = DFA.unpack(
        u"\23\uffff"
        )

    DFA103_eof = DFA.unpack(
        u"\23\uffff"
        )

    DFA103_min = DFA.unpack(
        u"\1\7\2\uffff\2\0\16\uffff"
        )

    DFA103_max = DFA.unpack(
        u"\1\u00aa\2\uffff\2\0\16\uffff"
        )

    DFA103_accept = DFA.unpack(
        u"\1\uffff\1\1\3\uffff\1\2\14\uffff\1\3"
        )

    DFA103_special = DFA.unpack(
        u"\3\uffff\1\0\1\1\16\uffff"
        )

            
    DFA103_transition = [
        DFA.unpack(u"\1\1\4\uffff\1\5\10\uffff\1\5\3\uffff\1\5\1\uffff\1"
        u"\5\1\uffff\2\5\3\uffff\1\5\3\uffff\1\5\5\uffff\1\22\12\uffff\1"
        u"\3\1\uffff\1\3\2\uffff\1\3\4\uffff\1\3\3\uffff\1\5\1\1\1\uffff"
        u"\1\3\6\uffff\2\3\1\uffff\2\5\5\uffff\1\3\2\uffff\1\5\2\uffff\1"
        u"\5\3\uffff\1\5\1\uffff\1\5\76\uffff\1\4\6\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #103

    class DFA103(DFA):
        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA103_3 = input.LA(1)

                 
                index103_3 = input.index()
                input.rewind()
                s = -1
                if (self.synpred146_Java()):
                    s = 1

                elif (self.synpred147_Java()):
                    s = 5

                 
                input.seek(index103_3)
                if s >= 0:
                    return s
            elif s == 1: 
                LA103_4 = input.LA(1)

                 
                index103_4 = input.index()
                input.rewind()
                s = -1
                if (self.synpred146_Java()):
                    s = 1

                elif (self.synpred147_Java()):
                    s = 5

                 
                input.seek(index103_4)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 103, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #127

    DFA127_eot = DFA.unpack(
        u"\15\uffff"
        )

    DFA127_eof = DFA.unpack(
        u"\15\uffff"
        )

    DFA127_min = DFA.unpack(
        u"\1\31\2\uffff\1\0\11\uffff"
        )

    DFA127_max = DFA.unpack(
        u"\1\u00aa\2\uffff\1\0\11\uffff"
        )

    DFA127_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\uffff\1\4\7\uffff\1\3"
        )

    DFA127_special = DFA.unpack(
        u"\3\uffff\1\0\11\uffff"
        )

            
    DFA127_transition = [
        DFA.unpack(u"\1\4\1\uffff\1\2\1\uffff\1\3\4\uffff\1\1\24\uffff\1"
        u"\4\1\uffff\1\4\2\uffff\1\4\4\uffff\1\4\3\uffff\1\4\2\uffff\1\4"
        u"\6\uffff\2\4\1\uffff\2\4\5\uffff\1\4\2\uffff\1\4\2\uffff\1\4\3"
        u"\uffff\1\4\1\uffff\1\4\76\uffff\7\4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #127

    class DFA127(DFA):
        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA127_3 = input.LA(1)

                 
                index127_3 = input.index()
                input.rewind()
                s = -1
                if (self.synpred190_Java()):
                    s = 12

                elif (True):
                    s = 4

                 
                input.seek(index127_3)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 127, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #139

    DFA139_eot = DFA.unpack(
        u"\14\uffff"
        )

    DFA139_eof = DFA.unpack(
        u"\14\uffff"
        )

    DFA139_min = DFA.unpack(
        u"\1\31\6\uffff\1\17\4\uffff"
        )

    DFA139_max = DFA.unpack(
        u"\1\u00aa\6\uffff\1\35\4\uffff"
        )

    DFA139_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\4\1\5\1\6\1\uffff\1\11\1\12\1\10\1\7"
        )

    DFA139_special = DFA.unpack(
        u"\14\uffff"
        )

            
    DFA139_transition = [
        DFA.unpack(u"\1\5\3\uffff\1\1\31\uffff\1\10\1\uffff\1\10\2\uffff"
        u"\1\10\4\uffff\1\10\3\uffff\1\2\2\uffff\1\10\6\uffff\2\10\1\uffff"
        u"\1\3\1\2\5\uffff\1\10\2\uffff\1\7\2\uffff\1\6\3\uffff\1\2\1\uffff"
        u"\1\11\76\uffff\1\4\6\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\12\15\uffff\1\13"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #139

    DFA139 = DFA
    # lookup tables for DFA #143

    DFA143_eot = DFA.unpack(
        u"\60\uffff"
        )

    DFA143_eof = DFA.unpack(
        u"\1\4\57\uffff"
        )

    DFA143_min = DFA.unpack(
        u"\1\4\1\0\1\uffff\1\0\54\uffff"
        )

    DFA143_max = DFA.unpack(
        u"\1\114\1\0\1\uffff\1\0\54\uffff"
        )

    DFA143_accept = DFA.unpack(
        u"\2\uffff\1\2\1\uffff\1\4\51\uffff\1\1\1\3"
        )

    DFA143_special = DFA.unpack(
        u"\1\uffff\1\0\1\uffff\1\1\54\uffff"
        )

            
    DFA143_transition = [
        DFA.unpack(u"\3\4\1\uffff\7\4\1\3\2\uffff\4\4\1\1\1\uffff\3\4\1\uffff"
        u"\1\4\1\2\4\4\1\uffff\22\4\27\uffff\1\4"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #143

    class DFA143(DFA):
        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA143_1 = input.LA(1)

                 
                index143_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred218_Java()):
                    s = 46

                elif (True):
                    s = 4

                 
                input.seek(index143_1)
                if s >= 0:
                    return s
            elif s == 1: 
                LA143_3 = input.LA(1)

                 
                index143_3 = input.index()
                input.rewind()
                s = -1
                if (self.synpred226_Java()):
                    s = 47

                elif (True):
                    s = 4

                 
                input.seek(index143_3)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 143, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #150

    DFA150_eot = DFA.unpack(
        u"\56\uffff"
        )

    DFA150_eof = DFA.unpack(
        u"\1\2\55\uffff"
        )

    DFA150_min = DFA.unpack(
        u"\1\4\1\0\54\uffff"
        )

    DFA150_max = DFA.unpack(
        u"\1\114\1\0\54\uffff"
        )

    DFA150_accept = DFA.unpack(
        u"\2\uffff\1\2\52\uffff\1\1"
        )

    DFA150_special = DFA.unpack(
        u"\1\uffff\1\0\54\uffff"
        )

            
    DFA150_transition = [
        DFA.unpack(u"\3\2\1\uffff\10\2\2\uffff\4\2\1\1\1\uffff\3\2\1\uffff"
        u"\1\2\1\uffff\4\2\1\uffff\22\2\27\uffff\1\2"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #150

    class DFA150(DFA):
        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA150_1 = input.LA(1)

                 
                index150_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred234_Java()):
                    s = 45

                elif (True):
                    s = 2

                 
                input.seek(index150_1)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 150, _s, input)
            self_.error(nvae)
            raise nvae
 

    FOLLOW_compilationUnit_in_javaSource4499 = frozenset([1])
    FOLLOW_annotationList_in_compilationUnit4535 = frozenset([1, 7, 44, 53, 61, 67, 70, 77, 78, 81, 84, 85, 86, 87, 90, 91, 94, 98, 102])
    FOLLOW_packageDeclaration_in_compilationUnit4545 = frozenset([1, 7, 44, 53, 61, 67, 70, 77, 78, 81, 85, 86, 87, 90, 91, 94, 98, 102])
    FOLLOW_importDeclaration_in_compilationUnit4556 = frozenset([1, 7, 44, 53, 61, 67, 70, 77, 78, 81, 85, 86, 87, 90, 91, 94, 98, 102])
    FOLLOW_typeDecls_in_compilationUnit4567 = frozenset([1, 7, 44, 53, 61, 67, 70, 77, 81, 85, 86, 87, 90, 91, 94, 98, 102])
    FOLLOW_typeDeclaration_in_typeDecls4587 = frozenset([1])
    FOLLOW_SEMI_in_typeDecls4597 = frozenset([1])
    FOLLOW_PACKAGE_in_packageDeclaration4617 = frozenset([164])
    FOLLOW_qualifiedIdentifier_in_packageDeclaration4620 = frozenset([44])
    FOLLOW_SEMI_in_packageDeclaration4622 = frozenset([1])
    FOLLOW_IMPORT_in_importDeclaration4642 = frozenset([90, 164])
    FOLLOW_STATIC_in_importDeclaration4645 = frozenset([164])
    FOLLOW_qualifiedIdentifier_in_importDeclaration4648 = frozenset([16, 44])
    FOLLOW_DOTSTAR_in_importDeclaration4650 = frozenset([44])
    FOLLOW_SEMI_in_importDeclaration4653 = frozenset([1])
    FOLLOW_modifierList_in_typeDeclaration4673 = frozenset([7, 53, 61, 67, 70, 77, 81, 85, 86, 87, 90, 91, 94, 98, 102])
    FOLLOW_classTypeDeclaration_in_typeDeclaration4688 = frozenset([1])
    FOLLOW_interfaceTypeDeclaration_in_typeDeclaration4703 = frozenset([1])
    FOLLOW_enumTypeDeclaration_in_typeDeclaration4718 = frozenset([1])
    FOLLOW_annotationTypeDeclaration_in_typeDeclaration4733 = frozenset([1])
    FOLLOW_CLASS_in_classTypeDeclaration4764 = frozenset([164])
    FOLLOW_IDENT_in_classTypeDeclaration4766 = frozenset([23, 25, 68, 75])
    FOLLOW_genericTypeParameterList_in_classTypeDeclaration4768 = frozenset([23, 25, 68, 75])
    FOLLOW_classExtendsClause_in_classTypeDeclaration4771 = frozenset([23, 25, 68, 75])
    FOLLOW_implementsClause_in_classTypeDeclaration4774 = frozenset([23, 25, 68, 75])
    FOLLOW_classBody_in_classTypeDeclaration4777 = frozenset([1])
    FOLLOW_EXTENDS_in_classExtendsClause4826 = frozenset([55, 57, 60, 65, 72, 79, 80, 89, 164])
    FOLLOW_type_in_classExtendsClause4828 = frozenset([1])
    FOLLOW_EXTENDS_in_interfaceExtendsClause4865 = frozenset([55, 57, 60, 65, 72, 79, 80, 89, 164])
    FOLLOW_typeList_in_interfaceExtendsClause4867 = frozenset([1])
    FOLLOW_IMPLEMENTS_in_implementsClause4904 = frozenset([55, 57, 60, 65, 72, 79, 80, 89, 164])
    FOLLOW_typeList_in_implementsClause4906 = frozenset([1])
    FOLLOW_LESS_THAN_in_genericTypeParameterList4943 = frozenset([164])
    FOLLOW_genericTypeParameter_in_genericTypeParameterList4945 = frozenset([8, 11, 20, 47])
    FOLLOW_COMMA_in_genericTypeParameterList4948 = frozenset([164])
    FOLLOW_genericTypeParameter_in_genericTypeParameterList4950 = frozenset([8, 11, 20, 47])
    FOLLOW_genericTypeListClosing_in_genericTypeParameterList4954 = frozenset([1])
    FOLLOW_GREATER_THAN_in_genericTypeListClosing5069 = frozenset([1])
    FOLLOW_SHIFT_RIGHT_in_genericTypeListClosing5079 = frozenset([1])
    FOLLOW_BIT_SHIFT_RIGHT_in_genericTypeListClosing5089 = frozenset([1])
    FOLLOW_IDENT_in_genericTypeParameter5117 = frozenset([1, 68])
    FOLLOW_bound_in_genericTypeParameter5119 = frozenset([1])
    FOLLOW_EXTENDS_in_bound5157 = frozenset([55, 57, 60, 65, 72, 79, 80, 89, 164])
    FOLLOW_type_in_bound5159 = frozenset([1, 4])
    FOLLOW_AND_in_bound5162 = frozenset([55, 57, 60, 65, 72, 79, 80, 89, 164])
    FOLLOW_type_in_bound5164 = frozenset([1, 4])
    FOLLOW_ENUM_in_enumTypeDeclaration5205 = frozenset([164])
    FOLLOW_IDENT_in_enumTypeDeclaration5207 = frozenset([23, 75])
    FOLLOW_implementsClause_in_enumTypeDeclaration5209 = frozenset([23, 75])
    FOLLOW_enumBody_in_enumTypeDeclaration5212 = frozenset([1])
    FOLLOW_LCURLY_in_enumBody5255 = frozenset([7, 53, 70, 81, 85, 86, 87, 90, 91, 94, 98, 102, 164])
    FOLLOW_enumScopeDeclarations_in_enumBody5257 = frozenset([42])
    FOLLOW_RCURLY_in_enumBody5259 = frozenset([1])
    FOLLOW_enumConstants_in_enumScopeDeclarations5296 = frozenset([1, 11, 44])
    FOLLOW_COMMA_in_enumScopeDeclarations5299 = frozenset([1, 44])
    FOLLOW_enumClassScopeDeclarations_in_enumScopeDeclarations5304 = frozenset([1])
    FOLLOW_SEMI_in_enumClassScopeDeclarations5324 = frozenset([1, 7, 23, 25, 44, 53, 55, 57, 60, 61, 65, 67, 70, 72, 77, 79, 80, 81, 85, 86, 87, 89, 90, 91, 94, 98, 101, 102, 164])
    FOLLOW_classScopeDeclarations_in_enumClassScopeDeclarations5326 = frozenset([1, 7, 23, 25, 44, 53, 55, 57, 60, 61, 65, 67, 70, 72, 77, 79, 80, 81, 85, 86, 87, 89, 90, 91, 94, 98, 101, 102, 164])
    FOLLOW_enumConstant_in_enumConstants5365 = frozenset([1, 11])
    FOLLOW_COMMA_in_enumConstants5368 = frozenset([7, 53, 70, 81, 85, 86, 87, 90, 91, 94, 98, 102, 164])
    FOLLOW_enumConstant_in_enumConstants5371 = frozenset([1, 11])
    FOLLOW_annotationList_in_enumConstant5392 = frozenset([164])
    FOLLOW_IDENT_in_enumConstant5394 = frozenset([1, 23, 25, 29, 68, 75])
    FOLLOW_arguments_in_enumConstant5397 = frozenset([1, 23, 25, 68, 75])
    FOLLOW_classBody_in_enumConstant5400 = frozenset([1])
    FOLLOW_INTERFACE_in_interfaceTypeDeclaration5421 = frozenset([164])
    FOLLOW_IDENT_in_interfaceTypeDeclaration5423 = frozenset([23, 25, 68])
    FOLLOW_genericTypeParameterList_in_interfaceTypeDeclaration5425 = frozenset([23, 25, 68])
    FOLLOW_interfaceExtendsClause_in_interfaceTypeDeclaration5428 = frozenset([23, 25, 68])
    FOLLOW_interfaceBody_in_interfaceTypeDeclaration5431 = frozenset([1])
    FOLLOW_type_in_typeList5477 = frozenset([1, 11])
    FOLLOW_COMMA_in_typeList5480 = frozenset([55, 57, 60, 65, 72, 79, 80, 89, 164])
    FOLLOW_type_in_typeList5483 = frozenset([1, 11])
    FOLLOW_LCURLY_in_classBody5504 = frozenset([7, 23, 25, 42, 44, 53, 55, 57, 60, 61, 65, 67, 70, 72, 77, 79, 80, 81, 85, 86, 87, 89, 90, 91, 94, 98, 101, 102, 164])
    FOLLOW_classScopeDeclarations_in_classBody5506 = frozenset([7, 23, 25, 42, 44, 53, 55, 57, 60, 61, 65, 67, 70, 72, 77, 79, 80, 81, 85, 86, 87, 89, 90, 91, 94, 98, 101, 102, 164])
    FOLLOW_RCURLY_in_classBody5509 = frozenset([1])
    FOLLOW_LCURLY_in_interfaceBody5547 = frozenset([7, 25, 42, 44, 53, 55, 57, 60, 61, 65, 67, 70, 72, 77, 79, 80, 81, 85, 86, 87, 89, 90, 91, 94, 98, 101, 102, 164])
    FOLLOW_interfaceScopeDeclarations_in_interfaceBody5549 = frozenset([7, 25, 42, 44, 53, 55, 57, 60, 61, 65, 67, 70, 72, 77, 79, 80, 81, 85, 86, 87, 89, 90, 91, 94, 98, 101, 102, 164])
    FOLLOW_RCURLY_in_interfaceBody5552 = frozenset([1])
    FOLLOW_block_in_classScopeDeclarations5590 = frozenset([1])
    FOLLOW_STATIC_in_classScopeDeclarations5619 = frozenset([23])
    FOLLOW_block_in_classScopeDeclarations5621 = frozenset([1])
    FOLLOW_modifierList_in_classScopeDeclarations5644 = frozenset([25, 55, 57, 60, 65, 72, 79, 80, 89, 101, 164])
    FOLLOW_genericTypeParameterList_in_classScopeDeclarations5658 = frozenset([55, 57, 60, 65, 72, 79, 80, 89, 101, 164])
    FOLLOW_type_in_classScopeDeclarations5677 = frozenset([164])
    FOLLOW_IDENT_in_classScopeDeclarations5679 = frozenset([29])
    FOLLOW_formalParameterList_in_classScopeDeclarations5681 = frozenset([22, 23, 44, 97])
    FOLLOW_arrayDeclaratorList_in_classScopeDeclarations5683 = frozenset([23, 44, 97])
    FOLLOW_throwsClause_in_classScopeDeclarations5686 = frozenset([23, 44])
    FOLLOW_block_in_classScopeDeclarations5690 = frozenset([1])
    FOLLOW_SEMI_in_classScopeDeclarations5694 = frozenset([1])
    FOLLOW_VOID_in_classScopeDeclarations5756 = frozenset([164])
    FOLLOW_IDENT_in_classScopeDeclarations5758 = frozenset([29])
    FOLLOW_formalParameterList_in_classScopeDeclarations5760 = frozenset([23, 44, 97])
    FOLLOW_throwsClause_in_classScopeDeclarations5762 = frozenset([23, 44])
    FOLLOW_block_in_classScopeDeclarations5766 = frozenset([1])
    FOLLOW_SEMI_in_classScopeDeclarations5770 = frozenset([1])
    FOLLOW_IDENT_in_classScopeDeclarations5829 = frozenset([29])
    FOLLOW_formalParameterList_in_classScopeDeclarations5831 = frozenset([23, 97])
    FOLLOW_throwsClause_in_classScopeDeclarations5833 = frozenset([23])
    FOLLOW_block_in_classScopeDeclarations5836 = frozenset([1])
    FOLLOW_type_in_classScopeDeclarations5900 = frozenset([164])
    FOLLOW_classFieldDeclaratorList_in_classScopeDeclarations5902 = frozenset([44])
    FOLLOW_SEMI_in_classScopeDeclarations5904 = frozenset([1])
    FOLLOW_typeDeclaration_in_classScopeDeclarations5949 = frozenset([1])
    FOLLOW_SEMI_in_classScopeDeclarations5959 = frozenset([1])
    FOLLOW_modifierList_in_interfaceScopeDeclarations5979 = frozenset([25, 55, 57, 60, 65, 72, 79, 80, 89, 101, 164])
    FOLLOW_genericTypeParameterList_in_interfaceScopeDeclarations5993 = frozenset([55, 57, 60, 65, 72, 79, 80, 89, 101, 164])
    FOLLOW_type_in_interfaceScopeDeclarations6012 = frozenset([164])
    FOLLOW_IDENT_in_interfaceScopeDeclarations6014 = frozenset([29])
    FOLLOW_formalParameterList_in_interfaceScopeDeclarations6016 = frozenset([22, 44, 97])
    FOLLOW_arrayDeclaratorList_in_interfaceScopeDeclarations6018 = frozenset([44, 97])
    FOLLOW_throwsClause_in_interfaceScopeDeclarations6021 = frozenset([44])
    FOLLOW_SEMI_in_interfaceScopeDeclarations6024 = frozenset([1])
    FOLLOW_VOID_in_interfaceScopeDeclarations6082 = frozenset([164])
    FOLLOW_IDENT_in_interfaceScopeDeclarations6084 = frozenset([29])
    FOLLOW_formalParameterList_in_interfaceScopeDeclarations6086 = frozenset([44, 97])
    FOLLOW_throwsClause_in_interfaceScopeDeclarations6088 = frozenset([44])
    FOLLOW_SEMI_in_interfaceScopeDeclarations6091 = frozenset([1])
    FOLLOW_type_in_interfaceScopeDeclarations6154 = frozenset([164])
    FOLLOW_interfaceFieldDeclaratorList_in_interfaceScopeDeclarations6156 = frozenset([44])
    FOLLOW_SEMI_in_interfaceScopeDeclarations6158 = frozenset([1])
    FOLLOW_typeDeclaration_in_interfaceScopeDeclarations6203 = frozenset([1])
    FOLLOW_SEMI_in_interfaceScopeDeclarations6213 = frozenset([1])
    FOLLOW_classFieldDeclarator_in_classFieldDeclaratorList6233 = frozenset([1, 11])
    FOLLOW_COMMA_in_classFieldDeclaratorList6236 = frozenset([164])
    FOLLOW_classFieldDeclarator_in_classFieldDeclaratorList6238 = frozenset([1, 11])
    FOLLOW_variableDeclaratorId_in_classFieldDeclarator6277 = frozenset([1, 6])
    FOLLOW_ASSIGN_in_classFieldDeclarator6280 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_variableInitializer_in_classFieldDeclarator6282 = frozenset([1])
    FOLLOW_interfaceFieldDeclarator_in_interfaceFieldDeclaratorList6323 = frozenset([1, 11])
    FOLLOW_COMMA_in_interfaceFieldDeclaratorList6326 = frozenset([164])
    FOLLOW_interfaceFieldDeclarator_in_interfaceFieldDeclaratorList6328 = frozenset([1, 11])
    FOLLOW_variableDeclaratorId_in_interfaceFieldDeclarator6367 = frozenset([6])
    FOLLOW_ASSIGN_in_interfaceFieldDeclarator6369 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_variableInitializer_in_interfaceFieldDeclarator6371 = frozenset([1])
    FOLLOW_IDENT_in_variableDeclaratorId6409 = frozenset([1, 22])
    FOLLOW_arrayDeclaratorList_in_variableDeclaratorId6412 = frozenset([1])
    FOLLOW_arrayInitializer_in_variableInitializer6432 = frozenset([1])
    FOLLOW_expression_in_variableInitializer6442 = frozenset([1])
    FOLLOW_LBRACK_in_arrayDeclarator6461 = frozenset([41])
    FOLLOW_RBRACK_in_arrayDeclarator6463 = frozenset([1])
    FOLLOW_arrayDeclarator_in_arrayDeclaratorList6497 = frozenset([1, 22])
    FOLLOW_LCURLY_in_arrayInitializer6535 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 42, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_variableInitializer_in_arrayInitializer6538 = frozenset([11, 42])
    FOLLOW_COMMA_in_arrayInitializer6541 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_variableInitializer_in_arrayInitializer6543 = frozenset([11, 42])
    FOLLOW_COMMA_in_arrayInitializer6547 = frozenset([42])
    FOLLOW_RCURLY_in_arrayInitializer6552 = frozenset([1])
    FOLLOW_THROWS_in_throwsClause6590 = frozenset([164])
    FOLLOW_qualifiedIdentList_in_throwsClause6592 = frozenset([1])
    FOLLOW_modifier_in_modifierList6629 = frozenset([1, 7, 53, 70, 81, 85, 86, 87, 90, 91, 94, 98, 102])
    FOLLOW_PUBLIC_in_modifier6667 = frozenset([1])
    FOLLOW_PROTECTED_in_modifier6677 = frozenset([1])
    FOLLOW_PRIVATE_in_modifier6687 = frozenset([1])
    FOLLOW_STATIC_in_modifier6697 = frozenset([1])
    FOLLOW_ABSTRACT_in_modifier6707 = frozenset([1])
    FOLLOW_NATIVE_in_modifier6717 = frozenset([1])
    FOLLOW_SYNCHRONIZED_in_modifier6727 = frozenset([1])
    FOLLOW_TRANSIENT_in_modifier6737 = frozenset([1])
    FOLLOW_VOLATILE_in_modifier6747 = frozenset([1])
    FOLLOW_STRICTFP_in_modifier6757 = frozenset([1])
    FOLLOW_localModifier_in_modifier6767 = frozenset([1])
    FOLLOW_localModifier_in_localModifierList6786 = frozenset([1, 7, 53, 70, 81, 85, 86, 87, 90, 91, 94, 98, 102])
    FOLLOW_FINAL_in_localModifier6823 = frozenset([1])
    FOLLOW_annotation_in_localModifier6833 = frozenset([1])
    FOLLOW_simpleType_in_type6852 = frozenset([1])
    FOLLOW_objectType_in_type6862 = frozenset([1])
    FOLLOW_primitiveType_in_simpleType6882 = frozenset([1, 22])
    FOLLOW_arrayDeclaratorList_in_simpleType6884 = frozenset([1])
    FOLLOW_qualifiedTypeIdent_in_objectType6925 = frozenset([1, 22])
    FOLLOW_arrayDeclaratorList_in_objectType6927 = frozenset([1])
    FOLLOW_qualifiedTypeIdentSimplified_in_objectTypeSimplified6967 = frozenset([1, 22])
    FOLLOW_arrayDeclaratorList_in_objectTypeSimplified6969 = frozenset([1])
    FOLLOW_typeIdent_in_qualifiedTypeIdent7009 = frozenset([1, 15])
    FOLLOW_DOT_in_qualifiedTypeIdent7012 = frozenset([55, 57, 60, 65, 72, 79, 80, 89, 164])
    FOLLOW_typeIdent_in_qualifiedTypeIdent7014 = frozenset([1, 15])
    FOLLOW_typeIdentSimplified_in_qualifiedTypeIdentSimplified7053 = frozenset([1, 15])
    FOLLOW_DOT_in_qualifiedTypeIdentSimplified7056 = frozenset([164])
    FOLLOW_typeIdentSimplified_in_qualifiedTypeIdentSimplified7058 = frozenset([1, 15])
    FOLLOW_IDENT_in_typeIdent7097 = frozenset([1, 25])
    FOLLOW_genericTypeArgumentList_in_typeIdent7100 = frozenset([1])
    FOLLOW_IDENT_in_typeIdentSimplified7120 = frozenset([1, 25])
    FOLLOW_genericTypeArgumentListSimplified_in_typeIdentSimplified7123 = frozenset([1])
    FOLLOW_set_in_primitiveType0 = frozenset([1])
    FOLLOW_LESS_THAN_in_genericTypeArgumentList7232 = frozenset([40, 55, 57, 60, 65, 72, 79, 80, 89, 164])
    FOLLOW_genericTypeArgument_in_genericTypeArgumentList7234 = frozenset([8, 11, 20, 47])
    FOLLOW_COMMA_in_genericTypeArgumentList7237 = frozenset([40, 55, 57, 60, 65, 72, 79, 80, 89, 164])
    FOLLOW_genericTypeArgument_in_genericTypeArgumentList7239 = frozenset([8, 11, 20, 47])
    FOLLOW_genericTypeListClosing_in_genericTypeArgumentList7243 = frozenset([1])
    FOLLOW_type_in_genericTypeArgument7281 = frozenset([1])
    FOLLOW_QUESTION_in_genericTypeArgument7291 = frozenset([1, 68, 92])
    FOLLOW_genericWildcardBoundType_in_genericTypeArgument7293 = frozenset([1])
    FOLLOW_set_in_genericWildcardBoundType7331 = frozenset([55, 57, 60, 65, 72, 79, 80, 89, 164])
    FOLLOW_type_in_genericWildcardBoundType7340 = frozenset([1])
    FOLLOW_LESS_THAN_in_genericTypeArgumentListSimplified7359 = frozenset([40, 55, 57, 60, 65, 72, 79, 80, 89, 164])
    FOLLOW_genericTypeArgumentSimplified_in_genericTypeArgumentListSimplified7361 = frozenset([8, 11, 20, 47])
    FOLLOW_COMMA_in_genericTypeArgumentListSimplified7364 = frozenset([40, 55, 57, 60, 65, 72, 79, 80, 89, 164])
    FOLLOW_genericTypeArgumentSimplified_in_genericTypeArgumentListSimplified7366 = frozenset([8, 11, 20, 47])
    FOLLOW_genericTypeListClosing_in_genericTypeArgumentListSimplified7370 = frozenset([1])
    FOLLOW_type_in_genericTypeArgumentSimplified7408 = frozenset([1])
    FOLLOW_QUESTION_in_genericTypeArgumentSimplified7418 = frozenset([1])
    FOLLOW_qualifiedIdentifier_in_qualifiedIdentList7437 = frozenset([1, 11])
    FOLLOW_COMMA_in_qualifiedIdentList7440 = frozenset([164])
    FOLLOW_qualifiedIdentifier_in_qualifiedIdentList7443 = frozenset([1, 11])
    FOLLOW_LPAREN_in_formalParameterList7464 = frozenset([7, 43, 53, 55, 57, 60, 65, 70, 72, 79, 80, 81, 85, 86, 87, 89, 90, 91, 94, 98, 102, 164])
    FOLLOW_formalParameterStandardDecl_in_formalParameterList7491 = frozenset([11, 43])
    FOLLOW_COMMA_in_formalParameterList7494 = frozenset([7, 53, 55, 57, 60, 65, 70, 72, 79, 80, 81, 85, 86, 87, 89, 90, 91, 94, 98, 102, 164])
    FOLLOW_formalParameterStandardDecl_in_formalParameterList7496 = frozenset([11, 43])
    FOLLOW_COMMA_in_formalParameterList7501 = frozenset([7, 53, 55, 57, 60, 65, 70, 72, 79, 80, 81, 85, 86, 87, 89, 90, 91, 94, 98, 102, 164])
    FOLLOW_formalParameterVarArgDecl_in_formalParameterList7503 = frozenset([43])
    FOLLOW_formalParameterVarArgDecl_in_formalParameterList7558 = frozenset([43])
    FOLLOW_RPAREN_in_formalParameterList7633 = frozenset([1])
    FOLLOW_localModifierList_in_formalParameterStandardDecl7652 = frozenset([55, 57, 60, 65, 72, 79, 80, 89, 164])
    FOLLOW_type_in_formalParameterStandardDecl7654 = frozenset([164])
    FOLLOW_variableDeclaratorId_in_formalParameterStandardDecl7656 = frozenset([1])
    FOLLOW_localModifierList_in_formalParameterVarArgDecl7696 = frozenset([55, 57, 60, 65, 72, 79, 80, 89, 164])
    FOLLOW_type_in_formalParameterVarArgDecl7698 = frozenset([17])
    FOLLOW_ELLIPSIS_in_formalParameterVarArgDecl7700 = frozenset([164])
    FOLLOW_variableDeclaratorId_in_formalParameterVarArgDecl7702 = frozenset([1])
    FOLLOW_IDENT_in_qualifiedIdentifier7746 = frozenset([1, 15])
    FOLLOW_DOT_in_qualifiedIdentifier7789 = frozenset([164])
    FOLLOW_IDENT_in_qualifiedIdentifier7793 = frozenset([1, 15])
    FOLLOW_annotation_in_annotationList7842 = frozenset([1, 7, 53, 70, 81, 85, 86, 87, 90, 91, 94, 98, 102])
    FOLLOW_AT_in_annotation7880 = frozenset([164])
    FOLLOW_qualifiedIdentifier_in_annotation7883 = frozenset([1, 29])
    FOLLOW_annotationInit_in_annotation7885 = frozenset([1])
    FOLLOW_LPAREN_in_annotationInit7905 = frozenset([7, 12, 21, 23, 25, 27, 29, 30, 34, 38, 53, 55, 57, 60, 65, 69, 70, 72, 79, 80, 81, 82, 83, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 99, 101, 102, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_annotationInitializers_in_annotationInit7907 = frozenset([43])
    FOLLOW_RPAREN_in_annotationInit7909 = frozenset([1])
    FOLLOW_annotationInitializer_in_annotationInitializers7946 = frozenset([1, 11])
    FOLLOW_COMMA_in_annotationInitializers7949 = frozenset([164])
    FOLLOW_annotationInitializer_in_annotationInitializers7951 = frozenset([1, 11])
    FOLLOW_annotationElementValue_in_annotationInitializers7981 = frozenset([1])
    FOLLOW_IDENT_in_annotationInitializer8018 = frozenset([6])
    FOLLOW_ASSIGN_in_annotationInitializer8021 = frozenset([7, 12, 21, 23, 25, 27, 29, 30, 34, 38, 53, 55, 57, 60, 65, 69, 70, 72, 79, 80, 81, 82, 83, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 99, 101, 102, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_annotationElementValue_in_annotationInitializer8024 = frozenset([1])
    FOLLOW_annotationElementValueExpression_in_annotationElementValue8043 = frozenset([1])
    FOLLOW_annotation_in_annotationElementValue8053 = frozenset([1])
    FOLLOW_annotationElementValueArrayInitializer_in_annotationElementValue8063 = frozenset([1])
    FOLLOW_conditionalExpression_in_annotationElementValueExpression8082 = frozenset([1])
    FOLLOW_LCURLY_in_annotationElementValueArrayInitializer8118 = frozenset([7, 11, 12, 21, 23, 25, 27, 29, 30, 34, 38, 42, 53, 55, 57, 60, 65, 69, 70, 72, 79, 80, 81, 82, 83, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 99, 101, 102, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_annotationElementValue_in_annotationElementValueArrayInitializer8121 = frozenset([11, 42])
    FOLLOW_COMMA_in_annotationElementValueArrayInitializer8124 = frozenset([7, 12, 21, 23, 25, 27, 29, 30, 34, 38, 53, 55, 57, 60, 65, 69, 70, 72, 79, 80, 81, 82, 83, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 99, 101, 102, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_annotationElementValue_in_annotationElementValueArrayInitializer8126 = frozenset([11, 42])
    FOLLOW_COMMA_in_annotationElementValueArrayInitializer8133 = frozenset([42])
    FOLLOW_RCURLY_in_annotationElementValueArrayInitializer8137 = frozenset([1])
    FOLLOW_AT_in_annotationTypeDeclaration8176 = frozenset([77])
    FOLLOW_INTERFACE_in_annotationTypeDeclaration8178 = frozenset([164])
    FOLLOW_IDENT_in_annotationTypeDeclaration8180 = frozenset([23])
    FOLLOW_annotationBody_in_annotationTypeDeclaration8182 = frozenset([1])
    FOLLOW_LCURLY_in_annotationBody8221 = frozenset([7, 42, 53, 55, 57, 60, 61, 65, 67, 70, 72, 77, 79, 80, 81, 85, 86, 87, 89, 90, 91, 94, 98, 102, 164])
    FOLLOW_annotationScopeDeclarations_in_annotationBody8223 = frozenset([7, 42, 53, 55, 57, 60, 61, 65, 67, 70, 72, 77, 79, 80, 81, 85, 86, 87, 89, 90, 91, 94, 98, 102, 164])
    FOLLOW_RCURLY_in_annotationBody8226 = frozenset([1])
    FOLLOW_modifierList_in_annotationScopeDeclarations8264 = frozenset([55, 57, 60, 65, 72, 79, 80, 89, 164])
    FOLLOW_type_in_annotationScopeDeclarations8266 = frozenset([164])
    FOLLOW_IDENT_in_annotationScopeDeclarations8280 = frozenset([29])
    FOLLOW_LPAREN_in_annotationScopeDeclarations8282 = frozenset([43])
    FOLLOW_RPAREN_in_annotationScopeDeclarations8284 = frozenset([44, 63])
    FOLLOW_annotationDefaultValue_in_annotationScopeDeclarations8286 = frozenset([44])
    FOLLOW_SEMI_in_annotationScopeDeclarations8289 = frozenset([1])
    FOLLOW_classFieldDeclaratorList_in_annotationScopeDeclarations8331 = frozenset([44])
    FOLLOW_SEMI_in_annotationScopeDeclarations8333 = frozenset([1])
    FOLLOW_typeDeclaration_in_annotationScopeDeclarations8378 = frozenset([1])
    FOLLOW_DEFAULT_in_annotationDefaultValue8397 = frozenset([7, 12, 21, 23, 25, 27, 29, 30, 34, 38, 53, 55, 57, 60, 65, 69, 70, 72, 79, 80, 81, 82, 83, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 99, 101, 102, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_annotationElementValue_in_annotationDefaultValue8400 = frozenset([1])
    FOLLOW_LCURLY_in_block8421 = frozenset([7, 12, 21, 23, 25, 27, 29, 30, 34, 38, 42, 44, 53, 54, 55, 56, 57, 60, 61, 62, 64, 65, 67, 69, 70, 72, 73, 74, 77, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100, 101, 102, 103, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_blockStatement_in_block8423 = frozenset([7, 12, 21, 23, 25, 27, 29, 30, 34, 38, 42, 44, 53, 54, 55, 56, 57, 60, 61, 62, 64, 65, 67, 69, 70, 72, 73, 74, 77, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100, 101, 102, 103, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_RCURLY_in_block8426 = frozenset([1])
    FOLLOW_localVariableDeclaration_in_blockStatement8464 = frozenset([44])
    FOLLOW_SEMI_in_blockStatement8466 = frozenset([1])
    FOLLOW_typeDeclaration_in_blockStatement8477 = frozenset([1])
    FOLLOW_statement_in_blockStatement8487 = frozenset([1])
    FOLLOW_localModifierList_in_localVariableDeclaration8506 = frozenset([55, 57, 60, 65, 72, 79, 80, 89, 164])
    FOLLOW_type_in_localVariableDeclaration8508 = frozenset([164])
    FOLLOW_classFieldDeclaratorList_in_localVariableDeclaration8510 = frozenset([1])
    FOLLOW_block_in_statement8551 = frozenset([1])
    FOLLOW_ASSERT_in_statement8561 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expression_in_statement8565 = frozenset([10, 44])
    FOLLOW_COLON_in_statement8579 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expression_in_statement8583 = frozenset([44])
    FOLLOW_SEMI_in_statement8585 = frozenset([1])
    FOLLOW_SEMI_in_statement8648 = frozenset([1])
    FOLLOW_IF_in_statement8737 = frozenset([29])
    FOLLOW_parenthesizedExpression_in_statement8739 = frozenset([7, 12, 21, 23, 25, 27, 29, 30, 34, 38, 44, 53, 54, 55, 56, 57, 60, 61, 62, 64, 65, 67, 69, 70, 72, 73, 74, 77, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100, 101, 102, 103, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_statement_in_statement8743 = frozenset([1, 66])
    FOLLOW_ELSE_in_statement8757 = frozenset([7, 12, 21, 23, 25, 27, 29, 30, 34, 38, 44, 53, 54, 55, 56, 57, 60, 61, 62, 64, 65, 67, 69, 70, 72, 73, 74, 77, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100, 101, 102, 103, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_statement_in_statement8761 = frozenset([1])
    FOLLOW_FOR_in_statement8924 = frozenset([29])
    FOLLOW_LPAREN_in_statement8926 = frozenset([7, 12, 21, 23, 25, 27, 29, 30, 34, 38, 44, 53, 55, 57, 60, 65, 69, 70, 72, 79, 80, 81, 82, 83, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 99, 101, 102, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_forInit_in_statement8940 = frozenset([44])
    FOLLOW_SEMI_in_statement8942 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 44, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_forCondition_in_statement8944 = frozenset([44])
    FOLLOW_SEMI_in_statement8946 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 43, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_forUpdater_in_statement8948 = frozenset([43])
    FOLLOW_RPAREN_in_statement8950 = frozenset([7, 12, 21, 23, 25, 27, 29, 30, 34, 38, 44, 53, 54, 55, 56, 57, 60, 61, 62, 64, 65, 67, 69, 70, 72, 73, 74, 77, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100, 101, 102, 103, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_statement_in_statement8952 = frozenset([1])
    FOLLOW_localModifierList_in_statement8986 = frozenset([55, 57, 60, 65, 72, 79, 80, 89, 164])
    FOLLOW_type_in_statement8988 = frozenset([164])
    FOLLOW_IDENT_in_statement8990 = frozenset([10])
    FOLLOW_COLON_in_statement8992 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expression_in_statement8994 = frozenset([43])
    FOLLOW_RPAREN_in_statement8996 = frozenset([7, 12, 21, 23, 25, 27, 29, 30, 34, 38, 44, 53, 54, 55, 56, 57, 60, 61, 62, 64, 65, 67, 69, 70, 72, 73, 74, 77, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100, 101, 102, 103, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_statement_in_statement8998 = frozenset([1])
    FOLLOW_WHILE_in_statement9112 = frozenset([29])
    FOLLOW_parenthesizedExpression_in_statement9114 = frozenset([7, 12, 21, 23, 25, 27, 29, 30, 34, 38, 44, 53, 54, 55, 56, 57, 60, 61, 62, 64, 65, 67, 69, 70, 72, 73, 74, 77, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100, 101, 102, 103, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_statement_in_statement9116 = frozenset([1])
    FOLLOW_DO_in_statement9165 = frozenset([7, 12, 21, 23, 25, 27, 29, 30, 34, 38, 44, 53, 54, 55, 56, 57, 60, 61, 62, 64, 65, 67, 69, 70, 72, 73, 74, 77, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100, 101, 102, 103, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_statement_in_statement9167 = frozenset([103])
    FOLLOW_WHILE_in_statement9169 = frozenset([29])
    FOLLOW_parenthesizedExpression_in_statement9171 = frozenset([44])
    FOLLOW_SEMI_in_statement9173 = frozenset([1])
    FOLLOW_TRY_in_statement9214 = frozenset([23])
    FOLLOW_block_in_statement9216 = frozenset([59, 71])
    FOLLOW_catches_in_statement9219 = frozenset([1, 59, 71])
    FOLLOW_finallyClause_in_statement9221 = frozenset([1])
    FOLLOW_finallyClause_in_statement9226 = frozenset([1])
    FOLLOW_SWITCH_in_statement9269 = frozenset([29])
    FOLLOW_parenthesizedExpression_in_statement9271 = frozenset([23])
    FOLLOW_LCURLY_in_statement9273 = frozenset([58, 63])
    FOLLOW_switchBlockLabels_in_statement9275 = frozenset([42])
    FOLLOW_RCURLY_in_statement9277 = frozenset([1])
    FOLLOW_SYNCHRONIZED_in_statement9303 = frozenset([29])
    FOLLOW_parenthesizedExpression_in_statement9305 = frozenset([23])
    FOLLOW_block_in_statement9307 = frozenset([1])
    FOLLOW_RETURN_in_statement9353 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 44, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expression_in_statement9355 = frozenset([44])
    FOLLOW_SEMI_in_statement9358 = frozenset([1])
    FOLLOW_THROW_in_statement9422 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expression_in_statement9424 = frozenset([44])
    FOLLOW_SEMI_in_statement9426 = frozenset([1])
    FOLLOW_BREAK_in_statement9491 = frozenset([44, 164])
    FOLLOW_IDENT_in_statement9493 = frozenset([44])
    FOLLOW_SEMI_in_statement9496 = frozenset([1])
    FOLLOW_CONTINUE_in_statement9566 = frozenset([44, 164])
    FOLLOW_IDENT_in_statement9568 = frozenset([44])
    FOLLOW_SEMI_in_statement9571 = frozenset([1])
    FOLLOW_IDENT_in_statement9638 = frozenset([10])
    FOLLOW_COLON_in_statement9640 = frozenset([7, 12, 21, 23, 25, 27, 29, 30, 34, 38, 44, 53, 54, 55, 56, 57, 60, 61, 62, 64, 65, 67, 69, 70, 72, 73, 74, 77, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100, 101, 102, 103, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_statement_in_statement9642 = frozenset([1])
    FOLLOW_expression_in_statement9709 = frozenset([44])
    FOLLOW_SEMI_in_statement9711 = frozenset([1])
    FOLLOW_SEMI_in_statement9722 = frozenset([1])
    FOLLOW_catchClause_in_catches9742 = frozenset([1, 59])
    FOLLOW_CATCH_in_catchClause9780 = frozenset([29])
    FOLLOW_LPAREN_in_catchClause9783 = frozenset([7, 53, 55, 57, 60, 65, 70, 72, 79, 80, 81, 85, 86, 87, 89, 90, 91, 94, 98, 102, 164])
    FOLLOW_formalParameterStandardDecl_in_catchClause9786 = frozenset([43])
    FOLLOW_RPAREN_in_catchClause9788 = frozenset([23])
    FOLLOW_block_in_catchClause9791 = frozenset([1])
    FOLLOW_FINALLY_in_finallyClause9810 = frozenset([23])
    FOLLOW_block_in_finallyClause9812 = frozenset([1])
    FOLLOW_switchCaseLabels_in_switchBlockLabels9847 = frozenset([1, 63])
    FOLLOW_switchDefaultLabel_in_switchBlockLabels9849 = frozenset([1])
    FOLLOW_switchCaseLabel_in_switchCaseLabels9890 = frozenset([1, 58])
    FOLLOW_CASE_in_switchCaseLabel9910 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expression_in_switchCaseLabel9913 = frozenset([10])
    FOLLOW_COLON_in_switchCaseLabel9915 = frozenset([1, 7, 12, 21, 23, 25, 27, 29, 30, 34, 38, 44, 53, 54, 55, 56, 57, 60, 61, 62, 64, 65, 67, 69, 70, 72, 73, 74, 77, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100, 101, 102, 103, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_blockStatement_in_switchCaseLabel9918 = frozenset([1, 7, 12, 21, 23, 25, 27, 29, 30, 34, 38, 44, 53, 54, 55, 56, 57, 60, 61, 62, 64, 65, 67, 69, 70, 72, 73, 74, 77, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100, 101, 102, 103, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_DEFAULT_in_switchDefaultLabel9938 = frozenset([10])
    FOLLOW_COLON_in_switchDefaultLabel9941 = frozenset([1, 7, 12, 21, 23, 25, 27, 29, 30, 34, 38, 44, 53, 54, 55, 56, 57, 60, 61, 62, 64, 65, 67, 69, 70, 72, 73, 74, 77, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100, 101, 102, 103, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_blockStatement_in_switchDefaultLabel9944 = frozenset([1, 7, 12, 21, 23, 25, 27, 29, 30, 34, 38, 44, 53, 54, 55, 56, 57, 60, 61, 62, 64, 65, 67, 69, 70, 72, 73, 74, 77, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100, 101, 102, 103, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_localVariableDeclaration_in_forInit9964 = frozenset([1])
    FOLLOW_expressionList_in_forInit9986 = frozenset([1])
    FOLLOW_expression_in_forCondition10070 = frozenset([1])
    FOLLOW_expressionList_in_forUpdater10108 = frozenset([1])
    FOLLOW_LPAREN_in_parenthesizedExpression10148 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expression_in_parenthesizedExpression10150 = frozenset([43])
    FOLLOW_RPAREN_in_parenthesizedExpression10152 = frozenset([1])
    FOLLOW_expression_in_expressionList10189 = frozenset([1, 11])
    FOLLOW_COMMA_in_expressionList10192 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expression_in_expressionList10195 = frozenset([1, 11])
    FOLLOW_assignmentExpression_in_expression10216 = frozenset([1])
    FOLLOW_conditionalExpression_in_assignmentExpression10252 = frozenset([1, 5, 6, 9, 14, 31, 33, 37, 39, 46, 48, 50, 52])
    FOLLOW_ASSIGN_in_assignmentExpression10270 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_PLUS_ASSIGN_in_assignmentExpression10289 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_MINUS_ASSIGN_in_assignmentExpression10308 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_STAR_ASSIGN_in_assignmentExpression10327 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_DIV_ASSIGN_in_assignmentExpression10346 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_AND_ASSIGN_in_assignmentExpression10365 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_OR_ASSIGN_in_assignmentExpression10384 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_XOR_ASSIGN_in_assignmentExpression10403 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_MOD_ASSIGN_in_assignmentExpression10422 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_SHIFT_LEFT_ASSIGN_in_assignmentExpression10441 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_SHIFT_RIGHT_ASSIGN_in_assignmentExpression10460 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_BIT_SHIFT_RIGHT_ASSIGN_in_assignmentExpression10479 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_assignmentExpression_in_assignmentExpression10500 = frozenset([1])
    FOLLOW_logicalOrExpression_in_conditionalExpression10521 = frozenset([1, 40])
    FOLLOW_QUESTION_in_conditionalExpression10524 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_assignmentExpression_in_conditionalExpression10527 = frozenset([10])
    FOLLOW_COLON_in_conditionalExpression10529 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_conditionalExpression_in_conditionalExpression10532 = frozenset([1])
    FOLLOW_logicalAndExpression_in_logicalOrExpression10553 = frozenset([1, 28])
    FOLLOW_LOGICAL_OR_in_logicalOrExpression10556 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_logicalAndExpression_in_logicalOrExpression10559 = frozenset([1, 28])
    FOLLOW_inclusiveOrExpression_in_logicalAndExpression10580 = frozenset([1, 26])
    FOLLOW_LOGICAL_AND_in_logicalAndExpression10583 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_inclusiveOrExpression_in_logicalAndExpression10586 = frozenset([1, 26])
    FOLLOW_exclusiveOrExpression_in_inclusiveOrExpression10607 = frozenset([1, 36])
    FOLLOW_OR_in_inclusiveOrExpression10610 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_exclusiveOrExpression_in_inclusiveOrExpression10613 = frozenset([1, 36])
    FOLLOW_andExpression_in_exclusiveOrExpression10634 = frozenset([1, 51])
    FOLLOW_XOR_in_exclusiveOrExpression10637 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_andExpression_in_exclusiveOrExpression10640 = frozenset([1, 51])
    FOLLOW_equalityExpression_in_andExpression10661 = frozenset([1, 4])
    FOLLOW_AND_in_andExpression10664 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_equalityExpression_in_andExpression10667 = frozenset([1, 4])
    FOLLOW_instanceOfExpression_in_equalityExpression10688 = frozenset([1, 18, 35])
    FOLLOW_EQUAL_in_equalityExpression10706 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_NOT_EQUAL_in_equalityExpression10725 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_instanceOfExpression_in_equalityExpression10754 = frozenset([1, 18, 35])
    FOLLOW_relationalExpression_in_instanceOfExpression10784 = frozenset([1, 76])
    FOLLOW_INSTANCEOF_in_instanceOfExpression10787 = frozenset([55, 57, 60, 65, 72, 79, 80, 89, 164])
    FOLLOW_type_in_instanceOfExpression10790 = frozenset([1])
    FOLLOW_shiftExpression_in_relationalExpression10811 = frozenset([1, 19, 20, 24, 25])
    FOLLOW_LESS_OR_EQUAL_in_relationalExpression10829 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_GREATER_OR_EQUAL_in_relationalExpression10848 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_LESS_THAN_in_relationalExpression10867 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_GREATER_THAN_in_relationalExpression10886 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_shiftExpression_in_relationalExpression10915 = frozenset([1, 19, 20, 24, 25])
    FOLLOW_additiveExpression_in_shiftExpression10945 = frozenset([1, 8, 45, 47])
    FOLLOW_BIT_SHIFT_RIGHT_in_shiftExpression10963 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_SHIFT_RIGHT_in_shiftExpression10982 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_SHIFT_LEFT_in_shiftExpression11001 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_additiveExpression_in_shiftExpression11030 = frozenset([1, 8, 45, 47])
    FOLLOW_multiplicativeExpression_in_additiveExpression11060 = frozenset([1, 30, 38])
    FOLLOW_PLUS_in_additiveExpression11078 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_MINUS_in_additiveExpression11097 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_multiplicativeExpression_in_additiveExpression11126 = frozenset([1, 30, 38])
    FOLLOW_unaryExpression_in_multiplicativeExpression11156 = frozenset([1, 13, 32, 49])
    FOLLOW_STAR_in_multiplicativeExpression11174 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_DIV_in_multiplicativeExpression11193 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_MOD_in_multiplicativeExpression11212 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_unaryExpression_in_multiplicativeExpression11241 = frozenset([1, 13, 32, 49])
    FOLLOW_PLUS_in_unaryExpression11271 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_unaryExpression_in_unaryExpression11273 = frozenset([1])
    FOLLOW_MINUS_in_unaryExpression11300 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_unaryExpression_in_unaryExpression11302 = frozenset([1])
    FOLLOW_INC_in_unaryExpression11328 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_postfixedExpression_in_unaryExpression11330 = frozenset([1])
    FOLLOW_DEC_in_unaryExpression11354 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_postfixedExpression_in_unaryExpression11356 = frozenset([1])
    FOLLOW_unaryExpressionNotPlusMinus_in_unaryExpression11380 = frozenset([1])
    FOLLOW_NOT_in_unaryExpressionNotPlusMinus11399 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_unaryExpression_in_unaryExpressionNotPlusMinus11401 = frozenset([1])
    FOLLOW_LOGICAL_NOT_in_unaryExpressionNotPlusMinus11448 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_unaryExpression_in_unaryExpressionNotPlusMinus11450 = frozenset([1])
    FOLLOW_LPAREN_in_unaryExpressionNotPlusMinus11489 = frozenset([55, 57, 60, 65, 72, 79, 80, 89, 164])
    FOLLOW_type_in_unaryExpressionNotPlusMinus11491 = frozenset([43])
    FOLLOW_RPAREN_in_unaryExpressionNotPlusMinus11493 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_unaryExpression_in_unaryExpressionNotPlusMinus11495 = frozenset([1])
    FOLLOW_postfixedExpression_in_unaryExpressionNotPlusMinus11530 = frozenset([1])
    FOLLOW_primaryExpression_in_postfixedExpression11562 = frozenset([1, 12, 15, 21, 22])
    FOLLOW_DOT_in_postfixedExpression11624 = frozenset([25, 82, 92, 95, 164])
    FOLLOW_genericTypeArgumentListSimplified_in_postfixedExpression11646 = frozenset([164])
    FOLLOW_IDENT_in_postfixedExpression11728 = frozenset([1, 12, 15, 21, 22, 29])
    FOLLOW_arguments_in_postfixedExpression11806 = frozenset([1, 12, 15, 21, 22])
    FOLLOW_THIS_in_postfixedExpression11880 = frozenset([1, 12, 15, 21, 22])
    FOLLOW_SUPER_in_postfixedExpression11943 = frozenset([29])
    FOLLOW_arguments_in_postfixedExpression11945 = frozenset([1, 12, 15, 21, 22])
    FOLLOW_SUPER_in_postfixedExpression11998 = frozenset([15])
    FOLLOW_DOT_in_postfixedExpression12002 = frozenset([164])
    FOLLOW_IDENT_in_postfixedExpression12004 = frozenset([1, 12, 15, 21, 22, 29])
    FOLLOW_arguments_in_postfixedExpression12071 = frozenset([1, 12, 15, 21, 22])
    FOLLOW_innerNewExpression_in_postfixedExpression12142 = frozenset([1, 12, 15, 21, 22])
    FOLLOW_LBRACK_in_postfixedExpression12199 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expression_in_postfixedExpression12201 = frozenset([41])
    FOLLOW_RBRACK_in_postfixedExpression12203 = frozenset([1, 12, 15, 21, 22])
    FOLLOW_INC_in_postfixedExpression12264 = frozenset([1])
    FOLLOW_DEC_in_postfixedExpression12288 = frozenset([1])
    FOLLOW_parenthesizedExpression_in_primaryExpression12328 = frozenset([1])
    FOLLOW_literal_in_primaryExpression12338 = frozenset([1])
    FOLLOW_newExpression_in_primaryExpression12348 = frozenset([1])
    FOLLOW_qualifiedIdentExpression_in_primaryExpression12358 = frozenset([1])
    FOLLOW_genericTypeArgumentListSimplified_in_primaryExpression12368 = frozenset([92, 95, 164])
    FOLLOW_SUPER_in_primaryExpression12382 = frozenset([15, 29])
    FOLLOW_arguments_in_primaryExpression12400 = frozenset([1])
    FOLLOW_DOT_in_primaryExpression12460 = frozenset([164])
    FOLLOW_IDENT_in_primaryExpression12462 = frozenset([29])
    FOLLOW_arguments_in_primaryExpression12464 = frozenset([1])
    FOLLOW_IDENT_in_primaryExpression12531 = frozenset([29])
    FOLLOW_arguments_in_primaryExpression12533 = frozenset([1])
    FOLLOW_THIS_in_primaryExpression12588 = frozenset([29])
    FOLLOW_arguments_in_primaryExpression12590 = frozenset([1])
    FOLLOW_THIS_in_primaryExpression12655 = frozenset([1, 29])
    FOLLOW_arguments_in_primaryExpression12723 = frozenset([1])
    FOLLOW_SUPER_in_primaryExpression12788 = frozenset([29])
    FOLLOW_arguments_in_primaryExpression12790 = frozenset([1])
    FOLLOW_SUPER_in_primaryExpression12846 = frozenset([15])
    FOLLOW_DOT_in_primaryExpression12848 = frozenset([164])
    FOLLOW_IDENT_in_primaryExpression12850 = frozenset([1, 29])
    FOLLOW_arguments_in_primaryExpression12874 = frozenset([1])
    FOLLOW_primitiveType_in_primaryExpression13016 = frozenset([15, 22])
    FOLLOW_arrayDeclarator_in_primaryExpression13075 = frozenset([15, 22])
    FOLLOW_DOT_in_primaryExpression13134 = frozenset([61])
    FOLLOW_CLASS_in_primaryExpression13136 = frozenset([1])
    FOLLOW_VOID_in_primaryExpression13196 = frozenset([15])
    FOLLOW_DOT_in_primaryExpression13198 = frozenset([61])
    FOLLOW_CLASS_in_primaryExpression13200 = frozenset([1])
    FOLLOW_qualifiedIdentifier_in_qualifiedIdentExpression13276 = frozenset([1, 15, 22, 29])
    FOLLOW_arrayDeclarator_in_qualifiedIdentExpression13346 = frozenset([15, 22])
    FOLLOW_DOT_in_qualifiedIdentExpression13413 = frozenset([61])
    FOLLOW_CLASS_in_qualifiedIdentExpression13415 = frozenset([1])
    FOLLOW_arguments_in_qualifiedIdentExpression13485 = frozenset([1])
    FOLLOW_DOT_in_qualifiedIdentExpression13546 = frozenset([25, 61, 82, 92, 95, 164])
    FOLLOW_CLASS_in_qualifiedIdentExpression13564 = frozenset([1])
    FOLLOW_genericTypeArgumentListSimplified_in_qualifiedIdentExpression13627 = frozenset([92, 164])
    FOLLOW_SUPER_in_qualifiedIdentExpression13651 = frozenset([29])
    FOLLOW_arguments_in_qualifiedIdentExpression13653 = frozenset([1])
    FOLLOW_SUPER_in_qualifiedIdentExpression13703 = frozenset([15])
    FOLLOW_DOT_in_qualifiedIdentExpression13707 = frozenset([164])
    FOLLOW_IDENT_in_qualifiedIdentExpression13709 = frozenset([29])
    FOLLOW_arguments_in_qualifiedIdentExpression13711 = frozenset([1])
    FOLLOW_IDENT_in_qualifiedIdentExpression13761 = frozenset([29])
    FOLLOW_arguments_in_qualifiedIdentExpression13763 = frozenset([1])
    FOLLOW_THIS_in_qualifiedIdentExpression13838 = frozenset([1])
    FOLLOW_SUPER_in_qualifiedIdentExpression13904 = frozenset([29])
    FOLLOW_arguments_in_qualifiedIdentExpression13906 = frozenset([1])
    FOLLOW_innerNewExpression_in_qualifiedIdentExpression13954 = frozenset([1])
    FOLLOW_NEW_in_newExpression14030 = frozenset([25, 55, 57, 60, 65, 72, 79, 80, 89, 164])
    FOLLOW_primitiveType_in_newExpression14044 = frozenset([22])
    FOLLOW_newArrayConstruction_in_newExpression14046 = frozenset([1])
    FOLLOW_genericTypeArgumentListSimplified_in_newExpression14090 = frozenset([25, 55, 57, 60, 65, 72, 79, 80, 89, 164])
    FOLLOW_qualifiedTypeIdentSimplified_in_newExpression14093 = frozenset([22, 29])
    FOLLOW_newArrayConstruction_in_newExpression14111 = frozenset([1])
    FOLLOW_arguments_in_newExpression14176 = frozenset([1, 23, 25, 68, 75])
    FOLLOW_classBody_in_newExpression14178 = frozenset([1])
    FOLLOW_NEW_in_innerNewExpression14273 = frozenset([25, 164])
    FOLLOW_genericTypeArgumentListSimplified_in_innerNewExpression14275 = frozenset([164])
    FOLLOW_IDENT_in_innerNewExpression14278 = frozenset([29])
    FOLLOW_arguments_in_innerNewExpression14280 = frozenset([1, 23, 25, 68, 75])
    FOLLOW_classBody_in_innerNewExpression14282 = frozenset([1])
    FOLLOW_arrayDeclaratorList_in_newArrayConstruction14328 = frozenset([23])
    FOLLOW_arrayInitializer_in_newArrayConstruction14330 = frozenset([1])
    FOLLOW_LBRACK_in_newArrayConstruction14340 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expression_in_newArrayConstruction14343 = frozenset([41])
    FOLLOW_RBRACK_in_newArrayConstruction14345 = frozenset([1, 22])
    FOLLOW_LBRACK_in_newArrayConstruction14349 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expression_in_newArrayConstruction14352 = frozenset([41])
    FOLLOW_RBRACK_in_newArrayConstruction14354 = frozenset([1, 22])
    FOLLOW_arrayDeclaratorList_in_newArrayConstruction14359 = frozenset([1])
    FOLLOW_LPAREN_in_arguments14379 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 43, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expressionList_in_arguments14381 = frozenset([43])
    FOLLOW_RPAREN_in_arguments14384 = frozenset([1])
    FOLLOW_set_in_literal0 = frozenset([1])
    FOLLOW_GREATER_THAN_in_synpred14_Java5069 = frozenset([1])
    FOLLOW_SHIFT_RIGHT_in_synpred15_Java5079 = frozenset([1])
    FOLLOW_BIT_SHIFT_RIGHT_in_synpred16_Java5089 = frozenset([1])
    FOLLOW_bound_in_synpred17_Java5119 = frozenset([1])
    FOLLOW_STATIC_in_synpred32_Java5619 = frozenset([23])
    FOLLOW_block_in_synpred32_Java5621 = frozenset([1])
    FOLLOW_genericTypeParameterList_in_synpred42_Java5658 = frozenset([55, 57, 60, 65, 72, 79, 80, 89, 101, 164])
    FOLLOW_type_in_synpred42_Java5677 = frozenset([164])
    FOLLOW_IDENT_in_synpred42_Java5679 = frozenset([29])
    FOLLOW_formalParameterList_in_synpred42_Java5681 = frozenset([22, 23, 44, 97])
    FOLLOW_arrayDeclaratorList_in_synpred42_Java5683 = frozenset([23, 44, 97])
    FOLLOW_throwsClause_in_synpred42_Java5686 = frozenset([23, 44])
    FOLLOW_block_in_synpred42_Java5690 = frozenset([1])
    FOLLOW_SEMI_in_synpred42_Java5694 = frozenset([1])
    FOLLOW_VOID_in_synpred42_Java5756 = frozenset([164])
    FOLLOW_IDENT_in_synpred42_Java5758 = frozenset([29])
    FOLLOW_formalParameterList_in_synpred42_Java5760 = frozenset([23, 44, 97])
    FOLLOW_throwsClause_in_synpred42_Java5762 = frozenset([23, 44])
    FOLLOW_block_in_synpred42_Java5766 = frozenset([1])
    FOLLOW_SEMI_in_synpred42_Java5770 = frozenset([1])
    FOLLOW_IDENT_in_synpred42_Java5829 = frozenset([29])
    FOLLOW_formalParameterList_in_synpred42_Java5831 = frozenset([23, 97])
    FOLLOW_throwsClause_in_synpred42_Java5833 = frozenset([23])
    FOLLOW_block_in_synpred42_Java5836 = frozenset([1])
    FOLLOW_modifierList_in_synpred43_Java5644 = frozenset([25, 55, 57, 60, 65, 72, 79, 80, 89, 101, 164])
    FOLLOW_genericTypeParameterList_in_synpred43_Java5658 = frozenset([55, 57, 60, 65, 72, 79, 80, 89, 101, 164])
    FOLLOW_type_in_synpred43_Java5677 = frozenset([164])
    FOLLOW_IDENT_in_synpred43_Java5679 = frozenset([29])
    FOLLOW_formalParameterList_in_synpred43_Java5681 = frozenset([22, 23, 44, 97])
    FOLLOW_arrayDeclaratorList_in_synpred43_Java5683 = frozenset([23, 44, 97])
    FOLLOW_throwsClause_in_synpred43_Java5686 = frozenset([23, 44])
    FOLLOW_block_in_synpred43_Java5690 = frozenset([1])
    FOLLOW_SEMI_in_synpred43_Java5694 = frozenset([1])
    FOLLOW_VOID_in_synpred43_Java5756 = frozenset([164])
    FOLLOW_IDENT_in_synpred43_Java5758 = frozenset([29])
    FOLLOW_formalParameterList_in_synpred43_Java5760 = frozenset([23, 44, 97])
    FOLLOW_throwsClause_in_synpred43_Java5762 = frozenset([23, 44])
    FOLLOW_block_in_synpred43_Java5766 = frozenset([1])
    FOLLOW_SEMI_in_synpred43_Java5770 = frozenset([1])
    FOLLOW_IDENT_in_synpred43_Java5829 = frozenset([29])
    FOLLOW_formalParameterList_in_synpred43_Java5831 = frozenset([23, 97])
    FOLLOW_throwsClause_in_synpred43_Java5833 = frozenset([23])
    FOLLOW_block_in_synpred43_Java5836 = frozenset([1])
    FOLLOW_type_in_synpred43_Java5900 = frozenset([164])
    FOLLOW_classFieldDeclaratorList_in_synpred43_Java5902 = frozenset([44])
    FOLLOW_SEMI_in_synpred43_Java5904 = frozenset([1])
    FOLLOW_typeDeclaration_in_synpred44_Java5949 = frozenset([1])
    FOLLOW_genericTypeParameterList_in_synpred50_Java5993 = frozenset([55, 57, 60, 65, 72, 79, 80, 89, 101, 164])
    FOLLOW_type_in_synpred50_Java6012 = frozenset([164])
    FOLLOW_IDENT_in_synpred50_Java6014 = frozenset([29])
    FOLLOW_formalParameterList_in_synpred50_Java6016 = frozenset([22, 44, 97])
    FOLLOW_arrayDeclaratorList_in_synpred50_Java6018 = frozenset([44, 97])
    FOLLOW_throwsClause_in_synpred50_Java6021 = frozenset([44])
    FOLLOW_SEMI_in_synpred50_Java6024 = frozenset([1])
    FOLLOW_VOID_in_synpred50_Java6082 = frozenset([164])
    FOLLOW_IDENT_in_synpred50_Java6084 = frozenset([29])
    FOLLOW_formalParameterList_in_synpred50_Java6086 = frozenset([44, 97])
    FOLLOW_throwsClause_in_synpred50_Java6088 = frozenset([44])
    FOLLOW_SEMI_in_synpred50_Java6091 = frozenset([1])
    FOLLOW_modifierList_in_synpred51_Java5979 = frozenset([25, 55, 57, 60, 65, 72, 79, 80, 89, 101, 164])
    FOLLOW_genericTypeParameterList_in_synpred51_Java5993 = frozenset([55, 57, 60, 65, 72, 79, 80, 89, 101, 164])
    FOLLOW_type_in_synpred51_Java6012 = frozenset([164])
    FOLLOW_IDENT_in_synpred51_Java6014 = frozenset([29])
    FOLLOW_formalParameterList_in_synpred51_Java6016 = frozenset([22, 44, 97])
    FOLLOW_arrayDeclaratorList_in_synpred51_Java6018 = frozenset([44, 97])
    FOLLOW_throwsClause_in_synpred51_Java6021 = frozenset([44])
    FOLLOW_SEMI_in_synpred51_Java6024 = frozenset([1])
    FOLLOW_VOID_in_synpred51_Java6082 = frozenset([164])
    FOLLOW_IDENT_in_synpred51_Java6084 = frozenset([29])
    FOLLOW_formalParameterList_in_synpred51_Java6086 = frozenset([44, 97])
    FOLLOW_throwsClause_in_synpred51_Java6088 = frozenset([44])
    FOLLOW_SEMI_in_synpred51_Java6091 = frozenset([1])
    FOLLOW_type_in_synpred51_Java6154 = frozenset([164])
    FOLLOW_interfaceFieldDeclaratorList_in_synpred51_Java6156 = frozenset([44])
    FOLLOW_SEMI_in_synpred51_Java6158 = frozenset([1])
    FOLLOW_typeDeclaration_in_synpred52_Java6203 = frozenset([1])
    FOLLOW_arrayDeclarator_in_synpred58_Java6497 = frozenset([1])
    FOLLOW_arrayDeclaratorList_in_synpred76_Java6884 = frozenset([1])
    FOLLOW_arrayDeclaratorList_in_synpred77_Java6927 = frozenset([1])
    FOLLOW_DOT_in_synpred79_Java7012 = frozenset([55, 57, 60, 65, 72, 79, 80, 89, 164])
    FOLLOW_typeIdent_in_synpred79_Java7014 = frozenset([1])
    FOLLOW_COMMA_in_synpred90_Java7237 = frozenset([40, 55, 57, 60, 65, 72, 79, 80, 89, 164])
    FOLLOW_genericTypeArgument_in_synpred90_Java7239 = frozenset([1])
    FOLLOW_genericWildcardBoundType_in_synpred92_Java7293 = frozenset([1])
    FOLLOW_COMMA_in_synpred97_Java7494 = frozenset([7, 53, 55, 57, 60, 65, 70, 72, 79, 80, 81, 85, 86, 87, 89, 90, 91, 94, 98, 102, 164])
    FOLLOW_formalParameterStandardDecl_in_synpred97_Java7496 = frozenset([1])
    FOLLOW_formalParameterStandardDecl_in_synpred99_Java7491 = frozenset([1, 11])
    FOLLOW_COMMA_in_synpred99_Java7494 = frozenset([7, 53, 55, 57, 60, 65, 70, 72, 79, 80, 81, 85, 86, 87, 89, 90, 91, 94, 98, 102, 164])
    FOLLOW_formalParameterStandardDecl_in_synpred99_Java7496 = frozenset([1, 11])
    FOLLOW_COMMA_in_synpred99_Java7501 = frozenset([7, 53, 55, 57, 60, 65, 70, 72, 79, 80, 81, 85, 86, 87, 89, 90, 91, 94, 98, 102, 164])
    FOLLOW_formalParameterVarArgDecl_in_synpred99_Java7503 = frozenset([1])
    FOLLOW_formalParameterVarArgDecl_in_synpred100_Java7558 = frozenset([1])
    FOLLOW_DOT_in_synpred101_Java7789 = frozenset([164])
    FOLLOW_IDENT_in_synpred101_Java7793 = frozenset([1])
    FOLLOW_annotation_in_synpred102_Java7842 = frozenset([1])
    FOLLOW_modifierList_in_synpred114_Java8264 = frozenset([55, 57, 60, 65, 72, 79, 80, 89, 164])
    FOLLOW_type_in_synpred114_Java8266 = frozenset([164])
    FOLLOW_IDENT_in_synpred114_Java8280 = frozenset([29])
    FOLLOW_LPAREN_in_synpred114_Java8282 = frozenset([43])
    FOLLOW_RPAREN_in_synpred114_Java8284 = frozenset([44, 63])
    FOLLOW_annotationDefaultValue_in_synpred114_Java8286 = frozenset([44])
    FOLLOW_SEMI_in_synpred114_Java8289 = frozenset([1])
    FOLLOW_classFieldDeclaratorList_in_synpred114_Java8331 = frozenset([44])
    FOLLOW_SEMI_in_synpred114_Java8333 = frozenset([1])
    FOLLOW_localVariableDeclaration_in_synpred116_Java8464 = frozenset([44])
    FOLLOW_SEMI_in_synpred116_Java8466 = frozenset([1])
    FOLLOW_typeDeclaration_in_synpred117_Java8477 = frozenset([1])
    FOLLOW_ELSE_in_synpred121_Java8757 = frozenset([7, 12, 21, 23, 25, 27, 29, 30, 34, 38, 44, 53, 54, 55, 56, 57, 60, 61, 62, 64, 65, 67, 69, 70, 72, 73, 74, 77, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100, 101, 102, 103, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_statement_in_synpred121_Java8761 = frozenset([1])
    FOLLOW_forInit_in_synpred123_Java8940 = frozenset([44])
    FOLLOW_SEMI_in_synpred123_Java8942 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 44, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_forCondition_in_synpred123_Java8944 = frozenset([44])
    FOLLOW_SEMI_in_synpred123_Java8946 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 43, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_forUpdater_in_synpred123_Java8948 = frozenset([43])
    FOLLOW_RPAREN_in_synpred123_Java8950 = frozenset([7, 12, 21, 23, 25, 27, 29, 30, 34, 38, 44, 53, 54, 55, 56, 57, 60, 61, 62, 64, 65, 67, 69, 70, 72, 73, 74, 77, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100, 101, 102, 103, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_statement_in_synpred123_Java8952 = frozenset([1])
    FOLLOW_localVariableDeclaration_in_synpred146_Java9964 = frozenset([1])
    FOLLOW_expressionList_in_synpred147_Java9986 = frozenset([1])
    FOLLOW_LPAREN_in_synpred190_Java11489 = frozenset([55, 57, 60, 65, 72, 79, 80, 89, 164])
    FOLLOW_type_in_synpred190_Java11491 = frozenset([43])
    FOLLOW_RPAREN_in_synpred190_Java11493 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_unaryExpression_in_synpred190_Java11495 = frozenset([1])
    FOLLOW_arrayDeclarator_in_synpred218_Java13346 = frozenset([15, 22])
    FOLLOW_DOT_in_synpred218_Java13413 = frozenset([61])
    FOLLOW_CLASS_in_synpred218_Java13415 = frozenset([1])
    FOLLOW_DOT_in_synpred226_Java13546 = frozenset([25, 61, 82, 92, 95, 164])
    FOLLOW_CLASS_in_synpred226_Java13564 = frozenset([1])
    FOLLOW_genericTypeArgumentListSimplified_in_synpred226_Java13627 = frozenset([92, 164])
    FOLLOW_SUPER_in_synpred226_Java13651 = frozenset([29])
    FOLLOW_arguments_in_synpred226_Java13653 = frozenset([1])
    FOLLOW_SUPER_in_synpred226_Java13703 = frozenset([15])
    FOLLOW_DOT_in_synpred226_Java13707 = frozenset([164])
    FOLLOW_IDENT_in_synpred226_Java13709 = frozenset([29])
    FOLLOW_arguments_in_synpred226_Java13711 = frozenset([1])
    FOLLOW_IDENT_in_synpred226_Java13761 = frozenset([29])
    FOLLOW_arguments_in_synpred226_Java13763 = frozenset([1])
    FOLLOW_THIS_in_synpred226_Java13838 = frozenset([1])
    FOLLOW_SUPER_in_synpred226_Java13904 = frozenset([29])
    FOLLOW_arguments_in_synpred226_Java13906 = frozenset([1])
    FOLLOW_innerNewExpression_in_synpred226_Java13954 = frozenset([1])
    FOLLOW_LBRACK_in_synpred234_Java14349 = frozenset([12, 21, 23, 25, 27, 29, 30, 34, 38, 55, 57, 60, 65, 69, 72, 79, 80, 82, 83, 89, 92, 95, 99, 101, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expression_in_synpred234_Java14352 = frozenset([41])
    FOLLOW_RBRACK_in_synpred234_Java14354 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("JavaLexer", JavaParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
