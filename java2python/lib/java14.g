// This file is part of PyANTLR. See LICENSE.txt for license
// details..........Copyright (C) Wolfgang Haefelinger, 2004.
//
// $Id$

options {
    language=Python;
}

class parser extends Parser;
options {
    k = 2;                           // two token lookahead
    exportVocab=Java;                // Call its vocabulary "Java"
    codeGenMakeSwitchThreshold = 2;  // Some optimizations
    codeGenBitsetTestThreshold = 3;
    defaultErrorHandler = false;     // Don't generate parser error handlers
    buildAST = true;
}

tokens {
    BLOCK; MODIFIERS; OBJBLOCK; SLIST; CTOR_DEF; METHOD_DEF; VARIABLE_DEF;
    INSTANCE_INIT; STATIC_INIT; TYPE; CLASS_DEF; INTERFACE_DEF;
    PACKAGE_DEF; ARRAY_DECLARATOR; EXTENDS_CLAUSE; IMPLEMENTS_CLAUSE;
    PARAMETERS; PARAMETER_DEF; LABELED_STAT; TYPECAST; INDEX_OP;
    POST_INC; POST_DEC; METHOD_CALL; EXPR; ARRAY_INIT;
    IMPORT; UNARY_MINUS; UNARY_PLUS; CASE_GROUP; ELIST; FOR_INIT; FOR_CONDITION;
    FOR_ITERATOR; EMPTY_STAT; FINAL="final"; ABSTRACT="abstract";
    STRICTFP="strictfp"; SUPER_CTOR_CALL; CTOR_CALL;
}

// Compilation Unit: In Java, this is a single file.  This is the start
//   rule for this parser
compilationUnit
    :   // A compilation unit starts with an optional package definition
        (   packageDefinition
        |   /* nothing */
        )

        // Next we have a series of zero or more import statements
        ( importDefinition )*

        // Wrapping things up with any number of class or interface
        //    definitions
        ( typeDefinition )*

        EOF!
    ;


