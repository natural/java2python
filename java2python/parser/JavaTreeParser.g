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
from java2python.parser.extra import LocalTreeParser
}

javaSource[module] @init { self.onJavaSource(module) }
    :   ^(JAVA_SOURCE annotationList packageDeclaration? importDeclaration* typeDeclaration*)
    ;

packageDeclaration
    :   ^(PACKAGE q0=qualifiedIdentifier) { self.onPackageDecl($q0.text) }
    ;

importDeclaration
    :   ^(IMPORT st0=STATIC? qi0=qualifiedIdentifier ds0=DOTSTAR?)
         { self.onImportDecl($qi0.text, bool($st0), bool($ds0)) }
    ;

typeDeclaration @after { self.commentHandler($start) }
    :   ^(CLASS m0=modifierList i0=IDENT t0=genericTypeParameterList?
                x0=extendsClause? p0=implementsClause?
          { klass = self.onClass($i0.text, $m0.mods, $x0.clauses, $p0.clauses) }
          classTopLevelScope
          { self.pop() }
        )

    |   ^(INTERFACE m1=modifierList i1=IDENT t1=genericTypeParameterList? x1=extendsClause?
          { self.onClass($i1.text, $m1.mods, $x1.clauses) }
          interfaceTopLevelScope
          { self.pop() }
        )

    |   ^(ENUM m2=modifierList i2=IDENT p2=implementsClause?
          { enum = self.onEnum($i2.text, $m2.mods, $p2.clauses) }
          enumTopLevelScope
          { self.pop() }
        )

    |   ^(AT m3=modifierList i3=IDENT
          { klass = self.onAnnoType($i3.text, $m3.mods) }
          annotationTopLevelScope
          { self.pop() }
        )
    ;

extendsClause returns [clauses] @init { clauses = [] }
    :   ^(EXTENDS_CLAUSE (t0=type { clauses.append($t0.value) })+)
    ;

implementsClause returns [clauses] @init { clauses = [] }
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
    :   ^(ENUM_TOP_LEVEL_SCOPE
            (e0=enumConstant { self.onEnumConstant($e0.decl) })+
            classTopLevelScope?
        )
    ;

enumConstant returns [decl] @init { decl = dict() }
    :   ^(i0=IDENT a0=annotationList g0=arguments?
          { $decl.update(id=$i0.text, annos=$a0.text, args=$g0.args) }
          // nb:  we're making an extra class body only if there's a scope.
          ({ $decl.update(klass=self.onClass($i0.text)) } classTopLevelScope)?
        )
    ;

classTopLevelScope
    :   ^(CLASS_TOP_LEVEL_SCOPE classScopeDeclarations*)
    ;

