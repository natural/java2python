/*
Current:

    This file is part of java2python.  Redistributed under terms of
    original license below.  Modifications Copyright (C) Troy Melhase
    <troy@gci.net>.

Original:

    This file is part of PyANTLR. See LICENSE.txt for license
    details..........Copyright (C) Wolfgang Haefelinger, 2004.
    Java 1.3 AST Recognizer Grammar
    Author: (see java.g preamble)
    This grammar is in the PUBLIC DOMAIN

*/
options {
    language=Python;
}


class walker extends TreeParser;
options {
    importVocab = Java;
}


walk[source]
    :   (pkg = package_def[source])?
        (imp = import_def[source])*
        (typ = type_def[source])*
    ;


package_def[block]
returns[pkg_ident]
    :   #(PACKAGE_DEF pkg_ident = identifier[block])
    ;


import_def[block]
returns[imp_stat]
    // we don't do anything with imports, but we could
    :   #(IMPORT imp_stat = identifier_star[block] )
    // static imports are ignored, too.  they might be partially
    // implemented in the future.
	|	#(STATIC_IMPORT imp_stat = identifier_star[block] )
    ;


type_def[block]
returns[klass = block.newClass()]
    :   #(CLASS_DEF
          modifiers[klass]
          name = identifier[klass] {klass.setName(name)}
          ext_clause = extends_clause[klass]
          imp_clause = implements_clause[klass]
          obj_block[klass]
        )
    |   #(INTERFACE_DEF
          modifiers[klass]
          name = identifier[klass] {klass.setName(name)}
          ext_clause = extends_clause[klass]
          interface_block[klass]
        )
	|	#(ENUM_DEF
          modifiers[klass]
          name = identifier[klass] {klass.setName(name)}
          imp_clause = implements_clause[klass]
          enum_block[klass]
        )
	|	#(ANNOTATION_DEF
          modifiers[klass]
          name = identifier[klass] {klass.setName(name)}
          annotation_block[klass]
        )
    ;


annotations[block]
returns[nil]
	:	#(ANNOTATIONS (as1=annotation[block])*)
	;


annotation[block]
returns[id0]
	:	{
        a1 = []
        }
        #(ANNOTATION
            id0 = identifier[block]
            (a2=annotation_member_value_init[block] {a1.append(a2)}
                | (a2=annotation_member_value_pair[block] {a1.append(a2)})+)?         )
        {
        if id0:
            if a1:
                block.addAnnotation("%s(%s)" % (id0, ", ".join(a1)))
            else:
                block.addAnnotation(id0)
        }
	;

annotation_member_value_init[block]
returns[init0]
	:	e = expr[block]
        {
        init0=e[1]
        }
    | init0 = annotation[block]
    | init0 = annotation_member_array_init[block]
	;

annotation_member_value_pair[block]
returns[pair]
	:	#(ANNOTATION_MEMBER_VALUE_PAIR
            id0:IDENT {block.setName(id0.getText())}
            a1=annotation_member_value_init[block]
            {pair = "%s=%s" % (id0.getText(), a1)}
        )
	;

annotation_member_array_init[block]
returns[a]
	:	#(ANNOTATION_ARRAY_INIT
            a:(annotation_member_array_value_init[block])*
        )
	;

annotation_member_array_value_init[block]
	:	e = expr[block]
    | a = annotation[block]
	;


annotation_block[block]
	:	#(	OBJBLOCK
			(	a = annotation_field_decl[block]
			|	variable_def[block]
			|	a = type_def[block]
			)*
		)
	;

annotation_field_decl[block]
returns[id0]
	:	{
        meth = block.newMethod()
        an0 = None
        }
        #(ANNOTATION_FIELD_DEF
            modifiers[meth]
            typ = type_spec[block]
            id0:IDENT
            (an0 = annotation_member_value_init[meth])?
        )
        {
        meth.setName(id0.getText())
        meth.type = typ
        if an0 is not None:
            meth.addSource("return %s" % an0)
        }
    ;



enum_block[block]
	:	#(	OBJBLOCK
			(enum_constant_def[block])*
			(	ctor_def[block]
			|	method_def[block]
			|	variable_def[block, False]
			|	tdef = type_def[block]
            |   #(STATIC_INIT statement_list[block])
            |   #(INSTANCE_INIT statement_list[block])
			)*
		)
	;

