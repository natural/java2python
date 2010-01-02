# $ANTLR 3.1.1 JavaTreeParser.g 2009-12-29 14:19:50

import sys
from antlr3 import *
from antlr3.tree import *
from antlr3.compat import set, frozenset
                     
from java2python import expression as ex, parameter as px, formatFloat
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
                self._state.following.append(self.FOLLOW_annotationList_in_javaSource110)
                self.annotationList()

                self._state.following.pop()
                # JavaTreeParser.g:67:11: ( packageDeclaration )?
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



                # JavaTreeParser.g:68:11: ( importDeclaration )*
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


                # JavaTreeParser.g:69:11: ( typeDeclaration )*
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
    # JavaTreeParser.g:79:1: importDeclaration : ^( IMPORT ( STATIC )? qi0= qualifiedIdentifier ( DOTSTAR )? ) ;
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

                # JavaTreeParser.g:81:5: ( ^( IMPORT ( STATIC )? qi0= qualifiedIdentifier ( DOTSTAR )? ) )
                # JavaTreeParser.g:81:9: ^( IMPORT ( STATIC )? qi0= qualifiedIdentifier ( DOTSTAR )? )
                pass 
                self.match(self.input, IMPORT, self.FOLLOW_IMPORT_in_importDeclaration217)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:81:18: ( STATIC )?
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
                # JavaTreeParser.g:81:50: ( DOTSTAR )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == DOTSTAR) :
                    alt5 = 1
                if alt5 == 1:
                    # JavaTreeParser.g:81:51: DOTSTAR
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

            self.value = None




    # $ANTLR start "typeDeclaration"
    # JavaTreeParser.g:87:1: typeDeclaration returns [value] : ( ^( CLASS md0= modifierList id0= IDENT ( genericTypeParameterList )? (ec0= extendsClause )? (ic0= implementsClause )? classTopLevelScope ) | ^( INTERFACE md0= modifierList id0= IDENT ( genericTypeParameterList )? (ec0= extendsClause )? interfaceTopLevelScope ) | ^( ENUM md0= modifierList id0= IDENT (ic0= implementsClause )? enumTopLevelScope ) | ^( AT md0= modifierList id0= IDENT annotationTopLevelScope ) );
    def typeDeclaration(self, ):

        retval = self.typeDeclaration_return()
        retval.start = self.input.LT(1)
        typeDeclaration_StartIndex = self.input.index()
        id0 = None
        md0 = None

        ec0 = None

        ic0 = None


        self.commentHandler(retval.start) 
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
                    self.match(self.input, CLASS, self.FOLLOW_CLASS_in_typeDeclaration287)

                    if self._state.backtracking == 0:
                        self.beginClassDeclaration() 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_typeDeclaration313)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addModifiers(md0) 

                    id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_typeDeclaration329)
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
                        self._state.following.append(self.FOLLOW_genericTypeParameterList_in_typeDeclaration343)
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
                        self._state.following.append(self.FOLLOW_extendsClause_in_typeDeclaration359)
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
                        self._state.following.append(self.FOLLOW_implementsClause_in_typeDeclaration378)
                        ic0 = self.implementsClause()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self.addBases(ic0) 




                    self._state.following.append(self.FOLLOW_classTopLevelScope_in_typeDeclaration394)
                    self.classTopLevelScope()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        retval.value = self.endClassDeclaration() 


                    self.match(self.input, UP, None)


                elif alt12 == 2:
                    # JavaTreeParser.g:99:9: ^( INTERFACE md0= modifierList id0= IDENT ( genericTypeParameterList )? (ec0= extendsClause )? interfaceTopLevelScope )
                    pass 
                    self.match(self.input, INTERFACE, self.FOLLOW_INTERFACE_in_typeDeclaration427)

                    if self._state.backtracking == 0:
                        self.beginInterfaceDeclaration() 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_typeDeclaration453)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addModifiers(md0) 

                    id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_typeDeclaration469)
                    if self._state.backtracking == 0:
                        self.setIdent(ident=id0.text) 

                    # JavaTreeParser.g:103:11: ( genericTypeParameterList )?
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == GENERIC_TYPE_PARAM_LIST) :
                        alt9 = 1
                    if alt9 == 1:
                        # JavaTreeParser.g:0:0: genericTypeParameterList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeParameterList_in_typeDeclaration483)
                        self.genericTypeParameterList()

                        self._state.following.pop()



                    # JavaTreeParser.g:104:11: (ec0= extendsClause )?
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == EXTENDS_CLAUSE) :
                        alt10 = 1
                    if alt10 == 1:
                        # JavaTreeParser.g:104:12: ec0= extendsClause
                        pass 
                        self._state.following.append(self.FOLLOW_extendsClause_in_typeDeclaration499)
                        ec0 = self.extendsClause()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self.addBases(ec0) 




                    self._state.following.append(self.FOLLOW_interfaceTopLevelScope_in_typeDeclaration515)
                    self.interfaceTopLevelScope()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        retval.value = self.endInterfaceDeclaration() 


                    self.match(self.input, UP, None)


                elif alt12 == 3:
                    # JavaTreeParser.g:108:9: ^( ENUM md0= modifierList id0= IDENT (ic0= implementsClause )? enumTopLevelScope )
                    pass 
                    self.match(self.input, ENUM, self.FOLLOW_ENUM_in_typeDeclaration548)

                    if self._state.backtracking == 0:
                        self.beginEnumerationDeclaration() 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_typeDeclaration574)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addModifiers(md0) 

                    id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_typeDeclaration590)
                    if self._state.backtracking == 0:
                        self.setIdent(ident=id0.text) 

                    # JavaTreeParser.g:112:11: (ic0= implementsClause )?
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == IMPLEMENTS_CLAUSE) :
                        alt11 = 1
                    if alt11 == 1:
                        # JavaTreeParser.g:112:12: ic0= implementsClause
                        pass 
                        self._state.following.append(self.FOLLOW_implementsClause_in_typeDeclaration607)
                        ic0 = self.implementsClause()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self.addBases(ic0) 




                    self._state.following.append(self.FOLLOW_enumTopLevelScope_in_typeDeclaration623)
                    self.enumTopLevelScope()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        retval.value = self.endEnumerationDeclaration() 


                    self.match(self.input, UP, None)


                elif alt12 == 4:
                    # JavaTreeParser.g:116:9: ^( AT md0= modifierList id0= IDENT annotationTopLevelScope )
                    pass 
                    self.match(self.input, AT, self.FOLLOW_AT_in_typeDeclaration656)

                    if self._state.backtracking == 0:
                        self.beginAnnotationDeclaration() 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_typeDeclaration682)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addModifiers(md0) 

                    id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_typeDeclaration698)
                    if self._state.backtracking == 0:
                        self.setIdent(ident=id0.text) 

                    self._state.following.append(self.FOLLOW_annotationTopLevelScope_in_typeDeclaration712)
                    self.annotationTopLevelScope()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        retval.value = self.endAnnotationDeclration() 


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
    # JavaTreeParser.g:126:1: extendsClause returns [values] : ^( EXTENDS_CLAUSE (tp0= type )+ ) ;
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

                # JavaTreeParser.g:128:5: ( ^( EXTENDS_CLAUSE (tp0= type )+ ) )
                # JavaTreeParser.g:128:9: ^( EXTENDS_CLAUSE (tp0= type )+ )
                pass 
                self.match(self.input, EXTENDS_CLAUSE, self.FOLLOW_EXTENDS_CLAUSE_in_extendsClause768)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:128:26: (tp0= type )+
                cnt13 = 0
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == TYPE) :
                        alt13 = 1


                    if alt13 == 1:
                        # JavaTreeParser.g:128:27: tp0= type
                        pass 
                        self._state.following.append(self.FOLLOW_type_in_extendsClause773)
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
    # JavaTreeParser.g:132:1: implementsClause returns [values] : ^( IMPLEMENTS_CLAUSE (tp0= type )+ ) ;
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

                # JavaTreeParser.g:134:5: ( ^( IMPLEMENTS_CLAUSE (tp0= type )+ ) )
                # JavaTreeParser.g:134:9: ^( IMPLEMENTS_CLAUSE (tp0= type )+ )
                pass 
                self.match(self.input, IMPLEMENTS_CLAUSE, self.FOLLOW_IMPLEMENTS_CLAUSE_in_implementsClause812)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:134:29: (tp0= type )+
                cnt14 = 0
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == TYPE) :
                        alt14 = 1


                    if alt14 == 1:
                        # JavaTreeParser.g:134:30: tp0= type
                        pass 
                        self._state.following.append(self.FOLLOW_type_in_implementsClause817)
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
    # JavaTreeParser.g:137:1: genericTypeParameterList : ^( GENERIC_TYPE_PARAM_LIST ( genericTypeParameter )+ ) ;
    def genericTypeParameterList(self, ):

        genericTypeParameterList_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 7):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:138:5: ( ^( GENERIC_TYPE_PARAM_LIST ( genericTypeParameter )+ ) )
                # JavaTreeParser.g:138:9: ^( GENERIC_TYPE_PARAM_LIST ( genericTypeParameter )+ )
                pass 
                self.match(self.input, GENERIC_TYPE_PARAM_LIST, self.FOLLOW_GENERIC_TYPE_PARAM_LIST_in_genericTypeParameterList842)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:138:35: ( genericTypeParameter )+
                cnt15 = 0
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == IDENT) :
                        alt15 = 1


                    if alt15 == 1:
                        # JavaTreeParser.g:0:0: genericTypeParameter
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeParameter_in_genericTypeParameterList844)
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
    # JavaTreeParser.g:141:1: genericTypeParameter : ^( IDENT ( bound )? ) ;
    def genericTypeParameter(self, ):

        genericTypeParameter_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 8):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:142:5: ( ^( IDENT ( bound )? ) )
                # JavaTreeParser.g:142:9: ^( IDENT ( bound )? )
                pass 
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_genericTypeParameter866)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:142:17: ( bound )?
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == EXTENDS_BOUND_LIST) :
                        alt16 = 1
                    if alt16 == 1:
                        # JavaTreeParser.g:0:0: bound
                        pass 
                        self._state.following.append(self.FOLLOW_bound_in_genericTypeParameter868)
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
    # JavaTreeParser.g:145:1: bound : ^( EXTENDS_BOUND_LIST ( type )+ ) ;
    def bound(self, ):

        bound_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 9):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:146:5: ( ^( EXTENDS_BOUND_LIST ( type )+ ) )
                # JavaTreeParser.g:146:9: ^( EXTENDS_BOUND_LIST ( type )+ )
                pass 
                self.match(self.input, EXTENDS_BOUND_LIST, self.FOLLOW_EXTENDS_BOUND_LIST_in_bound890)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:146:30: ( type )+
                cnt17 = 0
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == TYPE) :
                        alt17 = 1


                    if alt17 == 1:
                        # JavaTreeParser.g:0:0: type
                        pass 
                        self._state.following.append(self.FOLLOW_type_in_bound892)
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
    # JavaTreeParser.g:149:1: enumTopLevelScope : ^( ENUM_TOP_LEVEL_SCOPE ( enumConstant )+ ( classTopLevelScope )? ) ;
    def enumTopLevelScope(self, ):

        enumTopLevelScope_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 10):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:150:5: ( ^( ENUM_TOP_LEVEL_SCOPE ( enumConstant )+ ( classTopLevelScope )? ) )
                # JavaTreeParser.g:150:9: ^( ENUM_TOP_LEVEL_SCOPE ( enumConstant )+ ( classTopLevelScope )? )
                pass 
                self.match(self.input, ENUM_TOP_LEVEL_SCOPE, self.FOLLOW_ENUM_TOP_LEVEL_SCOPE_in_enumTopLevelScope914)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:150:32: ( enumConstant )+
                cnt18 = 0
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == IDENT) :
                        alt18 = 1


                    if alt18 == 1:
                        # JavaTreeParser.g:0:0: enumConstant
                        pass 
                        self._state.following.append(self.FOLLOW_enumConstant_in_enumTopLevelScope916)
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


                # JavaTreeParser.g:150:46: ( classTopLevelScope )?
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == CLASS_TOP_LEVEL_SCOPE) :
                    alt19 = 1
                if alt19 == 1:
                    # JavaTreeParser.g:0:0: classTopLevelScope
                    pass 
                    self._state.following.append(self.FOLLOW_classTopLevelScope_in_enumTopLevelScope919)
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
    # JavaTreeParser.g:153:1: enumConstant : ^(id0= IDENT (an0= annotationList ) (ag0= arguments )? ( classTopLevelScope )? ) ;
    def enumConstant(self, ):

        enumConstant_StartIndex = self.input.index()
        id0 = None
        an0 = None

        ag0 = None


        annos = args = None 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 11):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:155:5: ( ^(id0= IDENT (an0= annotationList ) (ag0= arguments )? ( classTopLevelScope )? ) )
                # JavaTreeParser.g:155:9: ^(id0= IDENT (an0= annotationList ) (ag0= arguments )? ( classTopLevelScope )? )
                pass 
                id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_enumConstant952)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:156:11: (an0= annotationList )
                # JavaTreeParser.g:156:12: an0= annotationList
                pass 
                self._state.following.append(self.FOLLOW_annotationList_in_enumConstant967)
                an0 = self.annotationList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    annos = an0 




                # JavaTreeParser.g:157:11: (ag0= arguments )?
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == ARGUMENT_LIST) :
                    alt20 = 1
                if alt20 == 1:
                    # JavaTreeParser.g:157:12: ag0= arguments
                    pass 
                    self._state.following.append(self.FOLLOW_arguments_in_enumConstant985)
                    ag0 = self.arguments()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        args = ag0 




                # JavaTreeParser.g:158:11: ( classTopLevelScope )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == CLASS_TOP_LEVEL_SCOPE) :
                    alt21 = 1
                if alt21 == 1:
                    # JavaTreeParser.g:0:0: classTopLevelScope
                    pass 
                    self._state.following.append(self.FOLLOW_classTopLevelScope_in_enumConstant1001)
                    self.classTopLevelScope()

                    self._state.following.pop()




                self.match(self.input, UP, None)
                if self._state.backtracking == 0:
                    self.addEnumValue(id0.text, args, annos) 





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
    # JavaTreeParser.g:164:1: classTopLevelScope : ^( CLASS_TOP_LEVEL_SCOPE ( classScopeDeclarations )* ) ;
    def classTopLevelScope(self, ):

        classTopLevelScope_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 12):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:165:5: ( ^( CLASS_TOP_LEVEL_SCOPE ( classScopeDeclarations )* ) )
                # JavaTreeParser.g:165:9: ^( CLASS_TOP_LEVEL_SCOPE ( classScopeDeclarations )* )
                pass 
                self.match(self.input, CLASS_TOP_LEVEL_SCOPE, self.FOLLOW_CLASS_TOP_LEVEL_SCOPE_in_classTopLevelScope1043)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:165:33: ( classScopeDeclarations )*
                    while True: #loop22
                        alt22 = 2
                        LA22_0 = self.input.LA(1)

                        if (LA22_0 == AT or LA22_0 == CLASS or LA22_0 == ENUM or LA22_0 == INTERFACE or (CLASS_INSTANCE_INITIALIZER <= LA22_0 <= CLASS_STATIC_INITIALIZER) or LA22_0 == CONSTRUCTOR_DECL or LA22_0 == FUNCTION_METHOD_DECL or LA22_0 == VAR_DECLARATION or LA22_0 == VOID_METHOD_DECL) :
                            alt22 = 1


                        if alt22 == 1:
                            # JavaTreeParser.g:0:0: classScopeDeclarations
                            pass 
                            self._state.following.append(self.FOLLOW_classScopeDeclarations_in_classTopLevelScope1045)
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
    # JavaTreeParser.g:169:1: classScopeDeclarations : ( ^( CLASS_INSTANCE_INITIALIZER block ) | ^( CLASS_STATIC_INITIALIZER block ) | ^( FUNCTION_METHOD_DECL md0= modifierList ( genericTypeParameterList )? tp0= type id0= IDENT fp0= formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block )? ) | ^( VOID_METHOD_DECL md0= modifierList ( genericTypeParameterList )? id0= IDENT fp0= formalParameterList ( throwsClause )? ( block )? ) | ^( VAR_DECLARATION md0= modifierList tp0= type vd0= variableDeclaratorList ) | ^( CONSTRUCTOR_DECL md0= modifierList ( genericTypeParameterList )? fp0= formalParameterList ( throwsClause )? block ) | typeDeclaration );
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

                # JavaTreeParser.g:175:5: ( ^( CLASS_INSTANCE_INITIALIZER block ) | ^( CLASS_STATIC_INITIALIZER block ) | ^( FUNCTION_METHOD_DECL md0= modifierList ( genericTypeParameterList )? tp0= type id0= IDENT fp0= formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block )? ) | ^( VOID_METHOD_DECL md0= modifierList ( genericTypeParameterList )? id0= IDENT fp0= formalParameterList ( throwsClause )? ( block )? ) | ^( VAR_DECLARATION md0= modifierList tp0= type vd0= variableDeclaratorList ) | ^( CONSTRUCTOR_DECL md0= modifierList ( genericTypeParameterList )? fp0= formalParameterList ( throwsClause )? block ) | typeDeclaration )
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
                    # JavaTreeParser.g:175:9: ^( CLASS_INSTANCE_INITIALIZER block )
                    pass 
                    self.match(self.input, CLASS_INSTANCE_INITIALIZER, self.FOLLOW_CLASS_INSTANCE_INITIALIZER_in_classScopeDeclarations1087)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_block_in_classScopeDeclarations1089)
                    self.block()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt32 == 2:
                    # JavaTreeParser.g:176:9: ^( CLASS_STATIC_INITIALIZER block )
                    pass 
                    self.match(self.input, CLASS_STATIC_INITIALIZER, self.FOLLOW_CLASS_STATIC_INITIALIZER_in_classScopeDeclarations1101)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_block_in_classScopeDeclarations1103)
                    self.block()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt32 == 3:
                    # JavaTreeParser.g:177:9: ^( FUNCTION_METHOD_DECL md0= modifierList ( genericTypeParameterList )? tp0= type id0= IDENT fp0= formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block )? )
                    pass 
                    self.match(self.input, FUNCTION_METHOD_DECL, self.FOLLOW_FUNCTION_METHOD_DECL_in_classScopeDeclarations1115)

                    if self._state.backtracking == 0:
                        self.beginMethodDecl() 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_classScopeDeclarations1141)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addModifiers(md0) 

                    # JavaTreeParser.g:180:11: ( genericTypeParameterList )?
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == GENERIC_TYPE_PARAM_LIST) :
                        alt23 = 1
                    if alt23 == 1:
                        # JavaTreeParser.g:0:0: genericTypeParameterList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeParameterList_in_classScopeDeclarations1155)
                        self.genericTypeParameterList()

                        self._state.following.pop()



                    self._state.following.append(self.FOLLOW_type_in_classScopeDeclarations1170)
                    tp0 = self.type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.setType(((tp0 is not None) and [tp0.value] or [None])[0]) 

                    id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_classScopeDeclarations1186)
                    if self._state.backtracking == 0:
                        self.setIdent(ident=id0.text) 

                    self._state.following.append(self.FOLLOW_formalParameterList_in_classScopeDeclarations1202)
                    fp0 = self.formalParameterList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addParameters(fp0) 

                    # JavaTreeParser.g:184:11: ( arrayDeclaratorList )?
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == ARRAY_DECLARATOR_LIST) :
                        alt24 = 1
                    if alt24 == 1:
                        # JavaTreeParser.g:0:0: arrayDeclaratorList
                        pass 
                        self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_classScopeDeclarations1216)
                        self.arrayDeclaratorList()

                        self._state.following.pop()



                    # JavaTreeParser.g:185:11: ( throwsClause )?
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == THROWS_CLAUSE) :
                        alt25 = 1
                    if alt25 == 1:
                        # JavaTreeParser.g:0:0: throwsClause
                        pass 
                        self._state.following.append(self.FOLLOW_throwsClause_in_classScopeDeclarations1229)
                        self.throwsClause()

                        self._state.following.pop()



                    # JavaTreeParser.g:186:11: ( block )?
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == BLOCK_SCOPE) :
                        alt26 = 1
                    if alt26 == 1:
                        # JavaTreeParser.g:0:0: block
                        pass 
                        self._state.following.append(self.FOLLOW_block_in_classScopeDeclarations1242)
                        self.block()

                        self._state.following.pop()



                    if self._state.backtracking == 0:
                        self.endMethodDecl() 


                    self.match(self.input, UP, None)


                elif alt32 == 4:
                    # JavaTreeParser.g:189:9: ^( VOID_METHOD_DECL md0= modifierList ( genericTypeParameterList )? id0= IDENT fp0= formalParameterList ( throwsClause )? ( block )? )
                    pass 
                    self.match(self.input, VOID_METHOD_DECL, self.FOLLOW_VOID_METHOD_DECL_in_classScopeDeclarations1276)

                    if self._state.backtracking == 0:
                        self.beginMethodDecl(type="void") 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_classScopeDeclarations1302)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addModifiers(md0) 

                    # JavaTreeParser.g:192:11: ( genericTypeParameterList )?
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == GENERIC_TYPE_PARAM_LIST) :
                        alt27 = 1
                    if alt27 == 1:
                        # JavaTreeParser.g:0:0: genericTypeParameterList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeParameterList_in_classScopeDeclarations1316)
                        self.genericTypeParameterList()

                        self._state.following.pop()



                    id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_classScopeDeclarations1331)
                    if self._state.backtracking == 0:
                        self.setIdent(ident=id0.text) 

                    self._state.following.append(self.FOLLOW_formalParameterList_in_classScopeDeclarations1347)
                    fp0 = self.formalParameterList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addParameters(fp0) 

                    # JavaTreeParser.g:195:11: ( throwsClause )?
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == THROWS_CLAUSE) :
                        alt28 = 1
                    if alt28 == 1:
                        # JavaTreeParser.g:0:0: throwsClause
                        pass 
                        self._state.following.append(self.FOLLOW_throwsClause_in_classScopeDeclarations1361)
                        self.throwsClause()

                        self._state.following.pop()



                    # JavaTreeParser.g:196:11: ( block )?
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if (LA29_0 == BLOCK_SCOPE) :
                        alt29 = 1
                    if alt29 == 1:
                        # JavaTreeParser.g:0:0: block
                        pass 
                        self._state.following.append(self.FOLLOW_block_in_classScopeDeclarations1374)
                        self.block()

                        self._state.following.pop()



                    if self._state.backtracking == 0:
                        self.endMethodDecl() 


                    self.match(self.input, UP, None)


                elif alt32 == 5:
                    # JavaTreeParser.g:199:9: ^( VAR_DECLARATION md0= modifierList tp0= type vd0= variableDeclaratorList )
                    pass 
                    self.match(self.input, VAR_DECLARATION, self.FOLLOW_VAR_DECLARATION_in_classScopeDeclarations1409)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_classScopeDeclarations1423)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_type_in_classScopeDeclarations1437)
                    tp0 = self.type()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_variableDeclaratorList_in_classScopeDeclarations1451)
                    vd0 = self.variableDeclaratorList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addVariables(vd0, ((tp0 is not None) and [tp0.value] or [None])[0], md0, cls=True) 


                    self.match(self.input, UP, None)


                elif alt32 == 6:
                    # JavaTreeParser.g:205:9: ^( CONSTRUCTOR_DECL md0= modifierList ( genericTypeParameterList )? fp0= formalParameterList ( throwsClause )? block )
                    pass 
                    self.match(self.input, CONSTRUCTOR_DECL, self.FOLLOW_CONSTRUCTOR_DECL_in_classScopeDeclarations1484)

                    if self._state.backtracking == 0:
                        self.beginMethodDecl(ident="__init__") 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_classScopeDeclarations1510)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addModifiers(md0) 

                    # JavaTreeParser.g:208:11: ( genericTypeParameterList )?
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == GENERIC_TYPE_PARAM_LIST) :
                        alt30 = 1
                    if alt30 == 1:
                        # JavaTreeParser.g:0:0: genericTypeParameterList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeParameterList_in_classScopeDeclarations1524)
                        self.genericTypeParameterList()

                        self._state.following.pop()



                    self._state.following.append(self.FOLLOW_formalParameterList_in_classScopeDeclarations1539)
                    fp0 = self.formalParameterList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addParameters(fp0) 

                    # JavaTreeParser.g:210:11: ( throwsClause )?
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == THROWS_CLAUSE) :
                        alt31 = 1
                    if alt31 == 1:
                        # JavaTreeParser.g:0:0: throwsClause
                        pass 
                        self._state.following.append(self.FOLLOW_throwsClause_in_classScopeDeclarations1553)
                        self.throwsClause()

                        self._state.following.pop()



                    self._state.following.append(self.FOLLOW_block_in_classScopeDeclarations1566)
                    self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.endMethodDecl() 


                    self.match(self.input, UP, None)


                elif alt32 == 7:
                    # JavaTreeParser.g:214:9: typeDeclaration
                    pass 
                    self._state.following.append(self.FOLLOW_typeDeclaration_in_classScopeDeclarations1598)
                    self.typeDeclaration()

                    self._state.following.pop()


                if self._state.backtracking == 0:
                                
                    self.endClassScopeDecls()
                    self.commentHandler(retval.start)
                        


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
    # JavaTreeParser.g:218:1: interfaceTopLevelScope : ^( INTERFACE_TOP_LEVEL_SCOPE ( interfaceScopeDeclarations )* ) ;
    def interfaceTopLevelScope(self, ):

        interfaceTopLevelScope_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 14):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:219:5: ( ^( INTERFACE_TOP_LEVEL_SCOPE ( interfaceScopeDeclarations )* ) )
                # JavaTreeParser.g:219:9: ^( INTERFACE_TOP_LEVEL_SCOPE ( interfaceScopeDeclarations )* )
                pass 
                self.match(self.input, INTERFACE_TOP_LEVEL_SCOPE, self.FOLLOW_INTERFACE_TOP_LEVEL_SCOPE_in_interfaceTopLevelScope1619)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:219:37: ( interfaceScopeDeclarations )*
                    while True: #loop33
                        alt33 = 2
                        LA33_0 = self.input.LA(1)

                        if (LA33_0 == AT or LA33_0 == CLASS or LA33_0 == ENUM or LA33_0 == INTERFACE or LA33_0 == FUNCTION_METHOD_DECL or LA33_0 == VAR_DECLARATION or LA33_0 == VOID_METHOD_DECL) :
                            alt33 = 1


                        if alt33 == 1:
                            # JavaTreeParser.g:0:0: interfaceScopeDeclarations
                            pass 
                            self._state.following.append(self.FOLLOW_interfaceScopeDeclarations_in_interfaceTopLevelScope1621)
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
    # JavaTreeParser.g:223:1: interfaceScopeDeclarations : ( ^( FUNCTION_METHOD_DECL md0= modifierList ( genericTypeParameterList )? tp0= type id0= IDENT fp0= formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ) | ^( VOID_METHOD_DECL md0= modifierList ( genericTypeParameterList )? id0= IDENT fp0= formalParameterList ( throwsClause )? ) | ^( VAR_DECLARATION md1= modifierList tp1= type vd1= variableDeclaratorList ) | typeDeclaration );
    def interfaceScopeDeclarations(self, ):

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
                    return 

                # JavaTreeParser.g:224:5: ( ^( FUNCTION_METHOD_DECL md0= modifierList ( genericTypeParameterList )? tp0= type id0= IDENT fp0= formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ) | ^( VOID_METHOD_DECL md0= modifierList ( genericTypeParameterList )? id0= IDENT fp0= formalParameterList ( throwsClause )? ) | ^( VAR_DECLARATION md1= modifierList tp1= type vd1= variableDeclaratorList ) | typeDeclaration )
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
                    # JavaTreeParser.g:224:9: ^( FUNCTION_METHOD_DECL md0= modifierList ( genericTypeParameterList )? tp0= type id0= IDENT fp0= formalParameterList ( arrayDeclaratorList )? ( throwsClause )? )
                    pass 
                    self.match(self.input, FUNCTION_METHOD_DECL, self.FOLLOW_FUNCTION_METHOD_DECL_in_interfaceScopeDeclarations1644)

                    if self._state.backtracking == 0:
                        self.beginMethodDecl() 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_interfaceScopeDeclarations1670)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addModifiers(md0) 

                    # JavaTreeParser.g:227:11: ( genericTypeParameterList )?
                    alt34 = 2
                    LA34_0 = self.input.LA(1)

                    if (LA34_0 == GENERIC_TYPE_PARAM_LIST) :
                        alt34 = 1
                    if alt34 == 1:
                        # JavaTreeParser.g:0:0: genericTypeParameterList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeParameterList_in_interfaceScopeDeclarations1684)
                        self.genericTypeParameterList()

                        self._state.following.pop()



                    self._state.following.append(self.FOLLOW_type_in_interfaceScopeDeclarations1699)
                    tp0 = self.type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.setType(((tp0 is not None) and [tp0.value] or [None])[0]) 

                    id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_interfaceScopeDeclarations1715)
                    if self._state.backtracking == 0:
                        self.setIdent(ident=id0.text) 

                    self._state.following.append(self.FOLLOW_formalParameterList_in_interfaceScopeDeclarations1731)
                    fp0 = self.formalParameterList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addParameters(fp0) 

                    # JavaTreeParser.g:231:11: ( arrayDeclaratorList )?
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if (LA35_0 == ARRAY_DECLARATOR_LIST) :
                        alt35 = 1
                    if alt35 == 1:
                        # JavaTreeParser.g:0:0: arrayDeclaratorList
                        pass 
                        self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_interfaceScopeDeclarations1745)
                        self.arrayDeclaratorList()

                        self._state.following.pop()



                    # JavaTreeParser.g:232:11: ( throwsClause )?
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if (LA36_0 == THROWS_CLAUSE) :
                        alt36 = 1
                    if alt36 == 1:
                        # JavaTreeParser.g:0:0: throwsClause
                        pass 
                        self._state.following.append(self.FOLLOW_throwsClause_in_interfaceScopeDeclarations1758)
                        self.throwsClause()

                        self._state.following.pop()



                    if self._state.backtracking == 0:
                        self.endMethodDecl() 


                    self.match(self.input, UP, None)


                elif alt39 == 2:
                    # JavaTreeParser.g:235:9: ^( VOID_METHOD_DECL md0= modifierList ( genericTypeParameterList )? id0= IDENT fp0= formalParameterList ( throwsClause )? )
                    pass 
                    self.match(self.input, VOID_METHOD_DECL, self.FOLLOW_VOID_METHOD_DECL_in_interfaceScopeDeclarations1792)

                    if self._state.backtracking == 0:
                        self.beginMethodDecl(type="void") 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_interfaceScopeDeclarations1818)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addModifiers(md0) 

                    # JavaTreeParser.g:238:11: ( genericTypeParameterList )?
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == GENERIC_TYPE_PARAM_LIST) :
                        alt37 = 1
                    if alt37 == 1:
                        # JavaTreeParser.g:0:0: genericTypeParameterList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeParameterList_in_interfaceScopeDeclarations1832)
                        self.genericTypeParameterList()

                        self._state.following.pop()



                    id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_interfaceScopeDeclarations1847)
                    if self._state.backtracking == 0:
                        self.setIdent(ident=id0.text) 

                    self._state.following.append(self.FOLLOW_formalParameterList_in_interfaceScopeDeclarations1863)
                    fp0 = self.formalParameterList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addParameters(fp0) 

                    # JavaTreeParser.g:241:11: ( throwsClause )?
                    alt38 = 2
                    LA38_0 = self.input.LA(1)

                    if (LA38_0 == THROWS_CLAUSE) :
                        alt38 = 1
                    if alt38 == 1:
                        # JavaTreeParser.g:0:0: throwsClause
                        pass 
                        self._state.following.append(self.FOLLOW_throwsClause_in_interfaceScopeDeclarations1877)
                        self.throwsClause()

                        self._state.following.pop()



                    if self._state.backtracking == 0:
                        self.endMethodDecl() 


                    self.match(self.input, UP, None)


                elif alt39 == 3:
                    # JavaTreeParser.g:244:9: ^( VAR_DECLARATION md1= modifierList tp1= type vd1= variableDeclaratorList )
                    pass 
                    self.match(self.input, VAR_DECLARATION, self.FOLLOW_VAR_DECLARATION_in_interfaceScopeDeclarations1911)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_interfaceScopeDeclarations1925)
                    md1 = self.modifierList()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_type_in_interfaceScopeDeclarations1939)
                    tp1 = self.type()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_variableDeclaratorList_in_interfaceScopeDeclarations1953)
                    vd1 = self.variableDeclaratorList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addClassVariables(vd1, ((tp1 is not None) and [tp1.value] or [None])[0], md1) 


                    self.match(self.input, UP, None)


                elif alt39 == 4:
                    # JavaTreeParser.g:250:9: typeDeclaration
                    pass 
                    self._state.following.append(self.FOLLOW_typeDeclaration_in_interfaceScopeDeclarations1985)
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
    # JavaTreeParser.g:253:1: variableDeclaratorList returns [values] : ^( VAR_DECLARATOR_LIST (vd0= variableDeclarator )+ ) ;
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

                # JavaTreeParser.g:255:5: ( ^( VAR_DECLARATOR_LIST (vd0= variableDeclarator )+ ) )
                # JavaTreeParser.g:255:9: ^( VAR_DECLARATOR_LIST (vd0= variableDeclarator )+ )
                pass 
                self.match(self.input, VAR_DECLARATOR_LIST, self.FOLLOW_VAR_DECLARATOR_LIST_in_variableDeclaratorList2018)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:255:31: (vd0= variableDeclarator )+
                cnt40 = 0
                while True: #loop40
                    alt40 = 2
                    LA40_0 = self.input.LA(1)

                    if (LA40_0 == VAR_DECLARATOR) :
                        alt40 = 1


                    if alt40 == 1:
                        # JavaTreeParser.g:255:32: vd0= variableDeclarator
                        pass 
                        self._state.following.append(self.FOLLOW_variableDeclarator_in_variableDeclaratorList2023)
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
    # JavaTreeParser.g:259:1: variableDeclarator returns [value] : ^( VAR_DECLARATOR (vd0= variableDeclaratorId ) (vi0= variableInitializer )? ) ;
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

                # JavaTreeParser.g:260:5: ( ^( VAR_DECLARATOR (vd0= variableDeclaratorId ) (vi0= variableInitializer )? ) )
                # JavaTreeParser.g:260:9: ^( VAR_DECLARATOR (vd0= variableDeclaratorId ) (vi0= variableInitializer )? )
                pass 
                self.match(self.input, VAR_DECLARATOR, self.FOLLOW_VAR_DECLARATOR_in_variableDeclarator2054)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:261:11: (vd0= variableDeclaratorId )
                # JavaTreeParser.g:261:12: vd0= variableDeclaratorId
                pass 
                self._state.following.append(self.FOLLOW_variableDeclaratorId_in_variableDeclarator2069)
                vd0 = self.variableDeclaratorId()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    value = ex(left=vd0, format="${left}") 




                # JavaTreeParser.g:263:11: (vi0= variableInitializer )?
                alt41 = 2
                LA41_0 = self.input.LA(1)

                if (LA41_0 == ARRAY_INITIALIZER or LA41_0 == EXPR) :
                    alt41 = 1
                if alt41 == 1:
                    # JavaTreeParser.g:263:12: vi0= variableInitializer
                    pass 
                    self._state.following.append(self.FOLLOW_variableInitializer_in_variableDeclarator2098)
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
    # JavaTreeParser.g:269:1: variableDeclaratorId returns [value] : ^( IDENT ( arrayDeclaratorList )? ) ;
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

                # JavaTreeParser.g:271:5: ( ^( IDENT ( arrayDeclaratorList )? ) )
                # JavaTreeParser.g:271:9: ^( IDENT ( arrayDeclaratorList )? )
                pass 
                IDENT1=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_variableDeclaratorId2157)

                if self._state.backtracking == 0:
                    expr = ex(self.altIdent(IDENT1.text), format="${left}", rename=True, ident=IDENT1.text)
                    value.update(expr)
                               


                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:275:11: ( arrayDeclaratorList )?
                    alt42 = 2
                    LA42_0 = self.input.LA(1)

                    if (LA42_0 == ARRAY_DECLARATOR_LIST) :
                        alt42 = 1
                    if alt42 == 1:
                        # JavaTreeParser.g:275:12: arrayDeclaratorList
                        pass 
                        self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_variableDeclaratorId2183)
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
    # JavaTreeParser.g:280:1: variableInitializer returns [value] : (ai0= arrayInitializer | ex0= expression );
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

                # JavaTreeParser.g:281:5: (ai0= arrayInitializer | ex0= expression )
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
                    # JavaTreeParser.g:281:9: ai0= arrayInitializer
                    pass 
                    self._state.following.append(self.FOLLOW_arrayInitializer_in_variableInitializer2223)
                    ai0 = self.arrayInitializer()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex(ai0, format="[${left}]") 



                elif alt43 == 2:
                    # JavaTreeParser.g:282:9: ex0= expression
                    pass 
                    self._state.following.append(self.FOLLOW_expression_in_variableInitializer2237)
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
    # JavaTreeParser.g:286:1: arrayDeclarator : LBRACK RBRACK ;
    def arrayDeclarator(self, ):

        arrayDeclarator_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 20):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:287:5: ( LBRACK RBRACK )
                # JavaTreeParser.g:287:9: LBRACK RBRACK
                pass 
                self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_arrayDeclarator2265)
                self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_arrayDeclarator2267)




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
    # JavaTreeParser.g:291:1: arrayDeclaratorList returns [values] : ^( ARRAY_DECLARATOR_LIST ( ARRAY_DECLARATOR )* ) ;
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

                # JavaTreeParser.g:293:5: ( ^( ARRAY_DECLARATOR_LIST ( ARRAY_DECLARATOR )* ) )
                # JavaTreeParser.g:293:9: ^( ARRAY_DECLARATOR_LIST ( ARRAY_DECLARATOR )* )
                pass 
                self.match(self.input, ARRAY_DECLARATOR_LIST, self.FOLLOW_ARRAY_DECLARATOR_LIST_in_arrayDeclaratorList2301)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:293:33: ( ARRAY_DECLARATOR )*
                    while True: #loop44
                        alt44 = 2
                        LA44_0 = self.input.LA(1)

                        if (LA44_0 == ARRAY_DECLARATOR) :
                            alt44 = 1


                        if alt44 == 1:
                            # JavaTreeParser.g:293:34: ARRAY_DECLARATOR
                            pass 
                            self.match(self.input, ARRAY_DECLARATOR, self.FOLLOW_ARRAY_DECLARATOR_in_arrayDeclaratorList2304)
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
    # JavaTreeParser.g:297:1: arrayInitializer returns [value] : ^( ARRAY_INITIALIZER (v0= variableInitializer )* ) ;
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

                # JavaTreeParser.g:299:5: ( ^( ARRAY_INITIALIZER (v0= variableInitializer )* ) )
                # JavaTreeParser.g:299:9: ^( ARRAY_INITIALIZER (v0= variableInitializer )* )
                pass 
                self.match(self.input, ARRAY_INITIALIZER, self.FOLLOW_ARRAY_INITIALIZER_in_arrayInitializer2343)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:300:13: (v0= variableInitializer )*
                    while True: #loop45
                        alt45 = 2
                        LA45_0 = self.input.LA(1)

                        if (LA45_0 == ARRAY_INITIALIZER or LA45_0 == EXPR) :
                            alt45 = 1


                        if alt45 == 1:
                            # JavaTreeParser.g:300:14: v0= variableInitializer
                            pass 
                            self._state.following.append(self.FOLLOW_variableInitializer_in_arrayInitializer2360)
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
    # JavaTreeParser.g:307:1: throwsClause : ^( THROWS_CLAUSE ( qualifiedIdentifier )+ ) ;
    def throwsClause(self, ):

        throwsClause_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 23):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:308:5: ( ^( THROWS_CLAUSE ( qualifiedIdentifier )+ ) )
                # JavaTreeParser.g:308:9: ^( THROWS_CLAUSE ( qualifiedIdentifier )+ )
                pass 
                self.match(self.input, THROWS_CLAUSE, self.FOLLOW_THROWS_CLAUSE_in_throwsClause2420)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:308:25: ( qualifiedIdentifier )+
                cnt46 = 0
                while True: #loop46
                    alt46 = 2
                    LA46_0 = self.input.LA(1)

                    if (LA46_0 == DOT or LA46_0 == IDENT) :
                        alt46 = 1


                    if alt46 == 1:
                        # JavaTreeParser.g:0:0: qualifiedIdentifier
                        pass 
                        self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_throwsClause2422)
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
    # JavaTreeParser.g:312:1: modifierList returns [values] : ^( MODIFIER_LIST (md0= modifier )* ) ;
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

                # JavaTreeParser.g:314:5: ( ^( MODIFIER_LIST (md0= modifier )* ) )
                # JavaTreeParser.g:314:9: ^( MODIFIER_LIST (md0= modifier )* )
                pass 
                self.match(self.input, MODIFIER_LIST, self.FOLLOW_MODIFIER_LIST_in_modifierList2458)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:314:25: (md0= modifier )*
                    while True: #loop47
                        alt47 = 2
                        LA47_0 = self.input.LA(1)

                        if (LA47_0 == AT or LA47_0 == ABSTRACT or LA47_0 == FINAL or LA47_0 == NATIVE or (PRIVATE <= LA47_0 <= PUBLIC) or (STATIC <= LA47_0 <= STRICTFP) or LA47_0 == SYNCHRONIZED or LA47_0 == TRANSIENT or LA47_0 == VOLATILE) :
                            alt47 = 1


                        if alt47 == 1:
                            # JavaTreeParser.g:314:26: md0= modifier
                            pass 
                            self._state.following.append(self.FOLLOW_modifier_in_modifierList2463)
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
    # JavaTreeParser.g:318:1: modifier returns [value] : ( PUBLIC | PROTECTED | PRIVATE | STATIC | ABSTRACT | NATIVE | SYNCHRONIZED | TRANSIENT | VOLATILE | STRICTFP | lm0= localModifier );
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

                # JavaTreeParser.g:320:5: ( PUBLIC | PROTECTED | PRIVATE | STATIC | ABSTRACT | NATIVE | SYNCHRONIZED | TRANSIENT | VOLATILE | STRICTFP | lm0= localModifier )
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
                    # JavaTreeParser.g:320:9: PUBLIC
                    pass 
                    self.match(self.input, PUBLIC, self.FOLLOW_PUBLIC_in_modifier2501)
                    if self._state.backtracking == 0:
                        retval.value.update(left=self.input.toString(retval.start, self.input.LT(-1))) 



                elif alt48 == 2:
                    # JavaTreeParser.g:321:9: PROTECTED
                    pass 
                    self.match(self.input, PROTECTED, self.FOLLOW_PROTECTED_in_modifier2524)
                    if self._state.backtracking == 0:
                        retval.value.update(left=self.input.toString(retval.start, self.input.LT(-1))) 



                elif alt48 == 3:
                    # JavaTreeParser.g:322:9: PRIVATE
                    pass 
                    self.match(self.input, PRIVATE, self.FOLLOW_PRIVATE_in_modifier2544)
                    if self._state.backtracking == 0:
                        retval.value.update(left=self.input.toString(retval.start, self.input.LT(-1))) 



                elif alt48 == 4:
                    # JavaTreeParser.g:323:9: STATIC
                    pass 
                    self.match(self.input, STATIC, self.FOLLOW_STATIC_in_modifier2566)
                    if self._state.backtracking == 0:
                        retval.value.update(left=self.input.toString(retval.start, self.input.LT(-1))) 



                elif alt48 == 5:
                    # JavaTreeParser.g:324:9: ABSTRACT
                    pass 
                    self.match(self.input, ABSTRACT, self.FOLLOW_ABSTRACT_in_modifier2589)
                    if self._state.backtracking == 0:
                        retval.value.update(left=self.input.toString(retval.start, self.input.LT(-1))) 



                elif alt48 == 6:
                    # JavaTreeParser.g:325:9: NATIVE
                    pass 
                    self.match(self.input, NATIVE, self.FOLLOW_NATIVE_in_modifier2610)
                    if self._state.backtracking == 0:
                        retval.value.update(left=self.input.toString(retval.start, self.input.LT(-1))) 



                elif alt48 == 7:
                    # JavaTreeParser.g:326:9: SYNCHRONIZED
                    pass 
                    self.match(self.input, SYNCHRONIZED, self.FOLLOW_SYNCHRONIZED_in_modifier2633)
                    if self._state.backtracking == 0:
                        retval.value.update(left=self.input.toString(retval.start, self.input.LT(-1))) 



                elif alt48 == 8:
                    # JavaTreeParser.g:327:9: TRANSIENT
                    pass 
                    self.match(self.input, TRANSIENT, self.FOLLOW_TRANSIENT_in_modifier2650)
                    if self._state.backtracking == 0:
                        retval.value.update(left=self.input.toString(retval.start, self.input.LT(-1))) 



                elif alt48 == 9:
                    # JavaTreeParser.g:328:9: VOLATILE
                    pass 
                    self.match(self.input, VOLATILE, self.FOLLOW_VOLATILE_in_modifier2670)
                    if self._state.backtracking == 0:
                        retval.value.update(left=self.input.toString(retval.start, self.input.LT(-1))) 



                elif alt48 == 10:
                    # JavaTreeParser.g:329:9: STRICTFP
                    pass 
                    self.match(self.input, STRICTFP, self.FOLLOW_STRICTFP_in_modifier2691)
                    if self._state.backtracking == 0:
                        retval.value.update(left=self.input.toString(retval.start, self.input.LT(-1))) 



                elif alt48 == 11:
                    # JavaTreeParser.g:330:9: lm0= localModifier
                    pass 
                    self._state.following.append(self.FOLLOW_localModifier_in_modifier2714)
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
    # JavaTreeParser.g:334:1: localModifierList returns [values] : ^( LOCAL_MODIFIER_LIST (md0= localModifier )* ) ;
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

                # JavaTreeParser.g:336:5: ( ^( LOCAL_MODIFIER_LIST (md0= localModifier )* ) )
                # JavaTreeParser.g:336:9: ^( LOCAL_MODIFIER_LIST (md0= localModifier )* )
                pass 
                self.match(self.input, LOCAL_MODIFIER_LIST, self.FOLLOW_LOCAL_MODIFIER_LIST_in_localModifierList2750)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:336:31: (md0= localModifier )*
                    while True: #loop49
                        alt49 = 2
                        LA49_0 = self.input.LA(1)

                        if (LA49_0 == AT or LA49_0 == FINAL) :
                            alt49 = 1


                        if alt49 == 1:
                            # JavaTreeParser.g:336:32: md0= localModifier
                            pass 
                            self._state.following.append(self.FOLLOW_localModifier_in_localModifierList2755)
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
    # JavaTreeParser.g:340:1: localModifier returns [value] : ( FINAL | an0= annotation );
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

                # JavaTreeParser.g:341:5: ( FINAL | an0= annotation )
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
                    # JavaTreeParser.g:341:9: FINAL
                    pass 
                    self.match(self.input, FINAL, self.FOLLOW_FINAL_in_localModifier2784)
                    if self._state.backtracking == 0:
                        value = "final" 



                elif alt50 == 2:
                    # JavaTreeParser.g:342:9: an0= annotation
                    pass 
                    self._state.following.append(self.FOLLOW_annotation_in_localModifier2798)
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
    # JavaTreeParser.g:346:1: type returns [value] : ^( TYPE (pt0= primitiveType | qt0= qualifiedTypeIdent ) ( arrayDeclaratorList )? ) ;
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

                # JavaTreeParser.g:348:5: ( ^( TYPE (pt0= primitiveType | qt0= qualifiedTypeIdent ) ( arrayDeclaratorList )? ) )
                # JavaTreeParser.g:348:9: ^( TYPE (pt0= primitiveType | qt0= qualifiedTypeIdent ) ( arrayDeclaratorList )? )
                pass 
                self.match(self.input, TYPE, self.FOLLOW_TYPE_in_type2834)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:349:11: (pt0= primitiveType | qt0= qualifiedTypeIdent )
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
                    # JavaTreeParser.g:349:12: pt0= primitiveType
                    pass 
                    self._state.following.append(self.FOLLOW_primitiveType_in_type2849)
                    pt0 = self.primitiveType()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        retval.value.update(left=self.renameType(((pt0 is not None) and [self.input.getTokenStream().toString(
                            self.input.getTreeAdaptor().getTokenStartIndex(pt0.start),
                            self.input.getTreeAdaptor().getTokenStopIndex(pt0.start)
                            )] or [None])[0])) 



                elif alt51 == 2:
                    # JavaTreeParser.g:350:12: qt0= qualifiedTypeIdent
                    pass 
                    self._state.following.append(self.FOLLOW_qualifiedTypeIdent_in_type2873)
                    qt0 = self.qualifiedTypeIdent()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        retval.value.update(left=self.renameType(qt0))




                # JavaTreeParser.g:351:11: ( arrayDeclaratorList )?
                alt52 = 2
                LA52_0 = self.input.LA(1)

                if (LA52_0 == ARRAY_DECLARATOR_LIST) :
                    alt52 = 1
                if alt52 == 1:
                    # JavaTreeParser.g:351:12: arrayDeclaratorList
                    pass 
                    self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_type2890)
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
    # JavaTreeParser.g:356:1: qualifiedTypeIdent returns [value] : ^( QUALIFIED_TYPE_IDENT (ti0= typeIdent )+ ) ;
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

                # JavaTreeParser.g:357:5: ( ^( QUALIFIED_TYPE_IDENT (ti0= typeIdent )+ ) )
                # JavaTreeParser.g:357:9: ^( QUALIFIED_TYPE_IDENT (ti0= typeIdent )+ )
                pass 
                self.match(self.input, QUALIFIED_TYPE_IDENT, self.FOLLOW_QUALIFIED_TYPE_IDENT_in_qualifiedTypeIdent2933)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:357:32: (ti0= typeIdent )+
                cnt53 = 0
                while True: #loop53
                    alt53 = 2
                    LA53_0 = self.input.LA(1)

                    if (LA53_0 == IDENT) :
                        alt53 = 1


                    if alt53 == 1:
                        # JavaTreeParser.g:357:33: ti0= typeIdent
                        pass 
                        self._state.following.append(self.FOLLOW_typeIdent_in_qualifiedTypeIdent2938)
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
    # JavaTreeParser.g:361:1: typeIdent returns [value] : ^(id0= IDENT ( genericTypeArgumentList )? ) ;
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

                # JavaTreeParser.g:362:5: ( ^(id0= IDENT ( genericTypeArgumentList )? ) )
                # JavaTreeParser.g:362:9: ^(id0= IDENT ( genericTypeArgumentList )? )
                pass 
                id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_typeIdent2970)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:362:21: ( genericTypeArgumentList )?
                    alt54 = 2
                    LA54_0 = self.input.LA(1)

                    if (LA54_0 == GENERIC_TYPE_ARG_LIST) :
                        alt54 = 1
                    if alt54 == 1:
                        # JavaTreeParser.g:0:0: genericTypeArgumentList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeArgumentList_in_typeIdent2972)
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
    # JavaTreeParser.g:366:1: primitiveType : ( BOOLEAN | CHAR | BYTE | SHORT | INT | LONG | FLOAT | DOUBLE );
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

                # JavaTreeParser.g:367:5: ( BOOLEAN | CHAR | BYTE | SHORT | INT | LONG | FLOAT | DOUBLE )
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
    # JavaTreeParser.g:378:1: genericTypeArgumentList returns [values] : ^( GENERIC_TYPE_ARG_LIST ( genericTypeArgument )+ ) ;
    def genericTypeArgumentList(self, ):

        values = None
        genericTypeArgumentList_StartIndex = self.input.index()
        values = [] 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 32):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return values

                # JavaTreeParser.g:380:5: ( ^( GENERIC_TYPE_ARG_LIST ( genericTypeArgument )+ ) )
                # JavaTreeParser.g:380:9: ^( GENERIC_TYPE_ARG_LIST ( genericTypeArgument )+ )
                pass 
                self.match(self.input, GENERIC_TYPE_ARG_LIST, self.FOLLOW_GENERIC_TYPE_ARG_LIST_in_genericTypeArgumentList3100)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:380:33: ( genericTypeArgument )+
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
    # JavaTreeParser.g:383:1: genericTypeArgument : ( type | ^( QUESTION ( genericWildcardBoundType )? ) );
    def genericTypeArgument(self, ):

        genericTypeArgument_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 33):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:384:5: ( type | ^( QUESTION ( genericWildcardBoundType )? ) )
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
                    # JavaTreeParser.g:384:9: type
                    pass 
                    self._state.following.append(self.FOLLOW_type_in_genericTypeArgument3123)
                    self.type()

                    self._state.following.pop()


                elif alt57 == 2:
                    # JavaTreeParser.g:385:9: ^( QUESTION ( genericWildcardBoundType )? )
                    pass 
                    self.match(self.input, QUESTION, self.FOLLOW_QUESTION_in_genericTypeArgument3134)

                    if self.input.LA(1) == DOWN:
                        self.match(self.input, DOWN, None)
                        # JavaTreeParser.g:385:20: ( genericWildcardBoundType )?
                        alt56 = 2
                        LA56_0 = self.input.LA(1)

                        if (LA56_0 == EXTENDS or LA56_0 == SUPER) :
                            alt56 = 1
                        if alt56 == 1:
                            # JavaTreeParser.g:0:0: genericWildcardBoundType
                            pass 
                            self._state.following.append(self.FOLLOW_genericWildcardBoundType_in_genericTypeArgument3136)
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
    # JavaTreeParser.g:388:1: genericWildcardBoundType : ( ^( EXTENDS type ) | ^( SUPER type ) );
    def genericWildcardBoundType(self, ):

        genericWildcardBoundType_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 34):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:389:5: ( ^( EXTENDS type ) | ^( SUPER type ) )
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
                    # JavaTreeParser.g:389:9: ^( EXTENDS type )
                    pass 
                    self.match(self.input, EXTENDS, self.FOLLOW_EXTENDS_in_genericWildcardBoundType3158)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_type_in_genericWildcardBoundType3160)
                    self.type()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt58 == 2:
                    # JavaTreeParser.g:390:9: ^( SUPER type )
                    pass 
                    self.match(self.input, SUPER, self.FOLLOW_SUPER_in_genericWildcardBoundType3172)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_type_in_genericWildcardBoundType3174)
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
    # JavaTreeParser.g:393:1: formalParameterList returns [values] : ^( FORMAL_PARAM_LIST (fp0= formalParameterStandardDecl )* (vd0= formalParameterVarargDecl )? ) ;
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

                # JavaTreeParser.g:395:5: ( ^( FORMAL_PARAM_LIST (fp0= formalParameterStandardDecl )* (vd0= formalParameterVarargDecl )? ) )
                # JavaTreeParser.g:395:9: ^( FORMAL_PARAM_LIST (fp0= formalParameterStandardDecl )* (vd0= formalParameterVarargDecl )? )
                pass 
                self.match(self.input, FORMAL_PARAM_LIST, self.FOLLOW_FORMAL_PARAM_LIST_in_formalParameterList3208)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:396:11: (fp0= formalParameterStandardDecl )*
                    while True: #loop59
                        alt59 = 2
                        LA59_0 = self.input.LA(1)

                        if (LA59_0 == FORMAL_PARAM_STD_DECL) :
                            alt59 = 1


                        if alt59 == 1:
                            # JavaTreeParser.g:396:12: fp0= formalParameterStandardDecl
                            pass 
                            self._state.following.append(self.FOLLOW_formalParameterStandardDecl_in_formalParameterList3223)
                            fp0 = self.formalParameterStandardDecl()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                values.append(fp0) 



                        else:
                            break #loop59


                    # JavaTreeParser.g:397:11: (vd0= formalParameterVarargDecl )?
                    alt60 = 2
                    LA60_0 = self.input.LA(1)

                    if (LA60_0 == FORMAL_PARAM_VARARG_DECL) :
                        alt60 = 1
                    if alt60 == 1:
                        # JavaTreeParser.g:397:12: vd0= formalParameterVarargDecl
                        pass 
                        self._state.following.append(self.FOLLOW_formalParameterVarargDecl_in_formalParameterList3242)
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
    # JavaTreeParser.g:401:1: formalParameterStandardDecl returns [value] : ^( FORMAL_PARAM_STD_DECL lm0= localModifierList tp0= type vd0= variableDeclaratorId ) ;
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

                # JavaTreeParser.g:402:5: ( ^( FORMAL_PARAM_STD_DECL lm0= localModifierList tp0= type vd0= variableDeclaratorId ) )
                # JavaTreeParser.g:402:9: ^( FORMAL_PARAM_STD_DECL lm0= localModifierList tp0= type vd0= variableDeclaratorId )
                pass 
                self.match(self.input, FORMAL_PARAM_STD_DECL, self.FOLLOW_FORMAL_PARAM_STD_DECL_in_formalParameterStandardDecl3282)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_localModifierList_in_formalParameterStandardDecl3296)
                lm0 = self.localModifierList()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_type_in_formalParameterStandardDecl3310)
                tp0 = self.type()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_variableDeclaratorId_in_formalParameterStandardDecl3324)
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
    # JavaTreeParser.g:409:1: formalParameterVarargDecl returns [value] : ^( FORMAL_PARAM_VARARG_DECL lm0= localModifierList tp0= type vd0= variableDeclaratorId ) ;
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

                # JavaTreeParser.g:410:5: ( ^( FORMAL_PARAM_VARARG_DECL lm0= localModifierList tp0= type vd0= variableDeclaratorId ) )
                # JavaTreeParser.g:410:9: ^( FORMAL_PARAM_VARARG_DECL lm0= localModifierList tp0= type vd0= variableDeclaratorId )
                pass 
                self.match(self.input, FORMAL_PARAM_VARARG_DECL, self.FOLLOW_FORMAL_PARAM_VARARG_DECL_in_formalParameterVarargDecl3360)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_localModifierList_in_formalParameterVarargDecl3374)
                lm0 = self.localModifierList()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_type_in_formalParameterVarargDecl3388)
                tp0 = self.type()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_variableDeclaratorId_in_formalParameterVarargDecl3402)
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
    # JavaTreeParser.g:417:1: qualifiedIdentifier returns [value] : ( IDENT | ^( DOT qi0= qualifiedIdentifier IDENT ) );
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

                # JavaTreeParser.g:418:5: ( IDENT | ^( DOT qi0= qualifiedIdentifier IDENT ) )
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
                    # JavaTreeParser.g:418:9: IDENT
                    pass 
                    IDENT2=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_qualifiedIdentifier3437)
                    if self._state.backtracking == 0:
                        value = ex(IDENT2.text, format="${left}", rename=True) 



                elif alt61 == 2:
                    # JavaTreeParser.g:420:9: ^( DOT qi0= qualifiedIdentifier IDENT )
                    pass 
                    self.match(self.input, DOT, self.FOLLOW_DOT_in_qualifiedIdentifier3458)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_qualifiedIdentifier3472)
                    qi0 = self.qualifiedIdentifier()

                    self._state.following.pop()
                    IDENT3=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_qualifiedIdentifier3484)
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
    # JavaTreeParser.g:431:1: annotationList returns [values] : ^( ANNOTATION_LIST (an0= annotation )* ) ;
    def annotationList(self, ):

        values = None
        annotationList_StartIndex = self.input.index()
        an0 = None


        values = [] 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 39):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return values

                # JavaTreeParser.g:433:5: ( ^( ANNOTATION_LIST (an0= annotation )* ) )
                # JavaTreeParser.g:433:9: ^( ANNOTATION_LIST (an0= annotation )* )
                pass 
                self.match(self.input, ANNOTATION_LIST, self.FOLLOW_ANNOTATION_LIST_in_annotationList3539)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:433:27: (an0= annotation )*
                    while True: #loop62
                        alt62 = 2
                        LA62_0 = self.input.LA(1)

                        if (LA62_0 == AT) :
                            alt62 = 1


                        if alt62 == 1:
                            # JavaTreeParser.g:433:28: an0= annotation
                            pass 
                            self._state.following.append(self.FOLLOW_annotation_in_annotationList3544)
                            an0 = self.annotation()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                values.append(an0) 



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

        return values

    # $ANTLR end "annotationList"


    # $ANTLR start "annotation"
    # JavaTreeParser.g:436:1: annotation returns [value] : ^( AT qi0= qualifiedIdentifier (ai0= annotationInit )? ) ;
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

                # JavaTreeParser.g:438:5: ( ^( AT qi0= qualifiedIdentifier (ai0= annotationInit )? ) )
                # JavaTreeParser.g:438:9: ^( AT qi0= qualifiedIdentifier (ai0= annotationInit )? )
                pass 
                self.match(self.input, AT, self.FOLLOW_AT_in_annotation3582)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_annotation3596)
                qi0 = self.qualifiedIdentifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    value.update(left=qi0, annotation=True) 

                # JavaTreeParser.g:440:11: (ai0= annotationInit )?
                alt63 = 2
                LA63_0 = self.input.LA(1)

                if (LA63_0 == ANNOTATION_INIT_BLOCK) :
                    alt63 = 1
                if alt63 == 1:
                    # JavaTreeParser.g:440:12: ai0= annotationInit
                    pass 
                    self._state.following.append(self.FOLLOW_annotationInit_in_annotation3613)
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
    # JavaTreeParser.g:448:1: annotationInit returns [values] : ^( ANNOTATION_INIT_BLOCK ai0= annotationInitializers ) ;
    def annotationInit(self, ):

        values = None
        annotationInit_StartIndex = self.input.index()
        ai0 = None


        values = [] 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 41):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return values

                # JavaTreeParser.g:450:5: ( ^( ANNOTATION_INIT_BLOCK ai0= annotationInitializers ) )
                # JavaTreeParser.g:450:9: ^( ANNOTATION_INIT_BLOCK ai0= annotationInitializers )
                pass 
                self.match(self.input, ANNOTATION_INIT_BLOCK, self.FOLLOW_ANNOTATION_INIT_BLOCK_in_annotationInit3682)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_annotationInitializers_in_annotationInit3686)
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
    # JavaTreeParser.g:453:1: annotationInitializers returns [values] : ( ^( ANNOTATION_INIT_KEY_LIST (ai0= annotationInitializer )+ ) | ^( ANNOTATION_INIT_DEFAULT_KEY annotationElementValue ) );
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

                # JavaTreeParser.g:455:5: ( ^( ANNOTATION_INIT_KEY_LIST (ai0= annotationInitializer )+ ) | ^( ANNOTATION_INIT_DEFAULT_KEY annotationElementValue ) )
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
                    # JavaTreeParser.g:455:9: ^( ANNOTATION_INIT_KEY_LIST (ai0= annotationInitializer )+ )
                    pass 
                    self.match(self.input, ANNOTATION_INIT_KEY_LIST, self.FOLLOW_ANNOTATION_INIT_KEY_LIST_in_annotationInitializers3722)

                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:456:11: (ai0= annotationInitializer )+
                    cnt64 = 0
                    while True: #loop64
                        alt64 = 2
                        LA64_0 = self.input.LA(1)

                        if (LA64_0 == IDENT) :
                            alt64 = 1


                        if alt64 == 1:
                            # JavaTreeParser.g:456:12: ai0= annotationInitializer
                            pass 
                            self._state.following.append(self.FOLLOW_annotationInitializer_in_annotationInitializers3737)
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
                    # JavaTreeParser.g:458:9: ^( ANNOTATION_INIT_DEFAULT_KEY annotationElementValue )
                    pass 
                    self.match(self.input, ANNOTATION_INIT_DEFAULT_KEY, self.FOLLOW_ANNOTATION_INIT_DEFAULT_KEY_in_annotationInitializers3762)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_annotationElementValue_in_annotationInitializers3764)
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
    # JavaTreeParser.g:461:1: annotationInitializer returns [value] : ^(id0= IDENT ae0= annotationElementValue ) ;
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

                # JavaTreeParser.g:462:5: ( ^(id0= IDENT ae0= annotationElementValue ) )
                # JavaTreeParser.g:462:9: ^(id0= IDENT ae0= annotationElementValue )
                pass 
                id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_annotationInitializer3791)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_annotationElementValue_in_annotationInitializer3795)
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
    # JavaTreeParser.g:468:1: annotationElementValue returns [value] : ( ^( ANNOTATION_INIT_ARRAY_ELEMENT ( annotationElementValue )* ) | (an0= annotation ) | (ex0= expression ) );
    def annotationElementValue(self, ):

        value = None
        annotationElementValue_StartIndex = self.input.index()
        an0 = None

        ex0 = None


        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 44):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:469:5: ( ^( ANNOTATION_INIT_ARRAY_ELEMENT ( annotationElementValue )* ) | (an0= annotation ) | (ex0= expression ) )
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
                    # JavaTreeParser.g:469:9: ^( ANNOTATION_INIT_ARRAY_ELEMENT ( annotationElementValue )* )
                    pass 
                    self.match(self.input, ANNOTATION_INIT_ARRAY_ELEMENT, self.FOLLOW_ANNOTATION_INIT_ARRAY_ELEMENT_in_annotationElementValue3832)

                    if self.input.LA(1) == DOWN:
                        self.match(self.input, DOWN, None)
                        # JavaTreeParser.g:469:41: ( annotationElementValue )*
                        while True: #loop66
                            alt66 = 2
                            LA66_0 = self.input.LA(1)

                            if (LA66_0 == AT or LA66_0 == ANNOTATION_INIT_ARRAY_ELEMENT or LA66_0 == EXPR) :
                                alt66 = 1


                            if alt66 == 1:
                                # JavaTreeParser.g:0:0: annotationElementValue
                                pass 
                                self._state.following.append(self.FOLLOW_annotationElementValue_in_annotationElementValue3834)
                                self.annotationElementValue()

                                self._state.following.pop()


                            else:
                                break #loop66



                        self.match(self.input, UP, None)



                elif alt67 == 2:
                    # JavaTreeParser.g:470:9: (an0= annotation )
                    pass 
                    # JavaTreeParser.g:470:9: (an0= annotation )
                    # JavaTreeParser.g:470:10: an0= annotation
                    pass 
                    self._state.following.append(self.FOLLOW_annotation_in_annotationElementValue3849)
                    an0 = self.annotation()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = an0 






                elif alt67 == 3:
                    # JavaTreeParser.g:471:9: (ex0= expression )
                    pass 
                    # JavaTreeParser.g:471:9: (ex0= expression )
                    # JavaTreeParser.g:471:10: ex0= expression
                    pass 
                    self._state.following.append(self.FOLLOW_expression_in_annotationElementValue3865)
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
    # JavaTreeParser.g:474:1: annotationTopLevelScope : ^( ANNOTATION_TOP_LEVEL_SCOPE (an0= annotationScopeDeclarations )* ) ;
    def annotationTopLevelScope(self, ):

        annotationTopLevelScope_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 45):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:475:5: ( ^( ANNOTATION_TOP_LEVEL_SCOPE (an0= annotationScopeDeclarations )* ) )
                # JavaTreeParser.g:475:9: ^( ANNOTATION_TOP_LEVEL_SCOPE (an0= annotationScopeDeclarations )* )
                pass 
                self.match(self.input, ANNOTATION_TOP_LEVEL_SCOPE, self.FOLLOW_ANNOTATION_TOP_LEVEL_SCOPE_in_annotationTopLevelScope3888)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:476:11: (an0= annotationScopeDeclarations )*
                    while True: #loop68
                        alt68 = 2
                        LA68_0 = self.input.LA(1)

                        if (LA68_0 == AT or LA68_0 == CLASS or LA68_0 == ENUM or LA68_0 == INTERFACE or LA68_0 == ANNOTATION_METHOD_DECL or LA68_0 == VAR_DECLARATION) :
                            alt68 = 1


                        if alt68 == 1:
                            # JavaTreeParser.g:476:12: an0= annotationScopeDeclarations
                            pass 
                            self._state.following.append(self.FOLLOW_annotationScopeDeclarations_in_annotationTopLevelScope3903)
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
    # JavaTreeParser.g:480:1: annotationScopeDeclarations : ( ^( ANNOTATION_METHOD_DECL md0= modifierList tp0= type id0= IDENT (ad0= annotationDefaultValue )? ) | ^( VAR_DECLARATION md1= modifierList tp1= type vd1= variableDeclaratorList ) | (tp0= typeDeclaration ) );
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

                # JavaTreeParser.g:484:5: ( ^( ANNOTATION_METHOD_DECL md0= modifierList tp0= type id0= IDENT (ad0= annotationDefaultValue )? ) | ^( VAR_DECLARATION md1= modifierList tp1= type vd1= variableDeclaratorList ) | (tp0= typeDeclaration ) )
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
                    # JavaTreeParser.g:484:9: ^( ANNOTATION_METHOD_DECL md0= modifierList tp0= type id0= IDENT (ad0= annotationDefaultValue )? )
                    pass 
                    self.match(self.input, ANNOTATION_METHOD_DECL, self.FOLLOW_ANNOTATION_METHOD_DECL_in_annotationScopeDeclarations3944)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_annotationScopeDeclarations3958)
                    md0 = self.modifierList()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_type_in_annotationScopeDeclarations3972)
                    tp0 = self.type()

                    self._state.following.pop()
                    id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_annotationScopeDeclarations3986)
                    # JavaTreeParser.g:488:11: (ad0= annotationDefaultValue )?
                    alt69 = 2
                    LA69_0 = self.input.LA(1)

                    if (LA69_0 == DEFAULT) :
                        alt69 = 1
                    if alt69 == 1:
                        # JavaTreeParser.g:488:12: ad0= annotationDefaultValue
                        pass 
                        self._state.following.append(self.FOLLOW_annotationDefaultValue_in_annotationScopeDeclarations4001)
                        ad0 = self.annotationDefaultValue()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            default = ad0 




                    if self._state.backtracking == 0:
                        self.addAnnotationMethod(md0, ((tp0 is not None) and [tp0.value] or [None])[0], id0.text, default) 


                    self.match(self.input, UP, None)


                elif alt70 == 2:
                    # JavaTreeParser.g:491:9: ^( VAR_DECLARATION md1= modifierList tp1= type vd1= variableDeclaratorList )
                    pass 
                    self.match(self.input, VAR_DECLARATION, self.FOLLOW_VAR_DECLARATION_in_annotationScopeDeclarations4038)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_modifierList_in_annotationScopeDeclarations4042)
                    md1 = self.modifierList()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_type_in_annotationScopeDeclarations4046)
                    tp1 = self.type()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_variableDeclaratorList_in_annotationScopeDeclarations4050)
                    vd1 = self.variableDeclaratorList()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        self.addVariables(vd1, ((tp1 is not None) and [tp1.value] or [None])[0], md1, local=True) 



                elif alt70 == 3:
                    # JavaTreeParser.g:493:9: (tp0= typeDeclaration )
                    pass 
                    # JavaTreeParser.g:493:9: (tp0= typeDeclaration )
                    # JavaTreeParser.g:493:10: tp0= typeDeclaration
                    pass 
                    self._state.following.append(self.FOLLOW_typeDeclaration_in_annotationScopeDeclarations4075)
                    tp0 = self.typeDeclaration()

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
    # JavaTreeParser.g:496:1: annotationDefaultValue returns [value] : ^( DEFAULT ae0= annotationElementValue ) ;
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

                # JavaTreeParser.g:497:5: ( ^( DEFAULT ae0= annotationElementValue ) )
                # JavaTreeParser.g:497:9: ^( DEFAULT ae0= annotationElementValue )
                pass 
                self.match(self.input, DEFAULT, self.FOLLOW_DEFAULT_in_annotationDefaultValue4100)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_annotationElementValue_in_annotationDefaultValue4104)
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

    class block_return(TreeRuleReturnScope):
        def __init__(self):
            TreeRuleReturnScope.__init__(self)





    # $ANTLR start "block"
    # JavaTreeParser.g:500:1: block : ^( BLOCK_SCOPE ( blockStatement )* ) ;
    def block(self, ):

        retval = self.block_return()
        retval.start = self.input.LT(1)
        block_StartIndex = self.input.index()
        self.commentHandler(retval.start) 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 48):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # JavaTreeParser.g:502:5: ( ^( BLOCK_SCOPE ( blockStatement )* ) )
                # JavaTreeParser.g:502:9: ^( BLOCK_SCOPE ( blockStatement )* )
                pass 
                self.match(self.input, BLOCK_SCOPE, self.FOLLOW_BLOCK_SCOPE_in_block4136)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:502:23: ( blockStatement )*
                    while True: #loop71
                        alt71 = 2
                        LA71_0 = self.input.LA(1)

                        if (LA71_0 == AT or LA71_0 == SEMI or LA71_0 == ASSERT or LA71_0 == BREAK or (CLASS <= LA71_0 <= CONTINUE) or LA71_0 == DO or LA71_0 == ENUM or (FOR <= LA71_0 <= IF) or LA71_0 == INTERFACE or LA71_0 == RETURN or (SWITCH <= LA71_0 <= SYNCHRONIZED) or LA71_0 == THROW or LA71_0 == TRY or LA71_0 == WHILE or LA71_0 == BLOCK_SCOPE or LA71_0 == EXPR or LA71_0 == FOR_EACH or LA71_0 == LABELED_STATEMENT or LA71_0 == VAR_DECLARATION) :
                            alt71 = 1


                        if alt71 == 1:
                            # JavaTreeParser.g:0:0: blockStatement
                            pass 
                            self._state.following.append(self.FOLLOW_blockStatement_in_block4138)
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

        return retval

    # $ANTLR end "block"


    # $ANTLR start "blockStatement"
    # JavaTreeParser.g:505:1: blockStatement : ( localVariableDeclaration | typeDeclaration | st0= statement );
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

                # JavaTreeParser.g:506:5: ( localVariableDeclaration | typeDeclaration | st0= statement )
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
                    # JavaTreeParser.g:506:9: localVariableDeclaration
                    pass 
                    self._state.following.append(self.FOLLOW_localVariableDeclaration_in_blockStatement4159)
                    self.localVariableDeclaration()

                    self._state.following.pop()


                elif alt72 == 2:
                    # JavaTreeParser.g:507:9: typeDeclaration
                    pass 
                    self._state.following.append(self.FOLLOW_typeDeclaration_in_blockStatement4169)
                    self.typeDeclaration()

                    self._state.following.pop()


                elif alt72 == 3:
                    # JavaTreeParser.g:508:9: st0= statement
                    pass 
                    self._state.following.append(self.FOLLOW_statement_in_blockStatement4181)
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
    # JavaTreeParser.g:511:1: localVariableDeclaration : ^( VAR_DECLARATION md0= localModifierList tp0= type vd0= variableDeclaratorList ) ;
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

                # JavaTreeParser.g:512:5: ( ^( VAR_DECLARATION md0= localModifierList tp0= type vd0= variableDeclaratorList ) )
                # JavaTreeParser.g:512:9: ^( VAR_DECLARATION md0= localModifierList tp0= type vd0= variableDeclaratorList )
                pass 
                self.match(self.input, VAR_DECLARATION, self.FOLLOW_VAR_DECLARATION_in_localVariableDeclaration4203)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_localModifierList_in_localVariableDeclaration4207)
                md0 = self.localModifierList()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_type_in_localVariableDeclaration4211)
                tp0 = self.type()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_variableDeclaratorList_in_localVariableDeclaration4215)
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
    # JavaTreeParser.g:517:1: statement returns [value] : ( block | ^( ASSERT (ex0= expression ) (ex1= expression )? ) | ^( IF pe0= parenthesizedExpression statement ( statement )? ) | ^( FOR finit0= forInit fcond0= forCondition fupdt0= forUpdater statement ) | ^( FOR_EACH localModifierList type id0= IDENT ex0= expression st0= statement ) | ^( WHILE pe0= parenthesizedExpression statement ) | ^( DO statement pe0= parenthesizedExpression ) | ^( TRY block ( catches )? ( block )? ) | ^( SWITCH (pe0= parenthesizedExpression ) switchBlockLabels ) | ^( SYNCHRONIZED (pe0= parenthesizedExpression ) block ) | ^( RETURN (ex0= expression )? ) | ^( THROW ex0= expression ) | ^( BREAK (id0= IDENT )? ) | ^( CONTINUE (id0= IDENT )? ) | ^( LABELED_STATEMENT id0= IDENT lb0= statement ) | ex0= expression | SEMI );
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


        label, value = None, ex() 
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 51):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return value

                # JavaTreeParser.g:519:5: ( block | ^( ASSERT (ex0= expression ) (ex1= expression )? ) | ^( IF pe0= parenthesizedExpression statement ( statement )? ) | ^( FOR finit0= forInit fcond0= forCondition fupdt0= forUpdater statement ) | ^( FOR_EACH localModifierList type id0= IDENT ex0= expression st0= statement ) | ^( WHILE pe0= parenthesizedExpression statement ) | ^( DO statement pe0= parenthesizedExpression ) | ^( TRY block ( catches )? ( block )? ) | ^( SWITCH (pe0= parenthesizedExpression ) switchBlockLabels ) | ^( SYNCHRONIZED (pe0= parenthesizedExpression ) block ) | ^( RETURN (ex0= expression )? ) | ^( THROW ex0= expression ) | ^( BREAK (id0= IDENT )? ) | ^( CONTINUE (id0= IDENT )? ) | ^( LABELED_STATEMENT id0= IDENT lb0= statement ) | ex0= expression | SEMI )
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
                    # JavaTreeParser.g:519:9: block
                    pass 
                    self._state.following.append(self.FOLLOW_block_in_statement4270)
                    self.block()

                    self._state.following.pop()


                elif alt80 == 2:
                    # JavaTreeParser.g:520:9: ^( ASSERT (ex0= expression ) (ex1= expression )? )
                    pass 
                    self.match(self.input, ASSERT, self.FOLLOW_ASSERT_in_statement4281)

                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:521:11: (ex0= expression )
                    # JavaTreeParser.g:521:12: ex0= expression
                    pass 
                    self._state.following.append(self.FOLLOW_expression_in_statement4296)
                    ex0 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        ae = self.makeAssert(ex0)  




                    # JavaTreeParser.g:522:11: (ex1= expression )?
                    alt73 = 2
                    LA73_0 = self.input.LA(1)

                    if (LA73_0 == EXPR) :
                        alt73 = 1
                    if alt73 == 1:
                        # JavaTreeParser.g:522:12: ex1= expression
                        pass 
                        self._state.following.append(self.FOLLOW_expression_in_statement4314)
                        ex1 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self.extendAssert(ae, ex1) 





                    self.match(self.input, UP, None)


                elif alt80 == 3:
                    # JavaTreeParser.g:524:9: ^( IF pe0= parenthesizedExpression statement ( statement )? )
                    pass 
                    self.match(self.input, IF, self.FOLLOW_IF_in_statement4339)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_statement4353)
                    pe0 = self.parenthesizedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        ifstat, elsestat = self.beginIf(pe0) 

                    self._state.following.append(self.FOLLOW_statement_in_statement4367)
                    self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.endIf() 

                    # JavaTreeParser.g:527:11: ( statement )?
                    alt74 = 2
                    LA74_0 = self.input.LA(1)

                    if (LA74_0 == SEMI or LA74_0 == ASSERT or LA74_0 == BREAK or LA74_0 == CONTINUE or LA74_0 == DO or (FOR <= LA74_0 <= IF) or LA74_0 == RETURN or (SWITCH <= LA74_0 <= SYNCHRONIZED) or LA74_0 == THROW or LA74_0 == TRY or LA74_0 == WHILE or LA74_0 == BLOCK_SCOPE or LA74_0 == EXPR or LA74_0 == FOR_EACH or LA74_0 == LABELED_STATEMENT) :
                        alt74 = 1
                    if alt74 == 1:
                        # JavaTreeParser.g:527:12: statement
                        pass 
                        if self._state.backtracking == 0:
                            self.beginElse(elsestat) 

                        self._state.following.append(self.FOLLOW_statement_in_statement4384)
                        self.statement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self.endElse() 





                    self.match(self.input, UP, None)


                elif alt80 == 4:
                    # JavaTreeParser.g:529:9: ^( FOR finit0= forInit fcond0= forCondition fupdt0= forUpdater statement )
                    pass 
                    self.match(self.input, FOR, self.FOLLOW_FOR_in_statement4409)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_forInit_in_statement4423)
                    finit0 = self.forInit()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_forCondition_in_statement4437)
                    fcond0 = self.forCondition()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_forUpdater_in_statement4451)
                    fupdt0 = self.forUpdater()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.beginForLoop(finit0, fcond0, fupdt0) 

                    self._state.following.append(self.FOLLOW_statement_in_statement4475)
                    self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.endForLoop() 


                    self.match(self.input, UP, None)


                elif alt80 == 5:
                    # JavaTreeParser.g:537:9: ^( FOR_EACH localModifierList type id0= IDENT ex0= expression st0= statement )
                    pass 
                    self.match(self.input, FOR_EACH, self.FOLLOW_FOR_EACH_in_statement4508)

                    if self._state.backtracking == 0:
                        self.beginForEach() 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_localModifierList_in_statement4532)
                    self.localModifierList()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_type_in_statement4544)
                    self.type()

                    self._state.following.pop()
                    id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_statement4558)
                    self._state.following.append(self.FOLLOW_expression_in_statement4572)
                    ex0 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.setExpression(ex(id0.text, ex0, format="${left} in ${right}")) 

                    self._state.following.append(self.FOLLOW_statement_in_statement4598)
                    st0 = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.append(st0) 

                    if self._state.backtracking == 0:
                        self.endForEach() 


                    self.match(self.input, UP, None)


                elif alt80 == 6:
                    # JavaTreeParser.g:547:9: ^( WHILE pe0= parenthesizedExpression statement )
                    pass 
                    self.match(self.input, WHILE, self.FOLLOW_WHILE_in_statement4633)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_statement4647)
                    pe0 = self.parenthesizedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.beginWhile(pe0) 

                    self._state.following.append(self.FOLLOW_statement_in_statement4671)
                    self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.endWhile() 


                    self.match(self.input, UP, None)


                elif alt80 == 7:
                    # JavaTreeParser.g:553:9: ^( DO statement pe0= parenthesizedExpression )
                    pass 
                    self.match(self.input, DO, self.FOLLOW_DO_in_statement4704)

                    if self._state.backtracking == 0:
                        self.beginDo() 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_statement_in_statement4728)
                    self.statement()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_statement4742)
                    pe0 = self.parenthesizedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.endDo(pe0) 


                    self.match(self.input, UP, None)


                elif alt80 == 8:
                    # JavaTreeParser.g:559:9: ^( TRY block ( catches )? ( block )? )
                    pass 
                    self.match(self.input, TRY, self.FOLLOW_TRY_in_statement4775)

                    if self._state.backtracking == 0:
                        self.beginTry() 


                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_block_in_statement4797)
                    self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.endTry() 

                    # JavaTreeParser.g:563:10: ( catches )?
                    alt75 = 2
                    LA75_0 = self.input.LA(1)

                    if (LA75_0 == CATCH_CLAUSE_LIST) :
                        alt75 = 1
                    if alt75 == 1:
                        # JavaTreeParser.g:0:0: catches
                        pass 
                        self._state.following.append(self.FOLLOW_catches_in_statement4819)
                        self.catches()

                        self._state.following.pop()



                    # JavaTreeParser.g:564:10: ( block )?
                    alt76 = 2
                    LA76_0 = self.input.LA(1)

                    if (LA76_0 == BLOCK_SCOPE) :
                        alt76 = 1
                    if alt76 == 1:
                        # JavaTreeParser.g:564:11: block
                        pass 
                        if self._state.backtracking == 0:
                            self.beginTryFinally() 

                        self._state.following.append(self.FOLLOW_block_in_statement4834)
                        self.block()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            sef.endTryFinally() 





                    self.match(self.input, UP, None)


                elif alt80 == 9:
                    # JavaTreeParser.g:566:9: ^( SWITCH (pe0= parenthesizedExpression ) switchBlockLabels )
                    pass 
                    self.match(self.input, SWITCH, self.FOLLOW_SWITCH_in_statement4859)

                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:567:11: (pe0= parenthesizedExpression )
                    # JavaTreeParser.g:567:12: pe0= parenthesizedExpression
                    pass 
                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_statement4874)
                    pe0 = self.parenthesizedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.beginSwitch(pe0) 




                    self._state.following.append(self.FOLLOW_switchBlockLabels_in_statement4889)
                    self.switchBlockLabels()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.endSwitch() 


                    self.match(self.input, UP, None)


                elif alt80 == 10:
                    # JavaTreeParser.g:571:9: ^( SYNCHRONIZED (pe0= parenthesizedExpression ) block )
                    pass 
                    self.match(self.input, SYNCHRONIZED, self.FOLLOW_SYNCHRONIZED_in_statement4922)

                    if self._state.backtracking == 0:
                        self.beginSync() 


                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:573:11: (pe0= parenthesizedExpression )
                    # JavaTreeParser.g:573:12: pe0= parenthesizedExpression
                    pass 
                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_statement4949)
                    pe0 = self.parenthesizedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.setExpression(pe0) 




                    self._state.following.append(self.FOLLOW_block_in_statement4964)
                    self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.endSync() 


                    self.match(self.input, UP, None)


                elif alt80 == 11:
                    # JavaTreeParser.g:577:9: ^( RETURN (ex0= expression )? )
                    pass 
                    self.match(self.input, RETURN, self.FOLLOW_RETURN_in_statement4998)

                    if self._state.backtracking == 0:
                        value.update(format="return") 


                    if self.input.LA(1) == DOWN:
                        self.match(self.input, DOWN, None)
                        # JavaTreeParser.g:579:11: (ex0= expression )?
                        alt77 = 2
                        LA77_0 = self.input.LA(1)

                        if (LA77_0 == EXPR) :
                            alt77 = 1
                        if alt77 == 1:
                            # JavaTreeParser.g:579:12: ex0= expression
                            pass 
                            self._state.following.append(self.FOLLOW_expression_in_statement5025)
                            ex0 = self.expression()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                value.update(right=ex0) 




                        if self._state.backtracking == 0:
                            value.update(format="return ${right}") 


                        self.match(self.input, UP, None)



                elif alt80 == 12:
                    # JavaTreeParser.g:582:9: ^( THROW ex0= expression )
                    pass 
                    self.match(self.input, THROW, self.FOLLOW_THROW_in_statement5062)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_statement5066)
                    ex0 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addThrow(ex0) 


                    self.match(self.input, UP, None)


                elif alt80 == 13:
                    # JavaTreeParser.g:583:9: ^( BREAK (id0= IDENT )? )
                    pass 
                    self.match(self.input, BREAK, self.FOLLOW_BREAK_in_statement5080)

                    if self.input.LA(1) == DOWN:
                        self.match(self.input, DOWN, None)
                        # JavaTreeParser.g:583:17: (id0= IDENT )?
                        alt78 = 2
                        LA78_0 = self.input.LA(1)

                        if (LA78_0 == IDENT) :
                            alt78 = 1
                        if alt78 == 1:
                            # JavaTreeParser.g:583:18: id0= IDENT
                            pass 
                            id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_statement5085)
                            if self._state.backtracking == 0:
                                label = id0.text 





                        self.match(self.input, UP, None)

                    if self._state.backtracking == 0:
                        self.addBreak(label=label) 



                elif alt80 == 14:
                    # JavaTreeParser.g:584:9: ^( CONTINUE (id0= IDENT )? )
                    pass 
                    self.match(self.input, CONTINUE, self.FOLLOW_CONTINUE_in_statement5104)

                    if self.input.LA(1) == DOWN:
                        self.match(self.input, DOWN, None)
                        # JavaTreeParser.g:584:20: (id0= IDENT )?
                        alt79 = 2
                        LA79_0 = self.input.LA(1)

                        if (LA79_0 == IDENT) :
                            alt79 = 1
                        if alt79 == 1:
                            # JavaTreeParser.g:584:21: id0= IDENT
                            pass 
                            id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_statement5109)
                            if self._state.backtracking == 0:
                                label = id0.text 





                        self.match(self.input, UP, None)

                    if self._state.backtracking == 0:
                        self.addContinue(label=label) 



                elif alt80 == 15:
                    # JavaTreeParser.g:585:9: ^( LABELED_STATEMENT id0= IDENT lb0= statement )
                    pass 
                    self.match(self.input, LABELED_STATEMENT, self.FOLLOW_LABELED_STATEMENT_in_statement5127)

                    self.match(self.input, DOWN, None)
                    id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_statement5131)
                    self._state.following.append(self.FOLLOW_statement_in_statement5135)
                    lb0 = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addLabel(id0.text) 


                    self.match(self.input, UP, None)


                elif alt80 == 16:
                    # JavaTreeParser.g:586:9: ex0= expression
                    pass 
                    self._state.following.append(self.FOLLOW_expression_in_statement5150)
                    ex0 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex0 



                elif alt80 == 17:
                    # JavaTreeParser.g:587:9: SEMI
                    pass 
                    self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement5162)



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
    # JavaTreeParser.g:590:1: catches : ^( CATCH_CLAUSE_LIST ( catchClause )+ ) ;
    def catches(self, ):

        catches_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 52):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:591:5: ( ^( CATCH_CLAUSE_LIST ( catchClause )+ ) )
                # JavaTreeParser.g:591:9: ^( CATCH_CLAUSE_LIST ( catchClause )+ )
                pass 
                self.match(self.input, CATCH_CLAUSE_LIST, self.FOLLOW_CATCH_CLAUSE_LIST_in_catches5183)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:591:29: ( catchClause )+
                cnt81 = 0
                while True: #loop81
                    alt81 = 2
                    LA81_0 = self.input.LA(1)

                    if (LA81_0 == CATCH) :
                        alt81 = 1


                    if alt81 == 1:
                        # JavaTreeParser.g:0:0: catchClause
                        pass 
                        self._state.following.append(self.FOLLOW_catchClause_in_catches5185)
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
    # JavaTreeParser.g:594:1: catchClause : ^( CATCH fp0= formalParameterStandardDecl block ) ;
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

                # JavaTreeParser.g:595:5: ( ^( CATCH fp0= formalParameterStandardDecl block ) )
                # JavaTreeParser.g:595:9: ^( CATCH fp0= formalParameterStandardDecl block )
                pass 
                self.match(self.input, CATCH, self.FOLLOW_CATCH_in_catchClause5207)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_formalParameterStandardDecl_in_catchClause5221)
                fp0 = self.formalParameterStandardDecl()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self.beginCatch(fp0) 

                self._state.following.append(self.FOLLOW_block_in_catchClause5235)
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
    # JavaTreeParser.g:601:1: switchBlockLabels : ^( SWITCH_BLOCK_LABEL_LIST ( switchCaseLabel )* ( switchDefaultLabel )? ) ;
    def switchBlockLabels(self, ):

        switchBlockLabels_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 54):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:604:5: ( ^( SWITCH_BLOCK_LABEL_LIST ( switchCaseLabel )* ( switchDefaultLabel )? ) )
                # JavaTreeParser.g:604:9: ^( SWITCH_BLOCK_LABEL_LIST ( switchCaseLabel )* ( switchDefaultLabel )? )
                pass 
                self.match(self.input, SWITCH_BLOCK_LABEL_LIST, self.FOLLOW_SWITCH_BLOCK_LABEL_LIST_in_switchBlockLabels5269)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:604:35: ( switchCaseLabel )*
                    while True: #loop82
                        alt82 = 2
                        LA82_0 = self.input.LA(1)

                        if (LA82_0 == CASE) :
                            alt82 = 1


                        if alt82 == 1:
                            # JavaTreeParser.g:0:0: switchCaseLabel
                            pass 
                            self._state.following.append(self.FOLLOW_switchCaseLabel_in_switchBlockLabels5271)
                            self.switchCaseLabel()

                            self._state.following.pop()


                        else:
                            break #loop82


                    # JavaTreeParser.g:604:52: ( switchDefaultLabel )?
                    alt83 = 2
                    LA83_0 = self.input.LA(1)

                    if (LA83_0 == DEFAULT) :
                        alt83 = 1
                    if alt83 == 1:
                        # JavaTreeParser.g:0:0: switchDefaultLabel
                        pass 
                        self._state.following.append(self.FOLLOW_switchDefaultLabel_in_switchBlockLabels5274)
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
    # JavaTreeParser.g:607:1: switchCaseLabel : ^( CASE (ex0= expression ) ( blockStatement )* ) ;
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

                # JavaTreeParser.g:608:5: ( ^( CASE (ex0= expression ) ( blockStatement )* ) )
                # JavaTreeParser.g:608:9: ^( CASE (ex0= expression ) ( blockStatement )* )
                pass 
                self.match(self.input, CASE, self.FOLLOW_CASE_in_switchCaseLabel5296)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:609:11: (ex0= expression )
                # JavaTreeParser.g:609:13: ex0= expression
                pass 
                self._state.following.append(self.FOLLOW_expression_in_switchCaseLabel5312)
                ex0 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self.addSwitchCase(ex0) 




                # JavaTreeParser.g:610:11: ( blockStatement )*
                while True: #loop84
                    alt84 = 2
                    LA84_0 = self.input.LA(1)

                    if (LA84_0 == AT or LA84_0 == SEMI or LA84_0 == ASSERT or LA84_0 == BREAK or (CLASS <= LA84_0 <= CONTINUE) or LA84_0 == DO or LA84_0 == ENUM or (FOR <= LA84_0 <= IF) or LA84_0 == INTERFACE or LA84_0 == RETURN or (SWITCH <= LA84_0 <= SYNCHRONIZED) or LA84_0 == THROW or LA84_0 == TRY or LA84_0 == WHILE or LA84_0 == BLOCK_SCOPE or LA84_0 == EXPR or LA84_0 == FOR_EACH or LA84_0 == LABELED_STATEMENT or LA84_0 == VAR_DECLARATION) :
                        alt84 = 1


                    if alt84 == 1:
                        # JavaTreeParser.g:0:0: blockStatement
                        pass 
                        self._state.following.append(self.FOLLOW_blockStatement_in_switchCaseLabel5328)
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
    # JavaTreeParser.g:615:1: switchDefaultLabel : ^( DEFAULT ( blockStatement )* ) ;
    def switchDefaultLabel(self, ):

        switchDefaultLabel_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 56):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:616:5: ( ^( DEFAULT ( blockStatement )* ) )
                # JavaTreeParser.g:616:9: ^( DEFAULT ( blockStatement )* )
                pass 
                self.match(self.input, DEFAULT, self.FOLLOW_DEFAULT_in_switchDefaultLabel5369)

                if self._state.backtracking == 0:
                    self.addSwitchCaseDefault() 


                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:618:11: ( blockStatement )*
                    while True: #loop85
                        alt85 = 2
                        LA85_0 = self.input.LA(1)

                        if (LA85_0 == AT or LA85_0 == SEMI or LA85_0 == ASSERT or LA85_0 == BREAK or (CLASS <= LA85_0 <= CONTINUE) or LA85_0 == DO or LA85_0 == ENUM or (FOR <= LA85_0 <= IF) or LA85_0 == INTERFACE or LA85_0 == RETURN or (SWITCH <= LA85_0 <= SYNCHRONIZED) or LA85_0 == THROW or LA85_0 == TRY or LA85_0 == WHILE or LA85_0 == BLOCK_SCOPE or LA85_0 == EXPR or LA85_0 == FOR_EACH or LA85_0 == LABELED_STATEMENT or LA85_0 == VAR_DECLARATION) :
                            alt85 = 1


                        if alt85 == 1:
                            # JavaTreeParser.g:0:0: blockStatement
                            pass 
                            self._state.following.append(self.FOLLOW_blockStatement_in_switchDefaultLabel5393)
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
    # JavaTreeParser.g:623:1: forInit returns [values] : ^( FOR_INIT ( localVariableDeclaration | (ex0= expression )* )? ) ;
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

                # JavaTreeParser.g:625:5: ( ^( FOR_INIT ( localVariableDeclaration | (ex0= expression )* )? ) )
                # JavaTreeParser.g:625:9: ^( FOR_INIT ( localVariableDeclaration | (ex0= expression )* )? )
                pass 
                self.match(self.input, FOR_INIT, self.FOLLOW_FOR_INIT_in_forInit5447)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:625:20: ( localVariableDeclaration | (ex0= expression )* )?
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
                        # JavaTreeParser.g:626:11: localVariableDeclaration
                        pass 
                        self._state.following.append(self.FOLLOW_localVariableDeclaration_in_forInit5461)
                        self.localVariableDeclaration()

                        self._state.following.pop()


                    elif alt87 == 2:
                        # JavaTreeParser.g:627:11: (ex0= expression )*
                        pass 
                        # JavaTreeParser.g:627:11: (ex0= expression )*
                        while True: #loop86
                            alt86 = 2
                            LA86_0 = self.input.LA(1)

                            if (LA86_0 == EXPR) :
                                alt86 = 1


                            if alt86 == 1:
                                # JavaTreeParser.g:627:12: ex0= expression
                                pass 
                                self._state.following.append(self.FOLLOW_expression_in_forInit5478)
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
    # JavaTreeParser.g:631:1: forCondition returns [value] : ^( FOR_CONDITION (ex0= expression )? ) ;
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

                # JavaTreeParser.g:633:5: ( ^( FOR_CONDITION (ex0= expression )? ) )
                # JavaTreeParser.g:633:9: ^( FOR_CONDITION (ex0= expression )? )
                pass 
                self.match(self.input, FOR_CONDITION, self.FOLLOW_FOR_CONDITION_in_forCondition5527)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:633:28: (ex0= expression )?
                    alt88 = 2
                    LA88_0 = self.input.LA(1)

                    if (LA88_0 == EXPR) :
                        alt88 = 1
                    if alt88 == 1:
                        # JavaTreeParser.g:0:0: ex0= expression
                        pass 
                        self._state.following.append(self.FOLLOW_expression_in_forCondition5531)
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
    # JavaTreeParser.g:636:1: forUpdater returns [values] : ^( FOR_UPDATE (ex0= expression )* ) ;
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

                # JavaTreeParser.g:638:5: ( ^( FOR_UPDATE (ex0= expression )* ) )
                # JavaTreeParser.g:638:9: ^( FOR_UPDATE (ex0= expression )* )
                pass 
                self.match(self.input, FOR_UPDATE, self.FOLLOW_FOR_UPDATE_in_forUpdater5569)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:638:22: (ex0= expression )*
                    while True: #loop89
                        alt89 = 2
                        LA89_0 = self.input.LA(1)

                        if (LA89_0 == EXPR) :
                            alt89 = 1


                        if alt89 == 1:
                            # JavaTreeParser.g:638:23: ex0= expression
                            pass 
                            self._state.following.append(self.FOLLOW_expression_in_forUpdater5574)
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
    # JavaTreeParser.g:641:1: parenthesizedExpression returns [value] : ^( PARENTESIZED_EXPR ex0= expression ) ;
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

                # JavaTreeParser.g:642:5: ( ^( PARENTESIZED_EXPR ex0= expression ) )
                # JavaTreeParser.g:642:9: ^( PARENTESIZED_EXPR ex0= expression )
                pass 
                self.match(self.input, PARENTESIZED_EXPR, self.FOLLOW_PARENTESIZED_EXPR_in_parenthesizedExpression5603)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_expression_in_parenthesizedExpression5607)
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
    # JavaTreeParser.g:645:1: expression returns [value] : ^( EXPR ex0= expr ) ;
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

                # JavaTreeParser.g:646:5: ( ^( EXPR ex0= expr ) )
                # JavaTreeParser.g:646:9: ^( EXPR ex0= expr )
                pass 
                self.match(self.input, EXPR, self.FOLLOW_EXPR_in_expression5634)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_expr_in_expression5638)
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
    # JavaTreeParser.g:649:1: expr returns [value] : ( ^( ASSIGN lv0= expr rv0= expr ) | ^( PLUS_ASSIGN lv0= expr rv0= expr ) | ^( MINUS_ASSIGN lv0= expr rv0= expr ) | ^( STAR_ASSIGN lv0= expr rv0= expr ) | ^( DIV_ASSIGN lv0= expr rv0= expr ) | ^( AND_ASSIGN lv0= expr rv0= expr ) | ^( OR_ASSIGN lv0= expr rv0= expr ) | ^( XOR_ASSIGN lv0= expr rv0= expr ) | ^( MOD_ASSIGN lv0= expr rv0= expr ) | ^( BIT_SHIFT_RIGHT_ASSIGN expr expr ) | ^( SHIFT_RIGHT_ASSIGN expr expr ) | ^( SHIFT_LEFT_ASSIGN expr expr ) | ^( QUESTION lv0= expr rv0= expr cv0= expr ) | ^( LOGICAL_OR lv0= expr rv0= expr ) | ^( LOGICAL_AND lv0= expr rv0= expr ) | ^( OR lv0= expr rv0= expr ) | ^( XOR lv0= expr rv0= expr ) | ^( AND lv0= expr rv0= expr ) | ^( EQUAL lv0= expr rv0= expr ) | ^( NOT_EQUAL lv0= expr rv0= expr ) | ^( INSTANCEOF lv0= expr tp0= type ) | ^( LESS_OR_EQUAL lv0= expr rv0= expr ) | ^( GREATER_OR_EQUAL lv0= expr rv0= expr ) | ^( BIT_SHIFT_RIGHT lv0= expr rv0= expr ) | ^( SHIFT_RIGHT lv0= expr rv0= expr ) | ^( GREATER_THAN lv0= expr rv0= expr ) | ^( SHIFT_LEFT lv0= expr rv0= expr ) | ^( LESS_THAN lv0= expr rv0= expr ) | ^( PLUS lv0= expr rv0= expr ) | ^( MINUS lv0= expr rv0= expr ) | ^( STAR lv0= expr rv0= expr ) | ^( DIV lv0= expr rv0= expr ) | ^( MOD lv0= expr rv0= expr ) | ^( UNARY_PLUS lv0= expr ) | ^( UNARY_MINUS lv0= expr ) | ^( PRE_INC lv0= expr ) | ^( PRE_DEC lv0= expr ) | ^( POST_INC lv0= expr ) | ^( POST_DEC lv0= expr ) | ^( NOT lv0= expr ) | ^( LOGICAL_NOT lv0= expr ) | ^( CAST_EXPR tp0= type rv0= expr ) | pe0= primaryExpression );
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

                # JavaTreeParser.g:657:5: ( ^( ASSIGN lv0= expr rv0= expr ) | ^( PLUS_ASSIGN lv0= expr rv0= expr ) | ^( MINUS_ASSIGN lv0= expr rv0= expr ) | ^( STAR_ASSIGN lv0= expr rv0= expr ) | ^( DIV_ASSIGN lv0= expr rv0= expr ) | ^( AND_ASSIGN lv0= expr rv0= expr ) | ^( OR_ASSIGN lv0= expr rv0= expr ) | ^( XOR_ASSIGN lv0= expr rv0= expr ) | ^( MOD_ASSIGN lv0= expr rv0= expr ) | ^( BIT_SHIFT_RIGHT_ASSIGN expr expr ) | ^( SHIFT_RIGHT_ASSIGN expr expr ) | ^( SHIFT_LEFT_ASSIGN expr expr ) | ^( QUESTION lv0= expr rv0= expr cv0= expr ) | ^( LOGICAL_OR lv0= expr rv0= expr ) | ^( LOGICAL_AND lv0= expr rv0= expr ) | ^( OR lv0= expr rv0= expr ) | ^( XOR lv0= expr rv0= expr ) | ^( AND lv0= expr rv0= expr ) | ^( EQUAL lv0= expr rv0= expr ) | ^( NOT_EQUAL lv0= expr rv0= expr ) | ^( INSTANCEOF lv0= expr tp0= type ) | ^( LESS_OR_EQUAL lv0= expr rv0= expr ) | ^( GREATER_OR_EQUAL lv0= expr rv0= expr ) | ^( BIT_SHIFT_RIGHT lv0= expr rv0= expr ) | ^( SHIFT_RIGHT lv0= expr rv0= expr ) | ^( GREATER_THAN lv0= expr rv0= expr ) | ^( SHIFT_LEFT lv0= expr rv0= expr ) | ^( LESS_THAN lv0= expr rv0= expr ) | ^( PLUS lv0= expr rv0= expr ) | ^( MINUS lv0= expr rv0= expr ) | ^( STAR lv0= expr rv0= expr ) | ^( DIV lv0= expr rv0= expr ) | ^( MOD lv0= expr rv0= expr ) | ^( UNARY_PLUS lv0= expr ) | ^( UNARY_MINUS lv0= expr ) | ^( PRE_INC lv0= expr ) | ^( PRE_DEC lv0= expr ) | ^( POST_INC lv0= expr ) | ^( POST_DEC lv0= expr ) | ^( NOT lv0= expr ) | ^( LOGICAL_NOT lv0= expr ) | ^( CAST_EXPR tp0= type rv0= expr ) | pe0= primaryExpression )
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
                    # JavaTreeParser.g:657:9: ^( ASSIGN lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_expr5674)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5678)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5682)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "=")   


                    self.match(self.input, UP, None)


                elif alt90 == 2:
                    # JavaTreeParser.g:658:9: ^( PLUS_ASSIGN lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, PLUS_ASSIGN, self.FOLLOW_PLUS_ASSIGN_in_expr5702)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5706)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5710)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "+=")  


                    self.match(self.input, UP, None)


                elif alt90 == 3:
                    # JavaTreeParser.g:659:9: ^( MINUS_ASSIGN lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, MINUS_ASSIGN, self.FOLLOW_MINUS_ASSIGN_in_expr5725)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5729)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5733)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "-=")  


                    self.match(self.input, UP, None)


                elif alt90 == 4:
                    # JavaTreeParser.g:660:9: ^( STAR_ASSIGN lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, STAR_ASSIGN, self.FOLLOW_STAR_ASSIGN_in_expr5747)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5751)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5755)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "*=")  


                    self.match(self.input, UP, None)


                elif alt90 == 5:
                    # JavaTreeParser.g:661:9: ^( DIV_ASSIGN lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, DIV_ASSIGN, self.FOLLOW_DIV_ASSIGN_in_expr5770)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5774)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5778)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "/=")  


                    self.match(self.input, UP, None)


                elif alt90 == 6:
                    # JavaTreeParser.g:662:9: ^( AND_ASSIGN lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, AND_ASSIGN, self.FOLLOW_AND_ASSIGN_in_expr5794)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5798)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5802)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "&=")  


                    self.match(self.input, UP, None)


                elif alt90 == 7:
                    # JavaTreeParser.g:663:9: ^( OR_ASSIGN lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, OR_ASSIGN, self.FOLLOW_OR_ASSIGN_in_expr5818)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5822)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5826)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "|=")  


                    self.match(self.input, UP, None)


                elif alt90 == 8:
                    # JavaTreeParser.g:664:9: ^( XOR_ASSIGN lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, XOR_ASSIGN, self.FOLLOW_XOR_ASSIGN_in_expr5843)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5847)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5851)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "^=")  


                    self.match(self.input, UP, None)


                elif alt90 == 9:
                    # JavaTreeParser.g:665:9: ^( MOD_ASSIGN lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, MOD_ASSIGN, self.FOLLOW_MOD_ASSIGN_in_expr5867)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5871)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5875)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "%=") 


                    self.match(self.input, UP, None)


                elif alt90 == 10:
                    # JavaTreeParser.g:666:9: ^( BIT_SHIFT_RIGHT_ASSIGN expr expr )
                    pass 
                    self.match(self.input, BIT_SHIFT_RIGHT_ASSIGN, self.FOLLOW_BIT_SHIFT_RIGHT_ASSIGN_in_expr5891)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5893)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5895)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt90 == 11:
                    # JavaTreeParser.g:667:9: ^( SHIFT_RIGHT_ASSIGN expr expr )
                    pass 
                    self.match(self.input, SHIFT_RIGHT_ASSIGN, self.FOLLOW_SHIFT_RIGHT_ASSIGN_in_expr5907)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5909)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5911)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt90 == 12:
                    # JavaTreeParser.g:668:9: ^( SHIFT_LEFT_ASSIGN expr expr )
                    pass 
                    self.match(self.input, SHIFT_LEFT_ASSIGN, self.FOLLOW_SHIFT_LEFT_ASSIGN_in_expr5923)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5925)
                    self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5927)
                    self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt90 == 13:
                    # JavaTreeParser.g:669:9: ^( QUESTION lv0= expr rv0= expr cv0= expr )
                    pass 
                    self.match(self.input, QUESTION, self.FOLLOW_QUESTION_in_expr5939)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5943)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5947)
                    rv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5951)
                    cv0 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        value.update(left=lv0, right=rv0,
                                      format="(${right} if ${left} else ${center})", center=cv0) 



                elif alt90 == 14:
                    # JavaTreeParser.g:672:9: ^( LOGICAL_OR lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, LOGICAL_OR, self.FOLLOW_LOGICAL_OR_in_expr5975)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr5979)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr5983)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "or")               


                    self.match(self.input, UP, None)


                elif alt90 == 15:
                    # JavaTreeParser.g:673:9: ^( LOGICAL_AND lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, LOGICAL_AND, self.FOLLOW_LOGICAL_AND_in_expr6003)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6007)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6011)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "and")              


                    self.match(self.input, UP, None)


                elif alt90 == 16:
                    # JavaTreeParser.g:674:9: ^( OR lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, OR, self.FOLLOW_OR_in_expr6030)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6034)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6038)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "|")                


                    self.match(self.input, UP, None)


                elif alt90 == 17:
                    # JavaTreeParser.g:675:9: ^( XOR lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, XOR, self.FOLLOW_XOR_in_expr6066)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6070)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6074)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "^")                


                    self.match(self.input, UP, None)


                elif alt90 == 18:
                    # JavaTreeParser.g:676:9: ^( AND lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, AND, self.FOLLOW_AND_in_expr6101)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6105)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6109)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "&")                


                    self.match(self.input, UP, None)


                elif alt90 == 19:
                    # JavaTreeParser.g:677:9: ^( EQUAL lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_expr6136)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6140)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6144)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "==")               


                    self.match(self.input, UP, None)


                elif alt90 == 20:
                    # JavaTreeParser.g:678:9: ^( NOT_EQUAL lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, NOT_EQUAL, self.FOLLOW_NOT_EQUAL_in_expr6169)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6173)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6177)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "!=")               


                    self.match(self.input, UP, None)


                elif alt90 == 21:
                    # JavaTreeParser.g:679:9: ^( INSTANCEOF lv0= expr tp0= type )
                    pass 
                    self.match(self.input, INSTANCEOF, self.FOLLOW_INSTANCEOF_in_expr6198)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6202)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_type_in_expr6206)
                    tp0 = self.type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex(lv0, ((tp0 is not None) and [tp0.value] or [None])[0], "isinstance(${left}, (${right}, ))") 


                    self.match(self.input, UP, None)


                elif alt90 == 22:
                    # JavaTreeParser.g:681:9: ^( LESS_OR_EQUAL lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, LESS_OR_EQUAL, self.FOLLOW_LESS_OR_EQUAL_in_expr6230)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6234)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6238)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "<=")               


                    self.match(self.input, UP, None)


                elif alt90 == 23:
                    # JavaTreeParser.g:682:9: ^( GREATER_OR_EQUAL lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, GREATER_OR_EQUAL, self.FOLLOW_GREATER_OR_EQUAL_in_expr6255)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6259)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6263)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, ">=")               


                    self.match(self.input, UP, None)


                elif alt90 == 24:
                    # JavaTreeParser.g:683:9: ^( BIT_SHIFT_RIGHT lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, BIT_SHIFT_RIGHT, self.FOLLOW_BIT_SHIFT_RIGHT_in_expr6277)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6281)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6285)
                    rv0 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt90 == 25:
                    # JavaTreeParser.g:684:9: ^( SHIFT_RIGHT lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, SHIFT_RIGHT, self.FOLLOW_SHIFT_RIGHT_in_expr6345)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6349)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6353)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, ">>")               


                    self.match(self.input, UP, None)


                elif alt90 == 26:
                    # JavaTreeParser.g:685:9: ^( GREATER_THAN lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, GREATER_THAN, self.FOLLOW_GREATER_THAN_in_expr6372)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6376)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6380)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, ">")                


                    self.match(self.input, UP, None)


                elif alt90 == 27:
                    # JavaTreeParser.g:686:9: ^( SHIFT_LEFT lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, SHIFT_LEFT, self.FOLLOW_SHIFT_LEFT_in_expr6398)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6402)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6406)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "<<")               


                    self.match(self.input, UP, None)


                elif alt90 == 28:
                    # JavaTreeParser.g:687:9: ^( LESS_THAN lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, LESS_THAN, self.FOLLOW_LESS_THAN_in_expr6426)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6430)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6434)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "<")                


                    self.match(self.input, UP, None)


                elif alt90 == 29:
                    # JavaTreeParser.g:688:9: ^( PLUS lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, PLUS, self.FOLLOW_PLUS_in_expr6455)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6459)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6463)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "+")                


                    self.match(self.input, UP, None)


                elif alt90 == 30:
                    # JavaTreeParser.g:689:9: ^( MINUS lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, MINUS, self.FOLLOW_MINUS_in_expr6489)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6493)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6497)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "-")                


                    self.match(self.input, UP, None)


                elif alt90 == 31:
                    # JavaTreeParser.g:690:9: ^( STAR lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, STAR, self.FOLLOW_STAR_in_expr6522)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6526)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6530)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "*")                


                    self.match(self.input, UP, None)


                elif alt90 == 32:
                    # JavaTreeParser.g:691:9: ^( DIV lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, DIV, self.FOLLOW_DIV_in_expr6556)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6560)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6564)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "/")                


                    self.match(self.input, UP, None)


                elif alt90 == 33:
                    # JavaTreeParser.g:692:9: ^( MOD lv0= expr rv0= expr )
                    pass 
                    self.match(self.input, MOD, self.FOLLOW_MOD_in_expr6591)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6595)
                    lv0 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6599)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs(lv0, rv0, "%")               


                    self.match(self.input, UP, None)


                elif alt90 == 34:
                    # JavaTreeParser.g:693:9: ^( UNARY_PLUS lv0= expr )
                    pass 
                    self.match(self.input, UNARY_PLUS, self.FOLLOW_UNARY_PLUS_in_expr6626)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6630)
                    lv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs1(lv0, "+")                    


                    self.match(self.input, UP, None)


                elif alt90 == 35:
                    # JavaTreeParser.g:694:9: ^( UNARY_MINUS lv0= expr )
                    pass 
                    self.match(self.input, UNARY_MINUS, self.FOLLOW_UNARY_MINUS_in_expr6659)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6663)
                    lv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = exs1(lv0, "-")                    


                    self.match(self.input, UP, None)


                elif alt90 == 36:
                    # JavaTreeParser.g:695:9: ^( PRE_INC lv0= expr )
                    pass 
                    self.match(self.input, PRE_INC, self.FOLLOW_PRE_INC_in_expr6691)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6695)
                    lv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex(lv0, format="${left} += 1")    


                    self.match(self.input, UP, None)


                elif alt90 == 37:
                    # JavaTreeParser.g:696:9: ^( PRE_DEC lv0= expr )
                    pass 
                    self.match(self.input, PRE_DEC, self.FOLLOW_PRE_DEC_in_expr6727)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6731)
                    lv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex(lv0, format="${left} -= 1")    


                    self.match(self.input, UP, None)


                elif alt90 == 38:
                    # JavaTreeParser.g:697:9: ^( POST_INC lv0= expr )
                    pass 
                    self.match(self.input, POST_INC, self.FOLLOW_POST_INC_in_expr6763)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6767)
                    lv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex(lv0, format="${left} += 1")    


                    self.match(self.input, UP, None)


                elif alt90 == 39:
                    # JavaTreeParser.g:698:9: ^( POST_DEC lv0= expr )
                    pass 
                    self.match(self.input, POST_DEC, self.FOLLOW_POST_DEC_in_expr6798)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6802)
                    lv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex(lv0, format="${left} -= 1")    


                    self.match(self.input, UP, None)


                elif alt90 == 40:
                    # JavaTreeParser.g:699:9: ^( NOT lv0= expr )
                    pass 
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_expr6833)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6837)
                    lv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex(lv0, format="~${left}")        


                    self.match(self.input, UP, None)


                elif alt90 == 41:
                    # JavaTreeParser.g:700:9: ^( LOGICAL_NOT lv0= expr )
                    pass 
                    self.match(self.input, LOGICAL_NOT, self.FOLLOW_LOGICAL_NOT_in_expr6873)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr6877)
                    lv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex(lv0, format="not ${left}")     


                    self.match(self.input, UP, None)


                elif alt90 == 42:
                    # JavaTreeParser.g:701:9: ^( CAST_EXPR tp0= type rv0= expr )
                    pass 
                    self.match(self.input, CAST_EXPR, self.FOLLOW_CAST_EXPR_in_expr6905)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_type_in_expr6909)
                    tp0 = self.type()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr6913)
                    rv0 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex(((tp0 is not None) and [tp0.value] or [None])[0], rv0, "${left}(${right})") 


                    self.match(self.input, UP, None)


                elif alt90 == 43:
                    # JavaTreeParser.g:702:9: pe0= primaryExpression
                    pass 
                    self._state.following.append(self.FOLLOW_primaryExpression_in_expr6935)
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
    # JavaTreeParser.g:708:1: primaryExpression returns [value] : ( ^( DOT (p0= primaryExpression ( IDENT | THIS | SUPER | ne0= innerNewExpression | CLASS ) | pt0= primitiveType CLASS | VOID CLASS ) ) | parenthesizedExpression | IDENT | ^( METHOD_CALL p0= primaryExpression ( genericTypeArgumentList )? a0= arguments ) | ec0= explicitConstructorCall | ^( ARRAY_ELEMENT_ACCESS p0= primaryExpression e0= expression ) | literal | newExpression | THIS | arrayTypeDeclarator | SUPER );
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

                # JavaTreeParser.g:710:5: ( ^( DOT (p0= primaryExpression ( IDENT | THIS | SUPER | ne0= innerNewExpression | CLASS ) | pt0= primitiveType CLASS | VOID CLASS ) ) | parenthesizedExpression | IDENT | ^( METHOD_CALL p0= primaryExpression ( genericTypeArgumentList )? a0= arguments ) | ec0= explicitConstructorCall | ^( ARRAY_ELEMENT_ACCESS p0= primaryExpression e0= expression ) | literal | newExpression | THIS | arrayTypeDeclarator | SUPER )
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
                    # JavaTreeParser.g:710:9: ^( DOT (p0= primaryExpression ( IDENT | THIS | SUPER | ne0= innerNewExpression | CLASS ) | pt0= primitiveType CLASS | VOID CLASS ) )
                    pass 
                    self.match(self.input, DOT, self.FOLLOW_DOT_in_primaryExpression6980)

                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:711:13: (p0= primaryExpression ( IDENT | THIS | SUPER | ne0= innerNewExpression | CLASS ) | pt0= primitiveType CLASS | VOID CLASS )
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
                        # JavaTreeParser.g:711:17: p0= primaryExpression ( IDENT | THIS | SUPER | ne0= innerNewExpression | CLASS )
                        pass 
                        self._state.following.append(self.FOLLOW_primaryExpression_in_primaryExpression7000)
                        p0 = self.primaryExpression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            value = ex(p0, format="${left}.${right}") 

                        # JavaTreeParser.g:713:17: ( IDENT | THIS | SUPER | ne0= innerNewExpression | CLASS )
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
                            # JavaTreeParser.g:713:21: IDENT
                            pass 
                            IDENT4=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_primaryExpression7040)
                            if self._state.backtracking == 0:
                                value["right"] = ex(IDENT4.text, format="${left}", rename=True) 



                        elif alt91 == 2:
                            # JavaTreeParser.g:715:21: THIS
                            pass 
                            self.match(self.input, THIS, self.FOLLOW_THIS_in_primaryExpression7084)
                            if self._state.backtracking == 0:
                                value["format"] = "${left}" 



                        elif alt91 == 3:
                            # JavaTreeParser.g:716:21: SUPER
                            pass 
                            self.match(self.input, SUPER, self.FOLLOW_SUPER_in_primaryExpression7110)
                            if self._state.backtracking == 0:
                                value["format"] = "${left}"
                                value["left"] = ex(value["left"], "", "super(${left}, self)")
                                                 



                        elif alt91 == 4:
                            # JavaTreeParser.g:720:18: ne0= innerNewExpression
                            pass 
                            self._state.following.append(self.FOLLOW_innerNewExpression_in_primaryExpression7150)
                            ne0 = self.innerNewExpression()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                value["right"] = ne0 



                        elif alt91 == 5:
                            # JavaTreeParser.g:721:21: CLASS
                            pass 
                            self.match(self.input, CLASS, self.FOLLOW_CLASS_in_primaryExpression7174)
                            if self._state.backtracking == 0:
                                value["right"] = ex("__class__", "", "${left}") 






                    elif alt92 == 2:
                        # JavaTreeParser.g:723:17: pt0= primitiveType CLASS
                        pass 
                        self._state.following.append(self.FOLLOW_primitiveType_in_primaryExpression7214)
                        pt0 = self.primitiveType()

                        self._state.following.pop()
                        self.match(self.input, CLASS, self.FOLLOW_CLASS_in_primaryExpression7216)
                        if self._state.backtracking == 0:
                            value = ex(((pt0 is not None) and [self.input.getTokenStream().toString(
                                self.input.getTreeAdaptor().getTokenStartIndex(pt0.start),
                                self.input.getTreeAdaptor().getTokenStopIndex(pt0.start)
                                )] or [None])[0], "__class__", "${left}.${right}") 



                    elif alt92 == 3:
                        # JavaTreeParser.g:724:17: VOID CLASS
                        pass 
                        self.match(self.input, VOID, self.FOLLOW_VOID_in_primaryExpression7236)
                        self.match(self.input, CLASS, self.FOLLOW_CLASS_in_primaryExpression7238)
                        if self._state.backtracking == 0:
                            value = ex("None", "__class__", "${left}.${right}") 





                    self.match(self.input, UP, None)


                elif alt94 == 2:
                    # JavaTreeParser.g:728:9: parenthesizedExpression
                    pass 
                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_primaryExpression7275)
                    parenthesizedExpression5 = self.parenthesizedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = parenthesizedExpression5 



                elif alt94 == 3:
                    # JavaTreeParser.g:729:9: IDENT
                    pass 
                    IDENT6=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_primaryExpression7287)
                    if self._state.backtracking == 0:
                        value = ex(self.altIdent(IDENT6.text), format="${left}", rename=True)  



                elif alt94 == 4:
                    # JavaTreeParser.g:730:9: ^( METHOD_CALL p0= primaryExpression ( genericTypeArgumentList )? a0= arguments )
                    pass 
                    self.match(self.input, METHOD_CALL, self.FOLLOW_METHOD_CALL_in_primaryExpression7300)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_primaryExpression_in_primaryExpression7314)
                    p0 = self.primaryExpression()

                    self._state.following.pop()
                    # JavaTreeParser.g:732:11: ( genericTypeArgumentList )?
                    alt93 = 2
                    LA93_0 = self.input.LA(1)

                    if (LA93_0 == GENERIC_TYPE_ARG_LIST) :
                        alt93 = 1
                    if alt93 == 1:
                        # JavaTreeParser.g:0:0: genericTypeArgumentList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeArgumentList_in_primaryExpression7326)
                        self.genericTypeArgumentList()

                        self._state.following.pop()



                    self._state.following.append(self.FOLLOW_arguments_in_primaryExpression7341)
                    a0 = self.arguments()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex(p0, a0, "${left}(${right})", call=True) 


                    self.match(self.input, UP, None)


                elif alt94 == 5:
                    # JavaTreeParser.g:736:9: ec0= explicitConstructorCall
                    pass 
                    self._state.following.append(self.FOLLOW_explicitConstructorCall_in_primaryExpression7375)
                    ec0 = self.explicitConstructorCall()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self.addSuperCall(ec0) 



                elif alt94 == 6:
                    # JavaTreeParser.g:737:9: ^( ARRAY_ELEMENT_ACCESS p0= primaryExpression e0= expression )
                    pass 
                    self.match(self.input, ARRAY_ELEMENT_ACCESS, self.FOLLOW_ARRAY_ELEMENT_ACCESS_in_primaryExpression7388)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_primaryExpression_in_primaryExpression7402)
                    p0 = self.primaryExpression()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expression_in_primaryExpression7416)
                    e0 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex(p0, e0, "${left}[${right}]") 


                    self.match(self.input, UP, None)


                elif alt94 == 7:
                    # JavaTreeParser.g:742:9: literal
                    pass 
                    self._state.following.append(self.FOLLOW_literal_in_primaryExpression7448)
                    literal7 = self.literal()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ex(((literal7 is not None) and [literal7.value] or [None])[0], format="${left}") 



                elif alt94 == 8:
                    # JavaTreeParser.g:743:9: newExpression
                    pass 
                    self._state.following.append(self.FOLLOW_newExpression_in_primaryExpression7460)
                    newExpression8 = self.newExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = newExpression8 



                elif alt94 == 9:
                    # JavaTreeParser.g:744:9: THIS
                    pass 
                    self.match(self.input, THIS, self.FOLLOW_THIS_in_primaryExpression7472)
                    if self._state.backtracking == 0:
                        value = ex("self", format="${left}") 



                elif alt94 == 10:
                    # JavaTreeParser.g:745:9: arrayTypeDeclarator
                    pass 
                    self._state.following.append(self.FOLLOW_arrayTypeDeclarator_in_primaryExpression7484)
                    self.arrayTypeDeclarator()

                    self._state.following.pop()


                elif alt94 == 11:
                    # JavaTreeParser.g:746:9: SUPER
                    pass 
                    self.match(self.input, SUPER, self.FOLLOW_SUPER_in_primaryExpression7494)
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
    # JavaTreeParser.g:749:1: explicitConstructorCall returns [value] : ( ^( THIS_CONSTRUCTOR_CALL ( genericTypeArgumentList )? arguments ) | ^( SUPER_CONSTRUCTOR_CALL (pe0= primaryExpression )? ( genericTypeArgumentList )? (ag0= arguments ) ) );
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

                # JavaTreeParser.g:751:5: ( ^( THIS_CONSTRUCTOR_CALL ( genericTypeArgumentList )? arguments ) | ^( SUPER_CONSTRUCTOR_CALL (pe0= primaryExpression )? ( genericTypeArgumentList )? (ag0= arguments ) ) )
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
                    # JavaTreeParser.g:751:9: ^( THIS_CONSTRUCTOR_CALL ( genericTypeArgumentList )? arguments )
                    pass 
                    self.match(self.input, THIS_CONSTRUCTOR_CALL, self.FOLLOW_THIS_CONSTRUCTOR_CALL_in_explicitConstructorCall7529)

                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:751:33: ( genericTypeArgumentList )?
                    alt95 = 2
                    LA95_0 = self.input.LA(1)

                    if (LA95_0 == GENERIC_TYPE_ARG_LIST) :
                        alt95 = 1
                    if alt95 == 1:
                        # JavaTreeParser.g:0:0: genericTypeArgumentList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeArgumentList_in_explicitConstructorCall7531)
                        self.genericTypeArgumentList()

                        self._state.following.pop()



                    self._state.following.append(self.FOLLOW_arguments_in_explicitConstructorCall7534)
                    self.arguments()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                elif alt98 == 2:
                    # JavaTreeParser.g:752:9: ^( SUPER_CONSTRUCTOR_CALL (pe0= primaryExpression )? ( genericTypeArgumentList )? (ag0= arguments ) )
                    pass 
                    self.match(self.input, SUPER_CONSTRUCTOR_CALL, self.FOLLOW_SUPER_CONSTRUCTOR_CALL_in_explicitConstructorCall7546)

                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:753:13: (pe0= primaryExpression )?
                    alt96 = 2
                    LA96_0 = self.input.LA(1)

                    if (LA96_0 == DOT or LA96_0 == FALSE or LA96_0 == NULL or LA96_0 == SUPER or LA96_0 == THIS or LA96_0 == TRUE or LA96_0 == ARRAY_DECLARATOR or LA96_0 == ARRAY_ELEMENT_ACCESS or LA96_0 == CLASS_CONSTRUCTOR_CALL or LA96_0 == METHOD_CALL or LA96_0 == PARENTESIZED_EXPR or (STATIC_ARRAY_CREATOR <= LA96_0 <= SUPER_CONSTRUCTOR_CALL) or LA96_0 == THIS_CONSTRUCTOR_CALL or (IDENT <= LA96_0 <= STRING_LITERAL)) :
                        alt96 = 1
                    if alt96 == 1:
                        # JavaTreeParser.g:753:14: pe0= primaryExpression
                        pass 
                        self._state.following.append(self.FOLLOW_primaryExpression_in_explicitConstructorCall7563)
                        pe0 = self.primaryExpression()

                        self._state.following.pop()



                    # JavaTreeParser.g:754:13: ( genericTypeArgumentList )?
                    alt97 = 2
                    LA97_0 = self.input.LA(1)

                    if (LA97_0 == GENERIC_TYPE_ARG_LIST) :
                        alt97 = 1
                    if alt97 == 1:
                        # JavaTreeParser.g:0:0: genericTypeArgumentList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeArgumentList_in_explicitConstructorCall7579)
                        self.genericTypeArgumentList()

                        self._state.following.pop()



                    # JavaTreeParser.g:755:13: (ag0= arguments )
                    # JavaTreeParser.g:755:14: ag0= arguments
                    pass 
                    self._state.following.append(self.FOLLOW_arguments_in_explicitConstructorCall7597)
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
    # JavaTreeParser.g:761:1: arrayTypeDeclarator : ^( ARRAY_DECLARATOR ( arrayTypeDeclarator | qualifiedIdentifier | primitiveType ) ) ;
    def arrayTypeDeclarator(self, ):

        arrayTypeDeclarator_StartIndex = self.input.index()
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 65):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return 

                # JavaTreeParser.g:762:5: ( ^( ARRAY_DECLARATOR ( arrayTypeDeclarator | qualifiedIdentifier | primitiveType ) ) )
                # JavaTreeParser.g:762:9: ^( ARRAY_DECLARATOR ( arrayTypeDeclarator | qualifiedIdentifier | primitiveType ) )
                pass 
                self.match(self.input, ARRAY_DECLARATOR, self.FOLLOW_ARRAY_DECLARATOR_in_arrayTypeDeclarator7656)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:762:28: ( arrayTypeDeclarator | qualifiedIdentifier | primitiveType )
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
                    # JavaTreeParser.g:762:29: arrayTypeDeclarator
                    pass 
                    self._state.following.append(self.FOLLOW_arrayTypeDeclarator_in_arrayTypeDeclarator7659)
                    self.arrayTypeDeclarator()

                    self._state.following.pop()


                elif alt99 == 2:
                    # JavaTreeParser.g:762:51: qualifiedIdentifier
                    pass 
                    self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_arrayTypeDeclarator7663)
                    self.qualifiedIdentifier()

                    self._state.following.pop()


                elif alt99 == 3:
                    # JavaTreeParser.g:762:73: primitiveType
                    pass 
                    self._state.following.append(self.FOLLOW_primitiveType_in_arrayTypeDeclarator7667)
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
    # JavaTreeParser.g:765:1: newExpression returns [value] : ( ^( STATIC_ARRAY_CREATOR (tp0= primitiveType ac0= newArrayConstruction | (gt1= genericTypeArgumentList )? tp1= qualifiedTypeIdent ac1= newArrayConstruction ) ) | ^( CLASS_CONSTRUCTOR_CALL ( genericTypeArgumentList )? q1= qualifiedTypeIdent a1= arguments ( classTopLevelScope )? ) );
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

                # JavaTreeParser.g:766:5: ( ^( STATIC_ARRAY_CREATOR (tp0= primitiveType ac0= newArrayConstruction | (gt1= genericTypeArgumentList )? tp1= qualifiedTypeIdent ac1= newArrayConstruction ) ) | ^( CLASS_CONSTRUCTOR_CALL ( genericTypeArgumentList )? q1= qualifiedTypeIdent a1= arguments ( classTopLevelScope )? ) )
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
                    # JavaTreeParser.g:766:9: ^( STATIC_ARRAY_CREATOR (tp0= primitiveType ac0= newArrayConstruction | (gt1= genericTypeArgumentList )? tp1= qualifiedTypeIdent ac1= newArrayConstruction ) )
                    pass 
                    self.match(self.input, STATIC_ARRAY_CREATOR, self.FOLLOW_STATIC_ARRAY_CREATOR_in_newExpression7693)

                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:767:11: (tp0= primitiveType ac0= newArrayConstruction | (gt1= genericTypeArgumentList )? tp1= qualifiedTypeIdent ac1= newArrayConstruction )
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
                        # JavaTreeParser.g:767:13: tp0= primitiveType ac0= newArrayConstruction
                        pass 
                        self._state.following.append(self.FOLLOW_primitiveType_in_newExpression7709)
                        tp0 = self.primitiveType()

                        self._state.following.pop()
                        self._state.following.append(self.FOLLOW_newArrayConstruction_in_newExpression7713)
                        ac0 = self.newArrayConstruction()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            value = self.makeArrayCreator(((tp0 is not None) and [self.input.getTokenStream().toString(
                                self.input.getTreeAdaptor().getTokenStartIndex(tp0.start),
                                self.input.getTreeAdaptor().getTokenStopIndex(tp0.start)
                                )] or [None])[0], ac0) 



                    elif alt101 == 2:
                        # JavaTreeParser.g:769:13: (gt1= genericTypeArgumentList )? tp1= qualifiedTypeIdent ac1= newArrayConstruction
                        pass 
                        # JavaTreeParser.g:769:16: (gt1= genericTypeArgumentList )?
                        alt100 = 2
                        LA100_0 = self.input.LA(1)

                        if (LA100_0 == GENERIC_TYPE_ARG_LIST) :
                            alt100 = 1
                        if alt100 == 1:
                            # JavaTreeParser.g:0:0: gt1= genericTypeArgumentList
                            pass 
                            self._state.following.append(self.FOLLOW_genericTypeArgumentList_in_newExpression7743)
                            gt1 = self.genericTypeArgumentList()

                            self._state.following.pop()



                        self._state.following.append(self.FOLLOW_qualifiedTypeIdent_in_newExpression7748)
                        tp1 = self.qualifiedTypeIdent()

                        self._state.following.pop()
                        self._state.following.append(self.FOLLOW_newArrayConstruction_in_newExpression7752)
                        ac1 = self.newArrayConstruction()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            value = self.makeArrayCreator(tp1, ac1, gt1) 





                    self.match(self.input, UP, None)


                elif alt104 == 2:
                    # JavaTreeParser.g:773:9: ^( CLASS_CONSTRUCTOR_CALL ( genericTypeArgumentList )? q1= qualifiedTypeIdent a1= arguments ( classTopLevelScope )? )
                    pass 
                    self.match(self.input, CLASS_CONSTRUCTOR_CALL, self.FOLLOW_CLASS_CONSTRUCTOR_CALL_in_newExpression7799)

                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:774:11: ( genericTypeArgumentList )?
                    alt102 = 2
                    LA102_0 = self.input.LA(1)

                    if (LA102_0 == GENERIC_TYPE_ARG_LIST) :
                        alt102 = 1
                    if alt102 == 1:
                        # JavaTreeParser.g:0:0: genericTypeArgumentList
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeArgumentList_in_newExpression7811)
                        self.genericTypeArgumentList()

                        self._state.following.pop()



                    self._state.following.append(self.FOLLOW_qualifiedTypeIdent_in_newExpression7826)
                    q1 = self.qualifiedTypeIdent()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_arguments_in_newExpression7840)
                    a1 = self.arguments()

                    self._state.following.pop()
                    # JavaTreeParser.g:777:11: ( classTopLevelScope )?
                    alt103 = 2
                    LA103_0 = self.input.LA(1)

                    if (LA103_0 == CLASS_TOP_LEVEL_SCOPE) :
                        alt103 = 1
                    if alt103 == 1:
                        # JavaTreeParser.g:0:0: classTopLevelScope
                        pass 
                        self._state.following.append(self.FOLLOW_classTopLevelScope_in_newExpression7852)
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
    # JavaTreeParser.g:783:1: innerNewExpression returns [value] : ^( CLASS_CONSTRUCTOR_CALL ( genericTypeArgumentList )? id0= IDENT ag0= arguments ( classTopLevelScope )? ) ;
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

                # JavaTreeParser.g:784:5: ( ^( CLASS_CONSTRUCTOR_CALL ( genericTypeArgumentList )? id0= IDENT ag0= arguments ( classTopLevelScope )? ) )
                # JavaTreeParser.g:784:9: ^( CLASS_CONSTRUCTOR_CALL ( genericTypeArgumentList )? id0= IDENT ag0= arguments ( classTopLevelScope )? )
                pass 
                self.match(self.input, CLASS_CONSTRUCTOR_CALL, self.FOLLOW_CLASS_CONSTRUCTOR_CALL_in_innerNewExpression7900)

                self.match(self.input, DOWN, None)
                # JavaTreeParser.g:785:11: ( genericTypeArgumentList )?
                alt105 = 2
                LA105_0 = self.input.LA(1)

                if (LA105_0 == GENERIC_TYPE_ARG_LIST) :
                    alt105 = 1
                if alt105 == 1:
                    # JavaTreeParser.g:0:0: genericTypeArgumentList
                    pass 
                    self._state.following.append(self.FOLLOW_genericTypeArgumentList_in_innerNewExpression7912)
                    self.genericTypeArgumentList()

                    self._state.following.pop()



                id0=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_innerNewExpression7927)
                self._state.following.append(self.FOLLOW_arguments_in_innerNewExpression7941)
                ag0 = self.arguments()

                self._state.following.pop()
                # JavaTreeParser.g:788:11: ( classTopLevelScope )?
                alt106 = 2
                LA106_0 = self.input.LA(1)

                if (LA106_0 == CLASS_TOP_LEVEL_SCOPE) :
                    alt106 = 1
                if alt106 == 1:
                    # JavaTreeParser.g:0:0: classTopLevelScope
                    pass 
                    self._state.following.append(self.FOLLOW_classTopLevelScope_in_innerNewExpression7953)
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
    # JavaTreeParser.g:793:1: newArrayConstruction returns [value] : (ad0= arrayDeclaratorList ai0= arrayInitializer | (ex0= expression )+ ( arrayDeclaratorList )? );
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

                # JavaTreeParser.g:795:5: (ad0= arrayDeclaratorList ai0= arrayInitializer | (ex0= expression )+ ( arrayDeclaratorList )? )
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
                    # JavaTreeParser.g:795:9: ad0= arrayDeclaratorList ai0= arrayInitializer
                    pass 
                    self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_newArrayConstruction8010)
                    ad0 = self.arrayDeclaratorList()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_arrayInitializer_in_newArrayConstruction8014)
                    ai0 = self.arrayInitializer()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        value = ai0 



                elif alt109 == 2:
                    # JavaTreeParser.g:797:9: (ex0= expression )+ ( arrayDeclaratorList )?
                    pass 
                    # JavaTreeParser.g:797:9: (ex0= expression )+
                    cnt107 = 0
                    while True: #loop107
                        alt107 = 2
                        LA107_0 = self.input.LA(1)

                        if (LA107_0 == EXPR) :
                            alt107 = 1


                        if alt107 == 1:
                            # JavaTreeParser.g:797:10: ex0= expression
                            pass 
                            self._state.following.append(self.FOLLOW_expression_in_newArrayConstruction8037)
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


                    # JavaTreeParser.g:801:9: ( arrayDeclaratorList )?
                    alt108 = 2
                    LA108_0 = self.input.LA(1)

                    if (LA108_0 == ARRAY_DECLARATOR_LIST) :
                        alt108 = 1
                    if alt108 == 1:
                        # JavaTreeParser.g:0:0: arrayDeclaratorList
                        pass 
                        self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_newArrayConstruction8059)
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
    # JavaTreeParser.g:804:1: arguments returns [values] : ^( ARGUMENT_LIST (ex0= expression )* ) ;
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

                # JavaTreeParser.g:806:5: ( ^( ARGUMENT_LIST (ex0= expression )* ) )
                # JavaTreeParser.g:806:9: ^( ARGUMENT_LIST (ex0= expression )* )
                pass 
                self.match(self.input, ARGUMENT_LIST, self.FOLLOW_ARGUMENT_LIST_in_arguments8093)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # JavaTreeParser.g:806:25: (ex0= expression )*
                    while True: #loop110
                        alt110 = 2
                        LA110_0 = self.input.LA(1)

                        if (LA110_0 == EXPR) :
                            alt110 = 1


                        if alt110 == 1:
                            # JavaTreeParser.g:806:26: ex0= expression
                            pass 
                            self._state.following.append(self.FOLLOW_expression_in_arguments8098)
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
    # JavaTreeParser.g:811:1: literal returns [value] : ( HEX_LITERAL | OCTAL_LITERAL | DECIMAL_LITERAL | FLOATING_POINT_LITERAL | CHARACTER_LITERAL | STRING_LITERAL | TRUE | FALSE | NULL );
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

                # JavaTreeParser.g:812:5: ( HEX_LITERAL | OCTAL_LITERAL | DECIMAL_LITERAL | FLOATING_POINT_LITERAL | CHARACTER_LITERAL | STRING_LITERAL | TRUE | FALSE | NULL )
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
                    # JavaTreeParser.g:812:9: HEX_LITERAL
                    pass 
                    self.match(self.input, HEX_LITERAL, self.FOLLOW_HEX_LITERAL_in_literal8145)
                    if self._state.backtracking == 0:
                        retval.value = self.input.toString(retval.start, self.input.LT(-1))              



                elif alt111 == 2:
                    # JavaTreeParser.g:813:9: OCTAL_LITERAL
                    pass 
                    self.match(self.input, OCTAL_LITERAL, self.FOLLOW_OCTAL_LITERAL_in_literal8168)
                    if self._state.backtracking == 0:
                        retval.value = self.input.toString(retval.start, self.input.LT(-1))              



                elif alt111 == 3:
                    # JavaTreeParser.g:814:9: DECIMAL_LITERAL
                    pass 
                    self.match(self.input, DECIMAL_LITERAL, self.FOLLOW_DECIMAL_LITERAL_in_literal8189)
                    if self._state.backtracking == 0:
                        retval.value = formatFloat(self.input.toString(retval.start, self.input.LT(-1))) 



                elif alt111 == 4:
                    # JavaTreeParser.g:815:9: FLOATING_POINT_LITERAL
                    pass 
                    self.match(self.input, FLOATING_POINT_LITERAL, self.FOLLOW_FLOATING_POINT_LITERAL_in_literal8208)
                    if self._state.backtracking == 0:
                        retval.value = formatFloat(self.input.toString(retval.start, self.input.LT(-1))) 



                elif alt111 == 5:
                    # JavaTreeParser.g:816:9: CHARACTER_LITERAL
                    pass 
                    self.match(self.input, CHARACTER_LITERAL, self.FOLLOW_CHARACTER_LITERAL_in_literal8220)
                    if self._state.backtracking == 0:
                        retval.value = self.input.toString(retval.start, self.input.LT(-1))              



                elif alt111 == 6:
                    # JavaTreeParser.g:817:9: STRING_LITERAL
                    pass 
                    self.match(self.input, STRING_LITERAL, self.FOLLOW_STRING_LITERAL_in_literal8237)
                    if self._state.backtracking == 0:
                        retval.value = self.input.toString(retval.start, self.input.LT(-1))              



                elif alt111 == 7:
                    # JavaTreeParser.g:818:9: TRUE
                    pass 
                    self.match(self.input, TRUE, self.FOLLOW_TRUE_in_literal8257)
                    if self._state.backtracking == 0:
                        retval.value = "True"             



                elif alt111 == 8:
                    # JavaTreeParser.g:819:9: FALSE
                    pass 
                    self.match(self.input, FALSE, self.FOLLOW_FALSE_in_literal8287)
                    if self._state.backtracking == 0:
                        retval.value = "False"            



                elif alt111 == 9:
                    # JavaTreeParser.g:820:9: NULL
                    pass 
                    self.match(self.input, NULL, self.FOLLOW_NULL_in_literal8316)
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
        # JavaTreeParser.g:627:11: ( (ex0= expression )* )
        # JavaTreeParser.g:627:11: (ex0= expression )*
        pass 
        # JavaTreeParser.g:627:11: (ex0= expression )*
        while True: #loop142
            alt142 = 2
            LA142_0 = self.input.LA(1)

            if (LA142_0 == EXPR) :
                alt142 = 1


            if alt142 == 1:
                # JavaTreeParser.g:627:12: ex0= expression
                pass 
                self._state.following.append(self.FOLLOW_expression_in_synpred131_JavaTreeParser5478)
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
    FOLLOW_CLASS_in_typeDeclaration287 = frozenset([2])
    FOLLOW_modifierList_in_typeDeclaration313 = frozenset([164])
    FOLLOW_IDENT_in_typeDeclaration329 = frozenset([123, 128, 138, 140])
    FOLLOW_genericTypeParameterList_in_typeDeclaration343 = frozenset([123, 128, 138, 140])
    FOLLOW_extendsClause_in_typeDeclaration359 = frozenset([123, 128, 138, 140])
    FOLLOW_implementsClause_in_typeDeclaration378 = frozenset([123, 128, 138, 140])
    FOLLOW_classTopLevelScope_in_typeDeclaration394 = frozenset([3])
    FOLLOW_INTERFACE_in_typeDeclaration427 = frozenset([2])
    FOLLOW_modifierList_in_typeDeclaration453 = frozenset([164])
    FOLLOW_IDENT_in_typeDeclaration469 = frozenset([128, 138, 139])
    FOLLOW_genericTypeParameterList_in_typeDeclaration483 = frozenset([128, 138, 139])
    FOLLOW_extendsClause_in_typeDeclaration499 = frozenset([128, 138, 139])
    FOLLOW_interfaceTopLevelScope_in_typeDeclaration515 = frozenset([3])
    FOLLOW_ENUM_in_typeDeclaration548 = frozenset([2])
    FOLLOW_modifierList_in_typeDeclaration574 = frozenset([164])
    FOLLOW_IDENT_in_typeDeclaration590 = frozenset([125, 140])
    FOLLOW_implementsClause_in_typeDeclaration607 = frozenset([125, 140])
    FOLLOW_enumTopLevelScope_in_typeDeclaration623 = frozenset([3])
    FOLLOW_AT_in_typeDeclaration656 = frozenset([2])
    FOLLOW_modifierList_in_typeDeclaration682 = frozenset([164])
    FOLLOW_IDENT_in_typeDeclaration698 = frozenset([111])
    FOLLOW_annotationTopLevelScope_in_typeDeclaration712 = frozenset([3])
    FOLLOW_EXTENDS_CLAUSE_in_extendsClause768 = frozenset([2])
    FOLLOW_type_in_extendsClause773 = frozenset([3, 157])
    FOLLOW_IMPLEMENTS_CLAUSE_in_implementsClause812 = frozenset([2])
    FOLLOW_type_in_implementsClause817 = frozenset([3, 157])
    FOLLOW_GENERIC_TYPE_PARAM_LIST_in_genericTypeParameterList842 = frozenset([2])
    FOLLOW_genericTypeParameter_in_genericTypeParameterList844 = frozenset([3, 164])
    FOLLOW_IDENT_in_genericTypeParameter866 = frozenset([2])
    FOLLOW_bound_in_genericTypeParameter868 = frozenset([3])
    FOLLOW_EXTENDS_BOUND_LIST_in_bound890 = frozenset([2])
    FOLLOW_type_in_bound892 = frozenset([3, 157])
    FOLLOW_ENUM_TOP_LEVEL_SCOPE_in_enumTopLevelScope914 = frozenset([2])
    FOLLOW_enumConstant_in_enumTopLevelScope916 = frozenset([3, 123, 128, 138, 140, 164])
    FOLLOW_classTopLevelScope_in_enumTopLevelScope919 = frozenset([3])
    FOLLOW_IDENT_in_enumConstant952 = frozenset([2])
    FOLLOW_annotationList_in_enumConstant967 = frozenset([3, 112, 123, 128, 138, 140])
    FOLLOW_arguments_in_enumConstant985 = frozenset([3, 123, 128, 138, 140])
    FOLLOW_classTopLevelScope_in_enumConstant1001 = frozenset([3])
    FOLLOW_CLASS_TOP_LEVEL_SCOPE_in_classTopLevelScope1043 = frozenset([2])
    FOLLOW_classScopeDeclarations_in_classTopLevelScope1045 = frozenset([3, 7, 61, 67, 77, 121, 122, 124, 136, 160, 163])
    FOLLOW_CLASS_INSTANCE_INITIALIZER_in_classScopeDeclarations1087 = frozenset([2])
    FOLLOW_block_in_classScopeDeclarations1089 = frozenset([3])
    FOLLOW_CLASS_STATIC_INITIALIZER_in_classScopeDeclarations1101 = frozenset([2])
    FOLLOW_block_in_classScopeDeclarations1103 = frozenset([3])
    FOLLOW_FUNCTION_METHOD_DECL_in_classScopeDeclarations1115 = frozenset([2])
    FOLLOW_modifierList_in_classScopeDeclarations1141 = frozenset([3, 138, 157])
    FOLLOW_genericTypeParameterList_in_classScopeDeclarations1155 = frozenset([3, 157])
    FOLLOW_type_in_classScopeDeclarations1170 = frozenset([164])
    FOLLOW_IDENT_in_classScopeDeclarations1186 = frozenset([133])
    FOLLOW_formalParameterList_in_classScopeDeclarations1202 = frozenset([3, 114, 117, 156])
    FOLLOW_arrayDeclaratorList_in_classScopeDeclarations1216 = frozenset([3, 117, 156])
    FOLLOW_throwsClause_in_classScopeDeclarations1229 = frozenset([3, 117])
    FOLLOW_block_in_classScopeDeclarations1242 = frozenset([3])
    FOLLOW_VOID_METHOD_DECL_in_classScopeDeclarations1276 = frozenset([2])
    FOLLOW_modifierList_in_classScopeDeclarations1302 = frozenset([138, 164])
    FOLLOW_genericTypeParameterList_in_classScopeDeclarations1316 = frozenset([164])
    FOLLOW_IDENT_in_classScopeDeclarations1331 = frozenset([133])
    FOLLOW_formalParameterList_in_classScopeDeclarations1347 = frozenset([3, 117, 156])
    FOLLOW_throwsClause_in_classScopeDeclarations1361 = frozenset([3, 117])
    FOLLOW_block_in_classScopeDeclarations1374 = frozenset([3])
    FOLLOW_VAR_DECLARATION_in_classScopeDeclarations1409 = frozenset([2])
    FOLLOW_modifierList_in_classScopeDeclarations1423 = frozenset([3, 157])
    FOLLOW_type_in_classScopeDeclarations1437 = frozenset([162])
    FOLLOW_variableDeclaratorList_in_classScopeDeclarations1451 = frozenset([3])
    FOLLOW_CONSTRUCTOR_DECL_in_classScopeDeclarations1484 = frozenset([2])
    FOLLOW_modifierList_in_classScopeDeclarations1510 = frozenset([133, 138])
    FOLLOW_genericTypeParameterList_in_classScopeDeclarations1524 = frozenset([133])
    FOLLOW_formalParameterList_in_classScopeDeclarations1539 = frozenset([117, 156])
    FOLLOW_throwsClause_in_classScopeDeclarations1553 = frozenset([117])
    FOLLOW_block_in_classScopeDeclarations1566 = frozenset([3])
    FOLLOW_typeDeclaration_in_classScopeDeclarations1598 = frozenset([1])
    FOLLOW_INTERFACE_TOP_LEVEL_SCOPE_in_interfaceTopLevelScope1619 = frozenset([2])
    FOLLOW_interfaceScopeDeclarations_in_interfaceTopLevelScope1621 = frozenset([3, 7, 61, 67, 77, 136, 160, 163])
    FOLLOW_FUNCTION_METHOD_DECL_in_interfaceScopeDeclarations1644 = frozenset([2])
    FOLLOW_modifierList_in_interfaceScopeDeclarations1670 = frozenset([3, 138, 157])
    FOLLOW_genericTypeParameterList_in_interfaceScopeDeclarations1684 = frozenset([3, 157])
    FOLLOW_type_in_interfaceScopeDeclarations1699 = frozenset([164])
    FOLLOW_IDENT_in_interfaceScopeDeclarations1715 = frozenset([133])
    FOLLOW_formalParameterList_in_interfaceScopeDeclarations1731 = frozenset([3, 114, 156])
    FOLLOW_arrayDeclaratorList_in_interfaceScopeDeclarations1745 = frozenset([3, 156])
    FOLLOW_throwsClause_in_interfaceScopeDeclarations1758 = frozenset([3])
    FOLLOW_VOID_METHOD_DECL_in_interfaceScopeDeclarations1792 = frozenset([2])
    FOLLOW_modifierList_in_interfaceScopeDeclarations1818 = frozenset([138, 164])
    FOLLOW_genericTypeParameterList_in_interfaceScopeDeclarations1832 = frozenset([164])
    FOLLOW_IDENT_in_interfaceScopeDeclarations1847 = frozenset([133])
    FOLLOW_formalParameterList_in_interfaceScopeDeclarations1863 = frozenset([3, 156])
    FOLLOW_throwsClause_in_interfaceScopeDeclarations1877 = frozenset([3])
    FOLLOW_VAR_DECLARATION_in_interfaceScopeDeclarations1911 = frozenset([2])
    FOLLOW_modifierList_in_interfaceScopeDeclarations1925 = frozenset([3, 157])
    FOLLOW_type_in_interfaceScopeDeclarations1939 = frozenset([162])
    FOLLOW_variableDeclaratorList_in_interfaceScopeDeclarations1953 = frozenset([3])
    FOLLOW_typeDeclaration_in_interfaceScopeDeclarations1985 = frozenset([1])
    FOLLOW_VAR_DECLARATOR_LIST_in_variableDeclaratorList2018 = frozenset([2])
    FOLLOW_variableDeclarator_in_variableDeclaratorList2023 = frozenset([3, 161])
    FOLLOW_VAR_DECLARATOR_in_variableDeclarator2054 = frozenset([2])
    FOLLOW_variableDeclaratorId_in_variableDeclarator2069 = frozenset([3, 116, 126])
    FOLLOW_variableInitializer_in_variableDeclarator2098 = frozenset([3])
    FOLLOW_IDENT_in_variableDeclaratorId2157 = frozenset([2])
    FOLLOW_arrayDeclaratorList_in_variableDeclaratorId2183 = frozenset([3])
    FOLLOW_arrayInitializer_in_variableInitializer2223 = frozenset([1])
    FOLLOW_expression_in_variableInitializer2237 = frozenset([1])
    FOLLOW_LBRACK_in_arrayDeclarator2265 = frozenset([41])
    FOLLOW_RBRACK_in_arrayDeclarator2267 = frozenset([1])
    FOLLOW_ARRAY_DECLARATOR_LIST_in_arrayDeclaratorList2301 = frozenset([2])
    FOLLOW_ARRAY_DECLARATOR_in_arrayDeclaratorList2304 = frozenset([3, 113])
    FOLLOW_ARRAY_INITIALIZER_in_arrayInitializer2343 = frozenset([2])
    FOLLOW_variableInitializer_in_arrayInitializer2360 = frozenset([3, 116, 126])
    FOLLOW_THROWS_CLAUSE_in_throwsClause2420 = frozenset([2])
    FOLLOW_qualifiedIdentifier_in_throwsClause2422 = frozenset([3, 15, 164])
    FOLLOW_MODIFIER_LIST_in_modifierList2458 = frozenset([2])
    FOLLOW_modifier_in_modifierList2463 = frozenset([3, 7, 53, 70, 81, 85, 86, 87, 90, 91, 94, 98, 102])
    FOLLOW_PUBLIC_in_modifier2501 = frozenset([1])
    FOLLOW_PROTECTED_in_modifier2524 = frozenset([1])
    FOLLOW_PRIVATE_in_modifier2544 = frozenset([1])
    FOLLOW_STATIC_in_modifier2566 = frozenset([1])
    FOLLOW_ABSTRACT_in_modifier2589 = frozenset([1])
    FOLLOW_NATIVE_in_modifier2610 = frozenset([1])
    FOLLOW_SYNCHRONIZED_in_modifier2633 = frozenset([1])
    FOLLOW_TRANSIENT_in_modifier2650 = frozenset([1])
    FOLLOW_VOLATILE_in_modifier2670 = frozenset([1])
    FOLLOW_STRICTFP_in_modifier2691 = frozenset([1])
    FOLLOW_localModifier_in_modifier2714 = frozenset([1])
    FOLLOW_LOCAL_MODIFIER_LIST_in_localModifierList2750 = frozenset([2])
    FOLLOW_localModifier_in_localModifierList2755 = frozenset([3, 7, 53, 70, 81, 85, 86, 87, 90, 91, 94, 98, 102])
    FOLLOW_FINAL_in_localModifier2784 = frozenset([1])
    FOLLOW_annotation_in_localModifier2798 = frozenset([1])
    FOLLOW_TYPE_in_type2834 = frozenset([2])
    FOLLOW_primitiveType_in_type2849 = frozenset([3, 114])
    FOLLOW_qualifiedTypeIdent_in_type2873 = frozenset([3, 114])
    FOLLOW_arrayDeclaratorList_in_type2890 = frozenset([3])
    FOLLOW_QUALIFIED_TYPE_IDENT_in_qualifiedTypeIdent2933 = frozenset([2])
    FOLLOW_typeIdent_in_qualifiedTypeIdent2938 = frozenset([3, 164])
    FOLLOW_IDENT_in_typeIdent2970 = frozenset([2])
    FOLLOW_genericTypeArgumentList_in_typeIdent2972 = frozenset([3])
    FOLLOW_set_in_primitiveType0 = frozenset([1])
    FOLLOW_GENERIC_TYPE_ARG_LIST_in_genericTypeArgumentList3100 = frozenset([2])
    FOLLOW_genericTypeArgument_in_genericTypeArgumentList3102 = frozenset([3, 40, 157])
    FOLLOW_type_in_genericTypeArgument3123 = frozenset([1])
    FOLLOW_QUESTION_in_genericTypeArgument3134 = frozenset([2])
    FOLLOW_genericWildcardBoundType_in_genericTypeArgument3136 = frozenset([3])
    FOLLOW_EXTENDS_in_genericWildcardBoundType3158 = frozenset([2])
    FOLLOW_type_in_genericWildcardBoundType3160 = frozenset([3])
    FOLLOW_SUPER_in_genericWildcardBoundType3172 = frozenset([2])
    FOLLOW_type_in_genericWildcardBoundType3174 = frozenset([3])
    FOLLOW_FORMAL_PARAM_LIST_in_formalParameterList3208 = frozenset([2])
    FOLLOW_formalParameterStandardDecl_in_formalParameterList3223 = frozenset([3, 134, 135])
    FOLLOW_formalParameterVarargDecl_in_formalParameterList3242 = frozenset([3])
    FOLLOW_FORMAL_PARAM_STD_DECL_in_formalParameterStandardDecl3282 = frozenset([2])
    FOLLOW_localModifierList_in_formalParameterStandardDecl3296 = frozenset([3, 157])
    FOLLOW_type_in_formalParameterStandardDecl3310 = frozenset([164])
    FOLLOW_variableDeclaratorId_in_formalParameterStandardDecl3324 = frozenset([3])
    FOLLOW_FORMAL_PARAM_VARARG_DECL_in_formalParameterVarargDecl3360 = frozenset([2])
    FOLLOW_localModifierList_in_formalParameterVarargDecl3374 = frozenset([3, 157])
    FOLLOW_type_in_formalParameterVarargDecl3388 = frozenset([164])
    FOLLOW_variableDeclaratorId_in_formalParameterVarargDecl3402 = frozenset([3])
    FOLLOW_IDENT_in_qualifiedIdentifier3437 = frozenset([1])
    FOLLOW_DOT_in_qualifiedIdentifier3458 = frozenset([2])
    FOLLOW_qualifiedIdentifier_in_qualifiedIdentifier3472 = frozenset([164])
    FOLLOW_IDENT_in_qualifiedIdentifier3484 = frozenset([3])
    FOLLOW_ANNOTATION_LIST_in_annotationList3539 = frozenset([2])
    FOLLOW_annotation_in_annotationList3544 = frozenset([3, 7, 53, 70, 81, 85, 86, 87, 90, 91, 94, 98, 102])
    FOLLOW_AT_in_annotation3582 = frozenset([2])
    FOLLOW_qualifiedIdentifier_in_annotation3596 = frozenset([3, 105])
    FOLLOW_annotationInit_in_annotation3613 = frozenset([3])
    FOLLOW_ANNOTATION_INIT_BLOCK_in_annotationInit3682 = frozenset([2])
    FOLLOW_annotationInitializers_in_annotationInit3686 = frozenset([3])
    FOLLOW_ANNOTATION_INIT_KEY_LIST_in_annotationInitializers3722 = frozenset([2])
    FOLLOW_annotationInitializer_in_annotationInitializers3737 = frozenset([3, 164])
    FOLLOW_ANNOTATION_INIT_DEFAULT_KEY_in_annotationInitializers3762 = frozenset([2])
    FOLLOW_annotationElementValue_in_annotationInitializers3764 = frozenset([3])
    FOLLOW_IDENT_in_annotationInitializer3791 = frozenset([2])
    FOLLOW_annotationElementValue_in_annotationInitializer3795 = frozenset([3])
    FOLLOW_ANNOTATION_INIT_ARRAY_ELEMENT_in_annotationElementValue3832 = frozenset([2])
    FOLLOW_annotationElementValue_in_annotationElementValue3834 = frozenset([3, 7, 53, 70, 81, 85, 86, 87, 90, 91, 94, 98, 102, 104, 116, 126])
    FOLLOW_annotation_in_annotationElementValue3849 = frozenset([1])
    FOLLOW_expression_in_annotationElementValue3865 = frozenset([1])
    FOLLOW_ANNOTATION_TOP_LEVEL_SCOPE_in_annotationTopLevelScope3888 = frozenset([2])
    FOLLOW_annotationScopeDeclarations_in_annotationTopLevelScope3903 = frozenset([3, 7, 61, 67, 77, 109, 160])
    FOLLOW_ANNOTATION_METHOD_DECL_in_annotationScopeDeclarations3944 = frozenset([2])
    FOLLOW_modifierList_in_annotationScopeDeclarations3958 = frozenset([3, 157])
    FOLLOW_type_in_annotationScopeDeclarations3972 = frozenset([164])
    FOLLOW_IDENT_in_annotationScopeDeclarations3986 = frozenset([3, 63])
    FOLLOW_annotationDefaultValue_in_annotationScopeDeclarations4001 = frozenset([3])
    FOLLOW_VAR_DECLARATION_in_annotationScopeDeclarations4038 = frozenset([2])
    FOLLOW_modifierList_in_annotationScopeDeclarations4042 = frozenset([3, 157])
    FOLLOW_type_in_annotationScopeDeclarations4046 = frozenset([162])
    FOLLOW_variableDeclaratorList_in_annotationScopeDeclarations4050 = frozenset([3])
    FOLLOW_typeDeclaration_in_annotationScopeDeclarations4075 = frozenset([1])
    FOLLOW_DEFAULT_in_annotationDefaultValue4100 = frozenset([2])
    FOLLOW_annotationElementValue_in_annotationDefaultValue4104 = frozenset([3])
    FOLLOW_BLOCK_SCOPE_in_block4136 = frozenset([2])
    FOLLOW_blockStatement_in_block4138 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_localVariableDeclaration_in_blockStatement4159 = frozenset([1])
    FOLLOW_typeDeclaration_in_blockStatement4169 = frozenset([1])
    FOLLOW_statement_in_blockStatement4181 = frozenset([1])
    FOLLOW_VAR_DECLARATION_in_localVariableDeclaration4203 = frozenset([2])
    FOLLOW_localModifierList_in_localVariableDeclaration4207 = frozenset([3, 157])
    FOLLOW_type_in_localVariableDeclaration4211 = frozenset([162])
    FOLLOW_variableDeclaratorList_in_localVariableDeclaration4215 = frozenset([3])
    FOLLOW_block_in_statement4270 = frozenset([1])
    FOLLOW_ASSERT_in_statement4281 = frozenset([2])
    FOLLOW_expression_in_statement4296 = frozenset([3, 116, 126])
    FOLLOW_expression_in_statement4314 = frozenset([3])
    FOLLOW_IF_in_statement4339 = frozenset([2])
    FOLLOW_parenthesizedExpression_in_statement4353 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_statement_in_statement4367 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_statement_in_statement4384 = frozenset([3])
    FOLLOW_FOR_in_statement4409 = frozenset([2])
    FOLLOW_forInit_in_statement4423 = frozenset([129])
    FOLLOW_forCondition_in_statement4437 = frozenset([132])
    FOLLOW_forUpdater_in_statement4451 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_statement_in_statement4475 = frozenset([3])
    FOLLOW_FOR_EACH_in_statement4508 = frozenset([2])
    FOLLOW_localModifierList_in_statement4532 = frozenset([3, 157])
    FOLLOW_type_in_statement4544 = frozenset([164])
    FOLLOW_IDENT_in_statement4558 = frozenset([116, 126])
    FOLLOW_expression_in_statement4572 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_statement_in_statement4598 = frozenset([3])
    FOLLOW_WHILE_in_statement4633 = frozenset([2])
    FOLLOW_parenthesizedExpression_in_statement4647 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_statement_in_statement4671 = frozenset([3])
    FOLLOW_DO_in_statement4704 = frozenset([2])
    FOLLOW_statement_in_statement4728 = frozenset([146])
    FOLLOW_parenthesizedExpression_in_statement4742 = frozenset([3])
    FOLLOW_TRY_in_statement4775 = frozenset([2])
    FOLLOW_block_in_statement4797 = frozenset([3, 117, 119])
    FOLLOW_catches_in_statement4819 = frozenset([3, 117])
    FOLLOW_block_in_statement4834 = frozenset([3])
    FOLLOW_SWITCH_in_statement4859 = frozenset([2])
    FOLLOW_parenthesizedExpression_in_statement4874 = frozenset([154])
    FOLLOW_switchBlockLabels_in_statement4889 = frozenset([3])
    FOLLOW_SYNCHRONIZED_in_statement4922 = frozenset([2])
    FOLLOW_parenthesizedExpression_in_statement4949 = frozenset([117])
    FOLLOW_block_in_statement4964 = frozenset([3])
    FOLLOW_RETURN_in_statement4998 = frozenset([2])
    FOLLOW_expression_in_statement5025 = frozenset([3])
    FOLLOW_THROW_in_statement5062 = frozenset([2])
    FOLLOW_expression_in_statement5066 = frozenset([3])
    FOLLOW_BREAK_in_statement5080 = frozenset([2])
    FOLLOW_IDENT_in_statement5085 = frozenset([3])
    FOLLOW_CONTINUE_in_statement5104 = frozenset([2])
    FOLLOW_IDENT_in_statement5109 = frozenset([3])
    FOLLOW_LABELED_STATEMENT_in_statement5127 = frozenset([2])
    FOLLOW_IDENT_in_statement5131 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_statement_in_statement5135 = frozenset([3])
    FOLLOW_expression_in_statement5150 = frozenset([1])
    FOLLOW_SEMI_in_statement5162 = frozenset([1])
    FOLLOW_CATCH_CLAUSE_LIST_in_catches5183 = frozenset([2])
    FOLLOW_catchClause_in_catches5185 = frozenset([3, 59])
    FOLLOW_CATCH_in_catchClause5207 = frozenset([2])
    FOLLOW_formalParameterStandardDecl_in_catchClause5221 = frozenset([117])
    FOLLOW_block_in_catchClause5235 = frozenset([3])
    FOLLOW_SWITCH_BLOCK_LABEL_LIST_in_switchBlockLabels5269 = frozenset([2])
    FOLLOW_switchCaseLabel_in_switchBlockLabels5271 = frozenset([3, 58, 63])
    FOLLOW_switchDefaultLabel_in_switchBlockLabels5274 = frozenset([3])
    FOLLOW_CASE_in_switchCaseLabel5296 = frozenset([2])
    FOLLOW_expression_in_switchCaseLabel5312 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_blockStatement_in_switchCaseLabel5328 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_DEFAULT_in_switchDefaultLabel5369 = frozenset([2])
    FOLLOW_blockStatement_in_switchDefaultLabel5393 = frozenset([3, 7, 44, 54, 56, 61, 62, 64, 67, 73, 74, 77, 88, 93, 94, 96, 100, 103, 116, 117, 126, 130, 141, 160])
    FOLLOW_FOR_INIT_in_forInit5447 = frozenset([2])
    FOLLOW_localVariableDeclaration_in_forInit5461 = frozenset([3])
    FOLLOW_expression_in_forInit5478 = frozenset([3, 116, 126])
    FOLLOW_FOR_CONDITION_in_forCondition5527 = frozenset([2])
    FOLLOW_expression_in_forCondition5531 = frozenset([3])
    FOLLOW_FOR_UPDATE_in_forUpdater5569 = frozenset([2])
    FOLLOW_expression_in_forUpdater5574 = frozenset([3, 116, 126])
    FOLLOW_PARENTESIZED_EXPR_in_parenthesizedExpression5603 = frozenset([2])
    FOLLOW_expression_in_parenthesizedExpression5607 = frozenset([3])
    FOLLOW_EXPR_in_expression5634 = frozenset([2])
    FOLLOW_expr_in_expression5638 = frozenset([3])
    FOLLOW_ASSIGN_in_expr5674 = frozenset([2])
    FOLLOW_expr_in_expr5678 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5682 = frozenset([3])
    FOLLOW_PLUS_ASSIGN_in_expr5702 = frozenset([2])
    FOLLOW_expr_in_expr5706 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5710 = frozenset([3])
    FOLLOW_MINUS_ASSIGN_in_expr5725 = frozenset([2])
    FOLLOW_expr_in_expr5729 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5733 = frozenset([3])
    FOLLOW_STAR_ASSIGN_in_expr5747 = frozenset([2])
    FOLLOW_expr_in_expr5751 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5755 = frozenset([3])
    FOLLOW_DIV_ASSIGN_in_expr5770 = frozenset([2])
    FOLLOW_expr_in_expr5774 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5778 = frozenset([3])
    FOLLOW_AND_ASSIGN_in_expr5794 = frozenset([2])
    FOLLOW_expr_in_expr5798 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5802 = frozenset([3])
    FOLLOW_OR_ASSIGN_in_expr5818 = frozenset([2])
    FOLLOW_expr_in_expr5822 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5826 = frozenset([3])
    FOLLOW_XOR_ASSIGN_in_expr5843 = frozenset([2])
    FOLLOW_expr_in_expr5847 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5851 = frozenset([3])
    FOLLOW_MOD_ASSIGN_in_expr5867 = frozenset([2])
    FOLLOW_expr_in_expr5871 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5875 = frozenset([3])
    FOLLOW_BIT_SHIFT_RIGHT_ASSIGN_in_expr5891 = frozenset([2])
    FOLLOW_expr_in_expr5893 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5895 = frozenset([3])
    FOLLOW_SHIFT_RIGHT_ASSIGN_in_expr5907 = frozenset([2])
    FOLLOW_expr_in_expr5909 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5911 = frozenset([3])
    FOLLOW_SHIFT_LEFT_ASSIGN_in_expr5923 = frozenset([2])
    FOLLOW_expr_in_expr5925 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5927 = frozenset([3])
    FOLLOW_QUESTION_in_expr5939 = frozenset([2])
    FOLLOW_expr_in_expr5943 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5947 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5951 = frozenset([3])
    FOLLOW_LOGICAL_OR_in_expr5975 = frozenset([2])
    FOLLOW_expr_in_expr5979 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr5983 = frozenset([3])
    FOLLOW_LOGICAL_AND_in_expr6003 = frozenset([2])
    FOLLOW_expr_in_expr6007 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6011 = frozenset([3])
    FOLLOW_OR_in_expr6030 = frozenset([2])
    FOLLOW_expr_in_expr6034 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6038 = frozenset([3])
    FOLLOW_XOR_in_expr6066 = frozenset([2])
    FOLLOW_expr_in_expr6070 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6074 = frozenset([3])
    FOLLOW_AND_in_expr6101 = frozenset([2])
    FOLLOW_expr_in_expr6105 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6109 = frozenset([3])
    FOLLOW_EQUAL_in_expr6136 = frozenset([2])
    FOLLOW_expr_in_expr6140 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6144 = frozenset([3])
    FOLLOW_NOT_EQUAL_in_expr6169 = frozenset([2])
    FOLLOW_expr_in_expr6173 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6177 = frozenset([3])
    FOLLOW_INSTANCEOF_in_expr6198 = frozenset([2])
    FOLLOW_expr_in_expr6202 = frozenset([3, 157])
    FOLLOW_type_in_expr6206 = frozenset([3])
    FOLLOW_LESS_OR_EQUAL_in_expr6230 = frozenset([2])
    FOLLOW_expr_in_expr6234 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6238 = frozenset([3])
    FOLLOW_GREATER_OR_EQUAL_in_expr6255 = frozenset([2])
    FOLLOW_expr_in_expr6259 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6263 = frozenset([3])
    FOLLOW_BIT_SHIFT_RIGHT_in_expr6277 = frozenset([2])
    FOLLOW_expr_in_expr6281 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6285 = frozenset([3])
    FOLLOW_SHIFT_RIGHT_in_expr6345 = frozenset([2])
    FOLLOW_expr_in_expr6349 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6353 = frozenset([3])
    FOLLOW_GREATER_THAN_in_expr6372 = frozenset([2])
    FOLLOW_expr_in_expr6376 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6380 = frozenset([3])
    FOLLOW_SHIFT_LEFT_in_expr6398 = frozenset([2])
    FOLLOW_expr_in_expr6402 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6406 = frozenset([3])
    FOLLOW_LESS_THAN_in_expr6426 = frozenset([2])
    FOLLOW_expr_in_expr6430 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6434 = frozenset([3])
    FOLLOW_PLUS_in_expr6455 = frozenset([2])
    FOLLOW_expr_in_expr6459 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6463 = frozenset([3])
    FOLLOW_MINUS_in_expr6489 = frozenset([2])
    FOLLOW_expr_in_expr6493 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6497 = frozenset([3])
    FOLLOW_STAR_in_expr6522 = frozenset([2])
    FOLLOW_expr_in_expr6526 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6530 = frozenset([3])
    FOLLOW_DIV_in_expr6556 = frozenset([2])
    FOLLOW_expr_in_expr6560 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6564 = frozenset([3])
    FOLLOW_MOD_in_expr6591 = frozenset([2])
    FOLLOW_expr_in_expr6595 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6599 = frozenset([3])
    FOLLOW_UNARY_PLUS_in_expr6626 = frozenset([2])
    FOLLOW_expr_in_expr6630 = frozenset([3])
    FOLLOW_UNARY_MINUS_in_expr6659 = frozenset([2])
    FOLLOW_expr_in_expr6663 = frozenset([3])
    FOLLOW_PRE_INC_in_expr6691 = frozenset([2])
    FOLLOW_expr_in_expr6695 = frozenset([3])
    FOLLOW_PRE_DEC_in_expr6727 = frozenset([2])
    FOLLOW_expr_in_expr6731 = frozenset([3])
    FOLLOW_POST_INC_in_expr6763 = frozenset([2])
    FOLLOW_expr_in_expr6767 = frozenset([3])
    FOLLOW_POST_DEC_in_expr6798 = frozenset([2])
    FOLLOW_expr_in_expr6802 = frozenset([3])
    FOLLOW_NOT_in_expr6833 = frozenset([2])
    FOLLOW_expr_in_expr6837 = frozenset([3])
    FOLLOW_LOGICAL_NOT_in_expr6873 = frozenset([2])
    FOLLOW_expr_in_expr6877 = frozenset([3])
    FOLLOW_CAST_EXPR_in_expr6905 = frozenset([2])
    FOLLOW_type_in_expr6909 = frozenset([4, 5, 6, 8, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 69, 76, 83, 92, 95, 99, 113, 115, 118, 120, 144, 146, 147, 148, 149, 150, 152, 153, 155, 158, 159, 164, 165, 166, 167, 168, 169, 170])
    FOLLOW_expr_in_expr6913 = frozenset([3])
    FOLLOW_primaryExpression_in_expr6935 = frozenset([1])
    FOLLOW_DOT_in_primaryExpression6980 = frozenset([2])
    FOLLOW_primaryExpression_in_primaryExpression7000 = frozenset([61, 92, 95, 120, 164])
    FOLLOW_IDENT_in_primaryExpression7040 = frozenset([3])
    FOLLOW_THIS_in_primaryExpression7084 = frozenset([3])
    FOLLOW_SUPER_in_primaryExpression7110 = frozenset([3])
    FOLLOW_innerNewExpression_in_primaryExpression7150 = frozenset([3])
    FOLLOW_CLASS_in_primaryExpression7174 = frozenset([3])
    FOLLOW_primitiveType_in_primaryExpression7214 = frozenset([61])
    FOLLOW_CLASS_in_primaryExpression7216 = frozenset([3])
    FOLLOW_VOID_in_primaryExpression7236 = frozenset([61])
    FOLLOW_CLASS_in_primaryExpression7238 = frozenset([3])
    FOLLOW_parenthesizedExpression_in_primaryExpression7275 = frozenset([1])
    FOLLOW_IDENT_in_primaryExpression7287 = frozenset([1])
    FOLLOW_METHOD_CALL_in_primaryExpression7300 = frozenset([2])
    FOLLOW_primaryExpression_in_primaryExpression7314 = frozenset([112, 137])
    FOLLOW_genericTypeArgumentList_in_primaryExpression7326 = frozenset([112])
    FOLLOW_arguments_in_primaryExpression7341 = frozenset([3])
    FOLLOW_explicitConstructorCall_in_primaryExpression7375 = frozenset([1])
    FOLLOW_ARRAY_ELEMENT_ACCESS_in_primaryExpression7388 = frozenset([2])
    FOLLOW_primaryExpression_in_primaryExpression7402 = frozenset([116, 126])
    FOLLOW_expression_in_primaryExpression7416 = frozenset([3])
    FOLLOW_literal_in_primaryExpression7448 = frozenset([1])
    FOLLOW_newExpression_in_primaryExpression7460 = frozenset([1])
    FOLLOW_THIS_in_primaryExpression7472 = frozenset([1])
    FOLLOW_arrayTypeDeclarator_in_primaryExpression7484 = frozenset([1])
    FOLLOW_SUPER_in_primaryExpression7494 = frozenset([1])
    FOLLOW_THIS_CONSTRUCTOR_CALL_in_explicitConstructorCall7529 = frozenset([2])
    FOLLOW_genericTypeArgumentList_in_explicitConstructorCall7531 = frozenset([112])
    FOLLOW_arguments_in_explicitConstructorCall7534 = frozenset([3])
    FOLLOW_SUPER_CONSTRUCTOR_CALL_in_explicitConstructorCall7546 = frozenset([2])
    FOLLOW_primaryExpression_in_explicitConstructorCall7563 = frozenset([112, 137])
    FOLLOW_genericTypeArgumentList_in_explicitConstructorCall7579 = frozenset([112])
    FOLLOW_arguments_in_explicitConstructorCall7597 = frozenset([3])
    FOLLOW_ARRAY_DECLARATOR_in_arrayTypeDeclarator7656 = frozenset([2])
    FOLLOW_arrayTypeDeclarator_in_arrayTypeDeclarator7659 = frozenset([3])
    FOLLOW_qualifiedIdentifier_in_arrayTypeDeclarator7663 = frozenset([3])
    FOLLOW_primitiveType_in_arrayTypeDeclarator7667 = frozenset([3])
    FOLLOW_STATIC_ARRAY_CREATOR_in_newExpression7693 = frozenset([2])
    FOLLOW_primitiveType_in_newExpression7709 = frozenset([114, 116, 126])
    FOLLOW_newArrayConstruction_in_newExpression7713 = frozenset([3])
    FOLLOW_genericTypeArgumentList_in_newExpression7743 = frozenset([151])
    FOLLOW_qualifiedTypeIdent_in_newExpression7748 = frozenset([114, 116, 126])
    FOLLOW_newArrayConstruction_in_newExpression7752 = frozenset([3])
    FOLLOW_CLASS_CONSTRUCTOR_CALL_in_newExpression7799 = frozenset([2])
    FOLLOW_genericTypeArgumentList_in_newExpression7811 = frozenset([151])
    FOLLOW_qualifiedTypeIdent_in_newExpression7826 = frozenset([112])
    FOLLOW_arguments_in_newExpression7840 = frozenset([3, 123, 128, 138, 140])
    FOLLOW_classTopLevelScope_in_newExpression7852 = frozenset([3])
    FOLLOW_CLASS_CONSTRUCTOR_CALL_in_innerNewExpression7900 = frozenset([2])
    FOLLOW_genericTypeArgumentList_in_innerNewExpression7912 = frozenset([164])
    FOLLOW_IDENT_in_innerNewExpression7927 = frozenset([112])
    FOLLOW_arguments_in_innerNewExpression7941 = frozenset([3, 123, 128, 138, 140])
    FOLLOW_classTopLevelScope_in_innerNewExpression7953 = frozenset([3])
    FOLLOW_arrayDeclaratorList_in_newArrayConstruction8010 = frozenset([116])
    FOLLOW_arrayInitializer_in_newArrayConstruction8014 = frozenset([1])
    FOLLOW_expression_in_newArrayConstruction8037 = frozenset([1, 114, 116, 126])
    FOLLOW_arrayDeclaratorList_in_newArrayConstruction8059 = frozenset([1])
    FOLLOW_ARGUMENT_LIST_in_arguments8093 = frozenset([2])
    FOLLOW_expression_in_arguments8098 = frozenset([3, 116, 126])
    FOLLOW_HEX_LITERAL_in_literal8145 = frozenset([1])
    FOLLOW_OCTAL_LITERAL_in_literal8168 = frozenset([1])
    FOLLOW_DECIMAL_LITERAL_in_literal8189 = frozenset([1])
    FOLLOW_FLOATING_POINT_LITERAL_in_literal8208 = frozenset([1])
    FOLLOW_CHARACTER_LITERAL_in_literal8220 = frozenset([1])
    FOLLOW_STRING_LITERAL_in_literal8237 = frozenset([1])
    FOLLOW_TRUE_in_literal8257 = frozenset([1])
    FOLLOW_FALSE_in_literal8287 = frozenset([1])
    FOLLOW_NULL_in_literal8316 = frozenset([1])
    FOLLOW_expression_in_synpred131_JavaTreeParser5478 = frozenset([1, 116, 126])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(JavaTreeParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
