package ANTLR::Runtime::MismatchedTokenException;
use ANTLR::Runtime::Class;

use Params::Validate qw( :types );
use ANTLR::Runtime::Token;

use overload
    '""' => \&to_string,
    'bool' => sub { 1 },
    fallback => 1;

extends 'ANTLR::Runtime::RecognitionException';

has 'expecting';

sub BUILD {
    my ($self, $arg_ref) = @_;

    if (exists $arg_ref->{expecting}) {
        $self->expecting($arg_ref->{expecting});
    }
    else {
        $self->expecting(ANTLR::Runtime::Token->INVALID_TOKEN_TYPE);
    }
}

sub get_expecting {
    my ($self) = @_;
    return $self->expecting;
}

sub to_string {
    my ($self) = @_;
    return "MismatchedTokenException(" . $self->get_unexpected_type() . "!=" . $self->expecting . ")";
}

1;