enum_constant_def[block]
	:	#(ENUM_CONSTANT_DEF
            annos = annotations[block]
            ident = identifier[block]
            (elist = expr_list[block])?
            (enum_constant_block[block])?
        )
	;

enum_constant_block[block]
	:	#(	OBJBLOCK
			(	method_def[block]
			|	variable_def[block, False]
			|	tdef = type_def[block]
            | #(INSTANCE_INIT statement_list[block])
			)*
		)
	;


type_spec[block]
returns[spec]
    :   #(t0:TYPE type_spec_array[block])
        {
        first = t0.getFirstChild()
        value = first.getText()
        if value == ".":
            seq = []
            next = first.getFirstChild()
            while next:
                seq.append(next.getText())
                next = next.getNextSibling()
            value = str.join(".", seq)
        try:
            spec = block.config.combined("typeTypeMap")[value]
        except (KeyError, ):
            spec = value
        }
    ;


type_spec_array[block]
    :   #(ad0:ARRAY_DECLARATOR type_spec_array[block])
    |   spec = type[block]
    ;


type[block]
returns[typ]
    :   typ = identifier[block]   {block.type = typ}
    |   typ = builtin_type[block] {block.type = typ}
    ;


builtin_type[block]
returns[typ]
    :   "void"    {typ = "null"   }
    |   "boolean" {typ = "bool"   }
    |   "byte"    {typ = "str"    }
    |   "char"    {typ = "str"    }
    |   "short"   {typ = "int"    }
    |   "int"     {typ = "int"    }
    |   "float"   {typ = "float"  }
    |   "long"    {typ = "long"   }
    |   "double"  {typ = "float"  }
    ;


modifiers[block, mod=None]
    :   #(MODIFIERS (mod = modifier[block]
        {
        if mod:
            block.addModifier(mod)
        })*
        )
    ;


modifier[block]
returns[mod]
    :   pri0:"private"         {mod = pri0.getText()}
    |   pub0:"public"          {mod = pub0.getText()}
    |   pro0:"protected"       {mod = pro0.getText()}
    |   sta0:"static"          {mod = sta0.getText()}
    |   tra0:"transient"       {mod = tra0.getText()}
    |   fin0:"final"           {mod = fin0.getText()}
    |   abt0:"abstract"        {mod = abt0.getText()}
    |   nat0:"native"          {mod = nat0.getText()}
    |   ths0:"threadsafe"      {mod = ths0.getText()}
    |   syn0:"synchronized"    {mod = syn0.getText()}
    |   con0:"const"           {mod = con0.getText()}
    |   vol0:"volatile"        {mod = vol0.getText()}
    |   sfp0:"strictfp"        {mod = sfp0.getText()}
	|	mod = annotation[block]
    ;


extends_clause[block]
returns[clause = None]
    :   #(EXTENDS_CLAUSE
            (clause = identifier[block])*) {block.addBaseClass(clause)}
    ;


implements_clause[block]
returns[clause = None]
    :   #(IMPLEMENTS_CLAUSE
            (clause = identifier[block])*) {block.addBaseClass(clause)}
    ;


interface_block[block]
    :   #(OBJBLOCK
            (method_decl[block]
                | variable_def[block, False]
                | typ = type_def[block]
            )*
        )
    ;


obj_block[block]
    :   #(OBJBLOCK
            (ctor_def[block]
                | method_def[block]
                | variable_def[block, False]
                | typ = type_def[block]
                | static_init[block]
                | #(INSTANCE_INIT statement_list[block])
            )*
        )
        { block.fixCtor() }
    ;


ctor_def[block]
    :   {
        meth = block.newMethod()
        meth.calledSuperCtor = False
        meth.calledOtherCtor = False
        }
        #(CTOR_DEF
            modifiers[meth]
            method_head[meth, "__init__"]
            (statement_list[meth])?
        )
    ;


method_decl[block]
    :   {
        meth = block.newMethod()
        meth.addSource("raise NotImplementedError()")
        }
        #(METHOD_DEF
            modifiers[meth]
            typ = type_spec[meth]
            method_head[meth]
        ) 
        {
        meth.type = typ
        }
    ;


