# A-Star-Magic-Moving-Square


This Python script implements an A* search algorithm to solve sliding puzzle problems, specifically for 3x3 and 4x4 grids. It utilizes heuristic functions to efficiently navigate through possible states of the puzzle. This was existing code that was heavily altred to meet the A* Moving Magic Square approach.

The existing code: https://github.com/cybr17crwlr/A-Star-8-puzzle-Python

## Components

- **Node Representation:** Each puzzle state is represented as a ```Node``` class, which contains methods for state manipulation, equality checking, and heuristic calculations.
- **Heuristic Functions:** Two heuristic functions are implemented to evaluate the closeness of a state to the goal.
- **Game Class:** The ```Game``` class manages the open and closed states during the solving process, implementing the A* algorithm to find the solution.

## Usage 

1. **Input File:** Prepare a text file (3x3_TestSq2.txt) containing the initial state of the puzzle in a linear format. For example, a 3x3 puzzle could look like this:
```
1
2
3
0
4
5
6
7
8
```
Here, ```0``` represents the blank tile.
Alternatively find other squared in the Test Cases folder. 

2. **Run the Script:** Execute the script from the command line:
```python3 nPuzzle.py```

3. **Output:** The program will output the number of visited nodes, heuristic calculations, and the final moves taken to solve the puzzle.


