from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        self.root.geometry("400x600")
        
        self.text_area = Text(self.root, wrap=WORD)
        self.text_area.pack(expand=True, fill=BOTH)
        
        self.create_menu()
    
    def create_menu(self):
        menubar = Menu(self.root)
        
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        menubar.add_cascade(label="File", menu=file_menu)
        
        edit_menu = Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Cut", command=self.cut_text)
        edit_menu.add_command(label="Copy", command=self.copy_text)
        edit_menu.add_command(label="Paste", command=self.paste_text)
        
        menubar.add_cascade(label="Edit", menu=edit_menu)
        
        self.root.config(menu=menubar)
    
    def new_file(self):
        self.text_area.delete(1.0, END)
    
    def open_file(self):
        file = askopenfile(mode="r", filetypes=[('Text Files', '*.txt')])
        if file is not None:
            content = file.read()
            self.text_area.delete(1.0, END)
            self.text_area.insert(END, content)
            file.close()
    
    def save_file(self):
        file = asksaveasfile(mode="w", defaultextension=".txt", filetypes=[('Text Files', '*.txt')])
        if file is not None:
            text = self.text_area.get(1.0, END)
            file.write(text)
            file.close()
    
    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")
    
    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")
    
    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")

if __name__ == "__main__":
    root = Tk()
    notepad = Notepad(root)
    root.mainloop()
