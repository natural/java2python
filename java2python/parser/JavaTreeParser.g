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
from java2python import expressionValue as ev
from java2python.parser.local import LocalTreeParser
}

// this is the interface for the client.  the client passes a block
// for the grammar to fill.
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
            (classTopLevelScope { print "####### enum class" } )?
        )
    ;

// nb:  we're making an extra class body only if there's a scope.
enumConstant returns [decl] @init { decl = dict() }
    :   ^(id0=IDENT an0=annotationList ag0=arguments?
          { $decl.update(id=$id0.text, annos=$an0.annos, args=$ag0.args) }
          ({ $decl.update(klass=self.onClass($id0.text)) }
           classTopLevelScope
           { self.pop() }
          )?
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
          { self.onMethod($id0.text, $md0.mods, $fp0.params, $tp0.value) }
          block?
          { self.commentHandler($start)
            self.pop() }
        )
    |   ^(VOID_METHOD_DECL md1=modifierList genericTypeParameterList? id1=IDENT
          fp1=formalParameterList throwsClause?
          { self.onMethod($id1.text, $md1.mods, $fp1.params, "void") }
          block?
          { self.commentHandler($start)
            self.pop() }
        )
    |   ^(VAR_DECLARATION md2=modifierList tp2=type vd2=variableDeclaratorList)
         { self.onVariables($vd2.decls, $tp2.value, $md2.mods) }
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
          { self.onMethod($id0.text, $md0.mods, $fp0.params, $tp0.value, pop=True) }
        )
    |   ^(VOID_METHOD_DECL md1=modifierList genericTypeParameterList? id0=IDENT
          fp1=formalParameterList throwsClause?
          { self.onMethod($id0.text, $md1.mods, $fp1.params, "void", pop=True) }
        )
    |   ^(VAR_DECLARATION md2=modifierList tp2=type vd0=variableDeclaratorList)
          { self.onVariables($vd0.decls, $tp2.value, $md2.mods) }
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
    :   ^(id0=IDENT { $decl["left"] = self.altId($id0.text) }
              (ad0=arrayDeclaratorList { $decl["array"] = True })?
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
                { $value, format = ev($value, $v0.value, format), "${left}, ${right}" }
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
          (pt0=primitiveType { $value["left"] = self.altType($pt0.text) } |
           qt0=qualifiedTypeIdent { $value["left"] = self.altType($qt0.value) })
          (arrayDeclaratorList
           { $value["array"] = True
             $value["format"] += "list" ##"array of \%s" \% $value["left"]
             $value["left"] = ""
           }
          )?
        )
    ;

qualifiedTypeIdent returns [value] @after { self.commentHandler($start) }
    :   ^(QUALIFIED_TYPE_IDENT (ti0=typeIdent { $value = $ti0.value })+)
    ;

typeIdent returns [value]
    :   ^(id0=IDENT genericTypeArgumentList?) { $value = self.altId($id0.text) }
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

genericTypeArgumentList returns [value] @init { $value = [] }
    :   ^(GENERIC_TYPE_ARG_LIST (ga0=genericTypeArgument { $value.append($ga0.value) })+)
    ;

genericTypeArgument returns [value] @init { $value = {} }
    :   tp0=type { $value $tp0.value }
    |   ^(QUESTION (gw0=genericWildcardBoundType { $value.update($gw0.value) })?)
    ;

genericWildcardBoundType returns [value]
    :   ^(EXTENDS tp0=type { $value = dict(extends=$tp0.value) })
    |   ^(SUPER tp1=type { $value = dict(super=$tp1.value) })
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
    :   IDENT { $value = ev(self.altId($text), format="${left}") }
    |   ^(DOT qi0=qualifiedIdentifier IDENT
        { $value = ev($qi0.value, self.altId($IDENT.text), "${left}.${right}") })
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

annotationDefaultValue returns [value]
    :   ^(DEFAULT (av0=annotationElementValue { $value = $av0.text }))
    ;

