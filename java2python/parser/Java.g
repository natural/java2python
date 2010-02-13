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


// scope alias for rules to refer to when the real block type (class,
// method, etc). is unknown or irrelevant.
scope py_block {
    block;
}


// scope for a (single) python module; for our puroposes this is
// equivalent to the java compilation unit.
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
// a contained expression.
scope py_expr {
    expr;
    nest;
}


@parser::header {
    from java2python.parser.local import LocalParser, Formats as FS, ruleName
    TOP, PREV = -1, -2
}


@lexer::members {
    ##// composite grammar files like this one don't provide
    ##// a way to indicate lexer base class so we implement
    ##// the methods we need directly.
    def addComment(self, start, stop, text):
        self.comments.append((start, stop, text.split('\n')))
}


compilationUnit returns [module]
scope py_module;
@init {
    ##// the topmost block, which is always a module
    $module = $py_module::module = self.factory('module')

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
@after { $py_module::module.addPackage($qn0.text) }
    :   'package' qn0=qualifiedName ';'
    ;


importDeclaration
@init  { isStatic = isStar = False }
@after { $py_module::module.addImport($qn0.text, isStatic, isStar) }
    :   'import' ('static' { isStatic=True })? qn0=qualifiedName ('.' '*' { isStar=True })? ';'
    ;


typeDeclaration
scope py_klass, py_block;
@init {
    ##// this rule is used only from the compilationUnit rule so we are
    ##// certain the parent must be the module.
    $py_klass::klass = $py_block::block = self.factory('class', parent=$py_module::module)
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


// note that don't need a separate py_mod scope because this rule is
// for class-like blocks only and we can refer to that scoped block
// directly.
classOrInterfaceModifier
@init  { anno = False }
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
    klass = $py_klass::klass
    klass.setVariation(isClass=True)
    $py_type::add = klass.addType
}
    :   'class' id0=Ident
        { klass.name = $id0.text }
        typeParameters?
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
@init {
    klass = $py_klass::klass
}
@after {
    klass.setVariation(isInterface=True)
}
    :   'interface' id0=Ident
        { klass.name = $id0.text }
        typeParameters? ('extends' typeList)? interfaceBody
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
        { method.name = $id0.text; method.type = 'void' }
        voidMethodDeclaratorRest

    |   modifiers id1=Ident
        { method.name = '__init__' }
        constructorDeclaratorRest

    |   modifiers type id2=Ident
        { method.name = $id2.text }
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
    klass.parent = $py_klass[PREV]::klass
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
scope py_block, py_method, py_type;
@init {
    method = self.factory('method', parent=$py_klass::klass)
    $py_block::block = $py_method::method = method
    $py_type::add = method.addType
}
    :   modifiers interfaceMethodOrFieldDecl

    |   modifiers interfaceGenericMethodDecl

    |   modifiers 'void' id0=Ident voidInterfaceMethodDeclaratorRest
        { method.name = $id0.text; method.type = 'void' }

    |   modifiers interfaceDeclaration

    |   modifiers classDeclaration

    |   ';'
    ;


interfaceMethodOrFieldDecl
    :   type id0=Ident
        { $py_block::block.name = $id0.text }
        interfaceMethodOrFieldRest
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
@init { method = $py_method::method }
    :   typeParameters
        (type | 'void')
        id0=Ident
        { method.name = $id0.text }
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
    expr = self.factory('expression', format=FS.assign, right='None', rule=ruleName())
    $py_expr::expr = expr
    $py_expr::nest = expr.nestRight
}
@after {
    expr.parent = $py_block::block
    if expr.right == 'None':
        expr.update(format=FS.tassign)
}
    :   variableDeclarator (',' variableDeclarator)*
    ;


