#Banker's Algorithm Implementation
r = int(input("resources: "))
instance = []
for i in range(r):
    x = int(input(f"R{i+1}: "))
    instance.append(x)
print("Total instances:", instance)

p = int(input("Processes: "))

#max need
max_need = []
for i in range(p):
    s = list(map(int, input(f"Max need for P{i}: ").split()))
    max_need.append(s)
print("Max Need Matrix:")
# for row in max_need:
#     print(row)

# allocated
allocated = []
for i in range(p):
    s = list(map(int, input(f"Allocated for P{i}: ").split()))
    allocated.append(s)
print("Allocated Matrix:")
for row in allocated:
    print(row)

#current need
cur_need = []
for i in range(p):
    need_row = []
    for j in range(r):
        need = max_need[i][j] - allocated[i][j]
        need_row.append(need)
    cur_need.append(need_row)

print("Current Need Matrix:")
for row in cur_need:
    print(row)

#available resources
total_allocated = list(map(sum,zip(*allocated)))
av_r = []
for i in range (r):
    av_r.append(instance[i] - total_allocated[i])

work = av_r[:]  # Copy of available resources
finish = [False] * p
safe_sequence = []

# Store available resources at each step
available_resources_list = []
available_resources_list.append(av_r[:])  # Initial available

# Find safe sequence
for _ in range(p):
    for i in range(p):
        if not finish[i]:
            # Check if process can execute
            can_allocate = True
            for j in range(r):
                if cur_need[i][j] > work[j]:
                    can_allocate = False
                    break
            
            if can_allocate:
                # Process finishes, release its resources
                for j in range(r):
                    work[j] += allocated[i][j]
                finish[i] = True
                safe_sequence.append(f"P{i}")
                
                # Store current available resources
                available_resources_list.append(work[:])

# Check if safe state exists
if all(finish):
    # Print available resources at each step FIRST
    print("\nAvailable resources at each step:")
    print(f"Initial: {available_resources_list[0]}")
    for i in range(len(safe_sequence)):
        print(f"After P{safe_sequence[i][1:]}: {available_resources_list[i+1]}")
    
    # Then print safe sequence
    print("\nSafe sequence exists: ", end="")
    print(" -> ".join(safe_sequence))
else:
    print("\nNo safe sequence exists (unsafe state)")