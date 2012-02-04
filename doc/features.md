## Translation Features

The java2python package can translate any syntactically valid Java source
code file.  The generated Python code is not guaranteed to run, nor is
guaranteed to be syntactically valid Python.  However, java2python works
well many cases, and in some of those, it creates perfectly usable and
workable Python code.


### General Approach

The approach taken by java2python is to favor readability over correctness.

### What Works

#### Identifiers and Qualified Identifiers

java2python copies identifiers from source to target, modifying the value only when:

  * the identifier conflicts with a Python keyword or builtin, or
  * the identifier has an explicit lexical transformation


#### Literals: Integer, Floating Point, Character, String, Boolean and Null

Literals are copied from source to target with the following modifications:

  * `null` is changed to `None`
  * `false` is changed to `False`
  * `true` is changed to `True`
  * if necessary, floating point literals are modified to become valid Python values
  * string and character literals are translated as Python strings

Transformation of literal values happens at the AST level; see the
`astTransforms` configuration value for details.

#### Expressions

##### ConstantExpression

Constant expressions are translated to their Python equivalents.

##### Ternary Expressions

Ternary expressions are translated to their Python form (`val if condition else other`)


#### Prefix Operators

All of the Java prefix operators are supported:

        ++        --    !    ~    +    -

In the case of `++` and `--`, java2python translates to `+= 1` and `-= 1`.  If necessary, those expressions are moved outside of statements.

#### Assignment Operators

All of the following assignment operators are translated into their Python equivalents:
     
    =    +=    -=    *=    /=    &=    |=    ^=    %=    <<=    >>=

The bit shift right (`>>>`)and bit shift assign right (`>>>=`) operators are mapped to a function; if java2python detects code that uses either of these, it replaces the operator with that function and includes the function within the output.  This behavior is controlled by the `modulePrologueHandlers` config item.

#### Infix Operators

The following operators are translated to their Python equivalents:

    ||    &&    |    ^    &    ==    !=    <    >
    <=    >=    <<   >>   >>>  +     -     *    /    %

Refer to the note above regarding bit shift right.

#### Basic Types

The basic Java types are mapped to Python types as follows:

    byte    => int
    short   => int
    char    => str
    int     => int
    long    => long
    float   => float
    double  => float
    boolean => bool

#### Types, Interfaces, Enums

Java classes, interfaces, and enums are translated into Python classes.

In the case of interfaces, the strategy is configurable.  By default,
interfaces are translated to classes utilizing the ABCMeta class.  The package
includes config handlers that can translate to simple classes (inheriting from
`object`), or from Zope Interfaces.

Enums are also translated via a configurable strategy.  By default, enumerated
values are created as class attributes with string values.  The package
includes a config handler to create class attributes with integer values.

#### Statements

##### assert
        
assert Expression [ : Expression] ;

##### if

if ParExpression Statement [else Statement]

##### for

for ( ForControl ) Statement

##### while and do

while ParExpression Statement
     
do Statement while ParExpression   ;

##### try and catch
     
try Block ( Catches | [Catches] finally Block )

##### switch

switch ParExpression { SwitchBlockStatementGroups }

##### synchronized

synchronized ParExpression Block

##### return

return [Expression] ;

##### throw

throw Expression   ;

##### break

break [Identifier]

###### continue

continue [Identifier]



#### Other Keywords:  new, super, this, void.class, instanceof


    this [Arguments]
    super SuperSuffix
        Literal
    new Creator
        Identifier { . Identifier }[ IdentifierSuffix]
        BasicType {[]} .class
    void.class

    ExplicitGenericInvocation:
        NonWildcardTypeArguments ExplicitGenericInvocationSuffix

    NonWildcardTypeArguments:
        < TypeList >


    ExplicitGenericInvocationSuffix:
     super SuperSuffix
        Identifier Arguments

##### Annotations

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

#### The Rest

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
     import [ static] Identifier {   .   Identifier } [   .   *   ] ;

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


http://java.sun.com/docs/books/jls/third_edition/html/syntax.html
