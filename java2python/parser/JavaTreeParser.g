/**
 * For more information see the head comment within the 'java.g' grammar file
 * that defines the input for this tree grammar.
 *
 * BSD licence
 *
 * Copyright (c) 2007-2008 by HABELITZ Software Developments
 *
 * All rights reserved.
 *
 * http://www.habelitz.com
 *
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 *  1. Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *  2. Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in the
 *     documentation and/or other materials provided with the distribution.
 *  3. The name of the author may not be used to endorse or promote products
 *     derived from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY HABELITZ SOFTWARE DEVELOPMENTS ('HSD') ``AS IS''
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL 'HSD' BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
 * OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
 * LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 * NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 */
tree grammar JavaTreeParser;

options {
    language=Python;
    backtrack=true;
    memoize=true;
    tokenVocab=Java;
    ASTLabelType=CommonTree;
}

@treeparser::header {
from java2python.sourcetypes import SimplePythonSourceStack
}

@treeparser::members {
# placeholder
}

javaSource[module]
    @init { self.source = SimplePythonSourceStack(module) }
    :   ^(JAVA_SOURCE annotationList packageDeclaration? importDeclaration* typeDeclaration*)
    ;

packageDeclaration
    :   ^(PACKAGE q0=qualifiedIdentifier)
         { self.source.onPackageDecl($q0.text) }
    ;

importDeclaration
    :   ^(IMPORT s0=STATIC? q0=qualifiedIdentifier d0=DOTSTAR?)
         { self.source.onImportDecl($q0.text, bool($s0), bool($d0)) }
    ;

typeDeclaration
    :   ^(CLASS m0=modifierList i0=IDENT t0=genericTypeParameterList? x0=extendsClause? p0=implementsClause?
          { klass = self.source.onClass($i0.text, $m0.modifiers, $x0.clauses, $p0.clauses) }
          classTopLevelScope
          { self.source.pop() }
        )

    |   ^(INTERFACE m1=modifierList i1=IDENT t1=genericTypeParameterList? x1=extendsClause?
          { self.source.onClass($i1.text, $m1.modifiers, $x1.clauses) }
          interfaceTopLevelScope
          { self.source.pop() }
        )

    |   ^(ENUM m2=modifierList i2=IDENT p2=implementsClause?
          { klass = self.source.onClass($i2.text, $m2.modifiers, ['EnumClass', ], $p2.clauses) }
          enumTopLevelScope
          { self.source.pop() }
        )

    |   ^(AT m3=modifierList i3=IDENT
          { klass = self.source.onAnnoType($i3.text, $m3.modifiers) }
          annotationTopLevelScope
          { self.source.pop() }
        )
    ;

extendsClause returns [clauses]
    @init {clauses = []}
    :   ^(EXTENDS_CLAUSE (t0=type { clauses.append($t0.value) })+)
    ;

implementsClause returns [clauses]
    @init {clauses = []}
    :   ^(IMPLEMENTS_CLAUSE (t0=type { clauses.append($t0.value) })+)
    ;

genericTypeParameterList
    :   ^(GENERIC_TYPE_PARAM_LIST genericTypeParameter+)
    ;

genericTypeParameter
    :   ^(IDENT bound?)
    ;

bound
    :   ^(EXTENDS_BOUND_LIST type+)
    ;

enumTopLevelScope
    @init { enums = [] }
    @after { self.source.onEnumScope(enums) }
    :   ^(ENUM_TOP_LEVEL_SCOPE (e0=enumConstant { enums.append($e0.decl) })+ classTopLevelScope?)
    ;

enumConstant returns [decl]
    @init { klass = None }
    @after {
        $decl=($i0.text, $a0.args)
        ##// if we didn't create a class for the scope
        ##// that means the scope is empty.  so we make an empty
        if not klass:
            klass = self.source.onEnum($i0.text, $a0.args)
        self.source.pop()

    }
    :   ^(i0=IDENT annotationList (a0=arguments)?
          ({ klass = self.source.onEnum($i0.text, $a0.args) } classTopLevelScope)?
        )
    ;

classTopLevelScope
    :   ^(CLASS_TOP_LEVEL_SCOPE classScopeDeclarations*)
    ;

