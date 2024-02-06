text = [1,2,3,4,5,6,7,8,9,10]

def divTwo():
    b =[]
    for i in text:
        if i %2 == 0:
            b.append(i)
            
    return b  
c = divTwo()    
print(c)