method_head[meth, name=None]
    :   ident = identifier[meth]
        {
        meth.setName(name if name else ident)
        }
        #(PARAMETERS (parameter_def[meth])*)
        (throws_clause[meth])?
    ;


method_def[block]
    :   {
        meth = block.newMethod()
        }
        #(METHOD_DEF
            modifiers[meth]
            typ = type_spec[block]
            method_head[meth]
            (statement_list[meth])?
        )
        {
        meth.type = typ
        }
    ;


variable_def[block, append = True]
    :   {
        var = block.newVariable()
        }
        #(VARIABLE_DEF
            modifiers[var]
            typ = type_spec[var]
            dec = var_decl[var]
            val = var_init[var]
        )
        {
        if val == block.emptyAssign:
            val = ("%s", block.config.combined("typeValueMap").get(typ, "null"))
        if dec:
            var.setName(dec[1])
        var.setExpression(val)
        if append or var.isStatic:
            block.addSource( ("%s = %s", (dec, val)) )
        }
    ;

static_init[block]
    :   #(STATIC_INIT
          {
            if not hasattr(block, "static_init"):
                block.static_init = block.newMethod("__static_init__")
                block.static_init.addModifier("static")
                block.parent.addSource("%s.__static_init__()\n" % block.className)
          }
          statement_list[block.static_init])
    ;

parameter_def[meth, exc=False]
    :   #(pd0:PARAMETER_DEF
            modifiers[meth]
            ptype = type_spec[meth]
            ident = identifier[meth]
        )
        {
        if exc:
            ptype = meth.alternateName(ptype, "exceptionTypeMapping")
            meth.setExpression(("(%s, ), %s", (("%s", ptype), ("%s", ident))))
        else:
            meth.addParameter(ptype, ident)

        }
    ;


obj_init[block]
    :   #(INSTANCE_INIT statement_list[block])
    ;


var_decl[block]
returns[decl]
    :   ident = identifier[block]      {decl = ("%s", ident)}
    |   LBRACK inner = var_decl[block] {decl = ("(%s)", inner)}
    ;


var_init[block]
returns[init = block.emptyAssign]
    :   #(ASSIGN init = initializer[block])
    |   // on purpose
    ;


initializer[block]
returns[init]
    :   init = expression[block, False]
    |   init = array_initializer[block] { init = ("[%s]", init) }
    ;


array_initializer[block]
returns[ret = None]
    :  #(ARRAY_INIT
         (init = initializer[block]
          {
        if ret:
            ret = ("%s, %s", (ret, init))
        else:
            ret = ("%s", init)
          } )*)
    ;


throws_clause[block, ident=None]
    :   #("throws" (ident = identifier[block])*)
        {
        if ident:
            block.addModifier("throws %s" % ident)
        }
    ;



identifier[block]
returns[ident]
    :   id0:IDENT
        {
        ident = id0.getText()
        }
    |   {
        exp = ()
        }
        #(DOT exp = identifier[block] id1:IDENT)
        {
        if exp:
            ident = ("%s.%s", (("%s", exp), ("%s", id1.getText())))
        else:
            ident = id1.getText()
        }
    ;


identifier_star[block]
returns[ident]
    :   id0:IDENT {ident = id0.getText()}
    |   {
        exp = ()
        }
        #(DOT exp = identifier[block] id1:(STAR|IDENT))
        {
        if exp and id1:
            ident = ("%s.%s", (("%s", exp), ("%s", id1.getText())))
        elif exp:
            ident = ("%s.%s", (("%s", exp), ("%s", "*")))
        else:
            ident = id1
        }
    ;


statement_list[block]
    :   #(SLIST (s1:statement[block])*)
    ;

// MARKER