classScopeDeclarations
    :   ^(CLASS_INSTANCE_INITIALIZER block)
    |   ^(CLASS_STATIC_INITIALIZER block)

    |   ^(FUNCTION_METHOD_DECL m0=modifierList genericTypeParameterList? t0=type i0=IDENT
          p0=formalParameterList arrayDeclaratorList? throwsClause?
          { self.source.onMethod($i0.text, $m0.modifiers, $p0.params) }
          block?
          { self.source.pop() }
        )

    |   ^(VOID_METHOD_DECL m1=modifierList genericTypeParameterList? i1=IDENT
          p1=formalParameterList throwsClause?
          { self.source.onMethod($i1.text, $m1.modifiers, $p1.params) }
          block?
          { self.source.pop() }
        )

    |   ^(VAR_DECLARATION m2=modifierList t2=type v2=variableDeclaratorList)
         {
         decls = $v2.decls
         for decl in decls:
            decl["type"] = $t2.value
         self.source.onVariables(decls)
         }

    |   ^(CONSTRUCTOR_DECL m3=modifierList genericTypeParameterList? p3=formalParameterList throwsClause?
          { self.source.onMethod("__init__", $m3.modifiers, $p3.params) }
          block
          { self.source.pop() }
        )
    |   typeDeclaration
    ;

interfaceTopLevelScope
    :   ^(INTERFACE_TOP_LEVEL_SCOPE interfaceScopeDeclarations*)
    ;

interfaceScopeDeclarations
    :   ^(FUNCTION_METHOD_DECL m0=modifierList genericTypeParameterList? t0=type i0=IDENT p0=formalParameterList arrayDeclaratorList? throwsClause?
          {
          self.source.onMethod($i0.text, $m0.modifiers, $p0.params)
          self.source.pop()
          }
        )
    |   ^(VOID_METHOD_DECL m1=modifierList genericTypeParameterList? i1=IDENT p1=formalParameterList throwsClause?
          {
          self.source.onMethod($i1.text, $m1.modifiers, $p1.params)
          self.source.pop()
          }
        )
    |   ^(VAR_DECLARATION modifierList type v2=variableDeclaratorList)
         { self.source.onVariables($v2.decls) }
    |   typeDeclaration
    ;

variableDeclaratorList returns [decls]
    @init { decls = [] }
    :   ^(VAR_DECLARATOR_LIST (v0=variableDeclarator { decls.append($v0.decl) } )+)
    ;

variableDeclarator returns [decl]
    @init { $decl = dict() }
    :   ^(VAR_DECLARATOR v0=variableDeclaratorId { $decl = $v0.decl }
          (vi0=variableInitializer { $decl["init"] = $vi0.exp } )?
         )
    ;

variableDeclaratorId returns [decl]
    @init { $decl = dict() }
    :   ^(i0=IDENT { $decl["id"] = $i0.text } (a0=arrayDeclaratorList { $decl["array"] = [a0] })?
        )
    ;
variableInitializer returns [exp]
    :   arrayInitializer
    |   expression { $exp = $expression.exp }
    ;

arrayDeclarator
    :   LBRACK RBRACK
    ;

arrayDeclaratorList
    :   ^(ARRAY_DECLARATOR_LIST ARRAY_DECLARATOR*)
    ;

arrayInitializer
    :   ^(ARRAY_INITIALIZER variableInitializer*)
    ;

throwsClause
    :   ^(THROWS_CLAUSE qualifiedIdentifier+)
    ;

modifierList returns [modifiers]
    @init { $modifiers = [] }
    :   ^(MODIFIER_LIST (m0=modifier { $modifiers.append($m0.value) })*)
    ;

modifier returns [value]
    :   PUBLIC { $value = $PUBLIC.text }
    |   PROTECTED { $value = $PROTECTED.text }
    |   PRIVATE { $value = $PRIVATE.text }
    |   STATIC { $value = $STATIC.text }
    |   ABSTRACT { $value = $ABSTRACT.text }
    |   NATIVE { $value = $NATIVE.text }
    |   SYNCHRONIZED { $value = $SYNCHRONIZED.text }
    |   TRANSIENT { $value = $TRANSIENT.text }
    |   VOLATILE { $value = $VOLATILE.text }
    |   STRICTFP { $value = $STRICTFP.text }
    |   localModifier { $value = $localModifier.value }
    ;

