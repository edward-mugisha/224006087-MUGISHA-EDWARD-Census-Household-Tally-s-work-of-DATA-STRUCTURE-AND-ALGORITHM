from collections import deque

# Step 1: Clients arrive in order (queue: front -> back)
clients = deque(["C1", "C2", "C3", "C4"])
print("Initial Queue:", list(clients))

# Step 2: The first client in the queue
first_client = clients[0]   # front of the queue
print("First client at BK ATM:", first_client)


