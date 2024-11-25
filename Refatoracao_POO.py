class Cliente():
    def init(self, nome, idade, saldo):
        self.nome = nome
        self.idade = idade
        self.saldo = saldo

    def mostrar_informacoes(self):
        print(f"Cliente: {self.nome}, Idade: {self.idade}, Saldo: {self.saldo}")

    def atualizar_saldo(self, valor):
        self.saldo += valor
        print(f"Saldo atualizado: R${self.saldo:.2f}")

#cliente1 = Cliente("João Silva", 30, 1000.0)
#cliente1.mostrar_informacoes()
#cliente1.atualizar_saldo(500.0)
#cliente1.mostrar_informacoes()

print("\nCadastro de cliente")
nome = input("Digite o nome do cliente: ")
idade = int(input("Digite a idade do cliente: "))
saldo = float(input("Digite o saldo inicial do cliente: "))

cliente1 = Cliente(nome, idade, saldo)
cliente1.mostrar_informacoes()

print("\nAtualizar Saldo")
valor = float(input("Digite o valor para atualizar o saldo: "))
cliente1.atualizar_saldo(valor)

cliente1.mostrar_informacoes()