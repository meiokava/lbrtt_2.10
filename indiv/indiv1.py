# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def sum_pos(*args):
    """
    The sum of the arguments located up to the last positive argument
    """
    if args:
        values = [float(arg) for arg in args]
        sum_ = 0
        for num in values:
            if num >= 0:
                sum_ += num
            else:
                break
        return sum_


if __name__ == "__main__":
    print(f'sum positive arguments: {sum_pos(1, 2, 3, 4, 5, -6, 7, 8)}')
    print(f'sum positive arguments: {sum_pos(1.5, 4.6, -9.3, 8.0, 10.5)}')

