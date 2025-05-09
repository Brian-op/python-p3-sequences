#!/usr/bin/env python3

def print_fibonacci(length):
    a, b = 0, 1
    count = 0
    result = []

    while count < length:
        result += [a]  
        a, b = b, a + b
        count += 1

    print(result)