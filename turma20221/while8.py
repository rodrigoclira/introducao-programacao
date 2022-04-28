# 1
# 2 2
# 3 3 3
# 4 4 4 4

fim = int(input("Última linha: "))
cont_l = 1
num = 1
while cont_l<=fim:
    cont_c = 1
    while cont_c <= cont_l:
        print(f"{num:02d}",end=" ")
        num+=1
        cont_c+=1
    print("")
    cont_l+=1
#while cont_l<=fim:
#    print(f"{cont_l} " * cont_l)
#    cont_l+=1
    