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
from logging import warn
from java2python import expression as ex, parameter as px, formatFloatLiteral
from java2python.parser.local import LocalTreeParser
}


@treeparser::members {
# placeholder
}


javaSource[module]
    @init  { self.beginJavaSource(module) }
    @after { self.endJavaSource() }
    :   ^(JAVA_SOURCE
          annotationList
          packageDeclaration?
          importDeclaration*
          typeDeclaration*
        )
    ;


packageDeclaration
    :   ^(PACKAGE qi0=qualifiedIdentifier { self.addPackage($qi0.value) })
    ;


importDeclaration
    :   ^(IMPORT STATIC? qualifiedIdentifier DOTSTAR?)
    ;


typeDeclaration
    @after {  }
    :   ^(CLASS
          { self.beginClassDeclaration() }
          md0=modifierList { self.addModifiers($md0.values) }
          id0=IDENT { self.setIdent(ident=$id0.text) }
          genericTypeParameterList?
          (ec0=extendsClause { self.addBases($ec0.values) })?
          (ic0=implementsClause { self.addBases($ic0.values) })?
          classTopLevelScope
          {
            self.commentHandler($start)
            self.endClassDeclaration()
          }
        )

    |   ^(INTERFACE
          { self.beginInterfaceDeclaration() }
          md0=modifierList { self.addModifiers($md0.values) }
          id0=IDENT { self.setIdent(ident=$id0.text) }
          genericTypeParameterList?
          (ec0=extendsClause { self.addBases($ec0.values) })?
          interfaceTopLevelScope
          {
            self.commentHandler($start)
            self.endInterfaceDeclaration()
          }
        )

    |   ^(ENUM
          { self.beginEnumerationDeclaration() }
          md0=modifierList { self.addModifiers($md0.values) }
          id0=IDENT { self.setIdent(ident=$id0.text) }
          (ic0=implementsClause { self.addBases($ic0.values) })?
          enumTopLevelScope
          {
            self.commentHandler($start)
            self.endEnumerationDeclaration()
          }
        )

    |   ^(AT
          { self.beginAnnotationDeclaration() }
          md0=modifierList { self.addModifiers($md0.values) }
          id0=IDENT { self.setIdent(ident=$id0.text) }
          annotationTopLevelScope
          {
            self.commentHandler($start)
            self.endAnnotationDeclration()
          }
        )
    ;


extendsClause returns [values]
    @init { $values = [] }
    :   ^(EXTENDS_CLAUSE (tp0=type { $values.append($tp0.value) })+)
    ;


implementsClause returns [values]
    @init { $values = [] }
    :   ^(IMPLEMENTS_CLAUSE (tp0=type { $values.append(tp0.value) })+)
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
    @init { args = None }
    :   ^(id0=IDENT
          annotationList
          (ag0=arguments { args = $ag0.values })?
          classTopLevelScope?
        )
        { self.addEnumValue($id0.text, args) }
    ;


classTopLevelScope
    :   ^(CLASS_TOP_LEVEL_SCOPE classScopeDeclarations*)
    ;


classScopeDeclarations
    @init  { self.beginClassScopeDecls() }
    @after { self.endClassScopeDecls() }

    :   ^(CLASS_INSTANCE_INITIALIZER block)

    |   ^(CLASS_STATIC_INITIALIZER block)

    |   ^(FUNCTION_METHOD_DECL

          { self.beginMethodDecl() }
          md0=modifierList { self.addModifiers($md0.values) }
          genericTypeParameterList?
          tp0=type { self.setType($tp0.value) }
          id0=IDENT { self.setIdent(ident=$id0.text) }
          fp0=formalParameterList { self.addParameters($fp0.values) }
          arrayDeclaratorList?
          throwsClause?
          block?
          {
           self.commentHandler($start)
           self.endMethodDecl()
          }
        )

    |   ^(VOID_METHOD_DECL
          { self.beginMethodDecl() }
          md0=modifierList { self.addModifiers($md0.values) }
          genericTypeParameterList?
          id0=IDENT { self.setIdent(ident=$id0.text) }
          fp0=formalParameterList { self.addParameters($fp0.values) }
          throwsClause?
          block?
          {
            self.commentHandler($start)
            self.setType("void")
            self.endMethodDecl()
          }
         )

    |   ^(VAR_DECLARATION
          md0=modifierList
          tp0=type
          vd0=variableDeclaratorList
          { self.addVariables($vd0.values, $tp0.value, $md0.values, cls=True) }
        )

    |   ^(CONSTRUCTOR_DECL
          { self.beginMethodDecl() }
          md0=modifierList { self.addModifiers($md0.values) }
          genericTypeParameterList?
          fp0=formalParameterList { self.addParameters($fp0.values) }
          throwsClause?
          block
          {
            self.commentHandler($start)
            self.setIdent("__init__")
            self.endMethodDecl()
          }
        )

    |   typeDeclaration
    ;


