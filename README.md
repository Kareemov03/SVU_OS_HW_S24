# CPU Scheduling Algorithms

This project implements three fundamental CPU scheduling algorithms:

1. **First Come First Served (FCFS)**
2. **Shortest Job Next (SJN)**
3. **Round Robin (RR)**

It provides a menu-based interface for users to simulate these algorithms with custom inputs and view results, including Gantt charts and average times.

---

## Features

- **Interactive input**: Users can define the number of processes, arrival times, burst times, and (for Round Robin) the time quantum.
- **Gantt Chart**: Displays the execution order of processes.
- **Performance Metrics**: Average Turnaround Time and Average Waiting Time for each algorithm.

---

## Requirements

- Python 3.6 or later

---

## Usage

1. Run the script using Python:

   ```bash
   python BSO_kareem_215608.py
   ```

2. Follow the interactive prompts:
   - Input the number of processes.
   - Enter arrival and burst times for each process.
   - For Round Robin, specify the quantum time.
   - Choose an option from the menu to simulate a specific algorithm or compare all.

---

## Example

### Input:
```
Number of processes: 3
Process 1 Arrival Time: 0
Process 1 Burst Time: 5
Process 2 Arrival Time: 1
Process 2 Burst Time: 3
Process 3 Arrival Time: 2
Process 3 Burst Time: 8
Round Robin Quantum Time: 2
```

### Output:
#### First Come First Served
```
Gantt Chart:
         | P1 | P2 | P3 |
         0    5    8    16

Average Turnaround Time: 8
Average Waiting Time:   4
```

#### Shortest Job Next
```
Gantt Chart:
         | P1 | P2 | P3 |
         0    5    8    16

Average Turnaround Time: 8
Average Waiting Time:   4
```

#### Round Robin
```
Gantt Chart:
         | P1 | P2 | P3 | P1 | P2 | P3 | P1 | P3 | P3 |
         0    2    4    6    8    9    11   12   14   16

Average Turnaround Time: 9
Average Waiting Time:   5
```

---


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
