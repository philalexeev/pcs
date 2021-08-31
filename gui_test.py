import easygui as eg
import tkinter as tk

# msgbox_result = eg.msgbox(msg="first try. not bad", title="warning window")
# print(msgbox_result)

# msgbox_result = eg.buttonbox(msg="choose a color", title="warning window", choices=(
#     "red",
#     "green",
#     "blue"
# ))
# print(msgbox_result)

# msgbox_result = eg.enterbox(msg="type something below", title="warning window")
# print(msgbox_result)

# msgbox_result = eg.fileopenbox(title="select a file")
# print(msgbox_result)

# ------------------ TkInter

window = tk.Tk()
# greeting = tk.Label(text="text from the tkinter")
# greeting.pack()

label = tk.Label(
    text="enter some dummy text"
)
label.pack()

entry = tk.Entry()
entry.pack()

def handle_keypress():
    print(entry.get())

button = tk.Button(
    text="main button",
    fg="white",
    bg="orange",
    width="25",
    height="5",
    command=handle_keypress
)
button.pack()


window.mainloop()