localModifierList returns [modifiers]
    @init { $modifiers = [] }
    :   ^(LOCAL_MODIFIER_LIST (m0=localModifier { $modifiers.append($m0.value) })*)
    ;

localModifier returns [value]
    :   FINAL { $value = $FINAL.text }
    |   annotation { $value = $annotation.value }
    ;

type returns [value]
    :   ^(TYPE
          (p0=primitiveType {$value = $p0.text} | q0=qualifiedTypeIdent {$value = $q0.text})
          arrayDeclaratorList?
        )
    ;

qualifiedTypeIdent
    :   ^(QUALIFIED_TYPE_IDENT typeIdent+)
    ;

typeIdent
    :   ^(IDENT genericTypeArgumentList?)
    ;

primitiveType
    :   BOOLEAN
    |   CHAR
    |   BYTE
    |   SHORT
    |   INT
    |   LONG
    |   FLOAT
    |   DOUBLE
    ;

genericTypeArgumentList
    :   ^(GENERIC_TYPE_ARG_LIST genericTypeArgument+)
    ;

genericTypeArgument
    :   type
    |   ^(QUESTION genericWildcardBoundType?)
    ;

genericWildcardBoundType
    :   ^(EXTENDS type)
    |   ^(SUPER type)
    ;

formalParameterList returns [params]
    @init {params = []}
    :   ^(FORMAL_PARAM_LIST (p0=formalParameterStandardDecl {params.append($p0.value)})*
          formalParameterVarargDecl?
        )
    ;

formalParameterStandardDecl returns [value]
    :   ^(FORMAL_PARAM_STD_DECL localModifierList t0=type v0=variableDeclaratorId)
         {
         $value = $v0.decl
         $value["type"] = $t0.text
         }
    ;

formalParameterVarargDecl
    :   ^(FORMAL_PARAM_VARARG_DECL localModifierList type variableDeclaratorId)
    ;

qualifiedIdentifier
    :   IDENT
    |   ^(DOT qualifiedIdentifier IDENT)
    ;

annotationList
    :   ^(ANNOTATION_LIST annotation*)
    ;

annotation returns [value]
    @init { initializers = [] }
    :   ^(AT q0=qualifiedIdentifier (a0=annotationInit { initializers.append($a0.exp) })?) { $value = [$q0.text, initializers] }
    ;

annotationInit returns [exp]
    :   ^(ANNOTATION_INIT_BLOCK (a0=annotationInitializers {$exp = $a0.initializers }))
    ;

annotationInitializers returns [initializers]
    @init { $initializers = [] }
    :   ^(ANNOTATION_INIT_KEY_LIST    (a0=annotationInitializer  { $initializers.append($a0.value) })+)
    |   ^(ANNOTATION_INIT_DEFAULT_KEY (a1=annotationElementValue { $initializers = [$a1.exp] }))
    ;

annotationInitializer returns [value]
    :   ^(i0=IDENT v0=annotationElementValue) { $value = [$i0.text, $v0.exp] }
    ;

annotationElementValue returns [exp]
    :   ^(ANNOTATION_INIT_ARRAY_ELEMENT annotationElementValue*)
    |   annotation // TODO
    |   expression { $exp = $expression.exp }
    ;

annotationTopLevelScope
    :   ^(ANNOTATION_TOP_LEVEL_SCOPE annotationScopeDeclarations*)
    ;

annotationScopeDeclarations
    :   ^(ANNOTATION_METHOD_DECL m0=modifierList t0=type i0=IDENT (d0=annotationDefaultValue)? )
          {
          m = self.source.onAnnotationMethod($i0.text, $m0.modifiers, $d0.value)
          }
    |   ^(VAR_DECLARATION modifierList type variableDeclaratorList)
    |   typeDeclaration
    ;

annotationDefaultValue returns[value]
    :   ^(DEFAULT (v0=annotationElementValue {$value = $v0.text }))
    ;

block
    :   ^(BLOCK_SCOPE blockStatement*)
    ;

