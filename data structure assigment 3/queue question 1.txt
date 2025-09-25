from collections import deque

# Step 1: Patients arrive in order (queue: front -> back)
patients = deque(["P1", "P2", "P3", "P4", "P5", "P6"])
print("Initial Queue:", list(patients))

# Step 2: Serve the first two patients (dequeue twice)
patients.popleft()   # P1 served
patients.popleft()   # P2 served
print("Queue after serving 2 patients:", list(patients))

# Step 3: Check the new front
front_patient = patients[0]   # front of the queue
print("Front patient now:", front_patient)

