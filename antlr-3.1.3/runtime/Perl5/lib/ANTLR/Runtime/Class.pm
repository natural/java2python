package ANTLR::Runtime::Class;

use strict;
use warnings;
use Carp;

use base 'Exporter';
our @EXPORT = qw( has extends );

sub create_accessor {
    my ($class, $name, $mode) = @_;

    if ($mode =~ /r/) {
        ## no critic (TestingAndDebugging::ProhibitNoStrict)
        no strict 'refs';
        *{"${class}::get_$name"} = sub {
            my ($self) = @_;
            return $self->$name;
        };
    }

    if ($mode =~ /w/) {
        ## no critic (TestingAndDebugging::ProhibitNoStrict)
        no strict 'refs';
        *{"${class}::set_$name"} = sub {
            my ($self, $value) = @_;
            $self->$name($value);
            return;
        };
    }
}

sub create_accessors {
    my ($class, $accessors) = @_;
    while (my ($name, $mode) = each %$accessors) {
        create_accessor($class, $name, $mode);
    }
}


sub create_attribute {
    my ($class, $name) = @_;

    ## no critic (TestingAndDebugging::ProhibitNoStrict)
    no strict 'refs';
    *{"${class}::$name"} = sub {
        if (@_ == 1) {
            my ($self) = @_;
            return $self->{$name};
        } elsif (@_ == 2) {
            my ($self, $value) = @_;
            return $self->{$name} = $value;
        }
    };
}

sub create_attributes {
    my ($class, $attributes) = @_;
    foreach my $attribute (@$attributes) {
        create_attribute($class, $attribute);
    }
}

sub new {
    my ($class) = @_;

    my $self = bless {}, $class;
    return $self;
}

sub import {
    ANTLR::Runtime::Class->export_to_level(1, @_);

    strict->import;
    warnings->import;

    my $class = (caller())[0];
    no strict 'refs';
    require ANTLR::Runtime::Object;
    push @{"${class}::ISA"}, 'ANTLR::Runtime::Object';

    return;
}

sub has {
    my ($name) = @_;
    my $class = (caller())[0];

    {
        ## no critic (TestingAndDebugging::ProhibitNoStrict)
        no strict 'refs';
        *{"${class}::$name"} = sub {
            if (@_ == 0) {
                croak "static call to accessor $name";
            }
            elsif (@_ == 1) {
                my ($self) = @_;
                return $self->{$name};
            }
            elsif (@_ == 2) {
                my ($self, $value) = @_;
                return $self->{$name} = $value;
            }
            else {
                croak "Too many arguments to $name";
            }
        };
    }
    return;
}

sub is_class_loaded {
    my ($class) = @_;

    my $pack = \*::;
    foreach my $part (split('::', $class)) {
        return 0 unless exists ${$$pack}{"${part}::"};
        $pack = \*{${$$pack}{"${part}::"}};
    }

    # check for $VERSION or @ISA
    return 1 if exists ${$$pack}{VERSION}
             && defined *{${$$pack}{VERSION}}{SCALAR};
    return 1 if exists ${$$pack}{ISA}
             && defined *{${$$pack}{ISA}}{ARRAY};

    # check for any method
    foreach ( keys %{$$pack} ) {
        next if substr($_, -2, 2) eq '::';

        my $glob = ${$$pack}{$_} || next;

        return 1 if ref $glob eq 'SCALAR';
        return 1 if defined *{$glob}{CODE};
    }

    # fail
    return 0;
}

sub extends {
    my (@superclasses) = @_;
    my $class = (caller())[0];

    foreach my $class (@superclasses) {
        next if is_class_loaded($class);
        eval "require $class";
        die $@ if $@;
    }

    no strict 'refs';
    @{"${class}::ISA"} = @superclasses;
}

1;
