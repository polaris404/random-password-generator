import tkinter as tk
import webbrowser
import pgenerator as pg

COLOUR = "grey80"
WORDS = pg.get_words()


def refresh_words():
    global WORDS
    WORDS = pg.get_words()


############################################################
#                 Building command functions
############################################################


def callback(url):
    webbrowser.open_new(url)


def showhint():
    global WORDS
    if bool(hint_var.get()):
        hint_label.config(text=f"Words Used : {WORDS}")
    else:
        hint_label.config(text=f"")


def generate_normal_pass():
    refresh_words()
    global WORDS
    # print(WORDS)
    password = "".join(WORDS)
    entry.configure(state="normal")
    entry.delete(0, "end")
    entry.insert(0, password)
    entry.configure(state="readonly")
    showhint()


def generate_complex_pass():
    refresh_words()
    global WORDS
    # print(WORDS)
    password = pg.add_complexity("".join(WORDS))
    entry.configure(state="normal")
    entry.delete(0, "end")
    entry.insert(0, password)
    entry.configure(state="readonly")
    showhint()


def generate_custom_pass():
    refresh_words()
    global WORDS
    string = "".join(WORDS)
    print(string)
    print(
        hint_var.get(),
        words_var.get(),
        upper_var.get(),
        digits_var.get(),
        symbols_var.get(),
    )
    if bool(words_var.get()):
        print("add n of word")
        print(no_of_words.get())
        WORDS = pg.get_words(no_of_words.get())
        print(WORDS)
        string = "".join(WORDS)
    if bool(upper_var.get()):
        string = pg.add_cap_letters(string)
    if bool(digits_var.get()):
        string = pg.add_digits(string)
    if bool(symbols_var.get()):
        string = pg.add_symbols(string)

    entry.configure(state="normal")
    entry.delete(0, "end")
    entry.insert(0, string)
    entry.configure(state="readonly")
    showhint()


def copy_pass():
    gui.clipboard_append(entry.get())


############################################################
#                     Building GUI
############################################################
gui = tk.Tk()
gui.geometry("730x480")
gui.title("Password Generator")
gui.resizable(0, 0)
gui.configure(bg=COLOUR)

# Checkbox variables
hint_var = tk.IntVar()
words_var = tk.IntVar()
upper_var = tk.IntVar()
digits_var = tk.IntVar()
symbols_var = tk.IntVar()

# Entry
display = tk.StringVar()
no_of_words = tk.IntVar()

frame_header = tk.Frame(bg="black")
tk.Label(
    text="Password Generator", font="Helvetica 30 bold", bg="black", fg="white"
).pack(ipady=10, fill="both")
tk.Label(
    text="A Password Generator based on Diceware",
    font="arial 11",
    bg="black",
    fg="white",
).pack(fil="both")
frame_header.pack(fill="both")

input_frame = tk.Frame(gui, width=180, height=1, borderwidth=2, relief=tk.SUNKEN)
entry = tk.Entry(
    input_frame, borderwidth=2, width=100, bg="red", font="12", relief=tk.FLAT
)
entry.pack(side="top", padx=20, pady=20)
entry.configure(state="readonly")
input_frame.pack(fill="x", expand=True, padx=110)

frame2 = tk.Frame(gui, bg=COLOUR)
tk.Checkbutton(
    frame2, text="Show Hint", bg=COLOUR, variable=hint_var, command=showhint
).grid(row=0, column=0, pady=5)
tk.Button(frame2, text="Copy", command=copy_pass).grid(row=0, column=1, sticky=tk.E)
frame2.grid_columnconfigure(1, weight=1)
frame2.grid_rowconfigure(0, weight=1)
frame2.pack(fill="x", padx=110)

hint_label = tk.Label(text=f"", bg=COLOUR)
hint_label.pack(anchor="nw", padx=130)

frame = tk.Frame(gui, bg=COLOUR)
tk.Label(frame, text="Generate a NORMAL password :", font="arial 12", bg=COLOUR).grid(
    row=0, column=0, columnspan=2, sticky=tk.W
)
tk.Button(
    frame, text="Generate", bg="black", fg="white", command=generate_normal_pass
).grid(row=0, column=2, padx=5, pady=10)
tk.Label(frame, text="Generate a COMPLEX password :", font="arial 12", bg=COLOUR).grid(
    row=1, column=0, columnspan=2, sticky=tk.W
)
tk.Button(
    frame, text="Generate", bg="black", fg="white", command=generate_complex_pass
).grid(row=1, column=2, padx=5, pady=10)
tk.Label(frame, text="Generate a CUSTOM password :", font="arial 12", bg=COLOUR).grid(
    row=2, column=0, columnspan=2, sticky=tk.W
)
tk.Button(
    frame, text="Generate", bg="black", fg="white", command=generate_custom_pass
).grid(row=2, column=2, padx=5, pady=10)
tk.Label(frame, text="Password must contain-", font="arial 9", bg=COLOUR).grid(
    row=3, column=1, sticky=tk.W
)

tk.Checkbutton(
    frame, text="Number of words(Default is 4) :", variable=words_var, bg=COLOUR
).grid(row=4, column=1, sticky=tk.W)
tk.Entry(frame, textvariable=no_of_words, width=5).grid(row=4, column=1, sticky=tk.E)
tk.Checkbutton(frame, text="Uppercase Letters", bg=COLOUR, variable=upper_var).grid(
    row=5, column=1, sticky=tk.W
)
tk.Checkbutton(frame, text="Digits", bg=COLOUR, variable=digits_var).grid(
    row=4, column=2, sticky=tk.W
)
tk.Checkbutton(frame, text="Symbols", bg=COLOUR, variable=symbols_var).grid(
    row=5, column=2
)

frame.pack(side=tk.LEFT, expand=True, padx=150, pady=25)

footer_frame = tk.Frame(gui)
link = tk.Label(
    footer_frame,
    text="by spicymaterial",
    font="arial 10 underline",
    bg=COLOUR,
    fg="blue",
)
link.pack(side=tk.BOTTOM, anchor="se", ipady=5, ipadx=10)
footer_frame.pack(side=tk.BOTTOM, anchor="se", fill="x")

############################################################
#                     Implementation
############################################################
link.bind("<Button-1>", lambda e: callback("https://github.com/spicymaterial"))
gui.mainloop()
