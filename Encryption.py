from tkinter import *
from tkinter import messagebox


class EncGui:

    def __init__(self):
        print("call enc gui")
        enc_root = Tk()
        enc_root.title("Encryption")
        self.plain_text = StringVar(enc_root, value="")
        enc_root.geometry("400x300+300+300")
        encrypt_entry = Entry(enc_root, textvariable=self.plain_text).grid(row=1, column=1)
        enc_button = Button(enc_root, text="Encrypt", command=lambda: self.encryption_process()).grid(row=1, column=2)
        # enc_button.bind("<Button-1>  ", )
        enc_root.mainloop()

    def encryption_process(self):
        print("pressed")
        encrypted_text = encrypt(self.plain_text.get())
        print(encrypted_text)
        messagebox.showinfo("encrypted", encrypted_text)


def encrypt(strr):
    i = 0
    st = list(strr)
    for i, char in enumerate(st):
        if 'a' <= st[i] <= 'z' or 'A' <= st[i] <= 'Z':
            st[i] = (chr(ord(st[i]) + 3))

    st = st[::-1]  # reverse the list
    st = list(st)
    i = len(st)//2

    while i < len(st):
        st[i] = (chr(ord(st[i]) - 1))

        i += 1

    return ''.join(st)

