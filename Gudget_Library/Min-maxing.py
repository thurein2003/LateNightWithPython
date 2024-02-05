a = int(input("enter your number: "))
b = int(input("Enter second number: "))
c = int(input("Enter a third number: "))

list =list([a,b,c])

    
def largest_different(list):
    final_result = sorted(list)
    final_result = list[2] - list[0]
    
    return final_result
ld = largest_different(list)
print(ld)
    