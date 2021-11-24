import FA
# Reserved Words
reserved=["for","True","False","in","and","or","is","Not","raise","while",
          "pass","break","continue", "if", "elif", "else","import","from",
          "as","return","class","def", "with"]

# Special Characters (ignored in lineToList)
special=["\n"," ","\r","\t"]

# Terminals
uppercase=[[chr(ord('A')+i)] for i in range(26)]
lowercase=[[chr(ord('a')+i)] for i in range(26)]
integer=[[chr(ord('0')+i)] for i in range(10)]
nonzero=[[chr(ord('1')+i)] for i in range(9)]
binary=[["+"],["-"],["*"],["/"],["%"],["|"],["^"],["&"]]
boolop=[["and"],["or"],["is"],["in"],["<"],[">"]]
unary=[["Not"],["+"],["-"],["~"]]
boolean=[["True"],["False"],["None"]]

# Rules of the grammar
Rules = {
     "V": [["V1","V2"],["V","V17"]]+uppercase+lowercase+[['_']],
     "V1":uppercase+lowercase+[['_']],
     "V2":[["V2","V2"]]+uppercase+lowercase+integer+[['_']],
     "V3":[["V4","V5"]]+integer,
     "V4":nonzero,
     "V5":integer+[["V5","V5"]],
     "V6":[["V3","V7"]],
     "V7":[["V8","V5"]],
     "V8":[["."]],
     "V9":[["V10","V11"]],
     "V10":[['"']],
     "V11":[["V12","V10"],['"']],
     "V12":[["V12","V12"],["$"]],
     "V13":[["V14","V15"]],
     "V14":[["'"]],
     "V15":[["V12","V14"],["'"]],
     "V16":[["V2","V17"],["E9","V18"]],
     "V17":[["E9","V18"],["V17","V17"]],
     "V18":[["E2","E36"]],
     "E":[["E1","E2"],["E37","E38"],["V","E19"],["E40","E38"],["E","C"],["E44","E45"]],
     "E1": [["E1", "E1"],["V","E3"]],
     "E3":[["="]],
     "E2":[["E2","E4"],["E6","E7"],["E9","E10"],["E9","E13"],["E18","E2"],
           ["V","E19"],["E6","E20"],["E23","E24"],["E23","E28"],["V1","V2"],
           ["E31","E2"],["V10","V11"],["V14","V15"],["V4","V5"],["V3","V7"],
           ["V","V17"],["E44","E45"]]+boolean+uppercase+lowercase+integer+[["_"]],
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
     "E13":[["E2","E14"]],
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
     "E33":[["*"],["="],["/"],["<"],[">"]],
     "E34":[[">"],["<"],["!"]],
     "E37":[["V","E39"]],
     "E38":[["E3","E2"]],
     "E39":binary,
     "E40":[["V","E41"]],
     "E41":[["E42","E42"]],
     "E42":[["*"],["/"],["<"],[">"]],
     "E43":[["E44","E45"]],
     "E44":[["E44","E44"],["V","E46"]],
     "E45":[["V1","V2"],["V","V17"]]+uppercase+lowercase+[['_']]+[["V","E19"]],
     "E46":[["."]],
     
     "R":[["R1","R2"]],
     "R1":[["raise"]],
     "R2":[["V","E19"]],
     # while loop
     "W":[["W1", "W2"],["W","C"]],
     "W1":[["while"]],
     "W2":[["E2", "W3"]],
     "W3":[[":"]],
     "W4":[["E1","E2"], ["E37","E38"], ["V","E19"], ["pass"], ["break"], ["continue"], ["W4","C"]],
     "W5":[["E1","E2"], ["E37","E38"], ["V","E19"], ["pass"], ["break"], ["continue"], ["W5","C"], ["return"],["O1", "E2"]],
     # for loop
     "F":[["F1", "F2"],["F","C"]],
     "F1":[["for"]],
     "F2":[["V","F3"]],
     "F3":[["F4","F5"]],
     "F4":[["in"]],
     "F5":[["E2", "F6"]],
     "F6":[[":"]],
     "F7":[["E1","E2"], ["E37","E38"], ["V","E19"], ["pass"], ["break"], ["continue"], ["F7","C"]],
     "F8":[["E1","E2"], ["E37","E38"], ["V","E19"], ["pass"], ["break"], ["continue"], ["F8","C"], ["return"],["O1", "E2"]],
     # if
     "I":[["I1", "I2"],["I","C"]],
     "I1":[["if"]],
     "I2":[["E2", "I3"]],
     "I3":[[":"]],
     "I4":[["I5", "I2"],["I4","C"]],
     "I5":[["elif"]],
     "I6":[["I7", "I3"],["I6","C"]],
     "I7":[["else"]],
     "I8":[["E1","E2"], ["E37","E38"], ["V","E19"], ["pass"], ["I8","C"]],
     "I9":[["E1","E2"], ["E37","E38"], ["V","E19"], ["pass"], ["I9","C"], ["return"],["O1", "E2"]],
     "I10":[["E1","E2"], ["E37","E38"], ["V","E19"], ["pass"], ["break"], ["continue"], ["I8","C"]],
     #with
     "M":[["M1", "M2"],["M","C"]],
     "M1":[["with"]],
     "M2":[["M3", "M4"]],
     "M3":[["V", "E19"],["V","E43"]],
     "M4":[["M5", "M6"]],
     "M5":[["as"]],
     "M6":[["V", "M7"]],
     "M7":[[":"]],
     #import
     "L":[["L1","L2"],["L3","L4"],["LI","V"]],
     "L1":[["LF","V"]],
     "LF":[["from"]],
     "L2":[["L3"],["L3","L4"]],
     "L3":[["LI","V"]],
     "LI":[["import"]],
     "L4":[["LA","V"]],
     "LA":[["as"]],
     #from
     #def
     "D":[["D1", "D2"]],
     "D1":[["def"]],
     "D2":[["D3", "D4"]],
     "D3":[["V1","V2"],["V1","V16"]]+uppercase+lowercase+[['_']],
     "D4":[["D5", "D6"]],
     "D5":[["("]],
     "D6":[["D8", "D7"]],
     "D7":[["D11", "D12"]],
     "D8":[[""], ["V","D9"]]+[["V1","V2"],["V1","V16"]]+uppercase+lowercase+[['_']],
     "D9":[["D10", "D8"]],
     "D10":[[","]],
     "D11":[[")"]],
     "D12":[[":"]],
     #return
     "O":[["return"],["O1", "E2"],["O","C"]],
     "O1":[["return"]],
     #class
     "P":[["P1", "P2"],["P","C"]],
     "P1":[["class"]],
     "P2":[["P3", "P4"]],
     "P3":[["V1","V2"],["V1","V16"]]+uppercase+lowercase+[['_']],
     "P4":[[":"]],
     #comments
     "C":[["C1","C2"]],
     "C1":[["#"]],
     "C2":[["C2","C2"],["$"]]
    }

