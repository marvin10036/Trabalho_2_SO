from random import randint, shuffle
from gerando_listas import generate_input_list_random, generate_input_list_with_repetition
from LRU import LRU

max_page_frames = int(input("Escreva o número de quadros (page frames): "))
pages_number = int(input("Escreva o número de paginas na tabela de paginas: "))

input_list_size = int(input("Escreva o número de referencias a memorias que devem ocorrer: "))
Input_List = generate_input_list_with_repetition(input_list_size, pages_number)
#Input_List = generate_input_list_random(input_list_size, pages_number)

#MP é a mesma não importando o algoritmo
#vou usar append e pop para manipular, não é pra haver espaços vazios entre entradas
MP = []

print(MP)
print(Input_List)

###main, page_number, Input_List, MP, max_page_frames
page_faults = LRU(pages_number, Input_List, MP, max_page_frames)
print(page_faults)

