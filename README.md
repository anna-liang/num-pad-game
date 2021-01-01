# Number Pad Game

On a number pad, we can travel from one number to another as long as they are adjacent (including diagonally).
From 1, it is allowed to travel to 2, 4, and 5.

Number Pad Game is a solution to this problem. Given a starting number on a number pad and the number of steps to take, the program outputs all travel possibilities in sequential order.

## Example
1. start = 1, steps = 1
                    [
                    [1, 2], 
                    [1, 4], 
                    [1, 5]
                    ]
2. start = 1, steps = 2 
                    [
                    [1, 2, 1], [1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 2, 6],
                    [1, 4, 1], [1, 4, 2], [1, 4, 5], [1, 4, 7], [1, 4, 8],
                    [1, 5, 1], [1, 5, 2], [1, 5, 3], [1, 5, 4], [1, 5, 6], [1, 5, 7], [1, 5, 8], [1, 5, 9]
                    ]

## Usage
```bash
python numPadGame.py <start> <steps>
```
