uppercase=[[chr(ord('A')+i)] for i in range(26)]
lowercase=[[chr(ord('a')+i)] for i in range(26)]
integer=[[chr(ord('0')+i)] for i in range(10)]
S=uppercase+lowercase+["_"]
F=S+integer

curState=0

def FA(w):
    state=0
    for c in w:
        if state==0 and (c in S):
            state=1
        elif state==1 and (c in F):
            state=1
        else:
            state=2
    if state==1:
        return True
    else:
        return False

def contFA(c):
    global curState
    if curState==0 and (c in S):
        curState=1
    elif curState==1 and (c in F):
        curState=1
    else:
        curState=0

def stat():
    if curState==1:
        return True
    else:
        return False