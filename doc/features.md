.. _features:

********************
Translation Features
********************

The |j2py| package can translate any syntactically valid Java source
code file.  The generated Python code is not guaranteed to run, nor is
guaranteed to be syntatically valid Python.  However, |j2py| works
well many cases, and in some of those, it creates perfectly usable and
workable Python code.

The remainder of this chapter describes how Java language features are
translated into Python constructs.


General Approach
================

The approach taken by |j2py| is to favor readability over correctness
for two reasons: first, it is quite rare to find Java source code that
will can be translated directly to Python without modification because
of semantic and run-time differences, and second, |j2py| is meant to
aid in one-time and ongoing translation projects.


What Works Well (Unless You Try Really Hard to Break It)
========================================================


What Works Mostly (Or Sometimes if You're Lucky)
================================================


What Works Barely (Or Not at All)
=================================


A (Mostly) Complete List
=========================

The following list is an edited version of the grammar presented in
JLS3.  The list has been edited for clarity and conciseness and |j2py|
support for each construct is noted as well.

http://java.sun.com/docs/books/jls/third_edition/html/syntax.html






  * ``Identifier: IDENTIFIER``

    |j2py| copies identifiers from source to target, modifying the value only when:

    * the identifier conflicts with a Python keyword or builtin, or
    * the identifier has an explicit lexical transformation

  * ``QualifiedIdentifier: Identifier { . Identifier }``

    Same behavior as Identifier; each value is examined and transformed individullly

  * ``Literal: IntegerLiteral | FloatingPointLiteral | CharacterLiteral | StringLiteral | BooleanLiteral | NullLiteral``

    Literals are copied from source to target with the following modifications:

    * ``null`` is changed to ``None``
    * ``false`` is changed to ``False``
    * ``true`` is changed to ``True``
    * if necessary, floating point literals are modified to become valid Python values
    * string and character literals are translated as Python strings

    Transformation of literal values happens at the AST level; see the
    ``astTransforms`` configuration value for details.

    * ``Expression: Expression1 [AssignmentOperator Expression1]]``

      Refer to the individual expression types below.

    * ``AssignmentOperator:
        =
        +=
        -=
        *=
        /=
        &=
        |=
        ^=
        %=
        <<=
        >>=
        >>>=
        ``


Type:
        Identifier [TypeArguments]{   .   Identifier [TypeArguments]} {[]}
        BasicType

TypeArguments:
        < TypeArgument {, TypeArgument} >

TypeArgument:
        Type
        ? [( extends |super ) Type]

StatementExpression:
        Expression

ConstantExpression:
        Expression

Expression1:
        Expression2 [Expression1Rest]

Expression1Rest:
        ?   Expression   :   Expression1

Expression2 :
        Expression3 [Expression2Rest]

Expression2Rest:
        {InfixOp Expression3}
        Expression3 instanceof Type

InfixOp:
        ||
        &&
        |
        ^
        &
        ==
        !=
        <
        >
        <=
        >=
        <<
        >>
        >>>
        +
        -
        *
        /
        %

Expression3:
        PrefixOp Expression3
        (   Expression | Type   )   Expression3
        Primary {Selector} {PostfixOp}

Primary:
        ParExpression
        NonWildcardTypeArguments (ExplicitGenericInvocationSuffix | this
Arguments)
  this [Arguments]
  super SuperSuffix
        Literal
  new Creator
        Identifier { . Identifier }[ IdentifierSuffix]
        BasicType {[]} .class
   void.class

IdentifierSuffix:
        [ ( ] {[]} .   class | Expression ])
        Arguments
        .   ( class | ExplicitGenericInvocation | this | super Arguments | new
[NonWildcardTypeArguments] InnerCreator )

ExplicitGenericInvocation:
        NonWildcardTypeArguments ExplicitGenericInvocationSuffix

NonWildcardTypeArguments:
        < TypeList >


ExplicitGenericInvocationSuffix:
     super SuperSuffix
        Identifier Arguments


PrefixOp:
        ++
        --
        !
        ~
        +
        -

PostfixOp:
        ++
        --

Selector: Selector:
        . Identifier [Arguments]
        . ExplicitGenericInvocation
        . this
   . super SuperSuffix
        . new [NonWildcardTypeArguments] InnerCreator
        [ Expression ]

SuperSuffix:
        Arguments
        . Identifier [Arguments]

