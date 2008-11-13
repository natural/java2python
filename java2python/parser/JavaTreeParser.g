/*
For more information see the head comment within the 'java.g' grammar file
that defines the input for this tree grammar.

BSD licence

Copyright (c) 2007-2008 by HABELITZ Software Developments

All rights reserved.

http://www.habelitz.com


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

THIS SOFTWARE IS PROVIDED BY HABELITZ SOFTWARE DEVELOPMENTS ('HSD') ``AS IS''
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL 'HSD' BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/
tree grammar JavaTreeParser;

options { language=Python; backtrack=true; memoize=true; tokenVocab=Java;
          ASTLabelType=CommonTree; superClass=LocalTreeParser; }

@treeparser::header {
from java2python import ev
from java2python.parser.local import LocalTreeParser
}

// this is the interface for the client, and the client must pass in a
// block instance when called.  the block instance is modified by the
// remaining rules in this grammar.
javaSource [module] @init { self.onJavaSource(module) }
    :   ^(JAVA_SOURCE annotationList packageDeclaration? importDeclaration*
            typeDeclaration*
        )
    ;

// package declarations aren't supported directly; but the configuration
// can be set to write out setuptools calls or comments, or both.
packageDeclaration
    :   ^(PACKAGE qi0=qualifiedIdentifier) { self.onPackageDecl($qi0.value) }
    ;

// import declarations aren't directly supported, either, but like
// packages, the user can control the behavior via the configuration.
importDeclaration
    :   ^(IMPORT st0=STATIC? qi0=qualifiedIdentifier ds0=DOTSTAR?)
         { self.onImportDecl($qi0.value, $st0, $ds0) }
    ;

// the typeDeclaration rule covers classes, interfaces, enums and
// annotations.  note how the blocks are built in-line within the rule
// and that each is popped after the rule.

typeDeclaration @after { self.commentHandler($start) }
    :   ^(CLASS md0=modifierList id0=IDENT tp0=genericTypeParameterList?
          et0=extendsClause? im0=implementsClause?
          { self.onClass($id0.text, $md0.mods, $et0.clauses, $im0.clauses) }
          classTopLevelScope
          { self.pop() }
        )
    |   ^(INTERFACE md1=modifierList id1=IDENT tp1=genericTypeParameterList?
          et1=extendsClause?
          { self.onClass($id1.text, $md1.mods, $et1.clauses) }
          interfaceTopLevelScope
          { self.pop() }
        )
    |   ^(ENUM md2=modifierList id2=IDENT im2=implementsClause?
          { enum = self.onEnum($id2.text, $md2.mods, $im2.clauses) }
          enumTopLevelScope
          { self.pop() }
        )
    |   ^(AT md3=modifierList id3=IDENT
          { klass = self.onAnnoType($id3.text, $md3.mods) }
          annotationTopLevelScope
          { self.pop() }
        )
    ;

// we percolate the extends and implements clauses as lists to the
// parent rules.
extendsClause returns [clauses] @init { clauses = [] }
    :   ^(EXTENDS_CLAUSE (tp0=type { clauses.append($tp0.value) })+)
    ;

implementsClause returns [clauses] @init { clauses = [] }
    :   ^(IMPLEMENTS_CLAUSE (tp0=type { clauses.append($tp0.value) })+)
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
    :   ^(ENUM_TOP_LEVEL_SCOPE
            (ec0=enumConstant { self.onEnumConstant($ec0.decl) })+
            classTopLevelScope?
        )
    ;

// nb:  we're making an extra class body only if there's a scope.
enumConstant returns [decl] @init { decl = dict() }
    :   ^(id0=IDENT an0=annotationList ag0=arguments?
          { $decl.update(id=$id0.text, annos=$an0.annos, args=$ag0.args) }
          ({ $decl.update(klass=self.onClass($id0.text)) } classTopLevelScope)?
        )
    ;

classTopLevelScope
    :   ^(CLASS_TOP_LEVEL_SCOPE classScopeDeclarations*)
    ;

classScopeDeclarations @after { self.commentHandler($start) }
    :   ^(CLASS_INSTANCE_INITIALIZER block)
    |   ^(CLASS_STATIC_INITIALIZER block)
    |   ^(FUNCTION_METHOD_DECL md0=modifierList genericTypeParameterList? tp0=type
          id0=IDENT fp0=formalParameterList arrayDeclaratorList? throwsClause?
          { self.onMethod($id0.text, $md0.mods, $fp0.params) }
          block?
          { self.commentHandler($start)
            self.pop() }
        )
    |   ^(VOID_METHOD_DECL md1=modifierList genericTypeParameterList? id1=IDENT
          fp1=formalParameterList throwsClause?
          { self.onMethod($id1.text, $md1.mods, $fp1.params) }
          block?
          { self.commentHandler($start)
            self.pop() }
        )
    |   ^(VAR_DECLARATION md2=modifierList tp2=type vd2=variableDeclaratorList)
         { self.onVariables($vd2.decls, $tp2.value) }
    |   ^(CONSTRUCTOR_DECL md3=modifierList genericTypeParameterList?
          fp3=formalParameterList throwsClause?
          { self.onMethod("__init__", $md3.mods, $fp3.params) }
          block
          { self.commentHandler($start)
            self.pop() }
        )
    |   typeDeclaration
    ;

interfaceTopLevelScope
    :   ^(INTERFACE_TOP_LEVEL_SCOPE interfaceScopeDeclarations*)
    ;

interfaceScopeDeclarations
    :   ^(FUNCTION_METHOD_DECL md0=modifierList genericTypeParameterList?
          tp0=type id0=IDENT fp0=formalParameterList
          arrayDeclaratorList? throwsClause?
          { self.onMethod($id0.text, $md0.mods, $fp0.params, pop=True) }
        )
    |   ^(VOID_METHOD_DECL md1=modifierList genericTypeParameterList? id0=IDENT
          fp1=formalParameterList throwsClause?
          { self.onMethod($id0.text, $md1.mods, $fp1.params, pop=True) }
        )
    |   ^(VAR_DECLARATION modifierList tp2=type vd0=variableDeclaratorList)
          { self.onVariables($vd0.decls, $tp2.value) }
    |   typeDeclaration
    ;

variableDeclaratorList returns [decls] @init { $decls = [] }
    :   ^(VAR_DECLARATOR_LIST (v0=variableDeclarator { $decls.append($v0.decl) })+)
    ;

variableDeclarator returns [decl] @init { $decl = ev() }
    :   ^(VAR_DECLARATOR v0=variableDeclaratorId { $decl = $v0.decl }
          (vi0=variableInitializer { $decl["right"] = $vi0.value })?
         )
    ;

variableDeclaratorId returns [decl] @init { $decl = ev(format="${left}") }
    :   ^(id0=IDENT { $decl["left"] = $id0.text }
              (ad0=arrayDeclaratorList { $decl["array"] = [$ad0.text] })?
        )
    ;

variableInitializer returns [value]
    :   ai0=arrayInitializer { $value = ev($ai0.value, format="[${left}]") }
    |   expression { $value = $expression.value }
    ;

arrayDeclarator
    :   LBRACK RBRACK
    ;

arrayDeclaratorList returns [value] @init { $value = [] }
    :   ^(ARRAY_DECLARATOR_LIST (ARRAY_DECLARATOR { $value.append($text) })*)
    ;

arrayInitializer returns [value] @init { $value, format = "", "${right}" }
    :   ^(ARRAY_INITIALIZER
            (v0=variableInitializer
                { $value, format = ev($value, v0, format), "${left}, ${right}" }
            )*
        )
    ;

throwsClause
    :   ^(THROWS_CLAUSE qualifiedIdentifier+)
    ;

modifierList returns [mods] @init { $mods = [] }
    :   ^(MODIFIER_LIST (md0=modifier { $mods.append($md0.value) })*)
    ;

modifier returns [value]
    :   PUBLIC { $value = $text }
    |   PROTECTED { $value = $text }
    |   PRIVATE { $value = $text }
    |   STATIC { $value = $text }
    |   ABSTRACT { $value = $text }
    |   NATIVE { $value = $text }
    |   SYNCHRONIZED { $value = $text }
    |   TRANSIENT { $value = $text }
    |   VOLATILE { $value = $text }
    |   STRICTFP { $value = $text }
    |   localModifier { $value = $localModifier.value }
    ;

localModifier returns [value]
    :   FINAL { $value = $text }
    |   annotation { $value = $annotation.value }
    ;

localModifierList returns [mods] @init { $mods = [] }
    :   ^(LOCAL_MODIFIER_LIST (md0=localModifier { $mods.append($md0.value) })*)
    ;

type returns [value] @init { $value = ev(format="${left}") }
    :   ^(TYPE
          (pt0=primitiveType { $value["left"] = self.mapType($pt0.text) } |
           qt0=qualifiedTypeIdent { $value["left"] = self.mapType($qt0.value) })
          (arrayDeclaratorList
           { $value["format"] += "list" #$arrayDeclaratorList.value
             $value["left"] = ""
           }
          )?
        )
    ;

qualifiedTypeIdent returns [value] @after { self.commentHandler($start) }
    :   ^(QUALIFIED_TYPE_IDENT (ti0=typeIdent { $value = $ti0.value })+)
    ;

typeIdent returns [value]
    :   ^(id0=IDENT genericTypeArgumentList?) { $value = $id0.text }
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

// generic types and arguments aren't handled -- yet
// one idea to use them is in python 3 output.
// see pep 3107 http://www.python.org/dev/peps/pep-3107/

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

formalParameterList returns [params] @init { params = [] }
    :   ^(FORMAL_PARAM_LIST (fp0=formalParameterStandardDecl { params.append($fp0.value) })*
            (vd0=formalParameterVarargDecl { params.append($vd0.value) })?
        )
    ;

formalParameterStandardDecl returns [value]
    :   ^(FORMAL_PARAM_STD_DECL localModifierList tp0=type vd0=variableDeclaratorId)
         { $value = self.makeParamDecl($vd0.decl, $tp0.text) }
    ;

formalParameterVarargDecl returns [value]
    :   ^(FORMAL_PARAM_VARARG_DECL localModifierList tp0=type vd0=variableDeclaratorId)
         { $value = self.makeParamDecl($vd0.decl, $tp0.text, isVariadic=True) }
    ;

qualifiedIdentifier returns [value]
    :   IDENT { $value = ev($text, format="${left}") }
    |   ^(DOT qi0=qualifiedIdentifier IDENT
        { $value = ev($qi0.value, $IDENT.text, "${left}.${right}") })
    ;

annotationList returns [annos] @init { $annos = [] }
    :   ^(ANNOTATION_LIST (an0=annotation { $annos.append($an0.value) })*)
    ;

annotation returns [value] @init { inits = [] }
    :   ^(AT id0=qualifiedIdentifier (ai0=annotationInit { inits.append($ai0.value) })?)
         { $value = [$id0.value, inits] }
    ;

annotationInit returns [value]
    :   ^(ANNOTATION_INIT_BLOCK (ai0=annotationInitializers { $value = $ai0.inits }))
    ;

annotationInitializers returns [inits] @init { $inits = [] }
    :   ^(ANNOTATION_INIT_KEY_LIST
            (ai0=annotationInitializer { $inits.append($ai0.value) })+
        )
    |   ^(ANNOTATION_INIT_DEFAULT_KEY
            (ai1=annotationElementValue { $inits = [$ai1.value] })
        )
    ;

annotationInitializer returns [value]
    :   ^(id0=IDENT ev0=annotationElementValue) { $value = [$id0.text, $ev0.value] }
    ;

annotationElementValue returns [value]
    :   ^(ANNOTATION_INIT_ARRAY_ELEMENT annotationElementValue*)
    |   annotation // TODO
    |   expression { $value = $expression.value }
    ;

annotationTopLevelScope
    :   ^(ANNOTATION_TOP_LEVEL_SCOPE annotationScopeDeclarations*)
    ;

annotationScopeDeclarations
    :   ^(ANNOTATION_METHOD_DECL md0=modifierList tp0=type id0=IDENT (dv0=annotationDefaultValue)?)
        { self.onAnnoMethod($id0.text, $md0.mods, $dv0.value) }
    |   ^(VAR_DECLARATION modifierList type variableDeclaratorList)
    |   typeDeclaration
    ;

annotationDefaultValue returns[value]
    :   ^(DEFAULT (av0=annotationElementValue { $value = $av0.text }))
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
    :   ^(VAR_DECLARATION md0=localModifierList tp0=type vd0=variableDeclaratorList)
         { self.onLocalDecls($vd0.decls, $tp0.value) }
    ;

statement
    :   block
    |   ^(ASSERT (ex0=expression { args=[$ex0.value] }
                 (ex1=expression { args.append($ex1.value) })?)
            { self.onAssert(*args) }
        )

    |   ^(IF parenthesizedExpression statement statement?)

    |   ^(FOR i0=forInit c0=forCondition u0=forUpdater
             { b, s = self.onFor($i0.values, $c0.cond) }
             statement
             { self.onForFinish(s, $u0.values, pop=True) }
        )

    |   ^(FOR_EACH
             localModifierList t1=type i1=IDENT e1=expression
             { self.onForEach($t1.value, $i1.text, $e1.value) }
             statement
             { self.pop() }
        )

    |   ^(WHILE { ws = self.onWhile() }
            p0=parenthesizedExpression
            statement
            { self.onWhileFinish(ws, $p0.value, pop=True) }
        )

    |   ^(DO { ds = self.onDo() }
            statement
            (p0=parenthesizedExpression { self.onDoFinish(ds, $p0.value, pop=True) })
        )

    |   ^(TRY { self.onTry() }
          block
          { self.pop() }
          catches?
          ({ self.onTryFinally() } block { self.pop() } )?
        )

    |   ^(SWITCH parenthesizedExpression switchBlockLabels)
    |   ^(SYNCHRONIZED parenthesizedExpression block)
    |   ^(RETURN (ex0=expression { self.onReturn($ex0.value) })?)
    |   ^(THROW (ex0=expression { self.onThrow($ex0.value) }))

    |   ^(BREAK (id0=IDENT)? ) { self.onBreak($id0.text if $id0 else None) }
    |   ^(CONTINUE (id0=IDENT)? ) { self.onContinue($id0.text if $id0 else None) }
    |   ^(LABELED_STATEMENT IDENT statement)
    |   (ex0=expression { self.onStatementExpression($ex0.value or "") })
    |   SEMI
    ;

catches
    :   ^(CATCH_CLAUSE_LIST (
          { stmt = self.onTryExcept() }
          c0=catchClause
          { self.onTryExceptClause(stmt, $c0.clause, pop=True) })+
        )
    ;

catchClause returns [clause]
    :   ^(CATCH (d0=formalParameterStandardDecl { $clause = $d0.value }) block)
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

forInit returns [values] @init { $values = [] }
    :   ^(FOR_INIT (vd0=localVariableDeclaration { $values.append($vd0.text) }
                   | (ex0=expression { $values.append($ex0.value) })*)?)
    ;

forCondition returns [cond] @init { $cond = None }
    :   ^(FOR_CONDITION (ex0=expression { $cond = $ex0.value })?)
    ;

forUpdater returns [values] @init { $values = [] }
    :   ^(FOR_UPDATE (ex0=expression {$values.append($ex0.value)})*)
    ;

parenthesizedExpression returns [value]
    :   ^(PARENTESIZED_EXPR ex0=expression
          { $value = ev(left=$ex0.value, format="(${left})") }
        )
    ;

expression returns [value]
    :   ^(EXPR ex0=expr { $value = $ex0.value } )
    ;

expr returns [value]
    :   ^(ASSIGN lv0=expr rv0=expr) { self.onAssign("=", lv0, rv0) }
    |   ^(PLUS_ASSIGN lv0=expr rv0=expr) { self.onAssign("+=", lv0, rv0) }
    |   ^(MINUS_ASSIGN lv0=expr rv0=expr) { self.onAssign("-=", lv0, rv0) }
    |   ^(STAR_ASSIGN lv0=expr rv0=expr) { self.onAssign("*=", lv0, rv0) }
    |   ^(DIV_ASSIGN lv0=expr rv0=expr) { self.onAssign("/=", lv0, rv0) }
    |   ^(AND_ASSIGN lv0=expr rv0=expr) { self.onAssign("&=", lv0, rv0) }
    |   ^(OR_ASSIGN  lv0=expr rv0=expr) { self.onAssign("|=", lv0, rv0) }
    |   ^(XOR_ASSIGN lv0=expr rv0=expr) { self.onAssign("^=", lv0, rv0) }
    |   ^(MOD_ASSIGN lv0=expr rv0=expr) { self.onAssign("\%=", lv0, rv0) }

        // no translation and/or test case for these:
    |   ^(BIT_SHIFT_RIGHT_ASSIGN expr expr)
    |   ^(SHIFT_RIGHT_ASSIGN left=expr right=expr) { self.onAssign(">>=", left, right) }
    |   ^(SHIFT_LEFT_ASSIGN left=expr right=expr) { self.onAssign("<<=", left, right) }

    |   ^(QUESTION lv0=expr rv0=expr rv1=expr)
          { $value = ev(lv0, rv0, "(${right} if ${left} else ${rv1})", rv1=rv1) }
    |   ^(LOGICAL_OR lv0=expr rv0=expr) { $value = ev(lv0, rv0, "${left} or ${right}") }
    |   ^(LOGICAL_AND lv0=expr rv0=expr) { $value = ev(lv0, rv0, "${left} and ${right}") }
    |   ^(OR lv0=expr rv0=expr) { $value = ev(lv0, rv0, "${left} | ${right}") }
    |   ^(XOR lv0=expr rv0=expr) { $value = ev(lv0, rv0, "${left} ^ ${right}") }
    |   ^(AND lv0=expr rv0=expr) { $value = ev(lv0, rv0, "${left} & ${right}") }
    |   ^(EQUAL lv0=expr rv0=expr) { $value = ev(lv0, rv0, "${left} == ${right}") }
    |   ^(NOT_EQUAL lv0=expr rv0=expr) { $value = ev(lv0, rv0, "${left} != ${right}") }

    |   ^(INSTANCEOF lv0=expr tp0=type)
          { $value = ev(lv0, $tp0.value, "isinstance(${left}, (${right}, ))") }
    |   ^(LESS_OR_EQUAL lv0=expr rv0=expr)
          { $value = ev(lv0, rv0, "${left} <= ${right}") }
    |   ^(GREATER_OR_EQUAL lv0=expr rv0=expr)
          { $value = ev(lv0, rv0, "${left} >= ${right}") }

    |   ^(BIT_SHIFT_RIGHT expr expr)

    |   ^(SHIFT_RIGHT lv0=expr rv0=expr) { $value = ev(lv0, rv0, "${left} >> ${right}") }
    |   ^(GREATER_THAN lv0=expr rv0=expr) { $value = ev(lv0, rv0, "${left} > ${right}") }
    |   ^(SHIFT_LEFT lv0=expr rv0=expr)  { $value = ev(lv0, rv0, "${left} << ${right}") }
    |   ^(LESS_THAN lv0=expr rv0=expr) { $value = ev(lv0, rv0, "${left} < ${right}") }

    |   ^(PLUS lv0=expr rv0=expr) { $value = ev(lv0, rv0, "${left} + ${right}") }
    |   ^(MINUS lv0=expr rv0=expr) { $value = ev(lv0, rv0, "${left} - ${right}") }
    |   ^(STAR lv0=expr rv0=expr) { $value = ev(lv0, rv0, "${left} * ${right}") }
    |   ^(DIV lv0=expr rv0=expr) { $value = ev(lv0, rv0, "${left} / ${right}") }
    |   ^(MOD lv0=expr rv0=expr) { $value = ev(lv0, rv0, "${left} \% ${right}") }
    |   ^(UNARY_PLUS lv0=expr) { $value = ev(lv0, format="+${left}") }
    |   ^(UNARY_MINUS lv0=expr) { $value = ev(lv0, format="-${left}") }

    |   ^(PRE_INC lv0=expr)     { $value = ev(lv0, format="${left} += 1") }
    |   ^(PRE_DEC lv0=expr)     { $value = ev(lv0, format="${left} -= 1") }
    |   ^(POST_INC lv0=expr)    { $value = ev(lv0, format="${left} += 1") }
    |   ^(POST_DEC lv0=expr)    { $value = ev(lv0, format="${left} -= 1") }
    |   ^(NOT lv0=expr)         { $value = ev(lv0, format="~${left}") }
    |   ^(LOGICAL_NOT lv0=expr) { $value = ev(lv0, format="not ${left}") }
    |   ^(CAST_EXPR lv0=type rv0=expr)   { $value = ev(lv0, rv0, "${left}(${right})") }
    |   p0=primaryExpression { $value = $p0.value }
    ;

primaryExpression returns [value] @init { $value = ev() }
    :   ^(  DOT
            (p0=primaryExpression
             { $value = ev($p0.value, format="${left}.${right}") }
                (   i0=IDENT { $value["right"] = ev($i0.text, format="${left}")}
                |   THIS
                |   SUPER
                |   innerNewExpression
                |   CLASS
                )
            |   primitiveType CLASS
            |   VOID CLASS
            )
        )
    |   parenthesizedExpression { $value = $parenthesizedExpression.value }
    |   IDENT { $value = ev($text, format="${left}")  }
    |   ^(METHOD_CALL p0=primaryExpression genericTypeArgumentList? a0=arguments
            { $value = ev($p0.value, $a0.args, "${left}(${right})") }
        )
    |   explicitConstructorCall
    |   ^(ARRAY_ELEMENT_ACCESS p0=primaryExpression e0=expression
            { $value = ev($p0.value, $e0.value, '${left}[${right}]') }
        )
    |   literal { $value = $literal.value }
    |   newExpression { $value = $newExpression.value }
    |   THIS { $value = ev('self', format="${left}") }
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

newExpression returns [value]
    :   ^(  STATIC_ARRAY_CREATOR
            (   tp0=primitiveType ac0=newArrayConstruction
                { $value = self.makeArrayCreator($tp0.text, $ac0.value) }
            // need test case:
            |   genericTypeArgumentList? qt0=qualifiedTypeIdent ac1=newArrayConstruction
                { $value = ev(right=ac1.value, format="${right}") }
            )
        )

    |   ^(CLASS_CONSTRUCTOR_CALL genericTypeArgumentList? q1=qualifiedTypeIdent
          a1=arguments classTopLevelScope?
          { $value = ev($q1.value, $a1.args, "${left}(${right})") }
        )
    ;

innerNewExpression // something like 'InnerType innerType = outer.new InnerType();'
    :   ^(CLASS_CONSTRUCTOR_CALL genericTypeArgumentList?
          IDENT arguments classTopLevelScope?)
    ;

newArrayConstruction returns [value] @init { $value, format = "", "${right}" }
    :   ad0=arrayDeclaratorList ai0=arrayInitializer
        { $value["right"] = ai0.value
          print "### newArrayConstruction 0", $value
        }
    |   (ex0=expression
        { $value = ev($value, ex0, format)
          format = "${left}, ${right}"
          print "### newArrayConstruction 1", $value
        })+
        arrayDeclaratorList?
    ;

//
arguments returns [args] @init { $args, format = "", "${right}" }
    :   ^(ARGUMENT_LIST (ex0=expression
          { $args, format = ev($args, $ex0.value, format), "${left}, ${right}" })*
        )
    ;

// pretty straight-forward.  see the tests/Literals.java class for its
// exercise.
literal returns [value]
    :   HEX_LITERAL { $value = $text }
    |   OCTAL_LITERAL { $value = $text }
    |   DECIMAL_LITERAL { $value = self.fixFloatLiteral($text) }
    |   FLOATING_POINT_LITERAL { $value = self.fixFloatLiteral($text) }
    |   CHARACTER_LITERAL { $value = $text }
    |   STRING_LITERAL { $value = $text }
    |   TRUE { $value = 'True' }
    |   FALSE { $value = 'False' }
    |   NULL { $value = 'None' }
    ;
