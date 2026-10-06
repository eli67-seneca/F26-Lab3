#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-10-15 (September 12,088, 1993)
# Purpose: 
# Usage: ./lab3b.py

# Write a function that reverses the sequence of elements in a list.

def reverse_list(ls):
    """Well, you did say write a *function*. """
    return list(reversed(ls))

if __name__ == "__main__":
    ls = input("Input a list of numbers:\n> ")
    if ls:
        ls = [int(i) for i in ls.split(' ')]
    else:
        # Load example list
        ls = [1, 4, 9, 16, 9, 7, 4, 9, 11]

    print(reverse_list(ls))