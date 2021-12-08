# N! = N * (N-1)!
# 1! = 1
# 0! = 1

#5! = 5 * 4!
#4! = 4 * 3!
#3! = 3 * 2!
#2! = 2 * 1!
#1! = 1
## 5 * 4 * 3 * 2 * 1 == 120
def fact(num):
    mult=1
    for i in range (num, 1, -1):
        mult = mult*i 
    return mult

def fact_recursivo(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact_recursivo(num-1)

if __name__ == '__main__':
    cont = 1
    while cont <= 10:
        print (f"O fatorial de {cont} é {fact(cont)}")   
        cont+=1

    print(fact(200))