def exprParse(line):
    # Bottom-Up DP
    n=len(line)
    # Initialize the dp table
    dp = [[set([]) for j in range(n)] for i in range(n)]
    
    for j in range(n):
        # Fill base cases
        FA.contFA(line[j])
        for l, lang in Rules.items():
            for r in lang:
                # Only adds to table if terminal
                if len(r)==1 and (r[0]==line[j] or r[0]=='$'):
                    dp[j][j].add(l) # Variable Accepted
                    # Check FA
                    if FA.stat():
                        dp[j][j].add('V')
        
        # DP Transitions
        for i in range(j,-1,-1):
            # Scan downwards
            for k in range(i,j):
                # Check if variable is accepted
                for l, lang in Rules.items():
                    for r in lang:
                        if len(r)==2 and (r[0] in dp[i][k]) and (r[1] in dp[k+1][j]):
                            dp[i][j].add(l)
    # Returns all starting points possible
    return dp[0][n-1]

def lineToList(s):
    l=[]
    temp=""
    # space and reserved words handling
    for c in s:
        if temp in reserved:
            l.append(temp)
            temp=""
        if c in special:
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

# Tests with lineToList

'''foo = open("tests\inputAcc.py", "r+")
line = foo.readline()
print(lineToList(line))
print("D" in exprParse(lineToList(line)))
foo.close()'''
