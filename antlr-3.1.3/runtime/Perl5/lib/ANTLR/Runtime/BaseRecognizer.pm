package ANTLR::Runtime::BaseRecognizer;
use ANTLR::Runtime::Class;

use Readonly;
use Carp;

use ANTLR::Runtime::RecognizerSharedState;
use ANTLR::Runtime::Token;
use ANTLR::Runtime::UnwantedTokenException;
use ANTLR::Runtime::MissingTokenException;
use ANTLR::Runtime::MismatchedTokenException;

use constant {
    MEMO_RULE_FAILED => -2,
    MEMO_RULE_UNKNOWN => -1,
    INITIAL_FOLLOW_STACK_SIZE => 100,

    # copies from Token object for convenience in actions
    DEFAULT_TOKEN_CHANNEL => ANTLR::Runtime::Token->DEFAULT_CHANNEL,
    HIDDEN => ANTLR::Runtime::Token->HIDDEN_CHANNEL,

    NEXT_TOKEN_RULE_NAME => 'next_token',
};

# State of a lexer, parser, or tree parser are collected into a state
# object so the state can be shared.  This sharing is needed to
# have one grammar import others and share same error variables
# and other state variables.  It's a kind of explicit multiple
# inheritance via delegation of methods and shared state.
has 'state';

sub BUILD {
    my ($self, $arg_ref) = @_;

    if (exists $arg_ref->{state}) {
        $self->state($arg_ref->{state});
    }
    else {
        $self->state(ANTLR::Runtime::RecognizerSharedState->new());
    }
}

sub reset {
    my ($self) = @_;

    if (!defined $self->state) {
        return;
    }

    my $state = $self->state;
    $state->_fsp(-1);
    $state->error_recovery(0);
    $state->last_error_index(-1);
    $state->failed(0);
    $state->syntax_errors(0);

    # wack everything related to backtracking and memoization
    $state->backtracking(0);
    # wipe cache
    $state->rule_memo([]);
}

sub match {
    Readonly my $usage => 'void match(IntStream input, int ttype, BitSet follow)';
    croak $usage if @_ != 4;
    my ($self, $input, $ttype, $follow) = @_;

    my $matched_symbol = $self->get_current_input_symbol($input);
    if ($input->LA(1) eq $ttype) {
        $input->consume();
        $self->state->error_recovery(0);
        $self->state->failed(0);
        return $matched_symbol;
    }

    if ($self->state->backtracking > 0) {
        $self->state->failed(1);
        return $matched_symbol;
    }

    return $self->recover_from_mismatched_token($input, $ttype, $follow);
}

sub match_any {
    Readonly my $usage => 'void match_any(IntStream input)';
    croak $usage if @_ != 2;
    my ($self, $input) = @_;

    $self->state->error_recovery(0);
    $self->state->failed(0);
    $input->consume();
}

sub mismatch_is_unwanted_token {
    my ($self, $input, $ttype) = @_;
    return $input->LA(2) == $ttype;
}

sub mismatch_is_missing_token {
    my ($self, $input, $follow) = @_;

    if (!defined $follow) {
        return 0;
    }

    if ($follow->member(ANTLR::Runtime::Token->EOR_TOKEN_TYPE)) {
        my $viable_tokens_following_this_rule = $self->compute_context_sensitive_rule_FOLLOW();
        $follow = $follow->or($viable_tokens_following_this_rule);
        if ($self->state->_fsp >= 0) {
            $follow->remove(ANTLR::Runtime::Token->EOR_TOKEN_TYPE);
        }
    }

    if ($follow->member($input->LA(1)) || $follow->member(ANTLR::Runtime::Token->EOR_TOKEN_TYPE)) {
        return 1;
    }
    return 0;
}

sub mismatch {
    Readonly my $usage => 'void mismatch(IntStream input, int ttype, BitSet follow)';
    croak $usage if @_ != 4;
    my ($self, $input, $ttype, $follow) = @_;

    if ($self->mismatch_is_unwanted_token($input, $ttype)) {
        ANTLR::Runtime::UnwantedTokenException->new({
            expecting => $ttype,
            input => $input
        })->throw();
    }
    elsif ($self->mismatch_is_missing_token($input, $follow)) {
        ANTLR::Runtime::MissingTokenException->new({
            expecting => $ttype,
            input => $input
        })->throw();
    }
    else {
        ANTLR::Runtime::MismatchedTokenException->new({
            expecting => $ttype,
            input => $input
        })->throw();
    }
}

sub report_error {
    Readonly my $usage => 'void report_error(RecognitionException e)';
    croak $usage if @_ != 2;
    my ($self, $e) = @_;

    if ($self->state->error_recovery) {
        return;
    }
    $self->state->syntax_errors($self->state->syntax_errors + 1);
    $self->state->error_recovery(1);

    $self->display_recognition_error($self->get_token_names(), $e);
    return;
}

