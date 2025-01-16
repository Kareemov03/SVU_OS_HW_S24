
# FIFO Page Replacement Algorithm

This project implements the **First-In-First-Out (FIFO)** page replacement algorithm, simulating virtual memory management.

---

## Features

- **Simulates FIFO page replacement**: Displays page fault occurrences and the state of the page table after each request.
- **User inputs**: Virtual memory size, page size, and the sequence of page requests.
- **Summary output**: Includes the total number of page faults and the final state of the memory.

---

## Requirements

- Python 3.6 or later

---

## Usage

1. Run the script using Python:

   ```bash
   python BSO_Task_2_kareem_215608.py
   ```

2. Follow the interactive prompts:
   - Enter the **virtual memory size**.
   - Specify the **page size**.
   - Provide the **page sequence** (as a string of digits, e.g., `12345`).

---

## Example

### Input:
```
Virtual Memory Size: 20
Page Size: 4
Page Sequence: 123435126
```

### Output:
```
Page Requests	Memory State
		  0       ['1']
        1       ['1', '2']     
        2       ['1', '2', '3']
        3       ['1', '2', '3', '4']
        4       ['1', '2', '3', '4']
        5       ['1', '2', '3', '4', '5']
        6       ['1', '2', '3', '4', '5']
        7       ['1', '2', '3', '4', '5']
        8       ['2', '3', '4', '5', '6']

Number of Fault Requests: 6
       Page       Table : ['1', '2', '3', '4', '5', '6']
```

---


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
