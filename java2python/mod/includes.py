def bsr(value, bits):
    """ bsr(value, bits) -> value shifted right by bits

    This function is here because an expression in the original java
    source contained the token '>>>' and/or '>>>=' (bit shift right
    and/or bit shift right assign).  In place of these, the python
    source code below contains calls to this function.

    Copyright 2003 Jeffrey Clement.  See pyrijnadel.py for license and
    original source.
    """
    minint = -2147483648
    if bits == 0:
        return value
    elif bits == 31:
        if value & minint:
            return 1
        else:
            return 0
    elif bits < 0 or bits > 31:
        raise ValueError('bad shift count')
    tmp = (value & 0x7FFFFFFE) // 2**bits
    if (value & minint):
        return (tmp | (0x40000000 // 2**(bits-1)))
    else:
        return tmp
