virtual_memory = int(input("Virtual Memory Size: "))
page_size = int(input("\nPage Size: "))
page_sequence = input("\nPage Sequence"
                      "\ninput example: 123456 or 1 2 3 4 5 6"
                      "\n--------> ")
page_sequence = [char for char in page_sequence if char != ' ']

class FIFO():
    def __init__(self):

        self.memory_size = virtual_memory // page_size
        self.page_fault = 0
        self.queue = []
        self.memory_state = []

        while True:

            for page in page_sequence :
                if page not in self.queue:
                    if len(self.queue) < self.memory_size :
                        self.queue.append(page)
                        self.page_fault += 1
                        self.memory_state += [self.queue.copy()]
                    else:
                        self.queue.pop(0)
                        self.page_fault += 1
                        self.queue.append(page)
                        self.memory_state += [self.queue.copy()]
                else: self.memory_state += [self.queue.copy()]
            break

    def __str__(self):
        self.result = "\nPage Requests\tMemory State\n"

        for i in range(len(self.memory_state)):

            self.result += str(f"\t{i}\t{self.memory_state[i]}\n")

        self.result += f"\nNumber of Fault Requests: {self.page_fault}"
        self.result += f"\n       Page       Table : {list(sorted(set(page_sequence)))}\n"


        return self.result


a = FIFO()
print(a)