// Package statement: "package" followed by an identifier.
packageDefinition
    options {defaultErrorHandler = true;} // let ANTLR handle errors
    :   p:"package"^ {#p.setType(PACKAGE_DEF);} identifier SEMI!
    ;


// Import statement: import followed by a package or class name
importDefinition
    options {defaultErrorHandler = true;}
    :   i:"import"^ {#i.setType(IMPORT);} identifierStar SEMI!
    ;

// A type definition in a file is either a class or interface definition.
typeDefinition
    options {defaultErrorHandler = true;}
    :   m:modifiers!
        ( classDefinition[#m]
        | interfaceDefinition[#m]
        )
    |   SEMI!
    ;

// A declaration is the creation of a reference or primitive-type variable
//  Create a separate Type/Var tree for each var in the var list.
//
declaration!
    :   m:modifiers t:typeSpec[False] v:variableDefinitions[#m,#t]
        {#declaration = #v;}
    ;

// A type specification is a type name with possible brackets afterwards
//   (which would make it an array type).
typeSpec[addImagNode]
    : classTypeSpec[addImagNode]
    | builtInTypeSpec[addImagNode]
    ;

// A class type specification is a class type with possible brackets afterwards
//   (which would make it an array type).
classTypeSpec[addImagNode]
    :   identifier (lb:LBRACK^ {#lb.setType(ARRAY_DECLARATOR);} RBRACK!)*
        {
            if addImagNode :
                #classTypeSpec = #(#[TYPE,"TYPE"], #classTypeSpec);
        }
    ;

// A builtin type specification is a builtin type with possible brackets
// afterwards (which would make it an array type).
builtInTypeSpec[addImagNode]
    :   builtInType (lb:LBRACK^ {#lb.setType(ARRAY_DECLARATOR);} RBRACK!)*
        {
            if addImagNode :
                #builtInTypeSpec = #(#[TYPE,"TYPE"], #builtInTypeSpec);
        }
    ;

// A type name. which is either a (possibly qualified) class name or
//   a primitive (builtin) type
type
    :   identifier
    |   builtInType
    ;

// The primitive types.
builtInType
    :   "void"
    |   "boolean"
    |   "byte"
    |   "char"
    |   "short"
    |   "int"
    |   "float"
    |   "long"
    |   "double"
    ;

// A (possibly-qualified) java identifier.  We start with the first IDENT
//   and expand its name by adding dots and following IDENTS
identifier
    :   IDENT  ( DOT^ IDENT )*
    ;

identifierStar
    :   IDENT
        ( DOT^ IDENT )*
        ( DOT^ STAR  )?
    ;

// A list of zero or more modifiers.  We could have used (modifier)* in
//   place of a call to modifiers, but I thought it was a good idea to keep
//   this rule separate so they can easily be collected in a Vector if
//   someone so desires
modifiers
    :   ( modifier )*
        {#modifiers = #([MODIFIERS, "MODIFIERS"], #modifiers);}
    ;

// modifiers for Java classes, interfaces, class/instance vars and methods
modifier
    :   "private"
    |   "public"
    |   "protected"
    |   "static"
    |   "transient"
    |   "final"
    |   "abstract"
    |   "native"
    |   "threadsafe"
    |   "synchronized"
//  |   "const"         // reserved word, but not valid
    |   "volatile"
    |   "strictfp"
    ;

// Definition of a Java class
classDefinition![modifiers]
    :   "class" IDENT
        // it _might_ have a superclass...
        sc:superClassClause
        // it might implement some interfaces...
        ic:implementsClause
        // now parse the body of the class
        cb:classBlock
        {#classDefinition = #(#[CLASS_DEF,"CLASS_DEF"],
                               modifiers,IDENT,sc,ic,cb);}
    ;

superClassClause!
    :   ( "extends" id:identifier )?
        {#superClassClause = #(#[EXTENDS_CLAUSE,"EXTENDS_CLAUSE"],id);}
    ;

// Definition of a Java Interface
interfaceDefinition![modifiers]
    :   "interface" IDENT
        // it might extend some other interfaces
        ie:interfaceExtends
        // now parse the body of the interface (looks like a class...)
        cb:classBlock
        {#interfaceDefinition = #(#[INTERFACE_DEF,"INTERFACE_DEF"],
                                    modifiers,IDENT,ie,cb);}
    ;


// This is the body of a class.  You can have fields and extra semicolons,
// That's about it (until you see what a field is...)
classBlock
    :   LCURLY!
            ( field | SEMI! )*
        RCURLY!
        {#classBlock = #([OBJBLOCK, "OBJBLOCK"], #classBlock);}
    ;

// An interface can extend several other interfaces...
interfaceExtends
    :   (
        e:"extends"!
        identifier ( COMMA! identifier )*
        )?
        {#interfaceExtends = #(#[EXTENDS_CLAUSE,"EXTENDS_CLAUSE"],
                            #interfaceExtends);}
    ;

// A class can implement several interfaces...
implementsClause
    :   (
            i:"implements"! identifier ( COMMA! identifier )*
        )?
        {#implementsClause = #(#[IMPLEMENTS_CLAUSE,"IMPLEMENTS_CLAUSE"],
                                 #implementsClause);}
    ;

// Now the various things that can be defined inside a class or interface...
// Note that not all of these are really valid in an interface (constructors,
//   for example), and if this grammar were used for a compiler there would
//   need to be some semantic checks to make sure we're doing the right thing...
field!
    :   // method, constructor, or variable declaration
        mods:modifiers
        (   h:ctorHead s:constructorBody // constructor
            {#field = #(#[CTOR_DEF,"CTOR_DEF"], mods, h, s);}

        |   cd:classDefinition[#mods]       // inner class
            {#field = #cd;}

        |   id:interfaceDefinition[#mods]   // inner interface
            {#field = #id;}

        |   t:typeSpec[False]  // method or variable declaration(s)
            (   IDENT  // the name of the method

                // parse the formal parameter declarations.
                LPAREN! param:parameterDeclarationList RPAREN!

                rt:declaratorBrackets[#t]

                // get the list of exceptions that this method is
                // declared to throw
                (tc:throwsClause)?

                ( s2:compoundStatement | SEMI )
                {#field = #(#[METHOD_DEF,"METHOD_DEF"],
                             mods,
                             #(#[TYPE,"TYPE"],rt),
                             IDENT,
                             param,
                             tc,
                             s2);}
            |   v:variableDefinitions[#mods,#t] SEMI
//              {#field = #(#[VARIABLE_DEF,"VARIABLE_DEF"], v);}
                {#field = #v;}
            )
        )

    // "static { ... }" class initializer
    |   "static" s3:compoundStatement
        {#field = #(#[STATIC_INIT,"STATIC_INIT"], s3);}

    // "{ ... }" instance initializer
    |   s4:compoundStatement
        {#field = #(#[INSTANCE_INIT,"INSTANCE_INIT"], s4);}
    ;

constructorBody
    :   lc:LCURLY^ {#lc.setType(SLIST);}
            ( options { greedy=true; } : explicitConstructorInvocation)?
            (statement)*
        RCURLY!
    ;

// Catch obvious constructor calls, but not the expr.super(...) calls */
explicitConstructorInvocation
    :   "this"! lp1:LPAREN^ argList RPAREN! SEMI!
        {#lp1.setType(CTOR_CALL);}
    |   "super"! lp2:LPAREN^ argList RPAREN! SEMI!
        {#lp2.setType(SUPER_CTOR_CALL);}
    ;

variableDefinitions[mods,t]
    :   variableDeclarator[antlr.dupTree(mods,self.getASTFactory()),antlr.dupTree(t,self.getASTFactory())]
        (   COMMA!
            variableDeclarator[antlr.dupTree(mods,self.getASTFactory()),
                               antlr.dupTree(t,self.getASTFactory())]
        )*
    ;

// Declaration of a variable.  This can be a class/instance variable,
//   or a local variable in a method
// It can also include possible initialization.
//
variableDeclarator![mods,t]
    :   id:IDENT d:declaratorBrackets[t] v:varInitializer
        {#variableDeclarator = #(#[VARIABLE_DEF,"VARIABLE_DEF"], mods, #(#[TYPE,"TYPE"],d), id, v);}
    ;

declaratorBrackets[typ]
    :   {#declaratorBrackets=typ;}
        (lb:LBRACK^ {#lb.setType(ARRAY_DECLARATOR);} RBRACK!)*
    ;

varInitializer
    :   ( ASSIGN^ initializer )?
    ;

// This is an initializer used to set up an array.
arrayInitializer
    :   lc:LCURLY^ {#lc.setType(ARRAY_INIT);}
            (   initializer
                (
                    // CONFLICT: does a COMMA after an initializer start a new
                    //           initializer or start the option ',' at end?
                    //           ANTLR generates proper code by matching
                    //           the comma as soon as possible.
                    options {
                        warnWhenFollowAmbig = false;
                    }
                :
                    COMMA! initializer
                )*
                (COMMA!)?
            )?
        RCURLY!
    ;


// The two "things" that can initialize an array element are an expression
//   and another (nested) array initializer.
initializer
    :   expression
    |   arrayInitializer
    ;

// This is the header of a method.  It includes the name and parameters
//   for the method.
//   This also watches for a list of exception classes in a "throws" clause.
ctorHead
    :   IDENT  // the name of the method

        // parse the formal parameter declarations.
        LPAREN! parameterDeclarationList RPAREN!

        // get the list of exceptions that this method is declared to throw
        (throwsClause)?
    ;

// This is a list of exception classes that the method is declared to throw
throwsClause
    :   "throws"^ identifier ( COMMA! identifier )*
    ;


// A list of formal parameters
parameterDeclarationList
    :   ( parameterDeclaration ( COMMA! parameterDeclaration )* )?
        {#parameterDeclarationList = #(#[PARAMETERS,"PARAMETERS"],
                                    #parameterDeclarationList);}
    ;

// A formal parameter.
parameterDeclaration!
    :   pm:parameterModifier t:typeSpec[False] id:IDENT
        pd:declaratorBrackets[#t]
        {#parameterDeclaration = #(#[PARAMETER_DEF,"PARAMETER_DEF"],
                                    pm, #([TYPE,"TYPE"],pd), id);}
    ;

parameterModifier
    :   (f:"final")?
        {#parameterModifier = #(#[MODIFIERS,"MODIFIERS"], f);}
    ;

// Compound statement.  This is used in many contexts:
//   Inside a class definition prefixed with "static":
//      it is a class initializer
//   Inside a class definition without "static":
//      it is an instance initializer
//   As the body of a method
//   As a completely indepdent braced block of code inside a method
//      it starts a new scope for variable definitions

compoundStatement
    :   lc:LCURLY^ {#lc.setType(SLIST);}
            // include the (possibly-empty) list of statements
            (statement)*
        RCURLY!
    ;


statement
    // A list of statements in curly braces -- start a new scope!
    :   compoundStatement

    // declarations are ambiguous with "ID DOT" relative to expression
    // statements.  Must backtrack to be sure.  Could use a semantic
    // predicate to test symbol table to see what the type was coming
    // up, but that's pretty hard without a symbol table ;)
    |   (declaration)=> declaration SEMI!

    // An expression statement.  This could be a method call,
    // assignment statement, or any other expression evaluated for
    // side-effects.
    |   expression SEMI!

    // class definition
    |   m:modifiers! classDefinition[#m]

    // Attach a label to the front of a statement
    |   IDENT c:COLON^ {#c.setType(LABELED_STAT);} statement

    // If-else statement
    |   "if"^ LPAREN! expression RPAREN! statement
        (
            // CONFLICT: the old "dangling-else" problem...
            //           ANTLR generates proper code matching
            //           as soon as possible.  Hush warning.
            options {
                warnWhenFollowAmbig = false;
            }
        :
            "else"! statement
        )?

    // For statement
    |   "for"^
            LPAREN!
                forInit SEMI!   // initializer
                forCond SEMI!   // condition test
                forIter         // updater
            RPAREN!
            statement                     // statement to loop over

    // While statement
    |   "while"^ LPAREN! expression RPAREN! statement

    // do-while statement
    |   "do"^ statement "while"! LPAREN! expression RPAREN! SEMI!

    // get out of a loop (or switch)
    |   "break"^ (IDENT)? SEMI!

    // do next iteration of a loop
    |   "continue"^ (IDENT)? SEMI!

    // Return an expression
    |   "return"^ (expression)? SEMI!

    // switch/case statement
    |   "switch"^ LPAREN! expression RPAREN! LCURLY!
            ( casesGroup )*
        RCURLY!

    // exception try-catch block
    |   tryBlock

    // throw an exception
    |   "throw"^ expression SEMI!

    // synchronize a statement
    |   "synchronized"^ LPAREN! expression RPAREN! compoundStatement

    // asserts (uncomment if you want 1.4 compatibility)
    // |    "assert"^ expression ( COLON! expression )? SEMI!

    // empty statement
    |   s:SEMI {#s.setType(EMPTY_STAT);}
    ;

casesGroup
    :   (   // CONFLICT: to which case group do the statements bind?
            //           ANTLR generates proper code: it groups the
            //           many "case"/"default" labels together then
            //           follows them with the statements
            options {
                greedy = true;
            }
            :
            aCase
        )+
        caseSList
        {#casesGroup = #([CASE_GROUP, "CASE_GROUP"], #casesGroup);}
    ;

aCase
    :   ("case"^ expression | "default") COLON!
    ;

caseSList
    :   (statement)*
        {#caseSList = #(#[SLIST,"SLIST"],#caseSList);}
    ;

// The initializer for a for loop
forInit
        // if it looks like a declaration, it is
    :   (   (declaration)=> declaration
        // otherwise it could be an expression list...
        |   expressionList
        )?
        {#forInit = #(#[FOR_INIT,"FOR_INIT"],#forInit);}
    ;

forCond
    :   (expression)?
        {#forCond = #(#[FOR_CONDITION,"FOR_CONDITION"],#forCond);}
    ;

forIter
    :   (expressionList)?
        {#forIter = #(#[FOR_ITERATOR,"FOR_ITERATOR"],#forIter);}
    ;

// an exception handler try/catch block
tryBlock
    :   "try"^ compoundStatement
        (handler)*
        ( finallyClause )?
    ;

finallyClause
    :   "finally"^ compoundStatement
    ;

// an exception handler
handler
    :   "catch"^ LPAREN! parameterDeclaration RPAREN! compoundStatement
    ;


// expressions
// Note that most of these expressions follow the pattern
//   thisLevelExpression :
//       nextHigherPrecedenceExpression
//           (OPERATOR nextHigherPrecedenceExpression)*
// which is a standard recursive definition for a parsing an expression.
// The operators in java have the following precedences:
//    lowest  (13)  = *= /= %= += -= <<= >>= >>>= &= ^= |=
//            (12)  ?:
//            (11)  ||
//            (10)  &&
//            ( 9)  |
//            ( 8)  ^
//            ( 7)  &
//            ( 6)  == !=
//            ( 5)  < <= > >=
//            ( 4)  << >>
//            ( 3)  +(binary) -(binary)
//            ( 2)  * / %
//            ( 1)  ++ -- +(unary) -(unary)  ~  !  (type)
//                  []   () (method call)  . (dot -- identifier qualification)
//                  new   ()  (explicit parenthesis)
//
// the last two are not usually on a precedence chart; I put them in
// to point out that new has a higher precedence than '.', so you
// can validy use
//     new Frame().show()
//
// Note that the above precedence levels map to the rules below...
// Once you have a precedence chart, writing the appropriate rules as below
//   is usually very straightfoward



// the mother of all expressions
expression
    :   assignmentExpression
        {#expression = #(#[EXPR,"EXPR"],#expression);}
    ;


// This is a list of expressions.
expressionList
    :   expression (COMMA! expression)*
        {#expressionList = #(#[ELIST,"ELIST"], expressionList);}
    ;


// assignment expression (level 13)
assignmentExpression
    :   conditionalExpression
        (   (   ASSIGN^
            |   PLUS_ASSIGN^
            |   MINUS_ASSIGN^
            |   STAR_ASSIGN^
            |   DIV_ASSIGN^
            |   MOD_ASSIGN^
            |   SR_ASSIGN^
            |   BSR_ASSIGN^
            |   SL_ASSIGN^
            |   BAND_ASSIGN^
            |   BXOR_ASSIGN^
            |   BOR_ASSIGN^
            )
            assignmentExpression
        )?
    ;


// conditional test (level 12)
conditionalExpression
    :   logicalOrExpression
        ( QUESTION^ assignmentExpression COLON! conditionalExpression )?
    ;


// logical or (||)  (level 11)
logicalOrExpression
    :   logicalAndExpression (LOR^ logicalAndExpression)*
    ;


// logical and (&&)  (level 10)
logicalAndExpression
    :   inclusiveOrExpression (LAND^ inclusiveOrExpression)*
    ;


// bitwise or non-short-circuiting or (|)  (level 9)
inclusiveOrExpression
    :   exclusiveOrExpression (BOR^ exclusiveOrExpression)*
    ;


// exclusive or (^)  (level 8)
exclusiveOrExpression
    :   andExpression (BXOR^ andExpression)*
    ;


// bitwise or non-short-circuiting and (&)  (level 7)
andExpression
    :   equalityExpression (BAND^ equalityExpression)*
    ;


// equality/inequality (==/!=) (level 6)
equalityExpression
    :   relationalExpression ((NOT_EQUAL^ | EQUAL^) relationalExpression)*
    ;


// boolean relational expressions (level 5)
relationalExpression
    :   shiftExpression
        (   (   (   LT^
                |   GT^
                |   LE^
                |   GE^
                )
                shiftExpression
            )*
        |   "instanceof"^ typeSpec[True]
        )
    ;


// bit shift expressions (level 4)
shiftExpression
    :   additiveExpression ((SL^ | SR^ | BSR^) additiveExpression)*
    ;


// binary addition/subtraction (level 3)
additiveExpression
    :   multiplicativeExpression ((PLUS^ | MINUS^) multiplicativeExpression)*
    ;


// multiplication/division/modulo (level 2)
multiplicativeExpression
    :   unaryExpression ((STAR^ | DIV^ | MOD^ ) unaryExpression)*
    ;

unaryExpression
    :   INC^ unaryExpression
    |   DEC^ unaryExpression
    |   MINUS^ {#MINUS.setType(UNARY_MINUS);} unaryExpression
    |   PLUS^  {#PLUS.setType(UNARY_PLUS);} unaryExpression
    |   unaryExpressionNotPlusMinus
    ;

unaryExpressionNotPlusMinus
    :   BNOT^ unaryExpression
    |   LNOT^ unaryExpression

        // use predicate to skip cases like: (int.class)
    |   (LPAREN builtInTypeSpec[True] RPAREN) =>
        lpb:LPAREN^ {#lpb.setType(TYPECAST);} builtInTypeSpec[True] RPAREN!
        unaryExpression

        // Have to backtrack to see if operator follows.  If no operator
        // follows, it's a typecast.  No semantic checking needed to parse.
        // if it _looks_ like a cast, it _is_ a cast; else it's a "(expr)"
    |   (LPAREN classTypeSpec[True] RPAREN unaryExpressionNotPlusMinus)=>
        lp:LPAREN^ {#lp.setType(TYPECAST);} classTypeSpec[True] RPAREN!
        unaryExpressionNotPlusMinus

    |   postfixExpression
    ;

// qualified names, array expressions, method invocation, post inc/dec
postfixExpression
    :
    /*
    "this"! lp1:LPAREN^ argList RPAREN!
        {#lp1.setType(CTOR_CALL);}

    |   "super"! lp2:LPAREN^ argList RPAREN!
        {#lp2.setType(SUPER_CTOR_CALL);}
    |
    */
        primaryExpression

        (
            /*
            options {
                // the use of postfixExpression in SUPER_CTOR_CALL adds DOT
                // to the lookahead set, and gives loads of false non-det
                // warnings.
                // shut them off.
                generateAmbigWarnings=false;
            }
        :   */
            DOT^ IDENT
            (   lp:LPAREN^ {#lp.setType(METHOD_CALL);}
                argList
                RPAREN!
            )?
        |   DOT^ "this"

        |   DOT^ "super"
            (   // (new Outer()).super()  (create enclosing instance)
                lp3:LPAREN^ argList RPAREN!
                {#lp3.setType(SUPER_CTOR_CALL);}
            |   DOT^ IDENT
                (   lps:LPAREN^ {#lps.setType(METHOD_CALL);}
                    argList
                    RPAREN!
                )?
            )
        |   DOT^ newExpression
        |   lb:LBRACK^ {#lb.setType(INDEX_OP);} expression RBRACK!
        )*

        (   // possibly add on a post-increment or post-decrement.
            // allows INC/DEC on too much, but semantics can check
            inc:INC^ {#inc.setType(POST_INC);}
        |   dec:DEC^ {#dec.setType(POST_DEC);}
        )?
    ;

// the basic element of an expression
primaryExpression
    :   identPrimary ( options {greedy=true;} : DOT^ "class" )?
    |   constant
    |   "true"
    |   "false"
    |   "null"
    |   newExpression
    |   "this"
    |   "super"
    |   LPAREN! assignmentExpression RPAREN!
        // look for int.class and int[].class
    |   builtInType
        ( lbt:LBRACK^ {#lbt.setType(ARRAY_DECLARATOR);} RBRACK! )*
        DOT^ "class"
    ;

/* Match a, a.b.c refs, a.b.c(...) refs, a.b.c[], a.b.c[].class,
 *  and a.b.c.class refs.  Also this(...) and super(...).  Match
 *  this or super.
 */
identPrimary
    :   IDENT
        (
            options {
                // .ident could match here or in postfixExpression.
                // We do want to match here.  Turn off warning.
                greedy=true;
            }
        :   DOT^ IDENT
        )*
        (
            options {
                // ARRAY_DECLARATOR here conflicts with INDEX_OP in
                // postfixExpression on LBRACK RBRACK.
                // We want to match [] here, so greedy.  This overcomes
                // limitation of linear approximate lookahead.
                greedy=true;
            }
        :   ( lp:LPAREN^ {#lp.setType(METHOD_CALL);} argList RPAREN! )
        |   ( options {greedy=true;} :
              lbc:LBRACK^ {#lbc.setType(ARRAY_DECLARATOR);} RBRACK!
            )+
        )?
    ;

/* object instantiation.
 *  Trees are built as illustrated by the following input/tree pairs:
 *
 *  new T()
 *
 *  new
 *   |
 *   T --  ELIST
 *           |
 *          arg1 -- arg2 -- .. -- argn
 *
 *  new int[]
 *
 *  new
 *   |
 *  int -- ARRAY_DECLARATOR
 *
 *  new int[] {1,2}
 *
 *  new
 *   |
 *  int -- ARRAY_DECLARATOR -- ARRAY_INIT
 *                                  |
 *                                EXPR -- EXPR
 *                                  |      |
 *                                  1      2
 *
 *  new int[3]
 *  new
 *   |
 *  int -- ARRAY_DECLARATOR
 *                |
 *              EXPR
 *                |
 *                3
 *
 *  new int[1][2]
 *
 *  new
 *   |
 *  int -- ARRAY_DECLARATOR
 *               |
 *         ARRAY_DECLARATOR -- EXPR
 *               |              |
 *             EXPR             1
 *               |
 *               2
 *
 */
newExpression
    :   "new"^ type
        (   LPAREN! argList RPAREN! (classBlock)?

            //java 1.1
            // Note: This will allow bad constructs like
            //    new int[4][][3] {exp,exp}.
            //    There needs to be a semantic check here...
            // to make sure:
            //   a) [ expr ] and [ ] are not mixed
            //   b) [ expr ] and an init are not used together

        |   newArrayDeclarator (arrayInitializer)?
        )
    ;

argList
    :   (   expressionList
        |   /*nothing*/
            {#argList = #[ELIST,"ELIST"];}
        )
    ;

newArrayDeclarator
    :   (
            // CONFLICT:
            // newExpression is a primaryExpression which can be
            // followed by an array index reference.  This is ok,
            // as the generated code will stay in this loop as
            // long as it sees an LBRACK (proper behavior)
            options {
                warnWhenFollowAmbig = false;
            }
        :
            lb:LBRACK^ {#lb.setType(ARRAY_DECLARATOR);}
                (expression)?
            RBRACK!
        )+
    ;

constant
    :   NUM_INT
    |   CHAR_LITERAL
    |   STRING_LITERAL
    |   NUM_FLOAT
    |   NUM_LONG
    |   NUM_DOUBLE
    ;



class lexer extends Lexer;

options {
    exportVocab=Java;      // call the vocabulary "Java"
    testLiterals=false;    // don't automatically test for literals
    k=4;                   // four characters of lookahead
    charVocabulary='\u0003'..'\u7FFE';
    // without inlining some bitset tests, couldn't do unicode;
    // I need to make ANTLR generate smaller bitsets; see
    // bottom of JavaLexer.java
    codeGenBitsetTestThreshold=20;
}



// OPERATORS
QUESTION        :   '?'     ;
LPAREN          :   '('     ;
RPAREN          :   ')'     ;
LBRACK          :   '['     ;
RBRACK          :   ']'     ;
LCURLY          :   '{'     ;
RCURLY          :   '}'     ;
COLON           :   ':'     ;
COMMA           :   ','     ;
DOT             :   '.'     ;
ASSIGN          :   '='     ;
EQUAL           :   "=="    ;
LNOT            :   '!'     ;
BNOT            :   '~'     ;
NOT_EQUAL       :   "!="    ;
DIV             :   '/'     ;
DIV_ASSIGN      :   "/="    ;
PLUS            :   '+'     ;
PLUS_ASSIGN     :   "+="    ;
INC             :   "++"    ;
MINUS           :   '-'     ;
MINUS_ASSIGN    :   "-="    ;
DEC             :   "--"    ;
STAR            :   '*'     ;
STAR_ASSIGN     :   "*="    ;
MOD             :   '%'     ;
MOD_ASSIGN      :   "%="    ;
SR              :   ">>"    ;
SR_ASSIGN       :   ">>="   ;
BSR             :   ">>>"   ;
BSR_ASSIGN      :   ">>>="  ;
GE              :   ">="    ;
GT              :   ">"     ;
SL              :   "<<"    ;
SL_ASSIGN       :   "<<="   ;
LE              :   "<="    ;
LT              :   '<'     ;
BXOR            :   '^'     ;
BXOR_ASSIGN     :   "^="    ;
BOR             :   '|'     ;
BOR_ASSIGN      :   "|="    ;
LOR             :   "||"    ;
BAND            :   '&'     ;
BAND_ASSIGN     :   "&="    ;
LAND            :   "&&"    ;
SEMI            :   ';'     ;


// Whitespace -- ignored
WS  :   (   ' '
        |   '\t'
        |   '\f'
            // handle newlines
        |   (   options {generateAmbigWarnings=false;}
            :   "\r\n"  // Evil DOS
            |   '\r'    // Macintosh
            |   '\n'    // Unix (the right way)
            )
            { $newline }
        )+
        { $skip }
    ;

// Single-line comments
SL_COMMENT
    :   "//"
        (~('\n'|'\r'))* ('\n'|'\r'('\n')?)?
        {$skip ; $newline}
    ;

// multiple-line comments
ML_COMMENT
    :   "/*"
        (   /*  '\r' '\n' can be matched in one alternative or by matching
                '\r' in one iteration and '\n' in another.  I am trying to
                handle any flavor of newline that comes in, but the language
                that allows both "\r\n" and "\r" and "\n" to all be valid
                newline is ambiguous.  Consequently, the resulting grammar
                must be ambiguous.  I'm shutting this warning off.
             */
            options {
                generateAmbigWarnings=false;
            }
        :
            { self.LA(2)!='/' }? '*'
        |   '\r' '\n'       {$newline;}
        |   '\r'            {$newline;}
        |   '\n'            {$newline;}
        |   ~('*'|'\n'|'\r')
        )*
        "*/"
        {$skip }
    ;


// character literals
CHAR_LITERAL
    :   '\'' ( ESC | ~('\''|'\n'|'\r'|'\\') ) '\''
    ;

// string literals
STRING_LITERAL
    :   '"' (ESC|~('"'|'\\'|'\n'|'\r'))* '"'
    ;


// escape sequence -- note that this is protected; it can only be called
//   from another lexer rule -- it will not ever directly return a token to
//   the parser
// There are various ambiguities hushed in this rule.  The optional
// '0'...'9' digit matches should be matched here rather than letting
// them go back to STRING_LITERAL to be matched.  ANTLR does the
// right thing by matching immediately; hence, it's ok to shut off
// the FOLLOW ambig warnings.
protected
ESC
    :   '\\'
        (   'n'
        |   'r'
        |   't'
        |   'b'
        |   'f'
        |   '"'
        |   '\''
        |   '\\'
        |   ('u')+ HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
        |   '0'..'3'
            (
                options {
                    warnWhenFollowAmbig = false;
                }
            :   '0'..'7'
                (
                    options {
                        warnWhenFollowAmbig = false;
                    }
                :   '0'..'7'
                )?
            )?
        |   '4'..'7'
            (
                options {
                    warnWhenFollowAmbig = false;
                }
            :   '0'..'7'
            )?
        )
    ;


// hexadecimal digit (again, note it's protected!)
protected
HEX_DIGIT
    :   ('0'..'9'|'A'..'F'|'a'..'f')
    ;


// an identifier.  Note that testLiterals is set to true!  This means
// that after we match the rule, we look in the literals table to see
// if it's a literal or really an identifer
IDENT
    options {testLiterals=true;}
    :   ('a'..'z'|'A'..'Z'|'_'|'$') ('a'..'z'|'A'..'Z'|'_'|'0'..'9'|'$')*
    ;


// a numeric literal
NUM_INT
    {
        isDecimal = False
        t = None
    }
    :   '.' {_ttype = DOT;}
            (   ('0'..'9')+ (EXPONENT)? (f1:FLOAT_SUFFIX {t=f1})?
                {
                if t != None:
                    if 'F' in t.getText().upper():
                        _ttype = NUM_FLOAT
                    else:
                        _ttype = NUM_DOUBLE
                }
            )?

    |   (   '0' {isDecimal = True;} // special case for just '0'
            (   ('x'|'X')
                (                                           // hex
                    // the 'e'|'E' and float suffix stuff look
                    // like hex digits, hence the (...)+ doesn't
                    // know when to stop: ambig.  ANTLR resolves
                    // it correctly by matching immediately.  It
                    // is therefor ok to hush warning.
                    options {
                        warnWhenFollowAmbig=false;
                    }
                :   HEX_DIGIT
                )+

            |   //float or double with leading zero
                (('0'..'9')+ ('.'|EXPONENT|FLOAT_SUFFIX)) => ('0'..'9')+

            |   ('0'..'7')+                                 // octal
            )?
        |   ('1'..'9') ('0'..'9')*  {isDecimal=True;}       // non-zero decimal
        )
        (   ('l'|'L') { _ttype = NUM_LONG; }

        // only check to see if it's a float if looks like decimal so far
        |   {isDecimal}?
            (   '.' ('0'..'9')* (EXPONENT)? (f2:FLOAT_SUFFIX {t=f2})?
            |   EXPONENT (f3:FLOAT_SUFFIX {t=f3})?
            |   f4:FLOAT_SUFFIX {t=f4}
            )
            {
                if t != None:
                    if 'F' in t.getText().upper():
                        _ttype = NUM_FLOAT
                    else:
                        _ttype = NUM_DOUBLE


            }
        )?
    ;


// a couple protected methods to assist in matching floating point numbers
protected
EXPONENT
    :   ('e'|'E') ('+'|'-')? ('0'..'9')+
    ;


protected
FLOAT_SUFFIX
    :   'f'|'F'|'d'|'D'
    ;

