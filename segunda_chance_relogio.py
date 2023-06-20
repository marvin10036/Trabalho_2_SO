import random


page_table = []

class Node:
    def __init__(self):
        self.page_number = None
        self.next = None
        self.referenced = 0


def print_circular_linked_list(first_node: Node, last_node: Node, pointer: Node):
    current_node = first_node
    while True:
        print(f'[{current_node.page_number},{current_node.referenced}]', end=',')
        current_node = current_node.next
        if current_node == last_node:
            print(f'[{current_node.page_number},{current_node.referenced}]    {pointer.page_number}')
            break


def second_chance_with_clock(max_page_frames: int, input_list: []):
    page_faults_counter = 0

    first_node = Node()
    last_node = Node()

    first_node.next = last_node
    last_node.next = first_node

    for page_number in range(max_page_frames-2):
        node = Node()
        node.next = first_node.next
        first_node.next = node

    current_node = first_node

    for page_number in input_list:
        if page_number in page_table:
            find_node = first_node
            while True:
                if page_number == find_node.page_number:
                    find_node.referenced = 1
                    break
                else:
                    find_node = find_node.next
        else:
            page_faults_counter += 1

            while page_number not in page_table:
                if current_node.referenced == 0:

                    if current_node.page_number is not None:
                        page_table.remove(current_node.page_number)

                    current_node.page_number = page_number
                    current_node.referenced = 1

                    page_table.append(page_number)
                    current_node = current_node.next

                else:
                    current_node.referenced = 0
                    current_node = current_node.next

        # Descomente para ver a lista circular sendo alterada.
        # Representacao: [page_number, bit de refecia], valor mais afastador é onde o ponteiro da lista se encontra

        # print_circular_linked_list(first_node, last_node, current_node)

    return page_faults_counter
