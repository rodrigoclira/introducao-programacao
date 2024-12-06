def imprimi_triangulo_numerico(linhas):
    cont_imp = 1
    for linha in range(1, linhas+1):
        cont_col = 1
        while cont_col <= linha:
            print(cont_imp, end=" ")
            cont_imp+=1
            cont_col+=1
        print()


imprimi_triangulo_numerico(3)