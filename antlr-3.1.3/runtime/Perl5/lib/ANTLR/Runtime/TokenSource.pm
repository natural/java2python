package ANTLR::Runtime::TokenSource;
use ANTLR::Runtime::Class;

# Return a Token object from your input stream (usually a CharStream).
# Do not fail/return upon lexing error; keep chewing on the characters
# until you get a good one; errors are not passed through to the parser.
sub next_token {
}

1;
__END__

=head1 NAME

ANTLR::Runtime::TokenSource

=head1 DESCRIPTION

A source of tokens must provide a sequence of tokens via nextToken()
and also must reveal it's source of characters; CommonToken's text is
computed from a CharStream; it only store indices into the char stream.

Errors from the lexer are never passed to the parser.  Either you want
to keep going or you do not upon token recognition error.  If you do not
want to continue lexing then you do not want to continue parsing.  Just
throw an exception not under RecognitionException and Java will naturally
toss you all the way out of the recognizers.  If you want to continue
lexing then you should not throw an exception to the parser--it has already
requested a token.  Keep lexing until you get a valid one.  Just report
errors and keep going, looking for a valid token.
