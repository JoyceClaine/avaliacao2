def menor(a,b):
    if a < b:
        return a
    else:
        return b


def troca(s, velho ,novo):
    ps = 0
    pv = 0
    for i in s:
        if i== velho:
            print(novo) 
        elif i== velho[pv] and velho[pv+1] == s[ps+1]:
            print(novo)            
        else:
            print(i)
        ps +=1
     
