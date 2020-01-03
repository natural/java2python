package ANTLR::Runtime::CommonToken;
use ANTLR::Runtime::Class;

use Readonly;

use overload
    'bool' => \&not_eof,
    fallback => 1,
    ;

extends 'ANTLR::Runtime::Token';

has 'type';
has 'line';
has 'char_position_in_line';
has 'channel';
has 'input';
has 'text';
has 'index';
has 'start';
has 'stop';

sub BUILD {
    my ($self, $arg_ref) = @_;

    $self->type(undef);
    $self->line(0);
    # set to invalid position
    $self->char_position_in_line(-1);
    $self->channel($self->DEFAULT_CHANNEL);
    $self->input(undef);

    # We need to be able to change the text once in a while.  If
    # this is non-null, then getText should return this.  Note that
    # start/stop are not affected by changing this.
    $self->text(undef);

    # What token number is this from 0..n-1 tokens; < 0 implies invalid index
    $self->index(-1);

    # The char position into the input buffer where this token starts
    $self->start(undef);

    # The char position into the input buffer where this token stops
    $self->stop(undef);

    if (exists $arg_ref->{type}) {
        $self->type($arg_ref->{type});
    }

    if (exists $arg_ref->{input}) {
        $self->input($arg_ref->{input});
    }

    if (exists $arg_ref->{channel}) {
        $self->channel($arg_ref->{channel});
    }

    if (exists $arg_ref->{start}) {
        $self->start($arg_ref->{start});
    }

    if (exists $arg_ref->{stop}) {
        $self->stop($arg_ref->{stop});
    }

    if (exists $arg_ref->{text}) {
        $self->text($arg_ref->{text});
    }

    if (exists $arg_ref->{token}) {
        my $token = $arg_ref->{token};
        $self->text($token->get_text());
        $self->type($token->get_type());
        $self->line($token->get_line());
        $self->index($token->get_token_index());
        $self->char_position_in_line($token->get_char_position_in_line());
        $self->channel($token->get_channel());
    }
}

ANTLR::Runtime::Class::create_accessors(__PACKAGE__, {
    type => 'rw',
    line => 'rw',
    text => 'w',
    char_position_in_line => 'rw',
    channel => 'rw',
    input => 'rw',
    index => 'rw',
    start => 'rw',
    stop => 'rw',
});

sub get_text {
    Readonly my $usage => 'string get_text()';
    croak $usage if @_ != 1;
    my ($self) = @_;

    if (defined $self->text) {
        return $self->text;
    }
    if (!defined $self->input) {
        return undef;
    }
    $self->text($self->input->substring($self->start, $self->stop));
    return $self->text;
}

sub get_start_index {
    my ($self) = @_;
    return $self->start;
}

sub set_start_index {
    my ($self, $start) = @_;
    $self->start($start);
}

sub get_stop_index {
    my ($self) = @_;
    return $self->stop;
}

sub set_stop_index {
    my ($self, $stop) = @_;
    $self->stop($stop);
}

sub get_token_index {
    my ($self) = @_;
    return $self->index;
}

sub set_token_index {
    my ($self, $index) = @_;
    $self->index($index);
}

sub not_eof {
    my ($self) = @_;
    return $self->type != ANTLR::Runtime::Token->EOF;
}

=begin later

	public String toString() {
		String channelStr = "";
		if ( channel>0 ) {
			channelStr=",channel="+channel;
		}
		String txt = getText();
		if ( txt!=null ) {
			txt = txt.replaceAll("\n","\\\\n");
			txt = txt.replaceAll("\r","\\\\r");
			txt = txt.replaceAll("\t","\\\\t");
		}
		else {
			txt = "<no text>";
		}
		return "[@"+getTokenIndex()+","+start+":"+stop+"='"+txt+"',<"+type+">"+channelStr+","+line+":"+getCharPositionInLine()+"]";
	}

=end later

=cut

1;
