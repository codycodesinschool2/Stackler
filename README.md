# Stackler
An esoteric language, we love stacks indeed <br/>
Following are the commands in the language: <br/>
\> Rotate right on the current stack <br/>
\< Rotate left on the current stack <br/>
w Move one stack up <br/>
s Move one stack down <br/>
\+ add the two top numbers on the current stack <br/>
\- subtract the top two numbers on the current stack (reverse polish style) <br/>
\* multiply the two top numbers on the current stack <br/>
/ divide the two top numbers on the current stack (again reverse polish) <br/>
\{ Jump to matching } if top stack is empty <br/>
\} Jump to matching { if top stack is not empty <br/>
[ Jump to matching ] if number on current stack is 0 <br/>
] Jump to matching [ if number on current stack is not 0 <br/>
o Push a zero to the current stack <br/>
p add one to the value of the selected value on the current stack <br/>
l subtract one from the value of the selected value on the current stack <br/>
k push new empty stack onto stack-list <br/>
v print current stack as numbers <br/>
b print current stack as letters <br/>
f print current stack top value as number <br/>
g print current stack top value as letter <br/>
d discard the top value of the current stack <br/>
a discord the top stack <br/>
everything else is interpreted as a comment