interfaceTopLevelScope
    :   ^(INTERFACE_TOP_LEVEL_SCOPE interfaceScopeDeclarations*)
    ;


interfaceScopeDeclarations
    @after { self.commentHandler($start) }
    :   ^(FUNCTION_METHOD_DECL
          { self.beginMethodDecl() }
          md0=modifierList { self.addModifiers($md0.values) }
          genericTypeParameterList?
          tp0=type { self.setType($tp0.value) }
          id0=IDENT { self.setIdent(ident=$id0.text) }
          fp0=formalParameterList { self.addParameters($fp0.values) }
          arrayDeclaratorList?
          throwsClause?
          { self.endMethodDecl() }
        )

    |   ^(VOID_METHOD_DECL
          { self.beginMethodDecl() }
          md0=modifierList { self.addModifiers($md0.values) }
          genericTypeParameterList?
          id0=IDENT { self.setIdent(ident=$id0.text) }
          fp0=formalParameterList { self.addParameters($fp0.values) }
          throwsClause?
          {
            self.setType("void")
            self.endMethodDecl()
          }
        )

    |   ^(VAR_DECLARATION
          md1=modifierList
          tp1=type
          vd1=variableDeclaratorList
          { self.addClassVariables($vd1.values, $tp1.value, $md1.values) }
        )

    |   typeDeclaration
    ;


variableDeclaratorList returns [values]
    @init { $values = [] }
    :   ^(VAR_DECLARATOR_LIST (vd0=variableDeclarator { $values.append($vd0.value) } )+)
    ;


variableDeclarator returns [value]
    :   ^(VAR_DECLARATOR
          (vd0=variableDeclaratorId
           { $value = ex(left=$vd0.value, format="${left}") })
          (vi0=variableInitializer
           { $value.update(right=$vi0.value, format="${left} = ${right}") })?
        )
    ;


variableDeclaratorId returns [value]
    @init { $value = ex(format="${left}") }
    :   ^(IDENT
           {
            expr = ex(self.altIdent($IDENT.text), format="${left}", rename=True, ident=$IDENT.text)
            $value.update(expr)
            }
          (arrayDeclaratorList { $value.update(format="${left}", array=True) })?
        )
    ;


variableInitializer returns [value]
    :   ai0=arrayInitializer { $value = ex($ai0.value, format="[${left}]") }
    |   ex0=expression       { $value = $ex0.value }
    ;


arrayDeclarator
    :   LBRACK RBRACK
    ;


arrayDeclaratorList returns [values] @init { $values = [] }
    :   ^(ARRAY_DECLARATOR_LIST (ARRAY_DECLARATOR { $values.append($text) })*)
    ;


arrayInitializer returns [value] @init { $value, format = "", "${right}" }
    :   ^(ARRAY_INITIALIZER
            (v0=variableInitializer
            { $value, format = ex($value, $v0.value, format), "${left}, ${right}" }
            )*
        )
    ;


throwsClause
    :   ^(THROWS_CLAUSE qualifiedIdentifier+)
    ;


modifierList returns [values]
    @init { $values = [] }
    :   ^(MODIFIER_LIST (md0=modifier { values.append($md0.value) })*)
    ;


modifier returns [value]
    @init { $value = ex(format="${left}") }
    :   PUBLIC            { $value.update(left=$text) }
    |   PROTECTED         { $value.update(left=$text) }
    |   PRIVATE           { $value.update(left=$text) }
    |   STATIC            { $value.update(left=$text) }
    |   ABSTRACT          { $value.update(left=$text) }
    |   NATIVE            { $value.update(left=$text) }
    |   SYNCHRONIZED      { $value.update(left=$text) }
    |   TRANSIENT         { $value.update(left=$text) }
    |   VOLATILE          { $value.update(left=$text) }
    |   STRICTFP          { $value.update(left=$text) }
    |   lm0=localModifier { $value = $lm0.value }
    ;