sub display_recognition_error {
    Readonly my $usage => 'void display_recognition_error(String[] token_names, RecognitionException e)';
    croak $usage if @_ != 3;
    my ($self, $token_names, $e) = @_;

    my $hdr = $self->get_error_header($e);
    my $msg = $self->get_error_message($e, $token_names);
    $self->emit_error_message("$hdr $msg");
}

sub get_error_message {
    Readonly my $usage => 'String get_error_message(RecognitionException e, String[] token_names)';
    croak $usage if @_ != 3;
    my ($self, $e, $token_names) = @_;

    if ($e->isa('ANTLR::Runtime::MismatchedTokenException')) {
        my $token_name;
        if ($e->get_expecting == ANTLR::Runtime::Token->EOF) {
            $token_name = 'EOF';
        } else {
            $token_name = $token_names->[$e->get_expecting];
        }

        return 'mismatched input ' . $self->get_token_error_display($e->get_token)
            . ' expecting ' . $token_name;
    } elsif ($e->isa('ANTLR::Runtime::MismatchedTreeNodeException')) {
        my $token_name;
        if ($e->get_expecting == ANTLR::Runtime::Token->EOF) {
            $token_name = 'EOF';
        } else {
            $token_name = $token_names->[$e->get_expecting];
        }

        return 'mismatched tree node: ' . $e->node
            . ' expecting ' . $token_name;
    } elsif ($e->isa('ANTLR::Runtime::NoViableAltException')) {
        return 'no viable alternative at input ' . $self->get_token_error_display($e->get_token);
    } elsif ($e->isa('ANTLR::Runtime::EarlyExitException')) {
        return 'required (...)+ loop did not match anything at input '
            . get_token_error_display($e->get_token);
    } elsif ($e->isa('ANTLR::Runtime::MismatchedSetException')) {
        return 'mismatched input ' . $self->get_token_error_display($e->get_token)
            . ' expecting set ' . $e->get_expecting;
    } elsif ($e->isa('ANTLR::Runtime::MismatchedNotSetException')) {
        return 'mismatched input ' . $self->get_token_error_display($e->get_token)
            . ' expecting set ' . $e->get_expecting;
    } elsif ($e->isa('ANTLR::Runtime::FailedPredicateException')) {
        return 'rule ' . $e->rule_name . ' failed predicate: {'
            . $e->predicate_text . '}?';
    } else {
        return undef;
    }
}

sub get_number_of_syntax_errors {
    my ($self) = @_;
    return $self->state->syntax_errors;
}

sub get_error_header {
    Readonly my $usage => 'String get_error_header(RecognitionException e)';
    croak $usage if @_ != 2;
    my ($self, $e) = @_;

    my $line = $e->get_line();
    my $col = $e->get_char_position_in_line();

    return "line $line:$col";
}

sub get_token_error_display {
    Readonly my $usage => 'String get_token_error_display(Token t)';
    croak $usage if @_ != 2;
    my ($self, $t) = @_;

    my $s = $t->get_text();
    if (!defined $s) {
        if ($t->get_type() == ANTLR::Runtime::Token->EOF) {
            $s = '<EOF>';
        } else {
            my $ttype = $t->get_type();
            $s = "<$ttype>";
        }
    }

    $s =~ s/\n/\\\\n/g;
    $s =~ s/\r/\\\\r/g;
    $s =~ s/\t/\\\\t/g;

    return "'$s'";
}

sub emit_error_message {
    Readonly my $usage => 'void emit_error_message(String msg)';
    croak $usage if @_ != 2;
    my ($self, $msg) = @_;

    print STDERR $msg, "\n";
}

sub recover {
    Readonly my $usage => 'void recover(IntStream input, RecognitionException re)';
    croak $usage if @_ != 3;
    my ($self, $input, $re) = @_;

    if ($self->state->last_error_index == $input->index()) {
	# uh oh, another error at same token index; must be a case
	# where LT(1) is in the recovery token set so nothing is
	# consumed; consume a single token so at least to prevent
	# an infinite loop; this is a failsafe.
        $input->consume();
    }

    $self->state->last_error_index($input->index());
    my $follow_set = $self->compute_error_recovery_set();
    $self->begin_resync();
    $self->consume_until($input, $follow_set);
    $self->end_resync();
}

sub begin_resync {
}

sub end_resync {
}

sub compute_error_recovery_set {
    Readonly my $usage => 'void compute_error_recovery_set()';
    croak $usage if @_ != 1;
    my ($self) = @_;

    $self->combine_follows(0);
}

