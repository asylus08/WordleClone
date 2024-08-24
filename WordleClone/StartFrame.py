import tkinter as tk

class StartFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#2e2e2e")  # Dark background for the frame
        self.controller = controller

        title = tk.Label(
            self,
            text="Wordle Clone :D",
            font=("Helvetica", 16),
            justify="center",
            wraplength=300,
            bg="#2e2e2e",  # Match the frame's background color
            fg="white"  # White text color
        )
        title.pack(pady=20)

        label = tk.Label(
            self,
            text="Hi, welcome to Wordle...but on a budget ;) \n"
                 "The rules are quite simple! Like Wordle, \n"
                 "you have to guess a 5 letter word chosen randomly. \n"
                 "However, you may find this a bit more difficult as \n"
                 "you CAN'T keep track of the used letters. \n"
                 "5 attempts, 5 letters. Best of luck!",
            font=("Helvetica", 12),
            wraplength=300,
            bg="#2e2e2e",  # Match the frame's background color
            fg="white"  # White text color
        )
        label.pack(pady=20)

        button = tk.Button(
            self,
            text="Start game",
            command=self.go_to_game_frame,
            bg="#f9c74f",  # Yellow background
            fg="black",  # White text color
            font=("Helvetica", 12, "bold"),
            relief="flat",
            padx=10,
            pady=5
        )
        button.pack()

        

    def go_to_game_frame(self):
        self.controller.show_frame("GameFrame")