localModifierList returns [values]
    @init { $values = [] }
    :   ^(LOCAL_MODIFIER_LIST (md0=localModifier { values.append($md0.value) })*)
    ;


localModifier returns [value]
    :   FINAL { $value = "final" }
    |   an0=annotation { $value = $an0.value }
    ;


type returns [value]
    @init { $value = ex(format="${left}") }
    :   ^(TYPE
          (pt0=primitiveType { $value.update(left=self.renameType($pt0.text)) } |
           qt0=qualifiedTypeIdent { $value.update(left=self.renameType($qt0.value)) })
          (arrayDeclaratorList
           { $value["array"] = True }
          )?
        )
    ;


qualifiedTypeIdent returns [value]
    :   ^(QUALIFIED_TYPE_IDENT (ti0=typeIdent { $value = $ti0.value })+)
    ;


typeIdent returns [value]
    :   ^(id0=IDENT genericTypeArgumentList?) { $value = self.renameType($id0.text) }
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
          (fp0=formalParameterStandardDecl { $values.append($fp0.value) })*
          (vd0=formalParameterVarargDecl   { $values.append($vd0.value) })?
        )
    ;


formalParameterStandardDecl returns [value]
    :   ^(FORMAL_PARAM_STD_DECL
          lm0=localModifierList
          tp0=type
          vd0=variableDeclaratorId
        ) { $value = px($vd0.value["ident"], $tp0.text, $lm0.values, variadic=False) }
    ;


formalParameterVarargDecl returns [value]
    :   ^(FORMAL_PARAM_VARARG_DECL
          lm0=localModifierList
          tp0=type
          vd0=variableDeclaratorId
        ) { $value = px($vd0.value["ident"], $tp0.text, $lm0.values, variadic=True) }
    ;


qualifiedIdentifier returns [value]
    :   IDENT
        { $value = ex($IDENT.text, format="${left}", rename=True) }
    |   ^(DOT
          qi0=qualifiedIdentifier
          IDENT
          { $value = ex($qi0.value,
                        $IDENT.text,
                        format="${left}.${right}",
                        rename=True)
          }
        )
    ;


annotationList
    :   ^(ANNOTATION_LIST annotation*)
    ;


annotation returns [value]
    @init { $value = ex(format="${left}()") }
    :   ^(AT
          qi0=qualifiedIdentifier { $value.update(left=$qi0.value, annotation=True) }
          (ai0=annotationInit
           {   right = ", ".join(self.formatExpression(v) for v in $ai0.values)
               $value.update(right=right, format="${left}(${right})") }
          )?
        )
    ;


annotationInit returns [values]
    :   ^(ANNOTATION_INIT_BLOCK ai0=annotationInitializers { $values = $ai0.values })
    ;


annotationInitializers returns [values]
    @init { $values = [] }
    :   ^(ANNOTATION_INIT_KEY_LIST (ai0=annotationInitializer { $values.append($ai0.value) })+)
    |   ^(ANNOTATION_INIT_DEFAULT_KEY annotationElementValue)
    ;


annotationInitializer returns [value]
    :   ^(id0=IDENT ae0=annotationElementValue
          { $value = ex(left=self.renameIdent($id0.text),
                        right=$ae0.value,
                        format="${left}=${right}") })
    ;


annotationElementValue returns [value]
    :   ^(ANNOTATION_INIT_ARRAY_ELEMENT annotationElementValue*)
    |   annotation
    |   ex0=expression { $value = $ex0.value }
    ;


annotationTopLevelScope
    :   ^(ANNOTATION_TOP_LEVEL_SCOPE annotationScopeDeclarations*)
    ;


annotationScopeDeclarations
    @init { default = None }
    :   ^(ANNOTATION_METHOD_DECL
          md0=modifierList
          tp0=type
          id0=IDENT
          (ad0=annotationDefaultValue { default = $ad0.value })?
          { self.addAnnotationMethod($md0.values, $tp0.value, $id0.text, default) }
        )
    |   ^(VAR_DECLARATION md1=modifierList tp1=type vd1=variableDeclaratorList)
         { self.addVariables($vd1.values, $tp1.value, $md1.values, local=True) }
    |   typeDeclaration
    ;


