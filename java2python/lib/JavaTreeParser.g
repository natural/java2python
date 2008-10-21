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
from java2python.lib import sourcetypes
from java2python.lib.support import tracer, trace_line
}


javaSource[source]
    @decorate { @tracer }
    :   ^(JAVA_SOURCE
            annotationList[source]
            (p=packageDeclaration {source.addPackage(p)})?
            (i=importDeclaration {source.addImport(i)})*
            (t=typeDeclaration {source.addSource(t)})*
        )
    ;


packageDeclaration
returns [decl]
    @decorate { @tracer }
    :   ^(PACKAGE q=qualifiedIdentifier {decl=q})
    ;


importDeclaration
returns [decl]
    @decorate { @tracer }
    :   ^(IMPORT STATIC? q=qualifiedIdentifier DOTSTAR?) {decl=(q, bool($DOTSTAR))}
    ;


typeDeclaration
returns [klass]
    @decorate { @tracer }
    @init {
        klass = sourcetypes.Class()
    }

    :   ^(CLASS
            modifiers=modifierList[klass]
            class_name=IDENT
            genericTypeParameterList?
            ext_clauses=extendsClause?
            imp_clauses=implementsClause?
            classTopLevelScope[klass]
        )
        {
        klass.setName(class_name)
        klass.addModifiers(modifiers)
        klass.addBaseClasses(ext_clauses)
        klass.addBaseClasses(imp_clauses)
        }

    |   ^(INTERFACE
            modifiers=modifierList[klass]
            interface_name=IDENT
            genericTypeParameterList?
            ext_clauses=extendsClause?
            interfaceTopLevelScope[klass]
        )
        {
        klass.setName(interface_name)
        klass.addBaseClasses(ext_clauses)
        }

    |   ^(ENUM
            modifiers=modifierList[klass]
            enum_name=IDENT
            imp_clauses=implementsClause?
            enumTopLevelScope[klass]
        )
        {
        klass.setName(enum_name)
        }

    |   ^(AT
            modifiers=modifierList[klass]
            anno_name=IDENT
            blk=annotationTopLevelScope[klass]
        )
        {
        klass.setName($anno_name)
        klass.addModifiers(modifiers)
        }
    ;


extendsClause
returns[clauses]
    @decorate { @tracer }
    @init { clauses = [] }
    :   ^(EXTENDS_CLAUSE (t=type {clauses.append(t)})+)
    ;


implementsClause
returns[clauses]
    @decorate { @tracer }
    @init { clauses = [] }
    :   ^(IMPLEMENTS_CLAUSE (t=type {clauses.append(t)})+)
    ;


genericTypeParameterList
    @decorate { @tracer }
    :   ^(GENERIC_TYPE_PARAM_LIST genericTypeParameter+)
    ;


genericTypeParameter
    @decorate { @tracer }
    :   ^(IDENT bound[None]?)
    ;


bound[klass]
    @decorate { @tracer }
    :   ^(EXTENDS_BOUND_LIST type+)
    ;


enumTopLevelScope[block]
    @decorate { @tracer }
    :   ^(ENUM_TOP_LEVEL_SCOPE enumConstant[block]+ classTopLevelScope[None]?)
    ;


enumConstant[block]
    @decorate { @tracer }
    :   ^(IDENT annotationList[block] arguments[block]? classTopLevelScope[block]?)
    ;


classTopLevelScope[source]
    @decorate { @tracer }
    :   ^(CLASS_TOP_LEVEL_SCOPE classScopeDeclarations[source]* )
    ;


