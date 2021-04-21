class Stack(object):
    def __init__(self, max_size):
        self.__items = []
        self.__reverse_stack = []
        self.__max_size = max_size

    def is_full(self):
        return len(self.__items) == self.__max_size

    def is_empty(self):
        return len(self.__items) == 0

    def print_stack(self):
        for i in range(self.get_num_elements() - 1, -1, -1):
            if i == self.get_num_elements() - 1:
                print(self.__items[i], "<--- top of stack")
            else:
                print(self.__items[i])

    def create_reverse_stack(self):
        for i in range(self.get_num_elements() - 1, -1, -1):
            self.__reverse_stack.append(self.__items[i])
        return self.__reverse_stack

    def print_reverse_stack(self):
        for i in range(self.get_num_elements() - 1, -1, -1):
            if i == self.get_num_elements() - 1:
                print(self.__reverse_stack[i], "<--- top of stack")
            else:
                print(self.__reverse_stack[i])

    def push(self, item):
        if self.is_full():
            print("Stack is full so cannot push")
        else:
            self.__items.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack is empty so cannot pop")
        else:
            self.__items.pop(-1)

    def set_max_size(self, new_size):
        self.__max_size = new_size

    def get_max_size(self):
        return self.__max_size

    def get_num_elements(self):
        return len(self.__items)

    def peak(self):
        return self.__items[-1]


if __name__ == "__main__":
    stack = Stack(5)
    stack.push("Hello")
    stack.push(3.14)
    stack.push([3, 2, 1])
    stack.print_stack()
