a = input('Insert size of a side\n')
b = input('Insert size of b side\n')
c = input('Insert size of c side\n')

def is_triangle():
    if int(a)>=int(b)+int(c) or int(b)>=int(a)+int(c) or int(c)>=int(a)+int(b):
        print('No')
    else:
        print('Yes')

is_triangle()