classScopeDeclarations[source]
    @decorate { @tracer }
    @init {
        blk = None
        varrenamemap = source.config.combined('variableNameMapping')
        typeValueMap = source.config.combined('typeValueMap')

    }
    :   ^(CLASS_INSTANCE_INITIALIZER block[source])
    |   ^(CLASS_STATIC_INITIALIZER block[source])

    |   {blk = source.newMethod()}
        ^(FUNCTION_METHOD_DECL
            modifiers=modifierList[blk]
            genericTypeParameterList?
            type
            ident=IDENT
            params=formalParameterList[blk]
            arrayDeclaratorList?
            throwsClause?
            block[blk]?
        )
        {
            blk.setName(ident)
            blk.addModifiers(modifiers)
            blk.addParameters(params)
        }

    |   {blk = source.newMethod()}
        ^(VOID_METHOD_DECL
            modifiers=modifierList[blk]
            genericTypeParameterList?
            ident=IDENT
            params=formalParameterList[blk]
            throwsClause?
            block[blk]?
        )
        {
            blk.setName(ident)
            blk.addModifiers(modifiers)
            blk.addParameters(params)
        }

    |   ^(VAR_DECLARATION
            modifiers=modifierList[blk]
            t=type
            vds=variableDeclaratorList[source]
        )
        {
            for name, value in vds:
                if value is None:
                    value = typeValueMap.get(t, 'None')
                var = source.newVariable()
                var.setName(name)
                var.setExpression(value)
                source.addSource( ("\%s = \%s", (("\%s", name, ), ("\%s", value, ))) )
        }

    |   ^(CONSTRUCTOR_DECL
            modifiers=modifierList[blk]
            genericTypeParameterList?
            params=formalParameterList[source]
            throwsClause?
            block[source]
        )

    |   (t=typeDeclaration {source.addSource(t)})

    ;


interfaceTopLevelScope[block]
    @decorate { @tracer }
    :   ^(INTERFACE_TOP_LEVEL_SCOPE interfaceScopeDeclarations[block]*)
    ;


interfaceScopeDeclarations[source]
    @decorate { @tracer }
    :   ^(FUNCTION_METHOD_DECL
            modifiers=modifierList[source]
            genericTypeParameterList?
            type
            IDENT
            params=formalParameterList[source]
            arrayDeclaratorList?
            throwsClause?
        )
    |   ^(VOID_METHOD_DECL
            modifiers=modifierList[source]
            genericTypeParameterList?
            IDENT
            params=formalParameterList[source]
            throwsClause?
        )
    // Interface constant declarations have been switched to variable
    // declarations by 'java.g'; the parser has already checked that
    // there's an obligatory initializer.
    |   ^(VAR_DECLARATION
            modifiers=modifierList[source]
            type
            vds=variableDeclaratorList[source]
        )
        {
            for name, value in vds:
                if value is None:
                    value = typeValueMap.get(t, 'None')
                var = source.newVariable()
                var.setName(name)
                var.setExpression(value)
                source.addSource( ("\%s = \%s", (("\%s", name, ), ("\%s", value, ))) )
        }

    |   typeDeclaration
    ;


variableDeclaratorList[block]
returns[decls]
    @decorate { @tracer }
    @init {
        decls = []
    }
    :   ^(VAR_DECLARATOR_LIST (vd=variableDeclarator[block] {decls.append(vd)})+)
    ;


variableDeclarator[block]
returns[decl]
    @decorate { @tracer }
    @init {
        decl = []
    }
    @after {
        if len(decl) == 1:decl.append(None)
        retval = decl
    }
    :   ^(VAR_DECLARATOR
            (v=variableDeclaratorId {decl.append(v)})
            (i=variableInitializer[block] {decl.append(i)} )?)
    ;


variableDeclaratorId
returns[var]
    @decorate { @tracer }
    :   ^((i=IDENT {var=$i.text})
          (a=arrayDeclaratorList {var=a})? )
    ;

variableInitializer[block]
returns [init]
    @decorate { @tracer }
    :   ai=arrayInitializer
        {
            init = ai
        }
    |   ex=expression[block]
        {
            init = ex
        }
    ;

arrayDeclarator
    @decorate { @tracer }
    :   LBRACK RBRACK
    ;