statement[block]
    :   typ = type_def[block]
    |   variable_def[block]
    |   exp = expression[block]
    |   #(LABELED_STAT IDENT statement[block])

    |   {
        if_stat = block.newStatement("if")
        else_stat = block.newStatement("else")
        }
        #("if"
            if_expr = expression[if_stat, False]
            statement[if_stat]
            (statement[else_stat])?
        )
        {
        if_stat.setExpression(if_expr)
        }


    |   {
        block.addComment("for-while")
        for_init, for_stat = block.newFor()
        for_iter = None
        for_cond = "True"
        }
        #("for"
            #(FOR_INIT
                ((variable_def[for_init])+ | for_exp = expr_list[for_init, True])?)
            #(FOR_CONDITION (for_cond = expression[for_stat, False])?)
            #(FOR_ITERATOR  (for_iter = expr_list[for_stat, False])?)
            statement[for_stat]
        )
        {
        for_stat.setExpression(("%s", for_cond))
        if for_iter:
            for_stat.addSource(("%s", for_iter))
        }


    |   {
        if_stat = while_stat = block.newStatement("while")
        }
        #(wh:"while"
          {
            useif = block.hasAssignInExpr(wh.getFirstChild())
            if (useif):
                if_stat = while_stat.newStatement("if")
                while_stat.setExpression("True")
                if_stat.newStatement("break")
          }
          while_expr = expression[if_stat, False] 
          statement[while_stat])
        {
        if useif:
            if_stat.setExpression(("not %s", while_expr))
        else:
            if_stat.setExpression(while_expr)
        }


    |   {
        while_stat = block.newStatement("while")
        while_stat.setExpression("True")
        }
        #("do"
          statement[while_stat]
          {
            if_stat = while_stat.newStatement("if")
            if_stat.newStatement("break")
          }
          do_exp = expression[if_stat, False])
          {
            if_stat.setExpression(("not %s", do_exp))
          }


    |   {
        break_stat = block.newStatement("break")
        break_label = block.missingValue
        }
        #("break" (break_label:IDENT)? )
        {
        if break_label is not block.missingValue:
            raise NotImplementedError("break with label")
        }



    |   {
        continue_stat = block.newStatement("continue")
        continue_label = block.missingValue
        }
        #("continue" (continue_label:IDENT)? )
        {
        if continue_label is not block.missingValue:
            raise NotImplementedError("continue with label")
        }


    |   {
        return_value = None
        }
        #("return" (return_value = expression[block, False])? )
        {
        if return_value in (None, ("%s", "null")):
            block.addSource("return")
        else:
            block.addSource(("return %s", return_value))
        }


    |   {
        while_block = block.newSwitch()
        }
        #("switch" switch_expr = expression[block, False]
                   (c:case_group[while_block, switch_expr])*
        )
        {
        while_block.newStatement("break")
        }

    |   {
        raise_stat = block.newStatement("raise")
        }
        #("throw" raise_exp = expression[block, False])
        {
        raise_stat.setExpression(raise_exp)
        }

    |   try_block[block]
    |   ctor_call[block]
    |   statement_list[block]
    |   EMPTY_STAT
    ;


case_group[block, switch_expr]
    :   {
        other = block.newStatement("if")
        right = None
        }
        #(CASE_GROUP
            (#("case"
               newright = expression[other, False]
               {
                if not right:
                    right = ("%s", newright)
                else:
                    right = ("%s, %s", (right, newright))
               }
              )
              | "default"
               {
                right = block.emptyAssign
                block.removeStatement(other)
                other = block
               }
            )+
            statement_list[other]
        )
        {
        if right is block.emptyAssign:
            pass
        elif right[0] == "%s":
            other.setExpression(("%s == %s", (switch_expr, right)))
        else:
            other.setExpression(("%s in (%s)", (switch_expr, right)))
        }
    ;


try_block[block]
    {
    try_stat = block.newStatement("try")

    finally_stat = block.newStatement("finally")
    }

    :   #("try"
            statement_list[try_stat]
            ({except_stat = block.newStatement("except")}
             handler[except_stat]
            )*
            (#("finally" statement_list[finally_stat]))?
        )
    ;


handler[block]
    :   #("catch"
            parameter_def[block, True]
            statement_list[block]
        )
    ;


expr_list[block, append=False]
returns[seq]
    :   #(ELIST
            (exp = expression[block, append]
            {
            if seq:
                seq = ("%s, %s", (("%s", seq), ("%s", exp)))
            else:
                seq = ("%s", exp)
            }
        )*
    )
    ;


