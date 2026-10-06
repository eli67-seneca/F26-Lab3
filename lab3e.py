# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026 10-26 (September 12,089 1993)
# Purpose:
# Usage: ./lab3e.py

students = ["Ama", "Elina", "Maija", "Daniel", "Ibrahim"]
students[1] = "Maggy"

for s in students:
    print(s)

# This also works:
# print(*students, sep='\n')