block  returns [values] @init { $values = [] }
    :   ^(BLOCK_SCOPE (bs0=blockStatement { $values.append($bs0.value)})*)
    ;

blockStatement returns [value]
    :   lv0=localVariableDeclaration { $value = $lv0.value }
    |   typeDeclaration { $value = '' }
    |   statement { $value = '' }
    ;

localVariableDeclaration returns [value] @init { $value='' }
    :   ^(VAR_DECLARATION md0=localModifierList tp0=type vd0=variableDeclaratorList)
         { self.onLocalDecls($vd0.decls, $tp0.value) }
    ;

statement returns [value] @init { $value='' }
    :   block
    |   ^(ASSERT (ex0=expression { args=[$ex0.value] }
                 (ex1=expression { args.append($ex1.value) })?)
            { self.onAssert(*args) }
        )
    |   ^(IF pe0=parenthesizedExpression
             { ifstat, elsestat = self.onIf($pe0.value) }
             statement
             { self.onIfFinish()
               self.pop()
             }
             ({self.push(elsestat)} statement? { self.pop() })
        )
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
    |   ^(SWITCH pe0=parenthesizedExpression { self.onSwitch($pe0.value) }
          switchBlockLabels
          { self.pop() }
        )
    |   ^(SYNCHRONIZED pe0=parenthesizedExpression
          { ss = self.onSync($pe0.value) }
          block
          { self.pop() }
        )
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
    :   ^(CASE ex0=expression { self.onSwitchCase($ex0.value) }
          blockStatement*
        )
    ;

