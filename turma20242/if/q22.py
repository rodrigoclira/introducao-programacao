tempo_servico = int(input("Informe a idade de serviço: "))
idade_trabalhador = int(input("Informe a idade do trabalhador: "))

if idade_trabalhador >= 65:
    print("Você pode se aposentar pela sua idade!")
elif tempo_servico >= 30:
    print("Você pode se aposentar pela idade de serviço!")
elif idade_trabalhador >= 60 and tempo_servico >= 25:
    print("Voc6e pode se aposentar devido a sua idade e tempo de serviço")
else:
    print("Você não pode se aposentar.")


# if (idade_trabalhador >= 65) or (tempo_servico >= 30) or (idade_trabalhador >= 60 and tempo_servico >= 25):
#     print("Você consegue se aposentar")
# else:
#     print("Você não pode se aposentar.")
