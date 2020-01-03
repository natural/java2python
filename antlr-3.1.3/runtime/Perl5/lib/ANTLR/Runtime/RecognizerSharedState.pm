package ANTLR::Runtime::RecognizerSharedState;
use ANTLR::Runtime::Class;

# Track the set of token types that can follow any rule invocation.
# Stack grows upwards.  When it hits the max, it grows 2x in size
# and keeps going.
has 'following';
has '_fsp';

# This is true when we see an error and before having successfully
# matched a token.  Prevents generation of more than one error message
# per error.
has 'error_recovery';

# The index into the input stream where the last error occurred.
# This is used to prevent infinite loops where an error is found
# but no token is consumed during recovery...another error is found,
# ad naseum.  This is a failsafe mechanism to guarantee that at least
# one token/tree node is consumed for two errors.
has 'last_error_index';

# In lieu of a return value, this indicates that a rule or token
# has failed to match.  Reset to false upon valid token match.
has 'failed';

# Did the recognizer encounter a syntax error?  Track how many.
has 'syntax_errors';

# If 0, no backtracking is going on.  Safe to exec actions etc...
# If >0 then it's the level of backtracking.
has 'backtracking';

# An array[size num rules] of Map<Integer,Integer> that tracks
# the stop token index for each rule.  ruleMemo[ruleIndex] is
# the memoization table for ruleIndex.  For key ruleStartIndex, you
# get back the stop token for associated rule or MEMO_RULE_FAILED.
# This is only used if rule memoization is on (which it is by default).
has 'rule_memo';

# The goal of all lexer rules/methods is to create a token object.
# This is an instance variable as multiple rules may collaborate to
# create a single token.  nextToken will return this object after
# matching lexer rule(s).  If you subclass to allow multiple token
# emissions, then set this to the last token to be matched or
# something nonnull so that the auto token emit mechanism will not
# emit another token.
has 'token';

# What character index in the stream did the current token start at?
# Needed, for example, to get the text for current token.  Set at
# the start of nextToken.
has 'token_start_char_index';

# The line on which the first character of the token resides
has 'token_start_line';

# The character position of first character within the line
has 'token_start_char_position_in_line';

# The channel number for the current token
has 'channel';

# The token type for the current token
has 'type';

# You can set the text for the current token to override what is in
# the input char buffer.  Use setText() or can set this instance var.
has 'text';

sub BUILD {
    my ($self, $arg_ref) = @_;

    $self->following([]);
    $self->_fsp(-1);
    $self->error_recovery(0);
    $self->last_error_index(-1);
    $self->failed(0);
    $self->syntax_errors(0);
    $self->backtracking(0);
    $self->token_start_char_index(-1);
}

1;
__END__