expression[block, append=True]
returns[exp]
    :   {
        fixAssign = not append
        }
        #(EXPR exp = expr[block, fixAssign])
        {
        if append:
            block.addSource(exp)
        if block.postIncDecInExprFixed:
            exp = block.fixPostIncDecInExprAfter(exp)
        }
    ;


expr[block, fixAssign=True]
returns[exp = block.unknownExpression]
    :   #(QUESTION a0=expr[block] b0=expr[block] c0=expr[block])
        {exp = ("%s %s", (("%s", b0), ("%s %s", (("if %s", a0), ("else %s", c0)))))}

    |   #(ASSIGN left=expr[block] right=expr[block])
        {exp = block.fixAssignInExpr(fixAssign, ("%s = %s", (left, right)), left)}

    |   #(PLUS_ASSIGN left=expr[block] right=expr[block])
        {exp = block.fixAssignInExpr(fixAssign, ("%s += %s", (left, right)), left)}

    |   #(MINUS_ASSIGN left=expr[block] right=expr[block])
        {exp = block.fixAssignInExpr(fixAssign, ("%s -= %s", (left, right)), left)}

    |   #(STAR_ASSIGN left=expr[block] right=expr[block])
        {exp = block.fixAssignInExpr(fixAssign, ("%s *= %s", (left, right)), left)}

    |   #(DIV_ASSIGN left=expr[block] right=expr[block])
        {exp = block.fixAssignInExpr(fixAssign, ("%s /= %s", (left, right)), left)}

    |   #(MOD_ASSIGN left=expr[block] right=expr[block])
        {exp = block.fixAssignInExpr(fixAssign, ("%s %%= %s", (left, right)), left)}

    |   #(SR_ASSIGN left=expr[block] right=expr[block])
        {exp = block.fixAssignInExpr(fixAssign, ("%s >>= %s", (left, right)), left)}

    |   #(BSR_ASSIGN left=expr[block] right=expr[block])
        // raise an exception during parsing, not at runtime
        {raise NotImplementedError("BSR_ASSIGN")}

    |   #(SL_ASSIGN left=expr[block] right=expr[block])
        {exp = block.fixAssignInExpr(fixAssign, ("%s <<= %s", (left, right)), left)}

    |   #(BAND_ASSIGN left=expr[block] right=expr[block])
        {exp = block.fixAssignInExpr(fixAssign, ("%s &= %s", (left, right)), left)}

    |   #(BXOR_ASSIGN left=expr[block] right=expr[block])
        {exp = block.fixAssignInExpr(fixAssign, ("%s ^= %s", (left, right)), left)}

    |   #(BOR_ASSIGN left=expr[block] right=expr[block])
        {exp = block.fixAssignInExpr(fixAssign, ("%s |= %s", (left, right)), left)}

    |   { left_if = right_if = block }
        #(lor:LOR
          {
            right_has = block.hasAssignInExpr(lor.getFirstChild().getNextSibling())
            if right_has:
                left_if = block.parent.newStatementBefore("if", block)
                right_if = left_if.newStatement("if")
          }
          left=expr[left_if] right=expr[right_if])
        {
        if right_has:
            left_if.setExpression(("not %s", left))
            if left != "_ret":
                left_else = block.parent.newStatementBefore("else", block)
                left_else.addSource("_ret = True")
            right_if.setExpression(right)
            right_if.addSource("_ret = True")
            right_else = left_if.newStatement("else")
            right_else.addSource("_ret = False")
            if left_if.postIncDecInExprFixed:
                left_if.fixPostIncDecInExprAfter(left)
            if right_if.postIncDecInExprFixed:
                right_if.fixPostIncDecInExprAfter(right)
            exp = "_ret"
        else:
            exp = ("%s or %s", (left, right))

        }

    |   { left_if = right_if = block }
        #(land:LAND
          {
            right_has = block.hasAssignInExpr(land.getFirstChild().getNextSibling())
            if right_has:
                left_if = block.parent.newStatementBefore("if", block)
                right_if = left_if.newStatement("if")
          }
          left=expr[left_if] right=expr[right_if])
        {
        if right_has:
            left_if.setExpression(left)
            if left != "_ret":
                left_else = block.parent.newStatementBefore("else", block)
                left_else.addSource("_ret = False")
            right_if.setExpression(right)
            right_if.addSource("_ret = True")
            right_else = left_if.newStatement("else")
            right_else.addSource("_ret = False")
            if left_if.postIncDecInExprFixed:
                left_if.fixPostIncDecInExprAfter(left)
            if right_if.postIncDecInExprFixed:
                right_if.fixPostIncDecInExprAfter(right)
            exp = "_ret"
        else:
            exp = ("%s and %s", (left, right))
        }

    |   #(BOR left=expr[block] right=expr[block])
        {exp = ("%s | %s", (left, right))}

    |   #(BXOR left=expr[block] right=expr[block])
        {exp = ("%s ^ %s", (left, right))}

    |   #(BAND left=expr[block] right=expr[block])
        {exp = ("%s & %s", (left, right))}

    |   #(NOT_EQUAL left=expr[block] right=expr[block])
        {
        if right in ("null", (("%s", "null"))):
            exp = ("%s is not %s", (left, right))
        else:
            exp = ("(%s != %s)", (left, right))
        }

    |   #(EQUAL left=expr[block] right=expr[block])
        {
        if right in ("null", (("%s", "null"))):
            exp = ("%s is %s", (left, right))
        else:
            exp = ("(%s == %s)", (left, right))
        }

    |   #(LT left=expr[block] right=expr[block])
        {exp = ("%s < %s", (left, right))}

    |   #(GT left=expr[block] right=expr[block])
        {exp = ("%s > %s", (left, right))}

    |   #(LE left=expr[block] right=expr[block])
        {exp = ("%s <= %s", (left, right))}

    |   #(GE left=expr[block] right=expr[block])
        {exp = ("%s >= %s", (left, right))}

    |   #(SL left=expr[block] right=expr[block])
        {exp = ("%s << %s", (left, right))}

    |   #(SR left=expr[block] right=expr[block])
        {exp = ("%s >> %s", (left, right))}

    |   #(BSR left=expr[block] right=expr[block])
        // raise an exception during parsing, not at runtime
        {raise NotImplementedError("BSR")}

    |   #(PLUS left=expr[block] right=expr[block])
        {exp = ("%s + %s", (left, right))}

    |   #(MINUS left=expr[block] right=expr[block])
        {exp = ("%s - %s", (left, right))}

    |   #(DIV left=expr[block] right=expr[block])
        {exp = ("%s / %s", (left, right))}

    |   #(MOD left=expr[block] right=expr[block])
        {exp = ("%s %% %s", (left, right))}

    |   #(STAR left=expr[block] right=expr[block])
        {exp = ("%s * %s", (left, right))}

    |   #(INC ex=expr[block])
        {exp = block.fixAssignInExpr(fixAssign, ("%s += 1", ex), ex)}

    |   #(DEC ex=expr[block])
        {exp = block.fixAssignInExpr(fixAssign, ("%s -= 1", ex), ex)}

    |   #(POST_INC ex=expr[block])
        {exp = block.fixPostIncDecInExpr(fixAssign, ("%s += 1", ex), ex, "+")}

    |   #(POST_DEC ex=expr[block])
        {exp = block.fixPostIncDecInExpr(fixAssign, ("%s -= 1", ex), ex, "-")}

    |   #(BNOT ex=expr[block])
        {exp = ("~%s", ex)}

    |   #(LNOT ex=expr[block])
        {exp = ("not %s", ex)}

    |   #("instanceof" obj=expr[block] typ=expr[block])
        {exp = ("isinstance(%s, (%s))", (obj, typ))}

    |   #(UNARY_MINUS uex=expr[block])
        {exp = ("-%s", uex)}

    |   #(UNARY_PLUS uex=expr[block])
        {exp = ("+%s", uex)}

    |   exp = primary_expr[block]
    ;


