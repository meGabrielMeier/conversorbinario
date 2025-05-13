numero =input("Digite o número binário: ")

soma = 0
posicao = 0

for digito in reversed(numero):
  valor = int(digito)
  calculo = 2**posicao
  resultado = calculo * valor
  soma += resultado
  posicao += 1

print("O número decimal é: ",soma)