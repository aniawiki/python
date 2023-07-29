import tkinter as tk
from tkinter import filedialog

class TextEditor(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("750x400")
        button_frame = tk.Frame(self)
        button_frame.pack(side="top", anchor="nw", padx=5, pady=5)  # Dodajemy padding, aby oddzielić przyciski od krawędzi okna

        # Tworzenie przycisków i umieszczenie ich w kontenerze
        open_button = tk.Button(button_frame, text="Open", command=self.open_file)
        open_button.pack(side="left", padx=1)  # Ustawiamy przycisk na lewo od ramki
        save_button = tk.Button(button_frame, text="Save", command=self.save_file)
        save_button.pack(side="left", padx=1)  # Ustawiamy przycisk na lewo od poprzedniego przycisku
        self.T = tk.Text(self, bg = '#222222', fg='white', cursor="xterm #ffffff")
        self.T.pack(fill="both", expand=True)
        self.bind("<Configure>", self.on_resize) # zmiana rozmiaru okna

    def on_resize(self, event):
        # Funkcja do przeskalowania pola tekstowego wraz ze zmianami rozmiaru okna
        self.T.config(height=self.winfo_height(), width=self.winfo_width())

    def open_file(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            with open(filepath, "r") as file:
                content = file.read()
                self.T.delete("1.0", "end")
                self.T.insert("1.0", content)

    def save_file(self):
        filepath = filedialog.asksaveasfilename()
        if filepath:
            with open(filepath, "w") as file:
                file.write(self.T.get(1.0, tk.END))
 

if __name__ == "__main__":
    app = TextEditor()
    app.mainloop()