# $ANTLR 3.1.1 JavaTreeParser.g 2009-08-26 12:49:39

import sys
from antlr3 import *
from antlr3.tree import *
from antlr3.compat import set, frozenset
                     
from java2python import expression as ex, parameter as px, formatFloatLiteral
from java2python.parser.local import LocalTreeParser



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
BREAK=56
LOGICAL_AND=26
BIT_SHIFT_RIGHT_ASSIGN=9
UNARY_PLUS=159
TYPE=157
FINAL=70
INC=21
RPAREN=43
IMPORT=78
STRING_LITERAL=170
FOR_UPDATE=132
FLOATING_POINT_LITERAL=168
CAST_EXPR=118
NOT_EQUAL=35
VOID_METHOD_DECL=163
RETURN=88
THIS=95
DOUBLE=65
VOID=101
ENUM_TOP_LEVEL_SCOPE=125
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
PROTECTED=86
DEC=12
CLASS=61
LBRACK=22
BIT_SHIFT_RIGHT=8
THROWS_CLAUSE=156
GREATER_OR_EQUAL=19
FOR=73
LOGICAL_NOT=27
THIS_CONSTRUCTOR_CALL=155
FLOAT=72
ABSTRACT=53
AND=4
POST_DEC=147
AND_ASSIGN=5
ANNOTATION_SCOPE=110
MODIFIER_LIST=145
STATIC_ARRAY_CREATOR=152
LPAREN=29
IF=74
AT=7
CONSTRUCTOR_DECL=124
ESCAPE_SEQUENCE=175
LABELED_STATEMENT=141
UNICODE_ESCAPE=176
BOOLEAN=55
SYNCHRONIZED=94
EXPR=126
CLASS_TOP_LEVEL_SCOPE=123
IMPLEMENTS=75
CONTINUE=62
COMMA=11
TRANSIENT=98
XOR_ASSIGN=52
EQUAL=18
LOGICAL_OR=28
ARGUMENT_LIST=112
QUALIFIED_TYPE_IDENT=151
IDENT=164
PLUS=38
ANNOTATION_INIT_BLOCK=105
HEX_LITERAL=165
DOT=15
SHIFT_LEFT_ASSIGN=46
FORMAL_PARAM_LIST=133
GENERIC_TYPE_ARG_LIST=137
DOTSTAR=16
ANNOTATION_TOP_LEVEL_SCOPE=111
BYTE=57
XOR=51
JAVA_ID_PART=179
GREATER_THAN=20
VOLATILE=102
PARENTESIZED_EXPR=146
LESS_OR_EQUAL=24
ARRAY_DECLARATOR_LIST=114
CLASS_STATIC_INITIALIZER=122
DEFAULT=63
OCTAL_LITERAL=166
HEX_DIGIT=171
SHORT=89
INSTANCEOF=76
MINUS=30
SEMI=44
TRUE=99
EXTENDS_CLAUSE=128
STAR_ASSIGN=50
VAR_DECLARATOR_LIST=162
COLON=10
ARRAY_DECLARATOR=113
OR_ASSIGN=37
ENUM=67
QUESTION=40
FINALLY=71
RCURLY=42
ASSIGN=6
PLUS_ASSIGN=39
ANNOTATION_INIT_ARRAY_ELEMENT=104
FUNCTION_METHOD_DECL=136
INTERFACE=77
DIV=13
POST_INC=148
LONG=80
CLASS_CONSTRUCTOR_CALL=120
PUBLIC=87
EXTENDS=68
FOR_EACH=130
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




