# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: 
# Usage: ./lab3f.py

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# matrix = [[3 * x + y + 1 for y in range(3)] for x in range(3)]

print(matrix[1][1])     # Prints the element `5`
print(matrix[0][1])     # Prints the element `2`
print(matrix[2][2])     # Prints the element `9`

for m in matrix:
    print(str(m).replace(' ', ''))