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


@parser::header {
    from functools import partial

    from java2python.lib import Formats as FS, ruleName as RN, ruleNames as RNS
    from java2python.parser.local import LocalParser

    TOP, PREV = -1, -2
}


compilationUnit returns [module]
@init {
    $module = module = self.factory('module')
    self.scope.module.push(self.scope.block.push(module))
    self.checkCommentsLeading($start)
}
@after {
    self.checkCommentsTrailing()
    module.cleanup()
    self.scope.block.pop()
    self.scope.module.pop()
}
    :   annotations
        (   packageDecl importDecl* typeDecl*
        |   classOrInterfaceDecl typeDecl*
        )
    |   packageDecl? importDecl* typeDecl*
    ;


packageDecl
    :   'package' qualifiedName ';'
    ;


importDecl
    :   'import' 'static'? qualifiedName ('.' '*')? ';'
    ;


typeDecl
    :   classOrInterfaceDecl
    |   ';'
    ;


classOrInterfaceDecl
    :   classOrInterfaceModifiers (classDecl | interfaceDecl)
    ;

classOrInterfaceModifiers
    :   classOrInterfaceModifier*
    ;


classOrInterfaceModifier
    :   annotation   // class or interface
    |   'public'     // class or interface
    |   'protected'  // class or interface
    |   'private'    // class or interface
    |   'abstract'   // class or interface
    |   'static'     // class or interface
    |   'final'      // class only -- does not apply to interfaces
    |   'strictfp'   // class or interface
    ;


modifiers returns [mods]
@init {
    $mods = []
}
    :   (modifier { $mods.append($modifier.value) })*
    ;


classDecl
@init {
    scope = self.scope.block
    block = scope.push(self.factory('class', parent=scope.top))
}
@after {
    scope.pop()
}
    :   normalClassDecl[block] |  enumDecl[block]
    ;


normalClassDecl [klass]
@after {
    klass.parent.addVariable(klass.name)
}
    :   'class' id0=Ident { klass.name = $id0.text } typeParameters?
        ('extends' tp0=type { klass.addType($tp0.value) })?
        ('implements' tl0=typeList { klass.addTypes($tl0.types) })?
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


enumDecl [klass]
    :   ENUM Ident ('implements' typeList)? enumBody
    ;


enumBody
    :   '{' enumConstants? ','? enumBodyDecls? '}'
    ;


enumConstants
    :   enumConstant (',' enumConstant)*
    ;


enumConstant
    :   annotations? Ident arguments? classBody?
    ;


enumBodyDecls
    :   ';' (classBodyDecl)*
    ;


interfaceDecl
@init {
    scope = self.scope.block
    block = scope.push(self.factory('class', parent=scope.top))
}
@after {
    scope.pop()
}
    :   normalInterfaceDecl[block]
    |   annotationTypeDecl
    ;


normalInterfaceDecl [iface]
    :   'interface' id0=Ident { iface.name = $id0.text }
         typeParameters?
         ('extends' tl0=typeList { iface.addTypes($tl0.types) })?
         interfaceBody
    ;


typeList returns [types]
@init {
    $types = []
    append = $types.append
}
    :   t0=type { append($t0.value) } (',' t1=type { append($t1.value) })*
    ;


classBody
    :   '{' classBodyDecl* '}'
    ;


classBodyDecl
    :   ';'
    |   'static'? block
    |   md0=modifiers memberDecl[$md0.mods]
    ;


memberDecl [mods]
    :   genericMethodOrConstructorDecl
    |   fieldOrMethodDecl[$mods]
    |   'void' id0=Ident voidMethodDeclRest[$id0.text, $mods]
    |   id1=Ident constructorDeclRest[$id1.text, $mods]
    |   interfaceDecl
    |   classDecl
    ;


fieldOrMethodDecl [mods]
    :   t0=type (methodDecl[$t0.value, $mods] | fieldDecl[$t0.value, $mods])
    ;


genericMethodOrConstructorDecl
    :   typeParameters genericMethodOrConstructorRest
    ;


