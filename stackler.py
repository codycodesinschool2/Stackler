import sys
STACK = []
code = ""
codePtr = 0
stackPtr = 0
try:
    f = open(sys.argv[1],"r")
    code = f.read()
except IndexError:
    print("A file is required")
def runCommand(com):
    if com == ">":
        STACK[stackPtr].insert(0,STACK[stackPtr].pop())
    if com == "<":
        STACK[stackPtr].append(STACK[stackPtr].pop(0))
    if com == "w":
        stackPtr+=1
    if com == "s":
        stackPtr-=1
    if com == "+":
        STACK[stackPtr].append(STACK[stackPtr].pop()+STACK[stackPtr].pop())
    if com == "-":
        STACK[stackPtr].append(STACK[stackPtr].pop()-STACK[stackPtr].pop())
    if com == "*":
        STACK[stackPtr].append(STACK[stackPtr].pop()*STACK[stackPtr].pop())
    if com == "/":
        STACK[stackPtr].append(STACK[stackPtr].pop()/STACK[stackPtr].pop())
    if com == "{":
        if len(STACK[-1]) != 0: return
        counter = 1
        found = -1
        for i in range(codePtr+1,len(code)-1,1):
            if code[i] == "}":
                counter -= 1
            elif code[i] == "{":
                counter += 1
            if counter == 0:
                found = i
                break
        if found>=0:
            codePtr = found
        else:
            print("CURLY BRACKET MISMATCH ERROR")
            exit()
    if com == "}":
        if len(STACK[-1]) == 0: return
        counter = -1
        found = -1
        for i in range(codePtr+1,len(code)-1,1):
            if code[i] == "}":
                counter -= 1
            elif code[i] == "{":
                counter += 1
            if counter == 0:
                found = i
                break
        if found>=0:
            codePtr = found
        else:
            print("CURLY BRACKET MISMATCH ERROR")
            exit()
    if com == "[":
        if STACK[stackPtr] != 0: return
        counter = 1
        found = -1
        for i in range(codePtr+1,len(code)-1,1):
            if code[i] == "]":
                counter -= 1
            elif code[i] == "[":
                counter += 1
            if counter == 0:
                found = i
                break
        if found>=0:
            codePtr = found
        else:
            print("SQUARE BRACKET MISMATCH ERROR")
            exit()
    if com == "]":
        if STACK[stackPtr] == 0: return
        counter = -1
        found = -1
        for i in range(codePtr+1,len(code)-1,1):
            if code[i] == "]":
                counter -= 1
            elif code[i] == "[":
                counter += 1
            if counter == 0:
                found = i
                break
        if found>=0:
            codePtr = found
        else:
            print("SQUARE BRACKET MISMATCH ERROR")
            exit()
    if com == "o":
        STACK[stackPtr].append(0)
    if com == "p":
        STACK[stackPtr] += 1
    if com == "l":
        STACK[stackPtr] -= 1
    if com == "k":
        STACK.append([])
    if com == "v":
        for v in STACK[stackPtr]:
            print(v,end=" ")
    if com == "b":
        for v in STACK[stackPtr]:
            print(chr(v),end="")
    if com == "f":
        print(STACK[stackPtr][-1])
    if com == "g":
        print(chr(STACK[stackPtr][-1]))
    if com == "d":
        STACK[stackPtr].pop()
    if com == "a":
        STACK.pop()
while True:
    if(codePtr >= len(code)):
        exit()
    runCommand(code[codePtr])
    codePtr+=1