sub compute_context_sensitive_rule_FOLLOW {
    Readonly my $usage => 'void compute_context_sensitive_rule_FOLLOW()';
    croak $usage if @_ != 1;
    my ($self) = @_;

    $self->combine_follows(1);
}

sub combine_follows {
    Readonly my $usage => 'BitSet combine_follows(boolean exact)';
    croak $usage if @_ != 2;
    my ($self, $exact) = @_;

    my $top = $self->state->_fsp;
    my $follow_set = ANTLR::Runtime::BitSet->new();

    foreach my $local_follow_set (reverse @{$self->state->following}) {
        $follow_set |= $local_follow_set;
        if ($exact && $local_follow_set->member(ANTLR::Runtime::Token->EOR_TOKEN_TYPE)) {
            last;
        }
    }
    #$follow_set->remove(ANTLR::Runtime::Token->EOR_TOKEN_TYPE);
    return $follow_set;
}

sub recover_from_mismatched_token {
    Readonly my $usage => 'void recover_from_mismatched_token(IntStream input, int ttype, BitSet follow)';
    croak $usage if @_ != 4;
    my ($self, $input, $ttype, $follow) = @_;

    if ($self->mismatch_is_unwanted_token($input, $ttype)) {
        my $ex = ANTLR::Runtime::UnwantedTokenException->new({
            expecting => $ttype,
            input => $input
        });

        $self->begin_resync();
        $input->consume();
        $self->end_resync();
        $self->report_error($ex);

        my $matched_symbol = $self->get_current_input_symbol($input);
        $input->consume();
        return $matched_symbol;
    }

    if ($self->mismatch_is_missing_token($input, $follow)) {
        my $inserted = $self->get_missing_symbol({
                input => $input,
                expected_token_type => $ttype,
                follow => $follow,
        });
        my $ex = ANTLR::Runtime::MissingTokenException({
            expecting => $ttype,
            input => $input,
            inserted => $inserted,
        });
        $self->report_error($ex);
        return $inserted;
    }

    ANTLR::Runtime::MismatchedTokenException->new({
        expecting => $ttype,
        input => $input
    })->throw();
}

sub recover_from_mismatched_set {
    Readonly my $usage => 'void recover_from_mismatched_set(IntStream input, RecognitionException e, BitSet follow)';
    croak $usage if @_ != 4;
    my ($self, $input, $e, $follow) = @_;

    if ($self->mismatch_is_missing_token($input, $follow)) {
        $self->report_error($e);
        return $self->get_missing_symbol({
                input => $input,
                exception => $e,
                expected_token_type => ANTLR::Runtime::Token->INVALID_TOKEN_TYPE,
                follow => $follow,
            });
    }

    $e->throw();
}

sub recover_from_mismatched_element {
    Readonly my $usage => 'boolean recover_from_mismatched_element(IntStream input, RecognitionException e, BitSet follow)';
    croak $usage if @_ != 4;
    my ($self, $input, $e, $follow) = @_;

    return 0 if (!defined $follow);

    if ($follow->member(ANTLR::Runtime::Token->EOR_TOKEN_TYPE)) {
        my $viable_tokens_following_this_rule = $self->compute_context_sensitive_rule_FOLLOW();
        $follow |= $viable_tokens_following_this_rule;
        $follow->remove(ANTLR::Runtime::Token->EOR_TOKEN_TYPE);
    }

    if ($follow->member($input->LA(1))) {
        $self->report_error($e);
        return 1;
    }

    return 0;
}

sub get_current_input_symbol {
    my ($self, $input) = @_;
    return undef;
}

sub get_missing_symbol {
    my ($self, $arg_ref) = @_;
    my $input = $arg_ref->{input};
    my $exception = $arg_ref->{exception};
    my $expected_token_type = $arg_ref->{expected_token_type};
    my $follow = $arg_ref->{follow};

    return undef;
}

sub consume_until {
    Readonly my $usage => 'void consume_until(IntStream input, (int token_type | BitSet set))';
    croak $usage if @_ != 3;

    if ($_[2]->isa('ANTLR::Runtime::BitSet')) {
        my ($self, $input, $set) = @_;

        my $ttype = $input->LA(1);
        while ($ttype != ANTLR::Runtime::Token->EOF && !$set->member($ttype)) {
            $input->consume();
            $ttype = $input->LA(1);
        }
    } else {
        my ($self, $input, $token_type) = @_;

        my $ttype = $input->LA(1);
        while ($ttype != ANTLR::Runtime::Token->EOF && $ttype != $token_type) {
            $input->consume();
            $ttype = $input->LA(1);
        }
    }
}

sub push_follow {
    Readonly my $usage => 'void push_follow(BitSet fset)';
    croak $usage if @_ != 2;
    my ($self, $fset) = @_;

    push @{$self->state->following}, $fset;
    $self->state->_fsp($self->state->_fsp + 1);
}

