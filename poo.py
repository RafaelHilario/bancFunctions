class Banco:
    def __init__(self, saldo_inicial=0, limite=500, limite_de_saques=3):
        self.saldo = saldo_inicial
        self.limite = limite
        self.extrato = ""
        self.numero_saques = 0
        self.limite_de_saques = limite_de_saques

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.limite_de_saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
            print("Saque realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")

def main():
    banco = Banco()

    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            banco.depositar(valor)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            banco.sacar(valor)

        elif opcao == "e":
            banco.exibir_extrato()

        elif opcao == "q":
            print("Obrigado por utilizar nosso sistema bancário. Até logo!")
            break

        else:
            print("Operação inválida, selecione a opção correta.")

if __name__ == "__main__":
    main()
