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
options {language=Python; backtrack=true; memoize=true; tokenVocab=Java; ASTLabelType=CommonTree;}

@treeparser::header {
from java2python.lib.sourcestack import SimplePythonSourceStack
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

    |   ^(ENUM modifierList IDENT implementsClause? enumTopLevelScope)
    |   ^(AT modifierList IDENT annotationTopLevelScope)
    ;

extendsClause
returns [clauses]
    @init {clauses = []}
    :   ^(EXTENDS_CLAUSE (t0=type { clauses.append($t0.value) })+)
    ;

implementsClause
returns [clauses]
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
    :   ^(ENUM_TOP_LEVEL_SCOPE enumConstant+ classTopLevelScope?)
    ;

enumConstant
    :   ^(IDENT annotationList arguments? classTopLevelScope?)
    ;


classTopLevelScope
    :   ^(CLASS_TOP_LEVEL_SCOPE classScopeDeclarations*)
    ;

// MARK
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
         { self.source.onVariables($v2.decls) }

    |   ^(CONSTRUCTOR_DECL
            modifierList
            genericTypeParameterList?
            formalParameterList
            throwsClause?
            block)
    |   typeDeclaration
    ;

interfaceTopLevelScope
    :   ^(INTERFACE_TOP_LEVEL_SCOPE interfaceScopeDeclarations*)
    ;

interfaceScopeDeclarations
    :   ^(FUNCTION_METHOD_DECL modifierList genericTypeParameterList? type IDENT formalParameterList arrayDeclaratorList? throwsClause?)
    |   ^(VOID_METHOD_DECL modifierList genericTypeParameterList? IDENT formalParameterList throwsClause?)
    |   ^(VAR_DECLARATION modifierList type variableDeclaratorList)
    |   typeDeclaration
    ;

variableDeclaratorList
returns [decls]
    @init { decls = [] }
    :   ^(VAR_DECLARATOR_LIST (v0=variableDeclarator { decls.append($v0.decl) } )+)
    ;

variableDeclarator
returns [decl]
    @init { $decl = dict() }
    :   ^(VAR_DECLARATOR v0=variableDeclaratorId { $decl = $v0.decl }
          (vi0=variableInitializer { $decl["init"] = $vi0.text } )?
         )
    ;

variableDeclaratorId
returns [decl]
    @init { $decl = dict() }
    :   ^(i0=IDENT { $decl["id"] = $i0.text } (a0=arrayDeclaratorList { $decl["array"] = [a0] })?
        )
    ;

variableInitializer
    :   arrayInitializer
    |   expression
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

modifierList
returns [modifiers]
    @init {modifiers = []}
    :   ^(MODIFIER_LIST (m0=modifier {modifiers.append($m0.text)})*)
    ;

modifier
    :   PUBLIC
    |   PROTECTED
    |   PRIVATE
    |   STATIC
    |   ABSTRACT
    |   NATIVE
    |   SYNCHRONIZED
    |   TRANSIENT
    |   VOLATILE
    |   STRICTFP
    |   localModifier
    ;

localModifierList
    :   ^(LOCAL_MODIFIER_LIST localModifier*)
    ;

localModifier
    :   FINAL
    |   annotation
    ;

type
returns [value]
    :   ^(TYPE (p0=primitiveType {$value = $p0.text} |
                q0=qualifiedTypeIdent {$value = $q0.text}) arrayDeclaratorList?)
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

formalParameterList
returns [params]
    @init {params = []}
    :   ^(FORMAL_PARAM_LIST (p0=formalParameterStandardDecl {params.append($p0.value)})*
          formalParameterVarargDecl?
        )
    ;

formalParameterStandardDecl
returns [value]
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

// ANNOTATIONS

annotationList
    :   ^(ANNOTATION_LIST annotation*)
    ;

annotation
    :   ^(AT qualifiedIdentifier annotationInit?)
    ;

annotationInit
    :   ^(ANNOTATION_INIT_BLOCK annotationInitializers)
    ;

annotationInitializers
    :   ^(ANNOTATION_INIT_KEY_LIST annotationInitializer+)
    |   ^(ANNOTATION_INIT_DEFAULT_KEY annotationElementValue)
    ;

annotationInitializer
    :   ^(IDENT annotationElementValue)
    ;

annotationElementValue
    :   ^(ANNOTATION_INIT_ARRAY_ELEMENT annotationElementValue*)
    |   annotation
    |   expression
    ;

annotationTopLevelScope
    :   ^(ANNOTATION_TOP_LEVEL_SCOPE annotationScopeDeclarations*)
    ;

annotationScopeDeclarations
    :   ^(ANNOTATION_METHOD_DECL modifierList type IDENT annotationDefaultValue?)
    |   ^(VAR_DECLARATION modifierList type variableDeclaratorList)
    |   typeDeclaration
    ;

annotationDefaultValue
    :   ^(DEFAULT annotationElementValue)
    ;

// STATEMENTS / BLOCKS

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
        {v = self.source.onVariables($v0.decls) }
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
    |   ^(RETURN expression?)
    |   ^(THROW expression)
    |   ^(BREAK IDENT?)
    |   ^(CONTINUE IDENT?)
    |   ^(LABELED_STATEMENT IDENT statement)
    |   expression
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

// EXPRESSIONS

parenthesizedExpression
    :   ^(PARENTESIZED_EXPR expression)
    ;

expression
    :   ^(EXPR expr)
    ;

expr
returns [exp]
    @init { exp = None }
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
    |   ^(PLUS expr expr)
    |   ^(MINUS expr expr)
    |   ^(STAR expr expr)
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

primaryExpression
returns [exp]
    :   ^(  DOT
            (   primaryExpression
                (   IDENT
                |   THIS
                |   SUPER
                |   innerNewExpression
                |   CLASS
                )
            |   primitiveType CLASS
            |   VOID CLASS
            )
        )
    |   parenthesizedExpression
    |   IDENT { $exp = $IDENT.text }
    |   ^(METHOD_CALL primaryExpression genericTypeArgumentList? arguments)
    |   explicitConstructorCall
    |   ^(ARRAY_ELEMENT_ACCESS primaryExpression expression)
    |   literal { $exp = $literal.text }
    |   newExpression
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

newExpression
    :   ^(  STATIC_ARRAY_CREATOR
            (   primitiveType newArrayConstruction
            |   genericTypeArgumentList? qualifiedTypeIdent newArrayConstruction
            )
        )
    |   ^(CLASS_CONSTRUCTOR_CALL genericTypeArgumentList? qualifiedTypeIdent arguments classTopLevelScope?)
    ;

innerNewExpression // something like 'InnerType innerType = outer.new InnerType();'
    :   ^(CLASS_CONSTRUCTOR_CALL genericTypeArgumentList? IDENT arguments classTopLevelScope?)
    ;

newArrayConstruction
    :   arrayDeclaratorList arrayInitializer
    |   expression+ arrayDeclaratorList?
    ;

arguments
    :   ^(ARGUMENT_LIST expression*)
    ;

literal
    :   HEX_LITERAL
    |   OCTAL_LITERAL
    |   DECIMAL_LITERAL
    |   FLOATING_POINT_LITERAL
    |   CHARACTER_LITERAL
    |   STRING_LITERAL
    |   TRUE
    |   FALSE
    |   NULL
    ;
