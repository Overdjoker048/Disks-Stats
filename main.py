from psutil import disk_usage
from win32api import GetLogicalDriveStrings
from tkinter import Tk, Label, LEFT

def analyse():
    drives = GetLogicalDriveStrings().split('\000')[:-1]

    storage = []
    for i in drives:
        try:
            storage.append(disk_usage(i))
        except PermissionError:
            storage.append("pass")
    drives_values = ""
    for i in range(len(storage)):
        if storage[i] != "pass":
            if i != 0:
                drives_values = drives_values + "\n"
            drives_values = f"{drives_values}({drives[i]}): {round(storage[i].used/10**9, 2)}Go/{round(storage[i].total/10**9, 2)}Go"

    drives_display['text'] = drives_values
    window.after(250, analyse)

window = Tk()
window.overrideredirect(True)
window.config(bg="#1E1E1E")
window.wm_attributes("-topmost", True)
drives_display = Label(window, font=("Courrier", 11, "bold"), fg="#252525", bg="white", highlightbackground="#1E1E1E", highlightcolor="#1E1E1E", highlightthickness=2)
drives_display.pack()

window.bind("<Control-m>", lambda event: window.destroy())
window.after(0, analyse)
window.mainloop()