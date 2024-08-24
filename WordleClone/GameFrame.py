import tkinter as tk
import FileReader

word_of_the_day = FileReader.choose_word()
print(word_of_the_day)

class GameFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#2e2e2e")  # Dark background for the frame
        self.controller = controller

        label = tk.Label(self, text="Guess the word!", font=("Helvetica", 16), bg="#2e2e2e", fg="white")
        label.pack(pady=10)

        # Create a grid of Entry widgets
        self.create_grid()

        button = tk.Button(self, text="Hint?", command=self.give_hint, bg="#f9c74f", fg="white", font=("Helvetica", 12, "bold"), relief="flat")
        button.pack(pady=10)

        # Set focus to the first cell
        self.entries[0][0].focus_set()

    def create_grid(self):
        grid_frame = tk.Frame(self, bg="#2e2e2e")
        grid_frame.pack(padx=5, pady=5, expand=False)

        self.entries = [[self.create_entry(grid_frame, row, col) for col in range(5)] for row in range(5)]

    def create_entry(self, parent, row, col):
        entry = tk.Entry(parent, width=2, font=("Helvetica", 24), justify='center', bg="#6c757d", fg="white", borderwidth=1, relief="solid")
        entry.grid(row=row, column=col, padx=5, pady=5)
        entry.bind('<KeyRelease>', self.handle_key_release)
        entry.bind('<Return>', self.move_to_next_row)
        entry.bind('<BackSpace>', self.move_back_one_space)
        entry.bind('<Button-1>', self.disable_mouse_event)
        return entry

    def handle_key_release(self, event):
        widget = event.widget

        if event.keysym == 'BackSpace':
            return

        if len(widget.get()) > 1:
            widget.delete(1, tk.END)

        if len(widget.get()) == 1:
            row, col = self.find_widget_position(widget)
            if col < 4:
                self.entries[row][col + 1].focus_set()
                self.entries[row][col + 1].icursor(tk.END)

        self.disable_other_rows(self.find_widget_position(widget)[0])

    def move_back_one_space(self, event):
        widget = event.widget
        row, col = self.find_widget_position(widget)

        if len(widget.get()) == 0 and col > 0:
            self.entries[row][col - 1].focus_set()
            self.entries[row][col - 1].icursor(tk.END)
        else:
            widget.delete(len(widget.get()) - 1, tk.END)
            widget.icursor(tk.END)
        
        return "break"

    def validate_answer(self, row):
        word = ''.join(self.entries[row][col].get() for col in range(5))
        if word == word_of_the_day:
            self.go_to_end_frame()

    def move_to_next_row(self, event):
        widget = event.widget
        row, col = self.find_widget_position(widget)

        if col == 4 and len(widget.get()) == 1:
            self.validate_answer(row)
            if row < 4:
                self.entries[row + 1][0].focus_set()
            else:
                self.go_to_end_frame()
        
        return "break"

    def give_hint(self):
        word = ""

    def go_to_end_frame(self):
        self.controller.show_frame("EndFrame")

    def find_widget_position(self, widget):
        for row_index, row_entries in enumerate(self.entries):
            if widget in row_entries:
                return row_index, row_entries.index(widget)
        return None, None

    def disable_other_rows(self, active_row):
        for row_index, row_entries in enumerate(self.entries):
            state = 'normal' if row_index == active_row else 'disabled'
            for entry in row_entries:
                entry.config(state=state)

    def disable_mouse_event(self, event):
        return "break"
