# CMS support for Karel

This adds support for Karel Java and Karel Pascal as used by the [Mexican Olimpiad in Informatics](https://www.olimpiadadeinformatica.org.mx/OMI/OMI/Inicio.aspx)


# Install

## Prerequisites


First install the compiler (Node must be at least 1.10.2)

`npm install -g @rekarel/cli`


Make sure it is in the correct place by running

`rekarel -V`

And

`type -a rekarel` 

It should be in `/usr/local/bin/rekarel`, otherwise, you'll have to move it.

## Karel for CMS

Run 

`python3 setup.py install`

Restart CMS


# Usage

This package adds two things
* Karel languages
* Karel task type.

A Karel task type it's a slightly modified version of a (batch)[https://cms.readthedocs.io/en/latest/Task%20types.html#batch] task that changes the task output so Instruction Limit Exceeded and RTE are correctly displayed. 



