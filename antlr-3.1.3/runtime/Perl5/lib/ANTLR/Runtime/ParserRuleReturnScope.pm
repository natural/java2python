package ANTLR::Runtime::ParserRuleReturnScope;
use ANTLR::Runtime::Class;

extends 'ANTLR::Runtime::RuleReturnScope';

has 'start';
has 'stop';

sub get_start {
    my ($self) = @_;
    return $self->start;
}

sub get_stop {
    my ($self) = @_;
    return $self->stop;
}

1;
__END__