arrayDeclaratorList
    @decorate { @tracer }
    :   ^(ARRAY_DECLARATOR_LIST ARRAY_DECLARATOR*)
    ;

arrayInitializer
returns [vis]
    @decorate { @tracer }
    @init {
        vis = []
    }
    :   ^(ARRAY_INITIALIZER (vi=variableInitializer[block] {vis.append(vi)})*)
    ;

throwsClause
    @decorate { @tracer }
    :   ^(THROWS_CLAUSE qualifiedIdentifier+)
    ;


modifierList[block]
returns [modifiers]
    @decorate { @tracer }
    @init {
        modifiers = []
    }
    :   ^(MODIFIER_LIST (modifier[block] {modifiers.append($modifier.text)})*)
    ;


modifier[block]
    @decorate { @tracer }
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
    |   localModifier[block]
    ;


localModifierList[block]
    @decorate { @tracer }
    :   ^(LOCAL_MODIFIER_LIST localModifier[block]*)
    ;


localModifier[block]
    @decorate { @tracer }
    :   FINAL
    |   annotation[block]
    ;


type
returns [typ]
    @decorate { @tracer }
    :   ^(TYPE
            ((p=primitiveType {typ=p}) |
             (q=qualifiedTypeIdent {typ=q})) arrayDeclaratorList?)
    ;


qualifiedTypeIdent
returns [qtid]
    @decorate { @tracer }
    @init { idents = [] }
    @after { qtid = ",".join(idents) }
    :   ^(QUALIFIED_TYPE_IDENT (t=typeIdent {idents.append(t)})+)
    ;


typeIdent
returns [tid]
    @decorate { @tracer }
    :   ^(IDENT {tid=$IDENT.text} genericTypeArgumentList?)
    ;


primitiveType
returns [ptype]
    @decorate { @tracer }
    :   BOOLEAN {ptype=$BOOLEAN.text}
    |   CHAR {ptype=$CHAR.text}
    |   BYTE {ptype=$BYTE.text}
    |   SHORT {ptype=$SHORT.text}
    |   INT {ptype=$INT.text}
    |   LONG {ptype=$LONG.text}
    |   FLOAT {ptype=$FLOAT.text}
    |   DOUBLE {ptype=$DOUBLE.text}
    ;


genericTypeArgumentList
    @decorate { @tracer }
    :   ^(GENERIC_TYPE_ARG_LIST genericTypeArgument+)
    ;

genericTypeArgument
    @decorate { @tracer }
    :   type
    |   ^(QUESTION genericWildcardBoundType?)
    ;

genericWildcardBoundType
    @decorate { @tracer }
    :   ^(EXTENDS type)
    |   ^(SUPER type)
    ;

formalParameterList[block]
returns [parameters]
    @decorate { @tracer }
    @init {
        parameters = []
    }
    :   ^(FORMAL_PARAM_LIST
            (p=formalParameterStandardDecl[block] {parameters.append(p)})*
            formalParameterVarargDecl[block]?
        )
    ;

formalParameterStandardDecl[block]
returns [param]
    @decorate { @tracer }
    :   ^(FORMAL_PARAM_STD_DECL
            localModifierList[block]
            t=type
            v=variableDeclaratorId
        )
        {
        param = (t or "", v or "")
        }
    ;

formalParameterVarargDecl[block]
    @decorate { @tracer }
    :   ^(FORMAL_PARAM_VARARG_DECL localModifierList[block] type variableDeclaratorId)
    ;


qualifiedIdentifier
returns [qid]
    @decorate { @tracer }
    :   IDENT {qid=$IDENT.text}
    |   ^(DOT q=qualifiedIdentifier IDENT {qid=(q or "") + "." + $IDENT.text})
    ;


// ANNOTATIONS
annotationList[block]
    @decorate { @tracer }
    :   ^(ANNOTATION_LIST annotation[block]*)
    ;

