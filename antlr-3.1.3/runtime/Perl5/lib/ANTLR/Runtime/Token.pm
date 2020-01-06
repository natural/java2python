package ANTLR::Runtime::Token;
use ANTLR::Runtime::Class;

use Readonly;

use ANTLR::Runtime::CharStream;
use ANTLR::Runtime::CommonToken;

use constant {
    EOR_TOKEN_TYPE => 1,

    # imaginary tree navigation type; traverse "get child" link
    DOWN => 2,

    # imaginary tree navigation type; finish with a child list
    UP => 3,
};

use constant MIN_TOKEN_TYPE => UP + 1;

# All tokens go to the parser (unless skip() is called in that rule)
# on a particular "channel".  The parser tunes to a particular channel
# so that whitespace etc... can go to the parser on a "hidden" channel.
use constant DEFAULT_CHANNEL => 0;

# Anything on different channel than DEFAULT_CHANNEL is not parsed
# by parser.
use constant HIDDEN_CHANNEL => 99;

use constant EOF => ANTLR::Runtime::CharStream->EOF;
#use constant EOF_TOKEN => ANTLR::Runtime::CommonToken->new({ type => EOF });
sub EOF_TOKEN() {
    return ANTLR::Runtime::CommonToken->new({ type => EOF });
}

use constant INVALID_TOKEN_TYPE => 0;
#use constant INVALID_TOKEN => ANTLR::Runtime::CommonToken->new({ type => INVALID_TOKEN_TYPE });
sub INVALID_TOKEN() {
    return ANTLR::Runtime::CommonToken->new({ type => INVALID_TOKEN_TYPE });
}

# In an action, a lexer rule can set token to this SKIP_TOKEN and ANTLR
# will avoid creating a token for this symbol and try to fetch another.
#use constant SKIP_TOKEN => ANTLR::Runtime::CommonToken->new({ type => INVALID_TOKEN_TYPE });
sub SKIP_TOKEN() {
    return ANTLR::Runtime::CommonToken->new({ type => INVALID_TOKEN_TYPE });
}

1;
