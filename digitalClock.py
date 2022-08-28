import tkinter
import time
import random

window = tkinter.Tk()
window.configure(background="black")
window.geometry("700x100")
window.title(" AKANT'S DIGITAL CLOCK ")

color = ["cyan", "red", "green"]


def gettime():
    string = time.strftime('%H:%M:%S %p')
    clock_label.configure(text=string)
    clock_label.configure(foreground="".join(random.choices(color)))
    clock_label.after(1000, gettime)


print("Hello World")
clock_label = tkinter.Label(window, font=('ds-digital', 100), background="black")
clock_label.pack(anchor="center")
gettime()
window.mainloop()
