numOfPrss = input("Add the number of the processes: ")

while True:
    if int(numOfPrss) == 0 :
        numOfPrss = input("Enter a number again: ")
    else: 
        processes = [0] * int(numOfPrss)
        arrival_times = [0] * int(numOfPrss)
        burst_times = [0] * int(numOfPrss)
        break
print("\n*PLEASE USE NATURAL NUMBERS*")

for i in range(int(numOfPrss)):
    processes[i] = f"P{i+1}"
    arrival_times[i] = int(input(f"\nEnter the arrival time for process {i+1}: "))
    burst_times[i] =   int(input(f"Enter the *burst* time for process {i+1}: "))


class FirstComeFirstServed:
    def __init__(self):
        self._ready_queue = []
        self._current_time = 0
        self._completion_times = [0] * len(processes)
        self._remaining_burst_times = burst_times[:]
        self._gantt_chart = []

        while sum(self._remaining_burst_times) > 0 :
            self._ready_queue = self.queue_update(processes, self._current_time, self._ready_queue)

            if len(self._ready_queue) > 0 :

                process_index = self._ready_queue[0]

                executed_time = self._remaining_burst_times[process_index]
                self._gantt_chart.append((processes[process_index], self._current_time, self._current_time + executed_time))


                self._remaining_burst_times[process_index] -= executed_time

                for i in range(executed_time):
                    self._current_time += 1
                    self._ready_queue = self.queue_update(processes, self._current_time, self._ready_queue)

                self._ready_queue.pop(0)
                self._completion_times[process_index] = self._current_time

            else: self._current_time += 1


    def queue_update(self, processes, current_time, queue):
        for i in range(len(processes)):
            if current_time == arrival_times[i] and self._remaining_burst_times[i] > 0 and i not in queue:
                queue.append(i)
        return queue


    def __str__(self):

        result = "\nFirst Come First Served\n"
        result += "Gantt Chart:"

        for item in self._gantt_chart:
            result += f"| {item[0]} "
        result += "|\n\t    "

        for item in self._gantt_chart:
            result += f"{item[1]:<4} "
        result += f"{self._gantt_chart[-1][2]:<4}"

        result += "\n\nAverage Turnaround Time:"+f"{round((sum(self._completion_times) - sum(arrival_times)) /len(processes))}"
        result += "\nAverage Waiting Time:   "+f"{round(((sum(self._completion_times) - sum(arrival_times)) - sum(burst_times)) /len(processes))}"

        return result


class ShortestJobNext:
    def __init__(self):
        self._ready_queue = []
        self._current_time = 0
        self._completion_times = [0] * len(processes)
        self._remaining_burst_times = burst_times[:]
        self._gantt_chart = []

        while sum(self._remaining_burst_times) != 0 :

            self._ready_queue = self.queue_update(processes, self._current_time, self._ready_queue)
            min_val = 1000
            j = 0

            if len(self._ready_queue) > 1 :
                for i in range(len(self._ready_queue)):
                    if self._remaining_burst_times[self._ready_queue[i]] < min_val:
                        min_val = self._remaining_burst_times[self._ready_queue[i]]
                        j = i

            if len(self._ready_queue) > 0 :

                process_index = self._ready_queue[j]

                executed_time = self._remaining_burst_times[process_index]
                self._gantt_chart.append((processes[process_index], self._current_time, self._current_time + executed_time))
                self._remaining_burst_times[process_index] -= executed_time
                self._completion_times[process_index] = executed_time + self._current_time

                for i in range(executed_time):
                    self._current_time += 1
                    self._ready_queue = self.queue_update(processes, self._current_time, self._ready_queue)

                self._ready_queue.pop(j)

            else : self._current_time += 1


    def queue_update(self, processes, current_time, queue):
        for i in range(len(processes)):
            if current_time == arrival_times[i] and self._remaining_burst_times[i] > 0 and i not in queue:
                queue.append(i)
        return queue


    def __str__(self):

        result = "\nShortest Job Next"
        result += "\nGantt Chart:"

        for item in self._gantt_chart:
            result += f"| {item[0]} "
        result += "|\n\t    "

        for item in self._gantt_chart:
            result += f"{item[1]:<4} "
        result += f"{self._gantt_chart[-1][2]:<4}"

        result += "\n\nAverage Turnaround Time:"+f"{round((sum(self._completion_times) - sum(arrival_times)) /len(processes))}"
        result += "\nAverage Waiting Time:   "+f"{round(((sum(self._completion_times) - sum(arrival_times)) - sum(burst_times)) /len(processes))}"

        return result


