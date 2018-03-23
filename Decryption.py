from tkinter import messagebox
from tkinter import *


class DecGui:

    def __init__(self):
        print("call dec gui")
        dec_root = Tk()
        dec_root.title("Decryption")
        self.plain_text = StringVar(dec_root, value="")
        dec_root.geometry("400x300+300+300")
        decrypt_entry = Entry(dec_root, textvariable=self.plain_text).grid(row=1, column=1)
        dec_button = Button(dec_root, text="Decrypt", command=lambda: self.decryption_process()).grid(row=1, column=2)
        # enc_button.bind("<Button-1>  ", )
        dec_root.mainloop()

    def decryption_process(self):
        print("pressed")
        decrypted_text = decrypt(self.plain_text.get())
        print(decrypted_text)
        messagebox.showinfo("decrypted", decrypted_text)


def decrypt(ss):
    st = list(ss)
    i = len(st) // 2
    while i < len(st):
        st[i] = chr((ord(st[i]) + 1))
        i += 1

    st = ''.join(reversed(st))  # reverse the list using reversed() function <<
    st = list(st)

    for i, char in enumerate(st):
        if chr(ord('a')+3) <= st[i] <= chr(ord('z')+3) or chr(ord('A')+3) <= st[i] <= chr(ord('Z')+3):
            st[i] = (chr(ord(st[i]) - 3))

    return ''.join(st)
