import CYK_linebased as lineCYK

lastError=-1 #memoizes line errors
lineError="" #last error line
lines=[] #saves lines
lineNumber={}

Lang = {
        "S":[["S","S"],["E"],["S5","S6"],["S5","S7"],["S5","S8"],["S5","S3"],
             ["S11","S12"],["S13", "S14"],["C"],["S15","S"],["O"],["S16","S"],["L"],["M"]],
        # if block
        "SI":[["S5", "S6"], ["S5", "S7"], ["S5", "S8"], ["S5", "S3"]], # not necessary
        "S1":[["S10","S3"], ["S1","S1"]],
        "S2":[["S4","S3"]],
        "S3":[["I8"], ["S5", "S6"], ["S5", "S7"], ["S5", "S8"], ["S5", "S3"], ["S11", "S12"], ["S13", "S14"], ["S3","S3"]],
        "S4":[["I6"]],
        "S5":[["I"]],
        "S6":[["S3","S9"]],
        "S7":[["S3","S1"]],
        "S8":[["S3","S2"]],
        "S9":[["S1","S2"]],
        "S10":[["I4"]],
        # while block
        "SW":[["S11","S12"]], # not necessary
        "S11":[["W"]],
        "S12":[["W4"], ["S5", "S6"], ["S5", "S7"], ["S5", "S8"], ["S5", "S3"], ["S11", "S12"], ["S13", "S14"], ["S12", "S12"]],
        # for block
        "SF":[["S13", "S14"]], # not necessary
        "S13":[["F"]],
        "S14":[["F7"], ["S5", "S6"], ["S5", "S7"], ["S5", "S8"], ["S5", "S3"], ["S11", "S12"], ["S13", "S14"], ["S14", "S14"]],
        # def block
        "SD":[["S15","S"]],
        "S15":[["D"]],
        # class block
        "SC":[["S16","S"]],
        "S16":[["P"]]
        }

def blockParse(w):
    global lastError
    global lineError
    n = len(w)
    # Initialize the dp table
    dp = [[set([]) for j in range(n)] for i in range(n)]
    
    for j in range(0, n):
        # Parse line
        #print(w[j])
        temp=lineCYK.exprParse(w[j])
        #print(temp)
        
        for l, rule in Lang.items():
            for r in rule:
                # Base cases
                if len(r) == 1 and (r[0] in temp):
                    dp[j][j].add(l)
        # DP Transitions
        for i in range(j, -1, -1):   
            for k in range(i, j):     
                for l, rule in Lang.items():
                    for r in rule:
                        if len(r) == 2 and (r[0] in dp[i][k]) and (r[1] in dp[k+1][j]):
                            dp[i][j].add(l)
        if (len(dp[j][j])==0):
            lineError=lines[j]
            lastError=j
            return False
        if (lastError==-1) and (not ('S' in dp[0][j])):
            lineError=lines[j]
            lastError=j
        if ('S' in dp[0][j]):
            lineError=""
            lastError=-1

    # If word can be formed by rules 
    # of given grammar
    #print(dp[0][n-1])
    return ('S' in dp[0][n-1])

def readFile(filename):
    global lineNumber
    ret=[]
    cnt=0
    with open(filename,"r+") as foo:
        for line in foo:
            cnt+=1
            if line=="\n" or line=="":
                continue
            lines.append(line)
            lineNumber[line]=cnt
            temp = lineCYK.lineToList(line)
            if len(temp) != 0:
                ret.append(temp)
    return ret

s=str(input("Masukkan nama file: "))
if (blockParse(readFile(s))):
    print("Compile Success!")
else:
    print(f"Error in line {lineNumber[lineError]}!")
    print(f"Error in : {(lineError)}")