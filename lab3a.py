# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-10-05 (September 12,088, 1993)
# Purpose: 
# Usage: ./lab3a.py
# MOTD: If you see something, say nothing, and drink to forget.

# Write a Python program that generates a sequence of 20 random values
# between 0 and 99, stores them in a list, prints the sequence, sorts it,
# and prints the sorted sequence.

import random

# Technicallly, this is all that's required:
# ls = [random.randint(0, 99) for i in range(21)]

# But I get the feeling that's not what you want.
ls = []
for i in range(21):
    ls.append(random.randint(0, 99))

print(f"{ls}")

# Sorts the sequence
ls.sort()

# Yes, that's it. In C++, Java, or indeed, most other languages
# you have to manipulate each individual element in the array directly.
# In Python, though, a list is just an array of pointers.

print(ls)