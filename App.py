import os
from colorama import Fore, Style, init
from tabulate import tabulate
from time import sleep


def prompt_cls():
    #Limpa o terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def navbar():
    print(f"{Fore.CYAN + Style.BRIGHT + '=' * 40}\n{Fore.GREEN + Style.BRIGHT + 'Calculo de IMC'.center(40)}\n{Fore.CYAN + Style.BRIGHT + '=' * 40}")

def pausar():
    input(Fore.YELLOW + 'Pressione qualquer tecla para continuar...')

def exibir_menu():
    opcoes_menu= [
        ['0', 'Exibir tabela do IMC'],
        ['1', 'Exibir resultado do IMC'],
        ['2', 'Fazer um novo cálculo'],
        ['3', 'Fechar Programa']
    ]

    prompt_cls()
    navbar()
    print(tabulate(opcoes_menu, headers=['Opção', 'Descrição'], tablefmt='fancy_grid'))

def exibir_tabela():
    opcoes_menu= [
        ['Abaixo de 17', 'Muito abaixo do peso'],
        ['Entre 17 e 18,5', 'Abaixo do Peso'],
        ['Entre 18,5 e 24,9', 'Peso normal'],
        ['Entre 25 e 29,9', 'Acima do peso'],
        ['Entre 30 e 34,5', 'Obesidade I'],
        ['Entre 35 e 39,9', 'Obesidade II (severa)'],
        ['Acima de 40', 'Obesidade III (mórbida)']
    ]

    prompt_cls()
    navbar()
    print(tabulate(opcoes_menu, headers=['IMC', 'Situação'], tablefmt='fancy_grid'))

def calc_imc(peso, altura):
    imc = peso / (altura * altura)

    result = ''
    if imc < 17:
        result = Fore.YELLOW + 'Muito abaixo do peso'
    elif imc >= 17 and imc < 18.5:
        result = 'Abaixo do peso'
    elif imc >= 18.5 and imc <= 24.9:
        result = Fore.GREEN + 'Peso normal'
    elif imc >= 25 and imc <= 29.9:
        result= 'Acima do peso'
    elif imc >= 30 and imc <= 34.9:
        result= Fore.RED + 'Obesidade I'
    elif imc >= 35 and imc <= 39.9:
        result= Fore.RED + 'Obesidade II (Severa)'
    elif imc >= 40:
        result= Fore.RED + 'Obesidade III (mórbida)'

    return imc, result


def pedir_dados():
    peso = None
    altura = None
    
    while peso == None:
        try:
            prompt_cls()
            peso = float(input(Fore.BLUE + 'Informe seu peso corporal em Kg: '))
        except:
            print(Fore.RED + 'O peso corporal precisa ser em kg, por exemplo: 55.3')
            sleep(2)

    while altura == None:
        try:
            prompt_cls()
            altura = float(input(Fore.BLUE + 'Informe a sua altura em metros: '))
        except:
            print(Fore.RED + 'A altura precisa ser em metros, por exemplo: 1.80')
            sleep(2)
    return peso, altura

def main():
    peso, altura = pedir_dados()

    while True:
        imc, result = calc_imc(peso, altura)

        exibir_menu()
        action= None
        while action == None:
                try:
                    action= int(input(Fore.BLUE + 'Selecione o número da opção que deseja: '))
                except:
                    pass

        if action == 0:
            exibir_tabela()
            pausar()
        elif action == 1:
            print(f'Seu IMC é: {imc}')
            print(f'Sua situação é: {result}')
            pausar()
        elif action == 2:
            peso, altura = pedir_dados()
            prompt_cls()
        elif action == 3:
            break
        else:
            pass

if __name__ == '__main__':
    main()