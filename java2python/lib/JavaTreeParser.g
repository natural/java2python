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
    language = Python;
    backtrack = true;
    memoize = true;
    tokenVocab = Java;
    ASTLabelType = CommonTree;
}


@treeparser::header {
# placeholder
}

@treeparser::members {
# placeholder
}

// Starting point for parsing a Java file.
javaSource[M]
    :   ^(JAVA_SOURCE annotationList packageDeclaration? importDeclaration* typeDeclaration*)
    ;

packageDeclaration
    :   ^(PACKAGE qualifiedIdentifier)
    ;

importDeclaration
    :   ^(IMPORT STATIC? qualifiedIdentifier DOTSTAR?)
    ;

typeDeclaration
    :   ^(CLASS modifierList IDENT genericTypeParameterList? extendsClause? implementsClause? classTopLevelScope)
    |   ^(INTERFACE modifierList IDENT genericTypeParameterList? extendsClause? interfaceTopLevelScope)
    |   ^(ENUM modifierList IDENT implementsClause? enumTopLevelScope)
    |   ^(AT modifierList IDENT annotationTopLevelScope)
    ;

extendsClause // actually 'type' for classes and 'type+' for interfaces, but this has
              // been resolved by the parser grammar.
    :   ^(EXTENDS_CLAUSE type+)
    ;

implementsClause
    :   ^(IMPLEMENTS_CLAUSE type+)
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

classScopeDeclarations
    :   ^(CLASS_INSTANCE_INITIALIZER block)
    |   ^(CLASS_STATIC_INITIALIZER block)
    |   ^(FUNCTION_METHOD_DECL modifierList genericTypeParameterList? type IDENT formalParameterList arrayDeclaratorList? throwsClause? block?)
    |   ^(VOID_METHOD_DECL modifierList genericTypeParameterList? IDENT formalParameterList throwsClause? block?)
    |   ^(VAR_DECLARATION modifierList type variableDeclaratorList)
    |   ^(CONSTRUCTOR_DECL modifierList genericTypeParameterList? formalParameterList throwsClause? block)
    |   typeDeclaration
    ;

interfaceTopLevelScope
    :   ^(INTERFACE_TOP_LEVEL_SCOPE interfaceScopeDeclarations*)
    ;

interfaceScopeDeclarations
    :   ^(FUNCTION_METHOD_DECL modifierList genericTypeParameterList? type IDENT formalParameterList arrayDeclaratorList? throwsClause?)
    |   ^(VOID_METHOD_DECL modifierList genericTypeParameterList? IDENT formalParameterList throwsClause?)
                         // Interface constant declarations have been switched to variable
                         // declarations by 'java.g'; the parser has already checked that
                         // there's an obligatory initializer.
    |   ^(VAR_DECLARATION modifierList type variableDeclaratorList)
    |   typeDeclaration
    ;

variableDeclaratorList
    :   ^(VAR_DECLARATOR_LIST variableDeclarator+)
    ;

variableDeclarator
    :   ^(VAR_DECLARATOR variableDeclaratorId variableInitializer?)
    ;

variableDeclaratorId
    :   ^(IDENT arrayDeclaratorList?)
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
    :   ^(MODIFIER_LIST modifier*)
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
    :   ^(TYPE (primitiveType | qualifiedTypeIdent) arrayDeclaratorList?)
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
    :   ^(FORMAL_PARAM_LIST formalParameterStandardDecl* formalParameterVarargDecl?)
    ;

formalParameterStandardDecl
    :   ^(FORMAL_PARAM_STD_DECL localModifierList type variableDeclaratorId)
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
    :   ^(VAR_DECLARATION localModifierList type variableDeclaratorList)
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
    :   ^(ASSIGN expr expr)
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
    |   primaryExpression
    ;

primaryExpression
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
    |   IDENT
    |   ^(METHOD_CALL primaryExpression genericTypeArgumentList? arguments)
    |   explicitConstructorCall
    |   ^(ARRAY_ELEMENT_ACCESS primaryExpression expression)
    |   literal
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
