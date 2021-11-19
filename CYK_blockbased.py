import CYK_linebased as lineCYK

Lang = {
        "S":[["S","E"],["E"]] #expression
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
        countif = []
        nret = len(ret)
        for i in range(nret):
            if ret[i][0] == 'if' :
                if len(countif)==0:
                    countif.append("if")
                else:
                    ret.append(countif)
                    countif = []
                    countif.append("if")
            elif ret[i][0] == "elif" :
                countif.append("elif")
            elif ret[i][0] == "else":
                countif.append("else")
            if (i == nret - 1) and (len(countif)!=0):
                ret.append(countif)
    return ret

s=str(input("Masukkan nama file:"))
#print(blockParse(readFile(s)))
print(readFile(s))