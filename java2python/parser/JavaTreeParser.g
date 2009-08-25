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
superClass=LocalTreeParser;
}


@treeparser::header {
from java2python import expression as ex
from java2python import parameter as px
from java2python.parser.local import LocalTreeParser
}


@treeparser::members {
# placeholder
}


javaSource[module]
    @init  { self.beginJavaSource(module) }
    @after { self.endJavaSource() }
    :   ^(JAVA_SOURCE annotationList packageDeclaration? importDeclaration* typeDeclaration*)
    ;


packageDeclaration
    :   ^(PACKAGE qualifiedIdentifier)
    ;


importDeclaration
    :   ^(IMPORT STATIC? qualifiedIdentifier DOTSTAR?)
    ;


typeDeclaration
    @init  { self.beginTypeDeclaration() }
    @after {
        self.commentHandler($start)
        self.endTypeDeclaration()
    }
    :   ^(CLASS
          md0=modifierList { self.setModifiers($md0.values) }
          id0=IDENT { self.setIdent(ident=$id0.text) }
          genericTypeParameterList?
          extendsClause?
          implementsClause?
          classTopLevelScope
        )

    |   ^(INTERFACE modifierList
          id1=IDENT
          genericTypeParameterList?
          extendsClause?
          interfaceTopLevelScope
        )

    |   ^(ENUM
          modifierList
          IDENT
          implementsClause?
          enumTopLevelScope
        )

    |   ^(AT
          modifierList
          IDENT
          annotationTopLevelScope
        )
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
    @init  { self.beginClassScopeDecls() }
    @after { self.endClassScopeDecls()   }

    :   ^(CLASS_INSTANCE_INITIALIZER block)

    |   ^(CLASS_STATIC_INITIALIZER block)

    |   ^(FUNCTION_METHOD_DECL
          modifierList
          genericTypeParameterList?
          type
          IDENT
          formalParameterList
          arrayDeclaratorList?
          throwsClause?
          block?)

    |   ^(VOID_METHOD_DECL
          { self.beginVoidMethodDecl() }
          md0=modifierList { self.setModifiers($md0.values) }
          genericTypeParameterList?
          id0=IDENT {self.setIdent(ident=$id0.text) }
          fp0=formalParameterList { self.setParameters($fp0.values) }
          throwsClause?
          block?
          { self.endVoidMethodDecl() }
        )

    |   ^(VAR_DECLARATION
          md1=modifierList
          tp1=type
          vd1=variableDeclaratorList
          { self.setVarDecls($vd1.values, $tp1.value, $md1.values) }
        )

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
                         // Interface constant declarations have been switched to variable
                         // declarations by 'java.g'; the parser has already checked that
                         // there's an obligatory initializer.
    |   ^(VAR_DECLARATION modifierList type variableDeclaratorList)
    |   typeDeclaration
    ;

variableDeclaratorList returns [values]
    @init { $values = [] }
    :   ^(VAR_DECLARATOR_LIST (vd0=variableDeclarator { $values.append($vd0.value) } )+)
    ;

variableDeclarator returns [value]
    @init { $value = px() }
    :   ^(VAR_DECLARATOR
          vd0=variableDeclaratorId { $value.update(id=$vd0.value) }
          (vi0=variableInitializer { $value.update(init=$vi0.value) })?
         )
    ;

variableDeclaratorId returns [value]
    @init { $value = ex(format="${left}") }
    :   ^(IDENT { $value["left"] = $IDENT.text }
          (arrayDeclaratorList { $value.update(right="[]", format="${left} = ${right}", array=True) })?
        )
    ;

variableInitializer returns [value]
    @init { $value = ex(format="${left}") }
    :   ai0=arrayInitializer { $value.update(left=$ai0.value) }
    |   ex0=expression       { $value.update(left=$ex0.value) }
    ;

arrayDeclarator
    :   LBRACK RBRACK
    ;

arrayDeclaratorList
    :   ^(ARRAY_DECLARATOR_LIST ARRAY_DECLARATOR*)
    ;

arrayInitializer returns [value]
    @init { $value = ex() }
    :   ^(ARRAY_INITIALIZER variableInitializer*)
    ;

throwsClause
    :   ^(THROWS_CLAUSE qualifiedIdentifier+)
    ;

modifierList returns [values]
    @init { $values = [] }
    :   ^(MODIFIER_LIST (md0=modifier { values.append($md0.text) })*)
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

localModifierList returns [values]
    @init { $values = [] }
    :   ^(LOCAL_MODIFIER_LIST (md0=localModifier { values.append($md0.value) })*)
    ;

localModifier returns [value]
    :   FINAL { $value = 'final' }
    |   an0=annotation { $value = $an0.value }
    ;

type returns [value]
    @init { $value = ex() }
    :   ^(TYPE (primitiveType |
                qualifiedTypeIdent
               )
          arrayDeclaratorList?
        )
    ;

qualifiedTypeIdent returns [value]
    :   ^(QUALIFIED_TYPE_IDENT (ti0=typeIdent { $value = $ti0.value })+)
    ;

typeIdent returns [value]
    :   ^(id0=IDENT genericTypeArgumentList?)
          { $value = $id0.text }
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

genericTypeArgumentList returns [values]
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

formalParameterList returns [values]
    @init { $values = [] }
    :   ^(FORMAL_PARAM_LIST
          (fp0=formalParameterStandardDecl { values.append($fp0.value) })*
          (vd0=formalParameterVarargDecl   { values.append($vd0.value) })?
        )
    ;

formalParameterStandardDecl returns [value]
    :   ^(FORMAL_PARAM_STD_DECL
          lm0=localModifierList
          tp0=type
          vd0=variableDeclaratorId
        ) { $value = px($vd0.value, $tp0.text, $lm0.values, variadic=False) }
    ;


