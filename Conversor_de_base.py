def para_decimal():
  numero = input("\nDigite o número binário: ")
  soma_binario = 0
  posicao_binario = 0
  for digito in reversed(numero):
    valor = int(digito)
    calculo = 2**posicao_binario
    resultado = calculo * valor
    soma_binario += resultado
    posicao_binario += 1

  print("O número decimal é: ",soma_binario)
  

resto_decimal = []
def para_binario():
  entrada = int(input("\nDigite um número inteiro: "))
  while entrada > 0:
    resto = entrada % 2
    resto_decimal.append(resto)
    entrada = entrada // 2

  resto_decimal.reverse()
  print("O número em binário é:", "".join(str(d) for d in resto_decimal))

while True:
  opcao = input("\n1 - Converter binário para decimal \n2 - Converter decimal para binário \n3 - Sair do sistema\nResposta: ")
  if opcao == "1":
    para_decimal()
  elif opcao == "2":
    para_binario()
  elif opcao == "3":
    print("Saindo do sistema...")
    break