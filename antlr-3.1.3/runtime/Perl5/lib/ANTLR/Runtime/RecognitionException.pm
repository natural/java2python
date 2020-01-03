package ANTLR::Runtime::RecognitionException;
use ANTLR::Runtime::Class;

use Carp;
use Readonly;

extends 'ANTLR::Runtime::Exception';

has 'input';
has 'index';
has 'token';
has 'node';
has 'c';
has 'line';
has 'char_position_in_line';

sub BUILD {
    my ($self, $arg_ref) = @_;

    if ($arg_ref) {
        my $input = $arg_ref->{input};

        $self->input($input);
        $self->index($input->index());

        if ($input->isa('ANTLR::Runtime::TokenStream')) {
            $self->token($input->LT(1));
            $self->line($self->token->get_line());
            $self->char_position_in_line($self->token->get_char_position_in_line());
        }
        if ($input->isa('ANTLR::Runtime::CommonTreeNodeStream')) {
            $self->node = $input->LT(1);
            if ($self->node->isa('ANTLR::Runtime::CommonTree')) {
                $self->token($self->node->token);
                $self->line($self->token->get_line());
                $self->char_position_in_line($self->token->get_char_position_in_line());
            }

        } elsif ($input->isa('ANTLR::Runtime::CharStream')) {
            $self->c($input->LA(1));
            $self->line($input->get_line());
            $self->char_position_in_line($input->get_char_position_in_line());
        } else {
            $self->c($input->LA(1));
        }
    }
    else {
        $self->input(undef);
        $self->index(0);
        $self->token(undef);
        $self->node(undef);
        $self->c(0);
        $self->line(0);
        $self->char_position_in_line(0);
    }
}

sub get_unexpected_type {
    Readonly my $usage => 'int get_unexpected_type()';
    croak $usage if @_ != 1;
    my ($self) = @_;

    if ($self->input->isa('ANTLR::Runtime::TokenStream')) {
        return $self->token->get_type();
    } else {
        return $self->c;
    }
}

sub get_c {
    my ($self) = @_;
    return $self->c;
}

sub get_line {
    my ($self) = @_;
    return $self->line;
}

sub get_char_position_in_line {
    my ($self) = @_;
    return $self->char_position_in_line;
}

sub get_token {
    my ($self) = @_;
    return $self->token;
}

1;
