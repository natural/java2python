package ANTLR::Runtime::Exception;
use ANTLR::Runtime::Class;

use Exception::Class;

has 'base';

sub BUILD {
    my ($self, $arg_ref) = @_;

    my %base_args;
    if (defined (my $message = $arg_ref->{message})) {
        $base_args{message} = $message;
    }
    my $base = Exception::Class::Base->new(%base_args);

    $self->base($base);
}

sub message {
    my ($self, @args) = @_;
    return $self->base->message(@args);
}

sub throw {
    return Exception::Class::Base::throw(@_);
}

sub rethrow {
    return Exception::Class::Base::rethrow(@_);
}

sub caught {
    return Exception::Class::Base::caught(@_);
}

sub description {
    return 'ANTLR::Runtime Base Exception';
}

1;
