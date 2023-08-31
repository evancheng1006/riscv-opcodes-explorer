# Intro
Explore unused Risc V space using this tool.

Data taken from https://github.com/riscv/riscv-opcodes/

Running __make__ command under the root folder of the riscv-opcodes repo generates _instr_dict.yaml_

This repo uses the data from _instr_dict.yaml_

# Definition
## Type
### __binary string__
    A string containing only {0,1}
### __instruction__
    A string containing only {0,1,-}
### __search string__
    A string containing only {0,1,-,*}
### __dictionary__
    A collection (set) of instructions
### _α-substitution_ of a string
    For every occurrence of character 'α' in a string, substitute with 0 or 1.
    For example, all possible '-'substitutions of string "0-1-" are  "0010", "0011", "0110", "0111"

## Relation
### __instruction__ I _includes_ __binary string__ B
    If only if there is a "-"substitution of I that is same as "B".

### __search string__ S _derives_ __instruction__ I
    If only if there is a "*"substitution of S that is same as "I".

### __instruction__ I _conflicts with_ __instruction__ J
    If only if there is a binary_str "B" such that I "includes" B and J "includes" B 

### __instruction__ I _conflicts with_ __dictionary__ D
    If only if there is a instruction J in dictionary D such that I "conflicts with" J

## Searches
This program contains _no-conflict-search_ and _showing-first-conflicts_.
### no-conflict-search (S,D)
    Given a search_str S, find all instructions {I1, I2,...} derived by S such that
    I does not conflict with D 

### showing-first-conflicts (S,D)
    Given a search_str S, for all instructions {I1, I2,...} derived by S,
    if I conflicts with D,
    print an instruction J in dictionary D, I coonflicts with instruction J

### showing-all-conflicts (S,D)
    Given a search_str S, for all instructions {I1, I2,...} derived by S,
    print every instruction J in dictionary D such that I coonflicts with instruction J
The _showing-all-conflicts_ search algorithm is omitted because it has too much output.



