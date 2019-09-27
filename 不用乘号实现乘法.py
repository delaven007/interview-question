
def add(a,b):
    if a==0:
        return b
    return add((a&b)<<1,a^b)



def mul(a,b):
    s=0
    while b:
        if b&1:
            s=add(s,a)
        a=a<<1
        b=b>>1
    return s

print(mul(2,3))


