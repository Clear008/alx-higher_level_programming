#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x1 = 0
    x2 = 0
    if len(tuple_a) - 1 >= 0:
        x1 += tuple_a[0]
    if len(tuple_b) - 1 >= 0:
        x1 += tuple_b[0]
    if len(tuple_a) - 1 >= 1:
        x2 += tuple_a[1]
    if len(tuple_b) - 1 >= 1:
        x2 += tuple_b[1]
    return (x1, x2)