BasicType:
  byte
  short
  char
  int
  long
  float
  double
  boolean

Arguments:
        ( [Expression { , Expression }] )

Creator:
        [NonWildcardTypeArguments] CreatedName ( ArrayCreatorRest  |
ClassCreatorRest )

CreatedName:
        Identifier [NonWildcardTypeArguments] {. Identifier
[NonWildcardTypeArguments]}

InnerCreator:
        Identifier ClassCreatorRest

ArrayCreatorRest:
        [ ( ] {[]} ArrayInitializer | Expression ] {[ Expression ]} {[]} )

ClassCreatorRest:
         Arguments [ClassBody]

ArrayInitializer:
        { [VariableInitializer {, VariableInitializer} [,]] }

VariableInitializer:
        ArrayInitializer
        Expression

ParExpression:
        ( Expression )

Block:
        { BlockStatements }

BlockStatements:
        { BlockStatement }

BlockStatement :
        LocalVariableDeclarationStatement
        ClassOrInterfaceDeclaration
        [Identifier :] Statement

LocalVariableDeclarationStatement:
        [final] Type VariableDeclarators   ;

Statement:
        Block
        assert Expression [ : Expression] ;
     if ParExpression Statement [else Statement]
     for ( ForControl ) Statement
     while ParExpression Statement
     do Statement while ParExpression   ;
     try Block ( Catches | [Catches] finally Block )
     switch ParExpression { SwitchBlockStatementGroups }
     synchronized ParExpression Block
     return [Expression] ;
     throw Expression   ;
     break [Identifier]
     continue [Identifier]
        ;
        StatementExpression ;
        Identifier   :   Statement

Catches:
        CatchClause {CatchClause}

CatchClause:
     catch ( FormalParameter ) Block

SwitchBlockStatementGroups:
        { SwitchBlockStatementGroup }

SwitchBlockStatementGroup:
        SwitchLabel BlockStatements

SwitchLabel:
     case ConstantExpression   :
        case EnumConstantName :
        default   :

MoreStatementExpressions:
        { , StatementExpression }

ForControl:
        ForVarControl
        ForInit;   [Expression]   ; [ForUpdate]

ForVarControl
        [final] [Annotations] Type Identifier ForVarControlRest

Annotations:
        Annotation [Annotations]

Annotation:
        @ TypeName [( [Identifier =] ElementValue)]

ElementValue:
        ConditionalExpression
        Annotation
        ElementValueArrayInitializer

ConditionalExpression:
        Expression2 Expression1Rest

    ElementValueArrayInitializer:
        { [ElementValues] [,] }

    ElementValues:
        ElementValue [ElementValues]

ForVarControlRest:
        VariableDeclaratorsRest;   [Expression]   ;   [ForUpdate]
        : Expression

ForInit:
        StatementExpression Expressions

Modifier:
  Annotation
  public
  protected
  private
  static
  abstract
  final
  native
  synchronized
  transient
  volatile
        strictfp

VariableDeclarators:
        VariableDeclarator { ,   VariableDeclarator }

VariableDeclaratorsRest:
        VariableDeclaratorRest { ,   VariableDeclarator }

ConstantDeclaratorsRest:
        ConstantDeclaratorRest { ,   ConstantDeclarator }

VariableDeclarator:
        Identifier VariableDeclaratorRest

ConstantDeclarator:
        Identifier ConstantDeclaratorRest

VariableDeclaratorRest:
        {[]} [  =   VariableInitializer]

ConstantDeclaratorRest:
        {[]} =   VariableInitializer

VariableDeclaratorId:
        Identifier {[]}

CompilationUnit:
        [[Annotations] package QualifiedIdentifier   ;  ] {ImportDeclaration}
{TypeDeclaration}

ImportDeclaration:
     import [ static] Identifier {   .   Identifier } [   .     *   ] ;

TypeDeclaration:
        ClassOrInterfaceDeclaration
        ;

ClassOrInterfaceDeclaration:
        {Modifier} (ClassDeclaration | InterfaceDeclaration)

ClassDeclaration:
        NormalClassDeclaration
        EnumDeclaration

NormalClassDeclaration:
     class Identifier [TypeParameters] [extends Type] [implements TypeList]
ClassBody

TypeParameters:
        < TypeParameter {, TypeParameter} >

