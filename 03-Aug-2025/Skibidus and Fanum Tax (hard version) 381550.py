# Problem: Skibidus and Fanum Tax (hard version) - http://codeforces.com/problemset/problem/2065/C2

from bisect import bisect_right

# Number of test cases
T = int(input())

for _ in range(T):
    # Read n and m
    length_of_a, length_of_b = map(int, input().split())
    
    # Read the arrays
    original_array = list(map(int, input().split()))
    modifier_array = list(map(int, input().split()))
    
    # Sort the modifier array for binary search
    modifier_array.sort()
    
    # We assume it's possible until we find a reason it's not
    is_possible_to_sort = True
    
    # Step 1: Start from the last element — no element comes after it, so we safely modify it if needed
    last_index = length_of_a - 1
    original_array[last_index] = max(
        original_array[last_index],
        modifier_array[-1] - original_array[last_index]
    )

    # Step 2: Walk from second-to-last to the start
    for current_index in range(length_of_a - 2, -1, -1):
        current_value = original_array[current_index]
        next_value = original_array[current_index + 1]

        # Binary search: Find the first b[j] > current + next
        insertion_point = bisect_right(modifier_array, current_value + next_value)
        
        # No valid b[j] found AND there's an inversion we can't fix
        if insertion_point == 0 and current_value > next_value:
            is_possible_to_sort = False
            break
        
        # If there's an inversion, or we can improve current_value to help earlier values
        elif current_value > next_value or (
            insertion_point > 0 and current_value < modifier_array[insertion_point - 1] - current_value
        ):
            best_bj = modifier_array[insertion_point - 1]
            modified_value = best_bj - current_value
            original_array[current_index] = modified_value

    
    print("YES" if is_possible_to_sort else "NO")
