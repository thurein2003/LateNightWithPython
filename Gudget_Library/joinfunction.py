def add_dots(a):
    aft = ".".join(a)
    return aft

def remove_dots(b):
    bef = b.replace(".", "")
    return bef

c = add_dots("hello")
d = remove_dots("world")
s = "helloworld"

print(c)  # Output: h.e.l.l.o
print(d)  # Output: world
print(s)  # Output: helloworld
