#7-7
from os.path import isfile as isfile
from time import time as time

Result = []
AllLines = []
FileName = r'FindLongesReuse.py'
def PreOperate():
    global AllLines
    with open (FileName,'r') as fp:
        for line in fp:
            line = ' '.join(line.split())
            if line !='':
                AllLines.append(line)

def IfHasDuplicated(Index1):
    for item in Result.values():
        for it in item:
            if Index1 == it[0]:
                return it[1]
    return False

def IsInSpan(Index2):
    for item in Result.values():
        for i in item:
            if i[0]<=Index2<i[0]+i[1]:
                return True
    return False

def MainCheck():
    global Result
    TotalLen = len(AllLines)
    Index1=0
    while Index1< TotalLen-1:
        span=IfHasDuplicated(Index1)
        if span:
            Index1+=span
            continue
        Index2 = Index1+1
        while Index2<TotalLen:
            if IsInSpan(Index2):
                 Index2+=1
                 continue
            scr = ''
            des = ''
            for i in range(10):
                if Index2+i>=TotalLen:
                    break
                scr+=AllLines[Index1+i]
                des+=AllLines[Index2+i]
                if scr == des:
                    t = Result.get(Index1, [])
                    for tt in t:
                        if tt[0] == Index2:
                            tt[1] = i + 1
                            break
                    else:
                        t.append([Index2, i + 1])
                    Result[Index1] = t
                else:
                    break
            t = Result.get(Index1,[])
            for tt in t:
                if tt[0]==Index2:
                    Index2+=tt[1]
                    break
            else:
                Index2+=1
        Result[Index1]=Result.get(Index1,[])
        for n in Result[Index1][::-1]:
            if n[1]<3:
                Result[Index1].remove(n)
        if not Result[Index1]:
            del Result[Index1]

def Output():
    print('-'*20)
    print('-'*20)
    print("Result:")
    for key,value in Result.items():
        print('The original line is: \n {0}'.format(AllLines[key]))
        print("Its line number is {0}".format((key)))
        print('The duplicated line number are:')
        for i in value:
            print('    start:',i[0],'     span:',i[1])
        print('-'*20)
    print('-'*20)

if isfile(FileName):
    start = time()
    PreOperate()
    MainCheck()
    Output()
    print('Time used:',time()-start)