package ANTLR::Runtime::Object;

use strict;
use warnings;

use Carp;
use Attribute::Handlers;
use List::MoreUtils qw( zip );
use Params::Validate qw( validate );

BEGIN {
    our @EXPORT = qw( unpack_params has );
}

sub Constant :ATTR(BEGIN) {
    my ($package, $symbol, $referent, $attr, $data, $phase, $filename, $linenum) = @_;
    my $args;
    if (defined $data) {
        $args = { @$data };
    }
    else {
        $args = {};
    }

    my $name;
    if ($args->{Name}) {
        $name = $args->{Name};
    }
    else {
        $name = *{$symbol}{NAME};
    }

    no strict 'refs';
    *{"${package}::$name"} = sub {
        return $$referent;
    };
}

sub Signature :ATTR(CODE) {
    my ($package, $symbol, $referent, $attr, $data, $phase, $filename, $linenum) = @_;
    #print map {"$_\n"} @_;
}

sub MODIFY_ARRAY_ATTRIBUTES {
    my ($package, $referent, @attributes) = @_;

    my @filtered_attributes;
    foreach my $attribute (@attributes) {
        if ($attribute =~ /^Field\((\w*)\)$/) {
            my $name = $1;
            push @filtered_attributes, 'Field';
            push @filtered_attributes, "Accessor(Name => '$name', Private => 1, lvalue => 1)";
        }
        elsif ($attribute =~ /^Name\((\w*)\)$/) {
            my $name = $1;
            push @filtered_attributes, "Accessor(Name => '$name', Private => 1, lvalue => 1)";
        }
        else {
            push @filtered_attributes, $attribute;
        }
    }
    return;
}

sub Abstract :ATTR(CODE) {
    my ($package, $symbol, $referent, $attr, $data, $phase, $filename, $linenum) = @_;

    my $fqmn = $package . '::' . *{$symbol}{NAME};
    no strict 'refs';
    *{$fqmn} = sub {
        my ($file, $line) = (caller)[1,2];
        croak "call to abstract method $fqmn at $file line $line.\n";
    };
}

sub unpack_params {
    my ($self, $params_ref, $opt_ref) = @_;

    my $spec = $opt_ref->{spec};

    my @params = @$params_ref;
    my $named_param_ref;
    if (@params == 1 && ref $params[0] eq 'HASH') {
        $named_param_ref = $params[0];
    }
    else {
        my @names = map { $_->{name} } grep { exists $_->{name} } @$spec;
        $named_param_ref = {
            zip(@names, @params)
        };
    }

    my $validate_spec = {};
    foreach my $s (@$spec) {
        my $name = $s->{name};
        my $vspec = { %$s };
        delete $vspec->{name};
        if (exists $vspec->{required}) {
            $vspec->{optional} = $vspec->{required};
        }
        $validate_spec->{$name} = $vspec;
    }

    my $params_unpacked_ref = {
        validate(@{[ $named_param_ref ]}, $validate_spec)
    };

    return $params_unpacked_ref;
}

sub unpack_method_args {
    my ($class, $args_ref, $opt_ref) = @_;

    my $spec = $opt_ref->{spec};
    my @param_names = map { $_->{name} } grep { exists $_->{name} } @$spec;

    my ($obj, @args) = @$args_ref;
    my $named_args_ref;
    if (@args == 1 && ref $args[0] eq 'HASH') {
        $named_args_ref = $args[0];
    }
    else {
        $named_args_ref = {
            zip(@param_names, @args)
        };
    }

    my $validate_spec = {};
    foreach my $s (@$spec) {
        my $name = $s->{name};
        my $vspec = { %$s };
        delete $vspec->{name};
        if (exists $vspec->{required}) {
            $vspec->{optional} = $vspec->{required};
        }
        $validate_spec->{$name} = $vspec;
    }

    my $unpacked_args_ref = {
        validate(@{[ $named_args_ref ]}, $validate_spec)
    };

    return ($obj, @{ $unpacked_args_ref }{ @param_names });
}

#---


sub new {
    my ($class, @args) = @_;
    my $self = bless {}, $class;
    my $arg_ref = $class->BUILDARGS(@args);
    $self->BUILDALL($arg_ref);
    return $self;
}

sub BUILDARGS {
    my ($class, @args) = @_;

    if (@args == 1) {
        if (ref $args[0] eq 'HASH') {
            return $args[0];
        }
        else {
            croak "Single parameters to new must be a hash reference";
        }
    }
    else {
        return {@args};
    }
}

sub linearized_isa {
    my ($class) = @_;
    return @{ mro::get_linear_isa($class) };
}

sub BUILDALL {
    my ($self, $arg_ref) = @_;
    foreach my $method (map { "${_}::BUILD" } reverse linearized_isa(ref $self)) {
        if ($self->can($method)) {
            $self->$method($arg_ref);
        }
    }
    return;
}

sub DEMOLISHALL {
    my ($self) = @_;
    foreach my $method (map { "${_}::DEMOLISH" } reverse linearized_isa(ref $self)) {
        if ($self->can($method)) {
            $self->$method();
        }
    }
    return;
}

sub DESTROY {
    my ($self) = @_;

    local $@ if $@;
    $self->DEMOLISHALL;
    return;
}

1;
