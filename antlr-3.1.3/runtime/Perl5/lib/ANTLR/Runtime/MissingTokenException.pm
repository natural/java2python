package ANTLR::Runtime::MissingTokenException;
use ANTLR::Runtime::Class;

use overload
    '""' => \&to_string;

extends 'ANTLR::Runtime::MismatchedTokenException';

has 'inserted';

sub BUILD {
    my ($self, $arg_ref) = @_;
    my $inserted = $arg_ref->{inserted};
    $self->inserted($inserted);
}

sub get_missing_type {
    my ($self) = @_;
    return $self->expecting;
}

sub to_string {
    my ($self) = @_;

    if (defined (my $inserted = $self->inserted) && defined (my $token = $self->token)) {
        return "MissingTokenException(inserted $inserted at " . $token->get_text() . ")";
    }
    if (defined $self->token) {
        return "MissingTokenException(at " . $self->token->get_text() . ")";
    }

    return "MissingTokenException";
}

1;
__END__
