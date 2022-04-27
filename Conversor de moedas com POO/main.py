from convert_currency import ConvertCurrency

api_key = "43fde194323e71e09c7f"
conv_curr = ConvertCurrency(api_key)

Your_money = input("Digite o código da moeda a ser convertida! Ex: BRL, USD, JPY ")
Target_money = input("Digite a moeda que você quer! Ex: BRL, USD, JPY ")
Amount = input("Digite um valor! ")

if Amount.isdigit() == False:
    print('Entrada invalida, Insira um número!')
    quit()

print(conv_curr.transform_currency(Your_money, Amount, Target_money))
