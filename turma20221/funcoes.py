def maior(num1, num2):
    if num1 > num2:
        res = num1
        #return num1
    elif num2 >= num1:
        res = num2
        #return num2
    print(res)

def maior2(num1, num2):
    return max([num1, num2])

def area_triangulo(base, altura):
    area = (base * altura)/2
    return area

def mydivmod(dividendo, divisor):
    resto = dividendo % divisor
    divisao = dividendo // divisor    
    return divisao, resto

def indices(lista, valor):
    res = []
    for pos, item in enumerate(lista):
        if item == valor:
            res.append(pos)
    return res

def fatorial(num=3):
    fat = 1
    #cont = 1
    #while cont <= num:
    #    fat *= cont
    #    cont+=1    
    for cont in range(1, num+1):
        fat *= cont
    
    return fat

### MAIN ###

maior(10, 10)
resultado = area_triangulo(4, 4)
print(resultado)

print(mydivmod(10, 2))
print(fatorial())