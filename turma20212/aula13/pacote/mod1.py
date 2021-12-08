
def func_z():
    return (10**2, 10**3)

y = 'variavel y do mod1'

print(__name__)

if __name__ == '__main__':
    ##Teste do módulo
    print("Testando o mod1")
    retorno_func = func_z()
    print(retorno_func)