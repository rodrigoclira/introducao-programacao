salario_antigo = float(input("Informe o salário: "))
tempo_servico = int(input("Informe o tempo de serviço: "))

if salario_antigo <= 500:
    perc = 0.25
elif salario_antigo <= 1000:
    perc = 0.20
elif salario_antigo <= 1500:
    perc = 0.15
elif salario_antigo <= 2000:
    perc = 0.1
else:
    perc = 0

if tempo_servico > 10:
    bonus = 500
elif tempo_servico >= 7:
    bonus = 300
elif tempo_servico >= 4:
    bonus = 200
elif tempo_servico >= 1:
    bonus = 100
else:
    bonus = 0

salario_novo = (1 + perc) * salario_antigo + bonus

print(f"O novo salário é R$ {salario_novo:.2f}")