annotation[block]
    @decorate { @tracer }
    :   ^(AT qualifiedIdentifier annotationInit[block]?)
    ;

annotationInit[block]
    @decorate { @tracer }
    :   ^(ANNOTATION_INIT_BLOCK annotationInitializers[block])
    ;

annotationInitializers[block]
    @decorate { @tracer }
    :   ^(ANNOTATION_INIT_KEY_LIST annotationInitializer[block]+)
    |   ^(ANNOTATION_INIT_DEFAULT_KEY annotationElementValue[block])
    ;

annotationInitializer[block]
    @decorate { @tracer }
    :   ^(IDENT annotationElementValue[block])
    ;

annotationElementValue[block]
returns [ev]
    @decorate { @tracer }
    :   ^(ANNOTATION_INIT_ARRAY_ELEMENT annotationElementValue[block]*)
    |   (an=annotation[block] {ev=an})
    |   (ex=expression[block] {ev=ex})
    ;

annotationTopLevelScope[cls]
returns [blk]
    @decorate { @tracer }
    @init {
        blk = []
    }
    :   ^(ANNOTATION_TOP_LEVEL_SCOPE (b=annotationScopeDeclarations[cls] {blk.append(b)})*)
    ;

annotationScopeDeclarations[source]
returns [decls]
    @decorate { @tracer }
    @init {
        decls = []
    }
    :   ^(ANNOTATION_METHOD_DECL
          modifiers=modifierList[source]
          t=type IDENT
          (av=annotationDefaultValue[source])?
        )
        {
            meth = source.newMethod($IDENT.text)
            meth.addModifiers(modifiers)
            if av:
                pass
            else:
                pass
        }
    |   ^(VAR_DECLARATION modifiers=modifierList[source] t0=type variableDeclaratorList[source])
        {
            decls.append([t0, ""])
        }
    |   typeDeclaration
    ;

annotationDefaultValue[block]
returns [v]
    @decorate { @tracer }
    :   ^(DEFAULT (a=annotationElementValue[block] {v=a}))
    ;


block[source]
returns [statements]
    @decorate { @tracer }
    @init {
        statements = []
    }
    :   ^(BLOCK_SCOPE (s=blockStatement[source] {if 0:source.addSource(s)})*)
    ;


blockStatement[source]
returns [exp]
    @decorate { @tracer }
    :   (v=localVariableDeclaration[source] {exp=v})
    |   (t=typeDeclaration {exp=t})
    |   (s=statement[source] {exp=s; source.addSource(exp)})
    ;


localVariableDeclaration[source]
returns [decl]
    @decorate { @tracer }
    :   ^(VAR_DECLARATION
          localModifierList[source]
          type
          (vds=variableDeclaratorList[source] {decl=vds})
        )
        {
            for name, value in vds:
                if value is None:
                    value = typeValueMap.get(t, 'None')
                var = source.newVariable()
                var.setName(name)
                var.setExpression(value)
                source.addSource( ("\%s = \%s", (("\%s", name, ), ("\%s", value, ))) )
        }


    ;


statement[block]
returns [s]
    @decorate { @tracer }
    :   x=block[None] {s=x}
    |   ^(ASSERT expression[block] expression[block]?)
    |   ^(IF parenthesizedExpression statement[block] statement[block]?)
    |   ^(FOR forInit forCondition forUpdater statement[block])
    |   ^(FOR_EACH localModifierList[block] type IDENT expression[block] statement[block])
    |   ^(WHILE parenthesizedExpression statement[block])
    |   ^(DO statement[block] parenthesizedExpression)
        // The second optional block is the optional finally block.
    |   ^(TRY block[None] catches[block]? block[None]?)
    |   ^(SWITCH parenthesizedExpression switchBlockLabels)
    |   ^(SYNCHRONIZED parenthesizedExpression block[None])
    |   ^(RETURN expression[block]?)
    |   ^(THROW expression[block])
    |   ^(BREAK IDENT?)
    |   ^(CONTINUE IDENT?)
    |   ^(LABELED_STATEMENT IDENT statement[block])
    |   x=expression[block] {
        s=x
        }
    |   SEMI // Empty statement.
    ;