annotationDefaultValue returns [value]
    :   ^(DEFAULT ae0=annotationElementValue { $value = $ae0.value })
    ;


block
    :   ^(BLOCK_SCOPE blockStatement*)
    ;


blockStatement
    @after { self.commentHandler($start) }
    :   localVariableDeclaration
    |   typeDeclaration
    |   st0=statement { self.append($st0.value) }
    ;


localVariableDeclaration
    :   ^(VAR_DECLARATION md0=localModifierList tp0=type vd0=variableDeclaratorList
          { self.addVariables($vd0.values, $tp0.value, $md0.values, local=True) }
        )
     ;


statement returns [value]
    @init {
        label = None
        $value = ex()
    }
    :   block
    |   ^(ASSERT
          (ex0=expression { ae = self.makeAssert($ex0.value)  })
          (ex1=expression { self.extendAssert(ae, $ex1.value) })?
        )
    |   ^(IF
          pe0=parenthesizedExpression { ifstat, elsestat = self.beginIf($pe0.value) }
          statement { self.endIf() }
          ({ self.beginElse(elsestat) } statement { self.endElse() })?
        )
    |   ^(FOR forInit forCondition forUpdater statement)
    |   ^(FOR_EACH
          { self.beginFor() }
          localModifierList
          type
          id0=IDENT
          ex0=expression
          { self.setExpression(ex($id0.text, $ex0.value, format="${left} in ${right}")) }
          st0=statement { self.append($st0.value) }
          { self.endFor() }
        )
    |   ^(WHILE
          pe0=parenthesizedExpression
          { self.beginWhile($pe0.value) }
          statement
          { self.endWhile() }
        )
    |   ^(DO
          { self.beginDo() }
          statement
          pe0=parenthesizedExpression
          { self.endDo($pe0.value) }
        )
    |   ^(TRY
         { self.beginTry() }
         block
         { self.endTry() }
         catches?
         ({ self.beginTryFinally() } block { sef.endTryFinally() })?
        )
    |   ^(SWITCH
          { self.beginSwitch() }
          (pe0=parenthesizedExpression { self.setExpression($pe0.value) })
          switchBlockLabels
          { self.endSwitch() }
        )
    |   ^(SYNCHRONIZED parenthesizedExpression block)
    |   ^(RETURN
          { $value.update(format="return") }
          (ex0=expression { $value.update(right=$ex0.value) })?
          { $value.update(format="return ${right}") }
        )
    |   ^(THROW expression)
    |   ^(BREAK (id0=IDENT { label = $id0.text })?)  { self.addBreak(label=label) }
    |   ^(CONTINUE (id0=IDENT { label = $id0.text })?) { self.addContinue(label=label) }
    |   ^(LABELED_STATEMENT id0=IDENT lb0=statement { self.addLabel($id0.text) })
    |   ex0=expression { $value = $ex0.value }
    |   SEMI // Empty statement.
    ;


catches
    :   ^(CATCH_CLAUSE_LIST catchClause+)
    ;


catchClause
    :   ^(CATCH
          fp0=formalParameterStandardDecl { self.beginCatch($fp0.value) }
          block { self.endCatch() }
        )
    ;


switchBlockLabels
// This is the original grammar that produces duplicate case blocks:
//  :   ^(SWITCH_BLOCK_LABEL_LIST switchCaseLabel* switchDefaultLabel? switchCaseLabel?)
    :   ^(SWITCH_BLOCK_LABEL_LIST switchCaseLabel* switchDefaultLabel?)
    ;


switchCaseLabel
    :   ^(CASE
          ( ex0=expression { self.addSwitchCase($ex0.value) } )
          blockStatement*
        )
        { self.maybePop(True) }
    ;


