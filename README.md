App Bancário Simples em Python

Este projeto é um aplicativo bancário básico desenvolvido em Python, com funcionalidades de depósito, saque e exibição de extrato. O objetivo é permitir operações simples e seguras para gerenciamento de saldo, mantendo um limite de saques por dia.
Funcionalidades

    Depósito: Permite ao usuário adicionar dinheiro à conta.
    Saque: Realiza saques com verificação de saldo, limite de valor por saque e limite de número de saques por dia.
    Exibir Extrato: Exibe todas as transações realizadas (depósitos e saques) e o saldo disponível.
    Limites:
        Limite de saque diário: R$ 500,00.
        Limite de até 3 saques por dia.

Estrutura do Projeto

    depositar(saldo, extrato): Função que permite ao usuário depositar valores na conta, atualizando o saldo e o extrato.
    sacar(saldo, extrato, numero_saques, limite, limite_de_saques): Função que realiza saques, verificando o saldo, o limite por saque e o número de saques diários permitidos.
    exibir_extrato(saldo, extrato): Exibe o extrato com todas as movimentações da conta, além do saldo atual.
    main(): Função principal que executa o menu interativo com as opções de operação bancária.

Como Executar o Projeto

    Clone o repositório:

    bash

git clone https://github.com/seu-usuario/app-bancario-simples.git

Navegue até a pasta do projeto:

bash

cd app-bancario-simples

Execute o script principal:

bash

    python main.py

Menu de Operações

O app exibe um menu interativo com as seguintes opções:

plaintext

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

    [d] Depositar: Adiciona um valor ao saldo.
    [s] Sacar: Retira um valor do saldo, respeitando o limite de R$ 500,00 por saque e até 3 saques por dia.
    [e] Extrato: Exibe o histórico de transações (depósitos e saques) e o saldo disponível.
    [q] Sair: Encerra o programa.
