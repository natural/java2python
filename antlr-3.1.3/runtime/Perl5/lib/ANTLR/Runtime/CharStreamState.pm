package ANTLR::Runtime::CharStreamState;
use ANTLR::Runtime::Class;

# Index into the char stream of next lookahead char
has 'p';

# What line number is the scanner at before processing buffer[p]?
has 'line';

# What char position 0..n-1 in line is scanner before processing buffer[p]?
has 'char_position_in_line';

1;
