import psutil
from tkinter import *

def main():

    def analyse():
        ram_value['text'] = f"{ref_deci((psutil.virtual_memory()[3] / 2 ** 30))}GB/{ref_deci((psutil.virtual_memory()[0] / 2 ** 30))}GB [{psutil.virtual_memory()[2]}%]"
        disk_value['text'] = f"{int(storage.used / 2 ** 30)}Go/{int(storage.total / 2 ** 30)}Go [{int((storage.used / 2 ** 30) / (storage.total / 2 ** 30) * 100)}%]"
        window.after(125, analyse)

    def ref_deci(nmb: float):
        entier, decimal = str(nmb).split(".")
        tour = 0
        new_decimale = ""
        for i in decimal:
            if tour == 2:
                new_decimale += "."
            new_decimale += str(i)
            tour += 1

        return float(f"{entier}.{str(round(float(new_decimale)))}")

    storage = psutil.disk_usage('/')
    window = Tk()
    window.overrideredirect(True)
    window.wm_attributes("-topmost", True)
    window.wm_attributes("-disabled", True)
    window.config(bg="#252525")
    window.geometry("375x90")

    frame = Frame(window, bg="#252525")
    frame.pack(expand=YES)
    frame_left = Frame(frame, bg="#252525")
    frame_left.pack(side=LEFT, fill=X)
    frame_right = Frame(frame, bg="#252525")
    frame_right.pack(side=RIGHT, fill=X)
    ram_title = Label(frame_left, text="Ram:", font=("Courrier", 15), fg="white", bg="#252525")
    ram_value = Label(frame_right, text=f"{ref_deci((psutil.virtual_memory()[3] / 2 ** 30))}GB/{ref_deci((psutil.virtual_memory()[0] / 2 ** 30))}GB [{psutil.virtual_memory()[2]}%]", font=("Courrier", 15), bg="white", fg="#252525")
    ram_title.pack(pady=2, padx=5)
    ram_value.pack(pady=2, padx=5, fill=X)
    disk_title = Label(frame_left, text="Disk used:", font=("Courrier", 15), fg="white", bg="#252525")
    disk_title.pack(pady=2, padx=5)
    disk_value = Label(frame_right, text=f"{int(storage.used / 2 ** 30)}Go/{int(storage.total / 2 ** 30)}Go [{int((storage.used / 2 ** 30) / (storage.total / 2 ** 30) * 100)}%]", font=("Courrier", 15), bg="white", fg="#252525")
    disk_value.pack(pady=2, padx=5, fill=X)

    window.after(125, analyse)
    window.mainloop()

if __name__ == "__main__":
    main()