class RoundRobin :
    def __init__(self):
        self._ready_queue = []
        self._current_time = 0
        self._completion_times = [0] * len(processes)
        self._remaining_burst_times = burst_times[:]
        self._gantt_chart = []
        self.time_quantum = int(input("\nDefine Quantum Time: "))


        while sum(self._remaining_burst_times) > 0 :
            self._ready_queue = self.queue_update(processes, self._current_time, self._ready_queue)

            if len(self._ready_queue) > 0 :

                process_index = self._ready_queue[0]

                executed_time = min(self._remaining_burst_times[process_index], self.time_quantum)
                self._gantt_chart.append((processes[process_index], self._current_time, self._current_time + executed_time))

                self._remaining_burst_times[process_index] -= executed_time

                for i in range(executed_time):
                    self._current_time += 1
                    self._ready_queue = self.queue_update(processes, self._current_time, self._ready_queue)

                self._ready_queue.pop(0)

                if self._remaining_burst_times[process_index] == 0 :
                    self._completion_times[process_index] = self._current_time

                else: self._ready_queue.append(process_index)

            else: self._current_time += 1


    def queue_update(self, processes, current_time, queue):
        for i in range(len(processes)):
            if current_time == arrival_times[i] and self._remaining_burst_times[i] > 0 and i not in queue:
                queue.append(i)
        return queue


    def __str__(self):
        result = "\nRound Robin"
        result += "\nGantt Chart:"

        for item in self._gantt_chart:
            result += f"| {item[0]} "
        result += "|\n\t    "

        for item in self._gantt_chart:
            result += f"{item[1]:<4} "
        result += f"{self._gantt_chart[-1][2]:<4}"

        result += "\n\nAverage Turnaround Time:"+f"{round((sum(self._completion_times) - sum(arrival_times)) /len(processes))}"
        result += "\nAverage Waiting Time:   "+f"{round(((sum(self._completion_times) - sum(arrival_times)) - sum(burst_times)) /len(processes))}"

        return result


usr_inpt = int(input("\nTo view First Come First Served type *1*"
                     "\nTo view   Shortest  Job    Next type *2*"
                     "\nTo view      Round        Robin type *3*"
                     "\nTo   compare   all   algorithms type *4*"
                     "\nTo Exit type *0*\n------> "))

while True:

    if usr_inpt == 1:
        a = FirstComeFirstServed()
        print(a)
        print("-------------------------------------")

    elif usr_inpt == 2:
        b = ShortestJobNext()
        print(b)
        print("-------------------------------------")

    elif usr_inpt == 3:
        c = RoundRobin()
        print(c)
        print("-------------------------------------")

    elif usr_inpt == 4:
        a = FirstComeFirstServed()
        print(a)
        print("-------------------------------------")
        b = ShortestJobNext()
        print(b)
        print("-------------------------------------")
        c = RoundRobin()
        print(c)
        print("-------------------------------------")

    elif usr_inpt == 0:
        break
    
    usr_inpt = int(input("\nTo view First Come First Served type *1*"
                     "\nTo view   Shortest  Job    Next type *2*"
                     "\nTo view      Round        Robin type *3*"
                     "\nTo   compare   all   algorithms type *4*"
                     "\nTo Exit type *0*\n------> "))