TypeParameter:
        Identifier [extends Bound]

Bound:
         Type {& Type}


EnumDeclaration:
        enum Identifier [implements TypeList] EnumBody

EnumBody:
        { [EnumConstants] [,] [EnumBodyDeclarations] }

EnumConstants:
        EnumConstant
        EnumConstants , EnumConstant

EnumConstant:
        Annotations Identifier [Arguments] [ClassBody]

EnumBodyDeclarations:
        ; {ClassBodyDeclaration}

InterfaceDeclaration:
        NormalInterfaceDeclaration
        AnnotationTypeDeclaration

NormalInterfaceDeclaration:
     interface Identifier [ TypeParameters] [extends TypeList] InterfaceBody

TypeList:
        Type {  ,   Type}

AnnotationTypeDeclaration:
        @ interface Identifier AnnotationTypeBody

    AnnotationTypeBody:
        { [AnnotationTypeElementDeclarations] }

    AnnotationTypeElementDeclarations:
        AnnotationTypeElementDeclaration
        AnnotationTypeElementDeclarations AnnotationTypeElementDeclaration

AnnotationTypeElementDeclaration:
        {Modifier} AnnotationTypeElementRest

AnnotationTypeElementRest:
         Type Identifier AnnotationMethodOrConstantRest;
        ClassDeclaration
        InterfaceDeclaration
        EnumDeclaration
        AnnotationTypeDeclaration

        AnnotationMethodOrConstantRest:
        AnnotationMethodRest
        AnnotationConstantRest

AnnotationMethodRest:
        ( ) [DefaultValue]

AnnotationConstantRest:
        VariableDeclarators


    DefaultValue:
        default ElementValue

ClassBody:
        { {ClassBodyDeclaration} }

InterfaceBody:
        { {InterfaceBodyDeclaration} }

ClassBodyDeclaration:
        ;
        [static] Block
        {Modifier} MemberDecl

MemberDecl:
        GenericMethodOrConstructorDecl
        MethodOrFieldDecl
        void Identifier VoidMethodDeclaratorRest
        Identifier ConstructorDeclaratorRest
        InterfaceDeclaration
        ClassDeclaration

GenericMethodOrConstructorDecl:
        TypeParameters GenericMethodOrConstructorRest

GenericMethodOrConstructorRest:
        (Type | void) Identifier MethodDeclaratorRest
        Identifier ConstructorDeclaratorRest

MethodOrFieldDecl:
        Type Identifier MethodOrFieldRest

MethodOrFieldRest:
        VariableDeclaratorRest
        MethodDeclaratorRest

InterfaceBodyDeclaration:
        ;
        {Modifier} InterfaceMemberDecl

InterfaceMemberDecl:
        InterfaceMethodOrFieldDecl
        InterfaceGenericMethodDecl
        void Identifier VoidInterfaceMethodDeclaratorRest
        InterfaceDeclaration
        ClassDeclaration

InterfaceMethodOrFieldDecl:
        Type Identifier InterfaceMethodOrFieldRest

InterfaceMethodOrFieldRest:
        ConstantDeclaratorsRest ;
        InterfaceMethodDeclaratorRest

MethodDeclaratorRest:
        FormalParameters {[]} [throws QualifiedIdentifierList] ( MethodBody |   ;
)

VoidMethodDeclaratorRest:
        FormalParameters [throws QualifiedIdentifierList] ( MethodBody |   ;  )

InterfaceMethodDeclaratorRest:
        FormalParameters {[]} [throws QualifiedIdentifierList]   ;

InterfaceGenericMethodDecl:
        TypeParameters (Type | void) Identifier InterfaceMethodDeclaratorRest

VoidInterfaceMethodDeclaratorRest:
        FormalParameters [throws QualifiedIdentifierList]   ;

ConstructorDeclaratorRest:
        FormalParameters [throws QualifiedIdentifierList] MethodBody

QualifiedIdentifierList:
        QualifiedIdentifier {  ,   QualifiedIdentifier}

FormalParameters:
        ( [FormalParameterDecls] )

FormalParameterDecls:
        [final] [Annotations] Type FormalParameterDeclsRest]

FormalParameterDeclsRest:
        VariableDeclaratorId [ , FormalParameterDecls]
        ... VariableDeclaratorId

MethodBody:
        Block

EnumConstantName:
        Identifier
