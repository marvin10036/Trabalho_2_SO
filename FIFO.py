class FIFO_Page_Table:
    class FIFO_Page_Table_Registry:
        def __init__(self, presente_ausente=False, MP_index=None):
            self.__presente_ausente = presente_ausente
            self.__MP_index = MP_index

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

    def __init__(self, max_pages):
        self.registers = []

        for i in range(max_pages):
            registry = self.FIFO_Page_Table_Registry()
            self.registers.append(registry)

        #a FIFO é uma estrutura auxiliar apenas para remoções e inserções
        self.fifo = []

    def allocate_in_MP(self, registry, MP_index):
        registry.MP_index = MP_index
        registry.presente_ausente = True

    def deallocate_from_MP(self, registry):
        registry.MP_index = None
        registry.presente_ausente = False

    def insert_in_fifo(self, page_table_index):
        self.fifo.append(page_table_index)

    def remove_from_fifo(self):
        return self.fifo.pop(0)

    #faz os dois, remove da fila e tira da MP
    def remove_first_element(self):
        page_table_index = self.remove_from_fifo()

        element_to_be_removed = self.registers[page_table_index]
        MP_index_to_remove = element_to_be_removed.MP_index

        self.deallocate_from_MP(element_to_be_removed)

        return MP_index_to_remove

def FIFO(max_pages, Input_List, MP, max_page_frames):
    page_faults_counter = 0

    FIFO_pt = FIFO_Page_Table(max_pages)
    for page_table_index in Input_List:
        registro_page_table = FIFO_pt.registers[page_table_index]

        if registro_page_table.presente_ausente:
            #a fifo nao atualiza a estrutura em caso de presenca
            pass
        else:
            page_faults_counter += 1

            #troca de MP_index entre oq entra e o que sai
            if len(MP) == max_page_frames:
                MP_index_to_remove = FIFO_pt.remove_first_element()
                FIFO_pt.allocate_in_MP(registro_page_table, MP_index_to_remove)
            else:
                MP.append(True)
                FIFO_pt.allocate_in_MP(registro_page_table, len(MP) -1)

            FIFO_pt.insert_in_fifo(page_table_index)

    return page_faults_counter

