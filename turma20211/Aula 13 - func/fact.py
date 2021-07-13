def fatr(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fatr(num-1)

def fat(num):
    cont = num 
    res = 1
    while cont>0:
        res = cont * res
        cont-=1
    return res

res = fat(1000)
print(res)

res = fatr(1000)
print(res)
