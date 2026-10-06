# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-10-06 (September 12,089 1993)
# Purpose: 
# Usage: ./lab3g.py

ls = []
while len(ls) < 6:
    n = None
    try:
        n = int(input("Input a number:\n> "))
    except ValueError:
        print("Please input an actual number.")
        pass
    if n:
        ls.append(n)

# Now, let's do this.
ls = [n * 10 for n in ls]

# Wait, in reverse order, or in *reversed* order? I'll do both.
print(f"Reverse:\t{sorted(ls, reverse=True)}")
print(f"Reversed:\t{list(reversed(ls))}")