input_a = input('Insert a\n')
input_b = input('Insert b\n')
input_c = input('Insert c\n')
input_n = input('Insert n\n')

def check_fermat():
    a = int(input_a)
    b = int(input_b)
    c = int(input_c)
    n = int(input_n)

    if n > 2:
        if math.pow(a,n) + math.pow(b,n) == math.pow(c,n):
            print('Holy smokes, Fermat was wrong!')
        else:
            print("No, that doesn't work")

check_fermat()
