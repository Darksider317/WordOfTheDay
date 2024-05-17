import tkinter as tk
from tkinter import messagebox
from words import get_random_word

class WordOfTheDayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Слово дня")
        
        self.label = tk.Label(root, text="Слово дня", font=("Helvetica", 18))
        self.label.pack(pady=20)
        
        self.word_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.word_label.pack(pady=10)
        
        self.meaning_label = tk.Label(root, text="", font=("Helvetica", 12), wraplength=300)
        self.meaning_label.pack(pady=10)
        
        self.button = tk.Button(root, text="Получить слово", command=self.get_word)
        self.button.pack(pady=20)
    
    def get_word(self):
        word, meaning = get_random_word()
        if word and meaning:
            self.word_label.config(text=word)
            self.meaning_label.config(text=meaning)
        else:
            messagebox.showerror("Ошибка", "Не удалось получить слово дня")

if __name__ == "__main__":
    root = tk.Tk()
    app = WordOfTheDayApp(root)
    root.mainloop()
