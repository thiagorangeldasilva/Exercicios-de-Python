#coding: UTF-8
'''
Irei construir um sistema bancário básico.
'''
def trocarVirgulaparaPonto(valor):
    if valor.count(',') > 0:
        valor = valor.replace(',', '.')
    return valor

def trocarPontoparaVirgula(valor):
    if valor.count('.') > 0:
        valor = valor.replace('.', ',')
    return valor

def tratarErroIntFloat(numero):
    numero = trocarVirgulaparaPonto(numero)
    if numero != '':
        if numero.isalpha() == False and numero.isalnum() == False:
            return 1
        elif numero.isdigit() == True:
            return 2
        else:
            return 0
    else:
        return 0

def trasnformar(tratar, numero):
    numero = trocarVirgulaparaPonto(numero)
    if tratar == 1:
        return float(numero)
    elif tratar == 2:
        return int(numero)

def printOpcao():
    print('------ MENU ------')
    print()
    print('(A) Consultar Saldo')
    print('(B) Saque')
    print('(C) Depósito')
    print('(D) Sair')

def confirmaAcao(acao):
    cond = True
    while cond:
        valor = input('Insira um valor para {0}: R$ '.format(acao))
        if tratarErroIntFloat(valor) == 1 or tratarErroIntFloat(valor) == 2:
            valor = trasnformar(tratarErroIntFloat(valor), valor)  
            while cond:
                print()
                print('Valor do ' + acao + ': R$ ' + str(valor).replace('.', ','))      
                print('Confirma ' + acao + '? (1) Sim / (2) Não')
                opcao = input('Opção escolhida: ')
                if tratarErroIntFloat(opcao) == 1 or tratarErroIntFloat(opcao) == 2:
                    opcao = trasnformar(tratarErroIntFloat(opcao), opcao)    
                    if opcao == 1:
                        print()
                        return valor
                    elif opcao == 2:
                        print()
                        break
                    else:
                        print('Opção inválida.')
                        print()
                else:
                    print('Opção inválida.')
                    print()
        else:
            print('Favor, informe um valor válido.')
            print()

def realizaroutro(acao, saldo):
    cond = True
    print('Saldo atual: R$', str(saldo).replace('.', ','))
    while cond:
        print('Realizar outro ' + acao + '? (1) Sim / (2) Não')
        opcao = input('Opção escolhida: ')
        if tratarErroIntFloat(opcao) == 1 or tratarErroIntFloat(opcao) == 2:
            opcao = trasnformar(tratarErroIntFloat(opcao), opcao)    
            if opcao == 1 or opcao == 2:
                return opcao
            else:
                print('Opção inválida.')
        else:
            print('Opção inválida.')
        
def saque(saldo):
    cond = True
    print()
    print('------ Saque ------')
    while cond:
        print()
        print('Valor disponível para saque: R$', str(saldo).replace('.', ','))
        saque = confirmaAcao('saque')
        if (saldo - saque) > 0:
            saldo -= saque
            print('Saque realizado.')        
            if realizaroutro('saque', saldo) == 2:
                return saldo
        else:
            print('Saque inválido, saldo menor que o saque pedido.')

def deposito(saldo):
    cond = True
    print()
    print('------ Deposito ------')
    while cond:
        print()
        print('Saldo atual: R$', str(saldo).replace('.', ','))
        deposito = confirmaAcao('deposito')
        saldo += deposito
        print('Saque realizado.')        
        if realizaroutro('deposito', saldo) == 2:
            return saldo

cond = True
saldo = 0

while cond:
    printOpcao()
    saldo = deposito(saldo)
    saldo = saque(saldo)
    break
input('Obrigado')