primary_expr[block]
returns[exp = block.missingValue]
    :   i0:IDENT {exp = ("%s", i0.getText())}

    |   {
        dotexpr = this0 = class0 = class1 = class2 = id0 = id1 = ar0 = typ = None
        index = None
        }
        #(DOT
            (dotexpr=expr[block]
                (id0:IDENT
                    | index = array_index[block]
                    | this0:"this"
                    | class0:"class"
                    | #("new" id1:IDENT el0=expr_list[block] )
                    | "super"
                )
                | #(ar0:ARRAY_DECLARATOR type_spec_array[block])
                  (class1:"class")?
                | typ = builtin_type[block](class2:"class")?
            )
        )
        {
        if id0:
            exp = ("%s.%s", (dotexpr, ("%s", id0.getText())))
        elif ar0:
            exp = ("%s", "[]")
            if class1:
                exp = ("%s.__class__", exp)
        elif typ:
            exp = ("%s", typ)
        elif id1:
            el0 = el0 or ""
            exp = ("%s(%s)", (("%s", id1.getText()), ("%s", el0)))
        }

    |   index = array_index[block] 
        {
        exp = index
        }

    |   #(METHOD_CALL pex = primary_expr[block] exl = expr_list[block])
        {
        if exl:
            exp = ("%s(%s)", (pex, exl))
        else:
            exp = ("%s()", pex)
       }

    |   ctor_call[block]

    |   #(TYPECAST 
            type_cast = type_spec[block]
            cast_exp = expr[block]
        )
        {
        exp = ("%s", cast_exp)
        }

    |   other_exp = new_expression[block] {exp = ("%s", other_exp)}
    |   con = constant[block] {exp = ("%s", con)}
    |   "super" {exp = ("%s", "super"  )}
    |   "true"  {exp = ("%s", "True"   )}
    |   "false" {exp = ("%s", "False"  )}
    |   "this"  {exp = ("%s", "self"   )}
    |   "null"  {exp = ("%s", "null"   )}
    // type name used with instanceof
    |   typ = type_spec[block] {exp = ("%s", typ)}
    ;