genericMethodOrConstructorRest
    :   (type | 'void') id0=Ident methodDeclRest[$id0.text]
    |   id1=Ident constructorDeclRest[$id1.text]
    ;


methodDecl [type, mods]
@init {
    scope = self.scope.block
    block = scope.push(self.factory('method', parent=scope.top, type=type))
}
@after {
    scope.pop()
}
    :   id0=Ident methodDeclRest[$id0.text, $mods]
    ;


fieldDecl [type, mods]
    :   variableDecls[type] ';'
    ;


interfaceBody
    :   '{' interfaceBodyDecl* '}'
    ;


interfaceBodyDecl
    :   md0=modifiers interfaceMemberDecl[$md0.mods]
    |   ';'
    ;


interfaceMemberDecl [mods]
    :   interfaceMethodOrFieldDecl[mods]
    |   interfaceGenericMethodDecl
    |   'void' id0=Ident voidInterfaceMethodDeclRest[$id0.text, mods]
    |   interfaceDecl
    |   classDecl
    ;


interfaceMethodOrFieldDecl [mods]
    :   type id0=Ident interfaceMethodOrFieldRest[$id0.text, mods]
    ;


interfaceMethodOrFieldRest [name, mods]
    :   constantDeclsRest ';'
    |   interfaceMethodDeclRest[name, mods]
    ;


methodDeclRest [name, mods]
@init {
    method = self.scope.block.top
    method.name = name
    method.modifiers.extend(mods)
}
    :   formalParameters ('[' ']')*
        ('throws' qualifiedNameList)?
        (   methodBody
        |   ';'
        )
    ;


voidMethodDeclRest [name, mods]
@init {
    scope = self.scope.block
    block = scope.push(self.factory('method', name=name, parent=scope.top,
                                    modifiers=mods, type='void'))
}
@after {
    scope.pop()
}
    :   formalParameters ('throws' qualifiedNameList)?
        (   methodBody
        |   ';'
        )
    ;


interfaceMethodDeclRest [name, mods]
@init {
    scope = self.scope.block
    block = scope.push(self.factory('method', name=name, parent=scope.top,
                                    modifiers=mods))
}
@after {
    scope.pop()
}
    :   formalParameters ('[' ']')* ('throws' qualifiedNameList)? ';'
    ;


interfaceGenericMethodDecl
    :   typeParameters (type | 'void') Ident
        interfaceMethodDeclRest[None, None]
    ;


voidInterfaceMethodDeclRest [name, mods]
@init {
    scope = self.scope.block
    block = scope.push(self.factory('method', name=name, parent=scope.top,
                                    modifiers=mods, type='void'))
}
@after {
    scope.pop()
}
    :   formalParameters ('throws' qualifiedNameList)? ';'
    ;


constructorDeclRest [name, mods]
@init {
    scope = self.scope.block
    block = scope.push(self.factory('method', name='__init__',
                                    parent=scope.top, modifiers=mods))
}
@after {
    scope.pop()
}
    :   formalParameters ('throws' qualifiedNameList)? constructorBody
    ;


constantDecl
    :   Ident constantDeclRest
    ;


variableDecls [type]
    :   variableDecl[type] (',' variableDecl[type] )*
    ;


variableDecl [type]
@init {
    scope = self.scope.block
}
    :   vd0=variableDeclId
        {
            expr = scope.push(
                self.factory('expression', format=FS.assign, left=$vd0.text,
                             right='None', parent=scope.top, type=type)
            )
        }
        ('='
            {
                self.scope.expr.push(expr)
            }
            variableInitializer
            {
                self.scope.expr.pop()
                if 0: # expr and str(expr) and expr.isBaseType:
                    expr.update(format=FS.r)
                ## also hacky but not as much
                if 0: # str(expr.right) == 'None':
                    expr.update(format=FS.r)
                #scope.pop()
            }
        )?
        {
            scope.pop()
        }
    ;


constantDeclsRest
    :   constantDeclRest (',' constantDecl)*
    ;


constantDeclRest
    :   ('[' ']')* '=' variableInitializer
    ;


