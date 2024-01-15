def mid(inw):
    length = len(inw)
    if length % 2 == 0:
        return ""
    else:
        midnum = length // 2
        return inw[midnum]
a = "asd"
b = "sdfa"
c = mid(a)
d = mid(b)
print(c)
print(d)