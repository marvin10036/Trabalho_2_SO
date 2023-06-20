from random import randint, shuffle
from gerando_listas import generate_input_list_random, generate_input_list_with_repetition
from LRU import LRU
from NRU import NRU
from FIFO import FIFO

max_page_frames = int(input("Escreva o número de quadros (page frames): ")) #10
max_page_table_size = int(input("Escreva o número de paginas na tabela de paginas: ")) #100

input_list_size = int(input("Escreva o número de referencias a memorias que devem ocorrer: ")) #1.000.000
Input_List = generate_input_list_with_repetition(input_list_size, max_page_table_size) #lista em si
#Input_List = generate_input_list_random(input_list_size, max_pages)

#MP é a mesma não importando o algoritmo
#vou usar apenas append para manipular, não é pra haver espaços vazios entre entradas
MP = []

###main, page_number, Input_List, MP, max_page_frames

page_faults = LRU(max_page_table_size, Input_List, MP, max_page_frames)
print(page_faults)
print(NRU([], max_page_frames, Input_List))


#MP = []
#page_faults = FIFO(max_pages, Input_List, MP, max_page_frames)
#print(page_faults)

