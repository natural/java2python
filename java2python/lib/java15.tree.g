/** Java 1.5 AST Recognizer Grammar
 *
 * Author: (see java.g preamble)
 *
 * This grammar is in the PUBLIC DOMAIN
 */
class JavaTreeParser extends TreeParser;

options {
	importVocab = Java;
}

compilationUnit
	:	(packageDefinition)?
		(importDefinition)*
		(typeDefinition)*
	;

packageDefinition
	:	#( PACKAGE_DEF annotations identifier )
	;

importDefinition
	:	#( IMPORT identifierStar )
	|	#( STATIC_IMPORT identifierStar )
	;

typeDefinition
	:	#(CLASS_DEF modifiers IDENT (typeParameters)? extendsClause implementsClause objBlock )
	|	#(INTERFACE_DEF modifiers IDENT (typeParameters)? extendsClause interfaceBlock )
	|	#(ENUM_DEF modifiers IDENT implementsClause enumBlock )
	|	#(ANNOTATION_DEF modifiers IDENT annotationBlock )
	;

typeParameters
	:	#(TYPE_PARAMETERS (typeParameter)+)
	;

typeParameter
	:	#(TYPE_PARAMETER IDENT (typeUpperBounds)?)
	;

typeUpperBounds
	:	#(TYPE_UPPER_BOUNDS (classOrInterfaceType)+)
	;

typeSpec
	:	#(TYPE typeSpecArray)
	;

typeSpecArray
	:	#( ARRAY_DECLARATOR typeSpecArray )
	|	type
	;

type
	:	classOrInterfaceType
	|	builtInType
	;

classOrInterfaceType
	:	IDENT (typeArguments)?
	|	#( DOT classOrInterfaceType )
	;

typeArguments
	:	#(TYPE_ARGUMENTS (typeArgument)+)
	;

typeArgument
	:	#(	TYPE_ARGUMENT
			(	typeSpec
			|	wildcardType
			)
		)
	;

wildcardType
	:	#(WILDCARD_TYPE (typeArgumentBounds)?)
	;

typeArgumentBounds
	:	#(TYPE_UPPER_BOUNDS (classOrInterfaceType)+)
	|	#(TYPE_LOWER_BOUNDS (classOrInterfaceType)+)
	;

builtInType
	:	"void"
	|	"boolean"
	|	"byte"
	|	"char"
	|	"short"
	|	"int"
	|	"float"
	|	"long"
	|	"double"
	;

modifiers
	:	#( MODIFIERS (modifier)* )
	;

modifier
	:	"private"
	|	"public"
	|	"protected"
	|	"static"
	|	"transient"
	|	"final"
	|	"abstract"
	|	"native"
	|	"threadsafe"
	|	"synchronized"
	|	"const"
	|	"volatile"
	|	"strictfp"
	|	annotation
	;

annotations
	:	#(ANNOTATIONS (annotation)* )
	;

annotation
	:	#(ANNOTATION identifier (annotationMemberValueInitializer | (anntotationMemberValuePair)+)? )
	;

annotationMemberValueInitializer
	:	conditionalExpr | annotation | annotationMemberArrayInitializer
	;

anntotationMemberValuePair
	:	#(ANNOTATION_MEMBER_VALUE_PAIR IDENT annotationMemberValueInitializer)
	;

annotationMemberArrayInitializer
	:	#(ANNOTATION_ARRAY_INIT (annotationMemberArrayValueInitializer)* )
	;

annotationMemberArrayValueInitializer
	:	conditionalExpr | annotation
	;

extendsClause
	:	#(EXTENDS_CLAUSE (classOrInterfaceType)* )
	;

implementsClause
	:	#(IMPLEMENTS_CLAUSE (classOrInterfaceType)* )
	;


interfaceBlock
	:	#(	OBJBLOCK
			(	methodDecl
			|	variableDef
			|	typeDefinition
			)*
		)
	;

objBlock
	:	#(	OBJBLOCK
			(	ctorDef
			|	methodDef
			|	variableDef
			|	typeDefinition
			|	#(STATIC_INIT slist)
			|	#(INSTANCE_INIT slist)
			)*
		)
	;

annotationBlock
	:	#(	OBJBLOCK
			(	annotationFieldDecl
			|	variableDef
			|	typeDefinition
			)*
		)
	;

enumBlock
	:	#(	OBJBLOCK
			(
				enumConstantDef
			)*
			(	ctorDef
			|	methodDef
			|	variableDef
			|	typeDefinition
			|	#(STATIC_INIT slist)
			|	#(INSTANCE_INIT slist)
			)*
		)
	;

ctorDef
	:	#(CTOR_DEF modifiers (typeParameters)? methodHead (slist)?)
	;

methodDecl
	:	#(METHOD_DEF modifiers (typeParameters)? typeSpec methodHead)
	;

methodDef
	:	#(METHOD_DEF modifiers (typeParameters)? typeSpec methodHead (slist)?)
	;

variableDef
	:	#(VARIABLE_DEF modifiers typeSpec variableDeclarator varInitializer)
	;

parameterDef
	:	#(PARAMETER_DEF modifiers typeSpec IDENT )
	;

variableLengthParameterDef
	:	#(VARIABLE_PARAMETER_DEF modifiers typeSpec IDENT )
	;

annotationFieldDecl
	:	#(ANNOTATION_FIELD_DEF modifiers typeSpec IDENT (annotationMemberValueInitializer)?)
	;

enumConstantDef
	:	#(ENUM_CONSTANT_DEF annotations IDENT (elist)? (enumConstantBlock)?)
	;