switchDefaultLabel
    :   ^(DEFAULT (blockStatement { self.onSwitchDefault() } )*)
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
    :   ^(ASSIGN lv0=expr rv0=expr)
          { $value = self.makeAssign("=", lv0, rv0) }
    |   ^(PLUS_ASSIGN lv0=expr rv0=expr)
          { $value = self.makeAssign("+=", lv0, rv0) }
    |   ^(MINUS_ASSIGN lv0=expr rv0=expr)
          { $value = self.makeAssign("-=", lv0, rv0) }
    |   ^(STAR_ASSIGN lv0=expr rv0=expr)
          { $value = self.makeAssign("*=", lv0, rv0) }
    |   ^(DIV_ASSIGN lv0=expr rv0=expr)
          { $value = self.makeAssign("/=", lv0, rv0) }
    |   ^(AND_ASSIGN lv0=expr rv0=expr)
          { $value = self.makeAssign("&=", lv0, rv0) }
    |   ^(OR_ASSIGN  lv0=expr rv0=expr)
          { $value = self.makeAssign("|=", lv0, rv0) }
    |   ^(XOR_ASSIGN lv0=expr rv0=expr)
          { $value = self.makeAssign("^=", lv0, rv0) }
    |   ^(MOD_ASSIGN lv0=expr rv0=expr)
          { $value = self.makeAssign("\%=", lv0, rv0) }
    |   ^(BIT_SHIFT_RIGHT_ASSIGN lv0=expr rv0=expr)
          { $value = self.onBsrAssign(lv0, rv0) }
    |   ^(SHIFT_RIGHT_ASSIGN left=expr right=expr)
          { $value = self.makeAssign(">>=", left, right) }
    |   ^(SHIFT_LEFT_ASSIGN left=expr right=expr)
          { $value = self.makeAssign("<<=", left, right) }
    |   ^(QUESTION lv0=expr rv0=expr cv0=expr)
          { $value = ev(lv0, rv0, "(${right} if ${left} else ${center})", center=cv0) }
    |   ^(LOGICAL_OR lv0=expr rv0=expr)
          { $value = ev(lv0, rv0, "${left} or ${right}") }
    |   ^(LOGICAL_AND lv0=expr rv0=expr)
          { $value = ev(lv0, rv0, "${left} and ${right}") }
    |   ^(OR lv0=expr rv0=expr)
          { $value = ev(lv0, rv0, "${left} | ${right}") }
    |   ^(XOR lv0=expr rv0=expr)
          { $value = ev(lv0, rv0, "${left} ^ ${right}") }
    |   ^(AND lv0=expr rv0=expr)
          { $value = ev(lv0, rv0, "${left} & ${right}") }
    |   ^(EQUAL lv0=expr rv0=expr)
          { $value = ev(lv0, rv0, "${left} == ${right}") }
    |   ^(NOT_EQUAL lv0=expr rv0=expr)
          { $value = ev(lv0, rv0, "${left} != ${right}") }
    |   ^(INSTANCEOF lv0=expr tp0=type)
          { $value = ev(lv0, $tp0.value, "isinstance(${left}, (${right}, ))") }
    |   ^(LESS_OR_EQUAL lv0=expr rv0=expr)
          { $value = ev(lv0, rv0, "${left} <= ${right}") }
    |   ^(GREATER_OR_EQUAL lv0=expr rv0=expr)
          { $value = ev(lv0, rv0, "${left} >= ${right}") }
    |   ^(BIT_SHIFT_RIGHT lv0=expr rv0=expr)
          { $value = self.onBsr(lv0, rv0) }
    |   ^(SHIFT_RIGHT lv0=expr rv0=expr)
          { $value = ev(lv0, rv0, "${left} >> ${right}") }
    |   ^(GREATER_THAN lv0=expr rv0=expr)
          { $value = ev(lv0, rv0, "${left} > ${right}") }
    |   ^(SHIFT_LEFT lv0=expr rv0=expr)
          { $value = ev(lv0, rv0, "${left} << ${right}") }
    |   ^(LESS_THAN lv0=expr rv0=expr)
          { $value = ev(lv0, rv0, "${left} < ${right}") }
    |   ^(PLUS lv0=expr rv0=expr)
          { $value = ev(lv0, rv0, "${left} + ${right}") }
    |   ^(MINUS lv0=expr rv0=expr)
          { $value = ev(lv0, rv0, "${left} - ${right}") }
    |   ^(STAR lv0=expr rv0=expr)
          { $value = ev(lv0, rv0, "${left} * ${right}") }
    |   ^(DIV lv0=expr rv0=expr)
          { $value = ev(lv0, rv0, "${left} / ${right}") }
    |   ^(MOD lv0=expr rv0=expr)
          { $value = ev(lv0, rv0, "${left} \% ${right}") }
    |   ^(UNARY_PLUS lv0=expr)
          { $value = ev(lv0, format="+${left}") }
    |   ^(UNARY_MINUS lv0=expr)
          { $value = ev(lv0, format="-${left}") }
    |   ^(PRE_INC lv0=expr)
          { $value = ev(lv0, format="${left} += 1", pre=True, assign=True) }
    |   ^(PRE_DEC lv0=expr)
          { $value = ev(lv0, format="${left} -= 1", pre=True, assign=True) }
    |   ^(POST_INC lv0=expr)
          { $value = ev(lv0, format="${left} += 1", post=True, assign=True) }
    |   ^(POST_DEC lv0=expr)
          { $value = ev(lv0, format="${left} -= 1", post=True, assign=True) }
    |   ^(NOT lv0=expr)
          { $value = ev(lv0, format="~${left}") }
    |   ^(LOGICAL_NOT lv0=expr)
          { $value = ev(lv0, format="not ${left}") }
    |   ^(CAST_EXPR lv0=type rv0=expr)
          { $value = ev(lv0, rv0, "${left}(${right})") }
    |   p0=primaryExpression { $value = $p0.value }
    ;