class JavaTreeParser(LocalTreeParser):
    grammarFileName = "JavaTreeParser.g"
    antlr_version = version_str_to_tuple("3.1.1")
    antlr_version_str = "3.1.1"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        LocalTreeParser.__init__(self, input, state)

        self._state.ruleMemo = {}






                


        

                          
    # placeholder



    # $ANTLR start "javaSource"
    # JavaTreeParser.g:62:1: javaSource[module] : ^( JAVA_SOURCE annotationList ( packageDeclaration )? ( importDeclaration )* ( typeDeclaration )* ) ;
    def javaSource(self, module):

        javaSource_StartIndex = self.input.index()
        self.beginJavaSource(module) 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 1):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:65:5: ( ^( JAVA_SOURCE annotationList ( packageDeclaration )? ( importDeclaration )* ( typeDeclaration )* ) )
                # JavaTreeParser.g:65:9: ^( JAVA_SOURCE annotationList ( packageDeclaration )? ( importDeclaration )* ( typeDeclaration )* )
                pass 
                self.match(self.input, JAVA_SOURCE, self.FOLLOW_JAVA_SOURCE_in_javaSource98)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_annotationList_in_javaSource112)
                self.annotationList()

                self._state.following.pop()
                # JavaTreeParser.g:67:13: ( packageDeclaration )?
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == PACKAGE) :
                    alt1 = 1
                if alt1 == 1:
                    # JavaTreeParser.g:0:0: packageDeclaration
                    pass 
                    self._state.following.append(self.FOLLOW_packageDeclaration_in_javaSource126)
                    self.packageDeclaration()

                    self._state.following.pop()



                # JavaTreeParser.g:68:13: ( importDeclaration )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == IMPORT) :
                        alt2 = 1


                    if alt2 == 1:
                        # JavaTreeParser.g:0:0: importDeclaration
                        pass 
                        self._state.following.append(self.FOLLOW_importDeclaration_in_javaSource141)
                        self.importDeclaration()

                        self._state.following.pop()


                    else:
                        break #loop2


                # JavaTreeParser.g:69:13: ( typeDeclaration )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == AT or LA3_0 == CLASS or LA3_0 == ENUM or LA3_0 == INTERFACE) :
                        alt3 = 1


                    if alt3 == 1:
                        # JavaTreeParser.g:0:0: typeDeclaration
                        pass 
                        self._state.following.append(self.FOLLOW_typeDeclaration_in_javaSource156)
                        self.typeDeclaration()

                        self._state.following.pop()


                    else:
                        break #loop3



                self.match(self.input, UP, None)



                if self._state.backtracking == 0:
                    self.endJavaSource() 


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 1, javaSource_StartIndex, success)

            pass

        return 

    # $ANTLR end "javaSource"


    # $ANTLR start "packageDeclaration"
    # JavaTreeParser.g:74:1: packageDeclaration : ^( PACKAGE qi0= qualifiedIdentifier ) ;
    def packageDeclaration(self, ):

        packageDeclaration_StartIndex = self.input.index()
        qi0 = None


        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 2):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:75:5: ( ^( PACKAGE qi0= qualifiedIdentifier ) )
                # JavaTreeParser.g:75:9: ^( PACKAGE qi0= qualifiedIdentifier )
                pass 
                self.match(self.input, PACKAGE, self.FOLLOW_PACKAGE_in_packageDeclaration188)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_packageDeclaration192)
                qi0 = self.qualifiedIdentifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self.addPackage(qi0) 


                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 2, packageDeclaration_StartIndex, success)

            pass

        return 

    # $ANTLR end "packageDeclaration"


    # $ANTLR start "importDeclaration"
    # JavaTreeParser.g:79:1: importDeclaration : ^( IMPORT ( STATIC )? qualifiedIdentifier ( DOTSTAR )? ) ;
    def importDeclaration(self, ):

        importDeclaration_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 3):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:80:5: ( ^( IMPORT ( STATIC )? qualifiedIdentifier ( DOTSTAR )? ) )
                # JavaTreeParser.g:80:9: ^( IMPORT ( STATIC )? qualifiedIdentifier ( DOTSTAR )? )
                pass 
                self.match(self.input, IMPORT, self.FOLLOW_IMPORT_in_importDeclaration216)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:80:18: ( STATIC )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == STATIC) :
                    alt4 = 1
                if alt4 == 1:
                    # JavaTreeParser.g:0:0: STATIC
                    pass 
                    self.match(self.input, STATIC, self.FOLLOW_STATIC_in_importDeclaration218)



                self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_importDeclaration221)
                self.qualifiedIdentifier()

                self._state.following.pop()
                # JavaTreeParser.g:80:46: ( DOTSTAR )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == DOTSTAR) :
                    alt5 = 1
                if alt5 == 1:
                    # JavaTreeParser.g:0:0: DOTSTAR
                    pass 
                    self.match(self.input, DOTSTAR, self.FOLLOW_DOTSTAR_in_importDeclaration223)




                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 3, importDeclaration_StartIndex, success)

            pass

        return 

    # $ANTLR end "importDeclaration"

    class typeDeclaration_return(TreeRuleReturnScope):
        def __init__(self):
            TreeRuleReturnScope.__init__(self)





    # $ANTLR start "typeDeclaration"
    # JavaTreeParser.g:84:1: typeDeclaration : ( ^( CLASS md0= modifierList id0= IDENT ( genericTypeParameterList )? (ec0= extendsClause )? (ic0= implementsClause )? classTopLevelScope ) | ^( INTERFACE md0= modifierList id0= IDENT ( genericTypeParameterList )? (ec0= extendsClause )? interfaceTopLevelScope ) | ^( ENUM modifierList IDENT ( implementsClause )? enumTopLevelScope ) | ^( AT modifierList IDENT annotationTopLevelScope ) );
    def typeDeclaration(self, ):

        retval = self.typeDeclaration_return()
        retval.start = self.input.LT(1)
        typeDeclaration_StartIndex = self.input.index()
        id0 = None
        md0 = None

        ec0 = None

        ic0 = None


        self.beginTypeDeclaration() 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 4):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # JavaTreeParser.g:90:5: ( ^( CLASS md0= modifierList id0= IDENT ( genericTypeParameterList )? (ec0= extendsClause )? (ic0= implementsClause )? classTopLevelScope ) | ^( INTERFACE md0= modifierList id0= IDENT ( genericTypeParameterList )? (ec0= extendsClause )? interfaceTopLevelScope ) | ^( ENUM modifierList IDENT ( implementsClause )? enumTopLevelScope ) | ^( AT modifierList IDENT annotationTopLevelScope ) )
                alt12 = 4
                LA12 = self.input.LA(1)
                if LA12 == CLASS:
                    alt12 = 1
                elif LA12 == INTERFACE:
                    alt12 = 2
                elif LA12 == ENUM:
                    alt12 = 3
                elif LA12 == AT:
                    alt12 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 12, 0, self.input)

                    raise nvae

                if alt12 == 1:
                    # JavaTreeParser.g:90:9: ^( CLASS md0= modifierList id0= IDENT ( genericTypeParameterList )? (ec0= extendsClause )? (ic0= implementsClause )? classTopLevelScope )
                    pass 
                    self.match(self.input, CLASS, self.FOLLOW_CLASS_in_typeDeclaration265)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_typeDeclaration279)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addModifiers(md0) 

                    id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_typeDeclaration295)
                    if self._state.backtracking == 0:
                        self.setIdent(ident=id0.text) 

                    # JavaTreeParser.g:93:11: ( genericTypeParameterList )?
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == GENERIC_TYPE_PARAM_LIST) :
                        alt6 = 1
                    if alt6 == 1:
                        # JavaTreeParser.g:0:0: genericTypeParameterList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeParameterList_in_typeDeclaration309)
                        self.genericTypeParameterList()

                        self._state.following.pop()



                    # JavaTreeParser.g:94:11: (ec0= extendsClause )?
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == EXTENDS_CLAUSE) :
                        alt7 = 1
                    if alt7 == 1:
                        # JavaTreeParser.g:94:12: ec0= extendsClause
                        pass 
                        self._state.following.append(self.FOLLOW_extendsClause_in_typeDeclaration325)
                        ec0 = self.extendsClause()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self.addBases(ec0) 




                    # JavaTreeParser.g:95:11: (ic0= implementsClause )?
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == IMPLEMENTS_CLAUSE) :
                        alt8 = 1
                    if alt8 == 1:
                        # JavaTreeParser.g:95:12: ic0= implementsClause
                        pass 
                        self._state.following.append(self.FOLLOW_implementsClause_in_typeDeclaration344)
                        ic0 = self.implementsClause()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self.addBases(ic0) 




                    self._state.following.append(self.FOLLOW_classTopLevelScope_in_typeDeclaration360)
                    self.classTopLevelScope()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt12 == 2:
                    # JavaTreeParser.g:99:9: ^( INTERFACE md0= modifierList id0= IDENT ( genericTypeParameterList )? (ec0= extendsClause )? interfaceTopLevelScope )
                    pass 
                    self.match(self.input, INTERFACE, self.FOLLOW_INTERFACE_in_typeDeclaration382)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_typeDeclaration396)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addModifiers(md0) 

                    id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_typeDeclaration412)
                    if self._state.backtracking == 0:
                        self.setIdent(ident=id0.text) 

                    # JavaTreeParser.g:102:11: ( genericTypeParameterList )?
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == GENERIC_TYPE_PARAM_LIST) :
                        alt9 = 1
                    if alt9 == 1:
                        # JavaTreeParser.g:0:0: genericTypeParameterList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeParameterList_in_typeDeclaration426)
                        self.genericTypeParameterList()

                        self._state.following.pop()



                    # JavaTreeParser.g:103:11: (ec0= extendsClause )?
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == EXTENDS_CLAUSE) :
                        alt10 = 1
                    if alt10 == 1:
                        # JavaTreeParser.g:103:12: ec0= extendsClause
                        pass 
                        self._state.following.append(self.FOLLOW_extendsClause_in_typeDeclaration442)
                        ec0 = self.extendsClause()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self.addBases(ec0) 




                    self._state.following.append(self.FOLLOW_interfaceTopLevelScope_in_typeDeclaration458)
                    self.interfaceTopLevelScope()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt12 == 3:
                    # JavaTreeParser.g:107:9: ^( ENUM modifierList IDENT ( implementsClause )? enumTopLevelScope )
                    pass 
                    self.match(self.input, ENUM, self.FOLLOW_ENUM_in_typeDeclaration480)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_typeDeclaration492)
                    self.modifierList()

                    self._state.following.pop()
                    self.match(self.input, IDENT, self.FOLLOW_IDENT_in_typeDeclaration504)
                    # JavaTreeParser.g:110:11: ( implementsClause )?
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == IMPLEMENTS_CLAUSE) :
                        alt11 = 1
                    if alt11 == 1:
                        # JavaTreeParser.g:0:0: implementsClause
                        pass 
                        self._state.following.append(self.FOLLOW_implementsClause_in_typeDeclaration516)
                        self.implementsClause()

                        self._state.following.pop()



                    self._state.following.append(self.FOLLOW_enumTopLevelScope_in_typeDeclaration529)
                    self.enumTopLevelScope()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt12 == 4:
                    # JavaTreeParser.g:114:9: ^( AT modifierList IDENT annotationTopLevelScope )
                    pass 
                    self.match(self.input, AT, self.FOLLOW_AT_in_typeDeclaration551)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_typeDeclaration563)
                    self.modifierList()

                    self._state.following.pop()
                    self.match(self.input, IDENT, self.FOLLOW_IDENT_in_typeDeclaration575)
                    self._state.following.append(self.FOLLOW_annotationTopLevelScope_in_typeDeclaration587)
                    self.annotationTopLevelScope()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                if self._state.backtracking == 0:
                                
                    self.commentHandler(retval.start)
                    self.endTypeDeclaration()
                        


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 4, typeDeclaration_StartIndex, success)

            pass

        return retval

    # $ANTLR end "typeDeclaration"


    # $ANTLR start "extendsClause"
    # JavaTreeParser.g:122:1: extendsClause returns [values] : ^( EXTENDS_CLAUSE (tp0= type )+ ) ;
    def extendsClause(self, ):

        values = None
        extendsClause_StartIndex = self.input.index()
        tp0 = None


        values = [] 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 5):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return values

                # JavaTreeParser.g:124:5: ( ^( EXTENDS_CLAUSE (tp0= type )+ ) )
                # JavaTreeParser.g:124:9: ^( EXTENDS_CLAUSE (tp0= type )+ )
                pass 
                self.match(self.input, EXTENDS_CLAUSE, self.FOLLOW_EXTENDS_CLAUSE_in_extendsClause631)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:124:26: (tp0= type )+
                cnt13 = 0
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == TYPE) :
                        alt13 = 1


                    if alt13 == 1:
                        # JavaTreeParser.g:124:27: tp0= type
                        pass 
                        self._state.following.append(self.FOLLOW_type_in_extendsClause636)
                        tp0 = self.type()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            values.append(((tp0 is not None) and [tp0.value] or [None])[0]) 



                    else:
                        if cnt13 >= 1:
                            break #loop13

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(13, self.input)
                        raise eee

                    cnt13 += 1



                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 5, extendsClause_StartIndex, success)

            pass

        return values

    # $ANTLR end "extendsClause"


    # $ANTLR start "implementsClause"
    # JavaTreeParser.g:128:1: implementsClause returns [values] : ^( IMPLEMENTS_CLAUSE (tp0= type )+ ) ;
    def implementsClause(self, ):

        values = None
        implementsClause_StartIndex = self.input.index()
        tp0 = None


        values = [] 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 6):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return values

                # JavaTreeParser.g:130:5: ( ^( IMPLEMENTS_CLAUSE (tp0= type )+ ) )
                # JavaTreeParser.g:130:9: ^( IMPLEMENTS_CLAUSE (tp0= type )+ )
                pass 
                self.match(self.input, IMPLEMENTS_CLAUSE, self.FOLLOW_IMPLEMENTS_CLAUSE_in_implementsClause675)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:130:29: (tp0= type )+
                cnt14 = 0
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == TYPE) :
                        alt14 = 1


                    if alt14 == 1:
                        # JavaTreeParser.g:130:30: tp0= type
                        pass 
                        self._state.following.append(self.FOLLOW_type_in_implementsClause680)
                        tp0 = self.type()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            values.append(tp0.value) 



                    else:
                        if cnt14 >= 1:
                            break #loop14

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(14, self.input)
                        raise eee

                    cnt14 += 1



                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 6, implementsClause_StartIndex, success)

            pass

        return values

    # $ANTLR end "implementsClause"


    # $ANTLR start "genericTypeParameterList"
    # JavaTreeParser.g:133:1: genericTypeParameterList : ^( GENERIC_TYPE_PARAM_LIST ( genericTypeParameter )+ ) ;
    def genericTypeParameterList(self, ):

        genericTypeParameterList_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 7):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:134:5: ( ^( GENERIC_TYPE_PARAM_LIST ( genericTypeParameter )+ ) )
                # JavaTreeParser.g:134:9: ^( GENERIC_TYPE_PARAM_LIST ( genericTypeParameter )+ )
                pass 
                self.match(self.input, GENERIC_TYPE_PARAM_LIST, self.FOLLOW_GENERIC_TYPE_PARAM_LIST_in_genericTypeParameterList705)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:134:35: ( genericTypeParameter )+
                cnt15 = 0
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == IDENT) :
                        alt15 = 1


                    if alt15 == 1:
                        # JavaTreeParser.g:0:0: genericTypeParameter
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeParameter_in_genericTypeParameterList707)
                        self.genericTypeParameter()

                        self._state.following.pop()


                    else:
                        if cnt15 >= 1:
                            break #loop15

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(15, self.input)
                        raise eee

                    cnt15 += 1



                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 7, genericTypeParameterList_StartIndex, success)

            pass

        return 

    # $ANTLR end "genericTypeParameterList"


    # $ANTLR start "genericTypeParameter"
    # JavaTreeParser.g:137:1: genericTypeParameter : ^( IDENT ( bound )? ) ;
    def genericTypeParameter(self, ):

        genericTypeParameter_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 8):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:138:5: ( ^( IDENT ( bound )? ) )
                # JavaTreeParser.g:138:9: ^( IDENT ( bound )? )
                pass 
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_genericTypeParameter729)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:138:17: ( bound )?
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == EXTENDS_BOUND_LIST) :
                        alt16 = 1
                    if alt16 == 1:
                        # JavaTreeParser.g:0:0: bound
                        pass 
                        self._state.following.append(self.FOLLOW_bound_in_genericTypeParameter731)
                        self.bound()

                        self._state.following.pop()




                    self.match(self.input, UP, None)





                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 8, genericTypeParameter_StartIndex, success)

            pass

        return 

    # $ANTLR end "genericTypeParameter"


    # $ANTLR start "bound"
    # JavaTreeParser.g:141:1: bound : ^( EXTENDS_BOUND_LIST ( type )+ ) ;
    def bound(self, ):

        bound_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 9):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:142:5: ( ^( EXTENDS_BOUND_LIST ( type )+ ) )
                # JavaTreeParser.g:142:9: ^( EXTENDS_BOUND_LIST ( type )+ )
                pass 
                self.match(self.input, EXTENDS_BOUND_LIST, self.FOLLOW_EXTENDS_BOUND_LIST_in_bound753)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:142:30: ( type )+
                cnt17 = 0
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == TYPE) :
                        alt17 = 1


                    if alt17 == 1:
                        # JavaTreeParser.g:0:0: type
                        pass 
                        self._state.following.append(self.FOLLOW_type_in_bound755)
                        self.type()

                        self._state.following.pop()


                    else:
                        if cnt17 >= 1:
                            break #loop17

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(17, self.input)
                        raise eee

                    cnt17 += 1



                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 9, bound_StartIndex, success)

            pass

        return 

    # $ANTLR end "bound"


    # $ANTLR start "enumTopLevelScope"
    # JavaTreeParser.g:145:1: enumTopLevelScope : ^( ENUM_TOP_LEVEL_SCOPE ( enumConstant )+ ( classTopLevelScope )? ) ;
    def enumTopLevelScope(self, ):

        enumTopLevelScope_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 10):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:146:5: ( ^( ENUM_TOP_LEVEL_SCOPE ( enumConstant )+ ( classTopLevelScope )? ) )
                # JavaTreeParser.g:146:9: ^( ENUM_TOP_LEVEL_SCOPE ( enumConstant )+ ( classTopLevelScope )? )
                pass 
                self.match(self.input, ENUM_TOP_LEVEL_SCOPE, self.FOLLOW_ENUM_TOP_LEVEL_SCOPE_in_enumTopLevelScope777)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:146:32: ( enumConstant )+
                cnt18 = 0
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == IDENT) :
                        alt18 = 1


                    if alt18 == 1:
                        # JavaTreeParser.g:0:0: enumConstant
                        pass 
                        self._state.following.append(self.FOLLOW_enumConstant_in_enumTopLevelScope779)
                        self.enumConstant()

                        self._state.following.pop()


                    else:
                        if cnt18 >= 1:
                            break #loop18

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(18, self.input)
                        raise eee

                    cnt18 += 1


                # JavaTreeParser.g:146:46: ( classTopLevelScope )?
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == CLASS_TOP_LEVEL_SCOPE) :
                    alt19 = 1
                if alt19 == 1:
                    # JavaTreeParser.g:0:0: classTopLevelScope
                    pass 
                    self._state.following.append(self.FOLLOW_classTopLevelScope_in_enumTopLevelScope782)
                    self.classTopLevelScope()

                    self._state.following.pop()




                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 10, enumTopLevelScope_StartIndex, success)

            pass

        return 

    # $ANTLR end "enumTopLevelScope"


    # $ANTLR start "enumConstant"
    # JavaTreeParser.g:149:1: enumConstant : ^( IDENT annotationList ( arguments )? ( classTopLevelScope )? ) ;
    def enumConstant(self, ):

        enumConstant_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 11):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:150:5: ( ^( IDENT annotationList ( arguments )? ( classTopLevelScope )? ) )
                # JavaTreeParser.g:150:9: ^( IDENT annotationList ( arguments )? ( classTopLevelScope )? )
                pass 
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_enumConstant804)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_annotationList_in_enumConstant806)
                self.annotationList()

                self._state.following.pop()
                # JavaTreeParser.g:150:32: ( arguments )?
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == ARGUMENT_LIST) :
                    alt20 = 1
                if alt20 == 1:
                    # JavaTreeParser.g:0:0: arguments
                    pass 
                    self._state.following.append(self.FOLLOW_arguments_in_enumConstant808)
                    self.arguments()

                    self._state.following.pop()



                # JavaTreeParser.g:150:43: ( classTopLevelScope )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == CLASS_TOP_LEVEL_SCOPE) :
                    alt21 = 1
                if alt21 == 1:
                    # JavaTreeParser.g:0:0: classTopLevelScope
                    pass 
                    self._state.following.append(self.FOLLOW_classTopLevelScope_in_enumConstant811)
                    self.classTopLevelScope()

                    self._state.following.pop()




                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 11, enumConstant_StartIndex, success)

            pass

        return 

    # $ANTLR end "enumConstant"


    # $ANTLR start "classTopLevelScope"
    # JavaTreeParser.g:154:1: classTopLevelScope : ^( CLASS_TOP_LEVEL_SCOPE ( classScopeDeclarations )* ) ;
    def classTopLevelScope(self, ):

        classTopLevelScope_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 12):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:155:5: ( ^( CLASS_TOP_LEVEL_SCOPE ( classScopeDeclarations )* ) )
                # JavaTreeParser.g:155:9: ^( CLASS_TOP_LEVEL_SCOPE ( classScopeDeclarations )* )
                pass 
                self.match(self.input, CLASS_TOP_LEVEL_SCOPE, self.FOLLOW_CLASS_TOP_LEVEL_SCOPE_in_classTopLevelScope834)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:155:33: ( classScopeDeclarations )*
                    while True: #loop22
                        alt22 = 2
                        LA22_0 = self.input.LA(1)

                        if (LA22_0 == AT or LA22_0 == CLASS or LA22_0 == ENUM or LA22_0 == INTERFACE or (CLASS_INSTANCE_INITIALIZER <= LA22_0 <= CLASS_STATIC_INITIALIZER) or LA22_0 == CONSTRUCTOR_DECL or LA22_0 == FUNCTION_METHOD_DECL or LA22_0 == VAR_DECLARATION or LA22_0 == VOID_METHOD_DECL) :
                            alt22 = 1


                        if alt22 == 1:
                            # JavaTreeParser.g:0:0: classScopeDeclarations
                            pass 
                            self._state.following.append(self.FOLLOW_classScopeDeclarations_in_classTopLevelScope836)
                            self.classScopeDeclarations()

                            self._state.following.pop()


                        else:
                            break #loop22



                    self.match(self.input, UP, None)





                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 12, classTopLevelScope_StartIndex, success)

            pass

        return 

    # $ANTLR end "classTopLevelScope"


    # $ANTLR start "classScopeDeclarations"
    # JavaTreeParser.g:158:1: classScopeDeclarations : ( ^( CLASS_INSTANCE_INITIALIZER block ) | ^( CLASS_STATIC_INITIALIZER block ) | ^( FUNCTION_METHOD_DECL md0= modifierList ( genericTypeParameterList )? tp0= type id0= IDENT fp0= formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block )? ) | ^( VOID_METHOD_DECL md0= modifierList ( genericTypeParameterList )? id0= IDENT fp0= formalParameterList ( throwsClause )? ( block )? ) | ^( VAR_DECLARATION md0= modifierList tp0= type vd0= variableDeclaratorList ) | ^( CONSTRUCTOR_DECL md0= modifierList ( genericTypeParameterList )? fp0= formalParameterList ( throwsClause )? block ) | typeDeclaration );
    def classScopeDeclarations(self, ):

        classScopeDeclarations_StartIndex = self.input.index()
        id0 = None
        md0 = None

        tp0 = None

        fp0 = None

        vd0 = None


        self.beginClassScopeDecls() 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 13):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:162:5: ( ^( CLASS_INSTANCE_INITIALIZER block ) | ^( CLASS_STATIC_INITIALIZER block ) | ^( FUNCTION_METHOD_DECL md0= modifierList ( genericTypeParameterList )? tp0= type id0= IDENT fp0= formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block )? ) | ^( VOID_METHOD_DECL md0= modifierList ( genericTypeParameterList )? id0= IDENT fp0= formalParameterList ( throwsClause )? ( block )? ) | ^( VAR_DECLARATION md0= modifierList tp0= type vd0= variableDeclaratorList ) | ^( CONSTRUCTOR_DECL md0= modifierList ( genericTypeParameterList )? fp0= formalParameterList ( throwsClause )? block ) | typeDeclaration )
                alt32 = 7
                LA32 = self.input.LA(1)
                if LA32 == CLASS_INSTANCE_INITIALIZER:
                    alt32 = 1
                elif LA32 == CLASS_STATIC_INITIALIZER:
                    alt32 = 2
                elif LA32 == FUNCTION_METHOD_DECL:
                    alt32 = 3
                elif LA32 == VOID_METHOD_DECL:
                    alt32 = 4
                elif LA32 == VAR_DECLARATION:
                    alt32 = 5
                elif LA32 == CONSTRUCTOR_DECL:
                    alt32 = 6
                elif LA32 == AT or LA32 == CLASS or LA32 == ENUM or LA32 == INTERFACE:
                    alt32 = 7
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 32, 0, self.input)

                    raise nvae

                if alt32 == 1:
                    # JavaTreeParser.g:162:9: ^( CLASS_INSTANCE_INITIALIZER block )
                    pass 
                    self.match(self.input, CLASS_INSTANCE_INITIALIZER, self.FOLLOW_CLASS_INSTANCE_INITIALIZER_in_classScopeDeclarations878)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_block_in_classScopeDeclarations880)
                    self.block()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt32 == 2:
                    # JavaTreeParser.g:164:9: ^( CLASS_STATIC_INITIALIZER block )
                    pass 
                    self.match(self.input, CLASS_STATIC_INITIALIZER, self.FOLLOW_CLASS_STATIC_INITIALIZER_in_classScopeDeclarations893)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_block_in_classScopeDeclarations895)
                    self.block()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt32 == 3:
                    # JavaTreeParser.g:166:9: ^( FUNCTION_METHOD_DECL md0= modifierList ( genericTypeParameterList )? tp0= type id0= IDENT fp0= formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block )? )
                    pass 
                    self.match(self.input, FUNCTION_METHOD_DECL, self.FOLLOW_FUNCTION_METHOD_DECL_in_classScopeDeclarations908)

                    if self._state.backtracking == 0:
                        self.beginMethodDecl() 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_classScopeDeclarations934)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addModifiers(md0) 

                    # JavaTreeParser.g:169:11: ( genericTypeParameterList )?
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == GENERIC_TYPE_PARAM_LIST) :
                        alt23 = 1
                    if alt23 == 1:
                        # JavaTreeParser.g:0:0: genericTypeParameterList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeParameterList_in_classScopeDeclarations948)
                        self.genericTypeParameterList()

                        self._state.following.pop()



                    self._state.following.append(self.FOLLOW_type_in_classScopeDeclarations963)
                    tp0 = self.type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.setType(((tp0 is not None) and [tp0.value] or [None])[0]) 

                    id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_classScopeDeclarations979)
                    if self._state.backtracking == 0:
                        self.setIdent(ident=id0.text) 

                    self._state.following.append(self.FOLLOW_formalParameterList_in_classScopeDeclarations995)
                    fp0 = self.formalParameterList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addParameters(fp0) 

                    # JavaTreeParser.g:173:11: ( arrayDeclaratorList )?
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == ARRAY_DECLARATOR_LIST) :
                        alt24 = 1
                    if alt24 == 1:
                        # JavaTreeParser.g:0:0: arrayDeclaratorList
                        pass 
                        self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_classScopeDeclarations1009)
                        self.arrayDeclaratorList()

                        self._state.following.pop()



                    # JavaTreeParser.g:174:11: ( throwsClause )?
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == THROWS_CLAUSE) :
                        alt25 = 1
                    if alt25 == 1:
                        # JavaTreeParser.g:0:0: throwsClause
                        pass 
                        self._state.following.append(self.FOLLOW_throwsClause_in_classScopeDeclarations1022)
                        self.throwsClause()

                        self._state.following.pop()



                    # JavaTreeParser.g:175:11: ( block )?
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == BLOCK_SCOPE) :
                        alt26 = 1
                    if alt26 == 1:
                        # JavaTreeParser.g:0:0: block
                        pass 
                        self._state.following.append(self.FOLLOW_block_in_classScopeDeclarations1035)
                        self.block()

                        self._state.following.pop()



                    if self._state.backtracking == 0:
                        self.endMethodDecl() 


                    self.match(self.input, UP, None)


                elif alt32 == 4:
                    # JavaTreeParser.g:179:9: ^( VOID_METHOD_DECL md0= modifierList ( genericTypeParameterList )? id0= IDENT fp0= formalParameterList ( throwsClause )? ( block )? )
                    pass 
                    self.match(self.input, VOID_METHOD_DECL, self.FOLLOW_VOID_METHOD_DECL_in_classScopeDeclarations1070)

                    if self._state.backtracking == 0:
                        self.beginMethodDecl() 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_classScopeDeclarations1096)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addModifiers(md0) 

                    # JavaTreeParser.g:182:11: ( genericTypeParameterList )?
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == GENERIC_TYPE_PARAM_LIST) :
                        alt27 = 1
                    if alt27 == 1:
                        # JavaTreeParser.g:0:0: genericTypeParameterList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeParameterList_in_classScopeDeclarations1110)
                        self.genericTypeParameterList()

                        self._state.following.pop()



                    id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_classScopeDeclarations1125)
                    if self._state.backtracking == 0:
                        self.setIdent(ident=id0.text) 

                    self._state.following.append(self.FOLLOW_formalParameterList_in_classScopeDeclarations1141)
                    fp0 = self.formalParameterList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addParameters(fp0) 

                    # JavaTreeParser.g:185:11: ( throwsClause )?
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == THROWS_CLAUSE) :
                        alt28 = 1
                    if alt28 == 1:
                        # JavaTreeParser.g:0:0: throwsClause
                        pass 
                        self._state.following.append(self.FOLLOW_throwsClause_in_classScopeDeclarations1155)
                        self.throwsClause()

                        self._state.following.pop()



                    # JavaTreeParser.g:186:11: ( block )?
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if (LA29_0 == BLOCK_SCOPE) :
                        alt29 = 1
                    if alt29 == 1:
                        # JavaTreeParser.g:0:0: block
                        pass 
                        self._state.following.append(self.FOLLOW_block_in_classScopeDeclarations1168)
                        self.block()

                        self._state.following.pop()



                    if self._state.backtracking == 0:
                                   
                        self.setType('void')
                        self.endMethodDecl()
                                  


                    self.match(self.input, UP, None)


                elif alt32 == 5:
                    # JavaTreeParser.g:193:9: ^( VAR_DECLARATION md0= modifierList tp0= type vd0= variableDeclaratorList )
                    pass 
                    self.match(self.input, VAR_DECLARATION, self.FOLLOW_VAR_DECLARATION_in_classScopeDeclarations1204)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_classScopeDeclarations1218)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_type_in_classScopeDeclarations1232)
                    tp0 = self.type()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_variableDeclaratorList_in_classScopeDeclarations1246)
                    vd0 = self.variableDeclaratorList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addClassVariables(vd0, ((tp0 is not None) and [tp0.value] or [None])[0], md0) 


                    self.match(self.input, UP, None)


                elif alt32 == 6:
                    # JavaTreeParser.g:200:9: ^( CONSTRUCTOR_DECL md0= modifierList ( genericTypeParameterList )? fp0= formalParameterList ( throwsClause )? block )
                    pass 
                    self.match(self.input, CONSTRUCTOR_DECL, self.FOLLOW_CONSTRUCTOR_DECL_in_classScopeDeclarations1280)

                    if self._state.backtracking == 0:
                        self.beginMethodDecl() 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_classScopeDeclarations1306)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addModifiers(md0) 

                    # JavaTreeParser.g:203:11: ( genericTypeParameterList )?
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == GENERIC_TYPE_PARAM_LIST) :
                        alt30 = 1
                    if alt30 == 1:
                        # JavaTreeParser.g:0:0: genericTypeParameterList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeParameterList_in_classScopeDeclarations1320)
                        self.genericTypeParameterList()

                        self._state.following.pop()



                    self._state.following.append(self.FOLLOW_formalParameterList_in_classScopeDeclarations1335)
                    fp0 = self.formalParameterList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addParameters(fp0) 

                    # JavaTreeParser.g:205:11: ( throwsClause )?
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == THROWS_CLAUSE) :
                        alt31 = 1
                    if alt31 == 1:
                        # JavaTreeParser.g:0:0: throwsClause
                        pass 
                        self._state.following.append(self.FOLLOW_throwsClause_in_classScopeDeclarations1349)
                        self.throwsClause()

                        self._state.following.pop()



                    self._state.following.append(self.FOLLOW_block_in_classScopeDeclarations1362)
                    self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                                   
                        self.setIdent("__init__")
                        self.endMethodDecl()
                                  


                    self.match(self.input, UP, None)


                elif alt32 == 7:
                    # JavaTreeParser.g:213:9: typeDeclaration
                    pass 
                    self._state.following.append(self.FOLLOW_typeDeclaration_in_classScopeDeclarations1395)
                    self.typeDeclaration()

                    self._state.following.pop()


                if self._state.backtracking == 0:
                    self.endClassScopeDecls() 


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 13, classScopeDeclarations_StartIndex, success)

            pass

        return 

    # $ANTLR end "classScopeDeclarations"


    # $ANTLR start "interfaceTopLevelScope"
    # JavaTreeParser.g:217:1: interfaceTopLevelScope : ^( INTERFACE_TOP_LEVEL_SCOPE ( interfaceScopeDeclarations )* ) ;
    def interfaceTopLevelScope(self, ):

        interfaceTopLevelScope_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 14):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:218:5: ( ^( INTERFACE_TOP_LEVEL_SCOPE ( interfaceScopeDeclarations )* ) )
                # JavaTreeParser.g:218:9: ^( INTERFACE_TOP_LEVEL_SCOPE ( interfaceScopeDeclarations )* )
                pass 
                self.match(self.input, INTERFACE_TOP_LEVEL_SCOPE, self.FOLLOW_INTERFACE_TOP_LEVEL_SCOPE_in_interfaceTopLevelScope1416)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:218:37: ( interfaceScopeDeclarations )*
                    while True: #loop33
                        alt33 = 2
                        LA33_0 = self.input.LA(1)

                        if (LA33_0 == AT or LA33_0 == CLASS or LA33_0 == ENUM or LA33_0 == INTERFACE or LA33_0 == FUNCTION_METHOD_DECL or LA33_0 == VAR_DECLARATION or LA33_0 == VOID_METHOD_DECL) :
                            alt33 = 1


                        if alt33 == 1:
                            # JavaTreeParser.g:0:0: interfaceScopeDeclarations
                            pass 
                            self._state.following.append(self.FOLLOW_interfaceScopeDeclarations_in_interfaceTopLevelScope1418)
                            self.interfaceScopeDeclarations()

                            self._state.following.pop()


                        else:
                            break #loop33



                    self.match(self.input, UP, None)





                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 14, interfaceTopLevelScope_StartIndex, success)

            pass

        return 

    # $ANTLR end "interfaceTopLevelScope"


    # $ANTLR start "interfaceScopeDeclarations"
    # JavaTreeParser.g:221:1: interfaceScopeDeclarations : ( ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ) | ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ) | ^( VAR_DECLARATION md1= modifierList tp1= type vd1= variableDeclaratorList ) | typeDeclaration );
    def interfaceScopeDeclarations(self, ):

        interfaceScopeDeclarations_StartIndex = self.input.index()
        md1 = None

        tp1 = None

        vd1 = None


        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 15):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:222:5: ( ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ) | ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ) | ^( VAR_DECLARATION md1= modifierList tp1= type vd1= variableDeclaratorList ) | typeDeclaration )
                alt39 = 4
                LA39 = self.input.LA(1)
                if LA39 == FUNCTION_METHOD_DECL:
                    alt39 = 1
                elif LA39 == VOID_METHOD_DECL:
                    alt39 = 2
                elif LA39 == VAR_DECLARATION:
                    alt39 = 3
                elif LA39 == AT or LA39 == CLASS or LA39 == ENUM or LA39 == INTERFACE:
                    alt39 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 39, 0, self.input)

                    raise nvae

                if alt39 == 1:
                    # JavaTreeParser.g:222:9: ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? )
                    pass 
                    self.match(self.input, FUNCTION_METHOD_DECL, self.FOLLOW_FUNCTION_METHOD_DECL_in_interfaceScopeDeclarations1440)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_interfaceScopeDeclarations1442)
                    self.modifierList()

                    self._state.following.pop()
                    # JavaTreeParser.g:222:45: ( genericTypeParameterList )?
                    alt34 = 2
                    LA34_0 = self.input.LA(1)

                    if (LA34_0 == GENERIC_TYPE_PARAM_LIST) :
                        alt34 = 1
                    if alt34 == 1:
                        # JavaTreeParser.g:0:0: genericTypeParameterList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeParameterList_in_interfaceScopeDeclarations1444)
                        self.genericTypeParameterList()

                        self._state.following.pop()



                    self._state.following.append(self.FOLLOW_type_in_interfaceScopeDeclarations1447)
                    self.type()

                    self._state.following.pop()
                    self.match(self.input, IDENT, self.FOLLOW_IDENT_in_interfaceScopeDeclarations1449)
                    self._state.following.append(self.FOLLOW_formalParameterList_in_interfaceScopeDeclarations1451)
                    self.formalParameterList()

                    self._state.following.pop()
                    # JavaTreeParser.g:222:102: ( arrayDeclaratorList )?
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if (LA35_0 == ARRAY_DECLARATOR_LIST) :
                        alt35 = 1
                    if alt35 == 1:
                        # JavaTreeParser.g:0:0: arrayDeclaratorList
                        pass 
                        self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_interfaceScopeDeclarations1453)
                        self.arrayDeclaratorList()

                        self._state.following.pop()



                    # JavaTreeParser.g:222:123: ( throwsClause )?
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if (LA36_0 == THROWS_CLAUSE) :
                        alt36 = 1
                    if alt36 == 1:
                        # JavaTreeParser.g:0:0: throwsClause
                        pass 
                        self._state.following.append(self.FOLLOW_throwsClause_in_interfaceScopeDeclarations1456)
                        self.throwsClause()

                        self._state.following.pop()




                    self.match(self.input, UP, None)


                elif alt39 == 2:
                    # JavaTreeParser.g:223:9: ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? )
                    pass 
                    self.match(self.input, VOID_METHOD_DECL, self.FOLLOW_VOID_METHOD_DECL_in_interfaceScopeDeclarations1469)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_interfaceScopeDeclarations1471)
                    self.modifierList()

                    self._state.following.pop()
                    # JavaTreeParser.g:223:41: ( genericTypeParameterList )?
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == GENERIC_TYPE_PARAM_LIST) :
                        alt37 = 1
                    if alt37 == 1:
                        # JavaTreeParser.g:0:0: genericTypeParameterList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeParameterList_in_interfaceScopeDeclarations1473)
                        self.genericTypeParameterList()

                        self._state.following.pop()



                    self.match(self.input, IDENT, self.FOLLOW_IDENT_in_interfaceScopeDeclarations1476)
                    self._state.following.append(self.FOLLOW_formalParameterList_in_interfaceScopeDeclarations1478)
                    self.formalParameterList()

                    self._state.following.pop()
                    # JavaTreeParser.g:223:93: ( throwsClause )?
                    alt38 = 2
                    LA38_0 = self.input.LA(1)

                    if (LA38_0 == THROWS_CLAUSE) :
                        alt38 = 1
                    if alt38 == 1:
                        # JavaTreeParser.g:0:0: throwsClause
                        pass 
                        self._state.following.append(self.FOLLOW_throwsClause_in_interfaceScopeDeclarations1480)
                        self.throwsClause()

                        self._state.following.pop()




                    self.match(self.input, UP, None)


                elif alt39 == 3:
                    # JavaTreeParser.g:227:9: ^( VAR_DECLARATION md1= modifierList tp1= type vd1= variableDeclaratorList )
                    pass 
                    self.match(self.input, VAR_DECLARATION, self.FOLLOW_VAR_DECLARATION_in_interfaceScopeDeclarations1571)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_interfaceScopeDeclarations1585)
                    md1 = self.modifierList()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_type_in_interfaceScopeDeclarations1599)
                    tp1 = self.type()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_variableDeclaratorList_in_interfaceScopeDeclarations1613)
                    vd1 = self.variableDeclaratorList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addClassVariables(vd1, ((tp1 is not None) and [tp1.value] or [None])[0], md1) 


                    self.match(self.input, UP, None)


                elif alt39 == 4:
                    # JavaTreeParser.g:234:9: typeDeclaration
                    pass 
                    self._state.following.append(self.FOLLOW_typeDeclaration_in_interfaceScopeDeclarations1646)
                    self.typeDeclaration()

                    self._state.following.pop()



                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 15, interfaceScopeDeclarations_StartIndex, success)

            pass

        return 

    # $ANTLR end "interfaceScopeDeclarations"


    # $ANTLR start "variableDeclaratorList"
    # JavaTreeParser.g:237:1: variableDeclaratorList returns [values] : ^( VAR_DECLARATOR_LIST (vd0= variableDeclarator )+ ) ;
    def variableDeclaratorList(self, ):

        values = None
        variableDeclaratorList_StartIndex = self.input.index()
        vd0 = None


        values = [] 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 16):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return values

                # JavaTreeParser.g:239:5: ( ^( VAR_DECLARATOR_LIST (vd0= variableDeclarator )+ ) )
                # JavaTreeParser.g:239:9: ^( VAR_DECLARATOR_LIST (vd0= variableDeclarator )+ )
                pass 
                self.match(self.input, VAR_DECLARATOR_LIST, self.FOLLOW_VAR_DECLARATOR_LIST_in_variableDeclaratorList1679)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:239:31: (vd0= variableDeclarator )+
                cnt40 = 0
                while True: #loop40
                    alt40 = 2
                    LA40_0 = self.input.LA(1)

                    if (LA40_0 == VAR_DECLARATOR) :
                        alt40 = 1


                    if alt40 == 1:
                        # JavaTreeParser.g:239:32: vd0= variableDeclarator
                        pass 
                        self._state.following.append(self.FOLLOW_variableDeclarator_in_variableDeclaratorList1684)
                        vd0 = self.variableDeclarator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            values.append(vd0) 



                    else:
                        if cnt40 >= 1:
                            break #loop40

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(40, self.input)
                        raise eee

                    cnt40 += 1



                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 16, variableDeclaratorList_StartIndex, success)

            pass

        return values

    # $ANTLR end "variableDeclaratorList"


    # $ANTLR start "variableDeclarator"
    # JavaTreeParser.g:242:1: variableDeclarator returns [value] : ^( VAR_DECLARATOR vd0= variableDeclaratorId (vi0= variableInitializer )? ) ;
    def variableDeclarator(self, ):

        value = None
        variableDeclarator_StartIndex = self.input.index()
        vd0 = None

        vi0 = None


        value = ex(format="${left}") 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 17):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:244:5: ( ^( VAR_DECLARATOR vd0= variableDeclaratorId (vi0= variableInitializer )? ) )
                # JavaTreeParser.g:244:9: ^( VAR_DECLARATOR vd0= variableDeclaratorId (vi0= variableInitializer )? )
                pass 
                self.match(self.input, VAR_DECLARATOR, self.FOLLOW_VAR_DECLARATOR_in_variableDeclarator1723)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_variableDeclaratorId_in_variableDeclarator1737)
                vd0 = self.variableDeclaratorId()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    value.update(left=vd0) 

                # JavaTreeParser.g:246:11: (vi0= variableInitializer )?
                alt41 = 2
                LA41_0 = self.input.LA(1)

                if (LA41_0 == ARRAY_INITIALIZER or LA41_0 == EXPR) :
                    alt41 = 1
                if alt41 == 1:
                    # JavaTreeParser.g:246:12: vi0= variableInitializer
                    pass 
                    self._state.following.append(self.FOLLOW_variableInitializer_in_variableDeclarator1754)
                    vi0 = self.variableInitializer()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value.update(right=vi0, format="${left} = ${right}") 





                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 17, variableDeclarator_StartIndex, success)

            pass

        return value

    # $ANTLR end "variableDeclarator"


    # $ANTLR start "variableDeclaratorId"
    # JavaTreeParser.g:250:1: variableDeclaratorId returns [value] : ^( IDENT ( arrayDeclaratorList )? ) ;
    def variableDeclaratorId(self, ):

        value = None
        variableDeclaratorId_StartIndex = self.input.index()
        IDENT1 = None

        value = ex(format="${left}") 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 18):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:252:5: ( ^( IDENT ( arrayDeclaratorList )? ) )
                # JavaTreeParser.g:252:9: ^( IDENT ( arrayDeclaratorList )? )
                pass 
                IDENT1=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_variableDeclaratorId1802)

                if self._state.backtracking == 0:
                    value.update(left=IDENT1.text, rename=True, ident=IDENT1.text) 


                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:253:11: ( arrayDeclaratorList )?
                    alt42 = 2
                    LA42_0 = self.input.LA(1)

                    if (LA42_0 == ARRAY_DECLARATOR_LIST) :
                        alt42 = 1
                    if alt42 == 1:
                        # JavaTreeParser.g:253:12: arrayDeclaratorList
                        pass 
                        self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_variableDeclaratorId1817)
                        self.arrayDeclaratorList()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            value.update(right="[]", format="${left} = ${right}", array=True) 





                    self.match(self.input, UP, None)





                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 18, variableDeclaratorId_StartIndex, success)

            pass

        return value

    # $ANTLR end "variableDeclaratorId"


    # $ANTLR start "variableInitializer"
    # JavaTreeParser.g:257:1: variableInitializer returns [value] : (ai0= arrayInitializer | ex0= expression );
    def variableInitializer(self, ):

        value = None
        variableInitializer_StartIndex = self.input.index()
        ai0 = None

        ex0 = None


        value = ex(format="${left}") 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 19):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:259:5: (ai0= arrayInitializer | ex0= expression )
                alt43 = 2
                LA43_0 = self.input.LA(1)

                if (LA43_0 == ARRAY_INITIALIZER) :
                    alt43 = 1
                elif (LA43_0 == EXPR) :
                    alt43 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 43, 0, self.input)

                    raise nvae

                if alt43 == 1:
                    # JavaTreeParser.g:259:9: ai0= arrayInitializer
                    pass 
                    self._state.following.append(self.FOLLOW_arrayInitializer_in_variableInitializer1865)
                    ai0 = self.arrayInitializer()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value.update(left=ai0) 



                elif alt43 == 2:
                    # JavaTreeParser.g:260:9: ex0= expression
                    pass 
                    self._state.following.append(self.FOLLOW_expression_in_variableInitializer1879)
                    ex0 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value.update(left=ex0) 




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 19, variableInitializer_StartIndex, success)

            pass

        return value

    # $ANTLR end "variableInitializer"


    # $ANTLR start "arrayDeclarator"
    # JavaTreeParser.g:263:1: arrayDeclarator : LBRACK RBRACK ;
    def arrayDeclarator(self, ):

        arrayDeclarator_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 20):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:264:5: ( LBRACK RBRACK )
                # JavaTreeParser.g:264:9: LBRACK RBRACK
                pass 
                self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_arrayDeclarator1906)
                self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_arrayDeclarator1908)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 20, arrayDeclarator_StartIndex, success)

            pass

        return 

    # $ANTLR end "arrayDeclarator"


    # $ANTLR start "arrayDeclaratorList"
    # JavaTreeParser.g:267:1: arrayDeclaratorList : ^( ARRAY_DECLARATOR_LIST ( ARRAY_DECLARATOR )* ) ;
    def arrayDeclaratorList(self, ):

        arrayDeclaratorList_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 21):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:268:5: ( ^( ARRAY_DECLARATOR_LIST ( ARRAY_DECLARATOR )* ) )
                # JavaTreeParser.g:268:9: ^( ARRAY_DECLARATOR_LIST ( ARRAY_DECLARATOR )* )
                pass 
                self.match(self.input, ARRAY_DECLARATOR_LIST, self.FOLLOW_ARRAY_DECLARATOR_LIST_in_arrayDeclaratorList1928)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:268:33: ( ARRAY_DECLARATOR )*
                    while True: #loop44
                        alt44 = 2
                        LA44_0 = self.input.LA(1)

                        if (LA44_0 == ARRAY_DECLARATOR) :
                            alt44 = 1


                        if alt44 == 1:
                            # JavaTreeParser.g:0:0: ARRAY_DECLARATOR
                            pass 
                            self.match(self.input, ARRAY_DECLARATOR, self.FOLLOW_ARRAY_DECLARATOR_in_arrayDeclaratorList1930)


                        else:
                            break #loop44



                    self.match(self.input, UP, None)





                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 21, arrayDeclaratorList_StartIndex, success)

            pass

        return 

    # $ANTLR end "arrayDeclaratorList"


    # $ANTLR start "arrayInitializer"
    # JavaTreeParser.g:271:1: arrayInitializer returns [value] : ^( ARRAY_INITIALIZER ( variableInitializer )* ) ;
    def arrayInitializer(self, ):

        value = None
        arrayInitializer_StartIndex = self.input.index()
        value = ex() 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 22):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:273:5: ( ^( ARRAY_INITIALIZER ( variableInitializer )* ) )
                # JavaTreeParser.g:273:9: ^( ARRAY_INITIALIZER ( variableInitializer )* )
                pass 
                self.match(self.input, ARRAY_INITIALIZER, self.FOLLOW_ARRAY_INITIALIZER_in_arrayInitializer1965)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:273:29: ( variableInitializer )*
                    while True: #loop45
                        alt45 = 2
                        LA45_0 = self.input.LA(1)

                        if (LA45_0 == ARRAY_INITIALIZER or LA45_0 == EXPR) :
                            alt45 = 1


                        if alt45 == 1:
                            # JavaTreeParser.g:0:0: variableInitializer
                            pass 
                            self._state.following.append(self.FOLLOW_variableInitializer_in_arrayInitializer1967)
                            self.variableInitializer()

                            self._state.following.pop()


                        else:
                            break #loop45



                    self.match(self.input, UP, None)





                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 22, arrayInitializer_StartIndex, success)

            pass

        return value

    # $ANTLR end "arrayInitializer"


    # $ANTLR start "throwsClause"
    # JavaTreeParser.g:276:1: throwsClause : ^( THROWS_CLAUSE ( qualifiedIdentifier )+ ) ;
    def throwsClause(self, ):

        throwsClause_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 23):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:277:5: ( ^( THROWS_CLAUSE ( qualifiedIdentifier )+ ) )
                # JavaTreeParser.g:277:9: ^( THROWS_CLAUSE ( qualifiedIdentifier )+ )
                pass 
                self.match(self.input, THROWS_CLAUSE, self.FOLLOW_THROWS_CLAUSE_in_throwsClause1989)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:277:25: ( qualifiedIdentifier )+
                cnt46 = 0
                while True: #loop46
                    alt46 = 2
                    LA46_0 = self.input.LA(1)

                    if (LA46_0 == DOT or LA46_0 == IDENT) :
                        alt46 = 1


                    if alt46 == 1:
                        # JavaTreeParser.g:0:0: qualifiedIdentifier
                        pass 
                        self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_throwsClause1991)
                        self.qualifiedIdentifier()

                        self._state.following.pop()


                    else:
                        if cnt46 >= 1:
                            break #loop46

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(46, self.input)
                        raise eee

                    cnt46 += 1



                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 23, throwsClause_StartIndex, success)

            pass

        return 

    # $ANTLR end "throwsClause"


    # $ANTLR start "modifierList"
    # JavaTreeParser.g:280:1: modifierList returns [values] : ^( MODIFIER_LIST (md0= modifier )* ) ;
    def modifierList(self, ):

        values = None
        modifierList_StartIndex = self.input.index()
        md0 = None


        values = [] 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 24):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return values

                # JavaTreeParser.g:282:5: ( ^( MODIFIER_LIST (md0= modifier )* ) )
                # JavaTreeParser.g:282:9: ^( MODIFIER_LIST (md0= modifier )* )
                pass 
                self.match(self.input, MODIFIER_LIST, self.FOLLOW_MODIFIER_LIST_in_modifierList2026)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:282:25: (md0= modifier )*
                    while True: #loop47
                        alt47 = 2
                        LA47_0 = self.input.LA(1)

                        if (LA47_0 == AT or LA47_0 == ABSTRACT or LA47_0 == FINAL or LA47_0 == NATIVE or (PRIVATE <= LA47_0 <= PUBLIC) or (STATIC <= LA47_0 <= STRICTFP) or LA47_0 == SYNCHRONIZED or LA47_0 == TRANSIENT or LA47_0 == VOLATILE) :
                            alt47 = 1


                        if alt47 == 1:
                            # JavaTreeParser.g:282:26: md0= modifier
                            pass 
                            self._state.following.append(self.FOLLOW_modifier_in_modifierList2031)
                            md0 = self.modifier()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                values.append(((md0 is not None) and [self.input.getTokenStream().toString(
                                    self.input.getTreeAdaptor().getTokenStartIndex(md0.start),
                                    self.input.getTreeAdaptor().getTokenStopIndex(md0.start)
                                    )] or [None])[0]) 



                        else:
                            break #loop47



                    self.match(self.input, UP, None)





                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 24, modifierList_StartIndex, success)

            pass

        return values

    # $ANTLR end "modifierList"

    class modifier_return(TreeRuleReturnScope):
        def __init__(self):
            TreeRuleReturnScope.__init__(self)





    # $ANTLR start "modifier"
    # JavaTreeParser.g:285:1: modifier : ( PUBLIC | PROTECTED | PRIVATE | STATIC | ABSTRACT | NATIVE | SYNCHRONIZED | TRANSIENT | VOLATILE | STRICTFP | localModifier );
    def modifier(self, ):

        retval = self.modifier_return()
        retval.start = self.input.LT(1)
        modifier_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 25):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # JavaTreeParser.g:286:5: ( PUBLIC | PROTECTED | PRIVATE | STATIC | ABSTRACT | NATIVE | SYNCHRONIZED | TRANSIENT | VOLATILE | STRICTFP | localModifier )
                alt48 = 11
                LA48 = self.input.LA(1)
                if LA48 == PUBLIC:
                    alt48 = 1
                elif LA48 == PROTECTED:
                    alt48 = 2
                elif LA48 == PRIVATE:
                    alt48 = 3
                elif LA48 == STATIC:
                    alt48 = 4
                elif LA48 == ABSTRACT:
                    alt48 = 5
                elif LA48 == NATIVE:
                    alt48 = 6
                elif LA48 == SYNCHRONIZED:
                    alt48 = 7
                elif LA48 == TRANSIENT:
                    alt48 = 8
                elif LA48 == VOLATILE:
                    alt48 = 9
                elif LA48 == STRICTFP:
                    alt48 = 10
                elif LA48 == AT or LA48 == FINAL:
                    alt48 = 11
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 48, 0, self.input)

                    raise nvae

                if alt48 == 1:
                    # JavaTreeParser.g:286:9: PUBLIC
                    pass 
                    self.match(self.input, PUBLIC, self.FOLLOW_PUBLIC_in_modifier2055)


                elif alt48 == 2:
                    # JavaTreeParser.g:287:9: PROTECTED
                    pass 
                    self.match(self.input, PROTECTED, self.FOLLOW_PROTECTED_in_modifier2065)


                elif alt48 == 3:
                    # JavaTreeParser.g:288:9: PRIVATE
                    pass 
                    self.match(self.input, PRIVATE, self.FOLLOW_PRIVATE_in_modifier2075)


                elif alt48 == 4:
                    # JavaTreeParser.g:289:9: STATIC
                    pass 
                    self.match(self.input, STATIC, self.FOLLOW_STATIC_in_modifier2085)


                elif alt48 == 5:
                    # JavaTreeParser.g:290:9: ABSTRACT
                    pass 
                    self.match(self.input, ABSTRACT, self.FOLLOW_ABSTRACT_in_modifier2095)


                elif alt48 == 6:
                    # JavaTreeParser.g:291:9: NATIVE
                    pass 
                    self.match(self.input, NATIVE, self.FOLLOW_NATIVE_in_modifier2105)


                elif alt48 == 7:
                    # JavaTreeParser.g:292:9: SYNCHRONIZED
                    pass 
                    self.match(self.input, SYNCHRONIZED, self.FOLLOW_SYNCHRONIZED_in_modifier2115)


                elif alt48 == 8:
                    # JavaTreeParser.g:293:9: TRANSIENT
                    pass 
                    self.match(self.input, TRANSIENT, self.FOLLOW_TRANSIENT_in_modifier2125)


                elif alt48 == 9:
                    # JavaTreeParser.g:294:9: VOLATILE
                    pass 
                    self.match(self.input, VOLATILE, self.FOLLOW_VOLATILE_in_modifier2135)


                elif alt48 == 10:
                    # JavaTreeParser.g:295:9: STRICTFP
                    pass 
                    self.match(self.input, STRICTFP, self.FOLLOW_STRICTFP_in_modifier2145)


                elif alt48 == 11:
                    # JavaTreeParser.g:296:9: localModifier
                    pass 
                    self._state.following.append(self.FOLLOW_localModifier_in_modifier2155)
                    self.localModifier()

                    self._state.following.pop()



                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 25, modifier_StartIndex, success)

            pass

        return retval

    # $ANTLR end "modifier"


    # $ANTLR start "localModifierList"
    # JavaTreeParser.g:299:1: localModifierList returns [values] : ^( LOCAL_MODIFIER_LIST (md0= localModifier )* ) ;
    def localModifierList(self, ):

        values = None
        localModifierList_StartIndex = self.input.index()
        md0 = None


        values = [] 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 26):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return values

                # JavaTreeParser.g:301:5: ( ^( LOCAL_MODIFIER_LIST (md0= localModifier )* ) )
                # JavaTreeParser.g:301:9: ^( LOCAL_MODIFIER_LIST (md0= localModifier )* )
                pass 
                self.match(self.input, LOCAL_MODIFIER_LIST, self.FOLLOW_LOCAL_MODIFIER_LIST_in_localModifierList2188)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:301:31: (md0= localModifier )*
                    while True: #loop49
                        alt49 = 2
                        LA49_0 = self.input.LA(1)

                        if (LA49_0 == AT or LA49_0 == FINAL) :
                            alt49 = 1


                        if alt49 == 1:
                            # JavaTreeParser.g:301:32: md0= localModifier
                            pass 
                            self._state.following.append(self.FOLLOW_localModifier_in_localModifierList2193)
                            md0 = self.localModifier()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                values.append(md0) 



                        else:
                            break #loop49



                    self.match(self.input, UP, None)





                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 26, localModifierList_StartIndex, success)

            pass

        return values

    # $ANTLR end "localModifierList"


    # $ANTLR start "localModifier"
    # JavaTreeParser.g:304:1: localModifier returns [value] : ( FINAL | an0= annotation );
    def localModifier(self, ):

        value = None
        localModifier_StartIndex = self.input.index()
        an0 = None


        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 27):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:305:5: ( FINAL | an0= annotation )
                alt50 = 2
                LA50_0 = self.input.LA(1)

                if (LA50_0 == FINAL) :
                    alt50 = 1
                elif (LA50_0 == AT) :
                    alt50 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 50, 0, self.input)

                    raise nvae

                if alt50 == 1:
                    # JavaTreeParser.g:305:9: FINAL
                    pass 
                    self.match(self.input, FINAL, self.FOLLOW_FINAL_in_localModifier2221)
                    if self._state.backtracking == 0:
                        value = 'final' 



                elif alt50 == 2:
                    # JavaTreeParser.g:306:9: an0= annotation
                    pass 
                    self._state.following.append(self.FOLLOW_annotation_in_localModifier2235)
                    an0 = self.annotation()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = an0 




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 27, localModifier_StartIndex, success)

            pass

        return value

    # $ANTLR end "localModifier"

    class type_return(TreeRuleReturnScope):
        def __init__(self):
            TreeRuleReturnScope.__init__(self)

            self.value = None




    # $ANTLR start "type"
    # JavaTreeParser.g:309:1: type returns [value] : ^( TYPE (pt0= primitiveType | qt0= qualifiedTypeIdent ) ( arrayDeclaratorList )? ) ;
    def type(self, ):

        retval = self.type_return()
        retval.start = self.input.LT(1)
        type_StartIndex = self.input.index()
        pt0 = None

        qt0 = None


        retval.value = ex(format="${left}") 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 28):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # JavaTreeParser.g:311:5: ( ^( TYPE (pt0= primitiveType | qt0= qualifiedTypeIdent ) ( arrayDeclaratorList )? ) )
                # JavaTreeParser.g:311:9: ^( TYPE (pt0= primitiveType | qt0= qualifiedTypeIdent ) ( arrayDeclaratorList )? )
                pass 
                self.match(self.input, TYPE, self.FOLLOW_TYPE_in_type2270)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:312:11: (pt0= primitiveType | qt0= qualifiedTypeIdent )
                alt51 = 2
                LA51_0 = self.input.LA(1)

                if (LA51_0 == BOOLEAN or LA51_0 == BYTE or LA51_0 == CHAR or LA51_0 == DOUBLE or LA51_0 == FLOAT or (INT <= LA51_0 <= LONG) or LA51_0 == SHORT) :
                    alt51 = 1
                elif (LA51_0 == QUALIFIED_TYPE_IDENT) :
                    alt51 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 51, 0, self.input)

                    raise nvae

                if alt51 == 1:
                    # JavaTreeParser.g:312:12: pt0= primitiveType
                    pass 
                    self._state.following.append(self.FOLLOW_primitiveType_in_type2285)
                    pt0 = self.primitiveType()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        retval.value.update(left=self.altType(((pt0 is not None) and [self.input.getTokenStream().toString(
                            self.input.getTreeAdaptor().getTokenStartIndex(pt0.start),
                            self.input.getTreeAdaptor().getTokenStopIndex(pt0.start)
                            )] or [None])[0])) 



                elif alt51 == 2:
                    # JavaTreeParser.g:313:12: qt0= qualifiedTypeIdent
                    pass 
                    self._state.following.append(self.FOLLOW_qualifiedTypeIdent_in_type2304)
                    qt0 = self.qualifiedTypeIdent()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        retval.value.update(left=self.altType(qt0)) 




                # JavaTreeParser.g:314:11: ( arrayDeclaratorList )?
                alt52 = 2
                LA52_0 = self.input.LA(1)

                if (LA52_0 == ARRAY_DECLARATOR_LIST) :
                    alt52 = 1
                if alt52 == 1:
                    # JavaTreeParser.g:314:12: arrayDeclaratorList
                    pass 
                    self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_type2320)
                    self.arrayDeclaratorList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        retval.value["format"] += "list" ##"array of %s" % retval.value["left"]
                        retval.value.update(array=True, left="")
                                   





                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 28, type_StartIndex, success)

            pass

        return retval

    # $ANTLR end "type"


    # $ANTLR start "qualifiedTypeIdent"
    # JavaTreeParser.g:323:1: qualifiedTypeIdent returns [value] : ^( QUALIFIED_TYPE_IDENT (ti0= typeIdent )+ ) ;
    def qualifiedTypeIdent(self, ):

        value = None
        qualifiedTypeIdent_StartIndex = self.input.index()
        ti0 = None


        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 29):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:324:5: ( ^( QUALIFIED_TYPE_IDENT (ti0= typeIdent )+ ) )
                # JavaTreeParser.g:324:9: ^( QUALIFIED_TYPE_IDENT (ti0= typeIdent )+ )
                pass 
                self.match(self.input, QUALIFIED_TYPE_IDENT, self.FOLLOW_QUALIFIED_TYPE_IDENT_in_qualifiedTypeIdent2381)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:324:32: (ti0= typeIdent )+
                cnt53 = 0
                while True: #loop53
                    alt53 = 2
                    LA53_0 = self.input.LA(1)

                    if (LA53_0 == IDENT) :
                        alt53 = 1


                    if alt53 == 1:
                        # JavaTreeParser.g:324:33: ti0= typeIdent
                        pass 
                        self._state.following.append(self.FOLLOW_typeIdent_in_qualifiedTypeIdent2386)
                        ti0 = self.typeIdent()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            value = ti0 



                    else:
                        if cnt53 >= 1:
                            break #loop53

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(53, self.input)
                        raise eee

                    cnt53 += 1



                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 29, qualifiedTypeIdent_StartIndex, success)

            pass

        return value

    # $ANTLR end "qualifiedTypeIdent"


    # $ANTLR start "typeIdent"
    # JavaTreeParser.g:327:1: typeIdent returns [value] : ^(id0= IDENT ( genericTypeArgumentList )? ) ;
    def typeIdent(self, ):

        value = None
        typeIdent_StartIndex = self.input.index()
        id0 = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 30):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:328:5: ( ^(id0= IDENT ( genericTypeArgumentList )? ) )
                # JavaTreeParser.g:328:9: ^(id0= IDENT ( genericTypeArgumentList )? )
                pass 
                id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_typeIdent2417)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:328:21: ( genericTypeArgumentList )?
                    alt54 = 2
                    LA54_0 = self.input.LA(1)

                    if (LA54_0 == GENERIC_TYPE_ARG_LIST) :
                        alt54 = 1
                    if alt54 == 1:
                        # JavaTreeParser.g:0:0: genericTypeArgumentList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeArgumentList_in_typeIdent2419)
                        self.genericTypeArgumentList()

                        self._state.following.pop()




                    self.match(self.input, UP, None)

                if self._state.backtracking == 0:
                    value = id0.text 





                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 30, typeIdent_StartIndex, success)

            pass

        return value

    # $ANTLR end "typeIdent"

    class primitiveType_return(TreeRuleReturnScope):
        def __init__(self):
            TreeRuleReturnScope.__init__(self)





    # $ANTLR start "primitiveType"
    # JavaTreeParser.g:332:1: primitiveType : ( BOOLEAN | CHAR | BYTE | SHORT | INT | LONG | FLOAT | DOUBLE );
    def primitiveType(self, ):

        retval = self.primitiveType_return()
        retval.start = self.input.LT(1)
        primitiveType_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 31):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # JavaTreeParser.g:333:5: ( BOOLEAN | CHAR | BYTE | SHORT | INT | LONG | FLOAT | DOUBLE )
                # JavaTreeParser.g:
                pass 
                if self.input.LA(1) == BOOLEAN or self.input.LA(1) == BYTE or self.input.LA(1) == CHAR or self.input.LA(1) == DOUBLE or self.input.LA(1) == FLOAT or (INT <= self.input.LA(1) <= LONG) or self.input.LA(1) == SHORT:
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse






                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 31, primitiveType_StartIndex, success)

            pass

        return retval

    # $ANTLR end "primitiveType"


    # $ANTLR start "genericTypeArgumentList"
    # JavaTreeParser.g:343:1: genericTypeArgumentList returns [values] : ^( GENERIC_TYPE_ARG_LIST ( genericTypeArgument )+ ) ;
    def genericTypeArgumentList(self, ):

        values = None
        genericTypeArgumentList_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 32):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return values

                # JavaTreeParser.g:344:5: ( ^( GENERIC_TYPE_ARG_LIST ( genericTypeArgument )+ ) )
                # JavaTreeParser.g:344:9: ^( GENERIC_TYPE_ARG_LIST ( genericTypeArgument )+ )
                pass 
                self.match(self.input, GENERIC_TYPE_ARG_LIST, self.FOLLOW_GENERIC_TYPE_ARG_LIST_in_genericTypeArgumentList2546)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:344:33: ( genericTypeArgument )+
                cnt55 = 0
                while True: #loop55
                    alt55 = 2
                    LA55_0 = self.input.LA(1)

                    if (LA55_0 == QUESTION or LA55_0 == TYPE) :
                        alt55 = 1


                    if alt55 == 1:
                        # JavaTreeParser.g:0:0: genericTypeArgument
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeArgument_in_genericTypeArgumentList2548)
                        self.genericTypeArgument()

                        self._state.following.pop()


                    else:
                        if cnt55 >= 1:
                            break #loop55

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(55, self.input)
                        raise eee

                    cnt55 += 1



                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 32, genericTypeArgumentList_StartIndex, success)

            pass

        return values

    # $ANTLR end "genericTypeArgumentList"


    # $ANTLR start "genericTypeArgument"
    # JavaTreeParser.g:347:1: genericTypeArgument : ( type | ^( QUESTION ( genericWildcardBoundType )? ) );
    def genericTypeArgument(self, ):

        genericTypeArgument_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 33):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:348:5: ( type | ^( QUESTION ( genericWildcardBoundType )? ) )
                alt57 = 2
                LA57_0 = self.input.LA(1)

                if (LA57_0 == TYPE) :
                    alt57 = 1
                elif (LA57_0 == QUESTION) :
                    alt57 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 57, 0, self.input)

                    raise nvae

                if alt57 == 1:
                    # JavaTreeParser.g:348:9: type
                    pass 
                    self._state.following.append(self.FOLLOW_type_in_genericTypeArgument2569)
                    self.type()

                    self._state.following.pop()


                elif alt57 == 2:
                    # JavaTreeParser.g:349:9: ^( QUESTION ( genericWildcardBoundType )? )
                    pass 
                    self.match(self.input, QUESTION, self.FOLLOW_QUESTION_in_genericTypeArgument2580)

                    if self.input.LA(1) == DOWN:
                        self.match(self.input, DOWN, None)
                        # JavaTreeParser.g:349:20: ( genericWildcardBoundType )?
                        alt56 = 2
                        LA56_0 = self.input.LA(1)

                        if (LA56_0 == EXTENDS or LA56_0 == SUPER) :
                            alt56 = 1
                        if alt56 == 1:
                            # JavaTreeParser.g:0:0: genericWildcardBoundType
                            pass 
                            self._state.following.append(self.FOLLOW_genericWildcardBoundType_in_genericTypeArgument2582)
                            self.genericWildcardBoundType()

                            self._state.following.pop()




                        self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 33, genericTypeArgument_StartIndex, success)

            pass

        return 

    # $ANTLR end "genericTypeArgument"


    # $ANTLR start "genericWildcardBoundType"
    # JavaTreeParser.g:352:1: genericWildcardBoundType : ( ^( EXTENDS type ) | ^( SUPER type ) );
    def genericWildcardBoundType(self, ):

        genericWildcardBoundType_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 34):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:353:5: ( ^( EXTENDS type ) | ^( SUPER type ) )
                alt58 = 2
                LA58_0 = self.input.LA(1)

                if (LA58_0 == EXTENDS) :
                    alt58 = 1
                elif (LA58_0 == SUPER) :
                    alt58 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 58, 0, self.input)

                    raise nvae

                if alt58 == 1:
                    # JavaTreeParser.g:353:9: ^( EXTENDS type )
                    pass 
                    self.match(self.input, EXTENDS, self.FOLLOW_EXTENDS_in_genericWildcardBoundType2604)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_type_in_genericWildcardBoundType2606)
                    self.type()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt58 == 2:
                    # JavaTreeParser.g:354:9: ^( SUPER type )
                    pass 
                    self.match(self.input, SUPER, self.FOLLOW_SUPER_in_genericWildcardBoundType2618)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_type_in_genericWildcardBoundType2620)
                    self.type()

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 34, genericWildcardBoundType_StartIndex, success)

            pass

        return 

    # $ANTLR end "genericWildcardBoundType"


    # $ANTLR start "formalParameterList"
    # JavaTreeParser.g:357:1: formalParameterList returns [values] : ^( FORMAL_PARAM_LIST (fp0= formalParameterStandardDecl )* (vd0= formalParameterVarargDecl )? ) ;
    def formalParameterList(self, ):

        values = None
        formalParameterList_StartIndex = self.input.index()
        fp0 = None

        vd0 = None


        values = [] 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 35):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return values

                # JavaTreeParser.g:359:5: ( ^( FORMAL_PARAM_LIST (fp0= formalParameterStandardDecl )* (vd0= formalParameterVarargDecl )? ) )
                # JavaTreeParser.g:359:9: ^( FORMAL_PARAM_LIST (fp0= formalParameterStandardDecl )* (vd0= formalParameterVarargDecl )? )
                pass 
                self.match(self.input, FORMAL_PARAM_LIST, self.FOLLOW_FORMAL_PARAM_LIST_in_formalParameterList2654)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:360:11: (fp0= formalParameterStandardDecl )*
                    while True: #loop59
                        alt59 = 2
                        LA59_0 = self.input.LA(1)

                        if (LA59_0 == FORMAL_PARAM_STD_DECL) :
                            alt59 = 1


                        if alt59 == 1:
                            # JavaTreeParser.g:360:12: fp0= formalParameterStandardDecl
                            pass 
                            self._state.following.append(self.FOLLOW_formalParameterStandardDecl_in_formalParameterList2669)
                            fp0 = self.formalParameterStandardDecl()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                values.append(fp0) 



                        else:
                            break #loop59


                    # JavaTreeParser.g:361:11: (vd0= formalParameterVarargDecl )?
                    alt60 = 2
                    LA60_0 = self.input.LA(1)

                    if (LA60_0 == FORMAL_PARAM_VARARG_DECL) :
                        alt60 = 1
                    if alt60 == 1:
                        # JavaTreeParser.g:361:12: vd0= formalParameterVarargDecl
                        pass 
                        self._state.following.append(self.FOLLOW_formalParameterVarargDecl_in_formalParameterList2688)
                        vd0 = self.formalParameterVarargDecl()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            values.append(vd0) 





                    self.match(self.input, UP, None)





                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 35, formalParameterList_StartIndex, success)

            pass

        return values

    # $ANTLR end "formalParameterList"


    # $ANTLR start "formalParameterStandardDecl"
    # JavaTreeParser.g:365:1: formalParameterStandardDecl returns [value] : ^( FORMAL_PARAM_STD_DECL lm0= localModifierList tp0= type vd0= variableDeclaratorId ) ;
    def formalParameterStandardDecl(self, ):

        value = None
        formalParameterStandardDecl_StartIndex = self.input.index()
        lm0 = None

        tp0 = None

        vd0 = None


        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 36):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:366:5: ( ^( FORMAL_PARAM_STD_DECL lm0= localModifierList tp0= type vd0= variableDeclaratorId ) )
                # JavaTreeParser.g:366:9: ^( FORMAL_PARAM_STD_DECL lm0= localModifierList tp0= type vd0= variableDeclaratorId )
                pass 
                self.match(self.input, FORMAL_PARAM_STD_DECL, self.FOLLOW_FORMAL_PARAM_STD_DECL_in_formalParameterStandardDecl2728)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_localModifierList_in_formalParameterStandardDecl2742)
                lm0 = self.localModifierList()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_type_in_formalParameterStandardDecl2756)
                tp0 = self.type()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_variableDeclaratorId_in_formalParameterStandardDecl2770)
                vd0 = self.variableDeclaratorId()

                self._state.following.pop()

                self.match(self.input, UP, None)
                if self._state.backtracking == 0:
                    value = px(vd0, ((tp0 is not None) and [self.input.getTokenStream().toString(
                        self.input.getTreeAdaptor().getTokenStartIndex(tp0.start),
                        self.input.getTreeAdaptor().getTokenStopIndex(tp0.start)
                        )] or [None])[0], lm0, variadic=False) 





                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 36, formalParameterStandardDecl_StartIndex, success)

            pass

        return value

    # $ANTLR end "formalParameterStandardDecl"


    # $ANTLR start "formalParameterVarargDecl"
    # JavaTreeParser.g:374:1: formalParameterVarargDecl returns [value] : ^( FORMAL_PARAM_VARARG_DECL lm0= localModifierList tp0= type vd0= variableDeclaratorId ) ;
    def formalParameterVarargDecl(self, ):

        value = None
        formalParameterVarargDecl_StartIndex = self.input.index()
        lm0 = None

        tp0 = None

        vd0 = None


        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 37):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:375:5: ( ^( FORMAL_PARAM_VARARG_DECL lm0= localModifierList tp0= type vd0= variableDeclaratorId ) )
                # JavaTreeParser.g:375:9: ^( FORMAL_PARAM_VARARG_DECL lm0= localModifierList tp0= type vd0= variableDeclaratorId )
                pass 
                self.match(self.input, FORMAL_PARAM_VARARG_DECL, self.FOLLOW_FORMAL_PARAM_VARARG_DECL_in_formalParameterVarargDecl2807)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_localModifierList_in_formalParameterVarargDecl2821)
                lm0 = self.localModifierList()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_type_in_formalParameterVarargDecl2835)
                tp0 = self.type()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_variableDeclaratorId_in_formalParameterVarargDecl2849)
                vd0 = self.variableDeclaratorId()

                self._state.following.pop()

                self.match(self.input, UP, None)
                if self._state.backtracking == 0:
                    value = px(vd0, ((tp0 is not None) and [self.input.getTokenStream().toString(
                        self.input.getTreeAdaptor().getTokenStartIndex(tp0.start),
                        self.input.getTreeAdaptor().getTokenStopIndex(tp0.start)
                        )] or [None])[0], lm0, variadic=True) 





                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 37, formalParameterVarargDecl_StartIndex, success)

            pass

        return value

    # $ANTLR end "formalParameterVarargDecl"


    # $ANTLR start "qualifiedIdentifier"
    # JavaTreeParser.g:383:1: qualifiedIdentifier returns [value] : ( IDENT | ^( DOT qi0= qualifiedIdentifier IDENT ) );
    def qualifiedIdentifier(self, ):

        value = None
        qualifiedIdentifier_StartIndex = self.input.index()
        IDENT2 = None
        IDENT3 = None
        qi0 = None


        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 38):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:384:5: ( IDENT | ^( DOT qi0= qualifiedIdentifier IDENT ) )
                alt61 = 2
                LA61_0 = self.input.LA(1)

                if (LA61_0 == IDENT) :
                    alt61 = 1
                elif (LA61_0 == DOT) :
                    alt61 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 61, 0, self.input)

                    raise nvae

                if alt61 == 1:
                    # JavaTreeParser.g:384:9: IDENT
                    pass 
                    IDENT2=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_qualifiedIdentifier2885)
                    if self._state.backtracking == 0:
                        value = ex(IDENT2.text, format="${left}") 



                elif alt61 == 2:
                    # JavaTreeParser.g:385:9: ^( DOT qi0= qualifiedIdentifier IDENT )
                    pass 
                    self.match(self.input, DOT, self.FOLLOW_DOT_in_qualifiedIdentifier2898)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_qualifiedIdentifier2912)
                    qi0 = self.qualifiedIdentifier()

                    self._state.following.pop()
                    IDENT3=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_qualifiedIdentifier2924)
                    if self._state.backtracking == 0:
                        value = ex(qi0, IDENT3.text, "${left}.${right}") 


                    self.match(self.input, UP, None)



                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 38, qualifiedIdentifier_StartIndex, success)

            pass

        return value

    # $ANTLR end "qualifiedIdentifier"


    # $ANTLR start "annotationList"
    # JavaTreeParser.g:395:1: annotationList : ^( ANNOTATION_LIST ( annotation )* ) ;
    def annotationList(self, ):

        annotationList_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 39):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:396:5: ( ^( ANNOTATION_LIST ( annotation )* ) )
                # JavaTreeParser.g:396:9: ^( ANNOTATION_LIST ( annotation )* )
                pass 
                self.match(self.input, ANNOTATION_LIST, self.FOLLOW_ANNOTATION_LIST_in_annotationList2969)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:396:27: ( annotation )*
                    while True: #loop62
                        alt62 = 2
                        LA62_0 = self.input.LA(1)

                        if (LA62_0 == AT) :
                            alt62 = 1


                        if alt62 == 1:
                            # JavaTreeParser.g:0:0: annotation
                            pass 
                            self._state.following.append(self.FOLLOW_annotation_in_annotationList2971)
                            self.annotation()

                            self._state.following.pop()


                        else:
                            break #loop62



                    self.match(self.input, UP, None)





                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 39, annotationList_StartIndex, success)

            pass

        return 

    # $ANTLR end "annotationList"


    # $ANTLR start "annotation"
    # JavaTreeParser.g:399:1: annotation returns [value] : ^( AT qi0= qualifiedIdentifier ( annotationInit )? ) ;
    def annotation(self, ):

        value = None
        annotation_StartIndex = self.input.index()
        qi0 = None


        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 40):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:400:5: ( ^( AT qi0= qualifiedIdentifier ( annotationInit )? ) )
                # JavaTreeParser.g:400:9: ^( AT qi0= qualifiedIdentifier ( annotationInit )? )
                pass 
                self.match(self.input, AT, self.FOLLOW_AT_in_annotation2997)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_annotation3011)
                qi0 = self.qualifiedIdentifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    value = qi0.value 

                # JavaTreeParser.g:402:11: ( annotationInit )?
                alt63 = 2
                LA63_0 = self.input.LA(1)

                if (LA63_0 == ANNOTATION_INIT_BLOCK) :
                    alt63 = 1
                if alt63 == 1:
                    # JavaTreeParser.g:0:0: annotationInit
                    pass 
                    self._state.following.append(self.FOLLOW_annotationInit_in_annotation3025)
                    self.annotationInit()

                    self._state.following.pop()




                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 40, annotation_StartIndex, success)

            pass

        return value

    # $ANTLR end "annotation"


    # $ANTLR start "annotationInit"
    # JavaTreeParser.g:406:1: annotationInit : ^( ANNOTATION_INIT_BLOCK annotationInitializers ) ;
    def annotationInit(self, ):

        annotationInit_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 41):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:407:5: ( ^( ANNOTATION_INIT_BLOCK annotationInitializers ) )
                # JavaTreeParser.g:407:9: ^( ANNOTATION_INIT_BLOCK annotationInitializers )
                pass 
                self.match(self.input, ANNOTATION_INIT_BLOCK, self.FOLLOW_ANNOTATION_INIT_BLOCK_in_annotationInit3056)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_annotationInitializers_in_annotationInit3058)
                self.annotationInitializers()

                self._state.following.pop()

                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 41, annotationInit_StartIndex, success)

            pass

        return 

    # $ANTLR end "annotationInit"


    # $ANTLR start "annotationInitializers"
    # JavaTreeParser.g:410:1: annotationInitializers : ( ^( ANNOTATION_INIT_KEY_LIST ( annotationInitializer )+ ) | ^( ANNOTATION_INIT_DEFAULT_KEY annotationElementValue ) );
    def annotationInitializers(self, ):

        annotationInitializers_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 42):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:411:5: ( ^( ANNOTATION_INIT_KEY_LIST ( annotationInitializer )+ ) | ^( ANNOTATION_INIT_DEFAULT_KEY annotationElementValue ) )
                alt65 = 2
                LA65_0 = self.input.LA(1)

                if (LA65_0 == ANNOTATION_INIT_KEY_LIST) :
                    alt65 = 1
                elif (LA65_0 == ANNOTATION_INIT_DEFAULT_KEY) :
                    alt65 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 65, 0, self.input)

                    raise nvae

                if alt65 == 1:
                    # JavaTreeParser.g:411:9: ^( ANNOTATION_INIT_KEY_LIST ( annotationInitializer )+ )
                    pass 
                    self.match(self.input, ANNOTATION_INIT_KEY_LIST, self.FOLLOW_ANNOTATION_INIT_KEY_LIST_in_annotationInitializers3079)

                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:411:36: ( annotationInitializer )+
                    cnt64 = 0
                    while True: #loop64
                        alt64 = 2
                        LA64_0 = self.input.LA(1)

                        if (LA64_0 == IDENT) :
                            alt64 = 1


                        if alt64 == 1:
                            # JavaTreeParser.g:0:0: annotationInitializer
                            pass 
                            self._state.following.append(self.FOLLOW_annotationInitializer_in_annotationInitializers3081)
                            self.annotationInitializer()

                            self._state.following.pop()


                        else:
                            if cnt64 >= 1:
                                break #loop64

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(64, self.input)
                            raise eee

                        cnt64 += 1



                    self.match(self.input, UP, None)


                elif alt65 == 2:
                    # JavaTreeParser.g:412:9: ^( ANNOTATION_INIT_DEFAULT_KEY annotationElementValue )
                    pass 
                    self.match(self.input, ANNOTATION_INIT_DEFAULT_KEY, self.FOLLOW_ANNOTATION_INIT_DEFAULT_KEY_in_annotationInitializers3094)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_annotationElementValue_in_annotationInitializers3096)
                    self.annotationElementValue()

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 42, annotationInitializers_StartIndex, success)

            pass

        return 

    # $ANTLR end "annotationInitializers"


    # $ANTLR start "annotationInitializer"
    # JavaTreeParser.g:415:1: annotationInitializer : ^( IDENT annotationElementValue ) ;
    def annotationInitializer(self, ):

        annotationInitializer_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 43):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:416:5: ( ^( IDENT annotationElementValue ) )
                # JavaTreeParser.g:416:9: ^( IDENT annotationElementValue )
                pass 
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_annotationInitializer3117)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_annotationElementValue_in_annotationInitializer3119)
                self.annotationElementValue()

                self._state.following.pop()

                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 43, annotationInitializer_StartIndex, success)

            pass

        return 

    # $ANTLR end "annotationInitializer"


    # $ANTLR start "annotationElementValue"
    # JavaTreeParser.g:419:1: annotationElementValue : ( ^( ANNOTATION_INIT_ARRAY_ELEMENT ( annotationElementValue )* ) | annotation | expression );
    def annotationElementValue(self, ):

        annotationElementValue_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 44):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:420:5: ( ^( ANNOTATION_INIT_ARRAY_ELEMENT ( annotationElementValue )* ) | annotation | expression )
                alt67 = 3
                LA67 = self.input.LA(1)
                if LA67 == ANNOTATION_INIT_ARRAY_ELEMENT:
                    alt67 = 1
                elif LA67 == AT:
                    alt67 = 2
                elif LA67 == EXPR:
                    alt67 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 67, 0, self.input)

                    raise nvae

                if alt67 == 1:
                    # JavaTreeParser.g:420:9: ^( ANNOTATION_INIT_ARRAY_ELEMENT ( annotationElementValue )* )
                    pass 
                    self.match(self.input, ANNOTATION_INIT_ARRAY_ELEMENT, self.FOLLOW_ANNOTATION_INIT_ARRAY_ELEMENT_in_annotationElementValue3140)

                    if self.input.LA(1) == DOWN:
                        self.match(self.input, DOWN, None)
                        # JavaTreeParser.g:420:41: ( annotationElementValue )*
                        while True: #loop66
                            alt66 = 2
                            LA66_0 = self.input.LA(1)

                            if (LA66_0 == AT or LA66_0 == ANNOTATION_INIT_ARRAY_ELEMENT or LA66_0 == EXPR) :
                                alt66 = 1


                            if alt66 == 1:
                                # JavaTreeParser.g:0:0: annotationElementValue
                                pass 
                                self._state.following.append(self.FOLLOW_annotationElementValue_in_annotationElementValue3142)
                                self.annotationElementValue()

                                self._state.following.pop()


                            else:
                                break #loop66



                        self.match(self.input, UP, None)



                elif alt67 == 2:
                    # JavaTreeParser.g:421:9: annotation
                    pass 
                    self._state.following.append(self.FOLLOW_annotation_in_annotationElementValue3154)
                    self.annotation()

                    self._state.following.pop()


                elif alt67 == 3:
                    # JavaTreeParser.g:422:9: expression
                    pass 
                    self._state.following.append(self.FOLLOW_expression_in_annotationElementValue3164)
                    self.expression()

                    self._state.following.pop()



                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 44, annotationElementValue_StartIndex, success)

            pass

        return 

    # $ANTLR end "annotationElementValue"


    # $ANTLR start "annotationTopLevelScope"
    # JavaTreeParser.g:425:1: annotationTopLevelScope : ^( ANNOTATION_TOP_LEVEL_SCOPE ( annotationScopeDeclarations )* ) ;
    def annotationTopLevelScope(self, ):

        annotationTopLevelScope_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 45):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:426:5: ( ^( ANNOTATION_TOP_LEVEL_SCOPE ( annotationScopeDeclarations )* ) )
                # JavaTreeParser.g:426:9: ^( ANNOTATION_TOP_LEVEL_SCOPE ( annotationScopeDeclarations )* )
                pass 
                self.match(self.input, ANNOTATION_TOP_LEVEL_SCOPE, self.FOLLOW_ANNOTATION_TOP_LEVEL_SCOPE_in_annotationTopLevelScope3184)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:426:38: ( annotationScopeDeclarations )*
                    while True: #loop68
                        alt68 = 2
                        LA68_0 = self.input.LA(1)

                        if (LA68_0 == AT or LA68_0 == CLASS or LA68_0 == ENUM or LA68_0 == INTERFACE or LA68_0 == ANNOTATION_METHOD_DECL or LA68_0 == VAR_DECLARATION) :
                            alt68 = 1


                        if alt68 == 1:
                            # JavaTreeParser.g:0:0: annotationScopeDeclarations
                            pass 
                            self._state.following.append(self.FOLLOW_annotationScopeDeclarations_in_annotationTopLevelScope3186)
                            self.annotationScopeDeclarations()

                            self._state.following.pop()


                        else:
                            break #loop68



                    self.match(self.input, UP, None)





                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 45, annotationTopLevelScope_StartIndex, success)

            pass

        return 

    # $ANTLR end "annotationTopLevelScope"


    # $ANTLR start "annotationScopeDeclarations"
    # JavaTreeParser.g:429:1: annotationScopeDeclarations : ( ^( ANNOTATION_METHOD_DECL modifierList type IDENT ( annotationDefaultValue )? ) | ^( VAR_DECLARATION modifierList type variableDeclaratorList ) | typeDeclaration );
    def annotationScopeDeclarations(self, ):

        annotationScopeDeclarations_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 46):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:430:5: ( ^( ANNOTATION_METHOD_DECL modifierList type IDENT ( annotationDefaultValue )? ) | ^( VAR_DECLARATION modifierList type variableDeclaratorList ) | typeDeclaration )
                alt70 = 3
                LA70 = self.input.LA(1)
                if LA70 == ANNOTATION_METHOD_DECL:
                    alt70 = 1
                elif LA70 == VAR_DECLARATION:
                    alt70 = 2
                elif LA70 == AT or LA70 == CLASS or LA70 == ENUM or LA70 == INTERFACE:
                    alt70 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 70, 0, self.input)

                    raise nvae

                if alt70 == 1:
                    # JavaTreeParser.g:430:9: ^( ANNOTATION_METHOD_DECL modifierList type IDENT ( annotationDefaultValue )? )
                    pass 
                    self.match(self.input, ANNOTATION_METHOD_DECL, self.FOLLOW_ANNOTATION_METHOD_DECL_in_annotationScopeDeclarations3208)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_annotationScopeDeclarations3210)
                    self.modifierList()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_type_in_annotationScopeDeclarations3212)
                    self.type()

                    self._state.following.pop()
                    self.match(self.input, IDENT, self.FOLLOW_IDENT_in_annotationScopeDeclarations3214)
                    # JavaTreeParser.g:430:58: ( annotationDefaultValue )?
                    alt69 = 2
                    LA69_0 = self.input.LA(1)

                    if (LA69_0 == DEFAULT) :
                        alt69 = 1
                    if alt69 == 1:
                        # JavaTreeParser.g:0:0: annotationDefaultValue
                        pass 
                        self._state.following.append(self.FOLLOW_annotationDefaultValue_in_annotationScopeDeclarations3216)
                        self.annotationDefaultValue()

                        self._state.following.pop()




                    self.match(self.input, UP, None)


                elif alt70 == 2:
                    # JavaTreeParser.g:431:9: ^( VAR_DECLARATION modifierList type variableDeclaratorList )
                    pass 
                    self.match(self.input, VAR_DECLARATION, self.FOLLOW_VAR_DECLARATION_in_annotationScopeDeclarations3229)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_annotationScopeDeclarations3231)
                    self.modifierList()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_type_in_annotationScopeDeclarations3233)
                    self.type()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_variableDeclaratorList_in_annotationScopeDeclarations3235)
                    self.variableDeclaratorList()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt70 == 3:
                    # JavaTreeParser.g:432:9: typeDeclaration
                    pass 
                    self._state.following.append(self.FOLLOW_typeDeclaration_in_annotationScopeDeclarations3246)
                    self.typeDeclaration()

                    self._state.following.pop()



                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 46, annotationScopeDeclarations_StartIndex, success)

            pass

        return 

    # $ANTLR end "annotationScopeDeclarations"


    # $ANTLR start "annotationDefaultValue"
    # JavaTreeParser.g:435:1: annotationDefaultValue : ^( DEFAULT annotationElementValue ) ;
    def annotationDefaultValue(self, ):

        annotationDefaultValue_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 47):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:436:5: ( ^( DEFAULT annotationElementValue ) )
                # JavaTreeParser.g:436:9: ^( DEFAULT annotationElementValue )
                pass 
                self.match(self.input, DEFAULT, self.FOLLOW_DEFAULT_in_annotationDefaultValue3266)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_annotationElementValue_in_annotationDefaultValue3268)
                self.annotationElementValue()

                self._state.following.pop()

                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 47, annotationDefaultValue_StartIndex, success)

            pass

        return 

    # $ANTLR end "annotationDefaultValue"


    # $ANTLR start "block"
    # JavaTreeParser.g:441:1: block : ^( BLOCK_SCOPE ( blockStatement )* ) ;
    def block(self, ):

        block_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 48):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:442:5: ( ^( BLOCK_SCOPE ( blockStatement )* ) )
                # JavaTreeParser.g:442:9: ^( BLOCK_SCOPE ( blockStatement )* )
                pass 
                self.match(self.input, BLOCK_SCOPE, self.FOLLOW_BLOCK_SCOPE_in_block3291)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:442:23: ( blockStatement )*
                    while True: #loop71
                        alt71 = 2
                        LA71_0 = self.input.LA(1)

                        if (LA71_0 == AT or LA71_0 == SEMI or LA71_0 == ASSERT or LA71_0 == BREAK or (CLASS <= LA71_0 <= CONTINUE) or LA71_0 == DO or LA71_0 == ENUM or (FOR <= LA71_0 <= IF) or LA71_0 == INTERFACE or LA71_0 == RETURN or (SWITCH <= LA71_0 <= SYNCHRONIZED) or LA71_0 == THROW or LA71_0 == TRY or LA71_0 == WHILE or LA71_0 == BLOCK_SCOPE or LA71_0 == EXPR or LA71_0 == FOR_EACH or LA71_0 == LABELED_STATEMENT or LA71_0 == VAR_DECLARATION) :
                            alt71 = 1


                        if alt71 == 1:
                            # JavaTreeParser.g:0:0: blockStatement
                            pass 
                            self._state.following.append(self.FOLLOW_blockStatement_in_block3293)
                            self.blockStatement()

                            self._state.following.pop()


                        else:
                            break #loop71



                    self.match(self.input, UP, None)





                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 48, block_StartIndex, success)

            pass

        return 

    # $ANTLR end "block"


    # $ANTLR start "blockStatement"
    # JavaTreeParser.g:445:1: blockStatement : ( localVariableDeclaration | typeDeclaration | st0= statement );
    def blockStatement(self, ):

        blockStatement_StartIndex = self.input.index()
        st0 = None


        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 49):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:446:5: ( localVariableDeclaration | typeDeclaration | st0= statement )
                alt72 = 3
                LA72 = self.input.LA(1)
                if LA72 == VAR_DECLARATION:
                    alt72 = 1
                elif LA72 == AT or LA72 == CLASS or LA72 == ENUM or LA72 == INTERFACE:
                    alt72 = 2
                elif LA72 == SEMI or LA72 == ASSERT or LA72 == BREAK or LA72 == CONTINUE or LA72 == DO or LA72 == FOR or LA72 == IF or LA72 == RETURN or LA72 == SWITCH or LA72 == SYNCHRONIZED or LA72 == THROW or LA72 == TRY or LA72 == WHILE or LA72 == BLOCK_SCOPE or LA72 == EXPR or LA72 == FOR_EACH or LA72 == LABELED_STATEMENT:
                    alt72 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 72, 0, self.input)

                    raise nvae

                if alt72 == 1:
                    # JavaTreeParser.g:446:9: localVariableDeclaration
                    pass 
                    self._state.following.append(self.FOLLOW_localVariableDeclaration_in_blockStatement3314)
                    self.localVariableDeclaration()

                    self._state.following.pop()


                elif alt72 == 2:
                    # JavaTreeParser.g:447:9: typeDeclaration
                    pass 
                    self._state.following.append(self.FOLLOW_typeDeclaration_in_blockStatement3324)
                    self.typeDeclaration()

                    self._state.following.pop()


                elif alt72 == 3:
                    # JavaTreeParser.g:448:9: st0= statement
                    pass 
                    self._state.following.append(self.FOLLOW_statement_in_blockStatement3336)
                    st0 = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.append(st0) 




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 49, blockStatement_StartIndex, success)

            pass

        return 

    # $ANTLR end "blockStatement"


    # $ANTLR start "localVariableDeclaration"
    # JavaTreeParser.g:451:1: localVariableDeclaration : ^( VAR_DECLARATION md1= localModifierList tp1= type vd1= variableDeclaratorList ) ;
    def localVariableDeclaration(self, ):

        localVariableDeclaration_StartIndex = self.input.index()
        md1 = None

        tp1 = None

        vd1 = None


        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 50):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:452:5: ( ^( VAR_DECLARATION md1= localModifierList tp1= type vd1= variableDeclaratorList ) )
                # JavaTreeParser.g:452:9: ^( VAR_DECLARATION md1= localModifierList tp1= type vd1= variableDeclaratorList )
                pass 
                self.match(self.input, VAR_DECLARATION, self.FOLLOW_VAR_DECLARATION_in_localVariableDeclaration3358)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_localModifierList_in_localVariableDeclaration3372)
                md1 = self.localModifierList()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_type_in_localVariableDeclaration3386)
                tp1 = self.type()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_variableDeclaratorList_in_localVariableDeclaration3400)
                vd1 = self.variableDeclaratorList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self.addLocalVariables(vd1, ((tp1 is not None) and [tp1.value] or [None])[0], md1) 


                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 50, localVariableDeclaration_StartIndex, success)

            pass

        return 

    # $ANTLR end "localVariableDeclaration"


    # $ANTLR start "statement"
    # JavaTreeParser.g:462:1: statement returns [value] : ( block | ^( ASSERT expression ( expression )? ) | ^( IF parenthesizedExpression statement ( statement )? ) | ^( FOR forInit forCondition forUpdater statement ) | ^( FOR_EACH localModifierList type id0= IDENT ex0= expression st0= statement ) | ^( WHILE parenthesizedExpression statement ) | ^( DO statement parenthesizedExpression ) | ^( TRY block ( catches )? ( block )? ) | ^( SWITCH parenthesizedExpression switchBlockLabels ) | ^( SYNCHRONIZED parenthesizedExpression block ) | ^( RETURN (ex0= expression )? ) | ^( THROW expression ) | ^( BREAK ( IDENT )? ) | ^( CONTINUE ( IDENT )? ) | ^( LABELED_STATEMENT IDENT statement ) | ex0= expression | SEMI );
    def statement(self, ):

        value = None
        statement_StartIndex = self.input.index()
        id0 = None
        ex0 = None

        st0 = None


        value = ex() 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 51):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:464:5: ( block | ^( ASSERT expression ( expression )? ) | ^( IF parenthesizedExpression statement ( statement )? ) | ^( FOR forInit forCondition forUpdater statement ) | ^( FOR_EACH localModifierList type id0= IDENT ex0= expression st0= statement ) | ^( WHILE parenthesizedExpression statement ) | ^( DO statement parenthesizedExpression ) | ^( TRY block ( catches )? ( block )? ) | ^( SWITCH parenthesizedExpression switchBlockLabels ) | ^( SYNCHRONIZED parenthesizedExpression block ) | ^( RETURN (ex0= expression )? ) | ^( THROW expression ) | ^( BREAK ( IDENT )? ) | ^( CONTINUE ( IDENT )? ) | ^( LABELED_STATEMENT IDENT statement ) | ex0= expression | SEMI )
                alt80 = 17
                LA80 = self.input.LA(1)
                if LA80 == BLOCK_SCOPE:
                    alt80 = 1
                elif LA80 == ASSERT:
                    alt80 = 2
                elif LA80 == IF:
                    alt80 = 3
                elif LA80 == FOR:
                    alt80 = 4
                elif LA80 == FOR_EACH:
                    alt80 = 5
                elif LA80 == WHILE:
                    alt80 = 6
                elif LA80 == DO:
                    alt80 = 7
                elif LA80 == TRY:
                    alt80 = 8
                elif LA80 == SWITCH:
                    alt80 = 9
                elif LA80 == SYNCHRONIZED:
                    alt80 = 10
                elif LA80 == RETURN:
                    alt80 = 11
                elif LA80 == THROW:
                    alt80 = 12
                elif LA80 == BREAK:
                    alt80 = 13
                elif LA80 == CONTINUE:
                    alt80 = 14
                elif LA80 == LABELED_STATEMENT:
                    alt80 = 15
                elif LA80 == EXPR:
                    alt80 = 16
                elif LA80 == SEMI:
                    alt80 = 17
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 80, 0, self.input)

                    raise nvae

                if alt80 == 1:
                    # JavaTreeParser.g:464:9: block
                    pass 
                    self._state.following.append(self.FOLLOW_block_in_statement3457)
                    self.block()

                    self._state.following.pop()


                elif alt80 == 2:
                    # JavaTreeParser.g:465:9: ^( ASSERT expression ( expression )? )
                    pass 
                    self.match(self.input, ASSERT, self.FOLLOW_ASSERT_in_statement3468)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_statement3470)
                    self.expression()

                    self._state.following.pop()
                    # JavaTreeParser.g:465:29: ( expression )?
                    alt73 = 2
                    LA73_0 = self.input.LA(1)

                    if (LA73_0 == EXPR) :
                        alt73 = 1
                    if alt73 == 1:
                        # JavaTreeParser.g:0:0: expression
                        pass 
                        self._state.following.append(self.FOLLOW_expression_in_statement3472)
                        self.expression()

                        self._state.following.pop()




                    self.match(self.input, UP, None)


                elif alt80 == 3:
                    # JavaTreeParser.g:466:9: ^( IF parenthesizedExpression statement ( statement )? )
                    pass 
                    self.match(self.input, IF, self.FOLLOW_IF_in_statement3485)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_statement3487)
                    self.parenthesizedExpression()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_statement_in_statement3489)
                    self.statement()

                    self._state.following.pop()
                    # JavaTreeParser.g:466:48: ( statement )?
                    alt74 = 2
                    LA74_0 = self.input.LA(1)

                    if (LA74_0 == SEMI or LA74_0 == ASSERT or LA74_0 == BREAK or LA74_0 == CONTINUE or LA74_0 == DO or (FOR <= LA74_0 <= IF) or LA74_0 == RETURN or (SWITCH <= LA74_0 <= SYNCHRONIZED) or LA74_0 == THROW or LA74_0 == TRY or LA74_0 == WHILE or LA74_0 == BLOCK_SCOPE or LA74_0 == EXPR or LA74_0 == FOR_EACH or LA74_0 == LABELED_STATEMENT) :
                        alt74 = 1
                    if alt74 == 1:
                        # JavaTreeParser.g:0:0: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statement3491)
                        self.statement()

                        self._state.following.pop()




                    self.match(self.input, UP, None)


                elif alt80 == 4:
                    # JavaTreeParser.g:467:9: ^( FOR forInit forCondition forUpdater statement )
                    pass 
                    self.match(self.input, FOR, self.FOLLOW_FOR_in_statement3504)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_forInit_in_statement3506)
                    self.forInit()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_forCondition_in_statement3508)
                    self.forCondition()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_forUpdater_in_statement3510)
                    self.forUpdater()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_statement_in_statement3512)
                    self.statement()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt80 == 5:
                    # JavaTreeParser.g:469:9: ^( FOR_EACH localModifierList type id0= IDENT ex0= expression st0= statement )
                    pass 
                    self.match(self.input, FOR_EACH, self.FOLLOW_FOR_EACH_in_statement3525)

                    if self._state.backtracking == 0:
                        self.beginFor() 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_localModifierList_in_statement3549)
                    self.localModifierList()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_type_in_statement3561)
                    self.type()

                    self._state.following.pop()
                    id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_statement3575)
                    self._state.following.append(self.FOLLOW_expression_in_statement3589)
                    ex0 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.setExpression(ex(id0.text, ex0, format="${left} in ${right}")) 

                    self._state.following.append(self.FOLLOW_statement_in_statement3615)
                    st0 = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.append(st0) 

                    if self._state.backtracking == 0:
                        self.endFor() 


                    self.match(self.input, UP, None)


                elif alt80 == 6:
                    # JavaTreeParser.g:479:9: ^( WHILE parenthesizedExpression statement )
                    pass 
                    self.match(self.input, WHILE, self.FOLLOW_WHILE_in_statement3650)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_statement3652)
                    self.parenthesizedExpression()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_statement_in_statement3654)
                    self.statement()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt80 == 7:
                    # JavaTreeParser.g:480:9: ^( DO statement parenthesizedExpression )
                    pass 
                    self.match(self.input, DO, self.FOLLOW_DO_in_statement3666)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_statement_in_statement3668)
                    self.statement()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_statement3670)
                    self.parenthesizedExpression()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt80 == 8:
                    # JavaTreeParser.g:481:9: ^( TRY block ( catches )? ( block )? )
                    pass 
                    self.match(self.input, TRY, self.FOLLOW_TRY_in_statement3682)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_block_in_statement3684)
                    self.block()

                    self._state.following.pop()
                    # JavaTreeParser.g:481:21: ( catches )?
                    alt75 = 2
                    LA75_0 = self.input.LA(1)

                    if (LA75_0 == CATCH_CLAUSE_LIST) :
                        alt75 = 1
                    if alt75 == 1:
                        # JavaTreeParser.g:0:0: catches
                        pass 
                        self._state.following.append(self.FOLLOW_catches_in_statement3686)
                        self.catches()

                        self._state.following.pop()



                    # JavaTreeParser.g:481:30: ( block )?
                    alt76 = 2
                    LA76_0 = self.input.LA(1)

                    if (LA76_0 == BLOCK_SCOPE) :
                        alt76 = 1
                    if alt76 == 1:
                        # JavaTreeParser.g:0:0: block
                        pass 
                        self._state.following.append(self.FOLLOW_block_in_statement3689)
                        self.block()

                        self._state.following.pop()




                    self.match(self.input, UP, None)


                elif alt80 == 9:
                    # JavaTreeParser.g:482:9: ^( SWITCH parenthesizedExpression switchBlockLabels )
                    pass 
                    self.match(self.input, SWITCH, self.FOLLOW_SWITCH_in_statement3704)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_statement3706)
                    self.parenthesizedExpression()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_switchBlockLabels_in_statement3708)
                    self.switchBlockLabels()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt80 == 10:
                    # JavaTreeParser.g:483:9: ^( SYNCHRONIZED parenthesizedExpression block )
                    pass 
                    self.match(self.input, SYNCHRONIZED, self.FOLLOW_SYNCHRONIZED_in_statement3720)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_statement3722)
                    self.parenthesizedExpression()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_block_in_statement3724)
                    self.block()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt80 == 11:
                    # JavaTreeParser.g:484:9: ^( RETURN (ex0= expression )? )
                    pass 
                    self.match(self.input, RETURN, self.FOLLOW_RETURN_in_statement3736)

                    if self.input.LA(1) == DOWN:
                        self.match(self.input, DOWN, None)
                        # JavaTreeParser.g:484:18: (ex0= expression )?
                        alt77 = 2
                        LA77_0 = self.input.LA(1)

                        if (LA77_0 == EXPR) :
                            alt77 = 1
                        if alt77 == 1:
                            # JavaTreeParser.g:484:19: ex0= expression
                            pass 
                            self._state.following.append(self.FOLLOW_expression_in_statement3741)
                            ex0 = self.expression()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                value.update(right=ex0) 




                        if self._state.backtracking == 0:
                            value.update(format="return ${right}") 


                        self.match(self.input, UP, None)



                elif alt80 == 12:
                    # JavaTreeParser.g:487:9: ^( THROW expression )
                    pass 
                    self.match(self.input, THROW, self.FOLLOW_THROW_in_statement3777)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_statement3779)
                    self.expression()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt80 == 13:
                    # JavaTreeParser.g:488:9: ^( BREAK ( IDENT )? )
                    pass 
                    self.match(self.input, BREAK, self.FOLLOW_BREAK_in_statement3791)

                    if self.input.LA(1) == DOWN:
                        self.match(self.input, DOWN, None)
                        # JavaTreeParser.g:488:17: ( IDENT )?
                        alt78 = 2
                        LA78_0 = self.input.LA(1)

                        if (LA78_0 == IDENT) :
                            alt78 = 1
                        if alt78 == 1:
                            # JavaTreeParser.g:0:0: IDENT
                            pass 
                            self.match(self.input, IDENT, self.FOLLOW_IDENT_in_statement3793)




                        self.match(self.input, UP, None)



                elif alt80 == 14:
                    # JavaTreeParser.g:489:9: ^( CONTINUE ( IDENT )? )
                    pass 
                    self.match(self.input, CONTINUE, self.FOLLOW_CONTINUE_in_statement3806)

                    if self.input.LA(1) == DOWN:
                        self.match(self.input, DOWN, None)
                        # JavaTreeParser.g:489:20: ( IDENT )?
                        alt79 = 2
                        LA79_0 = self.input.LA(1)

                        if (LA79_0 == IDENT) :
                            alt79 = 1
                        if alt79 == 1:
                            # JavaTreeParser.g:0:0: IDENT
                            pass 
                            self.match(self.input, IDENT, self.FOLLOW_IDENT_in_statement3808)




                        self.match(self.input, UP, None)



                elif alt80 == 15:
                    # JavaTreeParser.g:490:9: ^( LABELED_STATEMENT IDENT statement )
                    pass 
                    self.match(self.input, LABELED_STATEMENT, self.FOLLOW_LABELED_STATEMENT_in_statement3821)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, IDENT, self.FOLLOW_IDENT_in_statement3823)
                    self._state.following.append(self.FOLLOW_statement_in_statement3825)
                    self.statement()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt80 == 16:
                    # JavaTreeParser.g:491:9: ex0= expression
                    pass 
                    self._state.following.append(self.FOLLOW_expression_in_statement3838)
                    ex0 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex0 



                elif alt80 == 17:
                    # JavaTreeParser.g:492:9: SEMI
                    pass 
                    self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement3850)



                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 51, statement_StartIndex, success)

            pass

        return value

    # $ANTLR end "statement"


    # $ANTLR start "catches"
    # JavaTreeParser.g:495:1: catches : ^( CATCH_CLAUSE_LIST ( catchClause )+ ) ;
    def catches(self, ):

        catches_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 52):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:496:5: ( ^( CATCH_CLAUSE_LIST ( catchClause )+ ) )
                # JavaTreeParser.g:496:9: ^( CATCH_CLAUSE_LIST ( catchClause )+ )
                pass 
                self.match(self.input, CATCH_CLAUSE_LIST, self.FOLLOW_CATCH_CLAUSE_LIST_in_catches3871)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:496:29: ( catchClause )+
                cnt81 = 0
                while True: #loop81
                    alt81 = 2
                    LA81_0 = self.input.LA(1)

                    if (LA81_0 == CATCH) :
                        alt81 = 1


                    if alt81 == 1:
                        # JavaTreeParser.g:0:0: catchClause
                        pass 
                        self._state.following.append(self.FOLLOW_catchClause_in_catches3873)
                        self.catchClause()

                        self._state.following.pop()


                    else:
                        if cnt81 >= 1:
                            break #loop81

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(81, self.input)
                        raise eee

                    cnt81 += 1



                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 52, catches_StartIndex, success)

            pass

        return 

    # $ANTLR end "catches"


    # $ANTLR start "catchClause"
    # JavaTreeParser.g:499:1: catchClause : ^( CATCH formalParameterStandardDecl block ) ;
    def catchClause(self, ):

        catchClause_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 53):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:500:5: ( ^( CATCH formalParameterStandardDecl block ) )
                # JavaTreeParser.g:500:9: ^( CATCH formalParameterStandardDecl block )
                pass 
                self.match(self.input, CATCH, self.FOLLOW_CATCH_in_catchClause3895)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_formalParameterStandardDecl_in_catchClause3897)
                self.formalParameterStandardDecl()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_block_in_catchClause3899)
                self.block()

                self._state.following.pop()

                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 53, catchClause_StartIndex, success)

            pass

        return 

    # $ANTLR end "catchClause"


    # $ANTLR start "switchBlockLabels"
    # JavaTreeParser.g:503:1: switchBlockLabels : ^( SWITCH_BLOCK_LABEL_LIST ( switchCaseLabel )* ( switchDefaultLabel )? ( switchCaseLabel )* ) ;
    def switchBlockLabels(self, ):

        switchBlockLabels_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 54):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:504:5: ( ^( SWITCH_BLOCK_LABEL_LIST ( switchCaseLabel )* ( switchDefaultLabel )? ( switchCaseLabel )* ) )
                # JavaTreeParser.g:504:9: ^( SWITCH_BLOCK_LABEL_LIST ( switchCaseLabel )* ( switchDefaultLabel )? ( switchCaseLabel )* )
                pass 
                self.match(self.input, SWITCH_BLOCK_LABEL_LIST, self.FOLLOW_SWITCH_BLOCK_LABEL_LIST_in_switchBlockLabels3920)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:504:35: ( switchCaseLabel )*
                    while True: #loop82
                        alt82 = 2
                        LA82_0 = self.input.LA(1)

                        if (LA82_0 == CASE) :
                            LA82_2 = self.input.LA(2)

                            if (self.synpred125_JavaTreeParser()) :
                                alt82 = 1




                        if alt82 == 1:
                            # JavaTreeParser.g:0:0: switchCaseLabel
                            pass 
                            self._state.following.append(self.FOLLOW_switchCaseLabel_in_switchBlockLabels3922)
                            self.switchCaseLabel()

                            self._state.following.pop()


                        else:
                            break #loop82


                    # JavaTreeParser.g:504:52: ( switchDefaultLabel )?
                    alt83 = 2
                    LA83_0 = self.input.LA(1)

                    if (LA83_0 == DEFAULT) :
                        alt83 = 1
                    if alt83 == 1:
                        # JavaTreeParser.g:0:0: switchDefaultLabel
                        pass 
                        self._state.following.append(self.FOLLOW_switchDefaultLabel_in_switchBlockLabels3925)
                        self.switchDefaultLabel()

                        self._state.following.pop()



                    # JavaTreeParser.g:504:72: ( switchCaseLabel )*
                    while True: #loop84
                        alt84 = 2
                        LA84_0 = self.input.LA(1)

                        if (LA84_0 == CASE) :
                            alt84 = 1


                        if alt84 == 1:
                            # JavaTreeParser.g:0:0: switchCaseLabel
                            pass 
                            self._state.following.append(self.FOLLOW_switchCaseLabel_in_switchBlockLabels3928)
                            self.switchCaseLabel()

                            self._state.following.pop()


                        else:
                            break #loop84



                    self.match(self.input, UP, None)





                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 54, switchBlockLabels_StartIndex, success)

            pass

        return 

    # $ANTLR end "switchBlockLabels"


    # $ANTLR start "switchCaseLabel"
    # JavaTreeParser.g:507:1: switchCaseLabel : ^( CASE expression ( blockStatement )* ) ;
    def switchCaseLabel(self, ):

        switchCaseLabel_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 55):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:508:5: ( ^( CASE expression ( blockStatement )* ) )
                # JavaTreeParser.g:508:9: ^( CASE expression ( blockStatement )* )
                pass 
                self.match(self.input, CASE, self.FOLLOW_CASE_in_switchCaseLabel3950)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_expression_in_switchCaseLabel3952)
                self.expression()

                self._state.following.pop()
                # JavaTreeParser.g:508:27: ( blockStatement )*
                while True: #loop85
                    alt85 = 2
                    LA85_0 = self.input.LA(1)

                    if (LA85_0 == AT or LA85_0 == SEMI or LA85_0 == ASSERT or LA85_0 == BREAK or (CLASS <= LA85_0 <= CONTINUE) or LA85_0 == DO or LA85_0 == ENUM or (FOR <= LA85_0 <= IF) or LA85_0 == INTERFACE or LA85_0 == RETURN or (SWITCH <= LA85_0 <= SYNCHRONIZED) or LA85_0 == THROW or LA85_0 == TRY or LA85_0 == WHILE or LA85_0 == BLOCK_SCOPE or LA85_0 == EXPR or LA85_0 == FOR_EACH or LA85_0 == LABELED_STATEMENT or LA85_0 == VAR_DECLARATION) :
                        alt85 = 1


                    if alt85 == 1:
                        # JavaTreeParser.g:0:0: blockStatement
                        pass 
                        self._state.following.append(self.FOLLOW_blockStatement_in_switchCaseLabel3954)
                        self.blockStatement()

                        self._state.following.pop()


                    else:
                        break #loop85



                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 55, switchCaseLabel_StartIndex, success)

            pass

        return 

    # $ANTLR end "switchCaseLabel"


    # $ANTLR start "switchDefaultLabel"
    # JavaTreeParser.g:511:1: switchDefaultLabel : ^( DEFAULT ( blockStatement )* ) ;
    def switchDefaultLabel(self, ):

        switchDefaultLabel_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 56):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:512:5: ( ^( DEFAULT ( blockStatement )* ) )
                # JavaTreeParser.g:512:9: ^( DEFAULT ( blockStatement )* )
                pass 
                self.match(self.input, DEFAULT, self.FOLLOW_DEFAULT_in_switchDefaultLabel3976)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:512:19: ( blockStatement )*
                    while True: #loop86
                        alt86 = 2
                        LA86_0 = self.input.LA(1)

                        if (LA86_0 == AT or LA86_0 == SEMI or LA86_0 == ASSERT or LA86_0 == BREAK or (CLASS <= LA86_0 <= CONTINUE) or LA86_0 == DO or LA86_0 == ENUM or (FOR <= LA86_0 <= IF) or LA86_0 == INTERFACE or LA86_0 == RETURN or (SWITCH <= LA86_0 <= SYNCHRONIZED) or LA86_0 == THROW or LA86_0 == TRY or LA86_0 == WHILE or LA86_0 == BLOCK_SCOPE or LA86_0 == EXPR or LA86_0 == FOR_EACH or LA86_0 == LABELED_STATEMENT or LA86_0 == VAR_DECLARATION) :
                            alt86 = 1


                        if alt86 == 1:
                            # JavaTreeParser.g:0:0: blockStatement
                            pass 
                            self._state.following.append(self.FOLLOW_blockStatement_in_switchDefaultLabel3978)
                            self.blockStatement()

                            self._state.following.pop()


                        else:
                            break #loop86



                    self.match(self.input, UP, None)





                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 56, switchDefaultLabel_StartIndex, success)

            pass

        return 

    # $ANTLR end "switchDefaultLabel"


    # $ANTLR start "forInit"
    # JavaTreeParser.g:515:1: forInit : ^( FOR_INIT ( localVariableDeclaration | ( expression )* )? ) ;
    def forInit(self, ):

        forInit_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 57):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:516:5: ( ^( FOR_INIT ( localVariableDeclaration | ( expression )* )? ) )
                # JavaTreeParser.g:516:9: ^( FOR_INIT ( localVariableDeclaration | ( expression )* )? )
                pass 
                self.match(self.input, FOR_INIT, self.FOLLOW_FOR_INIT_in_forInit4000)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:516:20: ( localVariableDeclaration | ( expression )* )?
                    alt88 = 3
                    LA88 = self.input.LA(1)
                    if LA88 == VAR_DECLARATION:
                        alt88 = 1
                    elif LA88 == EXPR:
                        alt88 = 2
                    elif LA88 == 3:
                        LA88_3 = self.input.LA(2)

                        if (self.synpred132_JavaTreeParser()) :
                            alt88 = 2
                    if alt88 == 1:
                        # JavaTreeParser.g:516:21: localVariableDeclaration
                        pass 
                        self._state.following.append(self.FOLLOW_localVariableDeclaration_in_forInit4003)
                        self.localVariableDeclaration()

                        self._state.following.pop()


                    elif alt88 == 2:
                        # JavaTreeParser.g:516:48: ( expression )*
                        pass 
                        # JavaTreeParser.g:516:48: ( expression )*
                        while True: #loop87
                            alt87 = 2
                            LA87_0 = self.input.LA(1)

                            if (LA87_0 == EXPR) :
                                alt87 = 1


                            if alt87 == 1:
                                # JavaTreeParser.g:0:0: expression
                                pass 
                                self._state.following.append(self.FOLLOW_expression_in_forInit4007)
                                self.expression()

                                self._state.following.pop()


                            else:
                                break #loop87






                    self.match(self.input, UP, None)





                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 57, forInit_StartIndex, success)

            pass

        return 

    # $ANTLR end "forInit"


    # $ANTLR start "forCondition"
    # JavaTreeParser.g:519:1: forCondition : ^( FOR_CONDITION ( expression )? ) ;
    def forCondition(self, ):

        forCondition_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 58):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:520:5: ( ^( FOR_CONDITION ( expression )? ) )
                # JavaTreeParser.g:520:9: ^( FOR_CONDITION ( expression )? )
                pass 
                self.match(self.input, FOR_CONDITION, self.FOLLOW_FOR_CONDITION_in_forCondition4031)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:520:25: ( expression )?
                    alt89 = 2
                    LA89_0 = self.input.LA(1)

                    if (LA89_0 == EXPR) :
                        alt89 = 1
                    if alt89 == 1:
                        # JavaTreeParser.g:0:0: expression
                        pass 
                        self._state.following.append(self.FOLLOW_expression_in_forCondition4033)
                        self.expression()

                        self._state.following.pop()




                    self.match(self.input, UP, None)





                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 58, forCondition_StartIndex, success)

            pass

        return 

    # $ANTLR end "forCondition"


    # $ANTLR start "forUpdater"
    # JavaTreeParser.g:523:1: forUpdater : ^( FOR_UPDATE ( expression )* ) ;
    def forUpdater(self, ):

        forUpdater_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 59):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:524:5: ( ^( FOR_UPDATE ( expression )* ) )
                # JavaTreeParser.g:524:9: ^( FOR_UPDATE ( expression )* )
                pass 
                self.match(self.input, FOR_UPDATE, self.FOLLOW_FOR_UPDATE_in_forUpdater4055)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:524:22: ( expression )*
                    while True: #loop90
                        alt90 = 2
                        LA90_0 = self.input.LA(1)

                        if (LA90_0 == EXPR) :
                            alt90 = 1


                        if alt90 == 1:
                            # JavaTreeParser.g:0:0: expression
                            pass 
                            self._state.following.append(self.FOLLOW_expression_in_forUpdater4057)
                            self.expression()

                            self._state.following.pop()


                        else:
                            break #loop90



                    self.match(self.input, UP, None)





                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 59, forUpdater_StartIndex, success)

            pass

        return 

    # $ANTLR end "forUpdater"


    # $ANTLR start "parenthesizedExpression"
    # JavaTreeParser.g:529:1: parenthesizedExpression returns [value] : ^( PARENTESIZED_EXPR ex0= expression ) ;
    def parenthesizedExpression(self, ):

        value = None
        parenthesizedExpression_StartIndex = self.input.index()
        ex0 = None


        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 60):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:530:5: ( ^( PARENTESIZED_EXPR ex0= expression ) )
                # JavaTreeParser.g:530:9: ^( PARENTESIZED_EXPR ex0= expression )
                pass 
                self.match(self.input, PARENTESIZED_EXPR, self.FOLLOW_PARENTESIZED_EXPR_in_parenthesizedExpression4085)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_expression_in_parenthesizedExpression4089)
                ex0 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    value = ex(ex0, format="(${left})") 


                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 60, parenthesizedExpression_StartIndex, success)

            pass

        return value

    # $ANTLR end "parenthesizedExpression"


    # $ANTLR start "expression"
    # JavaTreeParser.g:533:1: expression returns [value] : ^( EXPR ex0= expr ) ;
    def expression(self, ):

        value = None
        expression_StartIndex = self.input.index()
        ex0 = None


        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 61):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:534:5: ( ^( EXPR ex0= expr ) )
                # JavaTreeParser.g:534:9: ^( EXPR ex0= expr )
                pass 
                self.match(self.input, EXPR, self.FOLLOW_EXPR_in_expression4116)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_expr_in_expression4120)
                ex0 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    value = ex0 


                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 61, expression_StartIndex, success)

            pass

        return value

    # $ANTLR end "expression"


    # $ANTLR start "expr"
    # JavaTreeParser.g:537:1: expr returns [value] : ( ^( ASSIGN lv0= expr rv0= expr ) | ^( PLUS_ASSIGN lv0= expr rv0= expr ) | ^( MINUS_ASSIGN expr expr ) | ^( STAR_ASSIGN expr expr ) | ^( DIV_ASSIGN expr expr ) | ^( AND_ASSIGN expr expr ) | ^( OR_ASSIGN expr expr ) | ^( XOR_ASSIGN expr expr ) | ^( MOD_ASSIGN expr expr ) | ^( BIT_SHIFT_RIGHT_ASSIGN expr expr ) | ^( SHIFT_RIGHT_ASSIGN expr expr ) | ^( SHIFT_LEFT_ASSIGN expr expr ) | ^( QUESTION lv0= expr rv0= expr cv0= expr ) | ^( LOGICAL_OR expr expr ) | ^( LOGICAL_AND expr expr ) | ^( OR expr expr ) | ^( XOR expr expr ) | ^( AND expr expr ) | ^( EQUAL lv0= expr rv0= expr ) | ^( NOT_EQUAL expr expr ) | ^( INSTANCEOF expr type ) | ^( LESS_OR_EQUAL expr expr ) | ^( GREATER_OR_EQUAL expr expr ) | ^( BIT_SHIFT_RIGHT expr expr ) | ^( SHIFT_RIGHT expr expr ) | ^( GREATER_THAN expr expr ) | ^( SHIFT_LEFT expr expr ) | ^( LESS_THAN expr expr ) | ^( PLUS lv0= expr rv0= expr ) | ^( MINUS expr expr ) | ^( STAR expr expr ) | ^( DIV expr expr ) | ^( MOD expr expr ) | ^( UNARY_PLUS expr ) | ^( UNARY_MINUS expr ) | ^( PRE_INC expr ) | ^( PRE_DEC expr ) | ^( POST_INC expr ) | ^( POST_DEC expr ) | ^( NOT expr ) | ^( LOGICAL_NOT expr ) | ^( CAST_EXPR type expr ) | pe0= primaryExpression );
    def expr(self, ):

        value = None
        expr_StartIndex = self.input.index()
        lv0 = None

        rv0 = None

        cv0 = None

        pe0 = None


        value = ex() 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 62):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:539:5: ( ^( ASSIGN lv0= expr rv0= expr ) | ^( PLUS_ASSIGN lv0= expr rv0= expr ) | ^( MINUS_ASSIGN expr expr ) | ^( STAR_ASSIGN expr expr ) | ^( DIV_ASSIGN expr expr ) | ^( AND_ASSIGN expr expr ) | ^( OR_ASSIGN expr expr ) | ^( XOR_ASSIGN expr expr ) | ^( MOD_ASSIGN expr expr ) | ^( BIT_SHIFT_RIGHT_ASSIGN expr expr ) | ^( SHIFT_RIGHT_ASSIGN expr expr ) | ^( SHIFT_LEFT_ASSIGN expr expr ) | ^( QUESTION lv0= expr rv0= expr cv0= expr ) | ^( LOGICAL_OR expr expr ) | ^( LOGICAL_AND expr expr ) | ^( OR expr expr ) | ^( XOR expr expr ) | ^( AND expr expr ) | ^( EQUAL lv0= expr rv0= expr ) | ^( NOT_EQUAL expr expr ) | ^( INSTANCEOF expr type ) | ^( LESS_OR_EQUAL expr expr ) | ^( GREATER_OR_EQUAL expr expr ) | ^( BIT_SHIFT_RIGHT expr expr ) | ^( SHIFT_RIGHT expr expr ) | ^( GREATER_THAN expr expr ) | ^( SHIFT_LEFT expr expr ) | ^( LESS_THAN expr expr ) | ^( PLUS lv0= expr rv0= expr ) | ^( MINUS expr expr ) | ^( STAR expr expr ) | ^( DIV expr expr ) | ^( MOD expr expr ) | ^( UNARY_PLUS expr ) | ^( UNARY_MINUS expr ) | ^( PRE_INC expr ) | ^( PRE_DEC expr ) | ^( POST_INC expr ) | ^( POST_DEC expr ) | ^( NOT expr ) | ^( LOGICAL_NOT expr ) | ^( CAST_EXPR type expr ) | pe0= primaryExpression )
                alt91 = 43
                LA91 = self.input.LA(1)
                if LA91 == ASSIGN:
                    alt91 = 1
                elif LA91 == PLUS_ASSIGN:
                    alt91 = 2
                elif LA91 == MINUS_ASSIGN:
                    alt91 = 3
                elif LA91 == STAR_ASSIGN:
                    alt91 = 4
                elif LA91 == DIV_ASSIGN:
                    alt91 = 5
                elif LA91 == AND_ASSIGN:
                    alt91 = 6
                elif LA91 == OR_ASSIGN:
                    alt91 = 7
                elif LA91 == XOR_ASSIGN:
                    alt91 = 8
                elif LA91 == MOD_ASSIGN:
                    alt91 = 9
                elif LA91 == BIT_SHIFT_RIGHT_ASSIGN:
                    alt91 = 10
                elif LA91 == SHIFT_RIGHT_ASSIGN:
                    alt91 = 11
                elif LA91 == SHIFT_LEFT_ASSIGN:
                    alt91 = 12
                elif LA91 == QUESTION:
                    alt91 = 13
                elif LA91 == LOGICAL_OR:
                    alt91 = 14
                elif LA91 == LOGICAL_AND:
                    alt91 = 15
                elif LA91 == OR:
                    alt91 = 16
                elif LA91 == XOR:
                    alt91 = 17
                elif LA91 == AND:
                    alt91 = 18
                elif LA91 == EQUAL:
                    alt91 = 19
                elif LA91 == NOT_EQUAL:
                    alt91 = 20
                elif LA91 == INSTANCEOF:
                    alt91 = 21
                elif LA91 == LESS_OR_EQUAL:
                    alt91 = 22
                elif LA91 == GREATER_OR_EQUAL:
                    alt91 = 23
                elif LA91 == BIT_SHIFT_RIGHT:
                    alt91 = 24
                elif LA91 == SHIFT_RIGHT:
                    alt91 = 25
                elif LA91 == GREATER_THAN:
                    alt91 = 26
                elif LA91 == SHIFT_LEFT:
                    alt91 = 27
                elif LA91 == LESS_THAN:
                    alt91 = 28
                elif LA91 == PLUS:
                    alt91 = 29
                elif LA91 == MINUS:
                    alt91 = 30
                elif LA91 == STAR:
                    alt91 = 31
                elif LA91 == DIV:
                    alt91 = 32
                elif LA91 == MOD:
                    alt91 = 33
                elif LA91 == UNARY_PLUS:
                    alt91 = 34
                elif LA91 == UNARY_MINUS:
                    alt91 = 35
                elif LA91 == PRE_INC:
                    alt91 = 36
                elif LA91 == PRE_DEC:
                    alt91 = 37
                elif LA91 == POST_INC:
                    alt91 = 38
                elif LA91 == POST_DEC:
                    alt91 = 39
                elif LA91 == NOT:
                    alt91 = 40
                elif LA91 == LOGICAL_NOT:
                    alt91 = 41
                elif LA91 == CAST_EXPR:
                    alt91 = 42
                elif LA91 == DOT or LA91 == FALSE or LA91 == NULL or LA91 == SUPER or LA91 == THIS or LA91 == TRUE or LA91 == ARRAY_DECLARATOR or LA91 == ARRAY_ELEMENT_ACCESS or LA91 == CLASS_CONSTRUCTOR_CALL or LA91 == METHOD_CALL or LA91 == PARENTESIZED_EXPR or LA91 == STATIC_ARRAY_CREATOR or LA91 == SUPER_CONSTRUCTOR_CALL or LA91 == THIS_CONSTRUCTOR_CALL or LA91 == IDENT or LA91 == HEX_LITERAL or LA91 == OCTAL_LITERAL or LA91 == DECIMAL_LITERAL or LA91 == FLOATING_POINT_LITERAL or LA91 == CHARACTER_LITERAL or LA91 == STRING_LITERAL:
                    alt91 = 43
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 91, 0, self.input)

                    raise nvae

                if alt91 == 1:
                    # JavaTreeParser.g:539:9: ^( ASSIGN lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_expr4156)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4160)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4164)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value.update(left=lv0, right=rv0, format="${left} = ${right}") 


                    self.match(self.input, UP, None)


                elif alt91 == 2:
                    # JavaTreeParser.g:541:9: ^( PLUS_ASSIGN lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, PLUS_ASSIGN, self.FOLLOW_PLUS_ASSIGN_in_expr4186)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4190)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4194)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value.update(left=lv0, right=rv0, format="${left} += ${right}") 


                    self.match(self.input, UP, None)


                elif alt91 == 3:
                    # JavaTreeParser.g:543:9: ^( MINUS_ASSIGN expr expr )
                    pass 
                    self.match(self.input, MINUS_ASSIGN, self.FOLLOW_MINUS_ASSIGN_in_expr4216)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4218)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4220)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 4:
                    # JavaTreeParser.g:544:9: ^( STAR_ASSIGN expr expr )
                    pass 
                    self.match(self.input, STAR_ASSIGN, self.FOLLOW_STAR_ASSIGN_in_expr4232)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4234)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4236)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 5:
                    # JavaTreeParser.g:545:9: ^( DIV_ASSIGN expr expr )
                    pass 
                    self.match(self.input, DIV_ASSIGN, self.FOLLOW_DIV_ASSIGN_in_expr4248)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4250)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4252)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 6:
                    # JavaTreeParser.g:546:9: ^( AND_ASSIGN expr expr )
                    pass 
                    self.match(self.input, AND_ASSIGN, self.FOLLOW_AND_ASSIGN_in_expr4264)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4266)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4268)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 7:
                    # JavaTreeParser.g:547:9: ^( OR_ASSIGN expr expr )
                    pass 
                    self.match(self.input, OR_ASSIGN, self.FOLLOW_OR_ASSIGN_in_expr4280)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4282)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4284)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 8:
                    # JavaTreeParser.g:548:9: ^( XOR_ASSIGN expr expr )
                    pass 
                    self.match(self.input, XOR_ASSIGN, self.FOLLOW_XOR_ASSIGN_in_expr4296)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4298)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4300)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 9:
                    # JavaTreeParser.g:549:9: ^( MOD_ASSIGN expr expr )
                    pass 
                    self.match(self.input, MOD_ASSIGN, self.FOLLOW_MOD_ASSIGN_in_expr4312)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4314)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4316)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 10:
                    # JavaTreeParser.g:550:9: ^( BIT_SHIFT_RIGHT_ASSIGN expr expr )
                    pass 
                    self.match(self.input, BIT_SHIFT_RIGHT_ASSIGN, self.FOLLOW_BIT_SHIFT_RIGHT_ASSIGN_in_expr4328)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4330)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4332)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 11:
                    # JavaTreeParser.g:551:9: ^( SHIFT_RIGHT_ASSIGN expr expr )
                    pass 
                    self.match(self.input, SHIFT_RIGHT_ASSIGN, self.FOLLOW_SHIFT_RIGHT_ASSIGN_in_expr4344)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4346)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4348)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 12:
                    # JavaTreeParser.g:552:9: ^( SHIFT_LEFT_ASSIGN expr expr )
                    pass 
                    self.match(self.input, SHIFT_LEFT_ASSIGN, self.FOLLOW_SHIFT_LEFT_ASSIGN_in_expr4360)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4362)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4364)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 13:
                    # JavaTreeParser.g:553:9: ^( QUESTION lv0= expr rv0= expr cv0= expr )
                    pass 
                    self.match(self.input, QUESTION, self.FOLLOW_QUESTION_in_expr4376)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4380)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4384)
                    rv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4388)
                    cv0 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        value.update(left=lv0, right=rv0,
                                      format="(${right} if ${left} else ${center})", center=cv0) 



                elif alt91 == 14:
                    # JavaTreeParser.g:556:9: ^( LOGICAL_OR expr expr )
                    pass 
                    self.match(self.input, LOGICAL_OR, self.FOLLOW_LOGICAL_OR_in_expr4412)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4414)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4416)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 15:
                    # JavaTreeParser.g:557:9: ^( LOGICAL_AND expr expr )
                    pass 
                    self.match(self.input, LOGICAL_AND, self.FOLLOW_LOGICAL_AND_in_expr4428)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4430)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4432)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 16:
                    # JavaTreeParser.g:558:9: ^( OR expr expr )
                    pass 
                    self.match(self.input, OR, self.FOLLOW_OR_in_expr4444)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4446)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4448)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 17:
                    # JavaTreeParser.g:559:9: ^( XOR expr expr )
                    pass 
                    self.match(self.input, XOR, self.FOLLOW_XOR_in_expr4460)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4462)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4464)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 18:
                    # JavaTreeParser.g:560:9: ^( AND expr expr )
                    pass 
                    self.match(self.input, AND, self.FOLLOW_AND_in_expr4476)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4478)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4480)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 19:
                    # JavaTreeParser.g:561:9: ^( EQUAL lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_expr4492)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4496)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4500)
                    rv0 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        value.update(left=lv0, right=rv0, format="${left} == ${right}") 



                elif alt91 == 20:
                    # JavaTreeParser.g:563:9: ^( NOT_EQUAL expr expr )
                    pass 
                    self.match(self.input, NOT_EQUAL, self.FOLLOW_NOT_EQUAL_in_expr4524)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4526)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4528)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 21:
                    # JavaTreeParser.g:564:9: ^( INSTANCEOF expr type )
                    pass 
                    self.match(self.input, INSTANCEOF, self.FOLLOW_INSTANCEOF_in_expr4540)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4542)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_type_in_expr4544)
                    self.type()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 22:
                    # JavaTreeParser.g:565:9: ^( LESS_OR_EQUAL expr expr )
                    pass 
                    self.match(self.input, LESS_OR_EQUAL, self.FOLLOW_LESS_OR_EQUAL_in_expr4556)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4558)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4560)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 23:
                    # JavaTreeParser.g:566:9: ^( GREATER_OR_EQUAL expr expr )
                    pass 
                    self.match(self.input, GREATER_OR_EQUAL, self.FOLLOW_GREATER_OR_EQUAL_in_expr4572)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4574)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4576)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 24:
                    # JavaTreeParser.g:567:9: ^( BIT_SHIFT_RIGHT expr expr )
                    pass 
                    self.match(self.input, BIT_SHIFT_RIGHT, self.FOLLOW_BIT_SHIFT_RIGHT_in_expr4588)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4590)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4592)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 25:
                    # JavaTreeParser.g:568:9: ^( SHIFT_RIGHT expr expr )
                    pass 
                    self.match(self.input, SHIFT_RIGHT, self.FOLLOW_SHIFT_RIGHT_in_expr4604)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4606)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4608)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 26:
                    # JavaTreeParser.g:569:9: ^( GREATER_THAN expr expr )
                    pass 
                    self.match(self.input, GREATER_THAN, self.FOLLOW_GREATER_THAN_in_expr4620)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4622)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4624)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 27:
                    # JavaTreeParser.g:570:9: ^( SHIFT_LEFT expr expr )
                    pass 
                    self.match(self.input, SHIFT_LEFT, self.FOLLOW_SHIFT_LEFT_in_expr4636)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4638)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4640)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 28:
                    # JavaTreeParser.g:571:9: ^( LESS_THAN expr expr )
                    pass 
                    self.match(self.input, LESS_THAN, self.FOLLOW_LESS_THAN_in_expr4652)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4654)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4656)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 29:
                    # JavaTreeParser.g:572:9: ^( PLUS lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, PLUS, self.FOLLOW_PLUS_in_expr4668)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4672)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4676)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value.update(left=lv0, right=rv0, format="${left} + ${right}") 


                    self.match(self.input, UP, None)


                elif alt91 == 30:
                    # JavaTreeParser.g:574:9: ^( MINUS expr expr )
                    pass 
                    self.match(self.input, MINUS, self.FOLLOW_MINUS_in_expr4698)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4700)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4702)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 31:
                    # JavaTreeParser.g:575:9: ^( STAR expr expr )
                    pass 
                    self.match(self.input, STAR, self.FOLLOW_STAR_in_expr4714)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4716)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4718)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 32:
                    # JavaTreeParser.g:576:9: ^( DIV expr expr )
                    pass 
                    self.match(self.input, DIV, self.FOLLOW_DIV_in_expr4730)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4732)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4734)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 33:
                    # JavaTreeParser.g:577:9: ^( MOD expr expr )
                    pass 
                    self.match(self.input, MOD, self.FOLLOW_MOD_in_expr4746)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4748)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4750)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 34:
                    # JavaTreeParser.g:578:9: ^( UNARY_PLUS expr )
                    pass 
                    self.match(self.input, UNARY_PLUS, self.FOLLOW_UNARY_PLUS_in_expr4762)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4764)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 35:
                    # JavaTreeParser.g:579:9: ^( UNARY_MINUS expr )
                    pass 
                    self.match(self.input, UNARY_MINUS, self.FOLLOW_UNARY_MINUS_in_expr4776)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4778)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 36:
                    # JavaTreeParser.g:580:9: ^( PRE_INC expr )
                    pass 
                    self.match(self.input, PRE_INC, self.FOLLOW_PRE_INC_in_expr4790)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4792)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 37:
                    # JavaTreeParser.g:581:9: ^( PRE_DEC expr )
                    pass 
                    self.match(self.input, PRE_DEC, self.FOLLOW_PRE_DEC_in_expr4804)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4806)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 38:
                    # JavaTreeParser.g:582:9: ^( POST_INC expr )
                    pass 
                    self.match(self.input, POST_INC, self.FOLLOW_POST_INC_in_expr4818)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4820)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 39:
                    # JavaTreeParser.g:583:9: ^( POST_DEC expr )
                    pass 
                    self.match(self.input, POST_DEC, self.FOLLOW_POST_DEC_in_expr4832)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4834)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 40:
                    # JavaTreeParser.g:584:9: ^( NOT expr )
                    pass 
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_expr4846)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4848)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 41:
                    # JavaTreeParser.g:585:9: ^( LOGICAL_NOT expr )
                    pass 
                    self.match(self.input, LOGICAL_NOT, self.FOLLOW_LOGICAL_NOT_in_expr4860)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr4862)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 42:
                    # JavaTreeParser.g:586:9: ^( CAST_EXPR type expr )
                    pass 
                    self.match(self.input, CAST_EXPR, self.FOLLOW_CAST_EXPR_in_expr4874)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_type_in_expr4876)
                    self.type()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr4878)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt91 == 43:
                    # JavaTreeParser.g:587:9: pe0= primaryExpression
                    pass 
                    self._state.following.append(self.FOLLOW_primaryExpression_in_expr4891)
                    pe0 = self.primaryExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        if pe0:value.update(pe0) 




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 62, expr_StartIndex, success)

            pass

        return value

    # $ANTLR end "expr"


    # $ANTLR start "primaryExpression"
    # JavaTreeParser.g:590:1: primaryExpression returns [value] : ( ^( DOT (p0= primaryExpression ( IDENT | THIS | SUPER | ne0= innerNewExpression | CLASS ) | pt0= primitiveType CLASS | VOID CLASS ) ) | parenthesizedExpression | IDENT | ^( METHOD_CALL p0= primaryExpression ( genericTypeArgumentList )? a0= arguments ) | ec0= explicitConstructorCall | ^( ARRAY_ELEMENT_ACCESS p0= primaryExpression e0= expression ) | literal | newExpression | THIS | arrayTypeDeclarator | SUPER );
    def primaryExpression(self, ):

        value = None
        primaryExpression_StartIndex = self.input.index()
        IDENT4 = None
        IDENT6 = None
        p0 = None

        ne0 = None

        pt0 = None

        a0 = None

        ec0 = None

        e0 = None

        parenthesizedExpression5 = None

        literal7 = None

        newExpression8 = None


        value = ex() 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 63):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:592:5: ( ^( DOT (p0= primaryExpression ( IDENT | THIS | SUPER | ne0= innerNewExpression | CLASS ) | pt0= primitiveType CLASS | VOID CLASS ) ) | parenthesizedExpression | IDENT | ^( METHOD_CALL p0= primaryExpression ( genericTypeArgumentList )? a0= arguments ) | ec0= explicitConstructorCall | ^( ARRAY_ELEMENT_ACCESS p0= primaryExpression e0= expression ) | literal | newExpression | THIS | arrayTypeDeclarator | SUPER )
                alt95 = 11
                LA95 = self.input.LA(1)
                if LA95 == DOT:
                    alt95 = 1
                elif LA95 == PARENTESIZED_EXPR:
                    alt95 = 2
                elif LA95 == IDENT:
                    alt95 = 3
                elif LA95 == METHOD_CALL:
                    alt95 = 4
                elif LA95 == SUPER_CONSTRUCTOR_CALL or LA95 == THIS_CONSTRUCTOR_CALL:
                    alt95 = 5
                elif LA95 == ARRAY_ELEMENT_ACCESS:
                    alt95 = 6
                elif LA95 == FALSE or LA95 == NULL or LA95 == TRUE or LA95 == HEX_LITERAL or LA95 == OCTAL_LITERAL or LA95 == DECIMAL_LITERAL or LA95 == FLOATING_POINT_LITERAL or LA95 == CHARACTER_LITERAL or LA95 == STRING_LITERAL:
                    alt95 = 7
                elif LA95 == CLASS_CONSTRUCTOR_CALL or LA95 == STATIC_ARRAY_CREATOR:
                    alt95 = 8
                elif LA95 == THIS:
                    alt95 = 9
                elif LA95 == ARRAY_DECLARATOR:
                    alt95 = 10
                elif LA95 == SUPER:
                    alt95 = 11
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 95, 0, self.input)

                    raise nvae

                if alt95 == 1:
                    # JavaTreeParser.g:592:9: ^( DOT (p0= primaryExpression ( IDENT | THIS | SUPER | ne0= innerNewExpression | CLASS ) | pt0= primitiveType CLASS | VOID CLASS ) )
                    pass 
                    self.match(self.input, DOT, self.FOLLOW_DOT_in_primaryExpression4928)

                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:593:13: (p0= primaryExpression ( IDENT | THIS | SUPER | ne0= innerNewExpression | CLASS ) | pt0= primitiveType CLASS | VOID CLASS )
                    alt93 = 3
                    LA93 = self.input.LA(1)
                    if LA93 == DOT or LA93 == FALSE or LA93 == NULL or LA93 == SUPER or LA93 == THIS or LA93 == TRUE or LA93 == ARRAY_DECLARATOR or LA93 == ARRAY_ELEMENT_ACCESS or LA93 == CLASS_CONSTRUCTOR_CALL or LA93 == METHOD_CALL or LA93 == PARENTESIZED_EXPR or LA93 == STATIC_ARRAY_CREATOR or LA93 == SUPER_CONSTRUCTOR_CALL or LA93 == THIS_CONSTRUCTOR_CALL or LA93 == IDENT or LA93 == HEX_LITERAL or LA93 == OCTAL_LITERAL or LA93 == DECIMAL_LITERAL or LA93 == FLOATING_POINT_LITERAL or LA93 == CHARACTER_LITERAL or LA93 == STRING_LITERAL:
                        alt93 = 1
                    elif LA93 == BOOLEAN or LA93 == BYTE or LA93 == CHAR or LA93 == DOUBLE or LA93 == FLOAT or LA93 == INT or LA93 == LONG or LA93 == SHORT:
                        alt93 = 2
                    elif LA93 == VOID:
                        alt93 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 93, 0, self.input)

                        raise nvae

                    if alt93 == 1:
                        # JavaTreeParser.g:593:17: p0= primaryExpression ( IDENT | THIS | SUPER | ne0= innerNewExpression | CLASS )
                        pass 
                        self._state.following.append(self.FOLLOW_primaryExpression_in_primaryExpression4948)
                        p0 = self.primaryExpression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            value = ex(p0, format="${left}.${right}") 

                        # JavaTreeParser.g:595:17: ( IDENT | THIS | SUPER | ne0= innerNewExpression | CLASS )
                        alt92 = 5
                        LA92 = self.input.LA(1)
                        if LA92 == IDENT:
                            alt92 = 1
                        elif LA92 == THIS:
                            alt92 = 2
                        elif LA92 == SUPER:
                            alt92 = 3
                        elif LA92 == CLASS_CONSTRUCTOR_CALL:
                            alt92 = 4
                        elif LA92 == CLASS:
                            alt92 = 5
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 92, 0, self.input)

                            raise nvae

                        if alt92 == 1:
                            # JavaTreeParser.g:595:21: IDENT
                            pass 
                            IDENT4=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_primaryExpression4988)
                            if self._state.backtracking == 0:
                                value["right"] = ex(IDENT4.text, format="${left}") 



                        elif alt92 == 2:
                            # JavaTreeParser.g:596:21: THIS
                            pass 
                            self.match(self.input, THIS, self.FOLLOW_THIS_in_primaryExpression5012)
                            if self._state.backtracking == 0:
                                value["format"] = "${left}" 



                        elif alt92 == 3:
                            # JavaTreeParser.g:597:21: SUPER
                            pass 
                            self.match(self.input, SUPER, self.FOLLOW_SUPER_in_primaryExpression5038)
                            if self._state.backtracking == 0:
                                value["format"] = "${left}"
                                value["left"] = ex(value["left"], "", "super(${left}, self)")
                                                 



                        elif alt92 == 4:
                            # JavaTreeParser.g:601:18: ne0= innerNewExpression
                            pass 
                            self._state.following.append(self.FOLLOW_innerNewExpression_in_primaryExpression5078)
                            ne0 = self.innerNewExpression()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                value = ne0 



                        elif alt92 == 5:
                            # JavaTreeParser.g:602:21: CLASS
                            pass 
                            self.match(self.input, CLASS, self.FOLLOW_CLASS_in_primaryExpression5102)
                            if self._state.backtracking == 0:
                                value["right"] = ex("__class__", "", "${left}") 






                    elif alt93 == 2:
                        # JavaTreeParser.g:604:17: pt0= primitiveType CLASS
                        pass 
                        self._state.following.append(self.FOLLOW_primitiveType_in_primaryExpression5142)
                        pt0 = self.primitiveType()

                        self._state.following.pop()
                        self.match(self.input, CLASS, self.FOLLOW_CLASS_in_primaryExpression5144)
                        if self._state.backtracking == 0:
                            value = ex(((pt0 is not None) and [self.input.getTokenStream().toString(
                                self.input.getTreeAdaptor().getTokenStartIndex(pt0.start),
                                self.input.getTreeAdaptor().getTokenStopIndex(pt0.start)
                                )] or [None])[0], "__class__", "${left}.${right}") 



                    elif alt93 == 3:
                        # JavaTreeParser.g:605:17: VOID CLASS
                        pass 
                        self.match(self.input, VOID, self.FOLLOW_VOID_in_primaryExpression5164)
                        self.match(self.input, CLASS, self.FOLLOW_CLASS_in_primaryExpression5166)
                        if self._state.backtracking == 0:
                            value = ex("None", "__class__", "${left}.${right}") 





                    self.match(self.input, UP, None)


                elif alt95 == 2:
                    # JavaTreeParser.g:609:9: parenthesizedExpression
                    pass 
                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_primaryExpression5203)
                    parenthesizedExpression5 = self.parenthesizedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = parenthesizedExpression5 



                elif alt95 == 3:
                    # JavaTreeParser.g:611:9: IDENT
                    pass 
                    IDENT6=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_primaryExpression5216)
                    if self._state.backtracking == 0:
                        value = ex(IDENT6.text, format="${left}", rename=True)  



                elif alt95 == 4:
                    # JavaTreeParser.g:613:9: ^( METHOD_CALL p0= primaryExpression ( genericTypeArgumentList )? a0= arguments )
                    pass 
                    self.match(self.input, METHOD_CALL, self.FOLLOW_METHOD_CALL_in_primaryExpression5230)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_primaryExpression_in_primaryExpression5244)
                    p0 = self.primaryExpression()

                    self._state.following.pop()
                    # JavaTreeParser.g:615:11: ( genericTypeArgumentList )?
                    alt94 = 2
                    LA94_0 = self.input.LA(1)

                    if (LA94_0 == GENERIC_TYPE_ARG_LIST) :
                        alt94 = 1
                    if alt94 == 1:
                        # JavaTreeParser.g:0:0: genericTypeArgumentList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeArgumentList_in_primaryExpression5256)
                        self.genericTypeArgumentList()

                        self._state.following.pop()



                    self._state.following.append(self.FOLLOW_arguments_in_primaryExpression5271)
                    a0 = self.arguments()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex(p0, a0, "${left}(${right})") 


                    self.match(self.input, UP, None)


                elif alt95 == 5:
                    # JavaTreeParser.g:620:9: ec0= explicitConstructorCall
                    pass 
                    self._state.following.append(self.FOLLOW_explicitConstructorCall_in_primaryExpression5306)
                    ec0 = self.explicitConstructorCall()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ec0 



                elif alt95 == 6:
                    # JavaTreeParser.g:622:9: ^( ARRAY_ELEMENT_ACCESS p0= primaryExpression e0= expression )
                    pass 
                    self.match(self.input, ARRAY_ELEMENT_ACCESS, self.FOLLOW_ARRAY_ELEMENT_ACCESS_in_primaryExpression5320)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_primaryExpression_in_primaryExpression5334)
                    p0 = self.primaryExpression()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expression_in_primaryExpression5348)
                    e0 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex(p0, e0, "${left}[${right}]") 


                    self.match(self.input, UP, None)


                elif alt95 == 7:
                    # JavaTreeParser.g:628:9: literal
                    pass 
                    self._state.following.append(self.FOLLOW_literal_in_primaryExpression5381)
                    literal7 = self.literal()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex(left=((literal7 is not None) and [literal7.value] or [None])[0], format="${left}", rename=False) 



                elif alt95 == 8:
                    # JavaTreeParser.g:630:9: newExpression
                    pass 
                    self._state.following.append(self.FOLLOW_newExpression_in_primaryExpression5394)
                    newExpression8 = self.newExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = newExpression8 



                elif alt95 == 9:
                    # JavaTreeParser.g:632:9: THIS
                    pass 
                    self.match(self.input, THIS, self.FOLLOW_THIS_in_primaryExpression5407)
                    if self._state.backtracking == 0:
                        value = ex("self", format="${left}") 



                elif alt95 == 10:
                    # JavaTreeParser.g:634:9: arrayTypeDeclarator
                    pass 
                    self._state.following.append(self.FOLLOW_arrayTypeDeclarator_in_primaryExpression5420)
                    self.arrayTypeDeclarator()

                    self._state.following.pop()


                elif alt95 == 11:
                    # JavaTreeParser.g:636:9: SUPER
                    pass 
                    self.match(self.input, SUPER, self.FOLLOW_SUPER_in_primaryExpression5431)
                    if self._state.backtracking == 0:
                        value = ex(self.topParentName, format="super(${left}, self)") 




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 63, primaryExpression_StartIndex, success)

            pass

        return value

    # $ANTLR end "primaryExpression"


    # $ANTLR start "explicitConstructorCall"
    # JavaTreeParser.g:640:1: explicitConstructorCall returns [value] : ( ^( THIS_CONSTRUCTOR_CALL ( genericTypeArgumentList )? arguments ) | ^( SUPER_CONSTRUCTOR_CALL ( primaryExpression )? ( genericTypeArgumentList )? arguments ) );
    def explicitConstructorCall(self, ):

        value = None
        explicitConstructorCall_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 64):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:641:5: ( ^( THIS_CONSTRUCTOR_CALL ( genericTypeArgumentList )? arguments ) | ^( SUPER_CONSTRUCTOR_CALL ( primaryExpression )? ( genericTypeArgumentList )? arguments ) )
                alt99 = 2
                LA99_0 = self.input.LA(1)

                if (LA99_0 == THIS_CONSTRUCTOR_CALL) :
                    alt99 = 1
                elif (LA99_0 == SUPER_CONSTRUCTOR_CALL) :
                    alt99 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 99, 0, self.input)

                    raise nvae

                if alt99 == 1:
                    # JavaTreeParser.g:641:9: ^( THIS_CONSTRUCTOR_CALL ( genericTypeArgumentList )? arguments )
                    pass 
                    self.match(self.input, THIS_CONSTRUCTOR_CALL, self.FOLLOW_THIS_CONSTRUCTOR_CALL_in_explicitConstructorCall5458)

                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:641:33: ( genericTypeArgumentList )?
                    alt96 = 2
                    LA96_0 = self.input.LA(1)

                    if (LA96_0 == GENERIC_TYPE_ARG_LIST) :
                        alt96 = 1
                    if alt96 == 1:
                        # JavaTreeParser.g:0:0: genericTypeArgumentList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeArgumentList_in_explicitConstructorCall5460)
                        self.genericTypeArgumentList()

                        self._state.following.pop()



                    self._state.following.append(self.FOLLOW_arguments_in_explicitConstructorCall5463)
                    self.arguments()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt99 == 2:
                    # JavaTreeParser.g:642:9: ^( SUPER_CONSTRUCTOR_CALL ( primaryExpression )? ( genericTypeArgumentList )? arguments )
                    pass 
                    self.match(self.input, SUPER_CONSTRUCTOR_CALL, self.FOLLOW_SUPER_CONSTRUCTOR_CALL_in_explicitConstructorCall5475)

                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:642:34: ( primaryExpression )?
                    alt97 = 2
                    LA97_0 = self.input.LA(1)

                    if (LA97_0 == DOT or LA97_0 == FALSE or LA97_0 == NULL or LA97_0 == SUPER or LA97_0 == THIS or LA97_0 == TRUE or LA97_0 == ARRAY_DECLARATOR or LA97_0 == ARRAY_ELEMENT_ACCESS or LA97_0 == CLASS_CONSTRUCTOR_CALL or LA97_0 == METHOD_CALL or LA97_0 == PARENTESIZED_EXPR or (STATIC_ARRAY_CREATOR <= LA97_0 <= SUPER_CONSTRUCTOR_CALL) or LA97_0 == THIS_CONSTRUCTOR_CALL or (IDENT <= LA97_0 <= STRING_LITERAL)) :
                        alt97 = 1
                    if alt97 == 1:
                        # JavaTreeParser.g:0:0: primaryExpression
                        pass 
                        self._state.following.append(self.FOLLOW_primaryExpression_in_explicitConstructorCall5477)
                        self.primaryExpression()

                        self._state.following.pop()



                    # JavaTreeParser.g:642:53: ( genericTypeArgumentList )?
                    alt98 = 2
                    LA98_0 = self.input.LA(1)

                    if (LA98_0 == GENERIC_TYPE_ARG_LIST) :
                        alt98 = 1
                    if alt98 == 1:
                        # JavaTreeParser.g:0:0: genericTypeArgumentList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeArgumentList_in_explicitConstructorCall5480)
                        self.genericTypeArgumentList()

                        self._state.following.pop()



                    self._state.following.append(self.FOLLOW_arguments_in_explicitConstructorCall5483)
                    self.arguments()

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 64, explicitConstructorCall_StartIndex, success)

            pass

        return value

    # $ANTLR end "explicitConstructorCall"


    # $ANTLR start "arrayTypeDeclarator"
    # JavaTreeParser.g:645:1: arrayTypeDeclarator : ^( ARRAY_DECLARATOR ( arrayTypeDeclarator | qualifiedIdentifier | primitiveType ) ) ;
    def arrayTypeDeclarator(self, ):

        arrayTypeDeclarator_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 65):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:646:5: ( ^( ARRAY_DECLARATOR ( arrayTypeDeclarator | qualifiedIdentifier | primitiveType ) ) )
                # JavaTreeParser.g:646:9: ^( ARRAY_DECLARATOR ( arrayTypeDeclarator | qualifiedIdentifier | primitiveType ) )
                pass 
                self.match(self.input, ARRAY_DECLARATOR, self.FOLLOW_ARRAY_DECLARATOR_in_arrayTypeDeclarator5504)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:646:28: ( arrayTypeDeclarator | qualifiedIdentifier | primitiveType )
                alt100 = 3
                LA100 = self.input.LA(1)
                if LA100 == ARRAY_DECLARATOR:
                    alt100 = 1
                elif LA100 == DOT or LA100 == IDENT:
                    alt100 = 2
                elif LA100 == BOOLEAN or LA100 == BYTE or LA100 == CHAR or LA100 == DOUBLE or LA100 == FLOAT or LA100 == INT or LA100 == LONG or LA100 == SHORT:
                    alt100 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 100, 0, self.input)

                    raise nvae

                if alt100 == 1:
                    # JavaTreeParser.g:646:29: arrayTypeDeclarator
                    pass 
                    self._state.following.append(self.FOLLOW_arrayTypeDeclarator_in_arrayTypeDeclarator5507)
                    self.arrayTypeDeclarator()

                    self._state.following.pop()


                elif alt100 == 2:
                    # JavaTreeParser.g:646:51: qualifiedIdentifier
                    pass 
                    self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_arrayTypeDeclarator5511)
                    self.qualifiedIdentifier()

                    self._state.following.pop()


                elif alt100 == 3:
                    # JavaTreeParser.g:646:73: primitiveType
                    pass 
                    self._state.following.append(self.FOLLOW_primitiveType_in_arrayTypeDeclarator5515)
                    self.primitiveType()

                    self._state.following.pop()




                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 65, arrayTypeDeclarator_StartIndex, success)

            pass

        return 

    # $ANTLR end "arrayTypeDeclarator"


    # $ANTLR start "newExpression"
    # JavaTreeParser.g:649:1: newExpression returns [value] : ( ^( STATIC_ARRAY_CREATOR (tp0= primitiveType ac0= newArrayConstruction | (gt1= genericTypeArgumentList )? tp1= qualifiedTypeIdent ac1= newArrayConstruction ) ) | ^( CLASS_CONSTRUCTOR_CALL ( genericTypeArgumentList )? q1= qualifiedTypeIdent a1= arguments ( classTopLevelScope )? ) );
    def newExpression(self, ):

        value = None
        newExpression_StartIndex = self.input.index()
        tp0 = None

        ac0 = None

        gt1 = None

        tp1 = None

        ac1 = None

        q1 = None

        a1 = None


        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 66):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:650:5: ( ^( STATIC_ARRAY_CREATOR (tp0= primitiveType ac0= newArrayConstruction | (gt1= genericTypeArgumentList )? tp1= qualifiedTypeIdent ac1= newArrayConstruction ) ) | ^( CLASS_CONSTRUCTOR_CALL ( genericTypeArgumentList )? q1= qualifiedTypeIdent a1= arguments ( classTopLevelScope )? ) )
                alt105 = 2
                LA105_0 = self.input.LA(1)

                if (LA105_0 == STATIC_ARRAY_CREATOR) :
                    alt105 = 1
                elif (LA105_0 == CLASS_CONSTRUCTOR_CALL) :
                    alt105 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 105, 0, self.input)

                    raise nvae

                if alt105 == 1:
                    # JavaTreeParser.g:650:9: ^( STATIC_ARRAY_CREATOR (tp0= primitiveType ac0= newArrayConstruction | (gt1= genericTypeArgumentList )? tp1= qualifiedTypeIdent ac1= newArrayConstruction ) )
                    pass 
                    self.match(self.input, STATIC_ARRAY_CREATOR, self.FOLLOW_STATIC_ARRAY_CREATOR_in_newExpression5541)

                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:651:11: (tp0= primitiveType ac0= newArrayConstruction | (gt1= genericTypeArgumentList )? tp1= qualifiedTypeIdent ac1= newArrayConstruction )
                    alt102 = 2
                    LA102_0 = self.input.LA(1)

                    if (LA102_0 == BOOLEAN or LA102_0 == BYTE or LA102_0 == CHAR or LA102_0 == DOUBLE or LA102_0 == FLOAT or (INT <= LA102_0 <= LONG) or LA102_0 == SHORT) :
                        alt102 = 1
                    elif (LA102_0 == GENERIC_TYPE_ARG_LIST or LA102_0 == QUALIFIED_TYPE_IDENT) :
                        alt102 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 102, 0, self.input)

                        raise nvae

                    if alt102 == 1:
                        # JavaTreeParser.g:651:13: tp0= primitiveType ac0= newArrayConstruction
                        pass 
                        self._state.following.append(self.FOLLOW_primitiveType_in_newExpression5557)
                        tp0 = self.primitiveType()

                        self._state.following.pop()
                        self._state.following.append(self.FOLLOW_newArrayConstruction_in_newExpression5561)
                        ac0 = self.newArrayConstruction()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            value = self.makeArrayCreator(((tp0 is not None) and [self.input.getTokenStream().toString(
                                self.input.getTreeAdaptor().getTokenStartIndex(tp0.start),
                                self.input.getTreeAdaptor().getTokenStopIndex(tp0.start)
                                )] or [None])[0], ac0) 



                    elif alt102 == 2:
                        # JavaTreeParser.g:653:13: (gt1= genericTypeArgumentList )? tp1= qualifiedTypeIdent ac1= newArrayConstruction
                        pass 
                        # JavaTreeParser.g:653:16: (gt1= genericTypeArgumentList )?
                        alt101 = 2
                        LA101_0 = self.input.LA(1)

                        if (LA101_0 == GENERIC_TYPE_ARG_LIST) :
                            alt101 = 1
                        if alt101 == 1:
                            # JavaTreeParser.g:0:0: gt1= genericTypeArgumentList
                            pass 
                            self._state.following.append(self.FOLLOW_genericTypeArgumentList_in_newExpression5591)
                            gt1 = self.genericTypeArgumentList()

                            self._state.following.pop()



                        self._state.following.append(self.FOLLOW_qualifiedTypeIdent_in_newExpression5596)
                        tp1 = self.qualifiedTypeIdent()

                        self._state.following.pop()
                        self._state.following.append(self.FOLLOW_newArrayConstruction_in_newExpression5600)
                        ac1 = self.newArrayConstruction()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            value = self.makeArrayCreator(tp1, ac1, gt1) 





                    self.match(self.input, UP, None)


                elif alt105 == 2:
                    # JavaTreeParser.g:657:9: ^( CLASS_CONSTRUCTOR_CALL ( genericTypeArgumentList )? q1= qualifiedTypeIdent a1= arguments ( classTopLevelScope )? )
                    pass 
                    self.match(self.input, CLASS_CONSTRUCTOR_CALL, self.FOLLOW_CLASS_CONSTRUCTOR_CALL_in_newExpression5647)

                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:657:34: ( genericTypeArgumentList )?
                    alt103 = 2
                    LA103_0 = self.input.LA(1)

                    if (LA103_0 == GENERIC_TYPE_ARG_LIST) :
                        alt103 = 1
                    if alt103 == 1:
                        # JavaTreeParser.g:0:0: genericTypeArgumentList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeArgumentList_in_newExpression5649)
                        self.genericTypeArgumentList()

                        self._state.following.pop()



                    self._state.following.append(self.FOLLOW_qualifiedTypeIdent_in_newExpression5654)
                    q1 = self.qualifiedTypeIdent()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_arguments_in_newExpression5668)
                    a1 = self.arguments()

                    self._state.following.pop()
                    # JavaTreeParser.g:658:24: ( classTopLevelScope )?
                    alt104 = 2
                    LA104_0 = self.input.LA(1)

                    if (LA104_0 == CLASS_TOP_LEVEL_SCOPE) :
                        alt104 = 1
                    if alt104 == 1:
                        # JavaTreeParser.g:0:0: classTopLevelScope
                        pass 
                        self._state.following.append(self.FOLLOW_classTopLevelScope_in_newExpression5670)
                        self.classTopLevelScope()

                        self._state.following.pop()



                    if self._state.backtracking == 0:
                        value = ex(q1, a1, "${left}(${right})") 


                    self.match(self.input, UP, None)



                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 66, newExpression_StartIndex, success)

            pass

        return value

    # $ANTLR end "newExpression"


    # $ANTLR start "innerNewExpression"
    # JavaTreeParser.g:665:1: innerNewExpression returns [value] : ^( CLASS_CONSTRUCTOR_CALL ( genericTypeArgumentList )? IDENT arguments ( classTopLevelScope )? ) ;
    def innerNewExpression(self, ):

        value = None
        innerNewExpression_StartIndex = self.input.index()
        value = None 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 67):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:667:5: ( ^( CLASS_CONSTRUCTOR_CALL ( genericTypeArgumentList )? IDENT arguments ( classTopLevelScope )? ) )
                # JavaTreeParser.g:667:9: ^( CLASS_CONSTRUCTOR_CALL ( genericTypeArgumentList )? IDENT arguments ( classTopLevelScope )? )
                pass 
                self.match(self.input, CLASS_CONSTRUCTOR_CALL, self.FOLLOW_CLASS_CONSTRUCTOR_CALL_in_innerNewExpression5728)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:667:34: ( genericTypeArgumentList )?
                alt106 = 2
                LA106_0 = self.input.LA(1)

                if (LA106_0 == GENERIC_TYPE_ARG_LIST) :
                    alt106 = 1
                if alt106 == 1:
                    # JavaTreeParser.g:0:0: genericTypeArgumentList
                    pass 
                    self._state.following.append(self.FOLLOW_genericTypeArgumentList_in_innerNewExpression5730)
                    self.genericTypeArgumentList()

                    self._state.following.pop()



                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_innerNewExpression5733)
                self._state.following.append(self.FOLLOW_arguments_in_innerNewExpression5735)
                self.arguments()

                self._state.following.pop()
                # JavaTreeParser.g:667:75: ( classTopLevelScope )?
                alt107 = 2
                LA107_0 = self.input.LA(1)

                if (LA107_0 == CLASS_TOP_LEVEL_SCOPE) :
                    alt107 = 1
                if alt107 == 1:
                    # JavaTreeParser.g:0:0: classTopLevelScope
                    pass 
                    self._state.following.append(self.FOLLOW_classTopLevelScope_in_innerNewExpression5737)
                    self.classTopLevelScope()

                    self._state.following.pop()




                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 67, innerNewExpression_StartIndex, success)

            pass

        return value

    # $ANTLR end "innerNewExpression"


    # $ANTLR start "newArrayConstruction"
    # JavaTreeParser.g:670:1: newArrayConstruction returns [value] : ( arrayDeclaratorList arrayInitializer | ( expression )+ ( arrayDeclaratorList )? );
    def newArrayConstruction(self, ):

        value = None
        newArrayConstruction_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 68):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:671:5: ( arrayDeclaratorList arrayInitializer | ( expression )+ ( arrayDeclaratorList )? )
                alt110 = 2
                LA110_0 = self.input.LA(1)

                if (LA110_0 == ARRAY_DECLARATOR_LIST) :
                    alt110 = 1
                elif (LA110_0 == EXPR) :
                    alt110 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 110, 0, self.input)

                    raise nvae

                if alt110 == 1:
                    # JavaTreeParser.g:671:9: arrayDeclaratorList arrayInitializer
                    pass 
                    self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_newArrayConstruction5762)
                    self.arrayDeclaratorList()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_arrayInitializer_in_newArrayConstruction5764)
                    self.arrayInitializer()

                    self._state.following.pop()


                elif alt110 == 2:
                    # JavaTreeParser.g:672:9: ( expression )+ ( arrayDeclaratorList )?
                    pass 
                    # JavaTreeParser.g:672:9: ( expression )+
                    cnt108 = 0
                    while True: #loop108
                        alt108 = 2
                        LA108_0 = self.input.LA(1)

                        if (LA108_0 == EXPR) :
                            alt108 = 1


                        if alt108 == 1:
                            # JavaTreeParser.g:0:0: expression
                            pass 
                            self._state.following.append(self.FOLLOW_expression_in_newArrayConstruction5774)
                            self.expression()

                            self._state.following.pop()


                        else:
                            if cnt108 >= 1:
                                break #loop108

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(108, self.input)
                            raise eee

                        cnt108 += 1


                    # JavaTreeParser.g:672:21: ( arrayDeclaratorList )?
                    alt109 = 2
                    LA109_0 = self.input.LA(1)

                    if (LA109_0 == ARRAY_DECLARATOR_LIST) :
                        alt109 = 1
                    if alt109 == 1:
                        # JavaTreeParser.g:0:0: arrayDeclaratorList
                        pass 
                        self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_newArrayConstruction5777)
                        self.arrayDeclaratorList()

                        self._state.following.pop()






                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 68, newArrayConstruction_StartIndex, success)

            pass

        return value

    # $ANTLR end "newArrayConstruction"


    # $ANTLR start "arguments"
    # JavaTreeParser.g:676:1: arguments returns [values] : ^( ARGUMENT_LIST (ex0= expression )* ) ;
    def arguments(self, ):

        values = None
        arguments_StartIndex = self.input.index()
        ex0 = None


        values, format = "", "${right}" 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 69):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return values

                # JavaTreeParser.g:678:5: ( ^( ARGUMENT_LIST (ex0= expression )* ) )
                # JavaTreeParser.g:678:9: ^( ARGUMENT_LIST (ex0= expression )* )
                pass 
                self.match(self.input, ARGUMENT_LIST, self.FOLLOW_ARGUMENT_LIST_in_arguments5812)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:678:25: (ex0= expression )*
                    while True: #loop111
                        alt111 = 2
                        LA111_0 = self.input.LA(1)

                        if (LA111_0 == EXPR) :
                            alt111 = 1


                        if alt111 == 1:
                            # JavaTreeParser.g:678:26: ex0= expression
                            pass 
                            self._state.following.append(self.FOLLOW_expression_in_arguments5817)
                            ex0 = self.expression()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                values, format = ex(values, ex0, format), "${left}, ${right}" 



                        else:
                            break #loop111



                    self.match(self.input, UP, None)





                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 69, arguments_StartIndex, success)

            pass

        return values

    # $ANTLR end "arguments"

    class literal_return(TreeRuleReturnScope):
        def __init__(self):
            TreeRuleReturnScope.__init__(self)

            self.value = None




    # $ANTLR start "literal"
    # JavaTreeParser.g:684:1: literal returns [value] : ( HEX_LITERAL | OCTAL_LITERAL | DECIMAL_LITERAL | FLOATING_POINT_LITERAL | CHARACTER_LITERAL | STRING_LITERAL | TRUE | FALSE | NULL );
    def literal(self, ):

        retval = self.literal_return()
        retval.start = self.input.LT(1)
        literal_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 70):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # JavaTreeParser.g:685:5: ( HEX_LITERAL | OCTAL_LITERAL | DECIMAL_LITERAL | FLOATING_POINT_LITERAL | CHARACTER_LITERAL | STRING_LITERAL | TRUE | FALSE | NULL )
                alt112 = 9
                LA112 = self.input.LA(1)
                if LA112 == HEX_LITERAL:
                    alt112 = 1
                elif LA112 == OCTAL_LITERAL:
                    alt112 = 2
                elif LA112 == DECIMAL_LITERAL:
                    alt112 = 3
                elif LA112 == FLOATING_POINT_LITERAL:
                    alt112 = 4
                elif LA112 == CHARACTER_LITERAL:
                    alt112 = 5
                elif LA112 == STRING_LITERAL:
                    alt112 = 6
                elif LA112 == TRUE:
                    alt112 = 7
                elif LA112 == FALSE:
                    alt112 = 8
                elif LA112 == NULL:
                    alt112 = 9
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 112, 0, self.input)

                    raise nvae

                if alt112 == 1:
                    # JavaTreeParser.g:685:9: HEX_LITERAL
                    pass 
                    self.match(self.input, HEX_LITERAL, self.FOLLOW_HEX_LITERAL_in_literal5865)
                    if self._state.backtracking == 0:
                        retval.value = self.input.toString(retval.start, self.input.LT(-1)) 



                elif alt112 == 2:
                    # JavaTreeParser.g:686:9: OCTAL_LITERAL
                    pass 
                    self.match(self.input, OCTAL_LITERAL, self.FOLLOW_OCTAL_LITERAL_in_literal5877)
                    if self._state.backtracking == 0:
                        retval.value = self.input.toString(retval.start, self.input.LT(-1)) 



                elif alt112 == 3:
                    # JavaTreeParser.g:687:9: DECIMAL_LITERAL
                    pass 
                    self.match(self.input, DECIMAL_LITERAL, self.FOLLOW_DECIMAL_LITERAL_in_literal5889)
                    if self._state.backtracking == 0:
                        retval.value = formatFloatLiteral(self.input.toString(retval.start, self.input.LT(-1))) 



                elif alt112 == 4:
                    # JavaTreeParser.g:688:9: FLOATING_POINT_LITERAL
                    pass 
                    self.match(self.input, FLOATING_POINT_LITERAL, self.FOLLOW_FLOATING_POINT_LITERAL_in_literal5901)
                    if self._state.backtracking == 0:
                        retval.value = formatFloatLiteral(self.input.toString(retval.start, self.input.LT(-1))) 



                elif alt112 == 5:
                    # JavaTreeParser.g:689:9: CHARACTER_LITERAL
                    pass 
                    self.match(self.input, CHARACTER_LITERAL, self.FOLLOW_CHARACTER_LITERAL_in_literal5913)
                    if self._state.backtracking == 0:
                        retval.value = self.input.toString(retval.start, self.input.LT(-1)) 



                elif alt112 == 6:
                    # JavaTreeParser.g:690:9: STRING_LITERAL
                    pass 
                    self.match(self.input, STRING_LITERAL, self.FOLLOW_STRING_LITERAL_in_literal5925)
                    if self._state.backtracking == 0:
                        retval.value = self.input.toString(retval.start, self.input.LT(-1)) 



                elif alt112 == 7:
                    # JavaTreeParser.g:691:9: TRUE
                    pass 
                    self.match(self.input, TRUE, self.FOLLOW_TRUE_in_literal5937)
                    if self._state.backtracking == 0:
                        retval.value = 'True' 



                elif alt112 == 8:
                    # JavaTreeParser.g:692:9: FALSE
                    pass 
                    self.match(self.input, FALSE, self.FOLLOW_FALSE_in_literal5949)
                    if self._state.backtracking == 0:
                        retval.value = 'False' 



                elif alt112 == 9:
                    # JavaTreeParser.g:693:9: NULL
                    pass 
                    self.match(self.input, NULL, self.FOLLOW_NULL_in_literal5961)
                    if self._state.backtracking == 0:
                        retval.value = 'None' 




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 70, literal_StartIndex, success)

            pass

        return retval

    # $ANTLR end "literal"

    # $ANTLR start "synpred125_JavaTreeParser"
    def synpred125_JavaTreeParser_fragment(self, ):
        # JavaTreeParser.g:504:35: ( switchCaseLabel )
        # JavaTreeParser.g:504:35: switchCaseLabel
        pass 
        self._state.following.append(self.FOLLOW_switchCaseLabel_in_synpred125_JavaTreeParser3922)
        self.switchCaseLabel()

        self._state.following.pop()


    # $ANTLR end "synpred125_JavaTreeParser"



    # $ANTLR start "synpred132_JavaTreeParser"
    def synpred132_JavaTreeParser_fragment(self, ):
        # JavaTreeParser.g:516:48: ( ( expression )* )
        # JavaTreeParser.g:516:48: ( expression )*
        pass 
        # JavaTreeParser.g:516:48: ( expression )*
        while True: #loop143
            alt143 = 2
            LA143_0 = self.input.LA(1)

            if (LA143_0 == EXPR) :
                alt143 = 1


            if alt143 == 1:
                # JavaTreeParser.g:0:0: expression
                pass 
                self._state.following.append(self.FOLLOW_expression_in_synpred132_JavaTreeParser4007)
                self.expression()

                self._state.following.pop()


            else:
                break #loop143




    # $ANTLR end "synpred132_JavaTreeParser"




    # Delegated rules

    def synpred132_JavaTreeParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred132_JavaTreeParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred125_JavaTreeParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred125_JavaTreeParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



 

    FOLLOW_JAVA_SOURCE_in_javaSource98 = frozenset([2])
    FOLLOW_annotationList_in_javaSource112 = frozenset([3, 7, 61, 67, 77, 78, 84])
    FOLLOW_packageDeclaration_in_javaSource126 = frozenset([3, 7, 61, 67, 77, 78])
    FOLLOW_importDeclaration_in_javaSource141 = frozenset([3, 7, 61, 67, 77, 78])
    FOLLOW_typeDeclaration_in_javaSource156 = frozenset([3, 7, 61, 67, 77])
    FOLLOW_PACKAGE_in_packageDeclaration188 = frozenset([2])
    FOLLOW_qualifiedIdentifier_in_packageDeclaration192 = frozenset([3])
    FOLLOW_IMPORT_in_importDeclaration216 = frozenset([2])
    FOLLOW_STATIC_in_importDeclaration218 = frozenset([15, 164])
    FOLLOW_qualifiedIdentifier_in_importDeclaration221 = frozenset([3, 16])
    FOLLOW_DOTSTAR_in_importDeclaration223 = frozenset([3])
    FOLLOW_CLASS_in_typeDeclaration265 = frozenset([2])
    FOLLOW_modifierList_in_typeDeclaration279 = frozenset([164])
    FOLLOW_IDENT_in_typeDeclaration295 = frozenset([123, 128, 138, 140])
    FOLLOW_genericTypeParameterList_in_typeDeclaration309 = frozenset([123, 128, 138, 140])
    FOLLOW_extendsClause_in_typeDeclaration325 = frozenset([123, 128, 138, 140])
    FOLLOW_implementsClause_in_typeDeclaration344 = frozenset([123, 128, 138, 140])
    FOLLOW_classTopLevelScope_in_typeDeclaration360 = frozenset([3])
    FOLLOW_INTERFACE_in_typeDeclaration382 = frozenset([2])
    FOLLOW_modifierList_in_typeDeclaration396 = frozenset([164])
    FOLLOW_IDENT_in_typeDeclaration412 = frozenset([128, 138, 139])
    FOLLOW_genericTypeParameterList_in_typeDeclaration426 = frozenset([128, 138, 139])
    FOLLOW_extendsClause_in_typeDeclaration442 = frozenset([128, 138, 139])
    FOLLOW_interfaceTopLevelScope_in_typeDeclaration458 = frozenset([3])
    FOLLOW_ENUM_in_typeDeclaration480 = frozenset([2])
    FOLLOW_modifierList_in_typeDeclaration492 = frozenset([164])
    FOLLOW_IDENT_in_typeDeclaration504 = frozenset([125, 140])
    FOLLOW_implementsClause_in_typeDeclaration516 = frozenset([125, 140])
    FOLLOW_enumTopLevelScope_in_typeDeclaration529 = frozenset([3])
    FOLLOW_AT_in_typeDeclaration551 = frozenset([2])
    FOLLOW_modifierList_in_typeDeclaration563 = frozenset([164])
    FOLLOW_IDENT_in_typeDeclaration575 = frozenset([111])
    FOLLOW_annotationTopLevelScope_in_typeDeclaration587 = frozenset([3])
    FOLLOW_EXTENDS_CLAUSE_in_extendsClause631 = frozenset([2])
    FOLLOW_type_in_extendsClause636 = frozenset([3, 157])
    FOLLOW_IMPLEMENTS_CLAUSE_in_implementsClause675 = frozenset([2])
    FOLLOW_type_in_implementsClause680 = frozenset([3, 157])
    FOLLOW_GENERIC_TYPE_PARAM_LIST_in_genericTypeParameterList705 = frozenset([2])
    FOLLOW_genericTypeParameter_in_genericTypeParameterList707 = frozenset([3, 164])
    FOLLOW_IDENT_in_genericTypeParameter729 = frozenset([2])
    FOLLOW_bound_in_genericTypeParameter731 = frozenset([3])
    FOLLOW_EXTENDS_BOUND_LIST_in_bound753 = frozenset([2])
    FOLLOW_type_in_bound755 = frozenset([3, 157])
    FOLLOW_ENUM_TOP_LEVEL_SCOPE_in_enumTopLevelScope777 = frozenset([2])
    FOLLOW_enumConstant_in_enumTopLevelScope779 = frozenset([3, 123, 128, 138, 140, 164])
    FOLLOW_classTopLevelScope_in_enumTopLevelScope782 = frozenset([3])
    FOLLOW_IDENT_in_enumConstant804 = frozenset([2])
    FOLLOW_annotationList_in_enumConstant806 = frozenset([3, 112, 123, 128, 138, 140])
    FOLLOW_arguments_in_enumConstant808 = frozenset([3, 123, 128, 138, 140])
    FOLLOW_classTopLevelScope_in_enumConstant811 = frozenset([3])
    FOLLOW_CLASS_TOP_LEVEL_SCOPE_in_classTopLevelScope834 = frozenset([2])
    FOLLOW_classScopeDeclarations_in_classTopLevelScope836 = frozenset([3, 7, 61, 67, 77, 121, 122, 124, 136, 160, 163])
    FOLLOW_CLASS_INSTANCE_INITIALIZER_in_classScopeDeclarations878 = frozenset([2])
    FOLLOW_block_in_classScopeDeclarations880 = frozenset([3])
    FOLLOW_CLASS_STATIC_INITIALIZER_in_classScopeDeclarations893 = frozenset([2])
    FOLLOW_block_in_classScopeDeclarations895 = frozenset([3])
    FOLLOW_FUNCTION_METHOD_DECL_in_classScopeDeclarations908 = frozenset([2])
    FOLLOW_modifierList_in_classScopeDeclarations934 = frozenset([3, 138, 157])
    FOLLOW_genericTypeParameterList_in_classScopeDeclarations948 = frozenset([3, 157])
    FOLLOW_type_in_classScopeDeclarations963 = frozenset([164])
    FOLLOW_IDENT_in_classScopeDeclarations979 = frozenset([133])
    FOLLOW_formalParameterList_in_classScopeDeclarations995 = frozenset([3, 114, 117, 156])
    FOLLOW_arrayDeclaratorList_in_classScopeDeclarations1009 = frozenset([3, 117, 156])
    FOLLOW_throwsClause_in_classScopeDeclarations1022 = frozenset([3, 117])
    FOLLOW_block_in_classScopeDeclarations1035 = frozenset([3])
    FOLLOW_VOID_METHOD_DECL_in_classScopeDeclarations1070 = frozenset([2])
    FOLLOW_modifierList_in_classScopeDeclarations1096 = frozenset([138, 164])
    FOLLOW_genericTypeParameterList_in_classScopeDeclarations1110 = frozenset([164])
    FOLLOW_IDENT_in_classScopeDeclarations1125 = frozenset([133])
    FOLLOW_formalParameterList_in_classScopeDeclarations1141 = frozenset([3, 117, 156])
    FOLLOW_throwsClause_in_classScopeDeclarations1155 = frozenset([3, 117])
    FOLLOW_block_in_classScopeDeclarations1168 = frozenset([3])
    FOLLOW_VAR_DECLARATION_in_classScopeDeclarations1204 = frozenset([2])
    FOLLOW_modifierList_in_classScopeDeclarations1218 = frozenset([3, 157])
    FOLLOW_type_in_classScopeDeclarations1232 = frozenset([162])
    FOLLOW_variableDeclaratorList_in_classScopeDeclarations1246 = frozenset([3])
    FOLLOW_CONSTRUCTOR_DECL_in_classScopeDeclarations1280 = frozenset([2])
    FOLLOW_modifierList_in_classScopeDeclarations1306 = frozenset([133, 138])
    FOLLOW_genericTypeParameterList_in_classScopeDeclarations1320 = frozenset([133])
    FOLLOW_formalParameterList_in_classScopeDeclarations1335 = frozenset([117, 156])
    FOLLOW_throwsClause_in_classScopeDeclarations1349 = frozenset([117])
    FOLLOW_block_in_classScopeDeclarations1362 = frozenset([3])
    FOLLOW_typeDeclaration_in_classScopeDeclarations1395 = frozenset([1])
    FOLLOW_INTERFACE_TOP_LEVEL_SCOPE_in_interfaceTopLevelScope1416 = frozenset([2])
    FOLLOW_interfaceScopeDeclarations_in_interfaceTopLevelScope1418 = frozenset([3, 7, 61, 67, 77, 136, 160, 163])
    FOLLOW_FUNCTION_METHOD_DECL_in_interfaceScopeDeclarations1440 = frozenset([2])
    FOLLOW_modifierList_in_interfaceScopeDeclarations1442 = frozenset([3, 138, 157])
    FOLLOW_genericTypeParameterList_in_interfaceScopeDeclarations1444 = frozenset([3, 157])
    FOLLOW_type_in_interfaceScopeDeclarations1447 = frozenset([164])
    FOLLOW_IDENT_in_interfaceScopeDeclarations1449 = frozenset([133])
    FOLLOW_formalParameterList_in_interfaceScopeDeclarations1451 = frozenset([3, 114, 156])
    FOLLOW_arrayDeclaratorList_in_interfaceScopeDeclarations1453 = frozenset([3, 156])
    FOLLOW_throwsClause_in_interfaceScopeDeclarations1456 = frozenset([3])
    FOLLOW_VOID_METHOD_DECL_in_interfaceScopeDeclarations1469 = frozenset([2])
    FOLLOW_modifierList_in_interfaceScopeDeclarations1471 = frozenset([138, 164])
    FOLLOW_genericTypeParameterList_in_interfaceScopeDeclarations1473 = frozenset([164])
    FOLLOW_IDENT_in_interfaceScopeDeclarations1476 = frozenset([133])
    FOLLOW_formalParameterList_in_interfaceScopeDeclarations1478 = frozenset([3, 156])
    FOLLOW_throwsClause_in_interfaceScopeDeclarations1480 = frozenset([3])
    FOLLOW_VAR_DECLARATION_in_interfaceScopeDeclarations1571 = frozenset([2])
    FOLLOW_modifierList_in_interfaceScopeDeclarations1585 = frozenset([3, 157])
    FOLLOW_type_in_interfaceScopeDeclarations1599 = frozenset([162])
    FOLLOW_variableDeclaratorList_in_interfaceScopeDeclarations1613 = frozenset([3])
    FOLLOW_typeDeclaration_in_interfaceScopeDeclarations1646 = frozenset([1])
    FOLLOW_VAR_DECLARATOR_LIST_in_variableDeclaratorList1679 = frozenset([2])
    FOLLOW_variableDeclarator_in_variableDeclaratorList1684 = frozenset([3, 161])
    FOLLOW_VAR_DECLARATOR_in_variableDeclarator1723 = frozenset([2])
    FOLLOW_variableDeclaratorId_in_variableDeclarator1737 = frozenset([3, 116, 126])
    FOLLOW_variableInitializer_in_variableDeclarator1754 = frozenset([3])
    FOLLOW_IDENT_in_variableDeclaratorId1802 = frozenset([2])
    FOLLOW_arrayDeclaratorList_in_variableDeclaratorId1817 = frozenset([3])
    FOLLOW_arrayInitializer_in_variableInitializer1865 = frozenset([1])
    FOLLOW_expression_in_variableInitializer1879 = frozenset([1])
    FOLLOW_LBRACK_in_arrayDeclarator1906 = frozenset([41])
    FOLLOW_RBRACK_in_arrayDeclarator1908 = frozenset([1])
    FOLLOW_ARRAY_DECLARATOR_LIST_in_arrayDeclaratorList1928 = frozenset([2])
    FOLLOW_ARRAY_DECLARATOR_in_arrayDeclaratorList1930 = frozenset([3, 113])
    FOLLOW_ARRAY_INITIALIZER_in_arrayInitializer1965 = frozenset([2])
    FOLLOW_variableInitializer_in_arrayInitializer1967 = frozenset([3, 116, 126])
    FOLLOW_THROWS_CLAUSE_in_throwsClause1989 = frozenset([2])
    FOLLOW_qualifiedIdentifier_in_throwsClause1991 = frozenset([3, 15, 164])
    FOLLOW_MODIFIER_LIST_in_modifierList2026 = frozenset([2])
    FOLLOW_modifier_in_modifierList2031 = frozenset([3, 7, 53, 70, 81, 85, 86, 87, 90, 91, 94, 98, 102])
    FOLLOW_PUBLIC_in_modifier2055 = frozenset([1])
    FOLLOW_PROTECTED_in_modifier2065 = frozenset([1])
    FOLLOW_PRIVATE_in_modifier2075 = frozenset([1])
    FOLLOW_STATIC_in_modifier2085 = frozenset([1])
    FOLLOW_ABSTRACT_in_modifier2095 = frozenset([1])
    FOLLOW_NATIVE_in_modifier2105 = frozenset([1])
    FOLLOW_SYNCHRONIZED_in_modifier2115 = frozenset([1])
    FOLLOW_TRANSIENT_in_modifier2125 = frozenset([1])
    FOLLOW_VOLATILE_in_modifier2135 = frozenset([1])
    FOLLOW_STRICTFP_in_modifier2145 = frozenset([1])
    FOLLOW_localModifier_in_modifier2155 = frozenset([1])
    FOLLOW_LOCAL_MODIFIER_LIST_in_localModifierList2188 = frozenset([2])
    FOLLOW_localModifier_in_localModifierList2193 = frozenset([3, 7, 53, 70, 81, 85, 86, 87, 90, 91, 94, 98, 102])
    FOLLOW_FINAL_in_localModifier2221 = frozenset([1])
    FOLLOW_annotation_in_localModifier2235 = frozenset([1])
    FOLLOW_TYPE_in_type2270 = frozenset([2])
    FOLLOW_primitiveType_in_type2285 = frozenset([3, 114])
    FOLLOW_qualifiedTypeIdent_in_type2304 = frozenset([3, 114])
    FOLLOW_arrayDeclaratorList_in_type2320 = frozenset([3])
    FOLLOW_QUALIFIED_TYPE_IDENT_in_qualifiedTypeIdent2381 = frozenset([2])
    FOLLOW_typeIdent_in_qualifiedTypeIdent2386 = frozenset([3, 164])
    FOLLOW_IDENT_in_typeIdent2417 = frozenset([2])
    FOLLOW_genericTypeArgumentList_in_typeIdent2419 = frozenset([3])
    FOLLOW_set_in_primitiveType0 = frozenset([1])
    FOLLOW_GENERIC_TYPE_ARG_LIST_in_genericTypeArgumentList2546 = frozenset([2])
    FOLLOW_genericTypeArgument_in_genericTypeArgumentList2548 = frozenset([3, 40, 157])
    FOLLOW_type_in_genericTypeArgument2569 = frozenset([1])
    FOLLOW_QUESTION_in_genericTypeArgument2580 = frozenset([2])
    FOLLOW_genericWildcardBoundType_in_genericTypeArgument2582 = frozenset([3])
    FOLLOW_EXTENDS_in_genericWildcardBoundType2604 = frozenset([2])
    FOLLOW_type_in_genericWildcardBoundType2606 = frozenset([3])
    FOLLOW_SUPER_in_genericWildcardBoundType2618 = frozenset([2])
    FOLLOW_type_in_genericWildcardBoundType2620 = frozenset([3])
    FOLLOW_FORMAL_PARAM_LIST_in_formalParameterList2654 = frozenset([2])
    FOLLOW_formalParameterStandardDecl_in_formalParameterList2669 = frozenset([3, 134, 135])
    FOLLOW_formalParameterVarargDecl_in_formalParameterList2688 = frozenset([3])
    FOLLOW_FORMAL_PARAM_STD_DECL_in_formalParameterStandardDecl2728 = frozenset([2])
    FOLLOW_localModifierList_in_formalParameterStandardDecl2742 = frozenset([3, 157])
    FOLLOW_type_in_formalParameterStandardDecl2756 = frozenset([164])
    FOLLOW_variableDeclaratorId_in_formalParameterStandardDecl2770 = frozenset([3])
    FOLLOW_FORMAL_PARAM_VARARG_DECL_in_formalParameterVarargDecl2807 = frozenset([2])
    FOLLOW_localModifierList_in_formalParameterVarargDecl2821 = frozenset([3, 157])
    FOLLOW_type_in_formalParameterVarargDecl2835 = frozenset([164])
    FOLLOW_variableDeclaratorId_in_formalParameterVarargDecl2849 = frozenset([3])
    FOLLOW_IDENT_in_qualifiedIdentifier2885 = frozenset([1])
    FOLLOW_DOT_in_qualifiedIdentifier2898 = frozenset([2])
    FOLLOW_qualifiedIdentifier_in_qualifiedIdentifier2912 = frozenset([164])
    FOLLOW_IDENT_in_qualifiedIdentifier2924 = frozenset([3])
    FOLLOW_ANNOTATION_LIST_in_annotationList2969 = frozenset([2])
    FOLLOW_annotation_in_annotationList2971 = frozenset([3, 7, 53, 70, 81, 85, 86, 87, 90, 91, 94, 98, 102])
    FOLLOW_AT_in_annotation2997 = frozenset([2])
    FOLLOW_qualifiedIdentifier_in_annotation3011 = frozenset([3, 105])
    FOLLOW_annotationInit_in_annotation3025 = frozenset([3])
    FOLLOW_ANNOTATION_INIT_BLOCK_in_annotationInit3056 = frozenset([2])
    FOLLOW_annotationInitializers_in_annotationInit3058 = frozenset([3])
    FOLLOW_ANNOTATION_INIT_KEY_LIST_in_annotationInitializers3079 = frozenset([2])
    FOLLOW_annotationInitializer_in_annotationInitializers3081 = frozenset([3, 164])
    FOLLOW_ANNOTATION_INIT_DEFAULT_KEY_in_annotationInitializers3094 = frozenset([2])
    FOLLOW_annotationElementValue_in_annotationInitializers3096 = frozenset([3])
    FOLLOW_IDENT_in_annotationInitializer3117 = frozenset([2])
    FOLLOW_annotationElementValue_in_annotationInitializer3119 = frozenset([3])
    FOLLOW_ANNOTATION_INIT_ARRAY_ELEMENT_in_annotationElementValue3140 = frozenset([2])
    FOLLOW_annotationElementValue_in_annotationElementValue3142 = frozenset([3, 7, 53, 70, 81, 85, 86, 87, 90, 91, 94, 98, 102, 104, 116, 126])
    FOLLOW_annotation_in_annotationElementValue3154 = frozenset([1])
    FOLLOW_expression_in_annotationElementValue3164 = frozenset([1])
    FOLLOW_ANNOTATION_TOP_LEVEL_SCOPE_in_annotationTopLevelScope3184 = frozenset([2])
    FOLLOW_annotationScopeDeclarations_in_annotationTopLevelScope3186 = frozenset([3, 7, 61, 67, 77, 109, 160])
    FOLLOW_ANNOTATION_METHOD_DECL_in_annotationScopeDeclarations3208 = frozenset([2])
    FOLLOW_modifierList_in_annotationScopeDeclarations3210 = frozenset([3, 157])
    FOLLOW_type_in_annotationScopeDeclarations3212 = frozenset([164])
    FOLLOW_IDENT_in_annotationScopeDeclarations3214 = frozenset([3, 63])
    FOLLOW_annotationDefaultValue_in_annotationScopeDeclarations3216 = frozenset([3])
    FOLLOW_VAR_DECLARATION_in_annotationScopeDeclarations3229 = frozenset([2])
    FOLLOW_modifierList_in_annotationScopeDeclarations3231 = frozenset([3, 157])
    FOLLOW_type_in_annotationScopeDeclarations3233 = frozenset([162])
    FOLLOW_variableDeclaratorList_in_annotationScopeDeclarations3235 = frozenset([3])
    FOLLOW_typeDeclaration_in_annotationScopeDeclarations3246 = frozenset([1])
    FOLLOW_DEFAULT_in_annotationDefaultValue3266 = frozenset([2])
    FOLLOW_annotationElementValue_in_annotationDefaultValue3268 = frozenset([3])
    FOLLOW_BLOCK_SCOPE_in_block3291 = frozenset([2])
    FOLLOW_blockStatement_in_block3293 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_localVariableDeclaration_in_blockStatement3314 = frozenset([1])
    FOLLOW_typeDeclaration_in_blockStatement3324 = frozenset([1])
    FOLLOW_statement_in_blockStatement3336 = frozenset([1])
    FOLLOW_VAR_DECLARATION_in_localVariableDeclaration3358 = frozenset([2])
    FOLLOW_localModifierList_in_localVariableDeclaration3372 = frozenset([3, 157])
    FOLLOW_type_in_localVariableDeclaration3386 = frozenset([162])
    FOLLOW_variableDeclaratorList_in_localVariableDeclaration3400 = frozenset([3])
    FOLLOW_block_in_statement3457 = frozenset([1])
    FOLLOW_ASSERT_in_statement3468 = frozenset([2])
    FOLLOW_expression_in_statement3470 = frozenset([3, 116, 126])
    FOLLOW_expression_in_statement3472 = frozenset([3])
    FOLLOW_IF_in_statement3485 = frozenset([2])
    FOLLOW_parenthesizedExpression_in_statement3487 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_statement_in_statement3489 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_statement_in_statement3491 = frozenset([3])
    FOLLOW_FOR_in_statement3504 = frozenset([2])
    FOLLOW_forInit_in_statement3506 = frozenset([129])
    FOLLOW_forCondition_in_statement3508 = frozenset([132])
    FOLLOW_forUpdater_in_statement3510 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_statement_in_statement3512 = frozenset([3])
    FOLLOW_FOR_EACH_in_statement3525 = frozenset([2])
    FOLLOW_localModifierList_in_statement3549 = frozenset([3, 157])
    FOLLOW_type_in_statement3561 = frozenset([164])
    FOLLOW_IDENT_in_statement3575 = frozenset([116, 126])
    FOLLOW_expression_in_statement3589 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_statement_in_statement3615 = frozenset([3])
    FOLLOW_WHILE_in_statement3650 = frozenset([2])
    FOLLOW_parenthesizedExpression_in_statement3652 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_statement_in_statement3654 = frozenset([3])
    FOLLOW_DO_in_statement3666 = frozenset([2])
    FOLLOW_statement_in_statement3668 = frozenset([146])
    FOLLOW_parenthesizedExpression_in_statement3670 = frozenset([3])
    FOLLOW_TRY_in_statement3682 = frozenset([2])
    FOLLOW_block_in_statement3684 = frozenset([3, 117, 119])
    FOLLOW_catches_in_statement3686 = frozenset([3, 117])
    FOLLOW_block_in_statement3689 = frozenset([3])
    FOLLOW_SWITCH_in_statement3704 = frozenset([2])
    FOLLOW_parenthesizedExpression_in_statement3706 = frozenset([154])
    FOLLOW_switchBlockLabels_in_statement3708 = frozenset([3])
    FOLLOW_SYNCHRONIZED_in_statement3720 = frozenset([2])
    FOLLOW_parenthesizedExpression_in_statement3722 = frozenset([117])
    FOLLOW_block_in_statement3724 = frozenset([3])
    FOLLOW_RETURN_in_statement3736 = frozenset([2])
    FOLLOW_expression_in_statement3741 = frozenset([3])
    FOLLOW_THROW_in_statement3777 = frozenset([2])
    FOLLOW_expression_in_statement3779 = frozenset([3])
    FOLLOW_BREAK_in_statement3791 = frozenset([2])
    FOLLOW_IDENT_in_statement3793 = frozenset([3])
    FOLLOW_CONTINUE_in_statement3806 = frozenset([2])
    FOLLOW_IDENT_in_statement3808 = frozenset([3])
    FOLLOW_LABELED_STATEMENT_in_statement3821 = frozenset([2])
    FOLLOW_IDENT_in_statement3823 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_statement_in_statement3825 = frozenset([3])
    FOLLOW_expression_in_statement3838 = frozenset([1])
    FOLLOW_SEMI_in_statement3850 = frozenset([1])
    FOLLOW_CATCH_CLAUSE_LIST_in_catches3871 = frozenset([2])
    FOLLOW_catchClause_in_catches3873 = frozenset([3, 59])
    FOLLOW_CATCH_in_catchClause3895 = frozenset([2])
    FOLLOW_formalParameterStandardDecl_in_catchClause3897 = frozenset([117])
    FOLLOW_block_in_catchClause3899 = frozenset([3])
    FOLLOW_SWITCH_BLOCK_LABEL_LIST_in_switchBlockLabels3920 = frozenset([2])
    FOLLOW_switchCaseLabel_in_switchBlockLabels3922 = frozenset([3, 58, 63])
    FOLLOW_switchDefaultLabel_in_switchBlockLabels3925 = frozenset([3, 58])
    FOLLOW_switchCaseLabel_in_switchBlockLabels3928 = frozenset([3, 58])
    FOLLOW_CASE_in_switchCaseLabel3950 = frozenset([2])
    FOLLOW_expression_in_switchCaseLabel3952 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_blockStatement_in_switchCaseLabel3954 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_DEFAULT_in_switchDefaultLabel3976 = frozenset([2])
    FOLLOW_blockStatement_in_switchDefaultLabel3978 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_FOR_INIT_in_forInit4000 = frozenset([2])
    FOLLOW_localVariableDeclaration_in_forInit4003 = frozenset([3])
    FOLLOW_expression_in_forInit4007 = frozenset([3, 116, 126])
    FOLLOW_FOR_CONDITION_in_forCondition4031 = frozenset([2])
    FOLLOW_expression_in_forCondition4033 = frozenset([3])
    FOLLOW_FOR_UPDATE_in_forUpdater4055 = frozenset([2])
    FOLLOW_expression_in_forUpdater4057 = frozenset([3, 116, 126])
    FOLLOW_PARENTESIZED_EXPR_in_parenthesizedExpression4085 = frozenset([2])
    FOLLOW_expression_in_parenthesizedExpression4089 = frozenset([3])
    FOLLOW_EXPR_in_expression4116 = frozenset([2])
    FOLLOW_expr_in_expression4120 = frozenset([3])
    FOLLOW_ASSIGN_in_expr4156 = frozenset([2])
    FOLLOW_expr_in_expr4160 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4164 = frozenset([3])
    FOLLOW_PLUS_ASSIGN_in_expr4186 = frozenset([2])
    FOLLOW_expr_in_expr4190 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4194 = frozenset([3])
    FOLLOW_MINUS_ASSIGN_in_expr4216 = frozenset([2])
    FOLLOW_expr_in_expr4218 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4220 = frozenset([3])
    FOLLOW_STAR_ASSIGN_in_expr4232 = frozenset([2])
    FOLLOW_expr_in_expr4234 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4236 = frozenset([3])
    FOLLOW_DIV_ASSIGN_in_expr4248 = frozenset([2])
    FOLLOW_expr_in_expr4250 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4252 = frozenset([3])
    FOLLOW_AND_ASSIGN_in_expr4264 = frozenset([2])
    FOLLOW_expr_in_expr4266 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4268 = frozenset([3])
    FOLLOW_OR_ASSIGN_in_expr4280 = frozenset([2])
    FOLLOW_expr_in_expr4282 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4284 = frozenset([3])
    FOLLOW_XOR_ASSIGN_in_expr4296 = frozenset([2])
    FOLLOW_expr_in_expr4298 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4300 = frozenset([3])
    FOLLOW_MOD_ASSIGN_in_expr4312 = frozenset([2])
    FOLLOW_expr_in_expr4314 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4316 = frozenset([3])
    FOLLOW_BIT_SHIFT_RIGHT_ASSIGN_in_expr4328 = frozenset([2])
    FOLLOW_expr_in_expr4330 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4332 = frozenset([3])
    FOLLOW_SHIFT_RIGHT_ASSIGN_in_expr4344 = frozenset([2])
    FOLLOW_expr_in_expr4346 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4348 = frozenset([3])
    FOLLOW_SHIFT_LEFT_ASSIGN_in_expr4360 = frozenset([2])
    FOLLOW_expr_in_expr4362 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4364 = frozenset([3])
    FOLLOW_QUESTION_in_expr4376 = frozenset([2])
    FOLLOW_expr_in_expr4380 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4384 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4388 = frozenset([3])
    FOLLOW_LOGICAL_OR_in_expr4412 = frozenset([2])
    FOLLOW_expr_in_expr4414 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4416 = frozenset([3])
    FOLLOW_LOGICAL_AND_in_expr4428 = frozenset([2])
    FOLLOW_expr_in_expr4430 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4432 = frozenset([3])
    FOLLOW_OR_in_expr4444 = frozenset([2])
    FOLLOW_expr_in_expr4446 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4448 = frozenset([3])
    FOLLOW_XOR_in_expr4460 = frozenset([2])
    FOLLOW_expr_in_expr4462 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4464 = frozenset([3])
    FOLLOW_AND_in_expr4476 = frozenset([2])
    FOLLOW_expr_in_expr4478 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4480 = frozenset([3])
    FOLLOW_EQUAL_in_expr4492 = frozenset([2])
    FOLLOW_expr_in_expr4496 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4500 = frozenset([3])
    FOLLOW_NOT_EQUAL_in_expr4524 = frozenset([2])
    FOLLOW_expr_in_expr4526 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4528 = frozenset([3])
    FOLLOW_INSTANCEOF_in_expr4540 = frozenset([2])
    FOLLOW_expr_in_expr4542 = frozenset([3, 157])
    FOLLOW_type_in_expr4544 = frozenset([3])
    FOLLOW_LESS_OR_EQUAL_in_expr4556 = frozenset([2])
    FOLLOW_expr_in_expr4558 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4560 = frozenset([3])
    FOLLOW_GREATER_OR_EQUAL_in_expr4572 = frozenset([2])
    FOLLOW_expr_in_expr4574 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4576 = frozenset([3])
    FOLLOW_BIT_SHIFT_RIGHT_in_expr4588 = frozenset([2])
    FOLLOW_expr_in_expr4590 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4592 = frozenset([3])
    FOLLOW_SHIFT_RIGHT_in_expr4604 = frozenset([2])
    FOLLOW_expr_in_expr4606 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4608 = frozenset([3])
    FOLLOW_GREATER_THAN_in_expr4620 = frozenset([2])
    FOLLOW_expr_in_expr4622 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4624 = frozenset([3])
    FOLLOW_SHIFT_LEFT_in_expr4636 = frozenset([2])
    FOLLOW_expr_in_expr4638 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4640 = frozenset([3])
    FOLLOW_LESS_THAN_in_expr4652 = frozenset([2])
    FOLLOW_expr_in_expr4654 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4656 = frozenset([3])
    FOLLOW_PLUS_in_expr4668 = frozenset([2])
    FOLLOW_expr_in_expr4672 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4676 = frozenset([3])
    FOLLOW_MINUS_in_expr4698 = frozenset([2])
    FOLLOW_expr_in_expr4700 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4702 = frozenset([3])
    FOLLOW_STAR_in_expr4714 = frozenset([2])
    FOLLOW_expr_in_expr4716 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4718 = frozenset([3])
    FOLLOW_DIV_in_expr4730 = frozenset([2])
    FOLLOW_expr_in_expr4732 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4734 = frozenset([3])
    FOLLOW_MOD_in_expr4746 = frozenset([2])
    FOLLOW_expr_in_expr4748 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4750 = frozenset([3])
    FOLLOW_UNARY_PLUS_in_expr4762 = frozenset([2])
    FOLLOW_expr_in_expr4764 = frozenset([3])
    FOLLOW_UNARY_MINUS_in_expr4776 = frozenset([2])
    FOLLOW_expr_in_expr4778 = frozenset([3])
    FOLLOW_PRE_INC_in_expr4790 = frozenset([2])
    FOLLOW_expr_in_expr4792 = frozenset([3])
    FOLLOW_PRE_DEC_in_expr4804 = frozenset([2])
    FOLLOW_expr_in_expr4806 = frozenset([3])
    FOLLOW_POST_INC_in_expr4818 = frozenset([2])
    FOLLOW_expr_in_expr4820 = frozenset([3])
    FOLLOW_POST_DEC_in_expr4832 = frozenset([2])
    FOLLOW_expr_in_expr4834 = frozenset([3])
    FOLLOW_NOT_in_expr4846 = frozenset([2])
    FOLLOW_expr_in_expr4848 = frozenset([3])
    FOLLOW_LOGICAL_NOT_in_expr4860 = frozenset([2])
    FOLLOW_expr_in_expr4862 = frozenset([3])
    FOLLOW_CAST_EXPR_in_expr4874 = frozenset([2])
    FOLLOW_type_in_expr4876 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr4878 = frozenset([3])
    FOLLOW_primaryExpression_in_expr4891 = frozenset([1])
    FOLLOW_DOT_in_primaryExpression4928 = frozenset([2])
    FOLLOW_primaryExpression_in_primaryExpression4948 = frozenset([61, 92, 95, 120, 164])
    FOLLOW_IDENT_in_primaryExpression4988 = frozenset([3])
    FOLLOW_THIS_in_primaryExpression5012 = frozenset([3])
    FOLLOW_SUPER_in_primaryExpression5038 = frozenset([3])
    FOLLOW_innerNewExpression_in_primaryExpression5078 = frozenset([3])
    FOLLOW_CLASS_in_primaryExpression5102 = frozenset([3])
    FOLLOW_primitiveType_in_primaryExpression5142 = frozenset([61])
    FOLLOW_CLASS_in_primaryExpression5144 = frozenset([3])
    FOLLOW_VOID_in_primaryExpression5164 = frozenset([61])
    FOLLOW_CLASS_in_primaryExpression5166 = frozenset([3])
    FOLLOW_parenthesizedExpression_in_primaryExpression5203 = frozenset([1])
    FOLLOW_IDENT_in_primaryExpression5216 = frozenset([1])
    FOLLOW_METHOD_CALL_in_primaryExpression5230 = frozenset([2])
    FOLLOW_primaryExpression_in_primaryExpression5244 = frozenset([112, 137])
    FOLLOW_genericTypeArgumentList_in_primaryExpression5256 = frozenset([112])
    FOLLOW_arguments_in_primaryExpression5271 = frozenset([3])
    FOLLOW_explicitConstructorCall_in_primaryExpression5306 = frozenset([1])
    FOLLOW_ARRAY_ELEMENT_ACCESS_in_primaryExpression5320 = frozenset([2])
    FOLLOW_primaryExpression_in_primaryExpression5334 = frozenset([116, 126])
    FOLLOW_expression_in_primaryExpression5348 = frozenset([3])
    FOLLOW_literal_in_primaryExpression5381 = frozenset([1])
    FOLLOW_newExpression_in_primaryExpression5394 = frozenset([1])
    FOLLOW_THIS_in_primaryExpression5407 = frozenset([1])
    FOLLOW_arrayTypeDeclarator_in_primaryExpression5420 = frozenset([1])
    FOLLOW_SUPER_in_primaryExpression5431 = frozenset([1])
    FOLLOW_THIS_CONSTRUCTOR_CALL_in_explicitConstructorCall5458 = frozenset([2])
    FOLLOW_genericTypeArgumentList_in_explicitConstructorCall5460 = frozenset([112])
    FOLLOW_arguments_in_explicitConstructorCall5463 = frozenset([3])
    FOLLOW_SUPER_CONSTRUCTOR_CALL_in_explicitConstructorCall5475 = frozenset([2])
    FOLLOW_primaryExpression_in_explicitConstructorCall5477 = frozenset([112, 137])
    FOLLOW_genericTypeArgumentList_in_explicitConstructorCall5480 = frozenset([112])
    FOLLOW_arguments_in_explicitConstructorCall5483 = frozenset([3])
    FOLLOW_ARRAY_DECLARATOR_in_arrayTypeDeclarator5504 = frozenset([2])
    FOLLOW_arrayTypeDeclarator_in_arrayTypeDeclarator5507 = frozenset([3])
    FOLLOW_qualifiedIdentifier_in_arrayTypeDeclarator5511 = frozenset([3])
    FOLLOW_primitiveType_in_arrayTypeDeclarator5515 = frozenset([3])
    FOLLOW_STATIC_ARRAY_CREATOR_in_newExpression5541 = frozenset([2])
    FOLLOW_primitiveType_in_newExpression5557 = frozenset([114, 116, 126])
    FOLLOW_newArrayConstruction_in_newExpression5561 = frozenset([3])
    FOLLOW_genericTypeArgumentList_in_newExpression5591 = frozenset([151])
    FOLLOW_qualifiedTypeIdent_in_newExpression5596 = frozenset([114, 116, 126])
    FOLLOW_newArrayConstruction_in_newExpression5600 = frozenset([3])
    FOLLOW_CLASS_CONSTRUCTOR_CALL_in_newExpression5647 = frozenset([2])
    FOLLOW_genericTypeArgumentList_in_newExpression5649 = frozenset([151])
    FOLLOW_qualifiedTypeIdent_in_newExpression5654 = frozenset([112])
    FOLLOW_arguments_in_newExpression5668 = frozenset([3, 123, 128, 138, 140])
    FOLLOW_classTopLevelScope_in_newExpression5670 = frozenset([3])
    FOLLOW_CLASS_CONSTRUCTOR_CALL_in_innerNewExpression5728 = frozenset([2])
    FOLLOW_genericTypeArgumentList_in_innerNewExpression5730 = frozenset([164])
    FOLLOW_IDENT_in_innerNewExpression5733 = frozenset([112])
    FOLLOW_arguments_in_innerNewExpression5735 = frozenset([3, 123, 128, 138, 140])
    FOLLOW_classTopLevelScope_in_innerNewExpression5737 = frozenset([3])
    FOLLOW_arrayDeclaratorList_in_newArrayConstruction5762 = frozenset([116])
    FOLLOW_arrayInitializer_in_newArrayConstruction5764 = frozenset([1])
    FOLLOW_expression_in_newArrayConstruction5774 = frozenset([1, 114, 116, 126])
    FOLLOW_arrayDeclaratorList_in_newArrayConstruction5777 = frozenset([1])
    FOLLOW_ARGUMENT_LIST_in_arguments5812 = frozenset([2])
    FOLLOW_expression_in_arguments5817 = frozenset([3, 116, 126])
    FOLLOW_HEX_LITERAL_in_literal5865 = frozenset([1])
    FOLLOW_OCTAL_LITERAL_in_literal5877 = frozenset([1])
    FOLLOW_DECIMAL_LITERAL_in_literal5889 = frozenset([1])
    FOLLOW_FLOATING_POINT_LITERAL_in_literal5901 = frozenset([1])
    FOLLOW_CHARACTER_LITERAL_in_literal5913 = frozenset([1])
    FOLLOW_STRING_LITERAL_in_literal5925 = frozenset([1])
    FOLLOW_TRUE_in_literal5937 = frozenset([1])
    FOLLOW_FALSE_in_literal5949 = frozenset([1])
    FOLLOW_NULL_in_literal5961 = frozenset([1])
    FOLLOW_switchCaseLabel_in_synpred125_JavaTreeParser3922 = frozenset([1])
    FOLLOW_expression_in_synpred132_JavaTreeParser4007 = frozenset([1, 116, 126])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(JavaTreeParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
