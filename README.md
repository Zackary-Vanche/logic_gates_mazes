# Logic Gates Mazes

This project is a logic game that involves elements of boolean logic, graph theory, combinatorics, arithmetic, and algorithmics, as well as concepts from other areas of discrete and continuous mathematics and computer science. Players must use logical reasoning, problem-solving skills, and mathematical concepts to solve mazes and get to the exit. 

The levels are more or less organized by increasing complexity (sometimes easy levels are after hard ones, so don't hesitate to skip some and go see further).

## Prerequisites

Before running the project, make sure you have the following dependencies installed:

- [Python 3.x](https://www.python.org/)
- [Pygame](https://www.pygame.org/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)

You can install python packages using `pip`:

```bash
pip install pygame pyautogui
```

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/Zackary-Vanche/logic_gates_mazes.git
```

You can also simply [download the repository](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives).

2. Navigate to the project directory:

```bash
cd logic_gates_mazes
```

## Usage

To start the application, run the following command from the project root:

```bash
python src/main.py
```

This will launch the program.

## Concepts used in the game

The folowing concepts are used in the game:
- Boolean logic, boolean satisfiability problem (3SAT and many other levels)
- Some of Karp's 21 NP-complete problems (hitting set, independent set, knapsack, ...)
- Graph theory problems (graph coloring, dominating set, minimum spanning tree research, ...)
- Pathfinding problems with constraints (walks, trails, path, Eulerian paths, hamiltonian paths, travelling salesman)
- Problems based on permutations (15 puzzle, tower of Hanoi, oval track puzzle, panex, superpremutations...)
- Chess based enigmas (Knight's tour problem, First and second Guarini problems, 8 queens problem, ...)
- Rotations in 3 and 4 dimensions problems
- Cellular automaton
- Some knowns solitary games (sudoku, the baguenaudier game, takuzu, mastermind, river crossing enigma, nonograms, the solitaire game, lights out game, sujiko, zebra puzzle, magic squares, water pouring enigma, zebra enigma)
- Many sorting algorithms (bubble sort, cocktail sort, odd even sort, gnome sort, cycle sort, merge sort, selection sort, insertion sort, heap sort, panckake sorting)
- Egyptian fractions, polynomial equations, matrix inversion, taxicab numbers
- Eratosthenes algorithm, euclidian algorithm
- Ferrers diagrams, Young tableaux
- Integer factorization, integer partition
- Fibonacci sequence
- Equations to solve where you have to figure the numbers used in an addition (level Quaternary)
- Some levels generated randomly

This list is not exhaustive.

## Contributing

Feel free to contribute by opening issues or submitting pull requests if you think of anything that might improve the game.

I mainly need to work on:
- the gameplay.  
(The gameplay is actually the part I don't like to work on...)
  - A better name would be great.  
  - I would like to add a more user friendly representation of the logical expressions (They could be represented as trees.). I think the best would be to let the user switch between the two representations (equations and trees).  
  - I would like to create a map-menu where the user can choose between levels, rather than just a list of all levels.  
  - I also think of adding elements that don't contribute to the game (like representations of graphs that are hidden in the equations) but that help the player understand what is happening.  
  - And also, making the game less static would be great.  
- making the game easier to install.  
I can export the game as a .exe with PyInstaller, but then it is much to heavy, so I need to find another solution.

## Inspiration

The games The Witness and [Chromagraph](https://adam-rumpf.github.io/games/chromagraph.html) gave me a lot of ideas for graph-theory oriented levels.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](https://github.com/Zackary-Vanche/logic_gates_mazes/blob/main/LICENSE) file for details.
