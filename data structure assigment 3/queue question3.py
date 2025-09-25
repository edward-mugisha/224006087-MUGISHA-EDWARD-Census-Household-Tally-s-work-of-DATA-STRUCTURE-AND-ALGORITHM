# Alg Step 0: imports
from collections import deque

# Alg Step 1: Input - customers in arrival order (front -> back)
arrivals = ["P1", "P2", "P3", "P4", "P5"]   # front is "P1"

SERVICE_TIME = 1.0   # assume fixed service time per customer (minutes)

# Alg Step 2: Simulate FIFO using a queue (deque)
queue = deque(arrivals)      # create a queue with arrival order       # Alg step 2
fifo_served = []             # will hold the served order under FIFO  # Alg step 2
fifo_wait = {}               # map customer -> waiting time (when service starts)
t = 0.0
while queue:                 # while there are customers in queue       # Alg step 2
    person = queue.popleft() # serve the front customer                 # Alg step 2
    fifo_served.append(person)
    fifo_wait[person] = t    # record when this person's service started
    t += SERVICE_TIME        # advance simulated time by one service

# Alg Step 3: Simulate LIFO using a stack (list)
stack = list(arrivals)       # stack with same arrival order (top = last item) # Alg step 3
lifo_served = []             # will hold the served order under LIFO        # Alg step 3
lifo_wait = {}
t = 0.0
while stack:                 # while stack not empty                       # Alg step 3
    person = stack.pop()     # pop: serve last arrival first               # Alg step 3
    lifo_served.append(person)
    lifo_wait[person] = t
    t += SERVICE_TIME

# Alg Step 4: Helpers to compute fairness metrics
def average_wait(wait_map):
    # average waiting time across customers (optional metric)
    return sum(wait_map.values()) / len(wait_map)

def inversion_count(arrival_list, served_order):
    # Count overtakes: for each pair (i<j) in arrival order,
    # increment if person i was served after person j.
    pos = {cust: idx for idx, cust in enumerate(served_order)}
    inv = 0
    n = len(arrival_list)
    for i in range(n):
        for j in range(i+1, n):
            if pos[arrival_list[i]] > pos[arrival_list[j]]:
                inv += 1
    return inv

# Alg Step 5: Compute metrics and compare
fifo_avg = average_wait(fifo_wait)          # optional
lifo_avg = average_wait(lifo_wait)          # optional
fifo_inv = inversion_count(arrivals, fifo_served)
lifo_inv = inversion_count(arrivals, lifo_served)

print("Arrivals (front->back):", arrivals)
print()
print("FIFO served order:", fifo_served)
print("FIFO waiting times (start-of-service):", fifo_wait)
print("FIFO average wait:", fifo_avg)
print("FIFO overtakes (inversions):", fifo_inv)
print()
print("LIFO served order:", lifo_served)
print("LIFO waiting times (start-of-service):", lifo_wait)
print("LIFO average wait:", lifo_avg)
print("LIFO overtakes (inversions):", lifo_inv)


What each algorithm step corresponds to in the code (explicit mapping)

Step 1 (Input) → arrivals = ["P1", ...] and SERVICE_TIME = 1.0.

Step 2 (FIFO simulation) → queue = deque(arrivals); the while queue: loop with queue.popleft() builds fifo_served and fifo_wait.

Step 3 (LIFO simulation) → stack = list(arrivals); the while stack: loop with stack.pop() builds lifo_served and lifo_wait.

Step 4 (Fairness metrics) → inversion_count() implements overtakes counting (important fairness metric). average_wait() computes an optional time-based metric.

Step 5 (Compare & output) → final prints showing served orders and fifo_inv vs lifo_inv.
