#!/bin/bash
## small script to compare the output of two commands.  should move this to the makefile.
o1=`$1`
r1=$?

o2=`$2`
r2=$?

let "e = $r2 | $r1"

if [[ "$o1" == "$o2" && $e == 0 ]]
then
    echo "[OKAY]" $3
else
    echo "[FAIL]" $3
fi
