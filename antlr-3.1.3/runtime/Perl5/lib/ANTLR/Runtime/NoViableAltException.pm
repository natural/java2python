package ANTLR::Runtime::NoViableAltException;
use ANTLR::Runtime::Class;

extends 'ANTLR::Runtime::RecognitionException';

has 'grammar_decision_description';
has 'decision_number';
has 'state_number';

sub BUILD {
    my ($self, $arg_ref) = @_;
    my ($grammar_decision_description, $decision_number, $state_number, $input) =
        @$arg_ref{qw( grammar_decision_description decision_number state_number input )};

    $self->grammar_decision_description($grammar_decision_description);
    $self->decision_number($decision_number);
    $self->state_number($state_number);
}

1;
