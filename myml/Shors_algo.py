"""import random
import math
def shor_algo(n):
    while True:
        x= random.randint(2,n-1)
        d=math.gcd(x,n)
        if d>=2:
            return d,n//d
        r= 1
        while pow(x,r,n)!=1:
            r+=1
        if r%2 == 0:
            d = math.gcd(pow(x,r//2)-1,n)
            if d >= 2:
                return d, n//d
print(shor_algo(15))"""


def show_shor():

    import sys
    from .code_viewer import show_code18

    module = sys.modules[__name__]

    show_code18(module)