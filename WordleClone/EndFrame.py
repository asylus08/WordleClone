import tkinter as tk

class EndFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#2e2e2e")
        self.controller = controller

        label = tk.Label(self, text="Your Statistics", font=("Helvetica", 12),
            justify="center",
            wraplength=300,
            bg="#2e2e2e",  
            fg="white"  
        )
        label.pack(pady=20)

        button = tk.Button(self, text="Go to the beginning", command=self.go_to_start_frame, bg="#f9c74f",
            fg="black",  # White text color
            font=("Helvetica", 12, "bold"),
            relief="flat",
            padx=10,
            pady=5
        )
        button.pack()

    def go_to_start_frame(self):
        self.controller.show_frame("StartFrame")