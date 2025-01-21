# Blind-Valley
This code tries to find the perfect valley for out trip using recurison
The game is a grid-based puzzle where players select cells to eliminate groups of connected numbers. When a group is selected, those cells are replaced with empty spaces, and the remaining numbers shift downward and leftward to fill gaps. The player's goal is to maximize their score, which increases based on the size of the eliminated groups and the value of the numbers. The game ends when no more groups of connected numbers remain.

The game features a recursive backtracking mechanism that ensures all connected cells with the same number are eliminated in a single move. The grid dynamically updates after each move, with gaps filled by shifting numbers downward and leftward. Players interact with the game by selecting rows and columns, ensuring that all moves are valid. A scoring system awards points based on the numbers and size of the eliminated groups, encouraging strategic gameplay. The game concludes when no connected groups of numbers remain, marking the end of the session.

input example:
2 -1 -1 //left col
-1 -1 2 //right col
-1 2 -1 -1 //top row
-1 -1 -1 0 //bottom row
L R L R
U U L R
D D L R

output example of filled valley:,
B H B H
H B N N
B H B H
