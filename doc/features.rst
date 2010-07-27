.. _features:

********************
Translation Features
********************

The |j2py| package can translate any syntactically valid Java source
code file.  The generated Python code is not guaranteed to run, nor is
guaranteed to be valid syntatically valid Python.  However, |j2py|
works well many cases, and in some of those, it creates perfectly
usable and workable Python code.

The remainder of this chapter describes how Java language features are
translated into Python constructs.


General Approach
================

The approach taken by |j2py| is to favor readability over correctness
for two reasons: first, it is quite rare that Java source code will
work correctly without modification because of semantic and run-time
differences, and second, |j2py| is meant to aid in one-time and
ongoing translation projects.


What Works Well (Unless You Try Really Hard to Break It)
========================================================


What Works Mostly (Or Sometimes if You're Lucky)
================================================


What Works Barely (Or Not at All)
=================================


A (Mostly) Complete List
=========================