variableDeclId returns [value]
@init {
    $value = dict(name='', dimensions=0)
}
    :   id0=Ident { $value['name'] = $id0.text }
        ('[' ']'  { $value['dimensions'] += 1  })*
    ;


variableInitializer
    :   arrayInitializer
    |   expression
    ;


arrayInitializer
    :   '{' (variableInitializer (',' variableInitializer)* (',')? )? '}'
    ;


modifier returns [value]
@init  { anno = False }
@after {
    $value = None if anno else $modifier.text
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


type returns [value]
@after {
    $value = self.scope.module.top.mapType($value)
}
    :	ct0=classOrInterfaceType { $value = ct0.value } ('[' ']')*
    |	pt0=primitiveType { $value = $pt0.text }  ('[' ']')*
    ;


classOrInterfaceType returns [value]
@init  {
    $value = []
}
@after {
    find = self.scope.block.top.findVariable
    $value = [find(v) for v in $value]
    $value = '.'.join($value)
    $value = find($value)
}
    :	id0=Ident { $value.append($id0.text) } typeArguments?
        ('.' id1=Ident { $value.append($id1.text) }  typeArguments?)*
    ;


primitiveType returns [value]
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
    :   variableModifiers t0=type formalParameterDeclsRest[$t0.value]
    ;


formalParameterDeclsRest [type]
@init {
    add = self.scope.block.top.addParameter
}
    :   vd0=variableDeclId { add(type=type, **$vd0.value) } (',' formalParameterDecls)?
    |   '...' vd1=variableDeclId { add(type=type, variadic=True, **$vd1.value) }
    ;


methodBody
    :   block
    ;


constructorBody
    :   '{' explicitConstructorInvocation? blockStatement* '}'
    ;


explicitConstructorInvocation
@init {
    scope = self.scope.expr
    expr = scope.push(self.factory('expression', format=FS.r, rule=RN()))
}
@after {
    scope.pop()
}
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
    |   BooleanLiteral
    |   NullLiteral
    ;


integerLiteral
    :   HexLiteral
    |   OctalLiteral
    |   DecimalLiteral
    ;


BooleanLiteral
    :   'true'
    |   'false'
    ;


NullLiteral
    :   'null'
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


annotationTypeDecl
    :   '@' 'interface' Ident annotationTypeBody
    ;


annotationTypeBody
    :   '{' (annotationTypeElementDecl)* '}'
    ;


annotationTypeElementDecl
    :   modifiers annotationTypeElementRest
    ;


annotationTypeElementRest
    :   type annotationMethodOrConstantRest ';'
    |   normalClassDecl[None] ';'?
    |   normalInterfaceDecl[None] ';'?
    |   enumDecl[None] ';'?
    |   annotationTypeDecl ';'?
    ;


annotationMethodOrConstantRest
    :   annotationMethodRest
    |   annotationConstantRest
    ;


annotationMethodRest
    :   Ident '(' ')' defaultValue?
    ;


annotationConstantRest
    :   variableDecls[None]
    ;


defaultValue
    :   'default' elementValue
    ;


// STATEMENTS / BLOCKS


block
    :   '{' blockStatement* '}'
    ;


blockStatement
    :   localVariableDeclStatement
    |   classOrInterfaceDecl
    |   statement
    ;


localVariableDeclStatement
    :    localVariableDecl ';'
    ;


localVariableDecl
    :   variableModifiers
        t0=type
        variableDecls[$t0.value]
    ;


variableModifiers
    :   variableModifier*
    ;


statement
    :   block
    |   ASSERT expression (':' expression)? ';'
    |   'if' parExpression statement (options {k=1;}:'else' statement)?
    |   'for' '(' forControl ')' statement
    |   'while' parExpression statement
    |   'do' statement 'while' parExpression ';'
    |   'try' block
        (   catches 'finally' block
        |   catches
        |   'finally' block
        )
    |   'switch' parExpression '{' switchBlockStatementGroups '}'
    |   'synchronized' parExpression block
    |   'return'
         expression? ';'
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
    :   variableModifiers type variableDeclId
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


forControl
options {k=3;} // be efficient for common case: for (ID ID : ID) ...
    :   enhancedForControl
    |   forInit? ';' expression? ';' forUpdate?
    ;


forInit
    :   localVariableDecl
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
    :   conditionalExpression (a0=assignmentOperator expression)?
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
        { $t1.getLine() == $t2.getLine() and \
          $t1.getCharPositionInLine() + 1 == $t2.getCharPositionInLine() and \
          $t2.getLine() == $t3.getLine() and \
          $t2.getCharPositionInLine() + 1 == $t3.getCharPositionInLine() }?
    |   ('>' '>' '>' '=')=> t1='>' t2='>' t3='>' t4='='
        { $t1.getLine() == $t2.getLine() and \
          $t1.getCharPositionInLine() + 1 == $t2.getCharPositionInLine() and \
          $t2.getLine() == $t3.getLine() and \
          $t2.getCharPositionInLine() + 1 == $t3.getCharPositionInLine() and \
          $t3.getLine() == $t4.getLine() and \
          $t3.getCharPositionInLine() + 1 == $t4.getCharPositionInLine() }?
    |   ('>' '>' '=')=> t1='>' t2='>' t3='='
        { $t1.getLine() == $t2.getLine() and \
          $t1.getCharPositionInLine() + 1 == $t2.getCharPositionInLine() and \
          $t2.getLine() == $t3.getLine() and \
          $t2.getCharPositionInLine() + 1 == $t3.getCharPositionInLine() }?
    ;


conditionalExpression
    :   conditionalOrExpression ('?' expression ':' expression )?
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
    :   instanceOfExpression
        (eq0=('==' | '!=')
        instanceOfExpression
        )*
    ;


instanceOfExpression
    :   relationalExpression ('instanceof' type)?
    ;


relationalExpression
    :   shiftExpression (op0=relationalOp shiftExpression)*
    ;


relationalOp
    :   ('<' '=')=> t1='<' t2='='
        { $t1.getLine() == $t2.getLine() and \
          $t1.getCharPositionInLine() + 1 == $t2.getCharPositionInLine() }?
    |   ('>' '=')=> t1='>' t2='='
        { $t1.getLine() == $t2.getLine() and \
          $t1.getCharPositionInLine() + 1 == $t2.getCharPositionInLine() }?
    |   '<'
    |   '>'
    ;


shiftExpression
    :   additiveExpression ( shiftOp additiveExpression )*
    ;


shiftOp
    :   ('<' '<')=> t1='<' t2='<'
        { $t1.getLine() == $t2.getLine() and \
          $t1.getCharPositionInLine() + 1 == $t2.getCharPositionInLine() }?
    |   ('>' '>' '>')=> t1='>' t2='>' t3='>'
        { $t1.getLine() == $t2.getLine() and \
          $t1.getCharPositionInLine() + 1 == $t2.getCharPositionInLine() and \
          $t2.getLine() == $t3.getLine() and \
          $t2.getCharPositionInLine() + 1 == $t3.getCharPositionInLine() }?
    |   ('>' '>')=> t1='>' t2='>'
        { $t1.getLine() == $t2.getLine() and \
          $t1.getCharPositionInLine() + 1 == $t2.getCharPositionInLine() }?
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

    def start():
        try:
            expr = self.scope.expr.top.nest(format=FS.r)
            pop = lambda:None
        except (IndexError, ):
            expr = self.factory('expression', format=FS.r, parent=self.scope.block.top)
            self.scope.expr.push(expr)
            pop = self.scope.expr.pop
        return expr, pop
}
    :   parExpression
    |   'this' ('.' id0=Ident)* identifierSuffix?
    |   'super' superSuffix

    |   { expr, pop = start() }
        literal
        {
            expr.update(right=$literal.text)
            pop()
        }
    |   'new' creator

    |   id1=Ident
        ('.' id2=Ident)*
        (identifierSuffix)?

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
    :   nonWildcardTypeArguments?
        id0=Ident
        classCreatorRest
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
    :   nonWildcardTypeArguments Ident arguments
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
