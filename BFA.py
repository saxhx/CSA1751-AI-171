def best_fit(partition_sizes, process_sizes):
    n = len(partition_sizes)  # Number of memory partitions
    m = len(process_sizes)    # Number of processes

    # To store the allocation of each process (-1 means not allocated)
    allocation = [-1] * m

    # Go through each process and find the best fit partition for it
    for i in range(m):
        # Initialize the index of the best fit partition
        best_fit_index = -1

        for j in range(n):
            # If the partition can fit the process and is the smallest possible fit
            if partition_sizes[j] >= process_sizes[i]:
                if best_fit_index == -1 or partition_sizes[j] < partition_sizes[best_fit_index]:
                    best_fit_index = j
        
        # If we found a valid partition, allocate the process to it
        if best_fit_index != -1:
            allocation[i] = best_fit_index
            partition_sizes[best_fit_index] -= process_sizes[i]

    return allocation

# Sample input and output
partition_sizes = [100, 500, 200, 300, 600]
process_sizes = [212, 417, 112, 426]

allocation = best_fit(partition_sizes, process_sizes)

# Display results
print("Process No.\tProcess Size\tPartition No.")
for i in range(len(process_sizes)):
    if allocation[i] != -1:
        print(f"{i + 1}\t\t{process_sizes[i]}\t\t{allocation[i] + 1}")
    else:
        print(f"{i + 1}\t\t{process_sizes[i]}\t\tNot Allocated")