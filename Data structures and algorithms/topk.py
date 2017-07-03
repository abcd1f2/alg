#!/usr/bin/env python
# coding: utf-8

"""
@file: topk.py
@time: 2017/2/24 10:30
"""

"""
    calculate sort
"""
def calcu_sort(data_to_sort, array_to_count):
    for i in data_to_sort:
        array_to_count[i] += 1

    r = list()
    for i in xrange(0, len(array_to_count)):
        if array_to_count[i] > 0:
            times = 0
            while times < array_to_count[i]:
                r.append(i)
                times += 1
    return r

"""
    to do ...
"""

if __name__ == "__main__":
    data = [5, 8, 3, 6, 3, 4, 2, 8, 9, 2, 4, 6, 1, 7, 9]
    count_array = [0] * 10
    print calcu_sort(data, count_array)

