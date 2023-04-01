import tkinter as tk

def show_frame(frame):
    frame.tkraise()
    
def set_difficulty(n):
    difficulty = n
    show_frame(color)
    
def show_game():
    show_frame(difficulty)
    
def show_tutorial():
    show_frame(tutorial)
    
def color_to_next():
    if difficulty == 1:
        get_result()
        
def get_result():
    pass

root = tk.Tk()
root.geometry("820x820")
root.title("Guess that Card!")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# ---Menu---
menu = tk.Frame(root)

# Title
title = tk.Label(menu, text="Main Menu", font=("Arial", 32, "bold"))
title.pack(side=tk.TOP, pady=(100, 50))

# New Game
new_game = tk.Button(menu, text="New Game", font=("Arial", 16, "bold"), command=show_game, width=50, height=5)
new_game.pack(side=tk.TOP, pady=(0, 25))

# Tutorial
tutorial = tk.Button(menu, text="How to Play", font=("Arial", 16, "bold"), command=show_tutorial, width=50, height=5)
tutorial.pack(side=tk.TOP, pady=25)

# Exit
exit = tk.Button(menu, text="Exit", font=("Arial", 16, "bold"), command=lambda:root.quit(), width=50, height=5)
exit.pack(side=tk.TOP, pady=25)

# ---Difficulty---
difficulty = tk.Frame(root)

# Title
title = tk.Label(difficulty, text="Select Difficulty", font=("Arial", 32, "bold"))
title.pack(side=tk.TOP, pady=(100, 50))

# New Game
easy = tk.Button(difficulty, text="Easy", font=("Arial", 16, "bold"), command=lambda:set_difficulty(1), width=50, height=5)
easy.pack(side=tk.TOP, pady=(0, 25))

# Tutorial
medium = tk.Button(difficulty, text="Medium", font=("Arial", 16, "bold"), command=lambda:set_difficulty(2), width=50, height=5)
medium.pack(side=tk.TOP, pady=25)

# Exit
hard = tk.Button(difficulty, text="Hard", font=("Arial", 16, "bold"), command=lambda:set_difficulty(3), width=50, height=5)
hard.pack(side=tk.TOP, pady=25)

# ---Game----
game = tk.Frame(root)
title = tk.Label(game, text="Game", font=("Arial", 32, "bold"))
title.pack(side=tk.TOP, pady=(100, 50))

# ---Color----
color = tk.Frame(root)
title = tk.Label(color, text="Color", font=("Arial", 32, "bold"))
title.pack(side=tk.TOP, pady=(100, 50))

player = 1
turn = tk.Label(color, text="Player " + str(player) + "'s Turn:", font=("Arial", 16, "bold"))
turn.pack(side=tk.TOP)

message = tk.Label(color, text="What is the color of the card? Pick your choice!", font=("Arial", 16, "bold"))
message.pack(side=tk.TOP, pady=(100, 0))

red = tk.Button(color, text="Red", font=("Arial", 16, "bold"), command=next_game, width=20, height=5, bg="red", fg="white")
red.pack(side=tk.LEFT, anchor="n", pady=(50, 0), padx=(100, 25))

black = tk.Button(color, text="Black", font=("Arial", 16, "bold"), command=next_game, width=20, height=5, bg="black", fg="white")
black.pack(side=tk.LEFT, anchor="n", pady=(50, 0), padx=(100, 25))



# ---Tutorial----
tutorial = tk.Frame(root)
title = tk.Label(tutorial, text="How to Play?", font=("Arial", 32, "bold"))
title.pack(side=tk.TOP, pady=(100, 50))

instructions = """
The game has three different levels: 

level 1: color of the card only 
level 2: color and number 
level 3: color, number, and suites"""

content = tk.Label(tutorial, text=instructions, font=("Arial", 16))
content.pack(side=tk.TOP, pady=100)

frames = [menu, difficulty, game, color, tutorial]

show_frame(menu)

for frame in frames:
    frame.grid(row=0, column=0, sticky='nsew')




root.mainloop()

