package ANTLR::Runtime::DFA;
use ANTLR::Runtime::Class;

use Params::Validate qw( :types );
use Error qw( :try );

has 'eot';
has 'eof';
has 'min';
has 'max';
has 'accept';
has 'special';
has 'transition';
has 'decision_number';

# Which recognizer encloses this DFA?  Needed to check backtracking
has 'recognizer';

sub get_description {
    return "n/a";
}

# From the input stream, predict what alternative will succeed
# using this DFA (representing the covering regular approximation
# to the underlying CFL).  Return an alternative number 1..n.  Throw
# an exception upon error.
sub predict {
    my $self = shift;
    my $param_ref = __PACKAGE__->unpack_params(\@_, {
        spec => [
            {
                name => 'input',
                isa => 'ANTLR::Runtime::IntStream',
            }

        ]
    });
    my $input = $param_ref->{input};

    my $mark = $input->mark();  # remember where decision started in input
    my $s = 0; # we always start at s0

    try {
        while (1) {
            my $special_state = $self->special->[$s];
            if ($special_state >= 0) {
                $s = $self->special_state_transition($special_state, $input);
                if ($s == -1) {
                    $self->no_viable_alt($s, $input);
                    return 0;
                }
                $input->consume();
                next;
            }

            if ($self->accept->[$s] >= 1) {
                return $self->accept->[$s];
            }

	    # look for a normal char transition
            my $c = $input->LA(1);  # -1 == \uFFFF, all tokens fit in 65000 space

            if ($c >= $self->min->[$s] && $c <= $self->max->[$s]) {
                my $next_s = $self->transition->[$s][$c - $self->min->[$s]];  # move to next state

                if ($next_s < 0) {
                    # was in range but not a normal transition
                    # must check EOT, which is like the else clause.
                    # eot[s]>=0 indicates that an EOT edge goes to another
                    # state.
                    if ($self->eot->[$s] >= 0) {  # EOT Transition to accept state?
                        $s = $self->eot->[$s];
                        $input->consume();
                        # TODO: I had this as return accept[eot[s]]
                        # which assumed here that the EOT edge always
                        #went to an accept...faster to do this, but
                        # what about predicated edges coming from EOT
                        # target?
                        next;
                    }

                    $self->no_viable_alt($s, $input);
                    return 0;
                }

                $s = $next_s;
                $input->consume();
                next;
            }

	    if ($self->eot->[$s] >= 0) {  # EOT Transition?
		$s = $self->eot->[$s];
		$input->consume();
		next;
	    }

	    if ($c == ANTLR::Runtime::Token->EOF && $self->eof->[$s] >= 0) {  # EOF Transition to accept state?
		return $self->accept->[$self->eof->[$s]];
	    }

	    # not in range and not EOF/EOT, must be invalid symbol
	    $self->no_viable_alt($s, $input);
	    return 0;
        }
    }
    finally {
	$input->rewind();
    };
}

sub no_viable_alt {
    my $self = shift;
    my $param_ref = __PACKAGE__->unpack_params(\@_, {
	spec => [
	    {
		name => 's',
		type => SCALAR,
	    },
	    {
		name => 'input',
		isa  => 'ANTLR::Runtime::IntStream'
	    },
	]
    });
    my $s = $param_ref->{s};
    my $input = $param_ref->{input};

    if ($self->recognizer->state->backtracking > 0) {
	$self->recognizer->state->failed = 1;
	return;
    }
    my $nvae = ANTLR::Runtime::NoViableAltException({
	grammar_decision_description => $self->get_description(),
	decision_number => $self->decision_number,
	state_number => $self->state_number,
	input => $input
    });
    $self->error($nvae);
    $nvae->throw();
}

# A hook for debugging interface
sub error {
    my $self = shift;
    my $param_ref = __PACKAGE__->unpack_params(\@_, {
	spec => [
	    {
		name => 'nvae',
		isa  => 'ANTLR::Runtime::NoViableAltException',
	    }
	]
    });

    my $nvae = $param_ref->{nvae};
}

sub special_state_transition {
    my $self = shift;
    my $param_ref  = __PACKAGE__->unpack_params(\@_, {
	spec => [
	    {
		name => 's',
		type => SCALAR,
	    },
	    {
		name => 'input',
		isa  => 'ANTLR::Runtime::IntStream',
	    },
	]
    });

    return -1;
}

sub unpack_rle {
    my $self = shift;
    my $param_ref = __PACKAGE__->unpack_params(\@_, {
        spec => [
            {
                name => 'rle',
                type => ARRAYREF,
            }
        ]
    });
    my $rle = $param_ref->{rle};

    my $data = [];
    for (my $i = 0; $i < scalar @$rle; $i += 2) {
        my $count = $rle->[$i];
        my $item = $rle->[$i];

        push @$data, ($item) x $count;
    }

    return $data;
}

# Given a String that has a run-length-encoding of some unsigned shorts
# like "\1\2\3\9", convert to short[] {2,9,9,9}.  We do this to avoid
# static short[] which generates so much init code that the class won't
# compile. :(
sub unpack_encoded_string {
    my $self = shift;
    my $param_ref = __PACKAGE__->unpack_params(\@_, {
        spec => [
            {
                name => 'encoded_string',
                type => SCALAR,
            },
        ]
    });

    my $encoded_string = $param_ref->{encoded_string};

    my $data = [];
    while ($encoded_string =~ /(.)(.)/g) {
        my ($n, $v) = ($1, $2);

        push @$data, $v x $n;
    }

    return $data;
}

sub unpack_encoded_string_to_unsigned_chars {
    unpack_encoded_string(@_);
}

1;

__END__
