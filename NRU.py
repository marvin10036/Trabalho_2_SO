import random


class Page:
    def __init__(self, page_number, referenced=False, modified=False):
        self.page_number = page_number
        self.referenced = referenced


def NRU(mp: [], max_page_frames, inputList: []):
    page_faults_counter = 0
    for page_number in inputList:
        if len(mp) < max_page_frames:
            mp.append(Page(page_number))
        else:
            if reference_page(mp, page_number):
                pass
            else:
                page_faults_counter += 1
                mp.remove(select_victim_page(mp))

    return page_faults_counter


def reference_page(pages: [Page], page_number):
    for page in pages:
        if page.page_number == page_number:
            page.referenced = True
            return True
    return False


def select_victim_page(pages):
    class_index = {0: [], 1: []}

    for page in pages:
        index = int(page.referenced)
        class_index[index].append(page)
        page.referenced = False

    for i in range(2):
        if len(class_index[i]) > 0:
            return class_index[i][random.randint(0, len(class_index[i])-1)]
