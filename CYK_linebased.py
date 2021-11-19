# Reserved Words
reserved=["for","True","False","in","and","or","is","Not","raise","while","pass","break","continue", "if", "elif", "else"]

# Terminals
uppercase=[[chr(ord('A')+i)] for i in range(26)]
lowercase=[[chr(ord('a')+i)] for i in range(26)]
integer=[[chr(ord('0')+i)] for i in range(10)]
nonzero=[[chr(ord('1')+i)] for i in range(9)]
binary=[["+"],["-"],["*"],["/"],["%"]]
boolop=[["and"],["or"],["is"],["in"],["<"],[">"]]
unary=[["Not"],["+"],["-"],["~"]]
boolean=[["True"],["False"],["None"]]

# Rules of the grammar
Rules = {
     "V": [["V1","V2"]]+uppercase+lowercase+[['_']],
     "V1":uppercase+lowercase+[['_']],
     "V2":[["V2","V2"]]+uppercase+lowercase+integer+[['_']],
     "V3":[["V4","V5"]]+nonzero,
     "V4":nonzero,
     "V5":integer,
     "V6":[["V3","V7"]],
     "V7":[["V8","V5"]],
     "V8":[["."]],
     "V9":[["V10","V11"]],
     "V10":[['"']],
     "V11":[["V12","V10"],['"']],
     "V12":[["V12","V12"],["|"]],
     "V13":[["V14","V15"]],
     "V14":[["'"]],
     "V15":[["V12","V14"],["'"]],
     "E":[["E1","E2"],["E37","E38"],["V","E19"]],
     "E1": [["E1", "E1"],["V","E3"]],
     "E3":[["="]],
     "E2":[["E2","E4"],["E6","E7"],["E9","E10"],["E9","E13"],["E18","E2"],
           ["V","E19"],["E6","E20"],["E23","E24"],["E23","E28"],["V1","V2"],
           ["E31","E2"],["V10","V11"],["V14","V15"],["V4","V5"],["V3","V7"]]
             +boolean+uppercase+lowercase+integer+[["_"]],
     "E4":[["E5","E2"]],
     "E5":binary+boolop,
     "E6":[["("]],
     "E7":[["E2","E8"]],
     "E8":[[")"]],
     "E9":[["["]],
     "E10":[["E2","E11"],["]"]],
     "E11":[["E12","E25"],["]"]],
     "E12":[[","]],
     "E25":[["E2","E11"],["]"]],
     "E13":[["V","E14"]],
     "E14":[["EF","E15"]],
     "EF":[["for"]],
     "E15":[["V","E16"]],
     "E16":[["E17","E35"]],
     "E35":[["E2","E36"]],
     "E36":[["]"]],
     "E17":[["in"]],
     "E18":unary,
     "E19":[["E6","E20"]],
     "E20":[["E2","E21"],[")"]],
     "E21":[["E12","E22"],[")"]],
     "E22":[["E2","E21"],[")"]],
     "E23":[["{"]],
     "E24":[["E2","E26"],["}"]],
     "E26":[["E12","E27"],["}"]],
     "E27":[["E2","E26"],["}"]],
     "E28":[["E2","E29"],["}"]],
     "E29":[["E12","E30"],["}"]],
     "E30":[["E2","E29"],["}"]],
     "E31":[["E2","E32"]],
     "E32":[["E33","E33"],["E34","E3"]],
     "E33":[["*"],["="],["/"]],
     "E34":[[">"],["<"]],
     "E37":[["V","E39"]],
     "E38":[["E3","E2"]],
     "E39":binary,
     "R":[["R1","R2"]],
     "R1":[["raise"]],
     "R2":[["V","E19"]],
     # while loop
     "W":[["W1", "W2"]],
     "W1":[["while"]],
     "W2":[["E2", "W3"]],
     "W3":[[":"]],
     "W4":[["E1","E2"], ["E37","E38"], ["V","E19"], ["pass"], ["break"], ["continue"]],
     # for loop
     "F":[["F1", "F2"]],
     "F1":[["for"]],
     "F2":[["V","F3"]],
     "F3":[["F4","F5"]],
     "F4":[["in"]],
     "F5":[["E2", "F6"]],
     "F6":[[":"]],
     "F7":[["E1","E2"], ["E37","E38"], ["V","E19"], ["pass"], ["break"], ["continue"]],
     # if
     "I":[["I1", "I2"]],
     "I1":[["if"]],
     "I2":[["E2", "I3"]],
     "I3":[[":"]],
     "I4":[["I5", "I2"]],
     "I5":[["elif"]],
     "I6":[["I7", "I3"]],
     "I7":[["else"]],
     "I8":[["E1","E2"], ["E37","E38"], ["V","E19"], ["pass"]],
     #"I8":[["I1", "I9"], ["if"]], # count
     #"I9":[["I5", "I9"], ["elif"], ["else"]]
    }
  
# Parses expression/literal/variable (must be in one line)
# Start symbols 
# S = "E" -> expression
# S = "V" -> variable
# S = "E2" -> literal
# S = "R" -> raise
def exprParse(w):
    n = len(w)
      
    # Initialize the table
    T = [[set([]) for j in range(n)] for i in range(n)]
  
    # Filling in the table
    for j in range(0, n):
  
        # Iterate over the rules
        for lhs, rule in Rules.items():
            for rhs in rule:
                # If a terminal is found
                if len(rhs) == 1 and (rhs[0] == w[j] or rhs[0]=='|'):
                    T[j][j].add(lhs)
  
        for i in range(j, -1, -1):   
               
            # Iterate over the range i to j + 1   
            for k in range(i, j):     
  
                # Iterate over the rules
                for lhs, rule in Rules.items():
                    for rhs in rule:
                          
                        # If a terminal is found
                        if len(rhs) == 2 and (rhs[0] in T[i][k]) and (rhs[1] in T[k+1][j]):
                            T[i][j].add(lhs)
  
    # If word can be formed by rules 
    # of given grammar
    return (T[0][n-1])

def lineToList(s):
    l=[]
    temp=""
    # space and reserved words handling
    for c in s:
        if temp in reserved:
            l.append(temp)
            temp=""
        if c==' ' or c=='\n':
            l+=list(temp)
            temp=""
        else:
            temp+=c
    if temp in reserved and len(temp)!=0:
        l.append(temp)
    elif not(temp in reserved) and len(temp)!=0:
        l+=temp
    return l
  
# Tests without lineToList
'''
v = "x = z".split()
w = "x = y = z = ( ( 5 * 2 ) + 3 )".split()
l = list("zy=x=1+2+(3*4)+range(1,3,)")
print(exprParse(l,"E"))
'''
'''
# Tests with lineToList
foo = open("foo.txt", "r+")
line = foo.readline()
print(lineToList(line))
print("E" in exprParse(lineToList(line)))
foo.close()
'''