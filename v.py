import queue
import random


# Define the Process class to keep track of process attributes
class Process:
    def __init__(self, process_id, rem_burst_time, burst_time, arrival_time):
        self.process_id = process_id
        self.rem_burst_time = rem_burst_time
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.turnaround_time = 0
        self.waiting_time = 0


# Define the RoundRobinScheduler class to implement the scheduling algorithm

class RoundRobinScheduler:
    def __init__(self):
        self.att = []
        self.que = queue.Queue()
        self.current_time = 0
        self.total_turnaround_time = 0
        self.total_waiting_time = 0
        self.quantum = int(input("Enter quantum size :"))

    # Method to add a new process to the list of processes
    def add_process(self, process_id, rem_burst_time, burst_time, arrival_time):
        p = Process(process_id, rem_burst_time, burst_time, arrival_time)
        self.att.append(p)

    # Method to add a new process to the list of processes
    def algorithm(self, n):
        completed_processes = 0  # Keep track of the number of completed processes
        print("Process table in order of process completion")
        print("pid\tAT\tBT\tCT\t\tTAT\t\tWT")
        while len(self.att) > 0 or not self.que.empty():
            # Keep track of the number of completed processes
            for i in self.att:
                if i.arrival_time == self.current_time:
                    self.que.put(i)
            # If the queue is not empty, execute the next process for the quantum size
            if not self.que.empty():
                a = self.que.get()
                for n in range(self.quantum):
                    if a.rem_burst_time > 0:
                        a.rem_burst_time -= 1
                        self.current_time += 1
                        # Add processes that have arrived at the current time to the queue

                        for i in self.att:
                            if i.arrival_time == self.current_time:
                                self.que.put(i)
                    else:
                        break
                if a.rem_burst_time > 0:
                    self.que.put(a)
                else:
                    a.turnaround_time = self.current_time - a.arrival_time
                    a.waiting_time = a.turnaround_time - a.burst_time
                    self.total_turnaround_time += a.turnaround_time
                    self.total_waiting_time += a.waiting_time
                    print(a.process_id, "\t", a.arrival_time, "\t", a.burst_time, "\t", self.current_time, "\t",
                          a.turnaround_time, "\t", a.waiting_time)
                    completed_processes += 1
                # calculate avg turn around and waiting time
                if len(self.att) == 0 or self.que.empty():
                    avg_turnaround_time = self.total_turnaround_time / completed_processes
                    avg_waiting_time = self.total_waiting_time / completed_processes
                    print("Average turnaround time:", avg_turnaround_time)
                    print("Average waiting time:", avg_waiting_time)

    # define function to generate random numbers
    @staticmethod
    def random_num_gen():
        return random.randint(0, 3)


scheduler = RoundRobinScheduler()
n = int(input("Enter number of processes: "))

for i in range(n):
    pid = i + 1
    arrival_time = scheduler.random_num_gen()
    burst_time = scheduler.random_num_gen() + 5
    rem_burst_time = burst_time
    scheduler.add_process(pid, rem_burst_time, burst_time, arrival_time)

scheduler.algorithm(n)