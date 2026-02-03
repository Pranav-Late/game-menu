import subprocess
from pathlib import Path

print("Welcome!")
print("Select")
print("1 for Tic Tac Toe")
print("2 for Guess The Number")
print("3 for Sudoku")
print("4 for Number Base Convertor")
print("5 to Quit")
script_dir = Path(__file__).parent.resolve()
sudoku_file = script_dir/"games_file"/"sudoku.py"
GTN_file = script_dir/"games_file"/"guess-the-number.py"
TTT_file = script_dir/"games_file"/"tic-tac-toe.exe"
NBC_file = script_dir/"games_file"/"number-base-convertor.py"

while True:
    try:
        choice = int(input(""))
    except ValueError:
        print("Please enter a number")
        continue
    match choice:
        case 1:
            if TTT_file.exists():
                subprocess.run([str(TTT_file)])
            else:
                print("Game not found")
        case 2:
            if GTN_file.exists():
                subprocess.run(["python", str(GTN_file)])
            else:
                print("Game not found")
        case 3:
            if sudoku_file.exists():
                subprocess.run(["python", str(sudoku_file)])
            else:
                print("Game not found")
        case 4:
            if NBC_file.exists():
                subprocess.run(["python", str(NBC_file)])
            else:
                print("Game not found")
        case 5:
            break
        case _:
            print("Enter number between 1 to 5")
    
