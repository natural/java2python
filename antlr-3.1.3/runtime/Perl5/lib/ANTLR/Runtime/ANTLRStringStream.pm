package ANTLR::Runtime::ANTLRStringStream;
use ANTLR::Runtime::Class;

use Carp;
use Readonly;

use ANTLR::Runtime::CharStreamState;

extends 'ANTLR::Runtime::CharStream';

has 'input';
has 'p';
has 'line';
has 'char_position_in_line';
has 'mark_depth';
has 'markers';
has 'last_marker';

sub BUILD {
    my ($self, $arg_ref) = @_;

    $self->input($arg_ref->{input});
    $self->p(0);
    $self->line(1);
    $self->char_position_in_line(0);
    $self->mark_depth(0);
    $self->markers([ undef ]);  # depth 0 means no backtracking, leave blank
    $self->last_marker(0);
}

sub get_line {
    my ($self) = @_;
    return $self->line;
}

sub set_line {
    my ($self, $value) = @_;
    $self->line($value);
    return;
}

sub get_char_position_in_line {
    my ($self) = @_;
    return $self->char_position_in_line;
}

sub set_char_position_in_line {
    my ($self, $value) = @_;
    $self->char_position_in_line($value);
    return;
}

sub reset {
    Readonly my $usage => 'reset()';
    croak $usage if @_ != 1;
    my ($self) = @_;

    $self->p(0);
    $self->line(1);
    $self->char_position_in_line(0);
    $self->mark_depth(0);
}

sub consume {
    Readonly my $usage => 'consume()';
    croak $usage if @_ != 1;
    my ($self) = @_;

    if ($self->p < length $self->input) {
        $self->char_position_in_line($self->char_position_in_line + 1);
        if (substr($self->input, $self->p, 1) eq "\n") {
            $self->line($self->line + 1);
            $self->char_position_in_line(0);
        }
        $self->p($self->p + 1);
    }
}

sub LA {
    Readonly my $usage => 'char LA($i)';
    croak $usage if @_ != 2;
    my ($self, $i) = @_;

    if ($i == 0) {
        return undef;
    }

    if ($i < 0) {
        ++$i; # e.g., translate LA(-1) to use offset i=0; then input[p+0-1]
        if ($self->p + $i - 1 < 0) {
            return $self->EOF;
        }
    }

    if ($self->p + $i - 1 >= length $self->input) {
        return $self->EOF;
    }

    return substr $self->input, $self->p + $i - 1, 1;
}

sub LT {
    Readonly my $usage => 'char LT($i)';
    croak $usage if @_ != 2;
    my ($self, $i) = @_;

    return $self->LA($i);
}

sub index {
    Readonly my $usage => 'int index()';
    croak $usage if @_ != 1;
    my ($self) = @_;

    return $self->p;
}

sub size {
    Readonly my $usage => 'int size()';
    croak $usage if @_ != 1;
    my ($self) = @_;

    return length $self->input;
}

sub mark {
    Readonly my $usage => 'int mark()';
    croak $usage if @_ != 1;
    my ($self) = @_;

    $self->mark_depth($self->mark_depth + 1);
    my $state;
    if ($self->mark_depth >= @{$self->markers}) {
        $state = ANTLR::Runtime::CharStreamState->new();
        push @{$self->markers}, $state;
    } else {
        $state = $self->markers->[$self->mark_depth];
    }

    $state->set_p($self->p);
    $state->set_line($self->line);
    $state->set_char_position_in_line($self->char_position_in_line);
    $self->last_marker($self->mark_depth);

    return $self->mark_depth;
}

sub rewind {
    Readonly my $usage => 'rewind($m)';
    croak $usage if @_ != 1 && @_ != 2;
    my $self = shift;
    my $m;
    if (@_ == 0) {
        $m = $self->last_marker;
    } else {
        $m = shift;
    }

    my $state = $self->markers->[$m];
    # restore stream state
    $self->seek($state->get_p);
    $self->line($state->get_line);
    $self->char_position_in_line($state->get_char_position_in_line);
    $self->release($m);
}

sub release {
    Readonly my $usage => 'release($marker)';
    croak $usage if @_ != 2;
    my ($self, $marker) = @_;

    # unwind any other markers made after m and release m
    $self->mark_depth($marker);
    # release this marker
    $self->mark_depth($self->mark_depth - 1);
}

# consume() ahead unit p == index; can't just set p = index as we must update
# line and char_position_in_line
sub seek {
    Readonly my $usage => 'seek($index)';
    croak $usage if @_ != 2;
    my ($self, $index) = @_;

    if ($index <= $self->p) {
        # just jump; don't update stream state (line, ...)
        $self->p($index);
        return;
    }

    # seek forward, consume until p hits index
    while ($self->p < $index) {
        $self->consume();
    }
}

sub substring {
    Readonly my $usage => 'string substring($start, $stop)';
    croak $usage if @_ != 3;
    my ($self, $start, $stop) = @_;

    return substr $self->input, $start, $stop - $start + 1;
}

1;
