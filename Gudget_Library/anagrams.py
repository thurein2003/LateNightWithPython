ansa =input("enter : ")
ansb =input("enter : ") 


def looping(ansa, ansb):
    i = 0
    j = 0
    while i < len(ansa) and j < len(ansb):
        if ansa[i] != ansb[j]:
            return False
        elif ansa[i] == ansb[j]:
            i += 1
            j += 1
    return i == len(ansa) and j == len(ansb)           
       
print(looping(ansa,ansb))

    
    
    
    
    
    
    
    
    
    
    
