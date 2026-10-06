# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-10-06 (September 12,089 1993)
# Purpose: Practice adding and removing elements in list.
# Usage: ./lab3d.py

mylist = list(range(1, 7))
mylist.append(7)
mylist.insert(0, 0)
mylist.pop(2)
print(mylist)
print(f"The element 6 is present at the index {mylist.index(6)}")