catches[block]
    @decorate { @tracer }
    :   ^(CATCH_CLAUSE_LIST catchClause[block]+)
    ;


catchClause[block]
    @decorate { @tracer }
    :   ^(CATCH formalParameterStandardDecl[block] block[None])
    ;


switchBlockLabels
    @decorate { @tracer }
    :   ^(SWITCH_BLOCK_LABEL_LIST switchCaseLabel* switchDefaultLabel? switchCaseLabel*)
    ;


switchCaseLabel
    @decorate { @tracer }
    :   ^(CASE expression[block] blockStatement[None]*)
    ;


switchDefaultLabel
    @decorate { @tracer }
    :   ^(DEFAULT blockStatement[None]*)
    ;


forInit
    @decorate { @tracer }
    :   ^(FOR_INIT (localVariableDeclaration[None] | expression[block]*)?)
    ;


forCondition
    @decorate { @tracer }
    :   ^(FOR_CONDITION expression[block]?)
    ;


forUpdater
    @decorate { @tracer }
    :   ^(FOR_UPDATE expression[block]*)
    ;


parenthesizedExpression
    @decorate { @tracer }
    :   ^(PARENTESIZED_EXPR expression[block])
    ;


expression[block]
returns[exp]
    @decorate { @tracer }
    :   ^(EXPR result=expr[block]) {exp = $result.text }
    ;


expr[block]
returns[exp]
    @decorate { @tracer }
    :   ^(ASSIGN expr[block] expr[block] {exp="BADVAL"})
    |   ^(PLUS_ASSIGN expr[block] expr[block])
    |   ^(MINUS_ASSIGN expr[block] expr[block])
    |   ^(STAR_ASSIGN expr[block] expr[block])
    |   ^(DIV_ASSIGN expr[block] expr[block])
    |   ^(AND_ASSIGN expr[block] expr[block])
    |   ^(OR_ASSIGN expr[block] expr[block])
    |   ^(XOR_ASSIGN expr[block] expr[block])
    |   ^(MOD_ASSIGN expr[block] expr[block])
    |   ^(BIT_SHIFT_RIGHT_ASSIGN expr[block] expr[block])
    |   ^(SHIFT_RIGHT_ASSIGN expr[block] expr[block])
    |   ^(SHIFT_LEFT_ASSIGN expr[block] expr[block])
    |   ^(QUESTION expr[block] expr[block] expr[block])
    |   ^(LOGICAL_OR expr[block] expr[block])
    |   ^(LOGICAL_AND expr[block] expr[block])
    |   ^(OR expr[block] expr[block])
    |   ^(XOR expr[block] expr[block])
    |   ^(AND expr[block] expr[block])
    |   ^(EQUAL expr[block] expr[block])
    |   ^(NOT_EQUAL expr[block] expr[block])
    |   ^(INSTANCEOF expr[block] type)
    |   ^(LESS_OR_EQUAL expr[block] expr[block])
    |   ^(GREATER_OR_EQUAL expr[block] expr[block])
    |   ^(BIT_SHIFT_RIGHT expr[block] expr[block])
    |   ^(SHIFT_RIGHT expr[block] expr[block])
    |   ^(GREATER_THAN expr[block] expr[block])
    |   ^(SHIFT_LEFT expr[block] expr[block])
    |   ^(LESS_THAN expr[block] expr[block])
    |   ^(PLUS expr[block] expr[block])
    |   ^(MINUS expr[block] expr[block])
    |   ^(STAR expr[block] expr[block])
    |   ^(DIV expr[block] expr[block])
    |   ^(MOD expr[block] expr[block])
    |   ^(UNARY_PLUS expr[block])
    |   ^(UNARY_MINUS expr[block])
    |   ^(PRE_INC expr[block])
    |   ^(PRE_DEC expr[block])
    |   ^(POST_INC expr[block])
    |   ^(POST_DEC expr[block])
    |   ^(NOT expr[block])
    |   ^(LOGICAL_NOT expr[block])
    |   ^(CAST_EXPR type expr[block])
    |   ex=primaryExpression[block] {exp=ex}
    ;

