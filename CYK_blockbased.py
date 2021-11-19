import CYK_linebased as lineCYK

Lang = {
        "S":[["S","S"],["E"],["S5","S6"],["S5","S7"],["S5","S8"],["S5","S3"],["S11","S12"],["S13", "S14"]],
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
        "S14":[["F7"], ["S5", "S6"], ["S5", "S7"], ["S5", "S8"], ["S5", "S3"], ["S11", "S12"], ["S13", "S14"], ["S14", "S14"]]
        }

def blockParse(w):
    n = len(w)
      
    # Initialize the table
    U = [[set([]) for j in range(n)] for i in range(n)]
  
    # Filling in the table
    for j in range(0, n):
  
        # Find possible non terminals
        U[j][j]=lineCYK.exprParse(w[j])
        
        for lhs, rule in Lang.items():
            for rhs in rule:
                # If a terminal is found
                if len(rhs) == 1 and (rhs[0] in U[j][j]):
                    U[j][j].add(lhs)
  
        for i in range(j, -1, -1):   
               
            # Iterate over the range i to j + 1   
            for k in range(i, j):     
  
                # Iterate over the rules
                for lhs, rule in Lang.items():
                    for rhs in rule:
                          
                        # If a non-terminal is found
                        if len(rhs) == 2 and (rhs[0] in U[i][k]) and (rhs[1] in U[k+1][j]):
                            U[i][j].add(lhs)

    # If word can be formed by rules 
    # of given grammar
    return ('S' in U[0][n-1])

def readFile(filename):
    ret=[]
    with open(filename,"r+") as foo:
        for line in foo:
            ret.append(lineCYK.lineToList(line))
    return ret

s=str(input("Masukkan nama file:"))
print(blockParse(readFile(s)))