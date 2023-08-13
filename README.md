# Stackler
An esoteric language, we love stacks indeed
Following are the commands in the language:
> Rotate right on the current stack
< Rotate left on the current stack
w Move one stack up
s Move one stack down
+ add the two top numbers on the current stack
- subtract the top two numbers on the current stack (reverse polish style)
* multiply the two top numbers on the current stack
/ divide the two top numbers on the current stack (again reverse polish)
{ Jump to matching } if top stack is empty
} Jump to matching { if top stack is not empty
\[ Jump to matching ] if number on current stack is 0
] Jump to matching [ if number on current stack is not 0
o Push a zero to the current stack
p add one to the value of the selected value on the current stack
l subtract one from the value of the selected value on the current stack
k push new empty stack onto stack-list
v print current stack as numbers
b print current stack as letters
f print current stack top value as number
g print current stack top value as letter
d discard the top value of the current stack
a discord the top stack
everything else is interpreted as a comment
