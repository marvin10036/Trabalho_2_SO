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
        self.registers = []

        for i in range(tamanho_page_table):
            registry = self.LRU_Page_Table_Registry(i)
            self.registers.append(registry)

        #self.len_registers = len(self.registers)
        #self.least_recently_used_pointer = 0

    def insert(self, registry):
        self.registers.append(registry)

    def remove_least_recently_used(self):
        #atencao algoritmo O(N), dava pra fzr melhor com um ponteiro, mas mt complexo
        for register in self.registers:
            if register.presente_ausente == True:
                registro_lru = register
                break

        registro_lru.presente_ausente = False

        MP_index_to_remove = registro_lru.MP_index
        registro_lru.MP_index = None

        return MP_index_to_remove

    #colocando ele no final da fila, para ele ser o mais recentemente utilizado
    def update(self, registry):
        aux_registry = registry

        self.registers.remove(registry)
        self.insert(aux_registry)

    #primeiro a ser chamado
    def search(self, element_PT_index):
        #atencao algoritmo O(N) a seguir
        for register in self.registers:
            if (register.PT_index == element_PT_index):
                return register


def LRU (pages_number, Input_List, MP, max_page_frames):
    page_faults_counter = 0

    LRU_pt = LRU_Page_Table(pages_number)
    for page_table_index in Input_List:
        registro_page_table = LRU_pt.search(page_table_index)

        if registro_page_table.presente_ausente:
            LRU_pt.update(registro_page_table)
        else:
            page_faults_counter += 1

            #tira da PT, tira da MP antes de inserir outro
            if len(MP) == max_page_frames:
                least_recently_used_MP_index = LRU_pt.remove_least_recently_used()
                MP.pop(least_recently_used_MP_index)

            MP.append(True)
            registro_page_table.MP_index = len(MP) - 1
            registro_page_table.presente_ausente = True
            LRU_pt.update(registro_page_table)

    return page_faults_counter