classScopeDeclarations @after { self.commentHandler($start) }
    :   ^(CLASS_INSTANCE_INITIALIZER block)
    |   ^(CLASS_STATIC_INITIALIZER block)
    |   ^(FUNCTION_METHOD_DECL m0=modifierList genericTypeParameterList? t0=type i0=IDENT
          p0=formalParameterList arrayDeclaratorList? throwsClause?
          { self.onMethod($i0.text, $m0.mods, $p0.params) }
          block?
          { self.pop() }
        )
    |   ^(VOID_METHOD_DECL m1=modifierList genericTypeParameterList? i1=IDENT
          p1=formalParameterList throwsClause?
          { self.onMethod($i1.text, $m1.mods, $p1.params) }
          block?
          { self.commentHandler($start)
            self.pop() }
        )
    |   ^(VAR_DECLARATION m2=modifierList t2=type v2=variableDeclaratorList)
         { self.onVariables($v2.decls, $t2.value) }
    |   ^(CONSTRUCTOR_DECL m3=modifierList genericTypeParameterList?
          p3=formalParameterList throwsClause?
          { self.onMethod("__init__", $m3.mods, $p3.params) }
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
    :   ^(FUNCTION_METHOD_DECL m0=modifierList genericTypeParameterList? t0=type i0=IDENT
          p0=formalParameterList arrayDeclaratorList? throwsClause?
          { self.onMethod($i0.text, $m0.mods, $p0.params, pop=True) }
        )
    |   ^(VOID_METHOD_DECL m1=modifierList genericTypeParameterList? i1=IDENT
          p1=formalParameterList throwsClause?
          { self.onMethod($i1.text, $m1.mods, $p1.params, pop=True) }
        )
    |   ^(VAR_DECLARATION modifierList t2=type v2=variableDeclaratorList)
          { self.onVariables($v2.decls, $t2.value) }
    |   typeDeclaration
    ;

variableDeclaratorList returns [decls] @init { $decls = [] }
    :   ^(VAR_DECLARATOR_LIST (v0=variableDeclarator { $decls.append($v0.decl) })+)
    ;

variableDeclarator returns [decl] @init { $decl = dict() }
    :   ^(VAR_DECLARATOR v0=variableDeclaratorId { $decl = $v0.decl.copy() }
          (vi0=variableInitializer { $decl["init"] = $vi0.value })?
         )
    ;

variableDeclaratorId returns [decl] @init { $decl = dict() }
    :   ^(i0=IDENT { $decl["id"] = $i0.text }
              (a0=arrayDeclaratorList { $decl["array"] = [$a0.text] })?
        )
    ;

variableInitializer returns [value]
    :   arrayInitializer { $value = $arrayInitializer.value }
    |   expression { $value = $expression.value }
    ;

arrayDeclarator
    :   LBRACK RBRACK
    ;

arrayDeclaratorList
    :   ^(ARRAY_DECLARATOR_LIST ARRAY_DECLARATOR*)
    ;

arrayInitializer returns [value] @init { $value = [] }
    @after { $value = "[" + ", ".join($value) + "]" }
    :   ^(ARRAY_INITIALIZER (v0=variableInitializer { $value.append($v0.value) })*)
    ;

throwsClause
    :   ^(THROWS_CLAUSE qualifiedIdentifier+)
    ;

modifierList returns [mods] @init { $mods = [] }
    :   ^(MODIFIER_LIST (m0=modifier { $mods.append($m0.value) })*)
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
    :   ^(LOCAL_MODIFIER_LIST (m0=localModifier { $mods.append($m0.value) })*)
    ;

type returns [value]
    :   ^(TYPE
          (p0=primitiveType { $value = $p0.text } | q0=qualifiedTypeIdent { $value = $q0.text })
          (arrayDeclaratorList { $value += $arrayDeclaratorList.text })? // FAIL
        )
    ;

qualifiedTypeIdent @after { self.commentHandler($start) }
    :   ^(QUALIFIED_TYPE_IDENT typeIdent+)
    ;

typeIdent returns [value]
    :   ^(i0=IDENT genericTypeArgumentList?) { $value = $i0.text }
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
    :   ^(FORMAL_PARAM_STD_DECL localModifierList t0=type v0=variableDeclaratorId)
         { $value = self.makeParamDecl($v0.decl, $t0.text) }
    ;

formalParameterVarargDecl returns [value]
    :   ^(FORMAL_PARAM_VARARG_DECL localModifierList t0=type v0=variableDeclaratorId)
         { $value = self.makeParamDecl($v0.decl, $t0.text, isVariadic=True) }
    ;

qualifiedIdentifier
    :   IDENT
    |   ^(DOT qualifiedIdentifier IDENT)
    ;

annotationList
    :   ^(ANNOTATION_LIST annotation*)
    ;

annotation returns [value] @init { inits = [] }
    :   ^(AT id0=qualifiedIdentifier (ai0=annotationInit { inits.append($ai0.value) })?)
         { $value = [$id0.text, inits] }
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
        { self.onAnnotationMethod($id0.text, $md0.mods, $dv0.value) }
    |   ^(VAR_DECLARATION modifierList type variableDeclaratorList)
    |   typeDeclaration
    ;

annotationDefaultValue returns[value]
    :   ^(DEFAULT (v0=annotationElementValue { $value = $v0.text }))
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
         { self.onVariables($v0.decls, $t0.value) }
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
          ({ self.onFinally() } block { self.pop() } )?
        )

    |   ^(SWITCH parenthesizedExpression switchBlockLabels)
    |   ^(SYNCHRONIZED parenthesizedExpression block)
    |   ^(RETURN (ex0=expression { self.onReturn($ex0.value) })?)
    |   ^(THROW (ex0=expression { self.onThrow($ex0.value) }))

    |   ^(BREAK (id0=IDENT)? ) { self.onBreak($id0.text if $id0 else None) }
    |   ^(CONTINUE (id0=IDENT)? ) { self.onContinue($id0.text if $id0 else None) }
    |   ^(LABELED_STATEMENT IDENT statement)
    |   (x0=expression { self.current.addSource($x0.value or "") })
    |   SEMI
    ;

