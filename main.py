from calculadora.operacoes import somar, subtrair, multiplicar, dividir

def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("❌ Valor inválido! Digite um número.")

def obter_operacao():
    operacoes = {"1": "Somar", "2": "Subtrair", "3": "Multiplicar", "4": "Dividir"}
    print("\nEscolha a operação:")
    for chave, valor in operacoes.items():
        print(f"  {chave} - {valor}")
    while True:
        opcao = input("Opção: ")
        if opcao in operacoes:
            return opcao
        print("❌ Opção inválida! Escolha entre 1 e 4.")

def main():
    print("=" * 35)
    print("      🧮 Calculadora Python")
    print("=" * 35)

    while True:
        opcao = obter_operacao()
        a = obter_numero("Digite o primeiro número: ")
        b = obter_numero("Digite o segundo número: ")

        try:
            if opcao == "1":
                resultado = somar(a, b)
            elif opcao == "2":
                resultado = subtrair(a, b)
            elif opcao == "3":
                resultado = multiplicar(a, b)
            elif opcao == "4":
                resultado = dividir(a, b)

            print(f"\n✅ Resultado: {resultado}\n")

        except ValueError as e:
            print(f"\n{e}\n")

        continuar = input("Deseja calcular novamente? (s/n): ")
        if continuar.lower() != "s":
            print("\nAté mais! 👋")
            break

if __name__ == "__main__":
    main()
