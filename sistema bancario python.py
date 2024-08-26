# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:55:22 2024

@author: 10723790
"""
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
idade = int(idade)
cidade = input("Digite sua cidade: ")
idadeMinima = int(18)
valorDisponivel = 1460

if (idade >= idadeMinima):

     print (f"Bem-vindo {nome}, você tem {idade} anos, e mora em {cidade}")

     print ("Serviços disponíveis: ")
     print ("1) Depósito")
     print ("2) Saque")
     print ("3) Extrato")
     selecaoOperacao = input("Digite qual operação você quer realizar: ")

if (selecaoOperacao == "1"):
    limiteDeposito = 5000
    print("Você selecionou Depósito!")
    valorDeposito = input("Digite o valor do depósito que deseja realizar: ")
    valorDeposito = int(valorDeposito)
    if (valorDeposito < limiteDeposito):
       valorDisponivel = float(valorDisponivel + valorDeposito)
       print ("Depósito realizado com sucesso.")
       print (f"Seu novo saldo é de R$ {valorDisponivel}")
    else:
        print (f"O depósito de R${valorDeposito} excedeu o limite que é R${limiteDeposito}")
           
elif (selecaoOperacao == "2"):
           
    valorSaque = input("Digite o valor do saque: ")
    valorSaque = int(valorSaque)

    if (valorSaque <= valorDisponivel):
        valorDisponivel = float(valorDisponivel - valorSaque)
        print(f"Senhor {nome}, você realizou um saque de R${valorSaque}. Seu novo saldo é de R${valorDisponivel}")
    else:
        print("Saque não foi realizado :(")
        print(f"O valor digitado não está disponível R${valorDisponivel}")

elif (selecaoOperacao == "3"):    
    print("Segue seu extrato:")
    print(f"Saldo disponivel {valorDisponivel}")
    print(f"Depósitos realizados {valorDeposito}")
    print(f"Saques realizados {valorSaque}")
    
else:
    print ("Não foi encontrada nenhuma operação")
    
    
    
    


        
        
    


