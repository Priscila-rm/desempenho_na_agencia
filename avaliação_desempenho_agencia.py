nome_do_agente = input(" qual é o seu nome? ")
nota_final = float(input(" qual sua nota final? "))

if 9.0 < nota_final > 10.0:
    print("Excelente 🏅")
elif 7.0 < nota_final > 8.9:
    print("Bom 👍")
elif 5.0 < nota_final > 6.9:
    print("Regular ⚠️")
elif 3.0 < nota_final > 4.9:
    print("Ruim 🚫")
elif 0.0 < nota_final > 2.9:
    print("Crítico 🚨")
else:
    print("Nota inválida ❌")

print(f'Agente {nome_do_agente}, sua classificação é: (nota: {nota_final})')