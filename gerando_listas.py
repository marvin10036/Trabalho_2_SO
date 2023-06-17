from random import randint, shuffle

'''
talvez não precise, só checar na hora de inserir se o len() é maior que o
page_frames_number, nesse caso inserções que impliquem remoções devem chamar o
algoritmo correspondente a iteração
'''

def generate_input_list_random(input_list_size, pages_number):
    input_list = []
    for i in range(input_list_size):
        current_value = randint(0, pages_number - 1)
        input_list.append(current_value)

    return input_list

def generate_input_list_with_repetition(input_list_size, pages_number):
    input_list = []

    '''
    5 é uma decisão arbitrária dos subconjuntos que eu quero deixar aleatório,
    tudo isso é para gerar repetições, já que com um simples randint quanto
    quanto maior o vetor, mais difícil haver repetições, tentando emular
    localidade aqui.
    '''
    tamanho_subconjunto = 5

    #vou assumir que o tamanho do input nunca será menor que o número de páginas
    numero_subconjuntos = pages_number // tamanho_subconjunto
    resto = pages_number % tamanho_subconjunto

    index_subconjunto = 0
    for i in range(input_list_size):
        lower_int = index_subconjunto * 5 #tem que ser 5 e n tamanho_subconjunto
        upper_int = lower_int + tamanho_subconjunto - 1 #-1 pois o intervalo é fechado no randint

        current_value = randint(lower_int, upper_int)
        input_list.append(current_value)

        tamanho_subconjunto = 5 #resetando o valor se ele tiver sido alterado

        index_subconjunto += 1
        if index_subconjunto == numero_subconjuntos:
            index_subconjunto = 0
        if index_subconjunto == (numero_subconjuntos - 1):
            tamanho_subconjunto += resto #o último subconjunto tem o resto agregado

    #dois shuffles na lista para não ser enviesado com esses acessos repetidos
    shuffle(input_list)
    shuffle(input_list)
    return input_list

