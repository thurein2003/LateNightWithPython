def capital_indexes(input_string):
    indexes = []

    for index, char in enumerate(input_string):
        if char.isupper():
            indexes.append(index)

    return indexes

# Example usage:
input_str = "HeLlO"
result = capital_indexes(input_str)
print(result)
