

def swaper(fun):
    def swap(a,b):
        if a<b:
            a,b = b, a
            return fun(a, b)
        return fun(a, b)

    return swap

@swaper
def sub(a,b):
    print(a-b)

sub(1, 2)