"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    nres=[]
    i=0
    while i < len(result):
        nres.append(result[i])
        if i < len(result):
            nres.append('@')
        i+=1
    print(nres)
    return nres  