blockStatement
    :   localVariableDeclaration
    |   typeDeclaration
    |   statement
    ;

localVariableDeclaration
    :   ^(VAR_DECLARATION m0=localModifierList t0=type v0=variableDeclaratorList)
         { self.source.onVariables($v0.decls) }
    ;

statement
    :   block
    |   ^(ASSERT expression expression?)
    |   ^(IF parenthesizedExpression statement statement?)
    |   ^(FOR forInit forCondition forUpdater statement)
    |   ^(FOR_EACH localModifierList type IDENT expression statement)
    |   ^(WHILE parenthesizedExpression statement)
    |   ^(DO statement parenthesizedExpression)
    |   ^(TRY block catches? block?)  // The second optional block is the optional finally block.
    |   ^(SWITCH parenthesizedExpression switchBlockLabels)
    |   ^(SYNCHRONIZED parenthesizedExpression block)
    |   ^(RETURN (ex0=expression { self.source.onReturn($ex0.exp) })?)
    |   ^(THROW expression)
    |   ^(BREAK IDENT?)
    |   ^(CONTINUE IDENT?)
    |   ^(LABELED_STATEMENT IDENT statement)
    |   (x0=expression { self.source.current.addSource($x0.exp or "") })
    |   SEMI // Empty statement.
    ;

catches
    :   ^(CATCH_CLAUSE_LIST catchClause+)
    ;

catchClause
    :   ^(CATCH formalParameterStandardDecl block)
    ;

switchBlockLabels
    :   ^(SWITCH_BLOCK_LABEL_LIST switchCaseLabel* switchDefaultLabel? switchCaseLabel*)
    ;

switchCaseLabel
    :   ^(CASE expression blockStatement*)
    ;

switchDefaultLabel
    :   ^(DEFAULT blockStatement*)
    ;

forInit
    :   ^(FOR_INIT (localVariableDeclaration | expression*)?)
    ;

forCondition
    :   ^(FOR_CONDITION expression?)
    ;

forUpdater
    :   ^(FOR_UPDATE expression*)
    ;

parenthesizedExpression returns [exp]
    :   ^(PARENTESIZED_EXPR e0=expression { $exp = "(" + ($e0.exp or "") + ")" })
    ;

expression returns [exp]
    :   ^(EXPR e0=expr { $exp = $e0.exp } )
    ;

expr returns [exp]
    :   ^(ASSIGN left=expr right=expr) { self.source.onAssign("+", left, right) }
    |   ^(PLUS_ASSIGN expr expr)
    |   ^(MINUS_ASSIGN expr expr)
    |   ^(STAR_ASSIGN expr expr)
    |   ^(DIV_ASSIGN expr expr)
    |   ^(AND_ASSIGN expr expr)
    |   ^(OR_ASSIGN expr expr)
    |   ^(XOR_ASSIGN expr expr)
    |   ^(MOD_ASSIGN expr expr)
    |   ^(BIT_SHIFT_RIGHT_ASSIGN expr expr)
    |   ^(SHIFT_RIGHT_ASSIGN expr expr)
    |   ^(SHIFT_LEFT_ASSIGN expr expr)
    |   ^(QUESTION expr expr expr)
    |   ^(LOGICAL_OR expr expr)
    |   ^(LOGICAL_AND expr expr)
    |   ^(OR expr expr)
    |   ^(XOR expr expr)
    |   ^(AND expr expr)
    |   ^(EQUAL expr expr)
    |   ^(NOT_EQUAL expr expr)
    |   ^(INSTANCEOF expr type)
    |   ^(LESS_OR_EQUAL expr expr)
    |   ^(GREATER_OR_EQUAL expr expr)
    |   ^(BIT_SHIFT_RIGHT expr expr)
    |   ^(SHIFT_RIGHT expr expr)
    |   ^(GREATER_THAN expr expr)
    |   ^(SHIFT_LEFT expr expr)
    |   ^(LESS_THAN expr expr)
    |   ^(PLUS left=expr right=expr) { $exp = ("\%s + \%s" \% (left, right)) }
    |   ^(MINUS expr expr)
    |   ^(STAR left=expr right=expr) { $exp = ("\%s * \%s" \% (left, right)) }
    |   ^(DIV expr expr)
    |   ^(MOD expr expr)
    |   ^(UNARY_PLUS expr)
    |   ^(UNARY_MINUS expr)
    |   ^(PRE_INC expr)
    |   ^(PRE_DEC expr)
    |   ^(POST_INC expr)
    |   ^(POST_DEC expr)
    |   ^(NOT expr)
    |   ^(LOGICAL_NOT expr)
    |   ^(CAST_EXPR type expr)
    |   p0=primaryExpression { $exp = $p0.exp }
    ;

