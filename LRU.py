class LRU_Page_Table:
    class LRU_Page_Table_Registry:
        def __init__(self, PT_index, presente_ausente=False, MP_index=None):
            self.__PT_index = PT_index
            self.__presente_ausente = presente_ausente
            self.__MP_index = MP_index

        @property
        def PT_index(self):
            return self.__PT_index

        @PT_index.setter
        def PT_index(self, new_PT_index):
            self.__PT_index = new_PT_index

        @property
        def presente_ausente(self):
            return self.__presente_ausente

        @presente_ausente.setter
        def presente_ausente(self, new_presente_ausente):
            self.__presente_ausente = new_presente_ausente

        @property
        def MP_index(self):
            return self.__MP_index

        @MP_index.setter
        def MP_index(self, new_MP_index):
            self.__MP_index = new_MP_index

    def __init__(self, tamanho_page_table):
        #diferente da implementacao da fifo, registers aqui seria a estrutura
        #auxiliar já, e o atributo PT_index ajuda a encontrar a posicao real em
        #uma lista hipoteticamente ordenada
        self.registers = []

        for i in range(tamanho_page_table):
            registry = self.LRU_Page_Table_Registry(i)
            self.registers.append(registry)

        #self.len_registers = len(self.registers)
        #self.least_recently_used_pointer = 0

    def allocate_in_MP(self, registry, MP_index):
        registry.MP_index = MP_index
        registry.presente_ausente = True

    def deallocate_from_MP(self, registry):
        registry.MP_index = None
        registry.presente_ausente = False

    def remove_least_recently_used(self):
        #atencao algoritmo O(N), dava pra fzr melhor com um ponteiro, mas mt complexo
        for register in self.registers:
            if register.presente_ausente == True:
                registro_lru = register
                break

        MP_index_to_remove = registro_lru.MP_index

        self.deallocate_from_MP(registro_lru)

        return MP_index_to_remove

    #colocando ele no final da fila, para ele ser o mais recentemente utilizado
    def update(self, registry):
        aux_registry = registry

        self.registers.remove(registry)
        self.registers.append(aux_registry)

    def search(self, element_PT_index):
        #atencao algoritmo O(N) a seguir
        for register in self.registers:
            if (register.PT_index == element_PT_index):
                return register


def LRU (max_pages, Input_List, MP, max_page_frames):
    page_faults_counter = 0

    LRU_pt = LRU_Page_Table(max_pages)
    for page_table_index in Input_List:
        registro_page_table = LRU_pt.search(page_table_index)

        if registro_page_table.presente_ausente:
            LRU_pt.update(registro_page_table)
        else:
            page_faults_counter += 1

            #nesse caso tem que trocar MP_index com o least_recently_used
            if len(MP) == max_page_frames:
                least_recently_used_MP_index = LRU_pt.remove_least_recently_used()
                LRU_pt.allocate_in_MP(registro_page_table,
                                      least_recently_used_MP_index)
            else:
                MP.append(True)
                LRU_pt.allocate_in_MP(registro_page_table, len(MP) - 1)

            LRU_pt.update(registro_page_table)

    return page_faults_counter

