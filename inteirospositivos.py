numeros = []
print("Obs: Se você digitar qualquer número negativo o programa ira parar de pedir para você informar números")
while True:
    numero = int(input("Informe um número:"))
    if numero >= 0:
        numeros.append(numero)
    else:
        print(f"A soma de todos os números é: {sum(numeros)}")
        print(f"A média aritmética de todos os números é {sum(numeros) / len(numeros)}")
        print(f"O maior número informado é: {max(numeros)}")
        print("Finalizado")
        exit()