def add(a,b):
    ans = a + b
    print("add=", ans)

def sub(a,b):
    ans = a - b
    print("sub=", ans)

def mul(a,b):
    ans = a * b
    print("mul=", ans)

def div(a,b):
    ans = a / b
    print("div=", ans)

print('__name__=',__name__)
if __name__ == '__main__':#if '__main__' == '__main__':
    add(100,200)
    sub(100,200)
    mul(100,200)
    div(100,200)
