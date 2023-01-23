# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 17:27:59 2023

@author: JSS-SHN
"""

import tkinter as tk
from googletrans import Translator

root = tk.Tk()
root.title("Language Translator")


combobox1 = tk.Combobox(root)
combobox1["values"] = ["en", "fr", "de", "es", "it"]
combobox1.current(0)
combobox1.pack()

combobox2 = tk.Combobox(root)
combobox2["values"] = ["en", "fr", "de", "es", "it"]
combobox2.current(0)
combobox2.pack()

textarea1 = tk.Text(root)
textarea1.pack()

textarea2 = tk.Text(root)
textarea2.pack()

def translate_text():
    src = combobox1.get()
    dest = combobox2.get()
    text = textarea1.get("1.0", tk.END)

    translator = Translator()
    try:
        translated = translator.translate(text, src=src, dest=dest)
        textarea2.delete("1.0", tk.END)
        textarea2.insert("1.0", translated.text)
    except Exception as e:
        textarea2.delete("1.0", tk.END)
        textarea2.insert("1.0", "Error: " + str(e))

translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack()

root.mainloop()
