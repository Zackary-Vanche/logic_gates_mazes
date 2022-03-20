# logic_gates_mazes

The folder logic_gates_mazes_executable contains the compiled code, and the application.
  The game only needs this folder to work.
  To launch the game :
	  Double-click on logic_gates_mazes_executable/logic_gates_maze/logic_gates_maze.exe. 
	  	(A shortcut is also available in logic_gates_mazes_executable)
	  A window will open.
	  Click once on that window.
	  The game starts.
solutions.txt contains the solutions of each level.

What comes next is only usefull if you want to develop the game.
It is useless if you only want to play.

I used PyInstaller to compile the game in a .exe.
The line used to do so is :
pyinstaller C:\Users\utilisateur\Documents\github\logic_gates_mazes\logic_gates_mazes_python_code\logic_gates_mazes_main.py --distpath C:\Users\utilisateur\Documents\github\logic_gates_mazes\logic_gates_mazes_executable --icon=C:\Users\utilisateur\Documents\github\logic_gates_mazes\icone.ico

In the folder logic_gates_mazes_python_code is the python code that needs to be compiled.
  The game doesn't need this folder to work.