primaryExpression returns [exp]
    @init { $exp = "" }
    :   ^(  DOT
            (   p0=primaryExpression { $exp += $p0.exp + "." }
                (   i0=IDENT { $exp += self.source.altName($i0.text) }
                |   THIS
                |   SUPER
                |   innerNewExpression
                |   CLASS
                )
            |   primitiveType CLASS
            |   VOID CLASS
            )
        )
    |   parenthesizedExpression { $exp = $parenthesizedExpression.exp }
    |   IDENT { $exp = self.source.altName($IDENT.text) }
    |   ^(METHOD_CALL p0=primaryExpression genericTypeArgumentList? a0=arguments
         { $exp = self.source.makeMethodExpr($p0.exp, $a0.args) }
        )
    |   explicitConstructorCall
    |   ^(ARRAY_ELEMENT_ACCESS primaryExpression expression)
    |   literal { $exp = $literal.value }
    |   newExpression { $exp = $newExpression.exp }
    |   THIS
    |   arrayTypeDeclarator
    |   SUPER
    ;

explicitConstructorCall
    :   ^(THIS_CONSTRUCTOR_CALL genericTypeArgumentList? arguments)
    |   ^(SUPER_CONSTRUCTOR_CALL primaryExpression? genericTypeArgumentList? arguments)
    ;

arrayTypeDeclarator
    :   ^(ARRAY_DECLARATOR (arrayTypeDeclarator | qualifiedIdentifier | primitiveType))
    ;

newExpression returns [exp]
    :   ^(  STATIC_ARRAY_CREATOR
            (   t0=primitiveType newArrayConstruction
            |   genericTypeArgumentList? q0=qualifiedTypeIdent newArrayConstruction
            )
            { $exp = ($q0.text, "") }
        )
    |   ^(CLASS_CONSTRUCTOR_CALL genericTypeArgumentList? q1=qualifiedTypeIdent
          a1=arguments classTopLevelScope?
          { $exp = ($q1.text, $a1.args) }
        )
    ;

innerNewExpression // something like 'InnerType innerType = outer.new InnerType();'
    :   ^(CLASS_CONSTRUCTOR_CALL genericTypeArgumentList? IDENT arguments classTopLevelScope?)
    ;

newArrayConstruction
    :   arrayDeclaratorList arrayInitializer
    |   expression+ arrayDeclaratorList?
    ;

arguments returns [args]
    @init {args = []}
    :   ^(ARGUMENT_LIST (ex0=expression { args.append($ex0.exp) })*)
    ;

literal returns [value]
    :   HEX_LITERAL { $value = $HEX_LITERAL.text }
    |   OCTAL_LITERAL { $value = $OCTAL_LITERAL.text }
    |   d0=DECIMAL_LITERAL
        {
        ## this rule does not fire; decimals are sent to the float literal
        $value = $d0.text
        if $value.startswith("."):$value = "0" + $value
        if $value.endswith(("f", "d")):$value = $value[:-1]
        if $value.endswith(("l", "L")):$value = $value[:-1] + "L"
        }

    |   f0=FLOATING_POINT_LITERAL
        {
        $value = $f0.text
        if $value.startswith("."):$value = "0" + $value
        if $value.endswith(("f", "d")):$value = $value[:-1]
        }
    |   CHARACTER_LITERAL { $value = $CHARACTER_LITERAL.text }
    |   STRING_LITERAL { $value = $STRING_LITERAL.text }
    |   TRUE { $value = 'True' }
    |   FALSE { $value = 'False' }
    |   NULL { $value = 'None' }
    ;
