horas = int(input("Digite a quantidade de horas: "))
dias = horas // 24
horas_restantes = horas % 24
print(f"{dias} dia(s) e {horas_restantes} hora(s)")