from currency_converter import brl_to

print("Conversor de Moedas em tempo real (base BRL)")

valor = float(input("Digite um valor em reais (BRL): "))
moeda = input("Para qual moeda? (USD/EUR/GBP/CHF): ")

try:
    resultado = brl_to(moeda, valor)
    print(f"R$ {valor:.2f} = {resultado:.2f} {moeda.upper()}")
except Exception as e:
    print("Erro:", e)