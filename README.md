
Project 65: Census Household Tally

1. Integers Section:
   - We start with a list of integers: [3, 5, 2, 6, 4, 7, 3].
   - These numbers represent household counts (e.g., number of people per household).
   - We compute:
       * Total = sum of the list.
       * Average = total divided by number of households.
       * Minimum = smallest household size.
       * Maximum = largest household size.

2. Strings Section:
   - We create two formatted f-strings to neatly display results.
   - Example: "Total households tally: 30, Average household size: 4.29"
   - This makes the output user-friendly.

3. Booleans Section:
   - We set a threshold = 4.
   - If the average household size is greater than 4 AND the maximum household size is greater than 6, print "Above Standard".
   - Otherwise, print "Below Standard".
   - This demonstrates the use of compound boolean conditions.

4. Lists Section:
   - Original list: [3, 5, 2, 6, 4, 7, 3].
   - Add a new household record with 8 members → list becomes [3, 5, 2, 6, 4, 7, 3, 8].
   - Remove households with fewer than 3 members → [3, 5, 6, 4, 7, 3, 8].
   - Sort the list → [3, 3, 4, 5, 6, 7, 8].
   - This shows adding, removing, and sorting data.

5. Arrays Section:
   - We use Python’s array module: array('i', [3, 5, 2, 6, 4, 7, 3]).
   - Compute the sum of the array → 30.
   - Compare array sum with list sum → both are equal, so it prints True.
   - This demonstrates fixed-size numeric storage.

6. Dictionaries Section:
   - We create a list of dictionaries, where each dictionary stores 'id', 'name', and 'value' (household size).
   - Example: {'id': 1, 'name': 'Smith', 'value': 3}
   - Update record: Johnson’s value changed from 5 → 6.
   - Add a new record: {'id': 4, 'name': 'Patel', 'value': 4}.
   - Delete record with id=3 (Lee).
   - Remaining records are Smith, Johnson, and Patel.
   - Compute the total from dictionaries: 3 + 6 + 4 = 13.

Conclusion:
This project shows how to work with different Python data types and structures (integers, strings, booleans, lists, arrays, and dictionaries) to process and report Census Household Tally data.
