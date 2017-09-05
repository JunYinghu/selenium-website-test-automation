def  oddNumbers(l, r):
    arr = range (l,r+1)
    out = []
    for i in arr:
        if (i % 2) == 1:
            out.append(i)
    return out

def reverse_each_word(sentence):
    out = ''
    arr = [] 
    for c in sentence:
        valid = c.isalnum()
        empty = len(arr) == 0
        if empty and valid:
            arr.append(c)
        elif (not empty) and valid:
            arr.append(c)
        elif (not empty) and (not valid):
            arr.reverse()
            out += ''.join (arr)
            out += c
            arr = []
        else:
            out += c
    
    if len(arr)>0:
        arr.reverse()
        out += ''.join (arr)
        
    return out