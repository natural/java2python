package ANTLR::Runtime::TokenStream;
use ANTLR::Runtime::Class;

use Readonly;

extends 'ANTLR::Runtime::IntStream';

sub LT {
    Readonly my $usage => 'Token LT(int k)';
}

sub get {
    Readonly my $usage => 'Token get(int i)';
}

sub get_token_source {
    Readonly my $usage => 'TokenSource get_token_source()';
}

sub to_string {
    Readonly my $usage => 'String to_string(int start, int stop) | String to_string(Token start, Token stop)';
}

1;