catches
    :   ^(CATCH_CLAUSE_LIST (
            { stmt = self.onExcept() }
            c0=catchClause
            { self.onExceptClause(stmt, $c0.clause, pop=True) }
         )+
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
    :   ^(FOR_INIT (d0=localVariableDeclaration { $values.append($d0.text) }
                   | (e0=expression { $values.append($e0.value) })*)?)
    ;

forCondition returns [cond] @init { $cond = None }
    :   ^(FOR_CONDITION (e0=expression { $cond = $e0.value })?)
    ;

forUpdater returns [values] @init { $values = [] }
    :   ^(FOR_UPDATE (e0=expression {$values.append($e0.value)})*)
    ;

parenthesizedExpression returns [value]
    :   ^(PARENTESIZED_EXPR e0=expression { $value = "(" + ($e0.value or "") + ")" })
    ;

expression returns [value]
    :   ^(EXPR e0=expr { $value = $e0.value } )
    ;

expr returns [value]
    :   ^(ASSIGN left=expr right=expr) { self.onAssign("=", left, right) }
    |   ^(PLUS_ASSIGN left=expr right=expr) { $value = "\%s += \%s" \% ($left.value, $right.value) }
    |   ^(MINUS_ASSIGN expr expr)
    |   ^(STAR_ASSIGN expr expr)
    |   ^(DIV_ASSIGN expr expr)
    |   ^(AND_ASSIGN expr expr)
    |   ^(OR_ASSIGN expr expr)
    |   ^(XOR_ASSIGN expr expr)
    |   ^(MOD_ASSIGN expr expr)
    |   ^(BIT_SHIFT_RIGHT_ASSIGN expr expr)
    |   ^(SHIFT_RIGHT_ASSIGN left=expr right=expr) { self.onAssign(">>=", left, right) }
    |   ^(SHIFT_LEFT_ASSIGN left=expr right=expr) { self.onAssign("<<=", left, right) }
    |   ^(QUESTION expr expr expr)
    |   ^(LOGICAL_OR expr expr)
    |   ^(LOGICAL_AND expr expr)
    |   ^(OR expr expr)
    |   ^(XOR expr expr)
    |   ^(AND expr expr)
    |   ^(EQUAL left=expr right=expr)  { $value = ("\%s == \%s" \% (left, right)) }
    |   ^(NOT_EQUAL expr expr)
    |   ^(INSTANCEOF expr type)
    |   ^(LESS_OR_EQUAL left=expr right=expr) { $value = ("\%s <= \%s" \% (left, right)) }
    |   ^(GREATER_OR_EQUAL expr expr)
    |   ^(BIT_SHIFT_RIGHT expr expr)
    |   ^(SHIFT_RIGHT left=expr right=expr) { self.onAssign(">>", left, right) }
    |   ^(GREATER_THAN left=expr right=expr) { $value = ("\%s > \%s" \% (left, right)) }
    |   ^(SHIFT_LEFT left=expr right=expr) { self.onAssign("<<", left, right) }
    |   ^(LESS_THAN left=expr right=expr) { $value = ("\%s < \%s" \% (left, right)) }
    |   ^(PLUS left=expr right=expr) { $value = ("\%s + \%s" \% (left, right)) }
    |   ^(MINUS expr expr)
    |   ^(STAR left=expr right=expr) { $value = ("\%s * \%s" \% (left, right)) }
    |   ^(DIV expr expr)
    |   ^(MOD expr expr)
    |   ^(UNARY_PLUS expr)
    |   ^(UNARY_MINUS expr)
    |   ^(PRE_INC left=expr) { $value = "\%s += 1" \% ($left.value, ) }
    |   ^(PRE_DEC expr)
    |   ^(POST_INC left=expr) { $value = "\%s += 1" \% ($left.value, ) }
    |   ^(POST_DEC left=expr)  { $value = "\%s -= 1" \% ($left.value, ) }
    |   ^(NOT right=expr)
    |   ^(LOGICAL_NOT right=expr) { $value = ("not \%s" \% (right.value, )) }
    |   ^(CAST_EXPR type expr)
    |   p0=primaryExpression { $value = $p0.value }
    ;

primaryExpression returns [value] @init { $value = "" }
    :   ^(  DOT
            (   p0=primaryExpression { $value += $p0.value + "." }
                (   i0=IDENT { $value += self.altName($i0.text) }
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
    |   IDENT { $value = self.altName($IDENT.text) }
    |   ^(METHOD_CALL p0=primaryExpression genericTypeArgumentList? a0=arguments
         { $value = self.makeMethodExpr($p0.value, $a0.args) }
        )
    |   explicitConstructorCall
    |   ^(ARRAY_ELEMENT_ACCESS p0=primaryExpression e0=expression
            { $value = self.makeArrayAccess($p0.value, $e0.value) }
        )
    |   literal { $value = $literal.value }
    |   newExpression { $value = $newExpression.value }
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

newExpression returns [value]
    :   ^(  STATIC_ARRAY_CREATOR
            (   t0=primitiveType newArrayConstruction
            |   genericTypeArgumentList? q0=qualifiedTypeIdent newArrayConstruction
            )
            { $value = ($q0.text, "") }
        )
    |   ^(CLASS_CONSTRUCTOR_CALL genericTypeArgumentList? q1=qualifiedTypeIdent
          a1=arguments classTopLevelScope?
          { $value = self.makeMethodExpr($q1.text, $a1.args) }
        )
    ;

innerNewExpression // something like 'InnerType innerType = outer.new InnerType();'
    :   ^(CLASS_CONSTRUCTOR_CALL genericTypeArgumentList? IDENT arguments classTopLevelScope?)
    ;

newArrayConstruction
    :   arrayDeclaratorList arrayInitializer
    |   expression+ arrayDeclaratorList?
    ;

arguments returns [args] @init { args = [] }
    :   ^(ARGUMENT_LIST (ex0=expression { args.append($ex0.value) })*)
    ;

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
