
def arrayManipulation(n, queries):
    L=[0]*n
    for qr in queries:
        L[qr[0]-1]+= qr[2]
        if qr[1]!=n:
            L[qr[1]]-=qr[2]
    temp=0
    max_value=0
    for i in L:
        temp+=i
        if temp>max_value:
            max_value= temp
    return max_value
