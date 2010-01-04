/*
 [The "BSD licence"]
 Copyright (c) 2007-2008 Terence Parr
 All rights reserved.

 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions
 are met:
 1. Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.
 2. Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.
 3. The name of the author may not be used to endorse or promote products
    derived from this software without specific prior written permission.

 THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
 IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
 OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
 IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
 INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
 NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
 THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/
grammar Java;


options {
    backtrack=true;
    memoize=true;
    language=Python;
    output=AST;
}


scope py_block {
    block;
}


scope py_klass {
    klass;
    name;
}


scope py_method {
    method;
}


scope py_mods {
    add;
}


scope py_params {
    add;
}


scope py_args {
    args;
    add;
}


scope py_expr {
    expr;
    add;
}


scope py_types {
    add;
}


@parser::members {
    factory = None
    def setFactory(self, factory):
        self.factory = factory
}


compilationUnit returns [module]
scope py_block;
@init { $module = $py_block::block = self.factory('module') }
    :   annotations
        (   packageDeclaration importDeclaration* typeDeclaration*
        |   classOrInterfaceDeclaration typeDeclaration*
        )
    |   packageDeclaration? importDeclaration* typeDeclaration*
    ;


packageDeclaration
    :   'package' qualifiedName ';'
    ;


importDeclaration
    :   'import' ('static')? qualifiedName ('.' '*')? ';'
    ;


typeDeclaration
scope py_klass, py_mods, py_types;
@init {
    klass = $py_klass::klass = self.factory('class')
    klass.setParent($py_block::block)
    $py_mods::add = klass.addModifier
    $py_types::add = klass.addBase
    }
    :   classOrInterfaceDeclaration
    |   ';'
    ;


classOrInterfaceDeclaration
    :   classOrInterfaceModifiers (classDeclaration | interfaceDeclaration)
    ;


classOrInterfaceModifiers
    :   classOrInterfaceModifier*
    ;


classOrInterfaceModifier
    :   annotation                                // class or interface
    |   'public'     {$py_mods::add('public')}    // class or interface
    |   'protected'  {$py_mods::add('protected')} // class or interface
    |   'private'    {$py_mods::add('private')}   // class or interface
    |   'abstract'   {$py_mods::add('abstract')}  // class or interface
    |   'static'     {$py_mods::add('static')}    // class or interface
    |   'final'      {$py_mods::add('final')}     // class only -- does not apply to interfaces
    |   'strictfp'   {$py_mods::add('strictfp')}  // class or interface
    ;


modifiers
    :   (modifier { $py_mods::add($modifier.text) })*
    ;


classDeclaration
    :   normalClassDeclaration
    |   enumDeclaration
    ;


normalClassDeclaration
    :   'class' Ident { $py_klass::klass.setName($Ident.text) } typeParameters?
        ('extends' type)?
        ('implements' typeList)?
        classBody
    ;


typeParameters
    :   '<' typeParameter (',' typeParameter)* '>'
    ;


typeParameter
    :   Ident ('extends' typeBound)?
    ;


typeBound
    :   type ('&' type)*
    ;


enumDeclaration
    :   ENUM Ident ('implements' typeList)? enumBody
    ;


enumBody
    :   '{' enumConstants? ','? enumBodyDeclarations? '}'
    ;


enumConstants
    :   enumConstant (',' enumConstant)*
    ;


enumConstant
    :   annotations? Ident arguments? classBody?
    ;


enumBodyDeclarations
    :   ';' (classBodyDeclaration)*
    ;


interfaceDeclaration
    :   normalInterfaceDeclaration
    |   annotationTypeDeclaration
    ;


normalInterfaceDeclaration
    :   'interface' Ident typeParameters? ('extends' typeList)? interfaceBody
    ;


typeList
    :   type (',' type)*
    ;


classBody
    :   '{' classBodyDeclaration* '}'
    ;


interfaceBody
    :   '{' interfaceBodyDeclaration* '}'
    ;


classBodyDeclaration
scope py_method, py_mods;
@init {
    $py_method::method = method = self.factory('method')
    $py_mods::add = method.addModifier
}
    :   ';'
    |   'static'? block
    |   modifiers memberDecl
    ;


memberDecl
scope py_params;
    :   genericMethodOrConstructorDecl
    |   memberDeclaration
    |   'void' Ident
        {
            method = $py_method::method
            method.setType('void')
            method.setParent($py_block::block)
            method.setName($Ident.text)
            $py_params::add = method.addParam
        }
        voidMethodDeclaratorRest
    |   Ident constructorDeclaratorRest
    |   interfaceDeclaration
    |   classDeclaration
    ;


memberDeclaration
scope py_types;
@init {
    $py_types::add = $py_method.setType
    }
    :   type (methodDeclaration | fieldDeclaration)
    ;


genericMethodOrConstructorDecl
    :   typeParameters genericMethodOrConstructorRest
    ;


genericMethodOrConstructorRest
    :   (type | 'void') Ident methodDeclaratorRest
    |   Ident constructorDeclaratorRest
    ;


methodDeclaration
    :   Ident methodDeclaratorRest
    ;


fieldDeclaration
    :   variableDeclarators ';'
    ;


interfaceBodyDeclaration
    :   modifiers interfaceMemberDecl
    |   ';'
    ;


interfaceMemberDecl
    :   interfaceMethodOrFieldDecl
    |   interfaceGenericMethodDecl
    |   'void' Ident voidInterfaceMethodDeclaratorRest
    |   interfaceDeclaration
    |   classDeclaration
    ;


interfaceMethodOrFieldDecl
    :   type Ident interfaceMethodOrFieldRest
    ;


interfaceMethodOrFieldRest
    :   constantDeclaratorsRest ';'
    |   interfaceMethodDeclaratorRest
    ;


methodDeclaratorRest
    :   formalParameters ('[' ']')*
        ('throws' qualifiedNameList)?
        (   methodBody
        |   ';'
        )
    ;


voidMethodDeclaratorRest
    :   formalParameters ('throws' qualifiedNameList)?
        (   methodBody
        |   ';'
        )
    ;


interfaceMethodDeclaratorRest
    :   formalParameters ('[' ']')* ('throws' qualifiedNameList)? ';'
    ;


interfaceGenericMethodDecl
    :   typeParameters (type | 'void') Ident
        interfaceMethodDeclaratorRest
    ;


voidInterfaceMethodDeclaratorRest
    :   formalParameters ('throws' qualifiedNameList)? ';'
    ;


constructorDeclaratorRest
    :   formalParameters ('throws' qualifiedNameList)? constructorBody
    ;


constantDeclarator
    :   Ident constantDeclaratorRest
    ;


variableDeclarators
    :   variableDeclarator (',' variableDeclarator)*
    ;


variableDeclarator
    :   variableDeclaratorId ('=' variableInitializer)?
    ;


constantDeclaratorsRest
    :   constantDeclaratorRest (',' constantDeclarator)*
    ;


constantDeclaratorRest
    :   ('[' ']')* '=' variableInitializer
    ;


variableDeclaratorId
    :   Ident ('[' ']')*
    ;


variableInitializer
    :   arrayInitializer
    |   expression
    ;


arrayInitializer
    :   '{' (variableInitializer (',' variableInitializer)* (',')? )? '}'
    ;


modifier
    :   annotation
    |   'public'
    |   'protected'
    |   'private'
    |   'static'
    |   'abstract'
    |   'final'
    |   'native'
    |   'synchronized'
    |   'transient'
    |   'volatile'
    |   'strictfp'
    ;


packageOrTypeName
    :   qualifiedName
    ;


enumConstantName
    :   Ident
    ;


typeName
    :   qualifiedName
    ;


type
    :	classOrInterfaceType ('[' ']')*
    |	primitiveType ('[' ']')* {$py_types::add($primitiveType.text)}
    ;


classOrInterfaceType
@init {
    values = []
}
    :	id0=Ident {values.append(id0.text)} typeArguments?
        ('.' id1=Ident typeArguments? {values.append(id1.text)} )*
        {$py_types::add(values)}
    ;


primitiveType
    :   'boolean'
    |   'char'
    |   'byte'
    |   'short'
    |   'int'
    |   'long'
    |   'float'
    |   'double'
    ;


variableModifier
    :   'final'
    |   annotation
    ;


typeArguments
    :   '<' typeArgument (',' typeArgument)* '>'
    ;


typeArgument
    :   type
    |   '?' (('extends' | 'super') type)?
    ;

qualifiedNameList
    :   qualifiedName (',' qualifiedName)*
    ;


formalParameters
scope py_types;
@init {
    $py_types::add = lambda x:None
}
    :   '(' formalParameterDecls? ')'
    ;


formalParameterDecls
    :   variableModifiers type formalParameterDeclsRest
    ;


formalParameterDeclsRest
    :   variableDeclaratorId
        {$py_params::add($variableDeclaratorId.text)}
        (',' formalParameterDecls)?
    |   '...' variableDeclaratorId
    ;


methodBody
    :   block
    ;


constructorBody
    :   '{' explicitConstructorInvocation? blockStatement* '}'
    ;


explicitConstructorInvocation
    :   nonWildcardTypeArguments? ('this' | 'super') arguments ';'
    |   primary '.' nonWildcardTypeArguments? 'super' arguments ';'
    ;


qualifiedName
    :   Ident ('.' Ident)*
    ;


literal
    :   integerLiteral
    |   FloatingPointLiteral
    |   CharacterLiteral
    |   StringLiteral
    |   booleanLiteral
    |   'null'
    ;


integerLiteral
    :   HexLiteral
    |   OctalLiteral
    |   DecimalLiteral
    ;


booleanLiteral
    :   'true'
    |   'false'
    ;


// ANNOTATIONS


annotations
    :   annotation+
    ;


annotation
    :   '@' annotationName ( '(' ( elementValuePairs | elementValue )? ')' )?
    ;


annotationName
    : Ident ('.' Ident)*
    ;


elementValuePairs
    :   elementValuePair (',' elementValuePair)*
    ;


elementValuePair
    :   Ident '=' elementValue
    ;


elementValue
    :   conditionalExpression
    |   annotation
    |   elementValueArrayInitializer
    ;


elementValueArrayInitializer
    :   '{' (elementValue (',' elementValue)*)? (',')? '}'
    ;


annotationTypeDeclaration
    :   '@' 'interface' Ident annotationTypeBody
    ;


annotationTypeBody
    :   '{' (annotationTypeElementDeclaration)* '}'
    ;


annotationTypeElementDeclaration
    :   modifiers annotationTypeElementRest
    ;


annotationTypeElementRest
    :   type annotationMethodOrConstantRest ';'
    |   normalClassDeclaration ';'?
    |   normalInterfaceDeclaration ';'?
    |   enumDeclaration ';'?
    |   annotationTypeDeclaration ';'?
    ;


annotationMethodOrConstantRest
    :   annotationMethodRest
    |   annotationConstantRest
    ;


annotationMethodRest
    :   Ident '(' ')' defaultValue?
    ;


annotationConstantRest
    :   variableDeclarators
    ;


defaultValue
    :   'default' elementValue
    ;


// STATEMENTS / BLOCKS


block
    :   '{' blockStatement* '}'
    ;


blockStatement
    :   localVariableDeclarationStatement
    |   classOrInterfaceDeclaration
    |   statement
    ;


localVariableDeclarationStatement
    :    localVariableDeclaration ';'
    ;


localVariableDeclaration
    :   variableModifiers type variableDeclarators
    ;


variableModifiers
    :   variableModifier*
    ;


statement
    : block
    |   ASSERT expression (':' expression)? ';'
    |   'if' parExpression statement (options {k=1;}:'else' statement)?
    |   'for' '(' forControl ')' statement
    |   'while' parExpression statement
    |   'do' statement 'while' parExpression ';'
    |   'try' block
        ( catches 'finally' block
        | catches
        |   'finally' block
        )
    |   'switch' parExpression '{' switchBlockStatementGroups '}'
    |   'synchronized' parExpression block
    |   'return' expression? ';'
    |   'throw' expression ';'
    |   'break' Ident? ';'
    |   'continue' Ident? ';'
    |   ';'
    |   statementExpression ';'
    |   Ident ':' statement
    ;


catches
    :   catchClause (catchClause)*
    ;


catchClause
    :   'catch' '(' formalParameter ')' block
    ;


formalParameter
    :   variableModifiers type variableDeclaratorId
    ;


switchBlockStatementGroups
    :   (switchBlockStatementGroup)*
    ;


switchBlockStatementGroup
    :   switchLabel+ blockStatement*
    ;


switchLabel
    :   'case' constantExpression ':'
    |   'case' enumConstantName ':'
    |   'default' ':'
    ;


forControl options {k=3;}
    :   enhancedForControl
    |   forInit? ';' expression? ';' forUpdate?
    ;


forInit
    :   localVariableDeclaration
    |   expressionList
    ;


enhancedForControl
    :   variableModifiers type Ident ':' expression
    ;


forUpdate
    :   expressionList
    ;


// EXPRESSIONS


parExpression
    :   '(' expression ')'
    ;


expressionList
    :   expression (',' expression)*
    ;


statementExpression
    :   expression
    ;


constantExpression
    :   expression
    ;


expression
    :   conditionalExpression (assignmentOperator expression)?
    ;


assignmentOperator
    :   '='
    |   '+='
    |   '-='
    |   '*='
    |   '/='
    |   '&='
    |   '|='
    |   '^='
    |   '%='
    |   ('<' '<' '=')=> t1='<' t2='<' t3='='
        {
          $t1.getLine() == $t2.getLine() and \
          $t1.getCharPositionInLine() + 1 == $t2.getCharPositionInLine() and \
          $t2.getLine() == $t3.getLine() and \
          $t2.getCharPositionInLine() + 1 == $t3.getCharPositionInLine()
        }?
    |   ('>' '>' '>' '=')=> t1='>' t2='>' t3='>' t4='='
        {
          $t1.getLine() == $t2.getLine() and \
          $t1.getCharPositionInLine() + 1 == $t2.getCharPositionInLine() and \
          $t2.getLine() == $t3.getLine() and \
          $t2.getCharPositionInLine() + 1 == $t3.getCharPositionInLine() and \
          $t3.getLine() == $t4.getLine() and \
          $t3.getCharPositionInLine() + 1 == $t4.getCharPositionInLine()
        }?
    |   ('>' '>' '=')=> t1='>' t2='>' t3='='
        {
          $t1.getLine() == $t2.getLine() and \
          $t1.getCharPositionInLine() + 1 == $t2.getCharPositionInLine() and \
          $t2.getLine() == $t3.getLine() and \
          $t2.getCharPositionInLine() + 1 == $t3.getCharPositionInLine()
        }?
    ;


conditionalExpression
    :   conditionalOrExpression ( '?' expression ':' expression )?
    ;


conditionalOrExpression
    :   conditionalAndExpression ( '||' conditionalAndExpression )*
    ;


conditionalAndExpression
    :   inclusiveOrExpression ( '&&' inclusiveOrExpression )*
    ;


inclusiveOrExpression
    :   exclusiveOrExpression ( '|' exclusiveOrExpression )*
    ;


exclusiveOrExpression
    :   andExpression ( '^' andExpression )*
    ;


andExpression
    :   equalityExpression ( '&' equalityExpression )*
    ;


equalityExpression
    :   instanceOfExpression ( ('==' | '!=') instanceOfExpression )*
    ;


instanceOfExpression
    :   relationalExpression ('instanceof' type)?
    ;


relationalExpression
    :   shiftExpression ( relationalOp shiftExpression )*
    ;


relationalOp
    :   ('<' '=')=> t1='<' t2='='
        {
          $t1.getLine() == $t2.getLine() and \
          $t1.getCharPositionInLine() + 1 == $t2.getCharPositionInLine()
        }?
    |   ('>' '=')=> t1='>' t2='='
        {
          $t1.getLine() == $t2.getLine() and \
          $t1.getCharPositionInLine() + 1 == $t2.getCharPositionInLine()
        }?
    |   '<'
    |   '>'
    ;


shiftExpression
    :   additiveExpression ( shiftOp additiveExpression )*
    ;


shiftOp
    :   ('<' '<')=> t1='<' t2='<'
        {
          $t1.getLine() == $t2.getLine() and \
          $t1.getCharPositionInLine() + 1 == $t2.getCharPositionInLine()
        }?
    |   ('>' '>' '>')=> t1='>' t2='>' t3='>'
        {
          $t1.getLine() == $t2.getLine() and \
          $t1.getCharPositionInLine() + 1 == $t2.getCharPositionInLine() and \
          $t2.getLine() == $t3.getLine() and \
          $t2.getCharPositionInLine() + 1 == $t3.getCharPositionInLine()
        }?
    |   ('>' '>')=> t1='>' t2='>'
        {
          $t1.getLine() == $t2.getLine() and \
          $t1.getCharPositionInLine() + 1 == $t2.getCharPositionInLine()
        }?
    ;


additiveExpression
    :   multiplicativeExpression ( ('+' | '-') multiplicativeExpression )*
    ;


multiplicativeExpression
    :   unaryExpression ( ( '*' | '/' | '%' ) unaryExpression )*
    ;


unaryExpression
    :   '+' unaryExpression
    |   '-' unaryExpression
    |   '++' unaryExpression
    |   '--' unaryExpression
    |   unaryExpressionNotPlusMinus
    ;


unaryExpressionNotPlusMinus
    :   '~' unaryExpression
    |   '!' unaryExpression
    |   castExpression
    |   primary selector* ('++'|'--')?
    ;


castExpression
    :  '(' primitiveType ')' unaryExpression
    |  '(' (type | expression) ')' unaryExpressionNotPlusMinus
    ;


primary
scope py_args, py_expr;
@init {
    $py_expr::expr = []
    $py_expr::add = $py_expr::expr.append
    $py_args::args = []
    $py_args::add = $py_args::args.append
}
@after {
    print '####', $py_expr::expr, $py_args::args
}
    :   parExpression
    |   'this' ('.' Ident)* identifierSuffix?
    |   'super' superSuffix
    |   literal {$py_expr::add( $literal.text )}
    |   'new' creator
    |   id0=Ident {$py_expr::add(id0.text)} ('.' id1=Ident {$py_expr::add(id1.text)})* identifierSuffix?
    |   primitiveType ('[' ']')* '.' 'class'
    |   'void' '.' 'class'
    ;


identifierSuffix
    :   ('[' ']')+ '.' 'class'
    |   ('[' expression ']')+ // can also be matched by selector, but do here
    |   arguments {$py_args::add($arguments.text)}
    |   '.' 'class'
    |   '.' explicitGenericInvocation
    |   '.' 'this'
    |   '.' 'super' arguments
    |   '.' 'new' innerCreator
    ;


creator
    :   nonWildcardTypeArguments createdName classCreatorRest
    |   createdName (arrayCreatorRest | classCreatorRest)
    ;


createdName
    :   classOrInterfaceType
    |   primitiveType
    ;


innerCreator
    :   nonWildcardTypeArguments? Ident classCreatorRest
    ;


arrayCreatorRest
    :   '['
        (   ']' ('[' ']')* arrayInitializer
        |   expression ']' ('[' expression ']')* ('[' ']')*
        )
    ;


classCreatorRest
    :   arguments classBody?
    ;


explicitGenericInvocation
    :   nonWildcardTypeArguments Ident  arguments
    ;


nonWildcardTypeArguments
    :   '<' typeList '>'
    ;


selector
    :   '.' Ident arguments?
    |   '.' 'this'
    |   '.' 'super' superSuffix
    |   '.' 'new' innerCreator
    |   '[' expression ']'
    ;


superSuffix
    :   arguments
    |   '.' Ident arguments?
    ;


arguments
    :   '(' expressionList? ')'
    ;


// LEXER


HexLiteral : '0' ('x'|'X') HexDigit+ IntegerTypeSuffix? ;


DecimalLiteral : ('0' | '1'..'9' '0'..'9'*) IntegerTypeSuffix? ;


OctalLiteral : '0' ('0'..'7')+ IntegerTypeSuffix? ;


fragment
HexDigit : ('0'..'9'|'a'..'f'|'A'..'F') ;


fragment
IntegerTypeSuffix : ('l'|'L') ;


FloatingPointLiteral
    :   ('0'..'9')+ '.' ('0'..'9')* Exponent? FloatTypeSuffix?
    |   '.' ('0'..'9')+ Exponent? FloatTypeSuffix?
    |   ('0'..'9')+ Exponent FloatTypeSuffix?
    |   ('0'..'9')+ FloatTypeSuffix
    ;


fragment
Exponent : ('e'|'E') ('+'|'-')? ('0'..'9')+ ;


fragment
FloatTypeSuffix : ('f'|'F'|'d'|'D') ;


CharacterLiteral
    :   '\'' ( EscapeSequence | ~('\''|'\\') ) '\''
    ;


StringLiteral
    :  '"' ( EscapeSequence | ~('\\'|'"') )* '"'
    ;


fragment
EscapeSequence
    :   '\\' ('b'|'t'|'n'|'f'|'r'|'\"'|'\''|'\\')
    |   UnicodeEscape
    |   OctalEscape
    ;


fragment
OctalEscape
    :   '\\' ('0'..'3') ('0'..'7') ('0'..'7')
    |   '\\' ('0'..'7') ('0'..'7')
    |   '\\' ('0'..'7')
    ;


fragment
UnicodeEscape
    :   '\\' 'u' HexDigit HexDigit HexDigit HexDigit
    ;


ENUM
    :   'enum'
    ;


ASSERT
    :   'assert'
    ;


Ident
    :   Letter (Letter|JavaIDDigit)*
    ;


fragment
Letter
    :  '\u0024' |
       '\u0041'..'\u005a' |
       '\u005f' |
       '\u0061'..'\u007a' |
       '\u00c0'..'\u00d6' |
       '\u00d8'..'\u00f6' |
       '\u00f8'..'\u00ff' |
       '\u0100'..'\u1fff' |
       '\u3040'..'\u318f' |
       '\u3300'..'\u337f' |
       '\u3400'..'\u3d2d' |
       '\u4e00'..'\u9fff' |
       '\uf900'..'\ufaff'
    ;


fragment
JavaIDDigit
    :  '\u0030'..'\u0039' |
       '\u0660'..'\u0669' |
       '\u06f0'..'\u06f9' |
       '\u0966'..'\u096f' |
       '\u09e6'..'\u09ef' |
       '\u0a66'..'\u0a6f' |
       '\u0ae6'..'\u0aef' |
       '\u0b66'..'\u0b6f' |
       '\u0be7'..'\u0bef' |
       '\u0c66'..'\u0c6f' |
       '\u0ce6'..'\u0cef' |
       '\u0d66'..'\u0d6f' |
       '\u0e50'..'\u0e59' |
       '\u0ed0'..'\u0ed9' |
       '\u1040'..'\u1049'
   ;


WS  :  (' '|'\r'|'\t'|'\u000C'|'\n') {$channel=HIDDEN;}
    ;


COMMENT
    :   '/*' ( options {greedy=false;} : . )* '*/' {$channel=HIDDEN;}
    ;


LINE_COMMENT
    : '//' ~('\n'|'\r')* '\r'? '\n' {$channel=HIDDEN;}
    ;
