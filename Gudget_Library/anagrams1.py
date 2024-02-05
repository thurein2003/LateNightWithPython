def sorting(s):
    ls =sorted(s)
    ans = ''.join(ls)
    
    return ans

#---------------------------------
ansa =input("enter : ")
ansb =input("enter : ") 

if len(ansa) == len(ansb):
    c = sorting(ansa) 
    d = sorting(ansb)
    
    if c == d:
       print("True")
    else:
        print("False")

    