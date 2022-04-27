from functions import *

print("Qual a data de vencimento?\n")
print("Formato: Dia-Mes-Ano\n")

due_date = input("")

if len(due_date) ==10:
    print(verify_due(due_date))
else:
    print ("entrada inválida")

