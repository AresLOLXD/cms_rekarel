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

Next, let's install the interpreter.

Download https://github.com/kishtarn555/rekarel-cpp-interpreter

Go to the download/clone folder and run:

Then 
```
mkdir bin
make karel
cd bin
sudo install -m 755 karel /usr/local/bin
```

## Karel for CMS

Run 

`python3 setup.py install`

Restart CMS


# Usage

This package adds two things
* Karel languages
* Karel task type.

A Karel task type is a slightly modified version of a [batch](https://cms.readthedocs.io/en/latest/Task%20types.html#batch) task that changes the task output the correct information, like Instruction Limit Exceeded and the type or Runtime Error


