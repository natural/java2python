package ANTLR::Runtime::Stream;
use ANTLR::Runtime::Class;

use Readonly;

sub consume {
    Readonly my $usage => 'void consume()';
}

sub LA {
    Readonly my $usage => 'int LA(int i)';
}

sub mark {
    Readonly my $usage => 'int mark()';
}

sub index {
    Readonly my $usage => 'int index()';
}

sub rewind {
    Readonly my $usage => 'void rewind()';
}

sub release {
    Readonly my $usage => 'void release(int marker)';
}

sub seek {
    Readonly my $usage => 'void seek(int index)';
}

sub size {
    Readonly my $usage => 'int size()';
}

1;
