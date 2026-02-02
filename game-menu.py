import subprocess
from pathlib import Path

print("Welcome!")
print("Select")
print("1 for Tic Tac Toe")
print("2 for Guess The Number")
print("3 for Sudoku")
print("4 to Quit")
script_dir = Path(__file__).parent.resolve()
sudoku_file = script_dir/"PY"/"Pythonfiles"/"sudoku.py"
GTN_file = script_dir/"PY"/"Pythonfiles"/"guess-the-number.py"
TTT_file = script_dir/"C"/"tic-tac-toe.exe"

while True:
    input1 = int(input(""))
    if input1 in range(1,5):
        if input1 == 4:
            break
        if input1 == 1:
            if TTT_file.exists():
                subprocess.run([str(TTT_file)])
            else:
                print("Game not found")
        if input1 == 2:
            if GTN_file.exists():
                subprocess.run(["python", str(GTN_file)])
            else:
                print("Game not found")
        if input1 == 3:
            if sudoku_file.exists():
                subprocess.run(["python", str(sudoku_file)])
            else:
                print("Game not found")        
    else:
        print("Enter number between 1 to 4")
