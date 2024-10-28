# Libs

import time
import threading
import os

# UI inicial

def print_UI():

    header_1 = "\n*****************************************\n"
    header_2 = "* Programinha de imprimir do Luizito :D *\n"
    header_3 = "*****************************************\n"
    header_4 = "\nDigite uma das opções abaixo:\n"
    header_5 = "\n1 - Imprimir frase pronta\n2 - Imprimir frase digitada\n3 - Imprimir ASCII art - em breve*\n"

    header = header_1 + header_2 + header_3 + header_4 + header_5
    
    print(header)

# Função de validação de entrada

def validate_input(min, max):
    while True:
        try:
            valid_input = int(input())
            if min <= valid_input <= max:
                return valid_input
            else:
                print("Opção inválida! Digite novamente!")
        except ValueError:
            print("Opção inválida! Digite novamente!")

# Menu e fluxo da aplicação

def solve_ready_sentence():

    ready_sentence_1 = "Fall in love again and again and again."
    ready_sentence_2 = "Ser feliz sem motivo é a mais autêntica forma de felicidade."
    ready_sentence_3 = "A mind that is stretched by a new experience can never go back to its old dimensions."
    
    print("\nEscolha uma das frases prontas abaixo:\n")
    print("1 - "+ ready_sentence_1)
    print("2 - "+ ready_sentence_2)
    print("3 - "+ ready_sentence_3 + "\n")
    
    option = validate_input(1,3)
    
    if option == 1:
        phrase = ready_sentence_1
    elif option == 2:
        phrase = ready_sentence_2
    elif option == 3:
        phrase = ready_sentence_3
    return phrase + " "

def solve_any_sentence():
    phrase = input("\nDigite a frase desejada abaixo:\n\n")
    return phrase + " "

# Tipo de execução do programa

def solve_exec_type():
    print("\nDeseja imprimir:\n\n1 - Infinitamente\n2 - Apenas 1 vez\n")
    exec_type = validate_input(1,2)
    return exec_type

# Velocidade de execução do programa

def solve_speed():

    print("\nQual a velocidade desejada?\n")
    print("1 - Rápido")
    print("2 - Médio")
    print("3 - Lento\n")

    speed = validate_input(1,3)

    if speed == 1:
        speed = 0.1
    elif speed == 2:
        speed = 0.3
    elif speed == 3:
        speed = 0.5

    return speed

# Início do algoritmo principal

# Função 1 - Popular uma lista com todas as palavras da frase

def identify_words(phrase):
    words = []
    a = ""
    for i in phrase:
        a = a + i
        if i == " ":
            word = a
            words.append(word)
            a = ""
    return words

# Função 2 - Imprimir as palavras - crescente

def print_asc(words, speed):
    a = ""
    for i in range(len(words)):
        a = a + words[i]
        print(a)
        time.sleep(speed)

# Função 3 - Imprimir as palavras - decrescente

def print_desc(words, speed):
    size = len(words)

    while size > 0:
        a = ""
        words.pop(size - 1)
        for i in range(len(words)):
            a = a + words[i]
        print(a)
        time.sleep(speed)
        size = size - 1

def print_sentece_infinitely(words, speed, phrase):
    while True:
        words = identify_words(phrase)
        print_asc(words, speed)
        print_desc(words, speed)

# Função de execução do programa:

def app():

    print_UI()

    print_type = validate_input(1,2)

    if print_type == 1:
        phrase = solve_ready_sentence()
    elif print_type == 2:
        phrase = solve_any_sentence()

    exec_type = solve_exec_type()
    speed = solve_speed()
    words = identify_words(phrase)

    if exec_type == 1:
        print_sentece_infinitely(words, speed, phrase)
    elif exec_type == 2:
        print_asc(words, speed)
        print_desc(words, speed)

    input("Pressione Enter para sair...")

# Execução do programa:

app()

# Fim da aplicação
# Glxy 2024