primaryExpression[block]
returns [expression]
    @decorate { @tracer }
    :   ^(  DOT
            (   dotexpr=primaryExpression[block]
                (   id0=IDENT
                |   THIS
                |   SUPER
                |   ex1=innerNewExpression
                |   ex=CLASS
                )
            |   primitiveType ex=CLASS
            |   VOID ex=CLASS
            )
        )
        {
        retval = ("\%s.\%s", (dotexpr, (ex, )))
        }

    |   parenthesizedExpression
    |   id1=IDENT {retval=id1}
    |   ^(METHOD_CALL
            expression2=primaryExpression[block]
            genericTypeArgumentList?
            argl=arguments[block]
        )
        {
        #retval = expression2
        if argl:
            retval = ("\%s(\%s)", (expression2, argl))
        else:
            retval = ("\%s()", expression or "")
        }
    |   explicitConstructorCall[block]
    |   ^(ARRAY_ELEMENT_ACCESS primaryExpression[block] expression[block])
    |   ex4=literal {retval=ex4}
    |   newExpression[block]
    |   THIS {exp = ("\%s", "self")}
    |   arrayTypeDeclarator
    |   SUPER {exp = ("\%s", "super")}
    ;


explicitConstructorCall[block]
    @decorate { @tracer }
    :   ^(THIS_CONSTRUCTOR_CALL genericTypeArgumentList? arguments[block])
    |   ^(SUPER_CONSTRUCTOR_CALL primaryExpression[block]? genericTypeArgumentList? arguments[block])
    ;


arrayTypeDeclarator
    @decorate { @tracer }
    :   ^(ARRAY_DECLARATOR (arrayTypeDeclarator | qualifiedIdentifier | primitiveType))
    ;


newExpression[block]
    @decorate { @tracer }
    :   ^(  STATIC_ARRAY_CREATOR
            (   primitiveType newArrayConstruction[block]
            |   genericTypeArgumentList? qualifiedTypeIdent newArrayConstruction[block]
            )
        )
    |   ^(CLASS_CONSTRUCTOR_CALL
          genericTypeArgumentList?
          qualifiedTypeIdent
          arguments[block]
          classTopLevelScope[block]?
        )
    ;


innerNewExpression
    @decorate { @tracer }
    // something like 'InnerType innerType = outer.new InnerType();'
    :   ^(CLASS_CONSTRUCTOR_CALL
          genericTypeArgumentList?
          IDENT
          arguments[block]
          classTopLevelScope[block]?
        )
    ;


newArrayConstruction[block]
    @decorate { @tracer }
    :   arrayDeclaratorList arrayInitializer
    |   expression[block]+ arrayDeclaratorList?
    ;


arguments[block]
returns[args]
    @decorate { @tracer }
    @init {
        args = []
    }
    @after {
        retval = args
    }
    :   ^(ARGUMENT_LIST (exp=expression[block] {args.append(exp)})*)
    ;


literal
returns[lit]
    @decorate { @tracer }
    :   v=HEX_LITERAL {lit=$v.text}
    |   v=OCTAL_LITERAL {lit=$v.text}
    |   v=DECIMAL_LITERAL {lit=$v.text}
    |   v=FLOATING_POINT_LITERAL {lit=$v.text}
    |   v=CHARACTER_LITERAL {lit=$v.text}
    |   v=STRING_LITERAL {lit=$v.text}
    |   TRUE {lit=True}
    |   FALSE {lit=False}
    |   NULL {lit=None}
    ;
