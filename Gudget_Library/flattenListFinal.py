def flatten(lst):
    return [item for sublist in lst for item in sublist]

result = flatten([[1,2],[3,4]])
print(result)