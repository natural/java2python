# $ANTLR 3.1.1 JavaTreeParser.g 2009-12-24 20:31:44

import sys
from antlr3 import *
from antlr3.tree import *
from antlr3.compat import set, frozenset
                     
from logging import warn
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
    # JavaTreeParser.g:63:1: javaSource[module] : ^( JAVA_SOURCE annotationList ( packageDeclaration )? ( importDeclaration )* ( typeDeclaration )* ) ;
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

                # JavaTreeParser.g:66:5: ( ^( JAVA_SOURCE annotationList ( packageDeclaration )? ( importDeclaration )* ( typeDeclaration )* ) )
                # JavaTreeParser.g:66:9: ^( JAVA_SOURCE annotationList ( packageDeclaration )? ( importDeclaration )* ( typeDeclaration )* )
                pass 
                self.match(self.input, JAVA_SOURCE, self.FOLLOW_JAVA_SOURCE_in_javaSource98)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_annotationList_in_javaSource110)
                self.annotationList()

                self._state.following.pop()
                # JavaTreeParser.g:68:11: ( packageDeclaration )?
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == PACKAGE) :
                    alt1 = 1
                if alt1 == 1:
                    # JavaTreeParser.g:0:0: packageDeclaration
                    pass 
                    self._state.following.append(self.FOLLOW_packageDeclaration_in_javaSource122)
                    self.packageDeclaration()

                    self._state.following.pop()



                # JavaTreeParser.g:69:11: ( importDeclaration )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == IMPORT) :
                        alt2 = 1


                    if alt2 == 1:
                        # JavaTreeParser.g:0:0: importDeclaration
                        pass 
                        self._state.following.append(self.FOLLOW_importDeclaration_in_javaSource135)
                        self.importDeclaration()

                        self._state.following.pop()


                    else:
                        break #loop2


                # JavaTreeParser.g:70:11: ( typeDeclaration )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == AT or LA3_0 == CLASS or LA3_0 == ENUM or LA3_0 == INTERFACE) :
                        alt3 = 1


                    if alt3 == 1:
                        # JavaTreeParser.g:0:0: typeDeclaration
                        pass 
                        self._state.following.append(self.FOLLOW_typeDeclaration_in_javaSource148)
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
    # JavaTreeParser.g:75:1: packageDeclaration : ^( PACKAGE qi0= qualifiedIdentifier ) ;
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

                # JavaTreeParser.g:76:5: ( ^( PACKAGE qi0= qualifiedIdentifier ) )
                # JavaTreeParser.g:76:9: ^( PACKAGE qi0= qualifiedIdentifier )
                pass 
                self.match(self.input, PACKAGE, self.FOLLOW_PACKAGE_in_packageDeclaration180)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_packageDeclaration184)
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
    # JavaTreeParser.g:80:1: importDeclaration : ^( IMPORT ( STATIC )? qi0= qualifiedIdentifier ( DOTSTAR )? ) ;
    def importDeclaration(self, ):

        importDeclaration_StartIndex = self.input.index()
        qi0 = None


        star = None 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 3):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:82:5: ( ^( IMPORT ( STATIC )? qi0= qualifiedIdentifier ( DOTSTAR )? ) )
                # JavaTreeParser.g:82:9: ^( IMPORT ( STATIC )? qi0= qualifiedIdentifier ( DOTSTAR )? )
                pass 
                self.match(self.input, IMPORT, self.FOLLOW_IMPORT_in_importDeclaration217)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:82:18: ( STATIC )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == STATIC) :
                    alt4 = 1
                if alt4 == 1:
                    # JavaTreeParser.g:0:0: STATIC
                    pass 
                    self.match(self.input, STATIC, self.FOLLOW_STATIC_in_importDeclaration219)



                self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_importDeclaration224)
                qi0 = self.qualifiedIdentifier()

                self._state.following.pop()
                # JavaTreeParser.g:82:50: ( DOTSTAR )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == DOTSTAR) :
                    alt5 = 1
                if alt5 == 1:
                    # JavaTreeParser.g:82:51: DOTSTAR
                    pass 
                    self.match(self.input, DOTSTAR, self.FOLLOW_DOTSTAR_in_importDeclaration227)
                    if self._state.backtracking == 0:
                        star=True 




                if self._state.backtracking == 0:
                    self.addImport(qi0, star) 


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
    # JavaTreeParser.g:88:1: typeDeclaration : ( ^( CLASS md0= modifierList id0= IDENT ( genericTypeParameterList )? (ec0= extendsClause )? (ic0= implementsClause )? classTopLevelScope ) | ^( INTERFACE md0= modifierList id0= IDENT ( genericTypeParameterList )? (ec0= extendsClause )? interfaceTopLevelScope ) | ^( ENUM md0= modifierList id0= IDENT (ic0= implementsClause )? enumTopLevelScope ) | ^( AT md0= modifierList id0= IDENT annotationTopLevelScope ) );
    def typeDeclaration(self, ):

        retval = self.typeDeclaration_return()
        retval.start = self.input.LT(1)
        typeDeclaration_StartIndex = self.input.index()
        id0 = None
        md0 = None

        ec0 = None

        ic0 = None


        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 4):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # JavaTreeParser.g:89:5: ( ^( CLASS md0= modifierList id0= IDENT ( genericTypeParameterList )? (ec0= extendsClause )? (ic0= implementsClause )? classTopLevelScope ) | ^( INTERFACE md0= modifierList id0= IDENT ( genericTypeParameterList )? (ec0= extendsClause )? interfaceTopLevelScope ) | ^( ENUM md0= modifierList id0= IDENT (ic0= implementsClause )? enumTopLevelScope ) | ^( AT md0= modifierList id0= IDENT annotationTopLevelScope ) )
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
                    # JavaTreeParser.g:89:9: ^( CLASS md0= modifierList id0= IDENT ( genericTypeParameterList )? (ec0= extendsClause )? (ic0= implementsClause )? classTopLevelScope )
                    pass 
                    self.match(self.input, CLASS, self.FOLLOW_CLASS_in_typeDeclaration274)

                    if self._state.backtracking == 0:
                        self.beginClassDeclaration() 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_typeDeclaration300)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addModifiers(md0) 

                    id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_typeDeclaration316)
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
                        self._state.following.append(self.FOLLOW_genericTypeParameterList_in_typeDeclaration330)
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
                        self._state.following.append(self.FOLLOW_extendsClause_in_typeDeclaration346)
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
                        self._state.following.append(self.FOLLOW_implementsClause_in_typeDeclaration365)
                        ic0 = self.implementsClause()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self.addBases(ic0) 




                    self._state.following.append(self.FOLLOW_classTopLevelScope_in_typeDeclaration381)
                    self.classTopLevelScope()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                                   
                        self.commentHandler(retval.start)
                        self.endClassDeclaration()
                                  


                    self.match(self.input, UP, None)


                elif alt12 == 2:
                    # JavaTreeParser.g:103:9: ^( INTERFACE md0= modifierList id0= IDENT ( genericTypeParameterList )? (ec0= extendsClause )? interfaceTopLevelScope )
                    pass 
                    self.match(self.input, INTERFACE, self.FOLLOW_INTERFACE_in_typeDeclaration415)

                    if self._state.backtracking == 0:
                        self.beginInterfaceDeclaration() 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_typeDeclaration441)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addModifiers(md0) 

                    id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_typeDeclaration457)
                    if self._state.backtracking == 0:
                        self.setIdent(ident=id0.text) 

                    # JavaTreeParser.g:107:11: ( genericTypeParameterList )?
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == GENERIC_TYPE_PARAM_LIST) :
                        alt9 = 1
                    if alt9 == 1:
                        # JavaTreeParser.g:0:0: genericTypeParameterList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeParameterList_in_typeDeclaration471)
                        self.genericTypeParameterList()

                        self._state.following.pop()



                    # JavaTreeParser.g:108:11: (ec0= extendsClause )?
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == EXTENDS_CLAUSE) :
                        alt10 = 1
                    if alt10 == 1:
                        # JavaTreeParser.g:108:12: ec0= extendsClause
                        pass 
                        self._state.following.append(self.FOLLOW_extendsClause_in_typeDeclaration487)
                        ec0 = self.extendsClause()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self.addBases(ec0) 




                    self._state.following.append(self.FOLLOW_interfaceTopLevelScope_in_typeDeclaration503)
                    self.interfaceTopLevelScope()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                                   
                        self.commentHandler(retval.start)
                        self.endInterfaceDeclaration()
                                  


                    self.match(self.input, UP, None)


                elif alt12 == 3:
                    # JavaTreeParser.g:116:9: ^( ENUM md0= modifierList id0= IDENT (ic0= implementsClause )? enumTopLevelScope )
                    pass 
                    self.match(self.input, ENUM, self.FOLLOW_ENUM_in_typeDeclaration537)

                    if self._state.backtracking == 0:
                        self.beginEnumerationDeclaration() 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_typeDeclaration563)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addModifiers(md0) 

                    id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_typeDeclaration579)
                    if self._state.backtracking == 0:
                        self.setIdent(ident=id0.text) 

                    # JavaTreeParser.g:120:11: (ic0= implementsClause )?
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == IMPLEMENTS_CLAUSE) :
                        alt11 = 1
                    if alt11 == 1:
                        # JavaTreeParser.g:120:12: ic0= implementsClause
                        pass 
                        self._state.following.append(self.FOLLOW_implementsClause_in_typeDeclaration596)
                        ic0 = self.implementsClause()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self.addBases(ic0) 




                    self._state.following.append(self.FOLLOW_enumTopLevelScope_in_typeDeclaration612)
                    self.enumTopLevelScope()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                                   
                        self.commentHandler(retval.start)
                        self.endEnumerationDeclaration()
                                  


                    self.match(self.input, UP, None)


                elif alt12 == 4:
                    # JavaTreeParser.g:128:9: ^( AT md0= modifierList id0= IDENT annotationTopLevelScope )
                    pass 
                    self.match(self.input, AT, self.FOLLOW_AT_in_typeDeclaration646)

                    if self._state.backtracking == 0:
                        self.beginAnnotationDeclaration() 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_typeDeclaration672)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addModifiers(md0) 

                    id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_typeDeclaration688)
                    if self._state.backtracking == 0:
                        self.setIdent(ident=id0.text) 

                    self._state.following.append(self.FOLLOW_annotationTopLevelScope_in_typeDeclaration702)
                    self.annotationTopLevelScope()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                                   
                        self.commentHandler(retval.start)
                        self.endAnnotationDeclration()
                                  


                    self.match(self.input, UP, None)



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
    # JavaTreeParser.g:141:1: extendsClause returns [values] : ^( EXTENDS_CLAUSE (tp0= type )+ ) ;
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

                # JavaTreeParser.g:143:5: ( ^( EXTENDS_CLAUSE (tp0= type )+ ) )
                # JavaTreeParser.g:143:9: ^( EXTENDS_CLAUSE (tp0= type )+ )
                pass 
                self.match(self.input, EXTENDS_CLAUSE, self.FOLLOW_EXTENDS_CLAUSE_in_extendsClause758)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:143:26: (tp0= type )+
                cnt13 = 0
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == TYPE) :
                        alt13 = 1


                    if alt13 == 1:
                        # JavaTreeParser.g:143:27: tp0= type
                        pass 
                        self._state.following.append(self.FOLLOW_type_in_extendsClause763)
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
    # JavaTreeParser.g:147:1: implementsClause returns [values] : ^( IMPLEMENTS_CLAUSE (tp0= type )+ ) ;
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

                # JavaTreeParser.g:149:5: ( ^( IMPLEMENTS_CLAUSE (tp0= type )+ ) )
                # JavaTreeParser.g:149:9: ^( IMPLEMENTS_CLAUSE (tp0= type )+ )
                pass 
                self.match(self.input, IMPLEMENTS_CLAUSE, self.FOLLOW_IMPLEMENTS_CLAUSE_in_implementsClause802)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:149:29: (tp0= type )+
                cnt14 = 0
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == TYPE) :
                        alt14 = 1


                    if alt14 == 1:
                        # JavaTreeParser.g:149:30: tp0= type
                        pass 
                        self._state.following.append(self.FOLLOW_type_in_implementsClause807)
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
    # JavaTreeParser.g:152:1: genericTypeParameterList : ^( GENERIC_TYPE_PARAM_LIST ( genericTypeParameter )+ ) ;
    def genericTypeParameterList(self, ):

        genericTypeParameterList_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 7):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:153:5: ( ^( GENERIC_TYPE_PARAM_LIST ( genericTypeParameter )+ ) )
                # JavaTreeParser.g:153:9: ^( GENERIC_TYPE_PARAM_LIST ( genericTypeParameter )+ )
                pass 
                self.match(self.input, GENERIC_TYPE_PARAM_LIST, self.FOLLOW_GENERIC_TYPE_PARAM_LIST_in_genericTypeParameterList832)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:153:35: ( genericTypeParameter )+
                cnt15 = 0
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == IDENT) :
                        alt15 = 1


                    if alt15 == 1:
                        # JavaTreeParser.g:0:0: genericTypeParameter
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeParameter_in_genericTypeParameterList834)
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
    # JavaTreeParser.g:156:1: genericTypeParameter : ^( IDENT ( bound )? ) ;
    def genericTypeParameter(self, ):

        genericTypeParameter_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 8):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:157:5: ( ^( IDENT ( bound )? ) )
                # JavaTreeParser.g:157:9: ^( IDENT ( bound )? )
                pass 
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_genericTypeParameter856)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:157:17: ( bound )?
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == EXTENDS_BOUND_LIST) :
                        alt16 = 1
                    if alt16 == 1:
                        # JavaTreeParser.g:0:0: bound
                        pass 
                        self._state.following.append(self.FOLLOW_bound_in_genericTypeParameter858)
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
    # JavaTreeParser.g:160:1: bound : ^( EXTENDS_BOUND_LIST ( type )+ ) ;
    def bound(self, ):

        bound_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 9):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:161:5: ( ^( EXTENDS_BOUND_LIST ( type )+ ) )
                # JavaTreeParser.g:161:9: ^( EXTENDS_BOUND_LIST ( type )+ )
                pass 
                self.match(self.input, EXTENDS_BOUND_LIST, self.FOLLOW_EXTENDS_BOUND_LIST_in_bound880)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:161:30: ( type )+
                cnt17 = 0
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == TYPE) :
                        alt17 = 1


                    if alt17 == 1:
                        # JavaTreeParser.g:0:0: type
                        pass 
                        self._state.following.append(self.FOLLOW_type_in_bound882)
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
    # JavaTreeParser.g:164:1: enumTopLevelScope : ^( ENUM_TOP_LEVEL_SCOPE ( enumConstant )+ ( classTopLevelScope )? ) ;
    def enumTopLevelScope(self, ):

        enumTopLevelScope_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 10):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:165:5: ( ^( ENUM_TOP_LEVEL_SCOPE ( enumConstant )+ ( classTopLevelScope )? ) )
                # JavaTreeParser.g:165:9: ^( ENUM_TOP_LEVEL_SCOPE ( enumConstant )+ ( classTopLevelScope )? )
                pass 
                self.match(self.input, ENUM_TOP_LEVEL_SCOPE, self.FOLLOW_ENUM_TOP_LEVEL_SCOPE_in_enumTopLevelScope904)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:165:32: ( enumConstant )+
                cnt18 = 0
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == IDENT) :
                        alt18 = 1


                    if alt18 == 1:
                        # JavaTreeParser.g:0:0: enumConstant
                        pass 
                        self._state.following.append(self.FOLLOW_enumConstant_in_enumTopLevelScope906)
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


                # JavaTreeParser.g:165:46: ( classTopLevelScope )?
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == CLASS_TOP_LEVEL_SCOPE) :
                    alt19 = 1
                if alt19 == 1:
                    # JavaTreeParser.g:0:0: classTopLevelScope
                    pass 
                    self._state.following.append(self.FOLLOW_classTopLevelScope_in_enumTopLevelScope909)
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
    # JavaTreeParser.g:168:1: enumConstant : ^(id0= IDENT annotationList (ag0= arguments )? ( classTopLevelScope )? ) ;
    def enumConstant(self, ):

        enumConstant_StartIndex = self.input.index()
        id0 = None
        ag0 = None


        args = None 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 11):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:170:5: ( ^(id0= IDENT annotationList (ag0= arguments )? ( classTopLevelScope )? ) )
                # JavaTreeParser.g:170:9: ^(id0= IDENT annotationList (ag0= arguments )? ( classTopLevelScope )? )
                pass 
                id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_enumConstant942)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_annotationList_in_enumConstant954)
                self.annotationList()

                self._state.following.pop()
                # JavaTreeParser.g:172:11: (ag0= arguments )?
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == ARGUMENT_LIST) :
                    alt20 = 1
                if alt20 == 1:
                    # JavaTreeParser.g:172:12: ag0= arguments
                    pass 
                    self._state.following.append(self.FOLLOW_arguments_in_enumConstant969)
                    ag0 = self.arguments()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        args = ag0 




                # JavaTreeParser.g:173:11: ( classTopLevelScope )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == CLASS_TOP_LEVEL_SCOPE) :
                    alt21 = 1
                if alt21 == 1:
                    # JavaTreeParser.g:0:0: classTopLevelScope
                    pass 
                    self._state.following.append(self.FOLLOW_classTopLevelScope_in_enumConstant985)
                    self.classTopLevelScope()

                    self._state.following.pop()




                self.match(self.input, UP, None)
                if self._state.backtracking == 0:
                    self.addEnumValue(id0.text, args) 





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
    # JavaTreeParser.g:179:1: classTopLevelScope : ^( CLASS_TOP_LEVEL_SCOPE ( classScopeDeclarations )* ) ;
    def classTopLevelScope(self, ):

        classTopLevelScope_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 12):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:180:5: ( ^( CLASS_TOP_LEVEL_SCOPE ( classScopeDeclarations )* ) )
                # JavaTreeParser.g:180:9: ^( CLASS_TOP_LEVEL_SCOPE ( classScopeDeclarations )* )
                pass 
                self.match(self.input, CLASS_TOP_LEVEL_SCOPE, self.FOLLOW_CLASS_TOP_LEVEL_SCOPE_in_classTopLevelScope1027)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:180:33: ( classScopeDeclarations )*
                    while True: #loop22
                        alt22 = 2
                        LA22_0 = self.input.LA(1)

                        if (LA22_0 == AT or LA22_0 == CLASS or LA22_0 == ENUM or LA22_0 == INTERFACE or (CLASS_INSTANCE_INITIALIZER <= LA22_0 <= CLASS_STATIC_INITIALIZER) or LA22_0 == CONSTRUCTOR_DECL or LA22_0 == FUNCTION_METHOD_DECL or LA22_0 == VAR_DECLARATION or LA22_0 == VOID_METHOD_DECL) :
                            alt22 = 1


                        if alt22 == 1:
                            # JavaTreeParser.g:0:0: classScopeDeclarations
                            pass 
                            self._state.following.append(self.FOLLOW_classScopeDeclarations_in_classTopLevelScope1029)
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

    class classScopeDeclarations_return(TreeRuleReturnScope):
        def __init__(self):
            TreeRuleReturnScope.__init__(self)





    # $ANTLR start "classScopeDeclarations"
    # JavaTreeParser.g:184:1: classScopeDeclarations : ( ^( CLASS_INSTANCE_INITIALIZER block ) | ^( CLASS_STATIC_INITIALIZER block ) | ^( FUNCTION_METHOD_DECL md0= modifierList ( genericTypeParameterList )? tp0= type id0= IDENT fp0= formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block )? ) | ^( VOID_METHOD_DECL md0= modifierList ( genericTypeParameterList )? id0= IDENT fp0= formalParameterList ( throwsClause )? ( block )? ) | ^( VAR_DECLARATION md0= modifierList tp0= type vd0= variableDeclaratorList ) | ^( CONSTRUCTOR_DECL md0= modifierList ( genericTypeParameterList )? fp0= formalParameterList ( throwsClause )? block ) | typeDeclaration );
    def classScopeDeclarations(self, ):

        retval = self.classScopeDeclarations_return()
        retval.start = self.input.LT(1)
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
                    return retval

                # JavaTreeParser.g:188:5: ( ^( CLASS_INSTANCE_INITIALIZER block ) | ^( CLASS_STATIC_INITIALIZER block ) | ^( FUNCTION_METHOD_DECL md0= modifierList ( genericTypeParameterList )? tp0= type id0= IDENT fp0= formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block )? ) | ^( VOID_METHOD_DECL md0= modifierList ( genericTypeParameterList )? id0= IDENT fp0= formalParameterList ( throwsClause )? ( block )? ) | ^( VAR_DECLARATION md0= modifierList tp0= type vd0= variableDeclaratorList ) | ^( CONSTRUCTOR_DECL md0= modifierList ( genericTypeParameterList )? fp0= formalParameterList ( throwsClause )? block ) | typeDeclaration )
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
                    # JavaTreeParser.g:188:9: ^( CLASS_INSTANCE_INITIALIZER block )
                    pass 
                    self.match(self.input, CLASS_INSTANCE_INITIALIZER, self.FOLLOW_CLASS_INSTANCE_INITIALIZER_in_classScopeDeclarations1072)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_block_in_classScopeDeclarations1074)
                    self.block()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt32 == 2:
                    # JavaTreeParser.g:190:9: ^( CLASS_STATIC_INITIALIZER block )
                    pass 
                    self.match(self.input, CLASS_STATIC_INITIALIZER, self.FOLLOW_CLASS_STATIC_INITIALIZER_in_classScopeDeclarations1087)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_block_in_classScopeDeclarations1089)
                    self.block()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt32 == 3:
                    # JavaTreeParser.g:192:9: ^( FUNCTION_METHOD_DECL md0= modifierList ( genericTypeParameterList )? tp0= type id0= IDENT fp0= formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block )? )
                    pass 
                    self.match(self.input, FUNCTION_METHOD_DECL, self.FOLLOW_FUNCTION_METHOD_DECL_in_classScopeDeclarations1102)

                    if self._state.backtracking == 0:
                        self.beginMethodDecl() 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_classScopeDeclarations1129)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addModifiers(md0) 

                    # JavaTreeParser.g:196:11: ( genericTypeParameterList )?
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == GENERIC_TYPE_PARAM_LIST) :
                        alt23 = 1
                    if alt23 == 1:
                        # JavaTreeParser.g:0:0: genericTypeParameterList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeParameterList_in_classScopeDeclarations1143)
                        self.genericTypeParameterList()

                        self._state.following.pop()



                    self._state.following.append(self.FOLLOW_type_in_classScopeDeclarations1158)
                    tp0 = self.type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.setType(((tp0 is not None) and [tp0.value] or [None])[0]) 

                    id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_classScopeDeclarations1174)
                    if self._state.backtracking == 0:
                        self.setIdent(ident=id0.text) 

                    self._state.following.append(self.FOLLOW_formalParameterList_in_classScopeDeclarations1190)
                    fp0 = self.formalParameterList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addParameters(fp0) 

                    # JavaTreeParser.g:200:11: ( arrayDeclaratorList )?
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == ARRAY_DECLARATOR_LIST) :
                        alt24 = 1
                    if alt24 == 1:
                        # JavaTreeParser.g:0:0: arrayDeclaratorList
                        pass 
                        self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_classScopeDeclarations1204)
                        self.arrayDeclaratorList()

                        self._state.following.pop()



                    # JavaTreeParser.g:201:11: ( throwsClause )?
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == THROWS_CLAUSE) :
                        alt25 = 1
                    if alt25 == 1:
                        # JavaTreeParser.g:0:0: throwsClause
                        pass 
                        self._state.following.append(self.FOLLOW_throwsClause_in_classScopeDeclarations1217)
                        self.throwsClause()

                        self._state.following.pop()



                    # JavaTreeParser.g:202:11: ( block )?
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == BLOCK_SCOPE) :
                        alt26 = 1
                    if alt26 == 1:
                        # JavaTreeParser.g:0:0: block
                        pass 
                        self._state.following.append(self.FOLLOW_block_in_classScopeDeclarations1230)
                        self.block()

                        self._state.following.pop()



                    if self._state.backtracking == 0:
                                   
                        self.commentHandler(retval.start)
                        self.endMethodDecl()
                                  


                    self.match(self.input, UP, None)


                elif alt32 == 4:
                    # JavaTreeParser.g:209:9: ^( VOID_METHOD_DECL md0= modifierList ( genericTypeParameterList )? id0= IDENT fp0= formalParameterList ( throwsClause )? ( block )? )
                    pass 
                    self.match(self.input, VOID_METHOD_DECL, self.FOLLOW_VOID_METHOD_DECL_in_classScopeDeclarations1265)

                    if self._state.backtracking == 0:
                        self.beginMethodDecl() 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_classScopeDeclarations1291)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addModifiers(md0) 

                    # JavaTreeParser.g:212:11: ( genericTypeParameterList )?
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == GENERIC_TYPE_PARAM_LIST) :
                        alt27 = 1
                    if alt27 == 1:
                        # JavaTreeParser.g:0:0: genericTypeParameterList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeParameterList_in_classScopeDeclarations1305)
                        self.genericTypeParameterList()

                        self._state.following.pop()



                    id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_classScopeDeclarations1320)
                    if self._state.backtracking == 0:
                        self.setIdent(ident=id0.text) 

                    self._state.following.append(self.FOLLOW_formalParameterList_in_classScopeDeclarations1336)
                    fp0 = self.formalParameterList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addParameters(fp0) 

                    # JavaTreeParser.g:215:11: ( throwsClause )?
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == THROWS_CLAUSE) :
                        alt28 = 1
                    if alt28 == 1:
                        # JavaTreeParser.g:0:0: throwsClause
                        pass 
                        self._state.following.append(self.FOLLOW_throwsClause_in_classScopeDeclarations1350)
                        self.throwsClause()

                        self._state.following.pop()



                    # JavaTreeParser.g:216:11: ( block )?
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if (LA29_0 == BLOCK_SCOPE) :
                        alt29 = 1
                    if alt29 == 1:
                        # JavaTreeParser.g:0:0: block
                        pass 
                        self._state.following.append(self.FOLLOW_block_in_classScopeDeclarations1363)
                        self.block()

                        self._state.following.pop()



                    if self._state.backtracking == 0:
                                   
                        self.commentHandler(retval.start)
                        self.setType("void")
                        self.endMethodDecl()
                                  


                    self.match(self.input, UP, None)


                elif alt32 == 5:
                    # JavaTreeParser.g:224:9: ^( VAR_DECLARATION md0= modifierList tp0= type vd0= variableDeclaratorList )
                    pass 
                    self.match(self.input, VAR_DECLARATION, self.FOLLOW_VAR_DECLARATION_in_classScopeDeclarations1399)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_classScopeDeclarations1413)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_type_in_classScopeDeclarations1427)
                    tp0 = self.type()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_variableDeclaratorList_in_classScopeDeclarations1441)
                    vd0 = self.variableDeclaratorList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addVariables(vd0, ((tp0 is not None) and [tp0.value] or [None])[0], md0, cls=True) 


                    self.match(self.input, UP, None)


                elif alt32 == 6:
                    # JavaTreeParser.g:231:9: ^( CONSTRUCTOR_DECL md0= modifierList ( genericTypeParameterList )? fp0= formalParameterList ( throwsClause )? block )
                    pass 
                    self.match(self.input, CONSTRUCTOR_DECL, self.FOLLOW_CONSTRUCTOR_DECL_in_classScopeDeclarations1475)

                    if self._state.backtracking == 0:
                        self.beginMethodDecl() 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_classScopeDeclarations1501)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addModifiers(md0) 

                    # JavaTreeParser.g:234:11: ( genericTypeParameterList )?
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == GENERIC_TYPE_PARAM_LIST) :
                        alt30 = 1
                    if alt30 == 1:
                        # JavaTreeParser.g:0:0: genericTypeParameterList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeParameterList_in_classScopeDeclarations1515)
                        self.genericTypeParameterList()

                        self._state.following.pop()



                    self._state.following.append(self.FOLLOW_formalParameterList_in_classScopeDeclarations1530)
                    fp0 = self.formalParameterList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addParameters(fp0) 

                    # JavaTreeParser.g:236:11: ( throwsClause )?
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == THROWS_CLAUSE) :
                        alt31 = 1
                    if alt31 == 1:
                        # JavaTreeParser.g:0:0: throwsClause
                        pass 
                        self._state.following.append(self.FOLLOW_throwsClause_in_classScopeDeclarations1544)
                        self.throwsClause()

                        self._state.following.pop()



                    self._state.following.append(self.FOLLOW_block_in_classScopeDeclarations1557)
                    self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                                   
                        self.commentHandler(retval.start)
                        self.setIdent("__init__")
                        self.endMethodDecl()
                                  


                    self.match(self.input, UP, None)


                elif alt32 == 7:
                    # JavaTreeParser.g:245:9: typeDeclaration
                    pass 
                    self._state.following.append(self.FOLLOW_typeDeclaration_in_classScopeDeclarations1590)
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

        return retval

    # $ANTLR end "classScopeDeclarations"


    # $ANTLR start "interfaceTopLevelScope"
    # JavaTreeParser.g:249:1: interfaceTopLevelScope : ^( INTERFACE_TOP_LEVEL_SCOPE ( interfaceScopeDeclarations )* ) ;
    def interfaceTopLevelScope(self, ):

        interfaceTopLevelScope_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 14):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:250:5: ( ^( INTERFACE_TOP_LEVEL_SCOPE ( interfaceScopeDeclarations )* ) )
                # JavaTreeParser.g:250:9: ^( INTERFACE_TOP_LEVEL_SCOPE ( interfaceScopeDeclarations )* )
                pass 
                self.match(self.input, INTERFACE_TOP_LEVEL_SCOPE, self.FOLLOW_INTERFACE_TOP_LEVEL_SCOPE_in_interfaceTopLevelScope1611)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:250:37: ( interfaceScopeDeclarations )*
                    while True: #loop33
                        alt33 = 2
                        LA33_0 = self.input.LA(1)

                        if (LA33_0 == AT or LA33_0 == CLASS or LA33_0 == ENUM or LA33_0 == INTERFACE or LA33_0 == FUNCTION_METHOD_DECL or LA33_0 == VAR_DECLARATION or LA33_0 == VOID_METHOD_DECL) :
                            alt33 = 1


                        if alt33 == 1:
                            # JavaTreeParser.g:0:0: interfaceScopeDeclarations
                            pass 
                            self._state.following.append(self.FOLLOW_interfaceScopeDeclarations_in_interfaceTopLevelScope1613)
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

    class interfaceScopeDeclarations_return(TreeRuleReturnScope):
        def __init__(self):
            TreeRuleReturnScope.__init__(self)





    # $ANTLR start "interfaceScopeDeclarations"
    # JavaTreeParser.g:254:1: interfaceScopeDeclarations : ( ^( FUNCTION_METHOD_DECL md0= modifierList ( genericTypeParameterList )? tp0= type id0= IDENT fp0= formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ) | ^( VOID_METHOD_DECL md0= modifierList ( genericTypeParameterList )? id0= IDENT fp0= formalParameterList ( throwsClause )? ) | ^( VAR_DECLARATION md1= modifierList tp1= type vd1= variableDeclaratorList ) | typeDeclaration );
    def interfaceScopeDeclarations(self, ):

        retval = self.interfaceScopeDeclarations_return()
        retval.start = self.input.LT(1)
        interfaceScopeDeclarations_StartIndex = self.input.index()
        id0 = None
        md0 = None

        tp0 = None

        fp0 = None

        md1 = None

        tp1 = None

        vd1 = None


        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 15):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # JavaTreeParser.g:256:5: ( ^( FUNCTION_METHOD_DECL md0= modifierList ( genericTypeParameterList )? tp0= type id0= IDENT fp0= formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ) | ^( VOID_METHOD_DECL md0= modifierList ( genericTypeParameterList )? id0= IDENT fp0= formalParameterList ( throwsClause )? ) | ^( VAR_DECLARATION md1= modifierList tp1= type vd1= variableDeclaratorList ) | typeDeclaration )
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
                    # JavaTreeParser.g:256:9: ^( FUNCTION_METHOD_DECL md0= modifierList ( genericTypeParameterList )? tp0= type id0= IDENT fp0= formalParameterList ( arrayDeclaratorList )? ( throwsClause )? )
                    pass 
                    self.match(self.input, FUNCTION_METHOD_DECL, self.FOLLOW_FUNCTION_METHOD_DECL_in_interfaceScopeDeclarations1645)

                    if self._state.backtracking == 0:
                        self.beginMethodDecl() 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_interfaceScopeDeclarations1671)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addModifiers(md0) 

                    # JavaTreeParser.g:259:11: ( genericTypeParameterList )?
                    alt34 = 2
                    LA34_0 = self.input.LA(1)

                    if (LA34_0 == GENERIC_TYPE_PARAM_LIST) :
                        alt34 = 1
                    if alt34 == 1:
                        # JavaTreeParser.g:0:0: genericTypeParameterList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeParameterList_in_interfaceScopeDeclarations1685)
                        self.genericTypeParameterList()

                        self._state.following.pop()



                    self._state.following.append(self.FOLLOW_type_in_interfaceScopeDeclarations1700)
                    tp0 = self.type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.setType(((tp0 is not None) and [tp0.value] or [None])[0]) 

                    id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_interfaceScopeDeclarations1716)
                    if self._state.backtracking == 0:
                        self.setIdent(ident=id0.text) 

                    self._state.following.append(self.FOLLOW_formalParameterList_in_interfaceScopeDeclarations1732)
                    fp0 = self.formalParameterList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addParameters(fp0) 

                    # JavaTreeParser.g:263:11: ( arrayDeclaratorList )?
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if (LA35_0 == ARRAY_DECLARATOR_LIST) :
                        alt35 = 1
                    if alt35 == 1:
                        # JavaTreeParser.g:0:0: arrayDeclaratorList
                        pass 
                        self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_interfaceScopeDeclarations1746)
                        self.arrayDeclaratorList()

                        self._state.following.pop()



                    # JavaTreeParser.g:264:11: ( throwsClause )?
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if (LA36_0 == THROWS_CLAUSE) :
                        alt36 = 1
                    if alt36 == 1:
                        # JavaTreeParser.g:0:0: throwsClause
                        pass 
                        self._state.following.append(self.FOLLOW_throwsClause_in_interfaceScopeDeclarations1759)
                        self.throwsClause()

                        self._state.following.pop()



                    if self._state.backtracking == 0:
                        self.endMethodDecl() 


                    self.match(self.input, UP, None)


                elif alt39 == 2:
                    # JavaTreeParser.g:268:9: ^( VOID_METHOD_DECL md0= modifierList ( genericTypeParameterList )? id0= IDENT fp0= formalParameterList ( throwsClause )? )
                    pass 
                    self.match(self.input, VOID_METHOD_DECL, self.FOLLOW_VOID_METHOD_DECL_in_interfaceScopeDeclarations1794)

                    if self._state.backtracking == 0:
                        self.beginMethodDecl() 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_interfaceScopeDeclarations1820)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addModifiers(md0) 

                    # JavaTreeParser.g:271:11: ( genericTypeParameterList )?
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == GENERIC_TYPE_PARAM_LIST) :
                        alt37 = 1
                    if alt37 == 1:
                        # JavaTreeParser.g:0:0: genericTypeParameterList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeParameterList_in_interfaceScopeDeclarations1834)
                        self.genericTypeParameterList()

                        self._state.following.pop()



                    id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_interfaceScopeDeclarations1849)
                    if self._state.backtracking == 0:
                        self.setIdent(ident=id0.text) 

                    self._state.following.append(self.FOLLOW_formalParameterList_in_interfaceScopeDeclarations1865)
                    fp0 = self.formalParameterList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addParameters(fp0) 

                    # JavaTreeParser.g:274:11: ( throwsClause )?
                    alt38 = 2
                    LA38_0 = self.input.LA(1)

                    if (LA38_0 == THROWS_CLAUSE) :
                        alt38 = 1
                    if alt38 == 1:
                        # JavaTreeParser.g:0:0: throwsClause
                        pass 
                        self._state.following.append(self.FOLLOW_throwsClause_in_interfaceScopeDeclarations1879)
                        self.throwsClause()

                        self._state.following.pop()



                    if self._state.backtracking == 0:
                                   
                        self.setType("void")
                        self.endMethodDecl()
                                  


                    self.match(self.input, UP, None)


                elif alt39 == 3:
                    # JavaTreeParser.g:281:9: ^( VAR_DECLARATION md1= modifierList tp1= type vd1= variableDeclaratorList )
                    pass 
                    self.match(self.input, VAR_DECLARATION, self.FOLLOW_VAR_DECLARATION_in_interfaceScopeDeclarations1914)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_interfaceScopeDeclarations1928)
                    md1 = self.modifierList()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_type_in_interfaceScopeDeclarations1942)
                    tp1 = self.type()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_variableDeclaratorList_in_interfaceScopeDeclarations1956)
                    vd1 = self.variableDeclaratorList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addClassVariables(vd1, ((tp1 is not None) and [tp1.value] or [None])[0], md1) 


                    self.match(self.input, UP, None)


                elif alt39 == 4:
                    # JavaTreeParser.g:288:9: typeDeclaration
                    pass 
                    self._state.following.append(self.FOLLOW_typeDeclaration_in_interfaceScopeDeclarations1989)
                    self.typeDeclaration()

                    self._state.following.pop()


                if self._state.backtracking == 0:
                    self.commentHandler(retval.start) 


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 15, interfaceScopeDeclarations_StartIndex, success)

            pass

        return retval

    # $ANTLR end "interfaceScopeDeclarations"


    # $ANTLR start "variableDeclaratorList"
    # JavaTreeParser.g:292:1: variableDeclaratorList returns [values] : ^( VAR_DECLARATOR_LIST (vd0= variableDeclarator )+ ) ;
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

                # JavaTreeParser.g:294:5: ( ^( VAR_DECLARATOR_LIST (vd0= variableDeclarator )+ ) )
                # JavaTreeParser.g:294:9: ^( VAR_DECLARATOR_LIST (vd0= variableDeclarator )+ )
                pass 
                self.match(self.input, VAR_DECLARATOR_LIST, self.FOLLOW_VAR_DECLARATOR_LIST_in_variableDeclaratorList2023)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:294:31: (vd0= variableDeclarator )+
                cnt40 = 0
                while True: #loop40
                    alt40 = 2
                    LA40_0 = self.input.LA(1)

                    if (LA40_0 == VAR_DECLARATOR) :
                        alt40 = 1


                    if alt40 == 1:
                        # JavaTreeParser.g:294:32: vd0= variableDeclarator
                        pass 
                        self._state.following.append(self.FOLLOW_variableDeclarator_in_variableDeclaratorList2028)
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
    # JavaTreeParser.g:298:1: variableDeclarator returns [value] : ^( VAR_DECLARATOR (vd0= variableDeclaratorId ) (vi0= variableInitializer )? ) ;
    def variableDeclarator(self, ):

        value = None
        variableDeclarator_StartIndex = self.input.index()
        vd0 = None

        vi0 = None


        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 17):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:299:5: ( ^( VAR_DECLARATOR (vd0= variableDeclaratorId ) (vi0= variableInitializer )? ) )
                # JavaTreeParser.g:299:9: ^( VAR_DECLARATOR (vd0= variableDeclaratorId ) (vi0= variableInitializer )? )
                pass 
                self.match(self.input, VAR_DECLARATOR, self.FOLLOW_VAR_DECLARATOR_in_variableDeclarator2059)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:300:11: (vd0= variableDeclaratorId )
                # JavaTreeParser.g:300:12: vd0= variableDeclaratorId
                pass 
                self._state.following.append(self.FOLLOW_variableDeclaratorId_in_variableDeclarator2074)
                vd0 = self.variableDeclaratorId()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    value = ex(left=vd0, format="${left}") 




                # JavaTreeParser.g:302:11: (vi0= variableInitializer )?
                alt41 = 2
                LA41_0 = self.input.LA(1)

                if (LA41_0 == ARRAY_INITIALIZER or LA41_0 == EXPR) :
                    alt41 = 1
                if alt41 == 1:
                    # JavaTreeParser.g:302:12: vi0= variableInitializer
                    pass 
                    self._state.following.append(self.FOLLOW_variableInitializer_in_variableDeclarator2103)
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
    # JavaTreeParser.g:308:1: variableDeclaratorId returns [value] : ^( IDENT ( arrayDeclaratorList )? ) ;
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

                # JavaTreeParser.g:310:5: ( ^( IDENT ( arrayDeclaratorList )? ) )
                # JavaTreeParser.g:310:9: ^( IDENT ( arrayDeclaratorList )? )
                pass 
                IDENT1=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_variableDeclaratorId2162)

                if self._state.backtracking == 0:
                                
                    expr = ex(self.altIdent(IDENT1.text), format="${left}", rename=True, ident=IDENT1.text)
                    value.update(expr)
                                


                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:315:11: ( arrayDeclaratorList )?
                    alt42 = 2
                    LA42_0 = self.input.LA(1)

                    if (LA42_0 == ARRAY_DECLARATOR_LIST) :
                        alt42 = 1
                    if alt42 == 1:
                        # JavaTreeParser.g:315:12: arrayDeclaratorList
                        pass 
                        self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_variableDeclaratorId2188)
                        self.arrayDeclaratorList()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            value.update(format="${left}", array=True) 





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
    # JavaTreeParser.g:320:1: variableInitializer returns [value] : (ai0= arrayInitializer | ex0= expression );
    def variableInitializer(self, ):

        value = None
        variableInitializer_StartIndex = self.input.index()
        ai0 = None

        ex0 = None


        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 19):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:321:5: (ai0= arrayInitializer | ex0= expression )
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
                    # JavaTreeParser.g:321:9: ai0= arrayInitializer
                    pass 
                    self._state.following.append(self.FOLLOW_arrayInitializer_in_variableInitializer2228)
                    ai0 = self.arrayInitializer()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex(ai0, format="[${left}]") 



                elif alt43 == 2:
                    # JavaTreeParser.g:322:9: ex0= expression
                    pass 
                    self._state.following.append(self.FOLLOW_expression_in_variableInitializer2242)
                    ex0 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex0 




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
    # JavaTreeParser.g:326:1: arrayDeclarator : LBRACK RBRACK ;
    def arrayDeclarator(self, ):

        arrayDeclarator_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 20):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:327:5: ( LBRACK RBRACK )
                # JavaTreeParser.g:327:9: LBRACK RBRACK
                pass 
                self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_arrayDeclarator2270)
                self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_arrayDeclarator2272)




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

    class arrayDeclaratorList_return(TreeRuleReturnScope):
        def __init__(self):
            TreeRuleReturnScope.__init__(self)

            self.values = None




    # $ANTLR start "arrayDeclaratorList"
    # JavaTreeParser.g:331:1: arrayDeclaratorList returns [values] : ^( ARRAY_DECLARATOR_LIST ( ARRAY_DECLARATOR )* ) ;
    def arrayDeclaratorList(self, ):

        retval = self.arrayDeclaratorList_return()
        retval.start = self.input.LT(1)
        arrayDeclaratorList_StartIndex = self.input.index()
        retval.values = [] 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 21):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # JavaTreeParser.g:332:5: ( ^( ARRAY_DECLARATOR_LIST ( ARRAY_DECLARATOR )* ) )
                # JavaTreeParser.g:332:9: ^( ARRAY_DECLARATOR_LIST ( ARRAY_DECLARATOR )* )
                pass 
                self.match(self.input, ARRAY_DECLARATOR_LIST, self.FOLLOW_ARRAY_DECLARATOR_LIST_in_arrayDeclaratorList2302)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:332:33: ( ARRAY_DECLARATOR )*
                    while True: #loop44
                        alt44 = 2
                        LA44_0 = self.input.LA(1)

                        if (LA44_0 == ARRAY_DECLARATOR) :
                            alt44 = 1


                        if alt44 == 1:
                            # JavaTreeParser.g:332:34: ARRAY_DECLARATOR
                            pass 
                            self.match(self.input, ARRAY_DECLARATOR, self.FOLLOW_ARRAY_DECLARATOR_in_arrayDeclaratorList2305)
                            if self._state.backtracking == 0:
                                retval.values.append(self.input.toString(retval.start, self.input.LT(-1))) 



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

        return retval

    # $ANTLR end "arrayDeclaratorList"


    # $ANTLR start "arrayInitializer"
    # JavaTreeParser.g:336:1: arrayInitializer returns [value] : ^( ARRAY_INITIALIZER (v0= variableInitializer )* ) ;
    def arrayInitializer(self, ):

        value = None
        arrayInitializer_StartIndex = self.input.index()
        v0 = None


        value, format = "", "${right}" 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 22):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:337:5: ( ^( ARRAY_INITIALIZER (v0= variableInitializer )* ) )
                # JavaTreeParser.g:337:9: ^( ARRAY_INITIALIZER (v0= variableInitializer )* )
                pass 
                self.match(self.input, ARRAY_INITIALIZER, self.FOLLOW_ARRAY_INITIALIZER_in_arrayInitializer2340)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:338:13: (v0= variableInitializer )*
                    while True: #loop45
                        alt45 = 2
                        LA45_0 = self.input.LA(1)

                        if (LA45_0 == ARRAY_INITIALIZER or LA45_0 == EXPR) :
                            alt45 = 1


                        if alt45 == 1:
                            # JavaTreeParser.g:338:14: v0= variableInitializer
                            pass 
                            self._state.following.append(self.FOLLOW_variableInitializer_in_arrayInitializer2357)
                            v0 = self.variableInitializer()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                value, format = ex(value, v0, format), "${left}, ${right}" 



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
    # JavaTreeParser.g:345:1: throwsClause : ^( THROWS_CLAUSE ( qualifiedIdentifier )+ ) ;
    def throwsClause(self, ):

        throwsClause_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 23):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:346:5: ( ^( THROWS_CLAUSE ( qualifiedIdentifier )+ ) )
                # JavaTreeParser.g:346:9: ^( THROWS_CLAUSE ( qualifiedIdentifier )+ )
                pass 
                self.match(self.input, THROWS_CLAUSE, self.FOLLOW_THROWS_CLAUSE_in_throwsClause2417)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:346:25: ( qualifiedIdentifier )+
                cnt46 = 0
                while True: #loop46
                    alt46 = 2
                    LA46_0 = self.input.LA(1)

                    if (LA46_0 == DOT or LA46_0 == IDENT) :
                        alt46 = 1


                    if alt46 == 1:
                        # JavaTreeParser.g:0:0: qualifiedIdentifier
                        pass 
                        self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_throwsClause2419)
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
    # JavaTreeParser.g:350:1: modifierList returns [values] : ^( MODIFIER_LIST (md0= modifier )* ) ;
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

                # JavaTreeParser.g:352:5: ( ^( MODIFIER_LIST (md0= modifier )* ) )
                # JavaTreeParser.g:352:9: ^( MODIFIER_LIST (md0= modifier )* )
                pass 
                self.match(self.input, MODIFIER_LIST, self.FOLLOW_MODIFIER_LIST_in_modifierList2455)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:352:25: (md0= modifier )*
                    while True: #loop47
                        alt47 = 2
                        LA47_0 = self.input.LA(1)

                        if (LA47_0 == AT or LA47_0 == ABSTRACT or LA47_0 == FINAL or LA47_0 == NATIVE or (PRIVATE <= LA47_0 <= PUBLIC) or (STATIC <= LA47_0 <= STRICTFP) or LA47_0 == SYNCHRONIZED or LA47_0 == TRANSIENT or LA47_0 == VOLATILE) :
                            alt47 = 1


                        if alt47 == 1:
                            # JavaTreeParser.g:352:26: md0= modifier
                            pass 
                            self._state.following.append(self.FOLLOW_modifier_in_modifierList2460)
                            md0 = self.modifier()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                values.append(((md0 is not None) and [md0.value] or [None])[0]) 



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

            self.value = None




    # $ANTLR start "modifier"
    # JavaTreeParser.g:356:1: modifier returns [value] : ( PUBLIC | PROTECTED | PRIVATE | STATIC | ABSTRACT | NATIVE | SYNCHRONIZED | TRANSIENT | VOLATILE | STRICTFP | lm0= localModifier );
    def modifier(self, ):

        retval = self.modifier_return()
        retval.start = self.input.LT(1)
        modifier_StartIndex = self.input.index()
        lm0 = None


        retval.value = ex(format="${left}") 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 25):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # JavaTreeParser.g:358:5: ( PUBLIC | PROTECTED | PRIVATE | STATIC | ABSTRACT | NATIVE | SYNCHRONIZED | TRANSIENT | VOLATILE | STRICTFP | lm0= localModifier )
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
                    # JavaTreeParser.g:358:9: PUBLIC
                    pass 
                    self.match(self.input, PUBLIC, self.FOLLOW_PUBLIC_in_modifier2498)
                    if self._state.backtracking == 0:
                        retval.value.update(left=self.input.toString(retval.start, self.input.LT(-1))) 



                elif alt48 == 2:
                    # JavaTreeParser.g:359:9: PROTECTED
                    pass 
                    self.match(self.input, PROTECTED, self.FOLLOW_PROTECTED_in_modifier2521)
                    if self._state.backtracking == 0:
                        retval.value.update(left=self.input.toString(retval.start, self.input.LT(-1))) 



                elif alt48 == 3:
                    # JavaTreeParser.g:360:9: PRIVATE
                    pass 
                    self.match(self.input, PRIVATE, self.FOLLOW_PRIVATE_in_modifier2541)
                    if self._state.backtracking == 0:
                        retval.value.update(left=self.input.toString(retval.start, self.input.LT(-1))) 



                elif alt48 == 4:
                    # JavaTreeParser.g:361:9: STATIC
                    pass 
                    self.match(self.input, STATIC, self.FOLLOW_STATIC_in_modifier2563)
                    if self._state.backtracking == 0:
                        retval.value.update(left=self.input.toString(retval.start, self.input.LT(-1))) 



                elif alt48 == 5:
                    # JavaTreeParser.g:362:9: ABSTRACT
                    pass 
                    self.match(self.input, ABSTRACT, self.FOLLOW_ABSTRACT_in_modifier2586)
                    if self._state.backtracking == 0:
                        retval.value.update(left=self.input.toString(retval.start, self.input.LT(-1))) 



                elif alt48 == 6:
                    # JavaTreeParser.g:363:9: NATIVE
                    pass 
                    self.match(self.input, NATIVE, self.FOLLOW_NATIVE_in_modifier2607)
                    if self._state.backtracking == 0:
                        retval.value.update(left=self.input.toString(retval.start, self.input.LT(-1))) 



                elif alt48 == 7:
                    # JavaTreeParser.g:364:9: SYNCHRONIZED
                    pass 
                    self.match(self.input, SYNCHRONIZED, self.FOLLOW_SYNCHRONIZED_in_modifier2630)
                    if self._state.backtracking == 0:
                        retval.value.update(left=self.input.toString(retval.start, self.input.LT(-1))) 



                elif alt48 == 8:
                    # JavaTreeParser.g:365:9: TRANSIENT
                    pass 
                    self.match(self.input, TRANSIENT, self.FOLLOW_TRANSIENT_in_modifier2647)
                    if self._state.backtracking == 0:
                        retval.value.update(left=self.input.toString(retval.start, self.input.LT(-1))) 



                elif alt48 == 9:
                    # JavaTreeParser.g:366:9: VOLATILE
                    pass 
                    self.match(self.input, VOLATILE, self.FOLLOW_VOLATILE_in_modifier2667)
                    if self._state.backtracking == 0:
                        retval.value.update(left=self.input.toString(retval.start, self.input.LT(-1))) 



                elif alt48 == 10:
                    # JavaTreeParser.g:367:9: STRICTFP
                    pass 
                    self.match(self.input, STRICTFP, self.FOLLOW_STRICTFP_in_modifier2688)
                    if self._state.backtracking == 0:
                        retval.value.update(left=self.input.toString(retval.start, self.input.LT(-1))) 



                elif alt48 == 11:
                    # JavaTreeParser.g:368:9: lm0= localModifier
                    pass 
                    self._state.following.append(self.FOLLOW_localModifier_in_modifier2711)
                    lm0 = self.localModifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        retval.value = lm0 




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
    # JavaTreeParser.g:372:1: localModifierList returns [values] : ^( LOCAL_MODIFIER_LIST (md0= localModifier )* ) ;
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

                # JavaTreeParser.g:374:5: ( ^( LOCAL_MODIFIER_LIST (md0= localModifier )* ) )
                # JavaTreeParser.g:374:9: ^( LOCAL_MODIFIER_LIST (md0= localModifier )* )
                pass 
                self.match(self.input, LOCAL_MODIFIER_LIST, self.FOLLOW_LOCAL_MODIFIER_LIST_in_localModifierList2747)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:374:31: (md0= localModifier )*
                    while True: #loop49
                        alt49 = 2
                        LA49_0 = self.input.LA(1)

                        if (LA49_0 == AT or LA49_0 == FINAL) :
                            alt49 = 1


                        if alt49 == 1:
                            # JavaTreeParser.g:374:32: md0= localModifier
                            pass 
                            self._state.following.append(self.FOLLOW_localModifier_in_localModifierList2752)
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
    # JavaTreeParser.g:378:1: localModifier returns [value] : ( FINAL | an0= annotation );
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

                # JavaTreeParser.g:379:5: ( FINAL | an0= annotation )
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
                    # JavaTreeParser.g:379:9: FINAL
                    pass 
                    self.match(self.input, FINAL, self.FOLLOW_FINAL_in_localModifier2781)
                    if self._state.backtracking == 0:
                        value = "final" 



                elif alt50 == 2:
                    # JavaTreeParser.g:380:9: an0= annotation
                    pass 
                    self._state.following.append(self.FOLLOW_annotation_in_localModifier2795)
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
    # JavaTreeParser.g:384:1: type returns [value] : ^( TYPE (pt0= primitiveType | qt0= qualifiedTypeIdent ) ( arrayDeclaratorList )? ) ;
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

                # JavaTreeParser.g:386:5: ( ^( TYPE (pt0= primitiveType | qt0= qualifiedTypeIdent ) ( arrayDeclaratorList )? ) )
                # JavaTreeParser.g:386:9: ^( TYPE (pt0= primitiveType | qt0= qualifiedTypeIdent ) ( arrayDeclaratorList )? )
                pass 
                self.match(self.input, TYPE, self.FOLLOW_TYPE_in_type2831)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:387:11: (pt0= primitiveType | qt0= qualifiedTypeIdent )
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
                    # JavaTreeParser.g:387:12: pt0= primitiveType
                    pass 
                    self._state.following.append(self.FOLLOW_primitiveType_in_type2846)
                    pt0 = self.primitiveType()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        retval.value.update(left=self.renameType(((pt0 is not None) and [self.input.getTokenStream().toString(
                            self.input.getTreeAdaptor().getTokenStartIndex(pt0.start),
                            self.input.getTreeAdaptor().getTokenStopIndex(pt0.start)
                            )] or [None])[0])) 



                elif alt51 == 2:
                    # JavaTreeParser.g:388:12: qt0= qualifiedTypeIdent
                    pass 
                    self._state.following.append(self.FOLLOW_qualifiedTypeIdent_in_type2865)
                    qt0 = self.qualifiedTypeIdent()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        retval.value.update(left=self.renameType(qt0)) 




                # JavaTreeParser.g:389:11: ( arrayDeclaratorList )?
                alt52 = 2
                LA52_0 = self.input.LA(1)

                if (LA52_0 == ARRAY_DECLARATOR_LIST) :
                    alt52 = 1
                if alt52 == 1:
                    # JavaTreeParser.g:389:12: arrayDeclaratorList
                    pass 
                    self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_type2881)
                    self.arrayDeclaratorList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        retval.value["array"] = True 





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
    # JavaTreeParser.g:396:1: qualifiedTypeIdent returns [value] : ^( QUALIFIED_TYPE_IDENT (ti0= typeIdent )+ ) ;
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

                # JavaTreeParser.g:397:5: ( ^( QUALIFIED_TYPE_IDENT (ti0= typeIdent )+ ) )
                # JavaTreeParser.g:397:9: ^( QUALIFIED_TYPE_IDENT (ti0= typeIdent )+ )
                pass 
                self.match(self.input, QUALIFIED_TYPE_IDENT, self.FOLLOW_QUALIFIED_TYPE_IDENT_in_qualifiedTypeIdent2942)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:397:32: (ti0= typeIdent )+
                cnt53 = 0
                while True: #loop53
                    alt53 = 2
                    LA53_0 = self.input.LA(1)

                    if (LA53_0 == IDENT) :
                        alt53 = 1


                    if alt53 == 1:
                        # JavaTreeParser.g:397:33: ti0= typeIdent
                        pass 
                        self._state.following.append(self.FOLLOW_typeIdent_in_qualifiedTypeIdent2947)
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
    # JavaTreeParser.g:401:1: typeIdent returns [value] : ^(id0= IDENT ( genericTypeArgumentList )? ) ;
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

                # JavaTreeParser.g:402:5: ( ^(id0= IDENT ( genericTypeArgumentList )? ) )
                # JavaTreeParser.g:402:9: ^(id0= IDENT ( genericTypeArgumentList )? )
                pass 
                id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_typeIdent2979)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:402:21: ( genericTypeArgumentList )?
                    alt54 = 2
                    LA54_0 = self.input.LA(1)

                    if (LA54_0 == GENERIC_TYPE_ARG_LIST) :
                        alt54 = 1
                    if alt54 == 1:
                        # JavaTreeParser.g:0:0: genericTypeArgumentList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeArgumentList_in_typeIdent2981)
                        self.genericTypeArgumentList()

                        self._state.following.pop()




                    self.match(self.input, UP, None)

                if self._state.backtracking == 0:
                    value = self.renameType(id0.text) 





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
    # JavaTreeParser.g:406:1: primitiveType : ( BOOLEAN | CHAR | BYTE | SHORT | INT | LONG | FLOAT | DOUBLE );
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

                # JavaTreeParser.g:407:5: ( BOOLEAN | CHAR | BYTE | SHORT | INT | LONG | FLOAT | DOUBLE )
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
    # JavaTreeParser.g:418:1: genericTypeArgumentList returns [values] : ^( GENERIC_TYPE_ARG_LIST ( genericTypeArgument )+ ) ;
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

                # JavaTreeParser.g:419:5: ( ^( GENERIC_TYPE_ARG_LIST ( genericTypeArgument )+ ) )
                # JavaTreeParser.g:419:9: ^( GENERIC_TYPE_ARG_LIST ( genericTypeArgument )+ )
                pass 
                self.match(self.input, GENERIC_TYPE_ARG_LIST, self.FOLLOW_GENERIC_TYPE_ARG_LIST_in_genericTypeArgumentList3100)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:419:33: ( genericTypeArgument )+
                cnt55 = 0
                while True: #loop55
                    alt55 = 2
                    LA55_0 = self.input.LA(1)

                    if (LA55_0 == QUESTION or LA55_0 == TYPE) :
                        alt55 = 1


                    if alt55 == 1:
                        # JavaTreeParser.g:0:0: genericTypeArgument
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeArgument_in_genericTypeArgumentList3102)
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
    # JavaTreeParser.g:423:1: genericTypeArgument : ( type | ^( QUESTION ( genericWildcardBoundType )? ) );
    def genericTypeArgument(self, ):

        genericTypeArgument_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 33):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:424:5: ( type | ^( QUESTION ( genericWildcardBoundType )? ) )
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
                    # JavaTreeParser.g:424:9: type
                    pass 
                    self._state.following.append(self.FOLLOW_type_in_genericTypeArgument3124)
                    self.type()

                    self._state.following.pop()


                elif alt57 == 2:
                    # JavaTreeParser.g:425:9: ^( QUESTION ( genericWildcardBoundType )? )
                    pass 
                    self.match(self.input, QUESTION, self.FOLLOW_QUESTION_in_genericTypeArgument3135)

                    if self.input.LA(1) == DOWN:
                        self.match(self.input, DOWN, None)
                        # JavaTreeParser.g:425:20: ( genericWildcardBoundType )?
                        alt56 = 2
                        LA56_0 = self.input.LA(1)

                        if (LA56_0 == EXTENDS or LA56_0 == SUPER) :
                            alt56 = 1
                        if alt56 == 1:
                            # JavaTreeParser.g:0:0: genericWildcardBoundType
                            pass 
                            self._state.following.append(self.FOLLOW_genericWildcardBoundType_in_genericTypeArgument3137)
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
    # JavaTreeParser.g:429:1: genericWildcardBoundType : ( ^( EXTENDS type ) | ^( SUPER type ) );
    def genericWildcardBoundType(self, ):

        genericWildcardBoundType_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 34):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:430:5: ( ^( EXTENDS type ) | ^( SUPER type ) )
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
                    # JavaTreeParser.g:430:9: ^( EXTENDS type )
                    pass 
                    self.match(self.input, EXTENDS, self.FOLLOW_EXTENDS_in_genericWildcardBoundType3160)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_type_in_genericWildcardBoundType3162)
                    self.type()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt58 == 2:
                    # JavaTreeParser.g:431:9: ^( SUPER type )
                    pass 
                    self.match(self.input, SUPER, self.FOLLOW_SUPER_in_genericWildcardBoundType3174)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_type_in_genericWildcardBoundType3176)
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
    # JavaTreeParser.g:435:1: formalParameterList returns [values] : ^( FORMAL_PARAM_LIST (fp0= formalParameterStandardDecl )* (vd0= formalParameterVarargDecl )? ) ;
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

                # JavaTreeParser.g:437:5: ( ^( FORMAL_PARAM_LIST (fp0= formalParameterStandardDecl )* (vd0= formalParameterVarargDecl )? ) )
                # JavaTreeParser.g:437:9: ^( FORMAL_PARAM_LIST (fp0= formalParameterStandardDecl )* (vd0= formalParameterVarargDecl )? )
                pass 
                self.match(self.input, FORMAL_PARAM_LIST, self.FOLLOW_FORMAL_PARAM_LIST_in_formalParameterList3211)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:438:11: (fp0= formalParameterStandardDecl )*
                    while True: #loop59
                        alt59 = 2
                        LA59_0 = self.input.LA(1)

                        if (LA59_0 == FORMAL_PARAM_STD_DECL) :
                            alt59 = 1


                        if alt59 == 1:
                            # JavaTreeParser.g:438:12: fp0= formalParameterStandardDecl
                            pass 
                            self._state.following.append(self.FOLLOW_formalParameterStandardDecl_in_formalParameterList3226)
                            fp0 = self.formalParameterStandardDecl()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                values.append(fp0) 



                        else:
                            break #loop59


                    # JavaTreeParser.g:439:11: (vd0= formalParameterVarargDecl )?
                    alt60 = 2
                    LA60_0 = self.input.LA(1)

                    if (LA60_0 == FORMAL_PARAM_VARARG_DECL) :
                        alt60 = 1
                    if alt60 == 1:
                        # JavaTreeParser.g:439:12: vd0= formalParameterVarargDecl
                        pass 
                        self._state.following.append(self.FOLLOW_formalParameterVarargDecl_in_formalParameterList3245)
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
    # JavaTreeParser.g:444:1: formalParameterStandardDecl returns [value] : ^( FORMAL_PARAM_STD_DECL lm0= localModifierList tp0= type vd0= variableDeclaratorId ) ;
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

                # JavaTreeParser.g:445:5: ( ^( FORMAL_PARAM_STD_DECL lm0= localModifierList tp0= type vd0= variableDeclaratorId ) )
                # JavaTreeParser.g:445:9: ^( FORMAL_PARAM_STD_DECL lm0= localModifierList tp0= type vd0= variableDeclaratorId )
                pass 
                self.match(self.input, FORMAL_PARAM_STD_DECL, self.FOLLOW_FORMAL_PARAM_STD_DECL_in_formalParameterStandardDecl3286)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_localModifierList_in_formalParameterStandardDecl3300)
                lm0 = self.localModifierList()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_type_in_formalParameterStandardDecl3314)
                tp0 = self.type()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_variableDeclaratorId_in_formalParameterStandardDecl3328)
                vd0 = self.variableDeclaratorId()

                self._state.following.pop()

                self.match(self.input, UP, None)
                if self._state.backtracking == 0:
                    value = px(vd0["ident"], ((tp0 is not None) and [self.input.getTokenStream().toString(
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
    # JavaTreeParser.g:453:1: formalParameterVarargDecl returns [value] : ^( FORMAL_PARAM_VARARG_DECL lm0= localModifierList tp0= type vd0= variableDeclaratorId ) ;
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

                # JavaTreeParser.g:454:5: ( ^( FORMAL_PARAM_VARARG_DECL lm0= localModifierList tp0= type vd0= variableDeclaratorId ) )
                # JavaTreeParser.g:454:9: ^( FORMAL_PARAM_VARARG_DECL lm0= localModifierList tp0= type vd0= variableDeclaratorId )
                pass 
                self.match(self.input, FORMAL_PARAM_VARARG_DECL, self.FOLLOW_FORMAL_PARAM_VARARG_DECL_in_formalParameterVarargDecl3365)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_localModifierList_in_formalParameterVarargDecl3379)
                lm0 = self.localModifierList()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_type_in_formalParameterVarargDecl3393)
                tp0 = self.type()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_variableDeclaratorId_in_formalParameterVarargDecl3407)
                vd0 = self.variableDeclaratorId()

                self._state.following.pop()

                self.match(self.input, UP, None)
                if self._state.backtracking == 0:
                    value = px(vd0["ident"], ((tp0 is not None) and [self.input.getTokenStream().toString(
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
    # JavaTreeParser.g:462:1: qualifiedIdentifier returns [value] : ( IDENT | ^( DOT qi0= qualifiedIdentifier IDENT ) );
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

                # JavaTreeParser.g:463:5: ( IDENT | ^( DOT qi0= qualifiedIdentifier IDENT ) )
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
                    # JavaTreeParser.g:463:9: IDENT
                    pass 
                    IDENT2=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_qualifiedIdentifier3443)
                    if self._state.backtracking == 0:
                        value = ex(IDENT2.text, format="${left}", rename=True) 



                elif alt61 == 2:
                    # JavaTreeParser.g:465:9: ^( DOT qi0= qualifiedIdentifier IDENT )
                    pass 
                    self.match(self.input, DOT, self.FOLLOW_DOT_in_qualifiedIdentifier3464)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_qualifiedIdentifier3478)
                    qi0 = self.qualifiedIdentifier()

                    self._state.following.pop()
                    IDENT3=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_qualifiedIdentifier3490)
                    if self._state.backtracking == 0:
                        value = ex(qi0,
                                    IDENT3.text,
                                    format="${left}.${right}",
                                    rename=True)
                                  


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
    # JavaTreeParser.g:477:1: annotationList : ^( ANNOTATION_LIST ( annotation )* ) ;
    def annotationList(self, ):

        annotationList_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 39):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:478:5: ( ^( ANNOTATION_LIST ( annotation )* ) )
                # JavaTreeParser.g:478:9: ^( ANNOTATION_LIST ( annotation )* )
                pass 
                self.match(self.input, ANNOTATION_LIST, self.FOLLOW_ANNOTATION_LIST_in_annotationList3533)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:478:27: ( annotation )*
                    while True: #loop62
                        alt62 = 2
                        LA62_0 = self.input.LA(1)

                        if (LA62_0 == AT) :
                            alt62 = 1


                        if alt62 == 1:
                            # JavaTreeParser.g:0:0: annotation
                            pass 
                            self._state.following.append(self.FOLLOW_annotation_in_annotationList3535)
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
    # JavaTreeParser.g:482:1: annotation returns [value] : ^( AT qi0= qualifiedIdentifier (ai0= annotationInit )? ) ;
    def annotation(self, ):

        value = None
        annotation_StartIndex = self.input.index()
        qi0 = None

        ai0 = None


        value = ex(format="${left}()") 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 40):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:484:5: ( ^( AT qi0= qualifiedIdentifier (ai0= annotationInit )? ) )
                # JavaTreeParser.g:484:9: ^( AT qi0= qualifiedIdentifier (ai0= annotationInit )? )
                pass 
                self.match(self.input, AT, self.FOLLOW_AT_in_annotation3571)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_annotation3585)
                qi0 = self.qualifiedIdentifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    value.update(left=qi0, annotation=True) 

                # JavaTreeParser.g:486:11: (ai0= annotationInit )?
                alt63 = 2
                LA63_0 = self.input.LA(1)

                if (LA63_0 == ANNOTATION_INIT_BLOCK) :
                    alt63 = 1
                if alt63 == 1:
                    # JavaTreeParser.g:486:12: ai0= annotationInit
                    pass 
                    self._state.following.append(self.FOLLOW_annotationInit_in_annotation3602)
                    ai0 = self.annotationInit()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        right = ", ".join(self.formatExpression(v) for v in ai0)
                        value.update(right=right, format="${left}(${right})") 





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
    # JavaTreeParser.g:494:1: annotationInit returns [values] : ^( ANNOTATION_INIT_BLOCK ai0= annotationInitializers ) ;
    def annotationInit(self, ):

        values = None
        annotationInit_StartIndex = self.input.index()
        ai0 = None


        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 41):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return values

                # JavaTreeParser.g:495:5: ( ^( ANNOTATION_INIT_BLOCK ai0= annotationInitializers ) )
                # JavaTreeParser.g:495:9: ^( ANNOTATION_INIT_BLOCK ai0= annotationInitializers )
                pass 
                self.match(self.input, ANNOTATION_INIT_BLOCK, self.FOLLOW_ANNOTATION_INIT_BLOCK_in_annotationInit3663)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_annotationInitializers_in_annotationInit3667)
                ai0 = self.annotationInitializers()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    values = ai0 


                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 41, annotationInit_StartIndex, success)

            pass

        return values

    # $ANTLR end "annotationInit"


    # $ANTLR start "annotationInitializers"
    # JavaTreeParser.g:499:1: annotationInitializers returns [values] : ( ^( ANNOTATION_INIT_KEY_LIST (ai0= annotationInitializer )+ ) | ^( ANNOTATION_INIT_DEFAULT_KEY annotationElementValue ) );
    def annotationInitializers(self, ):

        values = None
        annotationInitializers_StartIndex = self.input.index()
        ai0 = None


        values = [] 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 42):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return values

                # JavaTreeParser.g:501:5: ( ^( ANNOTATION_INIT_KEY_LIST (ai0= annotationInitializer )+ ) | ^( ANNOTATION_INIT_DEFAULT_KEY annotationElementValue ) )
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
                    # JavaTreeParser.g:501:9: ^( ANNOTATION_INIT_KEY_LIST (ai0= annotationInitializer )+ )
                    pass 
                    self.match(self.input, ANNOTATION_INIT_KEY_LIST, self.FOLLOW_ANNOTATION_INIT_KEY_LIST_in_annotationInitializers3704)

                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:501:36: (ai0= annotationInitializer )+
                    cnt64 = 0
                    while True: #loop64
                        alt64 = 2
                        LA64_0 = self.input.LA(1)

                        if (LA64_0 == IDENT) :
                            alt64 = 1


                        if alt64 == 1:
                            # JavaTreeParser.g:501:37: ai0= annotationInitializer
                            pass 
                            self._state.following.append(self.FOLLOW_annotationInitializer_in_annotationInitializers3709)
                            ai0 = self.annotationInitializer()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                values.append(ai0) 



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
                    # JavaTreeParser.g:502:9: ^( ANNOTATION_INIT_DEFAULT_KEY annotationElementValue )
                    pass 
                    self.match(self.input, ANNOTATION_INIT_DEFAULT_KEY, self.FOLLOW_ANNOTATION_INIT_DEFAULT_KEY_in_annotationInitializers3725)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_annotationElementValue_in_annotationInitializers3727)
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

        return values

    # $ANTLR end "annotationInitializers"


    # $ANTLR start "annotationInitializer"
    # JavaTreeParser.g:506:1: annotationInitializer returns [value] : ^(id0= IDENT ae0= annotationElementValue ) ;
    def annotationInitializer(self, ):

        value = None
        annotationInitializer_StartIndex = self.input.index()
        id0 = None
        ae0 = None


        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 43):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:507:5: ( ^(id0= IDENT ae0= annotationElementValue ) )
                # JavaTreeParser.g:507:9: ^(id0= IDENT ae0= annotationElementValue )
                pass 
                id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_annotationInitializer3755)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_annotationElementValue_in_annotationInitializer3759)
                ae0 = self.annotationElementValue()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    value = ex(left=self.renameIdent(id0.text),
                                right=ae0,
                                format="${left}=${right}") 


                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 43, annotationInitializer_StartIndex, success)

            pass

        return value

    # $ANTLR end "annotationInitializer"


    # $ANTLR start "annotationElementValue"
    # JavaTreeParser.g:514:1: annotationElementValue returns [value] : ( ^( ANNOTATION_INIT_ARRAY_ELEMENT ( annotationElementValue )* ) | annotation | ex0= expression );
    def annotationElementValue(self, ):

        value = None
        annotationElementValue_StartIndex = self.input.index()
        ex0 = None


        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 44):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:515:5: ( ^( ANNOTATION_INIT_ARRAY_ELEMENT ( annotationElementValue )* ) | annotation | ex0= expression )
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
                    # JavaTreeParser.g:515:9: ^( ANNOTATION_INIT_ARRAY_ELEMENT ( annotationElementValue )* )
                    pass 
                    self.match(self.input, ANNOTATION_INIT_ARRAY_ELEMENT, self.FOLLOW_ANNOTATION_INIT_ARRAY_ELEMENT_in_annotationElementValue3797)

                    if self.input.LA(1) == DOWN:
                        self.match(self.input, DOWN, None)
                        # JavaTreeParser.g:515:41: ( annotationElementValue )*
                        while True: #loop66
                            alt66 = 2
                            LA66_0 = self.input.LA(1)

                            if (LA66_0 == AT or LA66_0 == ANNOTATION_INIT_ARRAY_ELEMENT or LA66_0 == EXPR) :
                                alt66 = 1


                            if alt66 == 1:
                                # JavaTreeParser.g:0:0: annotationElementValue
                                pass 
                                self._state.following.append(self.FOLLOW_annotationElementValue_in_annotationElementValue3799)
                                self.annotationElementValue()

                                self._state.following.pop()


                            else:
                                break #loop66



                        self.match(self.input, UP, None)



                elif alt67 == 2:
                    # JavaTreeParser.g:516:9: annotation
                    pass 
                    self._state.following.append(self.FOLLOW_annotation_in_annotationElementValue3811)
                    self.annotation()

                    self._state.following.pop()


                elif alt67 == 3:
                    # JavaTreeParser.g:517:9: ex0= expression
                    pass 
                    self._state.following.append(self.FOLLOW_expression_in_annotationElementValue3823)
                    ex0 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex0 




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 44, annotationElementValue_StartIndex, success)

            pass

        return value

    # $ANTLR end "annotationElementValue"


    # $ANTLR start "annotationTopLevelScope"
    # JavaTreeParser.g:521:1: annotationTopLevelScope : ^( ANNOTATION_TOP_LEVEL_SCOPE ( annotationScopeDeclarations )* ) ;
    def annotationTopLevelScope(self, ):

        annotationTopLevelScope_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 45):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:522:5: ( ^( ANNOTATION_TOP_LEVEL_SCOPE ( annotationScopeDeclarations )* ) )
                # JavaTreeParser.g:522:9: ^( ANNOTATION_TOP_LEVEL_SCOPE ( annotationScopeDeclarations )* )
                pass 
                self.match(self.input, ANNOTATION_TOP_LEVEL_SCOPE, self.FOLLOW_ANNOTATION_TOP_LEVEL_SCOPE_in_annotationTopLevelScope3846)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:522:38: ( annotationScopeDeclarations )*
                    while True: #loop68
                        alt68 = 2
                        LA68_0 = self.input.LA(1)

                        if (LA68_0 == AT or LA68_0 == CLASS or LA68_0 == ENUM or LA68_0 == INTERFACE or LA68_0 == ANNOTATION_METHOD_DECL or LA68_0 == VAR_DECLARATION) :
                            alt68 = 1


                        if alt68 == 1:
                            # JavaTreeParser.g:0:0: annotationScopeDeclarations
                            pass 
                            self._state.following.append(self.FOLLOW_annotationScopeDeclarations_in_annotationTopLevelScope3848)
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
    # JavaTreeParser.g:526:1: annotationScopeDeclarations : ( ^( ANNOTATION_METHOD_DECL md0= modifierList tp0= type id0= IDENT (ad0= annotationDefaultValue )? ) | ^( VAR_DECLARATION md1= modifierList tp1= type vd1= variableDeclaratorList ) | typeDeclaration );
    def annotationScopeDeclarations(self, ):

        annotationScopeDeclarations_StartIndex = self.input.index()
        id0 = None
        md0 = None

        tp0 = None

        ad0 = None

        md1 = None

        tp1 = None

        vd1 = None


        default = None 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 46):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:528:5: ( ^( ANNOTATION_METHOD_DECL md0= modifierList tp0= type id0= IDENT (ad0= annotationDefaultValue )? ) | ^( VAR_DECLARATION md1= modifierList tp1= type vd1= variableDeclaratorList ) | typeDeclaration )
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
                    # JavaTreeParser.g:528:9: ^( ANNOTATION_METHOD_DECL md0= modifierList tp0= type id0= IDENT (ad0= annotationDefaultValue )? )
                    pass 
                    self.match(self.input, ANNOTATION_METHOD_DECL, self.FOLLOW_ANNOTATION_METHOD_DECL_in_annotationScopeDeclarations3880)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_annotationScopeDeclarations3894)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_type_in_annotationScopeDeclarations3908)
                    tp0 = self.type()

                    self._state.following.pop()
                    id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_annotationScopeDeclarations3922)
                    # JavaTreeParser.g:532:11: (ad0= annotationDefaultValue )?
                    alt69 = 2
                    LA69_0 = self.input.LA(1)

                    if (LA69_0 == DEFAULT) :
                        alt69 = 1
                    if alt69 == 1:
                        # JavaTreeParser.g:532:12: ad0= annotationDefaultValue
                        pass 
                        self._state.following.append(self.FOLLOW_annotationDefaultValue_in_annotationScopeDeclarations3937)
                        ad0 = self.annotationDefaultValue()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            default = ad0 




                    if self._state.backtracking == 0:
                        self.addAnnotationMethod(md0, ((tp0 is not None) and [tp0.value] or [None])[0], id0.text, default) 


                    self.match(self.input, UP, None)


                elif alt70 == 2:
                    # JavaTreeParser.g:535:9: ^( VAR_DECLARATION md1= modifierList tp1= type vd1= variableDeclaratorList )
                    pass 
                    self.match(self.input, VAR_DECLARATION, self.FOLLOW_VAR_DECLARATION_in_annotationScopeDeclarations3974)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_annotationScopeDeclarations3978)
                    md1 = self.modifierList()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_type_in_annotationScopeDeclarations3982)
                    tp1 = self.type()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_variableDeclaratorList_in_annotationScopeDeclarations3986)
                    vd1 = self.variableDeclaratorList()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        self.addVariables(vd1, ((tp1 is not None) and [tp1.value] or [None])[0], md1, local=True) 



                elif alt70 == 3:
                    # JavaTreeParser.g:537:9: typeDeclaration
                    pass 
                    self._state.following.append(self.FOLLOW_typeDeclaration_in_annotationScopeDeclarations4008)
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
    # JavaTreeParser.g:541:1: annotationDefaultValue returns [value] : ^( DEFAULT ae0= annotationElementValue ) ;
    def annotationDefaultValue(self, ):

        value = None
        annotationDefaultValue_StartIndex = self.input.index()
        ae0 = None


        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 47):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:542:5: ( ^( DEFAULT ae0= annotationElementValue ) )
                # JavaTreeParser.g:542:9: ^( DEFAULT ae0= annotationElementValue )
                pass 
                self.match(self.input, DEFAULT, self.FOLLOW_DEFAULT_in_annotationDefaultValue4033)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_annotationElementValue_in_annotationDefaultValue4037)
                ae0 = self.annotationElementValue()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    value = ae0 


                self.match(self.input, UP, None)




                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 47, annotationDefaultValue_StartIndex, success)

            pass

        return value

    # $ANTLR end "annotationDefaultValue"


    # $ANTLR start "block"
    # JavaTreeParser.g:546:1: block : ^( BLOCK_SCOPE ( blockStatement )* ) ;
    def block(self, ):

        block_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 48):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:547:5: ( ^( BLOCK_SCOPE ( blockStatement )* ) )
                # JavaTreeParser.g:547:9: ^( BLOCK_SCOPE ( blockStatement )* )
                pass 
                self.match(self.input, BLOCK_SCOPE, self.FOLLOW_BLOCK_SCOPE_in_block4061)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:547:23: ( blockStatement )*
                    while True: #loop71
                        alt71 = 2
                        LA71_0 = self.input.LA(1)

                        if (LA71_0 == AT or LA71_0 == SEMI or LA71_0 == ASSERT or LA71_0 == BREAK or (CLASS <= LA71_0 <= CONTINUE) or LA71_0 == DO or LA71_0 == ENUM or (FOR <= LA71_0 <= IF) or LA71_0 == INTERFACE or LA71_0 == RETURN or (SWITCH <= LA71_0 <= SYNCHRONIZED) or LA71_0 == THROW or LA71_0 == TRY or LA71_0 == WHILE or LA71_0 == BLOCK_SCOPE or LA71_0 == EXPR or LA71_0 == FOR_EACH or LA71_0 == LABELED_STATEMENT or LA71_0 == VAR_DECLARATION) :
                            alt71 = 1


                        if alt71 == 1:
                            # JavaTreeParser.g:0:0: blockStatement
                            pass 
                            self._state.following.append(self.FOLLOW_blockStatement_in_block4063)
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

    class blockStatement_return(TreeRuleReturnScope):
        def __init__(self):
            TreeRuleReturnScope.__init__(self)





    # $ANTLR start "blockStatement"
    # JavaTreeParser.g:551:1: blockStatement : ( localVariableDeclaration | typeDeclaration | st0= statement );
    def blockStatement(self, ):

        retval = self.blockStatement_return()
        retval.start = self.input.LT(1)
        blockStatement_StartIndex = self.input.index()
        st0 = None


        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 49):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # JavaTreeParser.g:553:5: ( localVariableDeclaration | typeDeclaration | st0= statement )
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
                    # JavaTreeParser.g:553:9: localVariableDeclaration
                    pass 
                    self._state.following.append(self.FOLLOW_localVariableDeclaration_in_blockStatement4094)
                    self.localVariableDeclaration()

                    self._state.following.pop()


                elif alt72 == 2:
                    # JavaTreeParser.g:554:9: typeDeclaration
                    pass 
                    self._state.following.append(self.FOLLOW_typeDeclaration_in_blockStatement4104)
                    self.typeDeclaration()

                    self._state.following.pop()


                elif alt72 == 3:
                    # JavaTreeParser.g:555:9: st0= statement
                    pass 
                    self._state.following.append(self.FOLLOW_statement_in_blockStatement4116)
                    st0 = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.append(st0) 



                if self._state.backtracking == 0:
                    self.commentHandler(retval.start) 


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 49, blockStatement_StartIndex, success)

            pass

        return retval

    # $ANTLR end "blockStatement"


    # $ANTLR start "localVariableDeclaration"
    # JavaTreeParser.g:559:1: localVariableDeclaration : ^( VAR_DECLARATION md0= localModifierList tp0= type vd0= variableDeclaratorList ) ;
    def localVariableDeclaration(self, ):

        localVariableDeclaration_StartIndex = self.input.index()
        md0 = None

        tp0 = None

        vd0 = None


        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 50):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:560:5: ( ^( VAR_DECLARATION md0= localModifierList tp0= type vd0= variableDeclaratorList ) )
                # JavaTreeParser.g:560:9: ^( VAR_DECLARATION md0= localModifierList tp0= type vd0= variableDeclaratorList )
                pass 
                self.match(self.input, VAR_DECLARATION, self.FOLLOW_VAR_DECLARATION_in_localVariableDeclaration4139)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_localModifierList_in_localVariableDeclaration4143)
                md0 = self.localModifierList()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_type_in_localVariableDeclaration4147)
                tp0 = self.type()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_variableDeclaratorList_in_localVariableDeclaration4151)
                vd0 = self.variableDeclaratorList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self.addVariables(vd0, ((tp0 is not None) and [tp0.value] or [None])[0], md0, local=True) 


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
    # JavaTreeParser.g:566:1: statement returns [value] : ( block | ^( ASSERT (ex0= expression ) (ex1= expression )? ) | ^( IF pe0= parenthesizedExpression statement ( statement )? ) | ^( FOR finit0= forInit fcond0= forCondition fupdt0= forUpdater statement ) | ^( FOR_EACH localModifierList type id0= IDENT ex0= expression st0= statement ) | ^( WHILE pe0= parenthesizedExpression statement ) | ^( DO statement pe0= parenthesizedExpression ) | ^( TRY block ( catches )? ( block )? ) | ^( SWITCH (pe0= parenthesizedExpression ) switchBlockLabels ) | ^( SYNCHRONIZED (pe0= parenthesizedExpression ) block ) | ^( RETURN (ex0= expression )? ) | ^( THROW ex0= expression ) | ^( BREAK (id0= IDENT )? ) | ^( CONTINUE (id0= IDENT )? ) | ^( LABELED_STATEMENT id0= IDENT lb0= statement ) | ex0= expression | SEMI );
    def statement(self, ):

        value = None
        statement_StartIndex = self.input.index()
        id0 = None
        ex0 = None

        ex1 = None

        pe0 = None

        finit0 = None

        fcond0 = None

        fupdt0 = None

        st0 = None

        lb0 = None


                   
        label = None
        value = ex()
            
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 51):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:571:5: ( block | ^( ASSERT (ex0= expression ) (ex1= expression )? ) | ^( IF pe0= parenthesizedExpression statement ( statement )? ) | ^( FOR finit0= forInit fcond0= forCondition fupdt0= forUpdater statement ) | ^( FOR_EACH localModifierList type id0= IDENT ex0= expression st0= statement ) | ^( WHILE pe0= parenthesizedExpression statement ) | ^( DO statement pe0= parenthesizedExpression ) | ^( TRY block ( catches )? ( block )? ) | ^( SWITCH (pe0= parenthesizedExpression ) switchBlockLabels ) | ^( SYNCHRONIZED (pe0= parenthesizedExpression ) block ) | ^( RETURN (ex0= expression )? ) | ^( THROW ex0= expression ) | ^( BREAK (id0= IDENT )? ) | ^( CONTINUE (id0= IDENT )? ) | ^( LABELED_STATEMENT id0= IDENT lb0= statement ) | ex0= expression | SEMI )
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
                    # JavaTreeParser.g:571:9: block
                    pass 
                    self._state.following.append(self.FOLLOW_block_in_statement4207)
                    self.block()

                    self._state.following.pop()


                elif alt80 == 2:
                    # JavaTreeParser.g:572:9: ^( ASSERT (ex0= expression ) (ex1= expression )? )
                    pass 
                    self.match(self.input, ASSERT, self.FOLLOW_ASSERT_in_statement4218)

                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:573:11: (ex0= expression )
                    # JavaTreeParser.g:573:12: ex0= expression
                    pass 
                    self._state.following.append(self.FOLLOW_expression_in_statement4233)
                    ex0 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        ae = self.makeAssert(ex0)  




                    # JavaTreeParser.g:574:11: (ex1= expression )?
                    alt73 = 2
                    LA73_0 = self.input.LA(1)

                    if (LA73_0 == EXPR) :
                        alt73 = 1
                    if alt73 == 1:
                        # JavaTreeParser.g:574:12: ex1= expression
                        pass 
                        self._state.following.append(self.FOLLOW_expression_in_statement4251)
                        ex1 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self.extendAssert(ae, ex1) 





                    self.match(self.input, UP, None)


                elif alt80 == 3:
                    # JavaTreeParser.g:576:9: ^( IF pe0= parenthesizedExpression statement ( statement )? )
                    pass 
                    self.match(self.input, IF, self.FOLLOW_IF_in_statement4276)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_statement4290)
                    pe0 = self.parenthesizedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        ifstat, elsestat = self.beginIf(pe0) 

                    self._state.following.append(self.FOLLOW_statement_in_statement4304)
                    self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.endIf() 

                    # JavaTreeParser.g:579:11: ( statement )?
                    alt74 = 2
                    LA74_0 = self.input.LA(1)

                    if (LA74_0 == SEMI or LA74_0 == ASSERT or LA74_0 == BREAK or LA74_0 == CONTINUE or LA74_0 == DO or (FOR <= LA74_0 <= IF) or LA74_0 == RETURN or (SWITCH <= LA74_0 <= SYNCHRONIZED) or LA74_0 == THROW or LA74_0 == TRY or LA74_0 == WHILE or LA74_0 == BLOCK_SCOPE or LA74_0 == EXPR or LA74_0 == FOR_EACH or LA74_0 == LABELED_STATEMENT) :
                        alt74 = 1
                    if alt74 == 1:
                        # JavaTreeParser.g:579:12: statement
                        pass 
                        if self._state.backtracking == 0:
                            self.beginElse(elsestat) 

                        self._state.following.append(self.FOLLOW_statement_in_statement4321)
                        self.statement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self.endElse() 





                    self.match(self.input, UP, None)


                elif alt80 == 4:
                    # JavaTreeParser.g:581:9: ^( FOR finit0= forInit fcond0= forCondition fupdt0= forUpdater statement )
                    pass 
                    self.match(self.input, FOR, self.FOLLOW_FOR_in_statement4346)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_forInit_in_statement4360)
                    finit0 = self.forInit()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_forCondition_in_statement4374)
                    fcond0 = self.forCondition()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_forUpdater_in_statement4388)
                    fupdt0 = self.forUpdater()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.beginForLoop(finit0, fcond0, fupdt0) 

                    self._state.following.append(self.FOLLOW_statement_in_statement4412)
                    self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.endForLoop() 


                    self.match(self.input, UP, None)


                elif alt80 == 5:
                    # JavaTreeParser.g:589:9: ^( FOR_EACH localModifierList type id0= IDENT ex0= expression st0= statement )
                    pass 
                    self.match(self.input, FOR_EACH, self.FOLLOW_FOR_EACH_in_statement4445)

                    if self._state.backtracking == 0:
                        self.beginForEach() 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_localModifierList_in_statement4469)
                    self.localModifierList()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_type_in_statement4481)
                    self.type()

                    self._state.following.pop()
                    id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_statement4495)
                    self._state.following.append(self.FOLLOW_expression_in_statement4509)
                    ex0 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.setExpression(ex(id0.text, ex0, format="${left} in ${right}")) 

                    self._state.following.append(self.FOLLOW_statement_in_statement4535)
                    st0 = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.append(st0) 

                    if self._state.backtracking == 0:
                        self.endForEach() 


                    self.match(self.input, UP, None)


                elif alt80 == 6:
                    # JavaTreeParser.g:599:9: ^( WHILE pe0= parenthesizedExpression statement )
                    pass 
                    self.match(self.input, WHILE, self.FOLLOW_WHILE_in_statement4570)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_statement4584)
                    pe0 = self.parenthesizedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.beginWhile(pe0) 

                    self._state.following.append(self.FOLLOW_statement_in_statement4608)
                    self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.endWhile() 


                    self.match(self.input, UP, None)


                elif alt80 == 7:
                    # JavaTreeParser.g:605:9: ^( DO statement pe0= parenthesizedExpression )
                    pass 
                    self.match(self.input, DO, self.FOLLOW_DO_in_statement4641)

                    if self._state.backtracking == 0:
                        self.beginDo() 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_statement_in_statement4665)
                    self.statement()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_statement4679)
                    pe0 = self.parenthesizedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.endDo(pe0) 


                    self.match(self.input, UP, None)


                elif alt80 == 8:
                    # JavaTreeParser.g:611:9: ^( TRY block ( catches )? ( block )? )
                    pass 
                    self.match(self.input, TRY, self.FOLLOW_TRY_in_statement4712)

                    if self._state.backtracking == 0:
                        self.beginTry() 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_block_in_statement4734)
                    self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.endTry() 

                    # JavaTreeParser.g:615:10: ( catches )?
                    alt75 = 2
                    LA75_0 = self.input.LA(1)

                    if (LA75_0 == CATCH_CLAUSE_LIST) :
                        alt75 = 1
                    if alt75 == 1:
                        # JavaTreeParser.g:0:0: catches
                        pass 
                        self._state.following.append(self.FOLLOW_catches_in_statement4756)
                        self.catches()

                        self._state.following.pop()



                    # JavaTreeParser.g:616:10: ( block )?
                    alt76 = 2
                    LA76_0 = self.input.LA(1)

                    if (LA76_0 == BLOCK_SCOPE) :
                        alt76 = 1
                    if alt76 == 1:
                        # JavaTreeParser.g:616:11: block
                        pass 
                        if self._state.backtracking == 0:
                            self.beginTryFinally() 

                        self._state.following.append(self.FOLLOW_block_in_statement4771)
                        self.block()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            sef.endTryFinally() 





                    self.match(self.input, UP, None)


                elif alt80 == 9:
                    # JavaTreeParser.g:618:9: ^( SWITCH (pe0= parenthesizedExpression ) switchBlockLabels )
                    pass 
                    self.match(self.input, SWITCH, self.FOLLOW_SWITCH_in_statement4796)

                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:619:11: (pe0= parenthesizedExpression )
                    # JavaTreeParser.g:619:12: pe0= parenthesizedExpression
                    pass 
                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_statement4811)
                    pe0 = self.parenthesizedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.beginSwitch(pe0) 




                    self._state.following.append(self.FOLLOW_switchBlockLabels_in_statement4826)
                    self.switchBlockLabels()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.endSwitch() 


                    self.match(self.input, UP, None)


                elif alt80 == 10:
                    # JavaTreeParser.g:623:9: ^( SYNCHRONIZED (pe0= parenthesizedExpression ) block )
                    pass 
                    self.match(self.input, SYNCHRONIZED, self.FOLLOW_SYNCHRONIZED_in_statement4859)

                    if self._state.backtracking == 0:
                        self.beginSync() 


                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:625:11: (pe0= parenthesizedExpression )
                    # JavaTreeParser.g:625:12: pe0= parenthesizedExpression
                    pass 
                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_statement4886)
                    pe0 = self.parenthesizedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.setExpression(pe0) 




                    self._state.following.append(self.FOLLOW_block_in_statement4901)
                    self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.endSync() 


                    self.match(self.input, UP, None)


                elif alt80 == 11:
                    # JavaTreeParser.g:629:9: ^( RETURN (ex0= expression )? )
                    pass 
                    self.match(self.input, RETURN, self.FOLLOW_RETURN_in_statement4935)

                    if self._state.backtracking == 0:
                        value.update(format="return") 


                    if self.input.LA(1) == DOWN:
                        self.match(self.input, DOWN, None)
                        # JavaTreeParser.g:631:11: (ex0= expression )?
                        alt77 = 2
                        LA77_0 = self.input.LA(1)

                        if (LA77_0 == EXPR) :
                            alt77 = 1
                        if alt77 == 1:
                            # JavaTreeParser.g:631:12: ex0= expression
                            pass 
                            self._state.following.append(self.FOLLOW_expression_in_statement4962)
                            ex0 = self.expression()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                value.update(right=ex0) 




                        if self._state.backtracking == 0:
                            value.update(format="return ${right}") 


                        self.match(self.input, UP, None)



                elif alt80 == 12:
                    # JavaTreeParser.g:634:9: ^( THROW ex0= expression )
                    pass 
                    self.match(self.input, THROW, self.FOLLOW_THROW_in_statement4999)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_statement5003)
                    ex0 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addThrow(ex0) 


                    self.match(self.input, UP, None)


                elif alt80 == 13:
                    # JavaTreeParser.g:635:9: ^( BREAK (id0= IDENT )? )
                    pass 
                    self.match(self.input, BREAK, self.FOLLOW_BREAK_in_statement5017)

                    if self.input.LA(1) == DOWN:
                        self.match(self.input, DOWN, None)
                        # JavaTreeParser.g:635:17: (id0= IDENT )?
                        alt78 = 2
                        LA78_0 = self.input.LA(1)

                        if (LA78_0 == IDENT) :
                            alt78 = 1
                        if alt78 == 1:
                            # JavaTreeParser.g:635:18: id0= IDENT
                            pass 
                            id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_statement5022)
                            if self._state.backtracking == 0:
                                label = id0.text 





                        self.match(self.input, UP, None)

                    if self._state.backtracking == 0:
                        self.addBreak(label=label) 



                elif alt80 == 14:
                    # JavaTreeParser.g:636:9: ^( CONTINUE (id0= IDENT )? )
                    pass 
                    self.match(self.input, CONTINUE, self.FOLLOW_CONTINUE_in_statement5041)

                    if self.input.LA(1) == DOWN:
                        self.match(self.input, DOWN, None)
                        # JavaTreeParser.g:636:20: (id0= IDENT )?
                        alt79 = 2
                        LA79_0 = self.input.LA(1)

                        if (LA79_0 == IDENT) :
                            alt79 = 1
                        if alt79 == 1:
                            # JavaTreeParser.g:636:21: id0= IDENT
                            pass 
                            id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_statement5046)
                            if self._state.backtracking == 0:
                                label = id0.text 





                        self.match(self.input, UP, None)

                    if self._state.backtracking == 0:
                        self.addContinue(label=label) 



                elif alt80 == 15:
                    # JavaTreeParser.g:637:9: ^( LABELED_STATEMENT id0= IDENT lb0= statement )
                    pass 
                    self.match(self.input, LABELED_STATEMENT, self.FOLLOW_LABELED_STATEMENT_in_statement5064)

                    self.match(self.input, DOWN, None)
                    id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_statement5068)
                    self._state.following.append(self.FOLLOW_statement_in_statement5072)
                    lb0 = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addLabel(id0.text) 


                    self.match(self.input, UP, None)


                elif alt80 == 16:
                    # JavaTreeParser.g:638:9: ex0= expression
                    pass 
                    self._state.following.append(self.FOLLOW_expression_in_statement5087)
                    ex0 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex0 



                elif alt80 == 17:
                    # JavaTreeParser.g:639:9: SEMI
                    pass 
                    self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement5099)



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
    # JavaTreeParser.g:643:1: catches : ^( CATCH_CLAUSE_LIST ( catchClause )+ ) ;
    def catches(self, ):

        catches_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 52):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:644:5: ( ^( CATCH_CLAUSE_LIST ( catchClause )+ ) )
                # JavaTreeParser.g:644:9: ^( CATCH_CLAUSE_LIST ( catchClause )+ )
                pass 
                self.match(self.input, CATCH_CLAUSE_LIST, self.FOLLOW_CATCH_CLAUSE_LIST_in_catches5121)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:644:29: ( catchClause )+
                cnt81 = 0
                while True: #loop81
                    alt81 = 2
                    LA81_0 = self.input.LA(1)

                    if (LA81_0 == CATCH) :
                        alt81 = 1


                    if alt81 == 1:
                        # JavaTreeParser.g:0:0: catchClause
                        pass 
                        self._state.following.append(self.FOLLOW_catchClause_in_catches5123)
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
    # JavaTreeParser.g:648:1: catchClause : ^( CATCH fp0= formalParameterStandardDecl block ) ;
    def catchClause(self, ):

        catchClause_StartIndex = self.input.index()
        fp0 = None


        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 53):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:649:5: ( ^( CATCH fp0= formalParameterStandardDecl block ) )
                # JavaTreeParser.g:649:9: ^( CATCH fp0= formalParameterStandardDecl block )
                pass 
                self.match(self.input, CATCH, self.FOLLOW_CATCH_in_catchClause5146)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_formalParameterStandardDecl_in_catchClause5160)
                fp0 = self.formalParameterStandardDecl()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self.beginCatch(fp0) 

                self._state.following.append(self.FOLLOW_block_in_catchClause5174)
                self.block()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self.endCatch() 


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
    # JavaTreeParser.g:656:1: switchBlockLabels : ^( SWITCH_BLOCK_LABEL_LIST ( switchCaseLabel )* ( switchDefaultLabel )? ) ;
    def switchBlockLabels(self, ):

        switchBlockLabels_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 54):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:659:5: ( ^( SWITCH_BLOCK_LABEL_LIST ( switchCaseLabel )* ( switchDefaultLabel )? ) )
                # JavaTreeParser.g:659:9: ^( SWITCH_BLOCK_LABEL_LIST ( switchCaseLabel )* ( switchDefaultLabel )? )
                pass 
                self.match(self.input, SWITCH_BLOCK_LABEL_LIST, self.FOLLOW_SWITCH_BLOCK_LABEL_LIST_in_switchBlockLabels5209)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:659:35: ( switchCaseLabel )*
                    while True: #loop82
                        alt82 = 2
                        LA82_0 = self.input.LA(1)

                        if (LA82_0 == CASE) :
                            alt82 = 1


                        if alt82 == 1:
                            # JavaTreeParser.g:0:0: switchCaseLabel
                            pass 
                            self._state.following.append(self.FOLLOW_switchCaseLabel_in_switchBlockLabels5211)
                            self.switchCaseLabel()

                            self._state.following.pop()


                        else:
                            break #loop82


                    # JavaTreeParser.g:659:52: ( switchDefaultLabel )?
                    alt83 = 2
                    LA83_0 = self.input.LA(1)

                    if (LA83_0 == DEFAULT) :
                        alt83 = 1
                    if alt83 == 1:
                        # JavaTreeParser.g:0:0: switchDefaultLabel
                        pass 
                        self._state.following.append(self.FOLLOW_switchDefaultLabel_in_switchBlockLabels5214)
                        self.switchDefaultLabel()

                        self._state.following.pop()




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
    # JavaTreeParser.g:663:1: switchCaseLabel : ^( CASE (ex0= expression ) ( blockStatement )* ) ;
    def switchCaseLabel(self, ):

        switchCaseLabel_StartIndex = self.input.index()
        ex0 = None


        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 55):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:664:5: ( ^( CASE (ex0= expression ) ( blockStatement )* ) )
                # JavaTreeParser.g:664:9: ^( CASE (ex0= expression ) ( blockStatement )* )
                pass 
                self.match(self.input, CASE, self.FOLLOW_CASE_in_switchCaseLabel5237)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:665:11: (ex0= expression )
                # JavaTreeParser.g:665:13: ex0= expression
                pass 
                self._state.following.append(self.FOLLOW_expression_in_switchCaseLabel5253)
                ex0 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self.addSwitchCase(ex0) 




                # JavaTreeParser.g:666:11: ( blockStatement )*
                while True: #loop84
                    alt84 = 2
                    LA84_0 = self.input.LA(1)

                    if (LA84_0 == AT or LA84_0 == SEMI or LA84_0 == ASSERT or LA84_0 == BREAK or (CLASS <= LA84_0 <= CONTINUE) or LA84_0 == DO or LA84_0 == ENUM or (FOR <= LA84_0 <= IF) or LA84_0 == INTERFACE or LA84_0 == RETURN or (SWITCH <= LA84_0 <= SYNCHRONIZED) or LA84_0 == THROW or LA84_0 == TRY or LA84_0 == WHILE or LA84_0 == BLOCK_SCOPE or LA84_0 == EXPR or LA84_0 == FOR_EACH or LA84_0 == LABELED_STATEMENT or LA84_0 == VAR_DECLARATION) :
                        alt84 = 1


                    if alt84 == 1:
                        # JavaTreeParser.g:0:0: blockStatement
                        pass 
                        self._state.following.append(self.FOLLOW_blockStatement_in_switchCaseLabel5269)
                        self.blockStatement()

                        self._state.following.pop()


                    else:
                        break #loop84



                self.match(self.input, UP, None)
                if self._state.backtracking == 0:
                    self.maybePop(pop=True) 





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
    # JavaTreeParser.g:672:1: switchDefaultLabel : ^( DEFAULT ( blockStatement )* ) ;
    def switchDefaultLabel(self, ):

        switchDefaultLabel_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 56):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:673:5: ( ^( DEFAULT ( blockStatement )* ) )
                # JavaTreeParser.g:673:9: ^( DEFAULT ( blockStatement )* )
                pass 
                self.match(self.input, DEFAULT, self.FOLLOW_DEFAULT_in_switchDefaultLabel5311)

                if self._state.backtracking == 0:
                    self.addSwitchCaseDefault() 


                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:675:11: ( blockStatement )*
                    while True: #loop85
                        alt85 = 2
                        LA85_0 = self.input.LA(1)

                        if (LA85_0 == AT or LA85_0 == SEMI or LA85_0 == ASSERT or LA85_0 == BREAK or (CLASS <= LA85_0 <= CONTINUE) or LA85_0 == DO or LA85_0 == ENUM or (FOR <= LA85_0 <= IF) or LA85_0 == INTERFACE or LA85_0 == RETURN or (SWITCH <= LA85_0 <= SYNCHRONIZED) or LA85_0 == THROW or LA85_0 == TRY or LA85_0 == WHILE or LA85_0 == BLOCK_SCOPE or LA85_0 == EXPR or LA85_0 == FOR_EACH or LA85_0 == LABELED_STATEMENT or LA85_0 == VAR_DECLARATION) :
                            alt85 = 1


                        if alt85 == 1:
                            # JavaTreeParser.g:0:0: blockStatement
                            pass 
                            self._state.following.append(self.FOLLOW_blockStatement_in_switchDefaultLabel5335)
                            self.blockStatement()

                            self._state.following.pop()


                        else:
                            break #loop85



                    self.match(self.input, UP, None)

                if self._state.backtracking == 0:
                    self.maybePop(pop=True) 





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
    # JavaTreeParser.g:681:1: forInit returns [values] : ^( FOR_INIT ( localVariableDeclaration | (ex0= expression )* )? ) ;
    def forInit(self, ):

        values = None
        forInit_StartIndex = self.input.index()
        ex0 = None


        values = [] 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 57):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return values

                # JavaTreeParser.g:683:5: ( ^( FOR_INIT ( localVariableDeclaration | (ex0= expression )* )? ) )
                # JavaTreeParser.g:683:9: ^( FOR_INIT ( localVariableDeclaration | (ex0= expression )* )? )
                pass 
                self.match(self.input, FOR_INIT, self.FOLLOW_FOR_INIT_in_forInit5390)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:683:20: ( localVariableDeclaration | (ex0= expression )* )?
                    alt87 = 3
                    LA87 = self.input.LA(1)
                    if LA87 == VAR_DECLARATION:
                        alt87 = 1
                    elif LA87 == EXPR:
                        alt87 = 2
                    elif LA87 == 3:
                        LA87_3 = self.input.LA(2)

                        if (self.synpred131_JavaTreeParser()) :
                            alt87 = 2
                    if alt87 == 1:
                        # JavaTreeParser.g:684:11: localVariableDeclaration
                        pass 
                        self._state.following.append(self.FOLLOW_localVariableDeclaration_in_forInit5404)
                        self.localVariableDeclaration()

                        self._state.following.pop()


                    elif alt87 == 2:
                        # JavaTreeParser.g:685:11: (ex0= expression )*
                        pass 
                        # JavaTreeParser.g:685:11: (ex0= expression )*
                        while True: #loop86
                            alt86 = 2
                            LA86_0 = self.input.LA(1)

                            if (LA86_0 == EXPR) :
                                alt86 = 1


                            if alt86 == 1:
                                # JavaTreeParser.g:685:12: ex0= expression
                                pass 
                                self._state.following.append(self.FOLLOW_expression_in_forInit5421)
                                ex0 = self.expression()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    values.append( ex0)



                            else:
                                break #loop86






                    self.match(self.input, UP, None)





                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 57, forInit_StartIndex, success)

            pass

        return values

    # $ANTLR end "forInit"


    # $ANTLR start "forCondition"
    # JavaTreeParser.g:689:1: forCondition returns [value] : ^( FOR_CONDITION (ex0= expression )? ) ;
    def forCondition(self, ):

        value = None
        forCondition_StartIndex = self.input.index()
        ex0 = None


        value = ex() 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 58):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:691:5: ( ^( FOR_CONDITION (ex0= expression )? ) )
                # JavaTreeParser.g:691:9: ^( FOR_CONDITION (ex0= expression )? )
                pass 
                self.match(self.input, FOR_CONDITION, self.FOLLOW_FOR_CONDITION_in_forCondition5470)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:691:28: (ex0= expression )?
                    alt88 = 2
                    LA88_0 = self.input.LA(1)

                    if (LA88_0 == EXPR) :
                        alt88 = 1
                    if alt88 == 1:
                        # JavaTreeParser.g:0:0: ex0= expression
                        pass 
                        self._state.following.append(self.FOLLOW_expression_in_forCondition5474)
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
                self.memoize(self.input, 58, forCondition_StartIndex, success)

            pass

        return value

    # $ANTLR end "forCondition"


    # $ANTLR start "forUpdater"
    # JavaTreeParser.g:694:1: forUpdater returns [values] : ^( FOR_UPDATE (ex0= expression )* ) ;
    def forUpdater(self, ):

        values = None
        forUpdater_StartIndex = self.input.index()
        ex0 = None


        values = [] 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 59):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return values

                # JavaTreeParser.g:696:5: ( ^( FOR_UPDATE (ex0= expression )* ) )
                # JavaTreeParser.g:696:9: ^( FOR_UPDATE (ex0= expression )* )
                pass 
                self.match(self.input, FOR_UPDATE, self.FOLLOW_FOR_UPDATE_in_forUpdater5512)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:696:22: (ex0= expression )*
                    while True: #loop89
                        alt89 = 2
                        LA89_0 = self.input.LA(1)

                        if (LA89_0 == EXPR) :
                            alt89 = 1


                        if alt89 == 1:
                            # JavaTreeParser.g:696:23: ex0= expression
                            pass 
                            self._state.following.append(self.FOLLOW_expression_in_forUpdater5517)
                            ex0 = self.expression()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                values.append( ex0) 



                        else:
                            break #loop89



                    self.match(self.input, UP, None)





                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 59, forUpdater_StartIndex, success)

            pass

        return values

    # $ANTLR end "forUpdater"


    # $ANTLR start "parenthesizedExpression"
    # JavaTreeParser.g:701:1: parenthesizedExpression returns [value] : ^( PARENTESIZED_EXPR ex0= expression ) ;
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

                # JavaTreeParser.g:702:5: ( ^( PARENTESIZED_EXPR ex0= expression ) )
                # JavaTreeParser.g:702:9: ^( PARENTESIZED_EXPR ex0= expression )
                pass 
                self.match(self.input, PARENTESIZED_EXPR, self.FOLLOW_PARENTESIZED_EXPR_in_parenthesizedExpression5548)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_expression_in_parenthesizedExpression5552)
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
    # JavaTreeParser.g:705:1: expression returns [value] : ^( EXPR ex0= expr ) ;
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

                # JavaTreeParser.g:706:5: ( ^( EXPR ex0= expr ) )
                # JavaTreeParser.g:706:9: ^( EXPR ex0= expr )
                pass 
                self.match(self.input, EXPR, self.FOLLOW_EXPR_in_expression5579)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_expr_in_expression5583)
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
    # JavaTreeParser.g:709:1: expr returns [value] : ( ^( ASSIGN lv0= expr rv0= expr ) | ^( PLUS_ASSIGN lv0= expr rv0= expr ) | ^( MINUS_ASSIGN lv0= expr rv0= expr ) | ^( STAR_ASSIGN lv0= expr rv0= expr ) | ^( DIV_ASSIGN lv0= expr rv0= expr ) | ^( AND_ASSIGN lv0= expr rv0= expr ) | ^( OR_ASSIGN lv0= expr rv0= expr ) | ^( XOR_ASSIGN lv0= expr rv0= expr ) | ^( MOD_ASSIGN lv0= expr rv0= expr ) | ^( BIT_SHIFT_RIGHT_ASSIGN expr expr ) | ^( SHIFT_RIGHT_ASSIGN expr expr ) | ^( SHIFT_LEFT_ASSIGN expr expr ) | ^( QUESTION lv0= expr rv0= expr cv0= expr ) | ^( LOGICAL_OR lv0= expr rv0= expr ) | ^( LOGICAL_AND lv0= expr rv0= expr ) | ^( OR lv0= expr rv0= expr ) | ^( XOR lv0= expr rv0= expr ) | ^( AND lv0= expr rv0= expr ) | ^( EQUAL lv0= expr rv0= expr ) | ^( NOT_EQUAL lv0= expr rv0= expr ) | ^( INSTANCEOF lv0= expr tp0= type ) | ^( LESS_OR_EQUAL lv0= expr rv0= expr ) | ^( GREATER_OR_EQUAL lv0= expr rv0= expr ) | ^( BIT_SHIFT_RIGHT lv0= expr rv0= expr ) | ^( SHIFT_RIGHT lv0= expr rv0= expr ) | ^( GREATER_THAN lv0= expr rv0= expr ) | ^( SHIFT_LEFT lv0= expr rv0= expr ) | ^( LESS_THAN lv0= expr rv0= expr ) | ^( PLUS lv0= expr rv0= expr ) | ^( MINUS lv0= expr rv0= expr ) | ^( STAR lv0= expr rv0= expr ) | ^( DIV lv0= expr rv0= expr ) | ^( MOD lv0= expr rv0= expr ) | ^( UNARY_PLUS lv0= expr ) | ^( UNARY_MINUS lv0= expr ) | ^( PRE_INC lv0= expr ) | ^( PRE_DEC lv0= expr ) | ^( POST_INC lv0= expr ) | ^( POST_DEC lv0= expr ) | ^( NOT lv0= expr ) | ^( LOGICAL_NOT lv0= expr ) | ^( CAST_EXPR tp0= type rv0= expr ) | pe0= primaryExpression );
    def expr(self, ):

        value = None
        expr_StartIndex = self.input.index()
        lv0 = None

        rv0 = None

        cv0 = None

        tp0 = None

        pe0 = None


                   
        value = ex()
        def exs(left, right, op):
            return ex(left, right, "${left} " + op + " ${right}")
        def exs1(left, op):
            return ex(left, format=op + "${left}")
            
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 62):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:717:5: ( ^( ASSIGN lv0= expr rv0= expr ) | ^( PLUS_ASSIGN lv0= expr rv0= expr ) | ^( MINUS_ASSIGN lv0= expr rv0= expr ) | ^( STAR_ASSIGN lv0= expr rv0= expr ) | ^( DIV_ASSIGN lv0= expr rv0= expr ) | ^( AND_ASSIGN lv0= expr rv0= expr ) | ^( OR_ASSIGN lv0= expr rv0= expr ) | ^( XOR_ASSIGN lv0= expr rv0= expr ) | ^( MOD_ASSIGN lv0= expr rv0= expr ) | ^( BIT_SHIFT_RIGHT_ASSIGN expr expr ) | ^( SHIFT_RIGHT_ASSIGN expr expr ) | ^( SHIFT_LEFT_ASSIGN expr expr ) | ^( QUESTION lv0= expr rv0= expr cv0= expr ) | ^( LOGICAL_OR lv0= expr rv0= expr ) | ^( LOGICAL_AND lv0= expr rv0= expr ) | ^( OR lv0= expr rv0= expr ) | ^( XOR lv0= expr rv0= expr ) | ^( AND lv0= expr rv0= expr ) | ^( EQUAL lv0= expr rv0= expr ) | ^( NOT_EQUAL lv0= expr rv0= expr ) | ^( INSTANCEOF lv0= expr tp0= type ) | ^( LESS_OR_EQUAL lv0= expr rv0= expr ) | ^( GREATER_OR_EQUAL lv0= expr rv0= expr ) | ^( BIT_SHIFT_RIGHT lv0= expr rv0= expr ) | ^( SHIFT_RIGHT lv0= expr rv0= expr ) | ^( GREATER_THAN lv0= expr rv0= expr ) | ^( SHIFT_LEFT lv0= expr rv0= expr ) | ^( LESS_THAN lv0= expr rv0= expr ) | ^( PLUS lv0= expr rv0= expr ) | ^( MINUS lv0= expr rv0= expr ) | ^( STAR lv0= expr rv0= expr ) | ^( DIV lv0= expr rv0= expr ) | ^( MOD lv0= expr rv0= expr ) | ^( UNARY_PLUS lv0= expr ) | ^( UNARY_MINUS lv0= expr ) | ^( PRE_INC lv0= expr ) | ^( PRE_DEC lv0= expr ) | ^( POST_INC lv0= expr ) | ^( POST_DEC lv0= expr ) | ^( NOT lv0= expr ) | ^( LOGICAL_NOT lv0= expr ) | ^( CAST_EXPR tp0= type rv0= expr ) | pe0= primaryExpression )
                alt90 = 43
                LA90 = self.input.LA(1)
                if LA90 == ASSIGN:
                    alt90 = 1
                elif LA90 == PLUS_ASSIGN:
                    alt90 = 2
                elif LA90 == MINUS_ASSIGN:
                    alt90 = 3
                elif LA90 == STAR_ASSIGN:
                    alt90 = 4
                elif LA90 == DIV_ASSIGN:
                    alt90 = 5
                elif LA90 == AND_ASSIGN:
                    alt90 = 6
                elif LA90 == OR_ASSIGN:
                    alt90 = 7
                elif LA90 == XOR_ASSIGN:
                    alt90 = 8
                elif LA90 == MOD_ASSIGN:
                    alt90 = 9
                elif LA90 == BIT_SHIFT_RIGHT_ASSIGN:
                    alt90 = 10
                elif LA90 == SHIFT_RIGHT_ASSIGN:
                    alt90 = 11
                elif LA90 == SHIFT_LEFT_ASSIGN:
                    alt90 = 12
                elif LA90 == QUESTION:
                    alt90 = 13
                elif LA90 == LOGICAL_OR:
                    alt90 = 14
                elif LA90 == LOGICAL_AND:
                    alt90 = 15
                elif LA90 == OR:
                    alt90 = 16
                elif LA90 == XOR:
                    alt90 = 17
                elif LA90 == AND:
                    alt90 = 18
                elif LA90 == EQUAL:
                    alt90 = 19
                elif LA90 == NOT_EQUAL:
                    alt90 = 20
                elif LA90 == INSTANCEOF:
                    alt90 = 21
                elif LA90 == LESS_OR_EQUAL:
                    alt90 = 22
                elif LA90 == GREATER_OR_EQUAL:
                    alt90 = 23
                elif LA90 == BIT_SHIFT_RIGHT:
                    alt90 = 24
                elif LA90 == SHIFT_RIGHT:
                    alt90 = 25
                elif LA90 == GREATER_THAN:
                    alt90 = 26
                elif LA90 == SHIFT_LEFT:
                    alt90 = 27
                elif LA90 == LESS_THAN:
                    alt90 = 28
                elif LA90 == PLUS:
                    alt90 = 29
                elif LA90 == MINUS:
                    alt90 = 30
                elif LA90 == STAR:
                    alt90 = 31
                elif LA90 == DIV:
                    alt90 = 32
                elif LA90 == MOD:
                    alt90 = 33
                elif LA90 == UNARY_PLUS:
                    alt90 = 34
                elif LA90 == UNARY_MINUS:
                    alt90 = 35
                elif LA90 == PRE_INC:
                    alt90 = 36
                elif LA90 == PRE_DEC:
                    alt90 = 37
                elif LA90 == POST_INC:
                    alt90 = 38
                elif LA90 == POST_DEC:
                    alt90 = 39
                elif LA90 == NOT:
                    alt90 = 40
                elif LA90 == LOGICAL_NOT:
                    alt90 = 41
                elif LA90 == CAST_EXPR:
                    alt90 = 42
                elif LA90 == DOT or LA90 == FALSE or LA90 == NULL or LA90 == SUPER or LA90 == THIS or LA90 == TRUE or LA90 == ARRAY_DECLARATOR or LA90 == ARRAY_ELEMENT_ACCESS or LA90 == CLASS_CONSTRUCTOR_CALL or LA90 == METHOD_CALL or LA90 == PARENTESIZED_EXPR or LA90 == STATIC_ARRAY_CREATOR or LA90 == SUPER_CONSTRUCTOR_CALL or LA90 == THIS_CONSTRUCTOR_CALL or LA90 == IDENT or LA90 == HEX_LITERAL or LA90 == OCTAL_LITERAL or LA90 == DECIMAL_LITERAL or LA90 == FLOATING_POINT_LITERAL or LA90 == CHARACTER_LITERAL or LA90 == STRING_LITERAL:
                    alt90 = 43
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 90, 0, self.input)

                    raise nvae

                if alt90 == 1:
                    # JavaTreeParser.g:717:9: ^( ASSIGN lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_expr5619)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5623)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5627)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "=")   


                    self.match(self.input, UP, None)


                elif alt90 == 2:
                    # JavaTreeParser.g:718:9: ^( PLUS_ASSIGN lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, PLUS_ASSIGN, self.FOLLOW_PLUS_ASSIGN_in_expr5647)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5651)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5655)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "+=")  


                    self.match(self.input, UP, None)


                elif alt90 == 3:
                    # JavaTreeParser.g:719:9: ^( MINUS_ASSIGN lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, MINUS_ASSIGN, self.FOLLOW_MINUS_ASSIGN_in_expr5670)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5674)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5678)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "-=")  


                    self.match(self.input, UP, None)


                elif alt90 == 4:
                    # JavaTreeParser.g:720:9: ^( STAR_ASSIGN lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, STAR_ASSIGN, self.FOLLOW_STAR_ASSIGN_in_expr5692)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5696)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5700)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "*=")  


                    self.match(self.input, UP, None)


                elif alt90 == 5:
                    # JavaTreeParser.g:721:9: ^( DIV_ASSIGN lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, DIV_ASSIGN, self.FOLLOW_DIV_ASSIGN_in_expr5715)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5719)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5723)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "/=")  


                    self.match(self.input, UP, None)


                elif alt90 == 6:
                    # JavaTreeParser.g:722:9: ^( AND_ASSIGN lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, AND_ASSIGN, self.FOLLOW_AND_ASSIGN_in_expr5739)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5743)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5747)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "&=")  


                    self.match(self.input, UP, None)


                elif alt90 == 7:
                    # JavaTreeParser.g:723:9: ^( OR_ASSIGN lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, OR_ASSIGN, self.FOLLOW_OR_ASSIGN_in_expr5763)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5767)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5771)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "|=")  


                    self.match(self.input, UP, None)


                elif alt90 == 8:
                    # JavaTreeParser.g:724:9: ^( XOR_ASSIGN lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, XOR_ASSIGN, self.FOLLOW_XOR_ASSIGN_in_expr5788)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5792)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5796)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "^=")  


                    self.match(self.input, UP, None)


                elif alt90 == 9:
                    # JavaTreeParser.g:725:9: ^( MOD_ASSIGN lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, MOD_ASSIGN, self.FOLLOW_MOD_ASSIGN_in_expr5812)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5816)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5820)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "%=") 


                    self.match(self.input, UP, None)


                elif alt90 == 10:
                    # JavaTreeParser.g:726:9: ^( BIT_SHIFT_RIGHT_ASSIGN expr expr )
                    pass 
                    self.match(self.input, BIT_SHIFT_RIGHT_ASSIGN, self.FOLLOW_BIT_SHIFT_RIGHT_ASSIGN_in_expr5836)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5838)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5840)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt90 == 11:
                    # JavaTreeParser.g:727:9: ^( SHIFT_RIGHT_ASSIGN expr expr )
                    pass 
                    self.match(self.input, SHIFT_RIGHT_ASSIGN, self.FOLLOW_SHIFT_RIGHT_ASSIGN_in_expr5852)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5854)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5856)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt90 == 12:
                    # JavaTreeParser.g:728:9: ^( SHIFT_LEFT_ASSIGN expr expr )
                    pass 
                    self.match(self.input, SHIFT_LEFT_ASSIGN, self.FOLLOW_SHIFT_LEFT_ASSIGN_in_expr5868)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5870)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5872)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt90 == 13:
                    # JavaTreeParser.g:729:9: ^( QUESTION lv0= expr rv0= expr cv0= expr )
                    pass 
                    self.match(self.input, QUESTION, self.FOLLOW_QUESTION_in_expr5884)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5888)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5892)
                    rv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5896)
                    cv0 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        value.update(left=lv0, right=rv0,
                                      format="(${right} if ${left} else ${center})", center=cv0) 



                elif alt90 == 14:
                    # JavaTreeParser.g:732:9: ^( LOGICAL_OR lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, LOGICAL_OR, self.FOLLOW_LOGICAL_OR_in_expr5920)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5924)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5928)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "or")               


                    self.match(self.input, UP, None)


                elif alt90 == 15:
                    # JavaTreeParser.g:733:9: ^( LOGICAL_AND lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, LOGICAL_AND, self.FOLLOW_LOGICAL_AND_in_expr5948)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5952)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5956)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "and")              


                    self.match(self.input, UP, None)


                elif alt90 == 16:
                    # JavaTreeParser.g:734:9: ^( OR lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, OR, self.FOLLOW_OR_in_expr5975)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5979)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5983)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "|")                


                    self.match(self.input, UP, None)


                elif alt90 == 17:
                    # JavaTreeParser.g:735:9: ^( XOR lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, XOR, self.FOLLOW_XOR_in_expr6011)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6015)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6019)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "^")                


                    self.match(self.input, UP, None)


                elif alt90 == 18:
                    # JavaTreeParser.g:736:9: ^( AND lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, AND, self.FOLLOW_AND_in_expr6046)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6050)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6054)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "&")                


                    self.match(self.input, UP, None)


                elif alt90 == 19:
                    # JavaTreeParser.g:737:9: ^( EQUAL lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_expr6081)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6085)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6089)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "==")               


                    self.match(self.input, UP, None)


                elif alt90 == 20:
                    # JavaTreeParser.g:738:9: ^( NOT_EQUAL lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, NOT_EQUAL, self.FOLLOW_NOT_EQUAL_in_expr6114)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6118)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6122)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "!=")               


                    self.match(self.input, UP, None)


                elif alt90 == 21:
                    # JavaTreeParser.g:739:9: ^( INSTANCEOF lv0= expr tp0= type )
                    pass 
                    self.match(self.input, INSTANCEOF, self.FOLLOW_INSTANCEOF_in_expr6143)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6147)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_type_in_expr6151)
                    tp0 = self.type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex(lv0, ((tp0 is not None) and [tp0.value] or [None])[0], "isinstance(${left}, (${right}, ))") 


                    self.match(self.input, UP, None)


                elif alt90 == 22:
                    # JavaTreeParser.g:741:9: ^( LESS_OR_EQUAL lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, LESS_OR_EQUAL, self.FOLLOW_LESS_OR_EQUAL_in_expr6175)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6179)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6183)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "<=")               


                    self.match(self.input, UP, None)


                elif alt90 == 23:
                    # JavaTreeParser.g:742:9: ^( GREATER_OR_EQUAL lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, GREATER_OR_EQUAL, self.FOLLOW_GREATER_OR_EQUAL_in_expr6200)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6204)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6208)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, ">=")               


                    self.match(self.input, UP, None)


                elif alt90 == 24:
                    # JavaTreeParser.g:743:9: ^( BIT_SHIFT_RIGHT lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, BIT_SHIFT_RIGHT, self.FOLLOW_BIT_SHIFT_RIGHT_in_expr6222)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6226)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6230)
                    rv0 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt90 == 25:
                    # JavaTreeParser.g:744:9: ^( SHIFT_RIGHT lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, SHIFT_RIGHT, self.FOLLOW_SHIFT_RIGHT_in_expr6290)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6294)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6298)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, ">>")               


                    self.match(self.input, UP, None)


                elif alt90 == 26:
                    # JavaTreeParser.g:745:9: ^( GREATER_THAN lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, GREATER_THAN, self.FOLLOW_GREATER_THAN_in_expr6317)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6321)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6325)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, ">")                


                    self.match(self.input, UP, None)


                elif alt90 == 27:
                    # JavaTreeParser.g:746:9: ^( SHIFT_LEFT lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, SHIFT_LEFT, self.FOLLOW_SHIFT_LEFT_in_expr6343)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6347)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6351)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "<<")               


                    self.match(self.input, UP, None)


                elif alt90 == 28:
                    # JavaTreeParser.g:747:9: ^( LESS_THAN lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, LESS_THAN, self.FOLLOW_LESS_THAN_in_expr6371)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6375)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6379)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "<")                


                    self.match(self.input, UP, None)


                elif alt90 == 29:
                    # JavaTreeParser.g:748:9: ^( PLUS lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, PLUS, self.FOLLOW_PLUS_in_expr6400)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6404)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6408)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "+")                


                    self.match(self.input, UP, None)


                elif alt90 == 30:
                    # JavaTreeParser.g:749:9: ^( MINUS lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, MINUS, self.FOLLOW_MINUS_in_expr6434)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6438)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6442)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "-")                


                    self.match(self.input, UP, None)


                elif alt90 == 31:
                    # JavaTreeParser.g:750:9: ^( STAR lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, STAR, self.FOLLOW_STAR_in_expr6467)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6471)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6475)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "*")                


                    self.match(self.input, UP, None)


                elif alt90 == 32:
                    # JavaTreeParser.g:751:9: ^( DIV lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, DIV, self.FOLLOW_DIV_in_expr6501)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6505)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6509)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "/")                


                    self.match(self.input, UP, None)


                elif alt90 == 33:
                    # JavaTreeParser.g:752:9: ^( MOD lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, MOD, self.FOLLOW_MOD_in_expr6536)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6540)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6544)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "%")               


                    self.match(self.input, UP, None)


                elif alt90 == 34:
                    # JavaTreeParser.g:753:9: ^( UNARY_PLUS lv0= expr )
                    pass 
                    self.match(self.input, UNARY_PLUS, self.FOLLOW_UNARY_PLUS_in_expr6571)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6575)
                    lv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs1(lv0, "+")                    


                    self.match(self.input, UP, None)


                elif alt90 == 35:
                    # JavaTreeParser.g:754:9: ^( UNARY_MINUS lv0= expr )
                    pass 
                    self.match(self.input, UNARY_MINUS, self.FOLLOW_UNARY_MINUS_in_expr6604)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6608)
                    lv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs1(lv0, "-")                    


                    self.match(self.input, UP, None)


                elif alt90 == 36:
                    # JavaTreeParser.g:755:9: ^( PRE_INC lv0= expr )
                    pass 
                    self.match(self.input, PRE_INC, self.FOLLOW_PRE_INC_in_expr6636)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6640)
                    lv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex(lv0, format="${left} += 1")    


                    self.match(self.input, UP, None)


                elif alt90 == 37:
                    # JavaTreeParser.g:756:9: ^( PRE_DEC lv0= expr )
                    pass 
                    self.match(self.input, PRE_DEC, self.FOLLOW_PRE_DEC_in_expr6672)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6676)
                    lv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex(lv0, format="${left} -= 1")    


                    self.match(self.input, UP, None)


                elif alt90 == 38:
                    # JavaTreeParser.g:757:9: ^( POST_INC lv0= expr )
                    pass 
                    self.match(self.input, POST_INC, self.FOLLOW_POST_INC_in_expr6708)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6712)
                    lv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex(lv0, format="${left} += 1")    


                    self.match(self.input, UP, None)


                elif alt90 == 39:
                    # JavaTreeParser.g:758:9: ^( POST_DEC lv0= expr )
                    pass 
                    self.match(self.input, POST_DEC, self.FOLLOW_POST_DEC_in_expr6743)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6747)
                    lv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex(lv0, format="${left} -= 1")    


                    self.match(self.input, UP, None)


                elif alt90 == 40:
                    # JavaTreeParser.g:759:9: ^( NOT lv0= expr )
                    pass 
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_expr6778)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6782)
                    lv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex(lv0, format="~${left}")        


                    self.match(self.input, UP, None)


                elif alt90 == 41:
                    # JavaTreeParser.g:760:9: ^( LOGICAL_NOT lv0= expr )
                    pass 
                    self.match(self.input, LOGICAL_NOT, self.FOLLOW_LOGICAL_NOT_in_expr6818)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6822)
                    lv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex(lv0, format="not ${left}")     


                    self.match(self.input, UP, None)


                elif alt90 == 42:
                    # JavaTreeParser.g:761:9: ^( CAST_EXPR tp0= type rv0= expr )
                    pass 
                    self.match(self.input, CAST_EXPR, self.FOLLOW_CAST_EXPR_in_expr6850)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_type_in_expr6854)
                    tp0 = self.type()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6858)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex(((tp0 is not None) and [tp0.value] or [None])[0], rv0, "${left}(${right})") 


                    self.match(self.input, UP, None)


                elif alt90 == 43:
                    # JavaTreeParser.g:762:9: pe0= primaryExpression
                    pass 
                    self._state.following.append(self.FOLLOW_primaryExpression_in_expr6880)
                    pe0 = self.primaryExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        if pe0:
                            value.update(pe0)
                                




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
    # JavaTreeParser.g:768:1: primaryExpression returns [value] : ( ^( DOT (p0= primaryExpression ( IDENT | THIS | SUPER | ne0= innerNewExpression | CLASS ) | pt0= primitiveType CLASS | VOID CLASS ) ) | parenthesizedExpression | IDENT | ^( METHOD_CALL p0= primaryExpression ( genericTypeArgumentList )? a0= arguments ) | ec0= explicitConstructorCall | ^( ARRAY_ELEMENT_ACCESS p0= primaryExpression e0= expression ) | literal | newExpression | THIS | arrayTypeDeclarator | SUPER );
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

                # JavaTreeParser.g:770:5: ( ^( DOT (p0= primaryExpression ( IDENT | THIS | SUPER | ne0= innerNewExpression | CLASS ) | pt0= primitiveType CLASS | VOID CLASS ) ) | parenthesizedExpression | IDENT | ^( METHOD_CALL p0= primaryExpression ( genericTypeArgumentList )? a0= arguments ) | ec0= explicitConstructorCall | ^( ARRAY_ELEMENT_ACCESS p0= primaryExpression e0= expression ) | literal | newExpression | THIS | arrayTypeDeclarator | SUPER )
                alt94 = 11
                LA94 = self.input.LA(1)
                if LA94 == DOT:
                    alt94 = 1
                elif LA94 == PARENTESIZED_EXPR:
                    alt94 = 2
                elif LA94 == IDENT:
                    alt94 = 3
                elif LA94 == METHOD_CALL:
                    alt94 = 4
                elif LA94 == SUPER_CONSTRUCTOR_CALL or LA94 == THIS_CONSTRUCTOR_CALL:
                    alt94 = 5
                elif LA94 == ARRAY_ELEMENT_ACCESS:
                    alt94 = 6
                elif LA94 == FALSE or LA94 == NULL or LA94 == TRUE or LA94 == HEX_LITERAL or LA94 == OCTAL_LITERAL or LA94 == DECIMAL_LITERAL or LA94 == FLOATING_POINT_LITERAL or LA94 == CHARACTER_LITERAL or LA94 == STRING_LITERAL:
                    alt94 = 7
                elif LA94 == CLASS_CONSTRUCTOR_CALL or LA94 == STATIC_ARRAY_CREATOR:
                    alt94 = 8
                elif LA94 == THIS:
                    alt94 = 9
                elif LA94 == ARRAY_DECLARATOR:
                    alt94 = 10
                elif LA94 == SUPER:
                    alt94 = 11
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 94, 0, self.input)

                    raise nvae

                if alt94 == 1:
                    # JavaTreeParser.g:770:9: ^( DOT (p0= primaryExpression ( IDENT | THIS | SUPER | ne0= innerNewExpression | CLASS ) | pt0= primitiveType CLASS | VOID CLASS ) )
                    pass 
                    self.match(self.input, DOT, self.FOLLOW_DOT_in_primaryExpression6925)

                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:771:13: (p0= primaryExpression ( IDENT | THIS | SUPER | ne0= innerNewExpression | CLASS ) | pt0= primitiveType CLASS | VOID CLASS )
                    alt92 = 3
                    LA92 = self.input.LA(1)
                    if LA92 == DOT or LA92 == FALSE or LA92 == NULL or LA92 == SUPER or LA92 == THIS or LA92 == TRUE or LA92 == ARRAY_DECLARATOR or LA92 == ARRAY_ELEMENT_ACCESS or LA92 == CLASS_CONSTRUCTOR_CALL or LA92 == METHOD_CALL or LA92 == PARENTESIZED_EXPR or LA92 == STATIC_ARRAY_CREATOR or LA92 == SUPER_CONSTRUCTOR_CALL or LA92 == THIS_CONSTRUCTOR_CALL or LA92 == IDENT or LA92 == HEX_LITERAL or LA92 == OCTAL_LITERAL or LA92 == DECIMAL_LITERAL or LA92 == FLOATING_POINT_LITERAL or LA92 == CHARACTER_LITERAL or LA92 == STRING_LITERAL:
                        alt92 = 1
                    elif LA92 == BOOLEAN or LA92 == BYTE or LA92 == CHAR or LA92 == DOUBLE or LA92 == FLOAT or LA92 == INT or LA92 == LONG or LA92 == SHORT:
                        alt92 = 2
                    elif LA92 == VOID:
                        alt92 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 92, 0, self.input)

                        raise nvae

                    if alt92 == 1:
                        # JavaTreeParser.g:771:17: p0= primaryExpression ( IDENT | THIS | SUPER | ne0= innerNewExpression | CLASS )
                        pass 
                        self._state.following.append(self.FOLLOW_primaryExpression_in_primaryExpression6945)
                        p0 = self.primaryExpression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            value = ex(p0, format="${left}.${right}") 

                        # JavaTreeParser.g:773:17: ( IDENT | THIS | SUPER | ne0= innerNewExpression | CLASS )
                        alt91 = 5
                        LA91 = self.input.LA(1)
                        if LA91 == IDENT:
                            alt91 = 1
                        elif LA91 == THIS:
                            alt91 = 2
                        elif LA91 == SUPER:
                            alt91 = 3
                        elif LA91 == CLASS_CONSTRUCTOR_CALL:
                            alt91 = 4
                        elif LA91 == CLASS:
                            alt91 = 5
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 91, 0, self.input)

                            raise nvae

                        if alt91 == 1:
                            # JavaTreeParser.g:773:21: IDENT
                            pass 
                            IDENT4=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_primaryExpression6985)
                            if self._state.backtracking == 0:
                                value["right"] = ex(IDENT4.text, format="${left}", rename=True) 



                        elif alt91 == 2:
                            # JavaTreeParser.g:775:21: THIS
                            pass 
                            self.match(self.input, THIS, self.FOLLOW_THIS_in_primaryExpression7029)
                            if self._state.backtracking == 0:
                                value["format"] = "${left}" 



                        elif alt91 == 3:
                            # JavaTreeParser.g:776:21: SUPER
                            pass 
                            self.match(self.input, SUPER, self.FOLLOW_SUPER_in_primaryExpression7055)
                            if self._state.backtracking == 0:
                                value["format"] = "${left}"
                                value["left"] = ex(value["left"], "", "super(${left}, self)")
                                                 



                        elif alt91 == 4:
                            # JavaTreeParser.g:780:18: ne0= innerNewExpression
                            pass 
                            self._state.following.append(self.FOLLOW_innerNewExpression_in_primaryExpression7095)
                            ne0 = self.innerNewExpression()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                value["right"] = ne0 



                        elif alt91 == 5:
                            # JavaTreeParser.g:781:21: CLASS
                            pass 
                            self.match(self.input, CLASS, self.FOLLOW_CLASS_in_primaryExpression7119)
                            if self._state.backtracking == 0:
                                value["right"] = ex("__class__", "", "${left}") 






                    elif alt92 == 2:
                        # JavaTreeParser.g:783:17: pt0= primitiveType CLASS
                        pass 
                        self._state.following.append(self.FOLLOW_primitiveType_in_primaryExpression7159)
                        pt0 = self.primitiveType()

                        self._state.following.pop()
                        self.match(self.input, CLASS, self.FOLLOW_CLASS_in_primaryExpression7161)
                        if self._state.backtracking == 0:
                            value = ex(((pt0 is not None) and [self.input.getTokenStream().toString(
                                self.input.getTreeAdaptor().getTokenStartIndex(pt0.start),
                                self.input.getTreeAdaptor().getTokenStopIndex(pt0.start)
                                )] or [None])[0], "__class__", "${left}.${right}") 



                    elif alt92 == 3:
                        # JavaTreeParser.g:784:17: VOID CLASS
                        pass 
                        self.match(self.input, VOID, self.FOLLOW_VOID_in_primaryExpression7181)
                        self.match(self.input, CLASS, self.FOLLOW_CLASS_in_primaryExpression7183)
                        if self._state.backtracking == 0:
                            value = ex("None", "__class__", "${left}.${right}") 





                    self.match(self.input, UP, None)


                elif alt94 == 2:
                    # JavaTreeParser.g:788:9: parenthesizedExpression
                    pass 
                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_primaryExpression7220)
                    parenthesizedExpression5 = self.parenthesizedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = parenthesizedExpression5 



                elif alt94 == 3:
                    # JavaTreeParser.g:790:9: IDENT
                    pass 
                    IDENT6=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_primaryExpression7233)
                    if self._state.backtracking == 0:
                        value = ex(self.altIdent(IDENT6.text), format="${left}", rename=True)  



                elif alt94 == 4:
                    # JavaTreeParser.g:792:9: ^( METHOD_CALL p0= primaryExpression ( genericTypeArgumentList )? a0= arguments )
                    pass 
                    self.match(self.input, METHOD_CALL, self.FOLLOW_METHOD_CALL_in_primaryExpression7247)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_primaryExpression_in_primaryExpression7261)
                    p0 = self.primaryExpression()

                    self._state.following.pop()
                    # JavaTreeParser.g:794:11: ( genericTypeArgumentList )?
                    alt93 = 2
                    LA93_0 = self.input.LA(1)

                    if (LA93_0 == GENERIC_TYPE_ARG_LIST) :
                        alt93 = 1
                    if alt93 == 1:
                        # JavaTreeParser.g:0:0: genericTypeArgumentList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeArgumentList_in_primaryExpression7273)
                        self.genericTypeArgumentList()

                        self._state.following.pop()



                    self._state.following.append(self.FOLLOW_arguments_in_primaryExpression7288)
                    a0 = self.arguments()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex(p0, a0, "${left}(${right})", call=True) 


                    self.match(self.input, UP, None)


                elif alt94 == 5:
                    # JavaTreeParser.g:799:9: ec0= explicitConstructorCall
                    pass 
                    self._state.following.append(self.FOLLOW_explicitConstructorCall_in_primaryExpression7323)
                    ec0 = self.explicitConstructorCall()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addSuperCall(ec0) 



                elif alt94 == 6:
                    # JavaTreeParser.g:801:9: ^( ARRAY_ELEMENT_ACCESS p0= primaryExpression e0= expression )
                    pass 
                    self.match(self.input, ARRAY_ELEMENT_ACCESS, self.FOLLOW_ARRAY_ELEMENT_ACCESS_in_primaryExpression7337)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_primaryExpression_in_primaryExpression7351)
                    p0 = self.primaryExpression()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expression_in_primaryExpression7365)
                    e0 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex(p0, e0, "${left}[${right}]") 


                    self.match(self.input, UP, None)


                elif alt94 == 7:
                    # JavaTreeParser.g:807:9: literal
                    pass 
                    self._state.following.append(self.FOLLOW_literal_in_primaryExpression7398)
                    literal7 = self.literal()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex(((literal7 is not None) and [literal7.value] or [None])[0], format="${left}") 



                elif alt94 == 8:
                    # JavaTreeParser.g:809:9: newExpression
                    pass 
                    self._state.following.append(self.FOLLOW_newExpression_in_primaryExpression7411)
                    newExpression8 = self.newExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = newExpression8 



                elif alt94 == 9:
                    # JavaTreeParser.g:811:9: THIS
                    pass 
                    self.match(self.input, THIS, self.FOLLOW_THIS_in_primaryExpression7424)
                    if self._state.backtracking == 0:
                        value = ex("self", format="${left}") 



                elif alt94 == 10:
                    # JavaTreeParser.g:813:9: arrayTypeDeclarator
                    pass 
                    self._state.following.append(self.FOLLOW_arrayTypeDeclarator_in_primaryExpression7437)
                    self.arrayTypeDeclarator()

                    self._state.following.pop()


                elif alt94 == 11:
                    # JavaTreeParser.g:815:9: SUPER
                    pass 
                    self.match(self.input, SUPER, self.FOLLOW_SUPER_in_primaryExpression7448)
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
    # JavaTreeParser.g:819:1: explicitConstructorCall returns [value] : ( ^( THIS_CONSTRUCTOR_CALL ( genericTypeArgumentList )? arguments ) | ^( SUPER_CONSTRUCTOR_CALL (pe0= primaryExpression )? ( genericTypeArgumentList )? (ag0= arguments ) ) );
    def explicitConstructorCall(self, ):

        value = None
        explicitConstructorCall_StartIndex = self.input.index()
        pe0 = None

        ag0 = None


        value = ex() 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 64):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:821:5: ( ^( THIS_CONSTRUCTOR_CALL ( genericTypeArgumentList )? arguments ) | ^( SUPER_CONSTRUCTOR_CALL (pe0= primaryExpression )? ( genericTypeArgumentList )? (ag0= arguments ) ) )
                alt98 = 2
                LA98_0 = self.input.LA(1)

                if (LA98_0 == THIS_CONSTRUCTOR_CALL) :
                    alt98 = 1
                elif (LA98_0 == SUPER_CONSTRUCTOR_CALL) :
                    alt98 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 98, 0, self.input)

                    raise nvae

                if alt98 == 1:
                    # JavaTreeParser.g:821:9: ^( THIS_CONSTRUCTOR_CALL ( genericTypeArgumentList )? arguments )
                    pass 
                    self.match(self.input, THIS_CONSTRUCTOR_CALL, self.FOLLOW_THIS_CONSTRUCTOR_CALL_in_explicitConstructorCall7484)

                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:821:33: ( genericTypeArgumentList )?
                    alt95 = 2
                    LA95_0 = self.input.LA(1)

                    if (LA95_0 == GENERIC_TYPE_ARG_LIST) :
                        alt95 = 1
                    if alt95 == 1:
                        # JavaTreeParser.g:0:0: genericTypeArgumentList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeArgumentList_in_explicitConstructorCall7486)
                        self.genericTypeArgumentList()

                        self._state.following.pop()



                    self._state.following.append(self.FOLLOW_arguments_in_explicitConstructorCall7489)
                    self.arguments()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt98 == 2:
                    # JavaTreeParser.g:822:9: ^( SUPER_CONSTRUCTOR_CALL (pe0= primaryExpression )? ( genericTypeArgumentList )? (ag0= arguments ) )
                    pass 
                    self.match(self.input, SUPER_CONSTRUCTOR_CALL, self.FOLLOW_SUPER_CONSTRUCTOR_CALL_in_explicitConstructorCall7501)

                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:823:13: (pe0= primaryExpression )?
                    alt96 = 2
                    LA96_0 = self.input.LA(1)

                    if (LA96_0 == DOT or LA96_0 == FALSE or LA96_0 == NULL or LA96_0 == SUPER or LA96_0 == THIS or LA96_0 == TRUE or LA96_0 == ARRAY_DECLARATOR or LA96_0 == ARRAY_ELEMENT_ACCESS or LA96_0 == CLASS_CONSTRUCTOR_CALL or LA96_0 == METHOD_CALL or LA96_0 == PARENTESIZED_EXPR or (STATIC_ARRAY_CREATOR <= LA96_0 <= SUPER_CONSTRUCTOR_CALL) or LA96_0 == THIS_CONSTRUCTOR_CALL or (IDENT <= LA96_0 <= STRING_LITERAL)) :
                        alt96 = 1
                    if alt96 == 1:
                        # JavaTreeParser.g:823:14: pe0= primaryExpression
                        pass 
                        self._state.following.append(self.FOLLOW_primaryExpression_in_explicitConstructorCall7518)
                        pe0 = self.primaryExpression()

                        self._state.following.pop()



                    # JavaTreeParser.g:824:13: ( genericTypeArgumentList )?
                    alt97 = 2
                    LA97_0 = self.input.LA(1)

                    if (LA97_0 == GENERIC_TYPE_ARG_LIST) :
                        alt97 = 1
                    if alt97 == 1:
                        # JavaTreeParser.g:0:0: genericTypeArgumentList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeArgumentList_in_explicitConstructorCall7534)
                        self.genericTypeArgumentList()

                        self._state.following.pop()



                    # JavaTreeParser.g:825:13: (ag0= arguments )
                    # JavaTreeParser.g:825:14: ag0= arguments
                    pass 
                    self._state.following.append(self.FOLLOW_arguments_in_explicitConstructorCall7552)
                    ag0 = self.arguments()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value.update(right=ag0) 





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
    # JavaTreeParser.g:832:1: arrayTypeDeclarator : ^( ARRAY_DECLARATOR ( arrayTypeDeclarator | qualifiedIdentifier | primitiveType ) ) ;
    def arrayTypeDeclarator(self, ):

        arrayTypeDeclarator_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 65):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:833:5: ( ^( ARRAY_DECLARATOR ( arrayTypeDeclarator | qualifiedIdentifier | primitiveType ) ) )
                # JavaTreeParser.g:833:9: ^( ARRAY_DECLARATOR ( arrayTypeDeclarator | qualifiedIdentifier | primitiveType ) )
                pass 
                self.match(self.input, ARRAY_DECLARATOR, self.FOLLOW_ARRAY_DECLARATOR_in_arrayTypeDeclarator7612)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:833:28: ( arrayTypeDeclarator | qualifiedIdentifier | primitiveType )
                alt99 = 3
                LA99 = self.input.LA(1)
                if LA99 == ARRAY_DECLARATOR:
                    alt99 = 1
                elif LA99 == DOT or LA99 == IDENT:
                    alt99 = 2
                elif LA99 == BOOLEAN or LA99 == BYTE or LA99 == CHAR or LA99 == DOUBLE or LA99 == FLOAT or LA99 == INT or LA99 == LONG or LA99 == SHORT:
                    alt99 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 99, 0, self.input)

                    raise nvae

                if alt99 == 1:
                    # JavaTreeParser.g:833:29: arrayTypeDeclarator
                    pass 
                    self._state.following.append(self.FOLLOW_arrayTypeDeclarator_in_arrayTypeDeclarator7615)
                    self.arrayTypeDeclarator()

                    self._state.following.pop()


                elif alt99 == 2:
                    # JavaTreeParser.g:833:51: qualifiedIdentifier
                    pass 
                    self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_arrayTypeDeclarator7619)
                    self.qualifiedIdentifier()

                    self._state.following.pop()


                elif alt99 == 3:
                    # JavaTreeParser.g:833:73: primitiveType
                    pass 
                    self._state.following.append(self.FOLLOW_primitiveType_in_arrayTypeDeclarator7623)
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
    # JavaTreeParser.g:837:1: newExpression returns [value] : ( ^( STATIC_ARRAY_CREATOR (tp0= primitiveType ac0= newArrayConstruction | (gt1= genericTypeArgumentList )? tp1= qualifiedTypeIdent ac1= newArrayConstruction ) ) | ^( CLASS_CONSTRUCTOR_CALL ( genericTypeArgumentList )? q1= qualifiedTypeIdent a1= arguments ( classTopLevelScope )? ) );
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

                # JavaTreeParser.g:838:5: ( ^( STATIC_ARRAY_CREATOR (tp0= primitiveType ac0= newArrayConstruction | (gt1= genericTypeArgumentList )? tp1= qualifiedTypeIdent ac1= newArrayConstruction ) ) | ^( CLASS_CONSTRUCTOR_CALL ( genericTypeArgumentList )? q1= qualifiedTypeIdent a1= arguments ( classTopLevelScope )? ) )
                alt104 = 2
                LA104_0 = self.input.LA(1)

                if (LA104_0 == STATIC_ARRAY_CREATOR) :
                    alt104 = 1
                elif (LA104_0 == CLASS_CONSTRUCTOR_CALL) :
                    alt104 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 104, 0, self.input)

                    raise nvae

                if alt104 == 1:
                    # JavaTreeParser.g:838:9: ^( STATIC_ARRAY_CREATOR (tp0= primitiveType ac0= newArrayConstruction | (gt1= genericTypeArgumentList )? tp1= qualifiedTypeIdent ac1= newArrayConstruction ) )
                    pass 
                    self.match(self.input, STATIC_ARRAY_CREATOR, self.FOLLOW_STATIC_ARRAY_CREATOR_in_newExpression7650)

                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:839:11: (tp0= primitiveType ac0= newArrayConstruction | (gt1= genericTypeArgumentList )? tp1= qualifiedTypeIdent ac1= newArrayConstruction )
                    alt101 = 2
                    LA101_0 = self.input.LA(1)

                    if (LA101_0 == BOOLEAN or LA101_0 == BYTE or LA101_0 == CHAR or LA101_0 == DOUBLE or LA101_0 == FLOAT or (INT <= LA101_0 <= LONG) or LA101_0 == SHORT) :
                        alt101 = 1
                    elif (LA101_0 == GENERIC_TYPE_ARG_LIST or LA101_0 == QUALIFIED_TYPE_IDENT) :
                        alt101 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 101, 0, self.input)

                        raise nvae

                    if alt101 == 1:
                        # JavaTreeParser.g:839:13: tp0= primitiveType ac0= newArrayConstruction
                        pass 
                        self._state.following.append(self.FOLLOW_primitiveType_in_newExpression7666)
                        tp0 = self.primitiveType()

                        self._state.following.pop()
                        self._state.following.append(self.FOLLOW_newArrayConstruction_in_newExpression7670)
                        ac0 = self.newArrayConstruction()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            value = self.makeArrayCreator(((tp0 is not None) and [self.input.getTokenStream().toString(
                                self.input.getTreeAdaptor().getTokenStartIndex(tp0.start),
                                self.input.getTreeAdaptor().getTokenStopIndex(tp0.start)
                                )] or [None])[0], ac0) 



                    elif alt101 == 2:
                        # JavaTreeParser.g:841:13: (gt1= genericTypeArgumentList )? tp1= qualifiedTypeIdent ac1= newArrayConstruction
                        pass 
                        # JavaTreeParser.g:841:16: (gt1= genericTypeArgumentList )?
                        alt100 = 2
                        LA100_0 = self.input.LA(1)

                        if (LA100_0 == GENERIC_TYPE_ARG_LIST) :
                            alt100 = 1
                        if alt100 == 1:
                            # JavaTreeParser.g:0:0: gt1= genericTypeArgumentList
                            pass 
                            self._state.following.append(self.FOLLOW_genericTypeArgumentList_in_newExpression7700)
                            gt1 = self.genericTypeArgumentList()

                            self._state.following.pop()



                        self._state.following.append(self.FOLLOW_qualifiedTypeIdent_in_newExpression7705)
                        tp1 = self.qualifiedTypeIdent()

                        self._state.following.pop()
                        self._state.following.append(self.FOLLOW_newArrayConstruction_in_newExpression7709)
                        ac1 = self.newArrayConstruction()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            value = self.makeArrayCreator(tp1, ac1, gt1) 





                    self.match(self.input, UP, None)


                elif alt104 == 2:
                    # JavaTreeParser.g:846:9: ^( CLASS_CONSTRUCTOR_CALL ( genericTypeArgumentList )? q1= qualifiedTypeIdent a1= arguments ( classTopLevelScope )? )
                    pass 
                    self.match(self.input, CLASS_CONSTRUCTOR_CALL, self.FOLLOW_CLASS_CONSTRUCTOR_CALL_in_newExpression7757)

                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:847:11: ( genericTypeArgumentList )?
                    alt102 = 2
                    LA102_0 = self.input.LA(1)

                    if (LA102_0 == GENERIC_TYPE_ARG_LIST) :
                        alt102 = 1
                    if alt102 == 1:
                        # JavaTreeParser.g:0:0: genericTypeArgumentList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeArgumentList_in_newExpression7769)
                        self.genericTypeArgumentList()

                        self._state.following.pop()



                    self._state.following.append(self.FOLLOW_qualifiedTypeIdent_in_newExpression7784)
                    q1 = self.qualifiedTypeIdent()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_arguments_in_newExpression7798)
                    a1 = self.arguments()

                    self._state.following.pop()
                    # JavaTreeParser.g:850:11: ( classTopLevelScope )?
                    alt103 = 2
                    LA103_0 = self.input.LA(1)

                    if (LA103_0 == CLASS_TOP_LEVEL_SCOPE) :
                        alt103 = 1
                    if alt103 == 1:
                        # JavaTreeParser.g:0:0: classTopLevelScope
                        pass 
                        self._state.following.append(self.FOLLOW_classTopLevelScope_in_newExpression7810)
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
    # JavaTreeParser.g:857:1: innerNewExpression returns [value] : ^( CLASS_CONSTRUCTOR_CALL ( genericTypeArgumentList )? id0= IDENT ag0= arguments ( classTopLevelScope )? ) ;
    def innerNewExpression(self, ):

        value = None
        innerNewExpression_StartIndex = self.input.index()
        id0 = None
        ag0 = None


        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 67):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:858:5: ( ^( CLASS_CONSTRUCTOR_CALL ( genericTypeArgumentList )? id0= IDENT ag0= arguments ( classTopLevelScope )? ) )
                # JavaTreeParser.g:858:9: ^( CLASS_CONSTRUCTOR_CALL ( genericTypeArgumentList )? id0= IDENT ag0= arguments ( classTopLevelScope )? )
                pass 
                self.match(self.input, CLASS_CONSTRUCTOR_CALL, self.FOLLOW_CLASS_CONSTRUCTOR_CALL_in_innerNewExpression7859)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:859:11: ( genericTypeArgumentList )?
                alt105 = 2
                LA105_0 = self.input.LA(1)

                if (LA105_0 == GENERIC_TYPE_ARG_LIST) :
                    alt105 = 1
                if alt105 == 1:
                    # JavaTreeParser.g:0:0: genericTypeArgumentList
                    pass 
                    self._state.following.append(self.FOLLOW_genericTypeArgumentList_in_innerNewExpression7871)
                    self.genericTypeArgumentList()

                    self._state.following.pop()



                id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_innerNewExpression7886)
                self._state.following.append(self.FOLLOW_arguments_in_innerNewExpression7900)
                ag0 = self.arguments()

                self._state.following.pop()
                # JavaTreeParser.g:862:11: ( classTopLevelScope )?
                alt106 = 2
                LA106_0 = self.input.LA(1)

                if (LA106_0 == CLASS_TOP_LEVEL_SCOPE) :
                    alt106 = 1
                if alt106 == 1:
                    # JavaTreeParser.g:0:0: classTopLevelScope
                    pass 
                    self._state.following.append(self.FOLLOW_classTopLevelScope_in_innerNewExpression7912)
                    self.classTopLevelScope()

                    self._state.following.pop()



                if self._state.backtracking == 0:
                    value = ex(self.altIdent(id0.text), ag0, "${left}(${right})", rename=True) 


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
    # JavaTreeParser.g:868:1: newArrayConstruction returns [value] : (ad0= arrayDeclaratorList ai0= arrayInitializer | (ex0= expression )+ ( arrayDeclaratorList )? );
    def newArrayConstruction(self, ):

        value = None
        newArrayConstruction_StartIndex = self.input.index()
        ad0 = None

        ai0 = None

        ex0 = None


        value, format = "", "${right}" 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 68):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:870:5: (ad0= arrayDeclaratorList ai0= arrayInitializer | (ex0= expression )+ ( arrayDeclaratorList )? )
                alt109 = 2
                LA109_0 = self.input.LA(1)

                if (LA109_0 == ARRAY_DECLARATOR_LIST) :
                    alt109 = 1
                elif (LA109_0 == EXPR) :
                    alt109 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 109, 0, self.input)

                    raise nvae

                if alt109 == 1:
                    # JavaTreeParser.g:870:9: ad0= arrayDeclaratorList ai0= arrayInitializer
                    pass 
                    self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_newArrayConstruction7970)
                    ad0 = self.arrayDeclaratorList()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_arrayInitializer_in_newArrayConstruction7974)
                    ai0 = self.arrayInitializer()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ai0 



                elif alt109 == 2:
                    # JavaTreeParser.g:872:9: (ex0= expression )+ ( arrayDeclaratorList )?
                    pass 
                    # JavaTreeParser.g:872:9: (ex0= expression )+
                    cnt107 = 0
                    while True: #loop107
                        alt107 = 2
                        LA107_0 = self.input.LA(1)

                        if (LA107_0 == EXPR) :
                            alt107 = 1


                        if alt107 == 1:
                            # JavaTreeParser.g:872:10: ex0= expression
                            pass 
                            self._state.following.append(self.FOLLOW_expression_in_newArrayConstruction7997)
                            ex0 = self.expression()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                value = ex(value, ex0, format)
                                format = "${left}, ${right}"
                                        



                        else:
                            if cnt107 >= 1:
                                break #loop107

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(107, self.input)
                            raise eee

                        cnt107 += 1


                    # JavaTreeParser.g:876:9: ( arrayDeclaratorList )?
                    alt108 = 2
                    LA108_0 = self.input.LA(1)

                    if (LA108_0 == ARRAY_DECLARATOR_LIST) :
                        alt108 = 1
                    if alt108 == 1:
                        # JavaTreeParser.g:0:0: arrayDeclaratorList
                        pass 
                        self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_newArrayConstruction8019)
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
    # JavaTreeParser.g:880:1: arguments returns [values] : ^( ARGUMENT_LIST (ex0= expression )* ) ;
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

                # JavaTreeParser.g:882:5: ( ^( ARGUMENT_LIST (ex0= expression )* ) )
                # JavaTreeParser.g:882:9: ^( ARGUMENT_LIST (ex0= expression )* )
                pass 
                self.match(self.input, ARGUMENT_LIST, self.FOLLOW_ARGUMENT_LIST_in_arguments8054)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:882:25: (ex0= expression )*
                    while True: #loop110
                        alt110 = 2
                        LA110_0 = self.input.LA(1)

                        if (LA110_0 == EXPR) :
                            alt110 = 1


                        if alt110 == 1:
                            # JavaTreeParser.g:882:26: ex0= expression
                            pass 
                            self._state.following.append(self.FOLLOW_expression_in_arguments8059)
                            ex0 = self.expression()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                values, format = ex(values, ex0, format), "${left}, ${right}" 



                        else:
                            break #loop110



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
    # JavaTreeParser.g:888:1: literal returns [value] : ( HEX_LITERAL | OCTAL_LITERAL | DECIMAL_LITERAL | FLOATING_POINT_LITERAL | CHARACTER_LITERAL | STRING_LITERAL | TRUE | FALSE | NULL );
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

                # JavaTreeParser.g:889:5: ( HEX_LITERAL | OCTAL_LITERAL | DECIMAL_LITERAL | FLOATING_POINT_LITERAL | CHARACTER_LITERAL | STRING_LITERAL | TRUE | FALSE | NULL )
                alt111 = 9
                LA111 = self.input.LA(1)
                if LA111 == HEX_LITERAL:
                    alt111 = 1
                elif LA111 == OCTAL_LITERAL:
                    alt111 = 2
                elif LA111 == DECIMAL_LITERAL:
                    alt111 = 3
                elif LA111 == FLOATING_POINT_LITERAL:
                    alt111 = 4
                elif LA111 == CHARACTER_LITERAL:
                    alt111 = 5
                elif LA111 == STRING_LITERAL:
                    alt111 = 6
                elif LA111 == TRUE:
                    alt111 = 7
                elif LA111 == FALSE:
                    alt111 = 8
                elif LA111 == NULL:
                    alt111 = 9
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 111, 0, self.input)

                    raise nvae

                if alt111 == 1:
                    # JavaTreeParser.g:889:9: HEX_LITERAL
                    pass 
                    self.match(self.input, HEX_LITERAL, self.FOLLOW_HEX_LITERAL_in_literal8107)
                    if self._state.backtracking == 0:
                        retval.value = self.input.toString(retval.start, self.input.LT(-1)) 



                elif alt111 == 2:
                    # JavaTreeParser.g:890:9: OCTAL_LITERAL
                    pass 
                    self.match(self.input, OCTAL_LITERAL, self.FOLLOW_OCTAL_LITERAL_in_literal8130)
                    if self._state.backtracking == 0:
                        retval.value = self.input.toString(retval.start, self.input.LT(-1)) 



                elif alt111 == 3:
                    # JavaTreeParser.g:891:9: DECIMAL_LITERAL
                    pass 
                    self.match(self.input, DECIMAL_LITERAL, self.FOLLOW_DECIMAL_LITERAL_in_literal8151)
                    if self._state.backtracking == 0:
                        retval.value = formatFloatLiteral(self.input.toString(retval.start, self.input.LT(-1))) 



                elif alt111 == 4:
                    # JavaTreeParser.g:892:9: FLOATING_POINT_LITERAL
                    pass 
                    self.match(self.input, FLOATING_POINT_LITERAL, self.FOLLOW_FLOATING_POINT_LITERAL_in_literal8170)
                    if self._state.backtracking == 0:
                        retval.value = formatFloatLiteral(self.input.toString(retval.start, self.input.LT(-1))) 



                elif alt111 == 5:
                    # JavaTreeParser.g:893:9: CHARACTER_LITERAL
                    pass 
                    self.match(self.input, CHARACTER_LITERAL, self.FOLLOW_CHARACTER_LITERAL_in_literal8182)
                    if self._state.backtracking == 0:
                        retval.value = self.input.toString(retval.start, self.input.LT(-1)) 



                elif alt111 == 6:
                    # JavaTreeParser.g:894:9: STRING_LITERAL
                    pass 
                    self.match(self.input, STRING_LITERAL, self.FOLLOW_STRING_LITERAL_in_literal8199)
                    if self._state.backtracking == 0:
                        retval.value = self.input.toString(retval.start, self.input.LT(-1)) 



                elif alt111 == 7:
                    # JavaTreeParser.g:895:9: TRUE
                    pass 
                    self.match(self.input, TRUE, self.FOLLOW_TRUE_in_literal8219)
                    if self._state.backtracking == 0:
                        retval.value = "True" 



                elif alt111 == 8:
                    # JavaTreeParser.g:896:9: FALSE
                    pass 
                    self.match(self.input, FALSE, self.FOLLOW_FALSE_in_literal8249)
                    if self._state.backtracking == 0:
                        retval.value = "False" 



                elif alt111 == 9:
                    # JavaTreeParser.g:897:9: NULL
                    pass 
                    self.match(self.input, NULL, self.FOLLOW_NULL_in_literal8278)
                    if self._state.backtracking == 0:
                        retval.value = "None" 




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

    # $ANTLR start "synpred131_JavaTreeParser"
    def synpred131_JavaTreeParser_fragment(self, ):
        # JavaTreeParser.g:685:11: ( (ex0= expression )* )
        # JavaTreeParser.g:685:11: (ex0= expression )*
        pass 
        # JavaTreeParser.g:685:11: (ex0= expression )*
        while True: #loop142
            alt142 = 2
            LA142_0 = self.input.LA(1)

            if (LA142_0 == EXPR) :
                alt142 = 1


            if alt142 == 1:
                # JavaTreeParser.g:685:12: ex0= expression
                pass 
                self._state.following.append(self.FOLLOW_expression_in_synpred131_JavaTreeParser5421)
                ex0 = self.expression()

                self._state.following.pop()


            else:
                break #loop142




    # $ANTLR end "synpred131_JavaTreeParser"




    # Delegated rules

    def synpred131_JavaTreeParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred131_JavaTreeParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



 

    FOLLOW_JAVA_SOURCE_in_javaSource98 = frozenset([2])
    FOLLOW_annotationList_in_javaSource110 = frozenset([3, 7, 61, 67, 77, 78, 84])
    FOLLOW_packageDeclaration_in_javaSource122 = frozenset([3, 7, 61, 67, 77, 78])
    FOLLOW_importDeclaration_in_javaSource135 = frozenset([3, 7, 61, 67, 77, 78])
    FOLLOW_typeDeclaration_in_javaSource148 = frozenset([3, 7, 61, 67, 77])
    FOLLOW_PACKAGE_in_packageDeclaration180 = frozenset([2])
    FOLLOW_qualifiedIdentifier_in_packageDeclaration184 = frozenset([3])
    FOLLOW_IMPORT_in_importDeclaration217 = frozenset([2])
    FOLLOW_STATIC_in_importDeclaration219 = frozenset([15, 164])
    FOLLOW_qualifiedIdentifier_in_importDeclaration224 = frozenset([3, 16])
    FOLLOW_DOTSTAR_in_importDeclaration227 = frozenset([3])
    FOLLOW_CLASS_in_typeDeclaration274 = frozenset([2])
    FOLLOW_modifierList_in_typeDeclaration300 = frozenset([164])
    FOLLOW_IDENT_in_typeDeclaration316 = frozenset([123, 128, 138, 140])
    FOLLOW_genericTypeParameterList_in_typeDeclaration330 = frozenset([123, 128, 138, 140])
    FOLLOW_extendsClause_in_typeDeclaration346 = frozenset([123, 128, 138, 140])
    FOLLOW_implementsClause_in_typeDeclaration365 = frozenset([123, 128, 138, 140])
    FOLLOW_classTopLevelScope_in_typeDeclaration381 = frozenset([3])
    FOLLOW_INTERFACE_in_typeDeclaration415 = frozenset([2])
    FOLLOW_modifierList_in_typeDeclaration441 = frozenset([164])
    FOLLOW_IDENT_in_typeDeclaration457 = frozenset([128, 138, 139])
    FOLLOW_genericTypeParameterList_in_typeDeclaration471 = frozenset([128, 138, 139])
    FOLLOW_extendsClause_in_typeDeclaration487 = frozenset([128, 138, 139])
    FOLLOW_interfaceTopLevelScope_in_typeDeclaration503 = frozenset([3])
    FOLLOW_ENUM_in_typeDeclaration537 = frozenset([2])
    FOLLOW_modifierList_in_typeDeclaration563 = frozenset([164])
    FOLLOW_IDENT_in_typeDeclaration579 = frozenset([125, 140])
    FOLLOW_implementsClause_in_typeDeclaration596 = frozenset([125, 140])
    FOLLOW_enumTopLevelScope_in_typeDeclaration612 = frozenset([3])
    FOLLOW_AT_in_typeDeclaration646 = frozenset([2])
    FOLLOW_modifierList_in_typeDeclaration672 = frozenset([164])
    FOLLOW_IDENT_in_typeDeclaration688 = frozenset([111])
    FOLLOW_annotationTopLevelScope_in_typeDeclaration702 = frozenset([3])
    FOLLOW_EXTENDS_CLAUSE_in_extendsClause758 = frozenset([2])
    FOLLOW_type_in_extendsClause763 = frozenset([3, 157])
    FOLLOW_IMPLEMENTS_CLAUSE_in_implementsClause802 = frozenset([2])
    FOLLOW_type_in_implementsClause807 = frozenset([3, 157])
    FOLLOW_GENERIC_TYPE_PARAM_LIST_in_genericTypeParameterList832 = frozenset([2])
    FOLLOW_genericTypeParameter_in_genericTypeParameterList834 = frozenset([3, 164])
    FOLLOW_IDENT_in_genericTypeParameter856 = frozenset([2])
    FOLLOW_bound_in_genericTypeParameter858 = frozenset([3])
    FOLLOW_EXTENDS_BOUND_LIST_in_bound880 = frozenset([2])
    FOLLOW_type_in_bound882 = frozenset([3, 157])
    FOLLOW_ENUM_TOP_LEVEL_SCOPE_in_enumTopLevelScope904 = frozenset([2])
    FOLLOW_enumConstant_in_enumTopLevelScope906 = frozenset([3, 123, 128, 138, 140, 164])
    FOLLOW_classTopLevelScope_in_enumTopLevelScope909 = frozenset([3])
    FOLLOW_IDENT_in_enumConstant942 = frozenset([2])
    FOLLOW_annotationList_in_enumConstant954 = frozenset([3, 112, 123, 128, 138, 140])
    FOLLOW_arguments_in_enumConstant969 = frozenset([3, 123, 128, 138, 140])
    FOLLOW_classTopLevelScope_in_enumConstant985 = frozenset([3])
    FOLLOW_CLASS_TOP_LEVEL_SCOPE_in_classTopLevelScope1027 = frozenset([2])
    FOLLOW_classScopeDeclarations_in_classTopLevelScope1029 = frozenset([3, 7, 61, 67, 77, 121, 122, 124, 136, 160, 163])
    FOLLOW_CLASS_INSTANCE_INITIALIZER_in_classScopeDeclarations1072 = frozenset([2])
    FOLLOW_block_in_classScopeDeclarations1074 = frozenset([3])
    FOLLOW_CLASS_STATIC_INITIALIZER_in_classScopeDeclarations1087 = frozenset([2])
    FOLLOW_block_in_classScopeDeclarations1089 = frozenset([3])
    FOLLOW_FUNCTION_METHOD_DECL_in_classScopeDeclarations1102 = frozenset([2])
    FOLLOW_modifierList_in_classScopeDeclarations1129 = frozenset([3, 138, 157])
    FOLLOW_genericTypeParameterList_in_classScopeDeclarations1143 = frozenset([3, 157])
    FOLLOW_type_in_classScopeDeclarations1158 = frozenset([164])
    FOLLOW_IDENT_in_classScopeDeclarations1174 = frozenset([133])
    FOLLOW_formalParameterList_in_classScopeDeclarations1190 = frozenset([3, 114, 117, 156])
    FOLLOW_arrayDeclaratorList_in_classScopeDeclarations1204 = frozenset([3, 117, 156])
    FOLLOW_throwsClause_in_classScopeDeclarations1217 = frozenset([3, 117])
    FOLLOW_block_in_classScopeDeclarations1230 = frozenset([3])
    FOLLOW_VOID_METHOD_DECL_in_classScopeDeclarations1265 = frozenset([2])
    FOLLOW_modifierList_in_classScopeDeclarations1291 = frozenset([138, 164])
    FOLLOW_genericTypeParameterList_in_classScopeDeclarations1305 = frozenset([164])
    FOLLOW_IDENT_in_classScopeDeclarations1320 = frozenset([133])
    FOLLOW_formalParameterList_in_classScopeDeclarations1336 = frozenset([3, 117, 156])
    FOLLOW_throwsClause_in_classScopeDeclarations1350 = frozenset([3, 117])
    FOLLOW_block_in_classScopeDeclarations1363 = frozenset([3])
    FOLLOW_VAR_DECLARATION_in_classScopeDeclarations1399 = frozenset([2])
    FOLLOW_modifierList_in_classScopeDeclarations1413 = frozenset([3, 157])
    FOLLOW_type_in_classScopeDeclarations1427 = frozenset([162])
    FOLLOW_variableDeclaratorList_in_classScopeDeclarations1441 = frozenset([3])
    FOLLOW_CONSTRUCTOR_DECL_in_classScopeDeclarations1475 = frozenset([2])
    FOLLOW_modifierList_in_classScopeDeclarations1501 = frozenset([133, 138])
    FOLLOW_genericTypeParameterList_in_classScopeDeclarations1515 = frozenset([133])
    FOLLOW_formalParameterList_in_classScopeDeclarations1530 = frozenset([117, 156])
    FOLLOW_throwsClause_in_classScopeDeclarations1544 = frozenset([117])
    FOLLOW_block_in_classScopeDeclarations1557 = frozenset([3])
    FOLLOW_typeDeclaration_in_classScopeDeclarations1590 = frozenset([1])
    FOLLOW_INTERFACE_TOP_LEVEL_SCOPE_in_interfaceTopLevelScope1611 = frozenset([2])
    FOLLOW_interfaceScopeDeclarations_in_interfaceTopLevelScope1613 = frozenset([3, 7, 61, 67, 77, 136, 160, 163])
    FOLLOW_FUNCTION_METHOD_DECL_in_interfaceScopeDeclarations1645 = frozenset([2])
    FOLLOW_modifierList_in_interfaceScopeDeclarations1671 = frozenset([3, 138, 157])
    FOLLOW_genericTypeParameterList_in_interfaceScopeDeclarations1685 = frozenset([3, 157])
    FOLLOW_type_in_interfaceScopeDeclarations1700 = frozenset([164])
    FOLLOW_IDENT_in_interfaceScopeDeclarations1716 = frozenset([133])
    FOLLOW_formalParameterList_in_interfaceScopeDeclarations1732 = frozenset([3, 114, 156])
    FOLLOW_arrayDeclaratorList_in_interfaceScopeDeclarations1746 = frozenset([3, 156])
    FOLLOW_throwsClause_in_interfaceScopeDeclarations1759 = frozenset([3])
    FOLLOW_VOID_METHOD_DECL_in_interfaceScopeDeclarations1794 = frozenset([2])
    FOLLOW_modifierList_in_interfaceScopeDeclarations1820 = frozenset([138, 164])
    FOLLOW_genericTypeParameterList_in_interfaceScopeDeclarations1834 = frozenset([164])
    FOLLOW_IDENT_in_interfaceScopeDeclarations1849 = frozenset([133])
    FOLLOW_formalParameterList_in_interfaceScopeDeclarations1865 = frozenset([3, 156])
    FOLLOW_throwsClause_in_interfaceScopeDeclarations1879 = frozenset([3])
    FOLLOW_VAR_DECLARATION_in_interfaceScopeDeclarations1914 = frozenset([2])
    FOLLOW_modifierList_in_interfaceScopeDeclarations1928 = frozenset([3, 157])
    FOLLOW_type_in_interfaceScopeDeclarations1942 = frozenset([162])
    FOLLOW_variableDeclaratorList_in_interfaceScopeDeclarations1956 = frozenset([3])
    FOLLOW_typeDeclaration_in_interfaceScopeDeclarations1989 = frozenset([1])
    FOLLOW_VAR_DECLARATOR_LIST_in_variableDeclaratorList2023 = frozenset([2])
    FOLLOW_variableDeclarator_in_variableDeclaratorList2028 = frozenset([3, 161])
    FOLLOW_VAR_DECLARATOR_in_variableDeclarator2059 = frozenset([2])
    FOLLOW_variableDeclaratorId_in_variableDeclarator2074 = frozenset([3, 116, 126])
    FOLLOW_variableInitializer_in_variableDeclarator2103 = frozenset([3])
    FOLLOW_IDENT_in_variableDeclaratorId2162 = frozenset([2])
    FOLLOW_arrayDeclaratorList_in_variableDeclaratorId2188 = frozenset([3])
    FOLLOW_arrayInitializer_in_variableInitializer2228 = frozenset([1])
    FOLLOW_expression_in_variableInitializer2242 = frozenset([1])
    FOLLOW_LBRACK_in_arrayDeclarator2270 = frozenset([41])
    FOLLOW_RBRACK_in_arrayDeclarator2272 = frozenset([1])
    FOLLOW_ARRAY_DECLARATOR_LIST_in_arrayDeclaratorList2302 = frozenset([2])
    FOLLOW_ARRAY_DECLARATOR_in_arrayDeclaratorList2305 = frozenset([3, 113])
    FOLLOW_ARRAY_INITIALIZER_in_arrayInitializer2340 = frozenset([2])
    FOLLOW_variableInitializer_in_arrayInitializer2357 = frozenset([3, 116, 126])
    FOLLOW_THROWS_CLAUSE_in_throwsClause2417 = frozenset([2])
    FOLLOW_qualifiedIdentifier_in_throwsClause2419 = frozenset([3, 15, 164])
    FOLLOW_MODIFIER_LIST_in_modifierList2455 = frozenset([2])
    FOLLOW_modifier_in_modifierList2460 = frozenset([3, 7, 53, 70, 81, 85, 86, 87, 90, 91, 94, 98, 102])
    FOLLOW_PUBLIC_in_modifier2498 = frozenset([1])
    FOLLOW_PROTECTED_in_modifier2521 = frozenset([1])
    FOLLOW_PRIVATE_in_modifier2541 = frozenset([1])
    FOLLOW_STATIC_in_modifier2563 = frozenset([1])
    FOLLOW_ABSTRACT_in_modifier2586 = frozenset([1])
    FOLLOW_NATIVE_in_modifier2607 = frozenset([1])
    FOLLOW_SYNCHRONIZED_in_modifier2630 = frozenset([1])
    FOLLOW_TRANSIENT_in_modifier2647 = frozenset([1])
    FOLLOW_VOLATILE_in_modifier2667 = frozenset([1])
    FOLLOW_STRICTFP_in_modifier2688 = frozenset([1])
    FOLLOW_localModifier_in_modifier2711 = frozenset([1])
    FOLLOW_LOCAL_MODIFIER_LIST_in_localModifierList2747 = frozenset([2])
    FOLLOW_localModifier_in_localModifierList2752 = frozenset([3, 7, 53, 70, 81, 85, 86, 87, 90, 91, 94, 98, 102])
    FOLLOW_FINAL_in_localModifier2781 = frozenset([1])
    FOLLOW_annotation_in_localModifier2795 = frozenset([1])
    FOLLOW_TYPE_in_type2831 = frozenset([2])
    FOLLOW_primitiveType_in_type2846 = frozenset([3, 114])
    FOLLOW_qualifiedTypeIdent_in_type2865 = frozenset([3, 114])
    FOLLOW_arrayDeclaratorList_in_type2881 = frozenset([3])
    FOLLOW_QUALIFIED_TYPE_IDENT_in_qualifiedTypeIdent2942 = frozenset([2])
    FOLLOW_typeIdent_in_qualifiedTypeIdent2947 = frozenset([3, 164])
    FOLLOW_IDENT_in_typeIdent2979 = frozenset([2])
    FOLLOW_genericTypeArgumentList_in_typeIdent2981 = frozenset([3])
    FOLLOW_set_in_primitiveType0 = frozenset([1])
    FOLLOW_GENERIC_TYPE_ARG_LIST_in_genericTypeArgumentList3100 = frozenset([2])
    FOLLOW_genericTypeArgument_in_genericTypeArgumentList3102 = frozenset([3, 40, 157])
    FOLLOW_type_in_genericTypeArgument3124 = frozenset([1])
    FOLLOW_QUESTION_in_genericTypeArgument3135 = frozenset([2])
    FOLLOW_genericWildcardBoundType_in_genericTypeArgument3137 = frozenset([3])
    FOLLOW_EXTENDS_in_genericWildcardBoundType3160 = frozenset([2])
    FOLLOW_type_in_genericWildcardBoundType3162 = frozenset([3])
    FOLLOW_SUPER_in_genericWildcardBoundType3174 = frozenset([2])
    FOLLOW_type_in_genericWildcardBoundType3176 = frozenset([3])
    FOLLOW_FORMAL_PARAM_LIST_in_formalParameterList3211 = frozenset([2])
    FOLLOW_formalParameterStandardDecl_in_formalParameterList3226 = frozenset([3, 134, 135])
    FOLLOW_formalParameterVarargDecl_in_formalParameterList3245 = frozenset([3])
    FOLLOW_FORMAL_PARAM_STD_DECL_in_formalParameterStandardDecl3286 = frozenset([2])
    FOLLOW_localModifierList_in_formalParameterStandardDecl3300 = frozenset([3, 157])
    FOLLOW_type_in_formalParameterStandardDecl3314 = frozenset([164])
    FOLLOW_variableDeclaratorId_in_formalParameterStandardDecl3328 = frozenset([3])
    FOLLOW_FORMAL_PARAM_VARARG_DECL_in_formalParameterVarargDecl3365 = frozenset([2])
    FOLLOW_localModifierList_in_formalParameterVarargDecl3379 = frozenset([3, 157])
    FOLLOW_type_in_formalParameterVarargDecl3393 = frozenset([164])
    FOLLOW_variableDeclaratorId_in_formalParameterVarargDecl3407 = frozenset([3])
    FOLLOW_IDENT_in_qualifiedIdentifier3443 = frozenset([1])
    FOLLOW_DOT_in_qualifiedIdentifier3464 = frozenset([2])
    FOLLOW_qualifiedIdentifier_in_qualifiedIdentifier3478 = frozenset([164])
    FOLLOW_IDENT_in_qualifiedIdentifier3490 = frozenset([3])
    FOLLOW_ANNOTATION_LIST_in_annotationList3533 = frozenset([2])
    FOLLOW_annotation_in_annotationList3535 = frozenset([3, 7, 53, 70, 81, 85, 86, 87, 90, 91, 94, 98, 102])
    FOLLOW_AT_in_annotation3571 = frozenset([2])
    FOLLOW_qualifiedIdentifier_in_annotation3585 = frozenset([3, 105])
    FOLLOW_annotationInit_in_annotation3602 = frozenset([3])
    FOLLOW_ANNOTATION_INIT_BLOCK_in_annotationInit3663 = frozenset([2])
    FOLLOW_annotationInitializers_in_annotationInit3667 = frozenset([3])
    FOLLOW_ANNOTATION_INIT_KEY_LIST_in_annotationInitializers3704 = frozenset([2])
    FOLLOW_annotationInitializer_in_annotationInitializers3709 = frozenset([3, 164])
    FOLLOW_ANNOTATION_INIT_DEFAULT_KEY_in_annotationInitializers3725 = frozenset([2])
    FOLLOW_annotationElementValue_in_annotationInitializers3727 = frozenset([3])
    FOLLOW_IDENT_in_annotationInitializer3755 = frozenset([2])
    FOLLOW_annotationElementValue_in_annotationInitializer3759 = frozenset([3])
    FOLLOW_ANNOTATION_INIT_ARRAY_ELEMENT_in_annotationElementValue3797 = frozenset([2])
    FOLLOW_annotationElementValue_in_annotationElementValue3799 = frozenset([3, 7, 53, 70, 81, 85, 86, 87, 90, 91, 94, 98, 102, 104, 116, 126])
    FOLLOW_annotation_in_annotationElementValue3811 = frozenset([1])
    FOLLOW_expression_in_annotationElementValue3823 = frozenset([1])
    FOLLOW_ANNOTATION_TOP_LEVEL_SCOPE_in_annotationTopLevelScope3846 = frozenset([2])
    FOLLOW_annotationScopeDeclarations_in_annotationTopLevelScope3848 = frozenset([3, 7, 61, 67, 77, 109, 160])
    FOLLOW_ANNOTATION_METHOD_DECL_in_annotationScopeDeclarations3880 = frozenset([2])
    FOLLOW_modifierList_in_annotationScopeDeclarations3894 = frozenset([3, 157])
    FOLLOW_type_in_annotationScopeDeclarations3908 = frozenset([164])
    FOLLOW_IDENT_in_annotationScopeDeclarations3922 = frozenset([3, 63])
    FOLLOW_annotationDefaultValue_in_annotationScopeDeclarations3937 = frozenset([3])
    FOLLOW_VAR_DECLARATION_in_annotationScopeDeclarations3974 = frozenset([2])
    FOLLOW_modifierList_in_annotationScopeDeclarations3978 = frozenset([3, 157])
    FOLLOW_type_in_annotationScopeDeclarations3982 = frozenset([162])
    FOLLOW_variableDeclaratorList_in_annotationScopeDeclarations3986 = frozenset([3])
    FOLLOW_typeDeclaration_in_annotationScopeDeclarations4008 = frozenset([1])
    FOLLOW_DEFAULT_in_annotationDefaultValue4033 = frozenset([2])
    FOLLOW_annotationElementValue_in_annotationDefaultValue4037 = frozenset([3])
    FOLLOW_BLOCK_SCOPE_in_block4061 = frozenset([2])
    FOLLOW_blockStatement_in_block4063 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_localVariableDeclaration_in_blockStatement4094 = frozenset([1])
    FOLLOW_typeDeclaration_in_blockStatement4104 = frozenset([1])
    FOLLOW_statement_in_blockStatement4116 = frozenset([1])
    FOLLOW_VAR_DECLARATION_in_localVariableDeclaration4139 = frozenset([2])
    FOLLOW_localModifierList_in_localVariableDeclaration4143 = frozenset([3, 157])
    FOLLOW_type_in_localVariableDeclaration4147 = frozenset([162])
    FOLLOW_variableDeclaratorList_in_localVariableDeclaration4151 = frozenset([3])
    FOLLOW_block_in_statement4207 = frozenset([1])
    FOLLOW_ASSERT_in_statement4218 = frozenset([2])
    FOLLOW_expression_in_statement4233 = frozenset([3, 116, 126])
    FOLLOW_expression_in_statement4251 = frozenset([3])
    FOLLOW_IF_in_statement4276 = frozenset([2])
    FOLLOW_parenthesizedExpression_in_statement4290 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_statement_in_statement4304 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_statement_in_statement4321 = frozenset([3])
    FOLLOW_FOR_in_statement4346 = frozenset([2])
    FOLLOW_forInit_in_statement4360 = frozenset([129])
    FOLLOW_forCondition_in_statement4374 = frozenset([132])
    FOLLOW_forUpdater_in_statement4388 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_statement_in_statement4412 = frozenset([3])
    FOLLOW_FOR_EACH_in_statement4445 = frozenset([2])
    FOLLOW_localModifierList_in_statement4469 = frozenset([3, 157])
    FOLLOW_type_in_statement4481 = frozenset([164])
    FOLLOW_IDENT_in_statement4495 = frozenset([116, 126])
    FOLLOW_expression_in_statement4509 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_statement_in_statement4535 = frozenset([3])
    FOLLOW_WHILE_in_statement4570 = frozenset([2])
    FOLLOW_parenthesizedExpression_in_statement4584 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_statement_in_statement4608 = frozenset([3])
    FOLLOW_DO_in_statement4641 = frozenset([2])
    FOLLOW_statement_in_statement4665 = frozenset([146])
    FOLLOW_parenthesizedExpression_in_statement4679 = frozenset([3])
    FOLLOW_TRY_in_statement4712 = frozenset([2])
    FOLLOW_block_in_statement4734 = frozenset([3, 117, 119])
    FOLLOW_catches_in_statement4756 = frozenset([3, 117])
    FOLLOW_block_in_statement4771 = frozenset([3])
    FOLLOW_SWITCH_in_statement4796 = frozenset([2])
    FOLLOW_parenthesizedExpression_in_statement4811 = frozenset([154])
    FOLLOW_switchBlockLabels_in_statement4826 = frozenset([3])
    FOLLOW_SYNCHRONIZED_in_statement4859 = frozenset([2])
    FOLLOW_parenthesizedExpression_in_statement4886 = frozenset([117])
    FOLLOW_block_in_statement4901 = frozenset([3])
    FOLLOW_RETURN_in_statement4935 = frozenset([2])
    FOLLOW_expression_in_statement4962 = frozenset([3])
    FOLLOW_THROW_in_statement4999 = frozenset([2])
    FOLLOW_expression_in_statement5003 = frozenset([3])
    FOLLOW_BREAK_in_statement5017 = frozenset([2])
    FOLLOW_IDENT_in_statement5022 = frozenset([3])
    FOLLOW_CONTINUE_in_statement5041 = frozenset([2])
    FOLLOW_IDENT_in_statement5046 = frozenset([3])
    FOLLOW_LABELED_STATEMENT_in_statement5064 = frozenset([2])
    FOLLOW_IDENT_in_statement5068 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_statement_in_statement5072 = frozenset([3])
    FOLLOW_expression_in_statement5087 = frozenset([1])
    FOLLOW_SEMI_in_statement5099 = frozenset([1])
    FOLLOW_CATCH_CLAUSE_LIST_in_catches5121 = frozenset([2])
    FOLLOW_catchClause_in_catches5123 = frozenset([3, 59])
    FOLLOW_CATCH_in_catchClause5146 = frozenset([2])
    FOLLOW_formalParameterStandardDecl_in_catchClause5160 = frozenset([117])
    FOLLOW_block_in_catchClause5174 = frozenset([3])
    FOLLOW_SWITCH_BLOCK_LABEL_LIST_in_switchBlockLabels5209 = frozenset([2])
    FOLLOW_switchCaseLabel_in_switchBlockLabels5211 = frozenset([3, 58, 63])
    FOLLOW_switchDefaultLabel_in_switchBlockLabels5214 = frozenset([3])
    FOLLOW_CASE_in_switchCaseLabel5237 = frozenset([2])
    FOLLOW_expression_in_switchCaseLabel5253 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_blockStatement_in_switchCaseLabel5269 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_DEFAULT_in_switchDefaultLabel5311 = frozenset([2])
    FOLLOW_blockStatement_in_switchDefaultLabel5335 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_FOR_INIT_in_forInit5390 = frozenset([2])
    FOLLOW_localVariableDeclaration_in_forInit5404 = frozenset([3])
    FOLLOW_expression_in_forInit5421 = frozenset([3, 116, 126])
    FOLLOW_FOR_CONDITION_in_forCondition5470 = frozenset([2])
    FOLLOW_expression_in_forCondition5474 = frozenset([3])
    FOLLOW_FOR_UPDATE_in_forUpdater5512 = frozenset([2])
    FOLLOW_expression_in_forUpdater5517 = frozenset([3, 116, 126])
    FOLLOW_PARENTESIZED_EXPR_in_parenthesizedExpression5548 = frozenset([2])
    FOLLOW_expression_in_parenthesizedExpression5552 = frozenset([3])
    FOLLOW_EXPR_in_expression5579 = frozenset([2])
    FOLLOW_expr_in_expression5583 = frozenset([3])
    FOLLOW_ASSIGN_in_expr5619 = frozenset([2])
    FOLLOW_expr_in_expr5623 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5627 = frozenset([3])
    FOLLOW_PLUS_ASSIGN_in_expr5647 = frozenset([2])
    FOLLOW_expr_in_expr5651 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5655 = frozenset([3])
    FOLLOW_MINUS_ASSIGN_in_expr5670 = frozenset([2])
    FOLLOW_expr_in_expr5674 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5678 = frozenset([3])
    FOLLOW_STAR_ASSIGN_in_expr5692 = frozenset([2])
    FOLLOW_expr_in_expr5696 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5700 = frozenset([3])
    FOLLOW_DIV_ASSIGN_in_expr5715 = frozenset([2])
    FOLLOW_expr_in_expr5719 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5723 = frozenset([3])
    FOLLOW_AND_ASSIGN_in_expr5739 = frozenset([2])
    FOLLOW_expr_in_expr5743 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5747 = frozenset([3])
    FOLLOW_OR_ASSIGN_in_expr5763 = frozenset([2])
    FOLLOW_expr_in_expr5767 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5771 = frozenset([3])
    FOLLOW_XOR_ASSIGN_in_expr5788 = frozenset([2])
    FOLLOW_expr_in_expr5792 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5796 = frozenset([3])
    FOLLOW_MOD_ASSIGN_in_expr5812 = frozenset([2])
    FOLLOW_expr_in_expr5816 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5820 = frozenset([3])
    FOLLOW_BIT_SHIFT_RIGHT_ASSIGN_in_expr5836 = frozenset([2])
    FOLLOW_expr_in_expr5838 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5840 = frozenset([3])
    FOLLOW_SHIFT_RIGHT_ASSIGN_in_expr5852 = frozenset([2])
    FOLLOW_expr_in_expr5854 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5856 = frozenset([3])
    FOLLOW_SHIFT_LEFT_ASSIGN_in_expr5868 = frozenset([2])
    FOLLOW_expr_in_expr5870 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5872 = frozenset([3])
    FOLLOW_QUESTION_in_expr5884 = frozenset([2])
    FOLLOW_expr_in_expr5888 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5892 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5896 = frozenset([3])
    FOLLOW_LOGICAL_OR_in_expr5920 = frozenset([2])
    FOLLOW_expr_in_expr5924 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5928 = frozenset([3])
    FOLLOW_LOGICAL_AND_in_expr5948 = frozenset([2])
    FOLLOW_expr_in_expr5952 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5956 = frozenset([3])
    FOLLOW_OR_in_expr5975 = frozenset([2])
    FOLLOW_expr_in_expr5979 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5983 = frozenset([3])
    FOLLOW_XOR_in_expr6011 = frozenset([2])
    FOLLOW_expr_in_expr6015 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6019 = frozenset([3])
    FOLLOW_AND_in_expr6046 = frozenset([2])
    FOLLOW_expr_in_expr6050 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6054 = frozenset([3])
    FOLLOW_EQUAL_in_expr6081 = frozenset([2])
    FOLLOW_expr_in_expr6085 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6089 = frozenset([3])
    FOLLOW_NOT_EQUAL_in_expr6114 = frozenset([2])
    FOLLOW_expr_in_expr6118 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6122 = frozenset([3])
    FOLLOW_INSTANCEOF_in_expr6143 = frozenset([2])
    FOLLOW_expr_in_expr6147 = frozenset([3, 157])
    FOLLOW_type_in_expr6151 = frozenset([3])
    FOLLOW_LESS_OR_EQUAL_in_expr6175 = frozenset([2])
    FOLLOW_expr_in_expr6179 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6183 = frozenset([3])
    FOLLOW_GREATER_OR_EQUAL_in_expr6200 = frozenset([2])
    FOLLOW_expr_in_expr6204 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6208 = frozenset([3])
    FOLLOW_BIT_SHIFT_RIGHT_in_expr6222 = frozenset([2])
    FOLLOW_expr_in_expr6226 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6230 = frozenset([3])
    FOLLOW_SHIFT_RIGHT_in_expr6290 = frozenset([2])
    FOLLOW_expr_in_expr6294 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6298 = frozenset([3])
    FOLLOW_GREATER_THAN_in_expr6317 = frozenset([2])
    FOLLOW_expr_in_expr6321 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6325 = frozenset([3])
    FOLLOW_SHIFT_LEFT_in_expr6343 = frozenset([2])
    FOLLOW_expr_in_expr6347 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6351 = frozenset([3])
    FOLLOW_LESS_THAN_in_expr6371 = frozenset([2])
    FOLLOW_expr_in_expr6375 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6379 = frozenset([3])
    FOLLOW_PLUS_in_expr6400 = frozenset([2])
    FOLLOW_expr_in_expr6404 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6408 = frozenset([3])
    FOLLOW_MINUS_in_expr6434 = frozenset([2])
    FOLLOW_expr_in_expr6438 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6442 = frozenset([3])
    FOLLOW_STAR_in_expr6467 = frozenset([2])
    FOLLOW_expr_in_expr6471 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6475 = frozenset([3])
    FOLLOW_DIV_in_expr6501 = frozenset([2])
    FOLLOW_expr_in_expr6505 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6509 = frozenset([3])
    FOLLOW_MOD_in_expr6536 = frozenset([2])
    FOLLOW_expr_in_expr6540 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6544 = frozenset([3])
    FOLLOW_UNARY_PLUS_in_expr6571 = frozenset([2])
    FOLLOW_expr_in_expr6575 = frozenset([3])
    FOLLOW_UNARY_MINUS_in_expr6604 = frozenset([2])
    FOLLOW_expr_in_expr6608 = frozenset([3])
    FOLLOW_PRE_INC_in_expr6636 = frozenset([2])
    FOLLOW_expr_in_expr6640 = frozenset([3])
    FOLLOW_PRE_DEC_in_expr6672 = frozenset([2])
    FOLLOW_expr_in_expr6676 = frozenset([3])
    FOLLOW_POST_INC_in_expr6708 = frozenset([2])
    FOLLOW_expr_in_expr6712 = frozenset([3])
    FOLLOW_POST_DEC_in_expr6743 = frozenset([2])
    FOLLOW_expr_in_expr6747 = frozenset([3])
    FOLLOW_NOT_in_expr6778 = frozenset([2])
    FOLLOW_expr_in_expr6782 = frozenset([3])
    FOLLOW_LOGICAL_NOT_in_expr6818 = frozenset([2])
    FOLLOW_expr_in_expr6822 = frozenset([3])
    FOLLOW_CAST_EXPR_in_expr6850 = frozenset([2])
    FOLLOW_type_in_expr6854 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6858 = frozenset([3])
    FOLLOW_primaryExpression_in_expr6880 = frozenset([1])
    FOLLOW_DOT_in_primaryExpression6925 = frozenset([2])
    FOLLOW_primaryExpression_in_primaryExpression6945 = frozenset([61, 92, 95, 120, 164])
    FOLLOW_IDENT_in_primaryExpression6985 = frozenset([3])
    FOLLOW_THIS_in_primaryExpression7029 = frozenset([3])
    FOLLOW_SUPER_in_primaryExpression7055 = frozenset([3])
    FOLLOW_innerNewExpression_in_primaryExpression7095 = frozenset([3])
    FOLLOW_CLASS_in_primaryExpression7119 = frozenset([3])
    FOLLOW_primitiveType_in_primaryExpression7159 = frozenset([61])
    FOLLOW_CLASS_in_primaryExpression7161 = frozenset([3])
    FOLLOW_VOID_in_primaryExpression7181 = frozenset([61])
    FOLLOW_CLASS_in_primaryExpression7183 = frozenset([3])
    FOLLOW_parenthesizedExpression_in_primaryExpression7220 = frozenset([1])
    FOLLOW_IDENT_in_primaryExpression7233 = frozenset([1])
    FOLLOW_METHOD_CALL_in_primaryExpression7247 = frozenset([2])
    FOLLOW_primaryExpression_in_primaryExpression7261 = frozenset([112, 137])
    FOLLOW_genericTypeArgumentList_in_primaryExpression7273 = frozenset([112])
    FOLLOW_arguments_in_primaryExpression7288 = frozenset([3])
    FOLLOW_explicitConstructorCall_in_primaryExpression7323 = frozenset([1])
    FOLLOW_ARRAY_ELEMENT_ACCESS_in_primaryExpression7337 = frozenset([2])
    FOLLOW_primaryExpression_in_primaryExpression7351 = frozenset([116, 126])
    FOLLOW_expression_in_primaryExpression7365 = frozenset([3])
    FOLLOW_literal_in_primaryExpression7398 = frozenset([1])
    FOLLOW_newExpression_in_primaryExpression7411 = frozenset([1])
    FOLLOW_THIS_in_primaryExpression7424 = frozenset([1])
    FOLLOW_arrayTypeDeclarator_in_primaryExpression7437 = frozenset([1])
    FOLLOW_SUPER_in_primaryExpression7448 = frozenset([1])
    FOLLOW_THIS_CONSTRUCTOR_CALL_in_explicitConstructorCall7484 = frozenset([2])
    FOLLOW_genericTypeArgumentList_in_explicitConstructorCall7486 = frozenset([112])
    FOLLOW_arguments_in_explicitConstructorCall7489 = frozenset([3])
    FOLLOW_SUPER_CONSTRUCTOR_CALL_in_explicitConstructorCall7501 = frozenset([2])
    FOLLOW_primaryExpression_in_explicitConstructorCall7518 = frozenset([112, 137])
    FOLLOW_genericTypeArgumentList_in_explicitConstructorCall7534 = frozenset([112])
    FOLLOW_arguments_in_explicitConstructorCall7552 = frozenset([3])
    FOLLOW_ARRAY_DECLARATOR_in_arrayTypeDeclarator7612 = frozenset([2])
    FOLLOW_arrayTypeDeclarator_in_arrayTypeDeclarator7615 = frozenset([3])
    FOLLOW_qualifiedIdentifier_in_arrayTypeDeclarator7619 = frozenset([3])
    FOLLOW_primitiveType_in_arrayTypeDeclarator7623 = frozenset([3])
    FOLLOW_STATIC_ARRAY_CREATOR_in_newExpression7650 = frozenset([2])
    FOLLOW_primitiveType_in_newExpression7666 = frozenset([114, 116, 126])
    FOLLOW_newArrayConstruction_in_newExpression7670 = frozenset([3])
    FOLLOW_genericTypeArgumentList_in_newExpression7700 = frozenset([151])
    FOLLOW_qualifiedTypeIdent_in_newExpression7705 = frozenset([114, 116, 126])
    FOLLOW_newArrayConstruction_in_newExpression7709 = frozenset([3])
    FOLLOW_CLASS_CONSTRUCTOR_CALL_in_newExpression7757 = frozenset([2])
    FOLLOW_genericTypeArgumentList_in_newExpression7769 = frozenset([151])
    FOLLOW_qualifiedTypeIdent_in_newExpression7784 = frozenset([112])
    FOLLOW_arguments_in_newExpression7798 = frozenset([3, 123, 128, 138, 140])
    FOLLOW_classTopLevelScope_in_newExpression7810 = frozenset([3])
    FOLLOW_CLASS_CONSTRUCTOR_CALL_in_innerNewExpression7859 = frozenset([2])
    FOLLOW_genericTypeArgumentList_in_innerNewExpression7871 = frozenset([164])
    FOLLOW_IDENT_in_innerNewExpression7886 = frozenset([112])
    FOLLOW_arguments_in_innerNewExpression7900 = frozenset([3, 123, 128, 138, 140])
    FOLLOW_classTopLevelScope_in_innerNewExpression7912 = frozenset([3])
    FOLLOW_arrayDeclaratorList_in_newArrayConstruction7970 = frozenset([116])
    FOLLOW_arrayInitializer_in_newArrayConstruction7974 = frozenset([1])
    FOLLOW_expression_in_newArrayConstruction7997 = frozenset([1, 114, 116, 126])
    FOLLOW_arrayDeclaratorList_in_newArrayConstruction8019 = frozenset([1])
    FOLLOW_ARGUMENT_LIST_in_arguments8054 = frozenset([2])
    FOLLOW_expression_in_arguments8059 = frozenset([3, 116, 126])
    FOLLOW_HEX_LITERAL_in_literal8107 = frozenset([1])
    FOLLOW_OCTAL_LITERAL_in_literal8130 = frozenset([1])
    FOLLOW_DECIMAL_LITERAL_in_literal8151 = frozenset([1])
    FOLLOW_FLOATING_POINT_LITERAL_in_literal8170 = frozenset([1])
    FOLLOW_CHARACTER_LITERAL_in_literal8182 = frozenset([1])
    FOLLOW_STRING_LITERAL_in_literal8199 = frozenset([1])
    FOLLOW_TRUE_in_literal8219 = frozenset([1])
    FOLLOW_FALSE_in_literal8249 = frozenset([1])
    FOLLOW_NULL_in_literal8278 = frozenset([1])
    FOLLOW_expression_in_synpred131_JavaTreeParser5421 = frozenset([1, 116, 126])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(JavaTreeParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
