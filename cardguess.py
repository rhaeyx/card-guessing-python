import tkinter as tk
from tkinter import ttk
import random

class CardGuessingGame:
    def main(self):
        # Globals
        self.difficulty = 1
        self.player = 1
        self.records = {
                "1" : {},
                "2" : {}
            }
                
        
        root = tk.Tk()
        self.root = root
        root.geometry("820x820")
        root.title("Guess that Card!")

        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)

        # ---Menu---
        menu = self.draw_menu(root)
        
        # ---Tutorial----
        tutorial = self.draw_tutorial(root)
        
        # ---Difficulty---
        difficulty = self.draw_difficulty(root)
        
        # ---Color----
        color1 = self.draw_color(root, "1")
        color2 = self.draw_color(root, "2")
        
        # ---Numbers----
        numbers1 = self.draw_numbers(root, "1")
        numbers2 = self.draw_numbers(root, "2")
        
        # ---Suits----
        suits1 = self.draw_suits(root, "1")
        suits2 = self.draw_suits(root, "2")

        # self.frames = [menu, difficulty, game, color, tutorial]
        self.frames = {
                        "menu": menu,
                        "tutorial": tutorial,
                        "difficulty": difficulty,
                        "color1": color1,
                        "color2": color2,
                        "numbers1": numbers1,
                        "numbers2": numbers2,
                        "suits1": suits1,
                        "suits2": suits2,
                    }

        self.show_frame(self.frames['menu'])

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky='nsew')

        root.mainloop()
    
    def draw_menu(self, root):
        # ---Menu---
        menu = tk.Frame(root)

        # Title
        title = tk.Label(menu, text="Main Menu", font=("Arial", 32, "bold"))
        title.pack(side=tk.TOP, pady=(100, 50))

        # New Game
        new_game = tk.Button(menu, text="New Game", font=("Arial", 16, "bold"), command=self.show_game, width=50, height=5)
        new_game.pack(side=tk.TOP, pady=(0, 25))

        # Tutorial
        tutorial = tk.Button(menu, text="How to Play", font=("Arial", 16, "bold"), command=self.show_tutorial, width=50, height=5)
        tutorial.pack(side=tk.TOP, pady=25)

        # Exit
        exit = tk.Button(menu, text="Exit", font=("Arial", 16, "bold"), command=lambda:root.quit(), width=50, height=5)
        exit.pack(side=tk.TOP, pady=25)
        
        return menu
    
    def draw_tutorial(self, root):
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
        
        return tutorial

    def draw_difficulty(self, root):
        difficulty = tk.Frame(root)

        # Title
        title = tk.Label(difficulty, text="Select Difficulty", font=("Arial", 32, "bold"))
        title.pack(side=tk.TOP, pady=(100, 50))

        # Easy
        easy = tk.Button(difficulty, text="Easy", font=("Arial", 16, "bold"), command=lambda:self.set_difficulty(1), width=50, height=5)
        easy.pack(side=tk.TOP, pady=(0, 25))

        # Medium
        medium = tk.Button(difficulty, text="Medium", font=("Arial", 16, "bold"), command=lambda:self.set_difficulty(2), width=50, height=5)
        medium.pack(side=tk.TOP, pady=25)

        # Hard
        hard = tk.Button(difficulty, text="Hard", font=("Arial", 16, "bold"), command=lambda:self.set_difficulty(3), width=50, height=5)
        hard.pack(side=tk.TOP, pady=25)
        
        return difficulty

    def draw_color(self, root, player):
        color = tk.Frame(root)
        title = tk.Label(color, text="Color", font=("Arial", 32, "bold"))
        title.pack(side=tk.TOP, pady=(100, 50))

        turn = tk.Label(color, text="Player " + player + "'s Turn:", font=("Arial", 16, "bold"))
        turn.pack(side=tk.TOP)

        message = tk.Label(color, text="What is the color of the card? Pick your choice!", font=("Arial", 16, "bold"))
        message.pack(side=tk.TOP, pady=(100, 0))

        red = tk.Button(color, text="Red", font=("Arial", 16, "bold"), command=lambda:self.record_color('red'), width=20, height=5, bg="red", fg="white")
        red.pack(side=tk.LEFT, anchor="n", pady=(50, 0), padx=(100, 25))

        black = tk.Button(color, text="Black", font=("Arial", 16, "bold"), command=lambda:self.record_color('black'), width=20, height=5, bg="black", fg="white")
        black.pack(side=tk.LEFT, anchor="n", pady=(50, 0), padx=(100, 25))
        
        return color
    
    def draw_numbers(self, root, player):
        number = tk.Frame(root)
        title = tk.Label(number, text="Number", font=("Arial", 32, "bold"))
        title.pack(side=tk.TOP, pady=(100, 50))

        turn = tk.Label(number, text="Player " + player + "'s Turn:", font=("Arial", 16, "bold"))
        turn.pack(side=tk.TOP)

        message = tk.Label(number, text="What is the number of the card? Pick your choice!", font=("Arial", 16, "bold"))
        message.pack(side=tk.TOP, pady=(100, 0))
        
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        
        rank = ttk.Combobox(number, values=ranks, state="readonly", width=50, height=20, font=("Arial", 16))
        rank.current(0)
        rank.pack(side=tk.TOP, pady=(50, 0))
        
        next = tk.Button(number, text="Next", font=("Arial", 16, "bold"), command=lambda:self.record_rank(rank.get()), width=20, height=2)
        next.pack(side=tk.TOP, pady=(50, 0), padx=(100, 25))

        return number
    
    def draw_suits(self, root, player):
        suit = tk.Frame(root)
        title = tk.Label(suit, text="Number", font=("Arial", 32, "bold"))
        title.pack(side=tk.TOP, pady=(100, 50))

        turn = tk.Label(suit, text="Player " + player + "'s Turn:", font=("Arial", 16, "bold"))
        turn.pack(side=tk.TOP)

        message = tk.Label(suit, text="What is the suit of the card? Pick your choice!", font=("Arial", 16, "bold"))
        message.pack(side=tk.TOP, pady=(100, 0))
        
        types = ["Diamonds", "Clubs", "Hearts", "Spades"]

        type = ttk.Combobox(suit, values=types, state="readonly", width=50, height=20, font=("Arial", 16))
        type.current(0)
        type.pack(side=tk.TOP, pady=(50, 0))
        
        next = tk.Button(suit, text="Next", font=("Arial", 16, "bold"), command=lambda:self.record_suit(type.get()), width=20, height=2)
        next.pack(side=tk.TOP, pady=(50, 0), padx=(100, 25))

        return suit


    def end_screen(self, root):
        suit =  self.suit
        rank =  self.rank
        color = self.color
            
        winner = "No Winner"
        p1 = 0
        p2 = 0
        
        if self.difficulty == 1:
            if self.records["1"]["color"] == color:
                p1 += 1
                
            if self.records["2"]["color"] == color:
                p2 += 1
        
        if self.difficulty > 1:
            if self.records["1"]["rank"] == rank:
                p1 += 1
            
            if self.records["2"]["rank"] == rank:
                p2 += 1
                
        if self.difficulty > 2:
            if self.records["1"]["suit"] == suit:
                p1 += 1
            
            if self.records["2"]["suit"] == suit:
                p2 += 1
                
        if p1 > p2:
            winner = "Player 1 is the winner!"
        elif p1 < p2:
            winner = "Player 2 is the winner!"
        elif (p1 > 0) and p1 == p2:
            winner = "Draw!"
            
        end_screen = tk.Frame(root)
        title = tk.Label(end_screen, text="Results", font=("Arial", 32, "bold"))
        title.pack(side=tk.TOP, pady=(100, 50))

        instructions = f"The Selected Card is a {color} {rank} of {suit} \n\n"
        instructions += f"Color: Player 1 picked \"{self.records['1']['color'].upper()}\" and Player 2 picked \"{self.records['2']['color'].upper()}\"\n\n"
        
        if (self.difficulty > 1):
            instructions += f"Rank: Player 1 picked \"{self.records['1']['rank'].upper()}\" and Player 2 picked \"{self.records['2']['rank'].upper()}\"\n\n"
        
        if (self.difficulty > 2):
            instructions += f"Suit: Player 1 picked \"{self.records['1']['suit'].upper()}\" and Player 2 picked \"{self.records['2']['suit'].upper()}\"\n\n"

        instructions += winner

        content = tk.Label(end_screen, text=instructions, font=("Arial", 16))
        content.pack(side=tk.TOP, pady=100)
        
        # New Game
        new_game = tk.Button(end_screen, text="New Game", font=("Arial", 16, "bold"), command=self.show_game, width=20, height=3)
        new_game.pack(side=tk.TOP, pady=(0, 25))
        
        end_screen.grid(row=0, column=0, sticky='nsew')
        
        self.show_frame(end_screen)
    
    def show_frame(self, frame):
        frame.tkraise()
        
    def set_difficulty(self, n):
        # GENERATE CARD
        suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.suit =  suits[random.randint(0, 3)]
        self.rank =  ranks[random.randint(0, 12)]
        self.color = "red"
        if self.suit in ["Clubs", "Spades"]:
            self.color = "black"
            
        print(self.suit, self.rank, self.color)
        self.difficulty = n
        self.player = 1
        self.records = {
                "1" : {},
                "2" : {}
            }

        self.show_frame(self.frames['color1'])
        
    def show_game(self):
        self.show_frame(self.frames['difficulty'])
        
    def show_tutorial(self):
        self.show_frame(self.frames['tutorial'])
        
    def color_to_next(self):
        if self.difficulty == 1:
            self.get_result()
            
    def get_result(self):
        print(self.records)
        self.end_screen(self.root)
        
    def record_color(self, color):
        self.records[str(self.player)]["color"] = color
        if self.difficulty == 1 and self.player == 2:
            self.get_result()
        elif self.difficulty == 1 and self.player == 1:
            self.player += 1
            self.show_frame(self.frames["color2"])
        else:
            self.show_frame(self.frames["numbers"+str(self.player)])
            
    def record_rank(self, rank):
        self.records[str(self.player)]["rank"] = rank
        if self.difficulty == 2 and self.player == 2:
            self.get_result()
        elif self.difficulty == 2 and self.player == 1:
            self.player += 1
            self.show_frame(self.frames["color2"])
        else:
            self.show_frame(self.frames["suits"+str(self.player)])
            
    def record_suit(self, suit):
        self.records[str(self.player)]["suit"] = suit
        if self.difficulty == 3 and self.player == 2:
            self.get_result()
        elif self.difficulty == 3 and self.player == 1:
            self.player += 1
            self.show_frame(self.frames["color2"])
        else:
            self.show_frame(self.frames["suits"+str(self.player)])
        
    
x = CardGuessingGame()
x.main()