sub get_rule_invocation_stack {
    Readonly my $usage => 'List get_rule_invocation_stack()';
    croak $usage if @_ != 1;
    my ($self) = @_;

    my $rules = [];
    for (my $i = 0; ; ++$i) {
        my @frame = caller $i;
        last if !@frame;

        my ($package, $filename, $line, $subroutine) = @frame;

        if ($package =~ /^ANTLR::Runtime::/) {
            next;
        }

        if ($subroutine eq NEXT_TOKEN_RULE_NAME) {
            next;
        }

        if ($package ne ref $self) {
            next;
        }

        push @{$rules}, $subroutine;
    }
}

sub get_backtracking_level {
    Readonly my $usage => 'int get_backtracking_level()';
    croak $usage if @_ != 1;
    my ($self) = @_;

    return $self->state->backtracking;
}

sub set_backtracking_level {
    my ($self, $n) = @_;
    $self->state->backtracking($n);
}

sub failed {
    my ($self) = @_;
    return $self->state->failed;
}

sub get_token_names {
    return undef;
}

sub get_grammar_file_name {
    return undef;
}

sub to_strings {
    Readonly my $usage => 'List to_strings(List tokens)';
    croak $usage if @_ != 2;
    my ($self, $tokens) = @_;

    if (!defined $tokens) {
        return undef;
    }

    return map { $_->get_text() } @{$tokens};
}

sub get_rule_memoization {
    Readonly my $usage => 'int get_rule_memoization(int rule_index, int rule_start_index)';
    croak $usage if @_ != 3;
    my ($self, $rule_index, $rule_start_index) = @_;

    if (!defined $self->rule_memo->[$rule_index]) {
        $self->rule_memo->[$rule_index] = {};
    }

    my $stop_index = $self->state->rule_memo->[$rule_index]->{$rule_start_index};
    if (!defined $stop_index) {
        return $self->MEMO_RULE_UNKNOWN;
    }
    return $stop_index;
}

sub alredy_parsed_rule {
    Readonly my $usage => 'boolean alredy_parsed_rule(IntStream input, int rule_index)';
    croak $usage if @_ != 3;
    my ($self, $input, $rule_index) = @_;

    my $stop_index = $self->get_rule_memoization($rule_index, $input->index());
    if ($stop_index == $self->MEMO_RULE_UNKNOWN) {
        return 0;
    }

    if ($stop_index == $self->MEMO_RULE_FAILED) {
        $self->state->failed(1);
    } else {
        $input->seek($stop_index + 1);
    }
    return 1;
}

sub memoize {
    Readonly my $usage => 'void memoize(IntStream input, int rule_index, int rule_start_index)';
    croak $usage if @_ != 4;
    my ($self, $input, $rule_index, $rule_start_index) = @_;

    my $stop_token_index = $self->state->failed ? $self->MEMO_RULE_FAILED : $input->index() - 1;
    if (defined $self->state->rule_memo->[$rule_index]) {
        $self->state->rule_memo->[$rule_index]->{$rule_start_index} = $stop_token_index;
    }
}

sub get_rule_memoization_cache_size {
    Readonly my $usage => 'int get_rule_memoization_cache_size()';
    croak $usage if @_ != 1;
    my ($self) = @_;

    my $n = 0;
    foreach my $m (@{$self->state->rule_memo}) {
        $n += keys %{$m} if defined $m;
    }

    return $n;
}

sub trace_in {
    Readonly my $usage => 'void trace_in(String rule_name, int rule_index, input_symbol)';
    croak $usage if @_ != 4;
    my ($self, $rule_name, $rule_index, $input_symbol) = @_;

    print "enter $rule_name $input_symbol";
    if ($self->state->failed) {
        print ' failed=', $self->state->failed;
    }
    if ($self->state->backtracking > 0) {
        print ' backtracking=', $self->state->backtracking;
    }
    print "\n";
}

sub trace_out {
    Readonly my $usage => 'void trace_out(String rule_name, int rule_index, input_symbol)';
    croak $usage if @_ != 4;
    my ($self, $rule_name, $rule_index, $input_symbol) = @_;

    print "exit $rule_name $input_symbol";
    if ($self->state->failed) {
        print ' failed=', $self->state->failed;
    }
    if ($self->state->backtracking > 0) {
        print ' backtracking=', $self->state->backtracking;
    }
    print "\n";
}

1;

__END__

=head1 NAME

ANTLR::Runtime::BaseRecognizer

=head1 DESCRIPTION

A generic recognizer that can handle recognizers generated from
lexer, parser, and tree grammars.  This is all the parsing
support code essentially; most of it is error recovery stuff and
backtracking.
