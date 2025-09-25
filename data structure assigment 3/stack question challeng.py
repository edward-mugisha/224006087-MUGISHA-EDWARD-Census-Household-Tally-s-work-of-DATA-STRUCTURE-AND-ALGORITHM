




input_str = "QUEUEORDER"         # Step 1: the queue contents (front->back)

stack = []                       # Step 2: create empty stack

# Step 3: push each character from the queue onto the stack
for ch in input_str:
    stack.append(ch)             # push (append) -> top grows to the right

# Step 4: pop all characters from the stack to build the reversed string
reversed_chars = []
while stack:                     # while stack is not empty
    reversed_chars.append(stack.pop())  # pop LIFO and collect

reversed_str = ''.join(reversed_chars)  # Step 5: finalize string

print("Original:", input_str)
print("Reversed:", reversed_str)
                                                                               


input_str = "QUEUEORDER" → (Alg. step 1) defines the queue contents.

stack = [] → (Alg. step 2) initializes an empty stack (Python list).

for ch in input_str: → begins iterating the queue from front to back.

stack.append(ch) → (Alg. step 3) push: each character is pushed onto the stack.

reversed_chars = [] → prepares a list to collect popped characters.

while stack: → loop until the stack is empty.

reversed_chars.append(stack.pop()) → (Alg. step 4) pop the top character and append it to result list.

reversed_str = ''.join(reversed_chars) → (Alg. step 5) join popped characters into a single string.

print(...) → shows original and reversed strings.