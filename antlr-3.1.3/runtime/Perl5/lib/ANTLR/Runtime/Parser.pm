package ANTLR::Runtime::Parser;
use ANTLR::Runtime::Class;

use Readonly;
use Carp;

extends 'ANTLR::Runtime::BaseRecognizer';

has 'input';

sub BUILD {
    my ($self, $arg_ref) = @_;

    $self->set_token_stream($arg_ref->{input});
}

sub reset {
    Readonly my $usage => 'void reset()';
    croak $usage if @_ != 1;
    my ($self) = @_;

    $self->SUPER::reset();  #  reset all recognizer state variables
    if (defined $self->input) {
        $self->input->seek(0);  # rewind the input
    }
}

sub get_current_input_symbol {
    my ($self, $input) = @_;
    return $self->input->LT(1);
}

sub get_missing_symbol {
    my ($self, $arg_ref) = @_;
    my $input = $arg_ref->{input};
    my $exception = $arg_ref->{exception};
    my $expected_token_type = $arg_ref->{expected_token_type};
    my $follow = $arg_ref->{follow};

    my $token_text;
    if ($expected_token_type == ANTLR::Runtime::Token->EOF) {
        $token_text = '<missing EOF>';
    }
    else {
        $token_text = '<missing ' . $self->get_token_names()->[$expected_token_type] . '>';
    }

    my $t = ANTLR::Runtime::CommonToken->new({
        type => $expected_token_type,
        text => $token_text
    });
    my $current = $input->LT(1);
    if ($current->get_type() == ANTLR::Runtime::Token->EOF) {
        $current = $input->LT(-1);
    }
    $t->set_line($current->get_line());
    $t->set_char_position_in_line($current->get_char_position_in_line());
    $t->set_channel($self->DEFAULT_TOKEN_CHANNEL);

    return $t;
}

sub set_token_stream {
    Readonly my $usage => 'void set_token_stream(TokenStream input)';
    croak $usage if @_ != 2;
    my ($self, $input) = @_;

    $self->input(undef);
    $self->reset();
    $self->input($input);
}

sub get_token_stream {
    Readonly my $usage => 'TokenStream get_token_stream()';
    croak $usage if @_ != 1;
    my ($self) = @_;

    return $self->input;
}

sub get_source_name {
    my ($self) = @_;
    return $self->input->get_source_name();
}

sub trace_in {
    Readonly my $usage => 'void trace_in(String rule_name, int rule_index)';
    croak $usage if @_ != 3;
    my ($self, $rule_name, $rule_index) = @_;

    $self->SUPER::trace_in($rule_name, $rule_index, $self->input->LT(1));
}

sub trace_out {
    Readonly my $usage => 'void trace_out(String rule_name, int rule_index)';
    croak $usage if @_ != 3;
    my ($self, $rule_name, $rule_index) = @_;

    $self->SUPER::trace_out($rule_name, $rule_index, $self->input->LT(1));
}

1;