switchDefaultLabel
    :   ^(DEFAULT
          { self.addSwitchCaseDefault() }
          blockStatement*
        )
        { self.maybePop(True) }
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
    @init {
    $value = ex()
    def exs(left, right, op):
        return ex(left, right, "${left} " + op + " ${right}")
    def exs1(left, op):
        return ex(left, format=op + "${left}")
    }
    :   ^(ASSIGN lv0=expr rv0=expr       { $value = exs(lv0, rv0, "=")   })
    |   ^(PLUS_ASSIGN lv0=expr rv0=expr  { $value = exs(lv0, rv0, "+=")  })
    |   ^(MINUS_ASSIGN lv0=expr rv0=expr { $value = exs(lv0, rv0, "-=")  })
    |   ^(STAR_ASSIGN lv0=expr rv0=expr  { $value = exs(lv0, rv0, "*=")  })
    |   ^(DIV_ASSIGN lv0=expr rv0=expr   { $value = exs(lv0, rv0, "/=")  })
    |   ^(AND_ASSIGN lv0=expr rv0=expr   { $value = exs(lv0, rv0, "&=")  })
    |   ^(OR_ASSIGN lv0=expr rv0=expr    { $value = exs(lv0, rv0, "|=")  })
    |   ^(XOR_ASSIGN lv0=expr rv0=expr   { $value = exs(lv0, rv0, "^=")  })
    |   ^(MOD_ASSIGN lv0=expr rv0=expr   { $value = exs(lv0, rv0, "\%=") })
    |   ^(BIT_SHIFT_RIGHT_ASSIGN expr expr)
    |   ^(SHIFT_RIGHT_ASSIGN expr expr)
    |   ^(SHIFT_LEFT_ASSIGN expr expr)
    |   ^(QUESTION lv0=expr rv0=expr cv0=expr)
          { $value.update(left=lv0, right=rv0,
                          format="(${right} if ${left} else ${center})", center=cv0) }
    |   ^(LOGICAL_OR expr expr)
    |   ^(LOGICAL_AND expr expr)
    |   ^(OR expr expr)
    |   ^(XOR expr expr)
    |   ^(AND expr expr)
    |   ^(EQUAL lv0=expr rv0=expr     { $value = exs(lv0, rv0, "==") })
    |   ^(NOT_EQUAL lv0=expr rv0=expr { $value = exs(lv0, rv0, "!=") })
    |   ^(INSTANCEOF lv0=expr tp0=type
          { $value = ex(lv0, $tp0.value, "isinstance(${left}, (${right}, ))") })
    |   ^(LESS_OR_EQUAL lv0=expr rv0=expr    { $value = exs(lv0, rv0, "<=")               })
    |   ^(GREATER_OR_EQUAL lv0=expr rv0=expr { $value = exs(lv0, rv0, ">=")               })
    |   ^(BIT_SHIFT_RIGHT lv0=expr rv0=expr  )
    |   ^(SHIFT_RIGHT lv0=expr rv0=expr      { $value = exs(lv0, rv0, ">>")               })
    |   ^(GREATER_THAN lv0=expr rv0=expr     { $value = exs(lv0, rv0, ">")                })
    |   ^(SHIFT_LEFT lv0=expr rv0=expr       { $value = exs(lv0, rv0, "<<")               })
    |   ^(LESS_THAN lv0=expr rv0=expr        { $value = exs(lv0, rv0, "<")                })
    |   ^(PLUS lv0=expr rv0=expr             { $value = exs(lv0, rv0, "+")                })
    |   ^(MINUS lv0=expr rv0=expr            { $value = exs(lv0, rv0, "-")                })
    |   ^(STAR lv0=expr rv0=expr             { $value = exs(lv0, rv0, "*")                })
    |   ^(DIV lv0=expr rv0=expr              { $value = exs(lv0, rv0, "/")                })
    |   ^(MOD lv0=expr rv0=expr              { $value = exs(lv0, rv0, "\%")               })
    |   ^(UNARY_PLUS lv0=expr                { $value = exs1(lv0, "+")                    })
    |   ^(UNARY_MINUS lv0=expr               { $value = exs1(lv0, "-")                    })
    |   ^(PRE_INC lv0=expr                   { $value = ex(lv0, format="${left} += 1")    })
    |   ^(PRE_DEC lv0=expr                   { $value = ex(lv0, format="${left} -= 1")    })
    |   ^(POST_INC lv0=expr                  { $value = ex(lv0, format="${left} += 1")    })
    |   ^(POST_DEC lv0=expr                  { $value = ex(lv0, format="${left} -= 1")    })
    |   ^(NOT lv0=expr                       { $value = ex(lv0, format="~${left}")        })
    |   ^(LOGICAL_NOT lv0=expr               { $value = ex(lv0, format="not ${left}")     })
    |   ^(CAST_EXPR tp0=type rv0=expr        { $value = ex($tp0.value, rv0, "${left}(${right})") })
    |   pe0=primaryExpression
        { if $pe0.value:
              $value.update($pe0.value)
        }
    ;