enumConstantBlock
	:	#(	OBJBLOCK
			(	methodDef
			|	variableDef
			|	typeDefinition
			|	#(INSTANCE_INIT slist)
			)*
		)
	;

objectinitializer
	:	#(INSTANCE_INIT slist)
	;

variableDeclarator
	:	IDENT
	|	LBRACK variableDeclarator
	;

varInitializer
	:	#(ASSIGN initializer)
	|
	;

initializer
	:	expression
	|	arrayInitializer
	;

arrayInitializer
	:	#(ARRAY_INIT (initializer)*)
	;

methodHead
	:	IDENT #( PARAMETERS (parameterDef)* ) (throwsClause)?
	;

throwsClause
	:	#( "throws" (classOrInterfaceType)* )
	;

identifier
	:	IDENT
	|	#( DOT identifier IDENT )
	;

identifierStar
	:	IDENT
	|	#( DOT identifier (STAR|IDENT) )
	;

slist
	:	#( SLIST (stat)* )
	;

stat:	typeDefinition
	|	variableDef
	|	expression
	|	#(LABELED_STAT IDENT stat)
	|	#("if" expression stat (stat)? )
	|	#(	"for"
			(
				#(FOR_INIT ((variableDef)+ | elist)?)
				#(FOR_CONDITION (expression)?)
				#(FOR_ITERATOR (elist)?)
			|
				#(FOR_EACH_CLAUSE parameterDef expression)
			)
			stat
		)
	|	#("while" expression stat)
	|	#("do" stat expression)
	|	#("break" (IDENT)? )
	|	#("continue" (IDENT)? )
	|	#("return" (expression)? )
	|	#("switch" expression (caseGroup)*)
	|	#("throw" expression)
	|	#("synchronized" expression stat)
	|	tryBlock
	|	slist // nested SLIST
	|	#("assert" expression (expression)?)
	|	EMPTY_STAT
	;

caseGroup
	:	#(CASE_GROUP (#("case" expression) | "default")+ slist)
	;

tryBlock
	:	#( "try" slist (handler)* (#("finally" slist))? )
	;

handler
	:	#( "catch" parameterDef slist )
	;

elist
	:	#( ELIST (expression)* )
	;

expression
	:	#(EXPR expr)
	;

expr
	:	conditionalExpr
	|	#(ASSIGN expr expr)			// binary operators...
	|	#(PLUS_ASSIGN expr expr)
	|	#(MINUS_ASSIGN expr expr)
	|	#(STAR_ASSIGN expr expr)
	|	#(DIV_ASSIGN expr expr)
	|	#(MOD_ASSIGN expr expr)
	|	#(SR_ASSIGN expr expr)
	|	#(BSR_ASSIGN expr expr)
	|	#(SL_ASSIGN expr expr)
	|	#(BAND_ASSIGN expr expr)
	|	#(BXOR_ASSIGN expr expr)
	|	#(BOR_ASSIGN expr expr)
	;

conditionalExpr
	:	#(QUESTION expr expr expr)	// trinary operator
	|	#(LOR expr expr)
	|	#(LAND expr expr)
	|	#(BOR expr expr)
	|	#(BXOR expr expr)
	|	#(BAND expr expr)
	|	#(NOT_EQUAL expr expr)
	|	#(EQUAL expr expr)
	|	#(LT expr expr)
	|	#(GT expr expr)
	|	#(LE expr expr)
	|	#(GE expr expr)
	|	#(SL expr expr)
	|	#(SR expr expr)
	|	#(BSR expr expr)
	|	#(PLUS expr expr)
	|	#(MINUS expr expr)
	|	#(DIV expr expr)
	|	#(MOD expr expr)
	|	#(STAR expr expr)
	|	#(INC expr)
	|	#(DEC expr)
	|	#(POST_INC expr)
	|	#(POST_DEC expr)
	|	#(BNOT expr)
	|	#(LNOT expr)
	|	#("instanceof" expr expr)
	|	#(UNARY_MINUS expr)
	|	#(UNARY_PLUS expr)
	|	primaryExpression
	;

primaryExpression
	:	IDENT
	|	#(	DOT
			(	expr
				(	IDENT
				|	arrayIndex
				|	"this"
				|	"class"
				|	newExpression
				|	"super"
				|	(typeArguments)? // for generic methods calls
				)
			|	#(ARRAY_DECLARATOR typeSpecArray)
			|	builtInType ("class")?
			)
		)
	|	arrayIndex
	|	#(METHOD_CALL primaryExpression (typeArguments)? elist)
	|	ctorCall
	|	#(TYPECAST typeSpec expr)
	|	newExpression
	|	constant
	|	"super"
	|	"true"
	|	"false"
	|	"this"
	|	"null"
	|	typeSpec // type name used with instanceof
	;

ctorCall
	:	#( CTOR_CALL elist )
	|	#( SUPER_CTOR_CALL
			(	elist
			|	primaryExpression elist
			)
		 )
	;

arrayIndex
	:	#(INDEX_OP expr expression)
	;

constant
	:	NUM_INT
	|	CHAR_LITERAL
	|	STRING_LITERAL
	|	NUM_FLOAT
	|	NUM_DOUBLE
	|	NUM_LONG
	;

newExpression
	:	#(	"new" (typeArguments)? type
			(	newArrayDeclarator (arrayInitializer)?
			|	elist (objBlock)?
			)
		)

	;

newArrayDeclarator
	:	#( ARRAY_DECLARATOR (newArrayDeclarator)? (expression)? )
	;
