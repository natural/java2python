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
    superClass=LocalParser;
}


// generic scope for rules to refer to when the real block type
// (class, method, etc). is unknown or irrelevant.
scope py_block {
    block;
}


// scope for a (single) python module; roughly equivalent to the java
// compilation unit.
scope py_module {
    module;
}


// scope for python classes; this scope is nested for us by the rule
// invocations.
scope py_klass {
    klass;
}


// scope for python methods.  this scope is never nested because java
// syntax rules prevent nested methods.
scope py_method {
    method;
}


// mixin scope to capture class, method, field and variable modifiers.
scope py_modifier {
    add;
}


// mixin scope to capture class, method, field and variable types.
scope py_type {
    add;
}


// scope for python expressions and statements.  the 'nest' attribute
// is set by the parent expression or block to indicate how to create
// a new contained expression.
scope py_expr {
    expr;
    nest;
}


@parser::header {
    from java2python.parser.local import LocalParser
    TOP = -1
}


@lexer::members {
    ##// composite grammar files like this one don't provide
    ##// a way to indicate lexer base class so we implement
    ##// the methods we need directly.
    def addComment(self, start, stop, text):
        self.comments.append((start, stop, text.split('\n')))
}


compilationUnit returns [module]
scope py_block, py_module, py_klass;
@init {
    ##// the topmost block, which is always a module
    $module = $py_module::module = self.factory('module')

    ##// every compilation unit has at least one class-like block
    ##// (class, enum, or interface), so we establish one here.  this also establishes
    ##// the topmost py_block scope.
    $py_klass::klass = $py_block::block = self.factory('class', parent=$module)

    ##// necessary to catch any leading comments before initial syntax.
    self.checkCommentsLeading($start)
}
@after {
    ##// necessary to catch any trailing comments.
    self.checkCommentsTrailing()

    ##// message the module that the parsing is complete.
    $module.cleanup()
}
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
    :   classOrInterfaceDeclaration
    |   ';'
    ;


classOrInterfaceDeclaration
    :   classOrInterfaceModifiers (classDeclaration | interfaceDeclaration)
    ;


classOrInterfaceModifiers
    :   classOrInterfaceModifier*
    ;


// note that don't need a separate py_mod scope because this rule is
// for class-like blocks only and we can refer to that scoped block
// directly.
classOrInterfaceModifier
@init {
    anno = False
}
@after {
    if not anno:
        $py_klass::klass.addModifier($classOrInterfaceModifier.text)
}
    :   annotation { anno = True }    // class or interface
    |   'public'                      // class or interface
    |   'protected'                   // class or interface
    |   'private'                     // class or interface
    |   'abstract'                    // class or interface
    |   'static'                      // class or interface
    |   'final'                       // class only -- does not apply to interfaces
    |   'strictfp'                    // class or interface
    ;


modifiers
    :   (modifier)*
    ;


classDeclaration
    :   normalClassDeclaration
    |   enumDeclaration
    ;


normalClassDeclaration
scope py_type;
@init {
    $py_type::add = $py_klass::klass.addType
}
    :   'class' id0=Ident { $py_klass::klass.name = $id0.text } typeParameters?
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


// this rule is heavily modified from the original.  this
// implementation splits up methods, fields, and inner classes for
// greater clarity and simplicity.
classBodyDeclaration
    :   ';'
    |   classBlockDecl
    |   classMethodDecl
    |   classFieldDecl
    |   classInnerClassDecl
    ;


classBlockDecl
    :  'static'? block
    ;


classMethodDecl
scope py_block, py_method, py_type;
@init {
    ##// this needs to be pushed down into the rule statements.
    $py_block::block = $py_method::method = method = self.factory('method')
    $py_type::add = method.addType
}
@after {
    method.parent = $py_klass::klass
}
    :   modifiers genericMethodOrConstructorDecl

    |   modifiers 'void' id0=Ident
        {
        method.name = $id0.text
        method.type = 'void'
        }
        voidMethodDeclaratorRest

    |   modifiers id1=Ident
        {
        method.name = '__init__'
        }
        constructorDeclaratorRest

    |   modifiers type id2=Ident
        {
        method.name = $id2.text
        }
        methodDeclaratorRest
    ;


