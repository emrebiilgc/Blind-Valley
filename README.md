# Blind-Valley
This code tries to find the perfect valley for out trip using recurison
The game is a grid-based puzzle where players select cells to eliminate groups of connected numbers. When a group is selected, those cells are replaced with empty spaces, and the remaining numbers shift downward and leftward to fill gaps. The player's goal is to maximize their score, which increases based on the size of the eliminated groups and the value of the numbers. The game ends when no more groups of connected numbers remain.

Key Features:

Recursive Backtracking: Ensures all connected cells with the same number are eliminated in one move.
Dynamic Grid Updates: Gaps are filled by shifting numbers downward and leftward.
Player Interaction: Players choose rows and columns, ensuring valid moves.
Scoring System: Points are earned based on the numbers and size of eliminated groups.
End Condition: The game ends when no connected groups are left.
