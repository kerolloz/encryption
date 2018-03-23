from Encryption import *
from Decryption import *
from tkinter import *


class Message:
    def __init__(self, root):
        root.title("Crypto Text")
        root.geometry("400x200+300+300")
        # to_process_text = StringVar(root, value="Enter your text Here!!!")
        self.encryptButton = Button(root, text="Encrypt My Text", command=lambda: EncGui()).grid(row=1, column=1)
        self.decryptButton = Button(root, text="Decrypt My Text", command=lambda: DecGui()).grid(row=1, column=2)


root = Tk()

Mes = Message(root)

root.mainloop()
