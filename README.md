# NumberPuzzle
Algorythm to find solution of 'Number Puzzle' - logic game by Professor Puzzle (R) [https://professorpuzzle.com/products/puzzles/einstein/number-puzzle/]
![puzzle](https://user-images.githubusercontent.com/6569984/211147053-3c5defdf-7c0b-42fb-83f3-e276e0f9ff12.jpg)

- It arranges the numbers so that each line – horizontal, vertical and corner-to-corner diagonal – adds up to 264.
- Each number is expressed as base + adder, e.g. 81 = 10*(6+2) + 1*(6-5), where 6 is a base and 2 & -5 are adders to tens and units respectively
- In first step (fill_U) script tries to find all valid matrixes of 'unit adders' U which meet requirement of unique adders in each column, row and diagonal. Script stores indexes of adders instead of adders themselves (In 'tens adders' matrix T indexes grow with each row from 0 to 3)
- In next step (sort_U) elements in U & T are shuffle within each column (excluding elements on diagonal) and if above requirement is met, solution is calculated and checked again, also for matrix rotated by 180 deg.

For assumptions:
```python
base = 6
adder = [-5,0,2,3]
sum = 264
```
code gives back 48 solutions:

	19. 98. 66. 81
	86. 61. 99. 18
	91. 16. 88. 69
	68. 89. 11. 96
	---------------
	19. 88. 96. 61
	91. 66. 18. 89
	68. 99. 81. 16
	86. 11. 69. 98
	---------------
	18. 89. 96. 61
	91. 66. 19. 88
	69. 98. 81. 16
	86. 11. 68. 99
	---------------
	18. 99. 66. 81
	86. 61. 98. 19
	91. 16. 89. 68
	69. 88. 11. 96
	---------------
	19. 96. 68. 81
	88. 61. 99. 16
	91. 18. 86. 69
	66. 89. 11. 98
	---------------
	19. 86. 98. 61
	91. 68. 16. 89
	66. 99. 81. 18
	88. 11. 69. 96
	---------------
	16. 89. 98. 61
	91. 68. 19. 86
	69. 96. 81. 18
	88. 11. 66. 99
	---------------
	16. 99. 68. 81
	88. 61. 96. 19
	91. 18. 89. 66
	69. 86. 11. 98
	---------------
	18. 96. 69. 81
	89. 61. 98. 16
	91. 19. 86. 68
	66. 88. 11. 99
	---------------
	18. 86. 99. 61
	91. 69. 16. 88
	66. 98. 81. 19
	89. 11. 68. 96
	---------------
	16. 88. 99. 61
	91. 69. 18. 86
	68. 96. 81. 19
	89. 11. 66. 98
	---------------
	16. 98. 69. 81
	89. 61. 96. 18
	91. 19. 88. 66
	68. 86. 11. 99
	---------------
	19. 98. 61. 86
	81. 66. 99. 18
	96. 11. 88. 69
	68. 89. 16. 91
	---------------
	19. 88. 91. 66
	96. 61. 18. 89
	68. 99. 86. 11
	81. 16. 69. 98
	---------------
	18. 89. 91. 66
	96. 61. 19. 88
	69. 98. 86. 11
	81. 16. 68. 99
	---------------
	18. 99. 61. 86
	81. 66. 98. 19
	96. 11. 89. 68
	69. 88. 16. 91
	---------------
	19. 91. 68. 86
	88. 66. 99. 11
	96. 18. 81. 69
	61. 89. 16. 98
	---------------
	19. 81. 98. 66
	96. 68. 11. 89
	61. 99. 86. 18
	88. 16. 69. 91
	---------------
	11. 89. 98. 66
	96. 68. 19. 81
	69. 91. 86. 18
	88. 16. 61. 99
	---------------
	11. 99. 68. 86
	88. 66. 91. 19
	96. 18. 89. 61
	69. 81. 16. 98
	---------------
	18. 91. 69. 86
	89. 66. 98. 11
	96. 19. 81. 68
	61. 88. 16. 99
	---------------
	18. 81. 99. 66
	96. 69. 11. 88
	61. 98. 86. 19
	89. 16. 68. 91
	---------------
	11. 88. 99. 66
	96. 69. 18. 81
	68. 91. 86. 19
	89. 16. 61. 98
	---------------
	11. 98. 69. 86
	89. 66. 91. 18
	96. 19. 88. 61
	68. 81. 16. 99
	---------------
	19. 96. 61. 88
	81. 68. 99. 16
	98. 11. 86. 69
	66. 89. 18. 91
	---------------
	19. 86. 91. 68
	98. 61. 16. 89
	66. 99. 88. 11
	81. 18. 69. 96
	---------------
	16. 89. 91. 68
	98. 61. 19. 86
	69. 96. 88. 11
	81. 18. 66. 99
	---------------
	16. 99. 61. 88
	81. 68. 96. 19
	98. 11. 89. 66
	69. 86. 18. 91
	---------------
	19. 91. 66. 88
	86. 68. 99. 11
	98. 16. 81. 69
	61. 89. 18. 96
	---------------
	19. 81. 96. 68
	98. 66. 11. 89
	61. 99. 88. 16
	86. 18. 69. 91
	---------------
	11. 89. 96. 68
	98. 66. 19. 81
	69. 91. 88. 16
	86. 18. 61. 99
	---------------
	11. 99. 66. 88
	86. 68. 91. 19
	98. 16. 89. 61
	69. 81. 18. 96
	---------------
	16. 91. 69. 88
	89. 68. 96. 11
	98. 19. 81. 66
	61. 86. 18. 99
	---------------
	16. 81. 99. 68
	98. 69. 11. 86
	61. 96. 88. 19
	89. 18. 66. 91
	---------------
	11. 86. 99. 68
	98. 69. 16. 81
	66. 91. 88. 19
	89. 18. 61. 96
	---------------
	11. 96. 69. 88
	89. 68. 91. 16
	98. 19. 86. 61
	66. 81. 18. 99
	---------------
	18. 96. 61. 89
	81. 69. 98. 16
	99. 11. 86. 68
	66. 88. 19. 91
	---------------
	18. 86. 91. 69
	99. 61. 16. 88
	66. 98. 89. 11
	81. 19. 68. 96
	---------------
	16. 88. 91. 69
	99. 61. 18. 86
	68. 96. 89. 11
	81. 19. 66. 98
	---------------
	16. 98. 61. 89
	81. 69. 96. 18
	99. 11. 88. 66
	68. 86. 19. 91
	---------------
	18. 91. 66. 89
	86. 69. 98. 11
	99. 16. 81. 68
	61. 88. 19. 96
	---------------
	18. 81. 96. 69
	99. 66. 11. 88
	61. 98. 89. 16
	86. 19. 68. 91
	---------------
	11. 88. 96. 69
	99. 66. 18. 81
	68. 91. 89. 16
	86. 19. 61. 98
	---------------
	11. 98. 66. 89
	86. 69. 91. 18
	99. 16. 88. 61
	68. 81. 19. 96
	---------------
	16. 91. 68. 89
	88. 69. 96. 11
	99. 18. 81. 66
	61. 86. 19. 98
	---------------
	16. 81. 98. 69
	99. 68. 11. 86
	61. 96. 89. 18
	88. 19. 66. 91
	---------------
	11. 86. 98. 69
	99. 68. 16. 81
	66. 91. 89. 18
	88. 19. 61. 96
	---------------
	11. 96. 68. 89
	88. 69. 91. 16
	99. 18. 86. 61
	66. 81. 19. 98
	---------------
