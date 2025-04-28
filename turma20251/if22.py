idade = int(input("Informe a idade do trabalhador: "))
tempo_servico = int(input("Informe o tempo de serviço do trabalhador: "))

if idade >= 65:
    print("Aposentado pela idade")
elif tempo_servico >= 30:
    print("Aposentado pelo tempo de serviço")
elif idade >= 60 and tempo_servico >= 25:
    print("Aposentado pela idade + tempo de serviço")
else:
    print("Você não pode se aposentar pelas regras atuais")



if idade >= 65 or tempo_servico >= 30 or (idade >=60 and tempo_servico >= 25):
    
