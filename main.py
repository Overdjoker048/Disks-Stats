import psutil
import win32api
import json
import os
from tkinter import *
from tkinter import messagebox

def main():
    with open("config.json", "a+") as file:
        file.close()
    if os.path.exists("config.json"):
        try:
            with open("config.json", "r+") as file:
                content = json.load(fp=file)
        except:
            content = {
                "first": "white",
                "second": "#252525",
            }
    else:
        content = {
            "first": "white",
            "second": "#252525",
        }

    def set_theme(first, second):
        info = {
            "first": first,
            "second": second
        }
        with open("config.json", "w+") as file:
            json.dump(info, file, indent=2)
        messagebox.showinfo(title="Stats Browser Info", message="You must restart the application\nfor the settings to be active.")


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
        window.after(100, analyse)

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
    menu = Menu(window)
    window.config(menu=menu, bg="red")
    window.wm_attributes("-topmost", True)
    window.wm_attributes("-transparentcolor", "red")

    ram = Label(window, text=f"Ram: {deci((psutil.virtual_memory()[3] / 2 ** 30))}GB/{deci((psutil.virtual_memory()[0] / 2 ** 30))}GB [{psutil.virtual_memory()[2]}%]", font=("Courrier", 13, "bold"), bg=content['first'], fg=content['second'])
    ram.pack(pady=2, fill=X)
    drives_display = Label(window, font=("Courrier", 13, "bold"), fg=content['second'], bg=content['first'])
    drives_display.pack(pady=2, fill=X)

    menu_themes = Menu(menu, tearoff=0)
    menu.add_cascade(label="Themes", menu=menu_themes)
    menu_themes.add_command(label="Dark", command=lambda: [set_theme("#252525", "white")])
    menu_themes.add_command(label="Light", command=lambda: [set_theme("white", "#252525")])

    menu.add_command(label="Exit", command=exit)
    menu.add_command(label="Help", command=lambda: [messagebox.showinfo(title="Stats Browser Help", message="Name: Stats Browser\nBy Overdjoker048\nUpdate: 1.1.0\nSource: https://github.com/Overdjoker048/Stats-Browser")])
    window.after(0, analyse)
    window.mainloop()

if __name__ == "__main__":
    main()
