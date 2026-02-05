import subprocess
from pathlib import Path
script_dir = Path(__file__).parent.resolve()
programs = {
    1 : {
        "name" : "Tic Tac Toe",
        "path" : script_dir/"games_file"/"tic-tac-toe.exe",
        "run_type" : "exe",
        
    },
    2 : {
        "name" : "Guess The Number",
        "path" : script_dir/"games_file"/"guess-the-number.py",
        "run_type" : "py",   
    },
    3 : {
        "name" : "Sudoku",
        "path" : script_dir/"games_file"/"sudoku.py",
        "run_type" : "py",
    },
    4 : {
        "name" : "Number Base Convertor",
        "path" : script_dir/"games_file"/"number-base-convertor.py",
        "run_type" : "py",
    },
    5 : {
        "name" : "Calculator",
        "path" : script_dir/"games_file"/"calculator.py",
        "run_type" : "py",
    }
}

print("Welcome")
print("Select")
for n in programs:
    print(f'{n} for {programs[n]["name"]}')
print("6 to Quit")


def play(programs):
    while True:
        try:
            choice = int(input(""))
        except ValueError:
            print("Please enter a number")
            continue
        if choice == 6:
            break
        elif choice in programs:
            if programs[choice]["path"].exists():
                if programs[choice]["run_type"] == "exe":
                    subprocess.run([str(programs[choice]["path"])])
                elif programs[choice]["run_type"] == "py":
                    subprocess.run(["python", programs[choice]["path"]])
            else:
                print("Game not found")
        else:
            print("Enter number between 1 to 6")
    
play(programs)
