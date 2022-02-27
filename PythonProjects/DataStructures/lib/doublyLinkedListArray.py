class DoublyLinkedListArray():
    def __init__(self):
        self.data = -999
        self.next_addr = None
        self.prev_addr = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next_addr(self):
        return self.next_addr

    def set_next_addr(self, next_addr):
        self.next_addr = next_addr

    def get_prev_addr(self):
        return self.prev_addr

    def set_prev_addr(self, prev_addr):
        self.prev_addr = prev_addr
