import psutil
import win32api
from tkinter import *

def main():

    def analyse():
        drives = win32api.GetLogicalDriveStrings().split('\000')[:-1]
        storage = []
        for i in drives:
            try:
                storage.append(psutil.disk_usage(i))
            except PermissionError:
                pass
        drives_values = ""
        for i in range(len(storage)):
            if i != 0:
                drives_values = drives_values + "\n"
            drives_values = f"{drives_values}({drives[i]}): {deci(storage[i].used / 2 ** 30)}Go/{deci(storage[i].total / 2 ** 30)}Go [{deci((storage[i].used / 2 ** 30) / deci(storage[i].total / 2 ** 30) * 100)}%]"

        ram['text'] = f"Ram: {deci((psutil.virtual_memory()[3] / 2 ** 30))}GB/{deci((psutil.virtual_memory()[0] / 2 ** 30))}GB [{psutil.virtual_memory()[2]}%]"
        drives_display['text'] = drives_values
        window.after(120, analyse)

    def deci(nmb: float):
        entier, decimal = str(nmb).split(".")
        tour = 0
        new_decimale = ""
        for i in decimal:
            if tour == 2:
                new_decimale += "."
            new_decimale += str(i)
            tour += 1

        return float(f"{entier}.{str(round(float(new_decimale)))}")

    window = Tk()
    window.overrideredirect(True)
    window.wm_attributes("-topmost", True)
    window.wm_attributes("-disabled", True)
    window.wm_attributes("-transparentcolor", "black")

    frame = Frame(window, bg="black")
    frame.pack(expand=YES)
    ram = Label(frame, text=f"Ram: {deci((psutil.virtual_memory()[3] / 2 ** 30))}GB/{deci((psutil.virtual_memory()[0] / 2 ** 30))}GB [{psutil.virtual_memory()[2]}%]", font=("Courrier", 13, "bold"), bg="white", fg="#252525")
    ram.pack(pady=3, padx=4, fill=X)
    drives_display = Label(frame, font=("Courrier", 13, "bold"), fg="#252525", bg="white")
    drives_display.pack(pady=3, padx=4, fill=X)

    window.after(0, analyse)
    window.mainloop()

if __name__ == "__main__":
    main()
