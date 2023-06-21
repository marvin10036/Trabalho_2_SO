from random import randint, shuffle
from gerando_listas import generate_input_list_random, generate_input_list_with_repetition
from LRU import LRU
from NRU import NRU
from FIFO import FIFO
from segunda_chance_relogio import second_chance_with_clock

max_page_frames = int(input("Escreva o número de quadros (page frames): ")) #10
max_page_table_size = int(input("Escreva o número de paginas na tabela de paginas: ")) #100

input_list_size = int(input("Escreva o número de referencias a memorias que devem ocorrer: ")) #1.000.000
Input_List = generate_input_list_with_repetition(input_list_size, max_page_table_size) #lista em si
#Input_List = generate_input_list_random(input_list_size, max_pages)

#MP é a mesma não importando o algoritmo
#vou usar apenas append para manipular, não é pra haver espaços vazios entre entradas

print("Número page faults com NRU: " + str(NRU([], max_page_frames, Input_List)))
print("Número page faults com LRU: " + str(LRU(max_page_table_size, Input_List, [], max_page_frames)))
print("Número page faults com FIFO: " + str(FIFO(max_page_table_size, Input_List, [], max_page_frames)))
print("Número page faults com segunda chance/relógio: " + str(second_chance_with_clock(max_page_frames, Input_List)))


