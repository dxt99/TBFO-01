import CYK_linebased as lineCYK

lastError=-1 #memoizes line errors
lineError="" #last error line
lines=[] #saves lines
lineNumber={}

Lang = {
        "S":[["S","S"],["E"],["S5","S6"],["S5","S7"],["S5","S8"],["S5","S3"],
             ["S11","S12"],["S13", "S14"],["C"],["S15","S16"],["S17","S"],["S18","S"],["L"]],
        # if block
        "SI":[["S5", "S6"], ["S5", "S7"], ["S5", "S8"], ["S5", "S3"]], # not necessary
        "S1":[["S10","S3"], ["S1","S1"]],
        "S2":[["S4","S3"]],
        "S3":[["I8"], ["S5", "S6"], ["S5", "S7"], ["S5", "S8"], ["S5", "S3"], ["S11", "S12"], ["S13", "S14"], ["S3","S3"], ["S15","S16"], ["S17","S"], ["S18","S"], ["L"]],
        "S4":[["I6"]],
        "S5":[["I"]],
        "S6":[["S3","S9"]],
        "S7":[["S3","S1"]],
        "S8":[["S3","S2"]],
        "S9":[["S1","S2"]],
        "S10":[["I4"]],
        # if block inside loop
        "SIL":[["S5L", "S6L"], ["S5L", "S7L"], ["S5L", "S8L"], ["S5L", "S3L"]], # not necessary
        "S1L":[["S10L","S3L"], ["S1L","S1L"]],
        "S2L":[["S4L","S3L"]],
        "S3L":[["I10"], ["S5L", "S6L"], ["S5L", "S7L"], ["S5L", "S8L"], ["S5L", "S3L"], ["S11L", "S12L"], ["S13L", "S14L"], ["S3L","S3L"], ["S15L","S16L"], ["S17L","SSL"]],
        "S4L":[["I6"]],
        "S5L":[["I"]],
        "S6L":[["S3L","S9L"]],
        "S7L":[["S3L","S1L"]],
        "S8L":[["S3L","S2L"]],
        "S9L":[["S1L","S2L"]],
        "S10L":[["I4"]],
        # while block
        "SW":[["S11","S12"]], # not necessary
        "S11":[["W"]],
        "S12":[["W4"], ["S5L", "S6L"], ["S5L", "S7L"], ["S5L", "S8L"], ["S5L", "S3L"], ["S11", "S12"], ["S13", "S14"], ["S12", "S12"], ["S15","S16"], ["S17","S"], ["S18","S"], ["L"]],
        # for block
        "SF":[["S13", "S14"]], # not necessary
        "S13":[["F"]],
        "S14":[["F7"], ["S5L", "S6L"], ["S5L", "S7L"], ["S5L", "S8L"], ["S5L", "S3L"], ["S11", "S12"], ["S13", "S14"], ["S14", "S14"], ["S15","S16"], ["S17","S"], ["S18","S"], ["L"]],
        # def block
        "SSD":[["SSD","SSD"],["E"],["S5D","S6D"],["S5D","S7D"],["S5D","S8D"],["S5D","S3D"],
             ["S11D","S12D"],["S13D", "S14D"],["C"],["S15","S16"],["S17D","SSD"],["L"]],
        "SD":[["S15","S16"]],
        "S15":[["D"]],
        "S16":[["O"], ["S5D", "S6D"], ["S5D", "S7D"], ["S5D", "S8D"], ["S5D", "S3D"], ["S11D", "S12D"], ["S13D", "S14D"], ["S16", "S16"], ["S15","S16"], ["S17D","SSD"]],
        "SID":[["S5D", "S6D"], ["S5D", "S7D"], ["S5D", "S8D"], ["S5D", "S3D"]], # not necessary
        "S1D":[["S10D","S3D"], ["S1D","S1D"]],
        "S2D":[["S4D","S3D"]],
        "S3D":[["I9"], ["S5D", "S6D"], ["S5D", "S7D"], ["S5D", "S8D"], ["S5D", "S3D"], ["S11D", "S12D"], ["S13D", "S14D"], ["S3D","S3D"], ["S15","S16"], ["S17D","SSD"]],
        "S4D":[["I6"]],
        "S5D":[["I"]],
        "S6D":[["S3D","S9D"]],
        "S7D":[["S3D","S1D"]],
        "S8D":[["S3D","S2D"]],
        "S9D":[["S1D","S2D"]],
        "S10D":[["I4"]],
        "SWD":[["S11D","S12D"]], # not necessary
        "S11D":[["W"]],
        "S12D":[["W5"], ["S5D", "S6D"], ["S5D", "S7D"], ["S5D", "S8D"], ["S5D", "S3D"], ["S11D", "S12D"], ["S13D", "S14D"], ["S12D", "S12D"], ["S15","S16"], ["S17D","SSD"]],
        "SFD":[["S13D", "S14D"]], # not necessary
        "S13D":[["F"]],
        "S14D":[["F8"], ["S5D", "S6D"], ["S5D", "S7D"], ["S5D", "S8D"], ["S5D", "S3D"], ["S11D", "S12D"], ["S13D", "S14D"], ["S14D", "S14D"], ["S15","S16"], ["S17D","SSD"]],
        "SCD":[["S17D","SSD"]],
        "S17D":[["P"]],
        # class block
        "SC":[["S17","S"]],
        "S17":[["P"]],
        #with block
        "ST":[["S18","S"]],
        "S18":[["M"]],
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
    inComment = False
    try:
        with open(filename,"r+") as foo:
            for line in foo:
                cnt+=1
                if line=="\n" or line=="":
                    continue
                temp = lineCYK.lineToList(line)
                if temp[0]=="'" and temp[1]=="'" and temp[2]=="'" and not(inComment):
                    inComment = True
                    continue
                if temp[0]=="'" and temp[1]=="'" and temp[2]=="'" and inComment:
                    inComment = False
                    continue
                if inComment:
                    continue
                if temp[0]=="#":
                    continue
                lines.append(line)
                lineNumber[line]=cnt
                if len(temp) != 0:
                    ret.append(temp)
    except FileNotFoundError:
        print("\nFile Tidak Ditemukan!\n")
        return False
    #print(ret)
    return ret