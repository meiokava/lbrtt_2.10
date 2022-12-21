#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def aver_harm(*args):
    if args:
        values = [float(arg) for arg in args]
        sz = len(args)
        s = 0
        for arg in values:
            s += 1 / arg
        g = sz / s
        return g
    else:
        return None


if __name__ == "__main__":
    print(f'harmonic mean is: {aver_harm(1, 2, 3, 4, 5, 6, 7, 8)}')
    print(f'harmonic mean is: {aver_harm()}')
    print(f'harmonic mean is: {aver_harm(1.5, 4.6, 9.3, 8.0, 10.5)}')
