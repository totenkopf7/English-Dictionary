from tkinter import *
from PyDictionary import PyDictionary

root = Tk()
root.geometry("450x550")
root.title("Dictionary")
root.columnconfigure(0, weight=1)
root.config(bg="black")


def space():
    space = Label(text="", bg="black")
    space.grid()


def find_meaning():
    word = entry.get()
    dictionary = PyDictionary(word)
    definition = dictionary.getMeanings()
    label_list = []

    try:

        if "Noun" in definition[word]:
            label_list.append("Noun: " + definition[word]["Noun"][0])
        if "Verb" in definition[word]:
            label_list.append("Verb: " + definition[word]["Verb"][0])
        if "Adjective" in definition[word]:
            label_list.append("Adjective: " + definition[word]["Adjective"][0])
        if "Adverb" in definition[word]:
            label_list.append("Adverb: " + definition[word]["Adverb"][0])
            # After each word form definition has been added,
            # join them together with two new lines in between each definition
        label = "\n\n".join(label_list)

    except Exception:
        label = "Wrong word entered!"


    return label


def write():
    label.config(text=find_meaning())
    entry.delete(0, END)

def funcs(z):
    find_meaning()
    write()

space()
dic_text = Label(root, text="Dictionary", fg="#3dcc8e", bg="black", font=("arial", 15, "bold"))
dic_text.grid()

space()
entry = Entry(root, font=("times", 23, "bold"))
entry.grid()

space()

btn = Button(root, text="Explain", bg="#3dcc8e", fg="black", font=("bold"), command=lambda: [find_meaning(), write()])
btn.grid()

space()
label = Label(root, text="Translation", background="#3e3e3e",
              width=40, height=21, relief=FLAT, state=DISABLED, disabledforeground="#3dcc8e", wraplength=200,
              justify=LEFT)
label.grid()

root.bind('<Return>', funcs)
root.mainloop()