formalParameterVarargDecl returns [value]
    :   ^(FORMAL_PARAM_VARARG_DECL
          lm0=localModifierList
          tp0=type
          vd0=variableDeclaratorId
        ) { $value = px($vd0.value, $tp0.text, $lm0.values, variadic=True) }
    ;


qualifiedIdentifier returns [value]
    :   IDENT { $value = ex(self.altId($text), format="${left}") }
    |   ^(DOT
          qi0=qualifiedIdentifier
          IDENT
          { $value = ex($qi0.value, self.altId($IDENT.text), "${left}.${right}") }
        )
    ;


// ANNOTATIONS

annotationList
    :   ^(ANNOTATION_LIST annotation*)
    ;

annotation returns [value]
    :   ^(AT
          qi0=qualifiedIdentifier { $value = qi0.value }
          annotationInit?
        )
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
    |   st0=statement { self.setExpression($st0.value) }
    ;

localVariableDeclaration
    :   ^(VAR_DECLARATION localModifierList type variableDeclaratorList)
    ;


statement returns [value]
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
    |   ex0=expression { $value = $ex0.value }
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

parenthesizedExpression returns [value]
    :   ^(PARENTESIZED_EXPR ex0=expression { $value = ex($ex0.value, format="(${left})") })
    ;

expression returns [value]
    :   ^(EXPR ex0=expr { $value = $ex0.value })
    ;

expr returns [value]
    @init { $value = ex() }
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
    |   pe0=primaryExpression { $value = $pe0.value }
    ;

primaryExpression returns [value]
    @init { $value = ex() }
    :   ^(  DOT
            (   p0=primaryExpression
                { $value = ex($p0.value, format="${left}.${right}") }
                (   IDENT { $value["right"] = ex($IDENT.text, format="${left}") }
                |   THIS  { $value["format"] = "${left}" } // broken
                |   SUPER
                 { $value["format"] = "${left}"
                   $value["left"] = ex($value["left"], "", "super(${left}, self)")
                 }
                |ne0=innerNewExpression { $value = $ne0.value }
                |   CLASS { $value["right"] = ex("__class__", "", "${left}") }
                )
            |   pt0=primitiveType CLASS { $value = ex($pt0.text, "__class__", "${left}.${right}") }
            |   VOID CLASS { $value = ex("None", "__class__", "${left}.${right}") }
            )
        )

    |   parenthesizedExpression { $value = $parenthesizedExpression.value }

    |   IDENT { $value = ex($IDENT.text, format="${left}")  }

    |   ^(METHOD_CALL
          p0=primaryExpression
          genericTypeArgumentList?
          a0=arguments
          { $value = ex($p0.value, $a0.values, "${left}(${right})") }
        )

    |   ec0=explicitConstructorCall { $value = $ec0.value }

    |   ^(ARRAY_ELEMENT_ACCESS
          p0=primaryExpression
          e0=expression
          { $value = ex($p0.value, $e0.value, "${left}[${right}]") }
        )

    |   literal { $value = $literal.value }

    |   newExpression { $value = $newExpression.value }

    |   THIS { $value = ex("self", format="${left}") }

    |   arrayTypeDeclarator

    |   SUPER { $value = ex(self.topParentName, format="super(${left}, self)") }
    ;


explicitConstructorCall returns [value]
    :   ^(THIS_CONSTRUCTOR_CALL genericTypeArgumentList? arguments)
    |   ^(SUPER_CONSTRUCTOR_CALL primaryExpression? genericTypeArgumentList? arguments)
    ;

arrayTypeDeclarator
    :   ^(ARRAY_DECLARATOR (arrayTypeDeclarator | qualifiedIdentifier | primitiveType))
    ;

newExpression returns [value]
    :   ^(STATIC_ARRAY_CREATOR
          ( tp0=primitiveType ac0=newArrayConstruction
            { $value = self.makeArrayCreator($tp0.text, $ac0.value) }
          | gt1=genericTypeArgumentList? tp1=qualifiedTypeIdent ac1=newArrayConstruction
            { $value = self.makeArrayCreator($tp1.value, $ac1.value, $gt1.values) }
          )
        )
    |   ^(CLASS_CONSTRUCTOR_CALL genericTypeArgumentList? q1=qualifiedTypeIdent
          a1=arguments classTopLevelScope?
          { $value = ex($q1.value, $a1.values, "${left}(${right})") }
        )
    ;


// something like 'InnerType innerType = outer.new InnerType();'
innerNewExpression returns [value]
    @init { value = None }
    :   ^(CLASS_CONSTRUCTOR_CALL genericTypeArgumentList? IDENT arguments classTopLevelScope?)
    ;

newArrayConstruction returns [value]
    :   arrayDeclaratorList arrayInitializer
    |   expression+ arrayDeclaratorList?
    ;


arguments returns [values]
    @init { $values, format = "", "${right}" }
    :   ^(ARGUMENT_LIST (ex0=expression
          { $values, format = ex($values, $ex0.value, format), "${left}, ${right}" })*
        )
    ;


literal returns [value]
    :   HEX_LITERAL { $value = $text }
    |   OCTAL_LITERAL { $value = $text }
    |   DECIMAL_LITERAL { $value = self.formatFloatLiteral($text) }
    |   FLOATING_POINT_LITERAL { $value = self.formatFloatLiteral($text) }
    |   CHARACTER_LITERAL { $value = $text }
    |   STRING_LITERAL { $value = $text }
    |   TRUE { $value = 'True' }
    |   FALSE { $value = 'False' }
    |   NULL { $value = 'None' }
    ;