primaryExpression returns [value]
    @init { $value = ex() }
    :   ^(  DOT
            (   p0=primaryExpression
                { $value = ex($p0.value, format="${left}.${right}") }
                (   IDENT
                    { $value["right"] = ex($IDENT.text, format="${left}", rename=True) }
                |   THIS  { $value["format"] = "${left}" } // broken
                |   SUPER
                 { $value["format"] = "${left}"
                   $value["left"] = ex($value["left"], "", "super(${left}, self)")
                 }
                |ne0=innerNewExpression { $value["right"] = $ne0.value }
                |   CLASS { $value["right"] = ex("__class__", "", "${left}") }
                )
            |   pt0=primitiveType CLASS { $value = ex($pt0.text, "__class__", "${left}.${right}") }
            |   VOID CLASS { $value = ex("None", "__class__", "${left}.${right}") }
            )
        )

    |   parenthesizedExpression { $value = $parenthesizedExpression.value }

    |   IDENT { $value = ex(self.altIdent($IDENT.text), format="${left}", rename=True)  }

    |   ^(METHOD_CALL
          p0=primaryExpression
          genericTypeArgumentList?
          a0=arguments
          { $value = ex($p0.value, $a0.values, "${left}(${right})", call=True) }
        )

    |   ec0=explicitConstructorCall { self.addSuperCall($ec0.value) }

    |   ^(ARRAY_ELEMENT_ACCESS
          p0=primaryExpression
          e0=expression
          { $value = ex($p0.value, $e0.value, "${left}[${right}]") }
        )

    |   literal { $value = ex($literal.value, format="${left}") }

    |   newExpression { $value = $newExpression.value }

    |   THIS { $value = ex("self", format="${left}") }

    |   arrayTypeDeclarator

    |   SUPER { $value = ex(self.topParentName, format="super(${left}, self)") }
    ;


explicitConstructorCall returns [value]
    @init { $value = ex() }
    :   ^(THIS_CONSTRUCTOR_CALL genericTypeArgumentList? arguments)
    |   ^(SUPER_CONSTRUCTOR_CALL
            (pe0=primaryExpression)?
            genericTypeArgumentList?
            (ag0=arguments
             { $value.update(right=$ag0.values) }
            )
        )
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

    |   ^(CLASS_CONSTRUCTOR_CALL
          genericTypeArgumentList?
          q1=qualifiedTypeIdent
          a1=arguments
          classTopLevelScope?
          { $value = ex($q1.value, $a1.values, "${left}(${right})") }
        )
    ;


//something like 'InnerType innerType = outer.new InnerType();'
innerNewExpression returns [value]
    :   ^(CLASS_CONSTRUCTOR_CALL
          genericTypeArgumentList?
          id0=IDENT
          ag0=arguments
          classTopLevelScope?
          { $value = ex(self.altIdent($id0.text), $ag0.values, "${left}(${right})", rename=True) }
        )
    ;


newArrayConstruction returns [value]
    @init { $value, format = "", "${right}" }
    :   ad0=arrayDeclaratorList ai0=arrayInitializer
        { $value = $ai0.value }
    |   (ex0=expression
        { $value = ex($value, ex0, format)
          format = "${left}, ${right}"
        })+
        arrayDeclaratorList?
    ;


arguments returns [values]
    @init { $values, format = "", "${right}" }
    :   ^(ARGUMENT_LIST (ex0=expression
          { $values, format = ex($values, $ex0.value, format), "${left}, ${right}" })*
        )
    ;


literal returns [value]
    :   HEX_LITERAL            { $value = $text }
    |   OCTAL_LITERAL          { $value = $text }
    |   DECIMAL_LITERAL        { $value = formatFloatLiteral($text) }
    |   FLOATING_POINT_LITERAL { $value = formatFloatLiteral($text) }
    |   CHARACTER_LITERAL      { $value = $text }
    |   STRING_LITERAL         { $value = $text }
    |   TRUE                   { $value = "True" }
    |   FALSE                  { $value = "False" }
    |   NULL                   { $value = "None" }
    ;
