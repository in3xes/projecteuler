#!/usr/bin/env python

"""Project Euler, problem 174

We shall define a square lamina to be a square outline with a square "hole" so
that the shape possesses vertical and horizontal symmetry.

Given eight tiles it is possible to form a lamina in only one way: 3x3 square
with a 1x1 hole in the middle. However, using thirty-two tiles it is possible
to form two distinct laminae.

If t represents the number of tiles used, we shall say that t = 8 is type L(1)
and t = 32 is type L(2).

Let N(n) be the number of t <= 1000000 such that t is type L(n); for example,
N(15) = 832.

What is sum(N(n)) for 1 <= n <= 10?
"""

from math import ceil
from collections import defaultdict

def gen_laminae(limit):
    """Yield laminae with up to limit squares, as tuples
    (outer, inner, squares)"""
    for outer in range(3, limit // 4 + 2):
        if outer & 1:
            min_min_inner = 1
        else:
            min_min_inner = 2
        min_inner_squared = outer ** 2 - limit
        if min_inner_squared < 0:
            min_inner = min_min_inner
        else:
            min_inner = max(min_min_inner, int(ceil(min_inner_squared ** 0.5)))
            if outer & 1 != min_inner & 1:
                min_inner += 1
        outer_squared = outer ** 2
        for inner in range(min_inner, outer - 1, 2):
            squares = outer_squared - inner ** 2
            yield (outer, inner, squares)

def main():
    squares_to_count = defaultdict(int)
    for (outer, inner, squares) in gen_laminae(1000000):
        squares_to_count[squares] += 1
    histogram = defaultdict(int)
    for val in squares_to_count.values():
        if val <= 10:
            histogram[val] += 1
    print sum(histogram.values())

if __name__ == "__main__":
    main()
