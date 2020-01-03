package ANTLR::Runtime::Object::Signature;

use strict;
use warnings;

use Attribute::Handlers;
use Filter::Simple;

sub Signature :ATTR(CODE) {
    my ($package, $symbol, $referent, $attr, $data, $phase, $filename, $linenum) = @_;
    #print map {"$_\n"} @_;
}

FILTER {
    #s{return \$lhs \+ \$rhs;}{ print "\@_\n"; };
    s{(return \$lhs \+ \$rhs;)}{ my \$self = shift; my \$lhs = shift; my \$rhs = shift; $1 };
};

1;
