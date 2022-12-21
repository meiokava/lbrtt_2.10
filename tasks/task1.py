#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def aver_geom(*args):
    if args:
        values = [float(arg) for arg in args]
        n = 1
        sz = len(args)
        for arg in values:
            n = n * arg
        g = math.pow(n, 1 / sz)
        return g
    else:
        return None


if __name__ == "__main__":
    print(f'geometric mean is: {aver_geom(1, 2, 3, 4, 5, 6, 7)}')
    print(f'geometric mean is: {aver_geom()}')
    print(f'geometric mean is: {aver_geom(2.3, 6.5, 9.2, 3.4)}')
