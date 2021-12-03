from collections import Counter
from copy import copy
import re


def gcd(a: int, b: int) -> (int, int):
    # Swapping `a` and `b`
    if a < b:
        a, b = b, a

    iter = 0
    while b > 0:
        iter += 1
        # An iteration of calculation
        # print(f'przed a= {a}, b={b}')
        a, b = b, a % b
        # print(f'po    a= {a}, b={b}')

    return a, iter


def shuffle_nums(div, iter):
    if iter == 0:
        return div, iter
    for x in range(div * iter, 10000*div, div):
        for y in range(x // 2, x, div):
            if gcd(x, y) == (div, iter):
                return x, y
    return -1, -1

if __name__ == '__main__':
    # divisor = 4
    # iterations = 3
    # a, b = divisor, divisor * 2
    # for _ in range(iterations + 0):oczywiście 2 bramki ronldo
    #     a, b = b, a + b
    # print(a, b)
    print(shuffle_nums(13, 13))
    print(shuffle_nums(13, 14))
    print(shuffle_nums(2, 3))

    print(gcd(24, 68))
