#!/bin/bash
## small script to compare the output of two commands.  should move this to the makefile.
o1=`$1`
o2=`$2`

m1=$3
m2=$4

if [ "$o1" == "$o2" ]; then
    echo "[OKAY]" $m1
else
    echo "[FAIL]" $m2
fi