variableDeclarator
    :   vd0=variableDeclaratorId
        { $py_expr::expr.update(left=$vd0.value['name']) }
        ('='
            {
            expr = $py_expr::nest(format=FS.l, rule=ruleName('assign'))
            $py_expr::expr = expr
            $py_expr::nest = $py_expr::expr.nestLeft
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
@init { $value = dict(name='', dimensions=0) }
    :   id0=Ident { $value['name'] = $id0.text }
        ('[' ']'  { $value['dimensions'] += 1 })*
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
@init {
    ids = []
}
@after {
    $py_type::add('.'.join(ids))
}
    :	id0=Ident
        { ids.append($id0.text) }
        typeArguments?
        (   '.' id1=Ident
            { ids.append($id1.text) }
            typeArguments?
        )*
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
scope py_type;
@init {
    $py_type::add = lambda x:None # todo:   add type to parameter decl
}
    :   '(' formalParameterDecls? ')'
    ;


formalParameterDecls
    :   variableModifiers type formalParameterDeclsRest
    ;


formalParameterDeclsRest
@init {
    add = $py_method::method.addParameter
}
    :   vd0=variableDeclaratorId
        { add(**$vd0.value) }
        (',' formalParameterDecls)?

    |   '...' vd1=variableDeclaratorId
        { add(variadic=True, **$vd1.value) }
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
    expr = self.factory('expression', format=FS.l, rule=ruleName())
    $py_expr::expr = expr
    $py_expr::nest = expr.nestLeft
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
/*
scope py_expr;
@init {
    expr = self.factory('expression', format=FS.r, rule=ruleName())
    $py_expr::expr = expr
    $py_expr::nest = expr.nestRight
}
@after {
    if not expr.isEmpty:
        expr.parent = $py_block::block
}
*/
    :   localVariableDeclarationStatement
    |   classOrInterfaceDeclaration
    |   statement
    ;


localVariableDeclarationStatement
    :    localVariableDeclaration ';'
    ;


localVariableDeclaration
scope py_block, py_type;
@init {
    $py_block::block = block = self.factory('block')
    $py_type::add = block.addType
}
@after {
    block.reparentChildren($py_block[PREV]::block)
}
    :   variableModifiers type variableDeclarators
    ;


variableModifiers
    :   variableModifier*
    ;


statement
scope py_expr;
@init {
    try:
        expr = $py_expr[PREV]::nest(format=FS.lr, rule=ruleName())
    except (IndexError, ):
        expr = self.factory('expression', format=FS.lr, rule=ruleName())
        expr.parent = $py_block::block
    $py_expr::expr = expr
    $py_expr::nest = expr.nestRight
}

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

    |   'return' { expr.update(left='return', format=FS.lsr) } expression? ';'

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
scope py_expr;
@init {
    $py_expr::expr = expr = $py_expr[PREV]::nest(format='('+FS.lr+')', rule=ruleName())
    $py_expr::nest = expr.nestLeft
}

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
scope py_expr;
@init {
    expr = self.factory('expression', format=FS.lr, rule=ruleName('0'))
    $py_expr::expr = expr
    $py_expr::nest = expr.nestLeft
}
@after {
    if not expr.isEmpty:
        $py_expr[PREV]::nest(format=FS.l, left=expr)
}
    :   conditionalExpression
        (   op0=assignmentOperator
            {
            op = $op0.text
            expr.update(format=FS.op(op), rule=ruleName('1'))
            if op == '>>>=':
                $py_module::module.addBsrSource()
            $py_expr::nest = expr.nestRight
            }
         expression
        )?
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
scope py_expr;
@init {
    pnest = $py_expr[PREV]::nest
    $py_expr::expr = expr = pnest(format=FS.lr)
    $py_expr::nest = nest = expr.nestLeft
}
    :   conditionalOrExpression
        (  '?'
            {
            $py_expr::expr = expr = pnest(format=FS.cond, center=expr)
            $py_expr::nest = expr.nestLeft
            }
            expression
            {
            $py_expr::nest = expr.nestRight
            }
            ':'
            expression
        )?
    ;


conditionalOrExpression
scope py_expr;
@init {
    $py_expr::expr = expr = $py_expr[PREV]::expr
    $py_expr::nest = nest = $py_expr[PREV]::nest
}
    :   conditionalAndExpression
        (   '||'
            {
            expr.update(format=FS.op('or'))
            $py_expr::expr = expr = expr.nestRight(format=FS.lr)
            $py_expr::nest = expr.nestRight
            }
            conditionalAndExpression
        )*
    ;


conditionalAndExpression
scope py_expr;
@init {
    $py_expr::expr = expr = $py_expr[PREV]::expr
    $py_expr::nest = nest = $py_expr[PREV]::nest
}
    :   inclusiveOrExpression
        (   '&&'
            {
            expr.update(format=FS.op('and'))
            $py_expr::expr = expr = expr.nestRight(format=FS.lr)
            $py_expr::nest = expr.nestRight
            }
            inclusiveOrExpression
        )*
    ;


inclusiveOrExpression
scope py_expr;
@init {
    $py_expr::expr = expr = $py_expr[PREV]::expr
    $py_expr::nest = nest = $py_expr[PREV]::nest
}
    :   exclusiveOrExpression
        (   '|'
            {
            expr.update(format=FS.op('|'))
            $py_expr::expr = expr = expr.nestRight(format=FS.lr)
            $py_expr::nest = expr.nestRight
            }
            exclusiveOrExpression
        )*
    ;


exclusiveOrExpression
scope py_expr;
@init {
    $py_expr::expr = expr = $py_expr[PREV]::expr
    $py_expr::nest = nest = $py_expr[PREV]::nest
}
    :   andExpression
        (   '^'
            {
            expr.update(format=FS.op('^'))
            $py_expr::expr = expr = expr.nestRight(format=FS.lr)
            $py_expr::nest = expr.nestRight
            }
            andExpression
        )*
    ;


andExpression
scope py_expr;
@init {
    $py_expr::expr = expr = $py_expr[PREV]::expr
    $py_expr::nest = nest = $py_expr[PREV]::nest
}
    :   equalityExpression
        (   '&'
            {
            expr.update(format=FS.op('&'))
            $py_expr::expr = expr = expr.nestRight(format=FS.lr)
            $py_expr::nest = expr.nestRight
            }
            equalityExpression
        )*
    ;


equalityExpression
scope py_expr;
@init {
    $py_expr::expr = expr = $py_expr[PREV]::expr
    $py_expr::nest = nest = $py_expr[PREV]::nest
}
    :   instanceOfExpression
        (   eq0=('==' | '!=')
            {
            expr.update(format=FS.op($eq0.text))
            $py_expr::expr = expr = expr.nestRight(format=FS.lr)
            $py_expr::nest = expr.nestRight
            }
            instanceOfExpression
        )*
    ;


instanceOfExpression
scope py_expr, py_type;
@init {
    $py_expr::expr = expr = $py_expr[PREV]::expr
    $py_expr::nest = nest = $py_expr[PREV]::nest
    $py_type::add = $py_type[PREV]::add
}
    :   relationalExpression
        (   'instanceof'
            {
            $py_type::add = expr.addType
            expr.update(format=FS.instance)
            }
            type
        )?
    ;


relationalExpression
scope py_expr;
@init {
    $py_expr::expr = expr = $py_expr[PREV]::expr
    $py_expr::nest = nest = $py_expr[PREV]::nest
}
    :   shiftExpression
        (   op0=relationalOp
            {
            expr.update(format=FS.op($op0.text))
            $py_expr::expr = expr = expr.nestRight(format=FS.lr)
            $py_expr::nest = expr.nestRight
            }
            shiftExpression
        )*
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
scope py_expr;
@init {
    $py_expr::expr = expr = $py_expr[PREV]::expr
    $py_expr::nest = nest = $py_expr[PREV]::nest
}
    :   additiveExpression
        (   op0=shiftOp
            {
            expr.update(format=FS.op($op0.text))
            $py_expr::expr = expr = expr.nestRight(format=FS.lr)
            $py_expr::nest = expr.nestRight
            }
            additiveExpression
        )*
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
scope py_expr;
@init {
    $py_expr::expr = expr = $py_expr[PREV]::nest(format=FS.lr)
    $py_expr::nest = nest = expr.nestLeft
}
    :   multiplicativeExpression
        (   op0=('+' | '-')
            {
            expr.update(format=FS.op($op0.text))
            $py_expr::expr = expr = expr.nestRight(format=FS.lr)
            $py_expr::nest = expr.nestRight
            }
            multiplicativeExpression
        )*
    ;


multiplicativeExpression
scope py_expr;
@init {
    $py_expr::expr = expr = $py_expr[PREV]::nest(format=FS.lr)
    $py_expr::nest = nest = expr.nestLeft
}
    :   unaryExpression
        (   op0=( '*' | '/' | '%' )
            {
            expr.update(format=FS.op($op0.text))
            $py_expr::expr = expr = expr.nestRight(format=FS.lr)
            $py_expr::nest = expr.nestRight
            }
            unaryExpression
        )*
    ;


unaryExpression
scope py_expr;
@init {
    $py_expr::expr = expr = $py_expr[PREV]::nest(format=FS.lr)
    $py_expr::nest = nest = expr.nestLeft
}
    :   '+'
        {
        expr.update(format='+'+FS.lr)
        $py_expr::nest = expr.nestRight
        }
        unaryExpression

    |   '-'
        {
        expr.update(format='-'+FS.lr)
        $py_expr::nest = expr.nestRight
        }
        unaryExpression

    |   '++'
        {
        ##//TODO:  add mutable values when ++ and -- appear within assignments (py2)
        ##// and nonlocal statement (py3)
        expr.update(format=FS.l + ' += 1')
        }
        unaryExpression

    |   '--'
        {
        expr.update(format=FS.l + ' -= 1')
        }
        unaryExpression

    |   unaryExpressionNotPlusMinus
    ;


unaryExpressionNotPlusMinus
scope py_expr;
@init {
    $py_expr::expr = expr = $py_expr[PREV]::nest(format=FS.lr)
    $py_expr::nest = nest = expr.nestLeft
}
    :   '~'
        {
        expr.update(format='~'+FS.lr)
        $py_expr::nest = expr.nestRight
        }
        unaryExpression

    |   '!'
        {
        expr.update(format='not '+FS.lr)
        $py_expr::nest = expr.nestRight
        }
        unaryExpression

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
    identLevel = 0
    subId = lambda:'ident:' + str(identLevel)

    expr = $py_expr[PREV]::nest(format=FS.lr, rule=ruleName())
    $py_expr::expr = expr
    $py_expr::nest = nest = expr.nestLeft
}
    :   parExpression // handled in rule

    |   'this' ('.' Ident)* identifierSuffix?

    |   'super' superSuffix

    |   literal
        { expr.update(left=$literal.text, rule=ruleName('literal')) }

    |   'new' creator

    |   id0=Ident
        {
        expr = nest(format=FS.lr, left=$id0.text, rule=ruleName(subId()))
        nest = expr.nestRight
        }
        ('.' id1=Ident
            {
            identLevel += 1
            expr = nest(format='.'+FS.lr, left=$id1.text, rule=ruleName(subId()))
            nest = expr.nestRight
            }
        )*
        {
        $py_expr::expr = expr
        $py_expr::nest = expr.nestRight
        }
        identifierSuffix?

    |   primitiveType ('[' ']')* '.' 'class'
    |   'void' '.' 'class'
    ;


identifierSuffix
scope py_expr;
@init {
    expr = $py_expr[PREV]::nest(format=FS.l, rule=ruleName())
    $py_expr::expr = expr
    $py_expr::nest = expr.nestLeft
}
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
scope py_expr, py_type;
@init {
    expr = $py_expr[PREV]::nest(format=FS.lr, rule=ruleName())
    $py_expr::expr = expr
    $py_expr::nest = expr.nestRight
    def setLeft(v):
        expr.addType(v)
        expr.left = expr.type
    $py_type::add = setLeft
}
    :   nonWildcardTypeArguments createdName classCreatorRest
    |   createdName
        (arrayCreatorRest | classCreatorRest)
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
@after {
    if 0:print '# exit selector:', $selector.text
}
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
scope py_expr;
@init {
    expr = $py_expr[PREV]::nest(format=FS.args, rule=ruleName())
    $py_expr::expr = expr
    $py_expr::nest = expr.nestLeft
}
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


NullLiteral
    :   'null'
    ;

BooleanLiteral
    :   'true'
    |   'false'
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