primaryExpression returns [value] @init { $value = ev() }
    :   ^(  DOT
            (p0=primaryExpression
             { $value = ev($p0.value, format="${left}.${right}") }
                (i0=IDENT { $value["right"] = ev(self.altId($i0.text), format="${left}")}
                |THIS { $value["format"] = "${left}" } // broken
                |SUPER
                 { $value["format"] = "${left}"
                   $value["left"] = ev($value["left"], "", "super(${left}, self)")
                 }
                |ne0=innerNewExpression { $value = $ne0.value }
                |CLASS { $value["right"] = ev("__class__", "", "${left}") }
                )
            |   pt0=primitiveType CLASS { $value = ev($pt0.text, "__class__", "${left}.${right}") }
            |   VOID CLASS { $value = ev("None", "__class__", "${left}.${right}") }
            )
        )
    |   parenthesizedExpression { $value = $parenthesizedExpression.value }
    |   IDENT { $value = ev(self.altId($text), "", "${left}")  }
    |   ^(METHOD_CALL p0=primaryExpression genericTypeArgumentList? a0=arguments
            { $value = ev($p0.value, $a0.args, "${left}(${right})") }
        )
    |   ec0=explicitConstructorCall { $value = $ec0.value }
    |   ^(ARRAY_ELEMENT_ACCESS p0=primaryExpression e0=expression
            { $value = ev($p0.value, $e0.value, "${left}[${right}]") }
        )
    |   literal { $value = $literal.value }
    |   newExpression { $value = $newExpression.value }
    |   THIS { $value = ev("self", "", "${left}") }
    |   arrayTypeDeclarator
    |   SUPER { $value = ev(self.topParentName, "", "super(${left}, self)") }
    ;

explicitConstructorCall returns [value]
    :   ^(THIS_CONSTRUCTOR_CALL ga0=genericTypeArgumentList? ag0=arguments)
        { $value = ev("self.__init__", $ag0.args, "${left}(${right})") }
    |   ^(SUPER_CONSTRUCTOR_CALL pe1=primaryExpression? ga1=genericTypeArgumentList? ag1=arguments)
        { $value = ev(self.topParentName, $ag1.args, "super(${left}, self).__init__(${right})", superCall=True) }
    ;

arrayTypeDeclarator
    :   ^(ARRAY_DECLARATOR (arrayTypeDeclarator | qualifiedIdentifier | primitiveType))
    ;

newExpression returns [value]
    // the static array creator rule is tested in tests/ArrayValues.java.
    :   ^(STATIC_ARRAY_CREATOR
          ( tp0=primitiveType ac0=newArrayConstruction
            { $value = self.makeArrayCreator($tp0.text, $ac0.value) }
          | gt1=genericTypeArgumentList? tp1=qualifiedTypeIdent ac1=newArrayConstruction
            { $value = self.makeArrayCreator($tp1.value, $ac1.value, $gt1.value) }
          )
        )
    |   ^(CLASS_CONSTRUCTOR_CALL genericTypeArgumentList? q1=qualifiedTypeIdent
          a1=arguments classTopLevelScope?
          { $value = ev($q1.value, $a1.args, "${left}(${right})") }
        )
    ;

innerNewExpression returns [value]
     // something like 'InnerType innerType = outer.new InnerType();'  see the file
     // tests/InnerNew.java for an example.
     // oh, and wtf is with the classTopLevelScope???
    :   ^(CLASS_CONSTRUCTOR_CALL genericTypeArgumentList?
          id0=IDENT ag0=arguments classTopLevelScope?)
        { $value = ev($id0.text, $ag0.args, "${left}(${right})")
          $value = {}
          print "#####", $value, $id0.text, $innerNewExpression.text
        }
    ;

newArrayConstruction returns [value] @init { $value, format = "", "${right}" }
    // matches statements like: new int[] {1, 2}
    :   ad0=arrayDeclaratorList ai0=arrayInitializer
        { $value = $ai0.value }
    |   (ex0=expression
        { $value = ev($value, ex0, format)
          format = "${left}, ${right}"
        })+
        arrayDeclaratorList?
    ;

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
    |   DECIMAL_LITERAL { $value = self.makeFloatLiteral($text) }
    |   FLOATING_POINT_LITERAL { $value = self.makeFloatLiteral($text) }
    |   CHARACTER_LITERAL { $value = $text }
    |   STRING_LITERAL { $value = $text }
    |   TRUE { $value = 'True' }
    |   FALSE { $value = 'False' }
    |   NULL { $value = 'None' }
    ;
