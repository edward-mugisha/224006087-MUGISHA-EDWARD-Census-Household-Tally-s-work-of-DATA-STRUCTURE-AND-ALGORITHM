import array

# ------------------------------------
# Integers: Generate household tallies
# ------------------------------------
household_counts = [3, 5, 2, 6, 4, 7, 3]  # Example data (family members per household)

total = sum(household_counts)
average = total / len(household_counts)
minimum = min(household_counts)
maximum = max(household_counts)

# ------------------------------------
# Strings: Create formatted report
# ------------------------------------
report = f"Total households tally: {total}, Average household size: {average:.2f}"
report2 = f"Minimum household size: {minimum}, Maximum household size: {maximum}"
print(report)
print(report2)

# ------------------------------------
# Booleans: Apply threshold condition
# ------------------------------------
threshold = 4
if average > threshold and maximum > 6:   # compound condition
    print("Above Standard")
else:
    print("Below Standard")

# ------------------------------------
# Lists: Manage household records
# ------------------------------------
print("\nOriginal household list:", household_counts)

# Add new household record
household_counts.append(8)

# Remove a household record if less than 3 members
household_counts = [h for h in household_counts if h >= 3]

# Sort the list
household_counts.sort()
print("Modified and sorted household list:", household_counts)

# ------------------------------------
# Arrays: Use Python's array module
# ------------------------------------
household_array = array.array('i', [3, 5, 2, 6, 4, 7, 3])
array_sum = sum(household_array)

print("\nSum of array:", array_sum)
print("Does list sum equal array sum?", array_sum == total)

# ------------------------------------
# Dictionaries: Build household records
# ------------------------------------
household_dicts = [
    {'id': 1, 'name': 'Smith', 'value': 3},
    {'id': 2, 'name': 'Johnson', 'value': 5},
    {'id': 3, 'name': 'Lee', 'value': 2},
]

# Update one record
household_dicts[1]['value'] = 6

# Add new record
household_dicts.append({'id': 4, 'name': 'Patel', 'value': 4})

# Delete one record
household_dicts = [d for d in household_dicts if d['id'] != 3]

# Compute total from dictionaries
dict_total = sum(d['value'] for d in household_dicts)

print("\nHousehold dictionary records:", household_dicts)
print("Total value from dictionaries:", dict_total)