classFieldDecl
scope py_block, py_type;
@init {
    ##// to capture the field decl, we declare a new empty scope and reassign
    ##// it's children to the current py_klass afterward.
    $py_block::block = block = self.factory('block')
    $py_type::add = block.addType
}
@after {
    block.reparentChildren($py_klass::klass)
}
    :   modifiers type variableDeclarators ';'
    ;


classInnerClassDecl
scope py_block, py_klass;
@init {
    $py_block::block = $py_klass::klass = klass = self.factory('class')
}
@after {
    klass.parent = $py_klass[TOP-1]::klass
}
    :    modifiers classDeclaration
    |    modifiers interfaceDeclaration
    ;


genericMethodOrConstructorDecl
    :   typeParameters genericMethodOrConstructorRest
    ;


genericMethodOrConstructorRest
    :   (type | 'void') Ident methodDeclaratorRest
    |   Ident constructorDeclaratorRest
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
scope py_expr;
@init {
    $py_expr::expr = expr = \
        self.factory('expression', format='{left} = {right}', right='None')
    $py_expr::nest = expr.nestRight
}
@after {
    expr.parent = $py_block::block
    if expr.right == 'None':
        expr.update(format='{left} = {type}()')
}
    :   variableDeclarator (',' variableDeclarator)*
    ;


variableDeclarator
    :   vd0=variableDeclaratorId
        { $py_expr::expr.update(left=$vd0.value['name']) }
        ('='
            {
            $py_expr::expr = expr = $py_expr::nest(format='{left}')
            $py_expr::nest = expr.nestLeft
            }
            variableInitializer
        )?
    ;


constantDeclaratorsRest
    :   constantDeclaratorRest (',' constantDeclarator)*
    ;


constantDeclaratorRest
    :   ('[' ']')* '=' variableInitializer
    ;


variableDeclaratorId returns [value]
@init {
    $value = dict(name='', dimensions=0)
}
    :   id0=Ident { $value['name'] = $id0.text }
        ('[' ']'  { $value['dimensions'] += 1})*
    ;


variableInitializer
    :   arrayInitializer
    |   expression
    ;


arrayInitializer
    :   '{' (variableInitializer (',' variableInitializer)* (',')? )? '}'
    ;


modifier
@init {
    anno = False
}
@after {
    if not anno:
        $py_block::block.addModifier($modifier.text)
}
    :   annotation { anno = True }
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
@init {
    add = $py_type::add
}
    :	classOrInterfaceType ('[' ']')*
    |	primitiveType
        { add($primitiveType.text) }
        ('[' ']')*
        // TODO:  add 'set-type-dimensions'
    ;


classOrInterfaceType
    :	id0=Ident typeArguments?
        ('.' id1=Ident typeArguments?)*
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
    :   '(' formalParameterDecls? ')'
    ;


formalParameterDecls
    :   variableModifiers type formalParameterDeclsRest
    ;


formalParameterDeclsRest
    :   vd0=variableDeclaratorId
        { $py_method::method.addParameter(**$vd0.value) }
        (',' formalParameterDecls)?

    |   '...' vd1=variableDeclaratorId
        { $py_method::method.addParameter(variadic=True, **$vd1.value) }
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
scope py_expr;
@init {
    $py_expr::expr = expr = self.factory('expression', format='{left}')
    $py_expr::nest = expr.nestLeft
}
@after {
    expr.parent = $py_block::block
}
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
@init {
    ##// this is only temporary; if there isn't an expression, it's because
    ##// the calling rule hasn't created one and is therefore wrong.
    try:
        expr = $py_expr::expr
    except (IndexError, ):
        pass
        #expr = self.factory('expression', format='{left}')
}
    :   parExpression
    |   'this' ('.' Ident)* identifierSuffix?
    |   'super' superSuffix
    |   literal { expr.update(left=$literal.text) }
    |   'new' creator
    |   id0=Ident ('.' id1=Ident)* identifierSuffix?
    |   primitiveType ('[' ']')* '.' 'class'
    |   'void' '.' 'class'
    ;


identifierSuffix
    :   ('[' ']')+ '.' 'class'
    |   ('[' expression ']')+ // can also be matched by selector, but do here
    |   arguments
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
    :   '/*' ( options {greedy=false;} : . )* '*/'
    {
    $channel = HIDDEN
    self.addComment($start, $stop, $text[2:-2])
    }
    ;


LINE_COMMENT
    : '//' ~('\n'|'\r')* '\r'? '\n'
    {
    $channel = HIDDEN
    self.addComment($start, $stop, $text[2:])
    }
    ;
