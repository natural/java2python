package ANTLR::Runtime::ANTLRFileStream;
use ANTLR::Runtime::Class;

use Carp;
use Readonly;

extends 'ANTLR::Runtime::ANTLRStringStream';

has 'file_name';

sub BUILD {
    my ($self, $arg_ref) = @_;

    $self->file_name($arg_ref->{file_name});
    $self->load(@$arg_ref{qw( file_name encoding )});
}

sub load {
    my ($self, $file_name, $encoding) = @_;

    if (!defined $file_name) {
        return;
    }

    my $fh;
    if (defined $encoding) {
        open $fh, "<:encoding($encoding)", $file_name
            or croak "Can't open $file_name: $!";
    }
    else {
        open $fh, '<', $file_name
            or croak "Can't open $file_name: $!";
    }

    my $content;
    {
        local $/;
        $content = <$fh>;
    }
    $self->input($content);
    return;
}

sub get_source_name {
    my ($self) = @_;
    return $self->file_name;
}

1;
__END__
