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


// topmost scope, a python module
scope py_module {
    module;
}

// python class scope
scope py_klass {
    klass;
}

// python method scope
scope py_method {
    method;
}

// the module, klass, and method scopes use this scope as a "mixin"
// scope to provide down-level rules a reference to the active scope
// without refering to it by a specific name.
scope py_block {
    block;
}


scope py_expr {
    expr;
    nest;
}


scope py_assign {
    assign;
}


@parser::header {
    TOP = -1
    from java2python.parser.local import LocalParser
}


@lexer::members {
    ##// composite grammar files like this one don't provide
    ##// a way to indicate lexer base class so we implement
    ##// the methods we need directly.  the client using the lexer
    ##// must call setComments before passing the lexer to a token
    ##// stream.
    def setComments(self, comments):
         self.comments = comments

    def addComment(self, start, stop, text):
        self.comments.append((start, stop, text.split('\n')))
}




compilationUnit returns [module]
scope py_module, py_block;
@init {
    ##// the topmost block, which is always a module
    $module = $py_module::module = $py_block::block = self.factory('module')
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


// this rule only executes within a py_module scope
packageDeclaration
@after { $py_module::module.addPackage($qn0.value) }
    :   'package' qn0=qualifiedName ';'
    ;


// this rule only executes within a py_module scope
importDeclaration
@init { isStatic = dotStar = False }
@after {
    $py_module::module.addImport($qn0.value, isStatic=isStatic, dotStar=dotStar)
}
    :   'import' ('static' { isStatic = True })?
        qn0=qualifiedName ('.' '*' { dotStar = True })? ';'
    ;


typeDeclaration
    :   classOrInterfaceDeclaration
    |   ';'
    ;


classOrInterfaceDeclaration
scope py_klass, py_block;
@init {
    $py_block::block = $py_klass::klass = \
        self.factory('class', parent=$py_block[TOP-1]::block)

}
    :   classOrInterfaceModifiers (classDeclaration | interfaceDeclaration)
    ;


classOrInterfaceModifiers
    :   classOrInterfaceModifier*
    ;


classOrInterfaceModifier
@init { isAnno = False }
@after {
    if not isAnno:
        $py_block::block.addModifier($classOrInterfaceModifier.text)
}
    :   annotation { isAnno = True } // class or interface
    |   'public'                     // class or interface
    |   'protected'                  // class or interface
    |   'private'                    // class or interface
    |   'abstract'                   // class or interface
    |   'static'                     // class or interface
    |   'final'                      // class only -- does not apply to interfaces
    |   'strictfp'                   // class or interface
    ;


modifiers
    :   (modifier)*
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
    :   ';'
    |   'static'? block
    |   memberDecl
    ;


memberDecl
scope py_klass, py_block;
@init {
    method = self.factory('method')
    klass = self.factory('class')
    field = self.factory('block')
    isClass = isMethod = isField = False
}
@after {
    parent = $py_block[TOP-1]::block
    if isMethod:
        method.setParent(parent)
    if isClass:
        klass.setParent(parent)
    if isField:
        field.reparentChildren(parent)
}
    :   modifiers genericMethodOrConstructorDecl

    |   { $py_block::block = method }
        modifiers type methodDeclaration
        { isMethod = True }

    |   { $py_block::block = field }
        modifiers type fieldDeclaration
        { isField = True }

    |   { $py_block::block = method }
        modifiers 'void' { method.setType('void') }
        id0=Ident  { method.setName($id0.text) }
        voidMethodDeclaratorRest
        { isMethod = True }

    |   { $py_block::block = method }
        modifiers Ident { method.setName('__init__') }
        constructorDeclaratorRest
        { isMethod = True }

    |   modifiers interfaceDeclaration

    |   { $py_klass::klass = $py_block::block = klass }
        modifiers classDeclaration
        { isClass = True }
    ;


genericMethodOrConstructorDecl
    :   typeParameters genericMethodOrConstructorRest
    ;


genericMethodOrConstructorRest
    :   (type | 'void') Ident methodDeclaratorRest
    |   Ident constructorDeclaratorRest
    ;


methodDeclaration
    :   id0=Ident { $py_block::block.setName($id0.text) }
        methodDeclaratorRest
    ;


fieldDeclaration
scope py_expr;
@init {
    expr = self.factory('expression', format='${left} = ${type}()', parent=$py_block::block)
    $py_expr::expr, $py_expr::nest = expr, expr.nestLeft
}
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
scope py_expr;
@init {
    $py_expr::expr = expr = $py_expr[TOP-1]::nest(format='${left}')
    $py_expr::nest = expr.nestLeft
}
    :   vd0=variableDeclaratorId { expr.update(left=$vd0.text) }
        ('='
            {
            $py_expr[TOP-1]::expr.update(format='${left} = ${right}')
            $py_expr::nest = $py_expr[TOP-1]::expr.nestRight
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
@init  { anno = False }
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
    :	classOrInterfaceType ('[' ']')*
    |	primitiveType
        { $py_block::block.setType($primitiveType.text) }
        ('[' ']')*
    ;


classOrInterfaceType
@init  { ids = [] }
@after {
    $py_block::block.setType(ids)
}
    :	id0=Ident
        { ids.append(id0.text) }
        typeArguments?
        ('.' id1=Ident typeArguments? { ids.append(id1.text) })*
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
scope py_block;
@init {
    $py_block::block = self.factory('block')
}
    :   variableModifiers type formalParameterDeclsRest
    ;


formalParameterDeclsRest
@init {
    param = self.factory('expression', format='${left}', type=$py_block::block.getType())
}
@after {
    $py_block[TOP-1]::block.addParameter(param)
}
    :   id0=variableDeclaratorId
        { param.update(left=$id0.text) }
        (',' formalParameterDecls)?

    |   '...'
        id1=variableDeclaratorId
        { param.update(left='*' + $id1.text) }
    ;


methodBody
    :   block
    ;


constructorBody
    :   '{' explicitConstructorInvocation? blockStatement* '}'
    ;


explicitConstructorInvocation
scope py_expr;
@init {
    $py_expr::expr = expr = self.factory('expression', format='${left}')
    $py_expr::nest = expr.nestLeft
}
    :   nonWildcardTypeArguments? ('this' | 'super') arguments ';'
    |   primary '.' nonWildcardTypeArguments? 'super' arguments ';'
    ;


qualifiedName returns [value]
@init { $value = [] }
    :   id0=Ident { $value.append($id0.text) }
        ('.' id1=Ident { $value.append($id1.text) })*
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
scope py_block;
@init {
    $py_block::block = self.factory('block')
}
@after {
    $py_block::block.reparentChildren($py_block[TOP-1]::block)
}
    :    localVariableDeclaration ';'
    ;


localVariableDeclaration
scope py_expr;
@init {
    $py_expr::expr = expr = self.factory('expression', format='${left}', parent=$py_block::block)
    $py_expr::nest = expr.nestLeft
}
    :   variableModifiers type variableDeclarators
    ;


variableModifiers
    :   variableModifier*
    ;


statement
scope py_block, py_expr;
@init {
    parent = $py_block[TOP-1]::block
    $py_expr::expr = expr = self.factory('expression', format='${left}')
    $py_expr::nest = expr.nestLeft
}
    :   // generic block
        { $py_block::block = block = self.factory('block') }
        block
        { block.reparentChildren(parent) }


    |   ASSERT expression (':' expression)? ';'

    |   // if statement
        {
        $py_block::block = block = self.factory('statement', name='if', parent=parent)
        $py_expr::expr = expr = block.getPrimaryExpression()
        $py_expr::nest = expr.nestLeft
        }
        'if' parExpression
        st0=statement
        (options {k=1;}: 'else' statement)?


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


    |   // return statement
        {
        $py_block::block = self.factory('block')
        expr = self.factory('expression', left='return', format='${left}', 
                            parent=$py_block[TOP-1]::block)

        }
        'return' ({
                    expr.update(format='${left} ${right}', right='${right}')
                    $py_expr::expr = expr
                    $py_expr::nest = expr.nestRight
                  }
        expression)?
        ';'

    |   'throw' expression ';'
    |   'break' Ident? ';'
    |   'continue' Ident? ';'
    |   ';'

    |   // expression statement
        {
        $py_block::block = self.factory('block')
        expr.setParent($py_block[TOP-1]::block)
        }
        statementExpression ';'

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


statementExpression
    :   expression
    ;


constantExpression
    :   expression
    ;


parExpression
    :   '(' expression ')'
    ;


expressionList
scope py_expr;
@init {
    $py_expr::expr = expr = $py_expr[TOP-1]::nest(format='${left}, ${right}')
    $py_expr::nest = expr.nestLeft
}
@after {
    ##// update the last expression (which may be the first and only
    ##// expression) to not have a trailing comma.
    expr.update(format='${left}')
}
    :   expression
        (','
            {
            ##// update the scope for the next iteration
            $py_expr::expr = expr = expr.nestRight(format='${left}, ${right}')
            $py_expr::nest = expr.nestLeft
            }
            expression
        )*
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
    :   instanceOfExpression
        ( ex0=('==' | '!=')
            {
            $py_expr[TOP]::expr.update(format='${left} ' + $ex0.text + ' ${right}')
            $py_expr[TOP]::nest = $py_expr[TOP]::expr.nestRight
            }
          instanceOfExpression
        )*
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
scope py_expr;
@init {
    nest = $py_expr[TOP-1]::nest
    $py_expr::expr = expr = nest(format='${left}')
    $py_expr::nest = expr.nestLeft
}
    :   parExpression
    |   'this' ('.' Ident)* identifierSuffix?
    |   'super' superSuffix

    |   literal { $py_expr::expr.update(left=$literal.text) }

    |   { $py_expr::nest = expr.nestLeft }
        'new' creator

    |   id0=Ident
        { expr.update(left=$id0.text, format='${left}${right}') }
        ('.' id1=Ident
            { expr = expr.nestRight(left=$id1.text, format='.${left}${right}') }
        )*
        { $py_expr::nest = expr.nestRight }
        identifierSuffix?

    |   primitiveType ('[' ']')* '.' 'class'

    |   'void' '.' 'class'
    ;


identifierSuffix
scope py_expr;
@init {
    $py_expr::expr = expr = $py_expr[TOP-1]::nest(format="(${left})")
    $py_expr::nest = expr.nestLeft
}
    :   ('[' ']')+ '.' 'class'
    |   ('[' expression ']')+

    |   '(' (expressionList)? ')'

    |   '.' 'class'
    |   '.' explicitGenericInvocation
    |   '.' 'this'
    |   '.' 'super' arguments
    |   '.' 'new' innerCreator
    ;


creator
scope py_block, py_expr;
@init {
    $py_block::block = self.factory('block')
    nest = $py_expr[TOP-1]::nest
    $py_expr::expr = expr = nest(format="${type}(${left})")
    $py_expr::nest = expr.nestLeft

}
@after {
    expr.update(type=$py_block::block.getType())
}
    :   nonWildcardTypeArguments createdName classCreatorRest
    |   createdName (arrayCreatorRest | classCreatorRest)
    ;


createdName
    :   classOrInterfaceType
    |   primitiveType { $py_block::block.setType($primitiveType.text) }
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
