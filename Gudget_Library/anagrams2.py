def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted characters of both strings are the same
    return sorted(str1) == sorted(str2)

# Test cases
result1 = is_anagram("typhoon", "opython")
result2 = is_anagram("Alice", "Bob")

print(result1)  # Should print True
print(result2)  # Should print False
