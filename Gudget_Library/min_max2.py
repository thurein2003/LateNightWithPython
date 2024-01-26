def largest_difference(numbers):
    # Check if the list is not empty
    if not numbers:
        return None  # Return None for an empty list

    # Find the maximum and minimum values in the list
    max_number = max(numbers)
    min_number = min(numbers)

    # Calculate the difference
    difference = max_number - min_number

    return difference

# Example usage:
numbers_list = [1, 2, 3]
result = largest_difference(numbers_list)
print(result)  # Output: 2
