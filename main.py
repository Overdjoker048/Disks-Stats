from psutil import virtual_memory, disk_usage
from win32api import GetLogicalDriveStrings
from os import path
from json import dump, load
from sys import exit
from tkinter import Tk, Label, Menu, X, messagebox

def main():
    with open("config.json", "a+") as file:
        file.close()
    if path.exists("config.json"):
        try:
            with open("config.json", "r+") as file:
                content = load(fp=file)
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
            dump(info, file, indent=2)
        drives_display.config(fg=second, bg=first)
        ram.config(fg=second, bg=first)

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
                drives_values = f"{drives_values}({drives[i]}): {deci(storage[i].used)}Go/{deci(storage[i].total)}Go [{deci((storage[i].used) / deci(storage[i].total) * 100)}%]"

        ram['text'] = f"Ram: {deci((virtual_memory()[3]))}GB/{deci((virtual_memory()[0]))}GB [{virtual_memory()[2]}%]"
        drives_display['text'] = drives_values
        window.after(125, analyse)

    def deci(nmb: float):
        if round(nmb / 10 ** 7) == 0:
            return 0
        else:
            entier, decimal = str(nmb/ 10 ** 9).split(".")
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

    ram = Label(window, text=f"Ram: {deci((virtual_memory()[3] / 2 ** 30))}GB/{deci((virtual_memory()[0] / 2 ** 30))}GB [{virtual_memory()[2]}%]", font=("Courrier", 13, "bold"), bg=content['first'], fg=content['second'])
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