ctor_call[block]
    :   #(cn:CTOR_CALL seq=expr_list[block, False] )
        {
        name = block.parent.name
        call = ("self.__init__(%s)", ("%s", seq))
        block.addSource(call)
        block.calledOtherCtor = True
        }

    |   #(SUPER_CTOR_CALL
            (seq=expr_list[block]
                | p=primary_expr[block] el2=expr_list[block]
            )
            {
            if seq is None:
                seq = ""
            name = block.parent.name
            call = ("super(%s, self).__init__(%s)", (("%s", name), ("%s", seq)))
            block.addSource(call)
            }
        )
        {
        block.calledSuperCtor = True
        block.stmtAfterSuper = block.newStatement("if")
        }
    ;


array_index[block]
returns[index]
    :   #(INDEX_OP 
            array_exp = expr[block] 
            index_exp = expression[block, False]
        )
        {
        index = ("%s[%s]", (array_exp, index_exp))
        }
    ;


constant[block]
returns[value]
    :   i0:NUM_INT        {value = i0.getText()}
    |   c0:CHAR_LITERAL   {value = c0.getText()}
    |   s0:STRING_LITERAL {value = s0.getText()}
    |   f0:NUM_FLOAT      {value = f0.getText().rstrip("fF")}
    |   d0:NUM_DOUBLE     {value = d0.getText()}
    |   l0:NUM_LONG       {value = l0.getText()}
    ;


new_expression[block]
returns[value = block.missingValue]
    {
    exp = ()
    arrexp = None
    arrdecl = None
    klass = block.newClass()
    }
    :   #("new"
            typ = type[block]
            (arrdecl = new_array_declarator[block]
                ( arrexp = array_initializer[block])?
                | exp = expr_list[block] (obj_block[klass])?
            )
        )
        {
        if len(klass.lines):
            block.anonymousClassCount += 1
            klass.addBaseClass(typ)
            klass.setName("%s%s" % (typ, block.anonymousClassCount))
        else:
            block.lines.remove(klass)
        alltypes = block.config.combined("typeValueMap")
        if arrdecl:
            value = ("[%s() for __idx0 in range(%s)]", (("%s", typ), ("%s", arrdecl)))
        elif exp:
            value = ("%s(%s)", (("%s", typ), ("%s", exp)))
        elif typ in alltypes:
            value = ("%s", alltypes[typ])
        else:
            value = ("%s()", typ)
        }
    ;


new_array_declarator[block]
returns[exp = None]
    :   #(ad0:ARRAY_DECLARATOR
            (exp = new_array_declarator[block])? 
            (exp = expression[block, False])?
        )
    ;
