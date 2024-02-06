def checker(words):
    if words == words[::-1] :
        return True
    else: 
        return False
req =input("Enter a words : ")
print(checker(req))

