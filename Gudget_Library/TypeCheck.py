def only_ints(a,b):
    c = type(a)
    d = type(b)
    if c == int and d == int:
        print("True")
    else :
        print("False")
only_ints(1,2)
only_ints("df",1)