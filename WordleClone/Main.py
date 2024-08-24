import tkinter as tk
from EndFrame import EndFrame
from StartFrame import StartFrame
from GameFrame import GameFrame

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Guess the word of the day")
        self.geometry("400x400")
        self.resizable(False, False)

        self.frames = {}
        self.setup_frames()

        self.show_frame("StartFrame")

    def setup_frames(self):
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        for FrameClass in (StartFrame, EndFrame, GameFrame):
            page_name = FrameClass.__name__
            self.frames[page_name] = FrameClass(container, self)
            self.frames[page_name].grid(row=0, column=0, sticky="nsew")

    def show_frame(self, frame_name):
        frame = self.frames.get(frame_name)
        if frame:
            frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
