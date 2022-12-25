import psutil
import socket
#import cpuinfo
from tkinter import *

def main():
    def display():
        ram_title.pack(pady=2, padx=5)
        ram_value.pack(pady=2, padx=5, fill=X)
        #cpu_title.pack(pady=2, padx=5)
        #cpu_value.pack(pady=2, padx=5, fill=X)
        disk_title.pack(pady=2, padx=5)
        disk_value.pack(pady=2, padx=5, fill=X)

    def remove():
        try:
            ram_title.pack_forget()
            ram_value.pack_forget()
            # cpu_title.pack_forget()
            # cpu_value.pack_forget()
            disk_title.pack_forget()
            disk_value.pack_forget()
        except:
            print()
        try:
            ram_used.pack_forget()
            total_ram_title.pack_forget()
            total_ram_value.pack_forget()
        except:
            print()
        try:
            disk_used.pack_forget()
            disk_title_used.pack_forget()
            total_disk_title.pack_forget()
            total_disk_value.pack_forget()
        except:
            print()

    #def cpu_display():
    #    remove()

    def ram_display():
        remove()
        global total_ram_title, total_ram_value
        ram_title.pack(pady=2, padx=5)
        ram_used.pack(pady=2, padx=5, fill=X)
        total_ram_title = Label(frame_left, text="Total Ram:", font=("Courrier", 15), fg="white", bg="#21252B")
        total_ram_title.pack(pady=2, padx=5)
        total_ram_value = Label(frame_right, text=f"{ref_deci((psutil.virtual_memory()[0] / 1000000000)-1.5)}GB", font=("Courrier", 15), bg="white", fg="#21252B")
        total_ram_value.pack(pady=2, padx=5, fill=X)

    def storage_display():
        remove()
        global total_disk_title, total_disk_value
        disk_title_used.pack(pady=2, padx=5)
        disk_used.pack(pady=2, padx=5, fill=X)
        total_disk_title = Label(frame_left, text="Total Disk:", font=("Courrier", 15), fg="white", bg="#21252B")
        total_disk_title.pack(pady=2, padx=5)
        total_disk_value = Label(frame_right, text=f"{int((storage.total / 2 ** 30))}Go", font=("Courrier", 15), bg="white", fg="#21252B")
        total_disk_value.pack(pady=2, padx=5, fill=X)

    def analyse():
        #cpu_value['text'] = f"{psutil.cpu_percent(4)}%"
        ram_value['text'] = f"{ref_deci((psutil.virtual_memory()[3] / 2 ** 30)-1.5)}GB/{ref_deci((psutil.virtual_memory()[0] / 2 ** 30)-1.5)}GB [{psutil.virtual_memory()[2]}%]"
        ram_used['text'] = f"{ref_deci((psutil.virtual_memory()[3] / 2 ** 30)-1.5)}GB [{psutil.virtual_memory()[2]}%]"
        disk_value['text'] = f"{int(storage.used / 2 ** 30)}Go/{int(storage.total / 2 ** 30)}Go [{int((storage.used / 2 ** 30)/(storage.total / 2 ** 30)*100)}%]"
        disk_used['text'] = f"{int(storage.used / 2 ** 30)}Go [{int((storage.used / 2 ** 30)/(storage.total / 2 ** 30)*100)}%]"
        window.after(100, analyse)

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

    # cpu = cpuinfo.get_cpu_info()['brand_raw']
    storage = psutil.disk_usage('/')

    window = Tk()
    menu = Menu(window)
    window.config(bg="#21252B", menu=menu)
    window.iconbitmap("icon.ico")
    window.minsize(375, 75)
    window.maxsize(375, 75)
    window.geometry("375x75")
    window.title(socket.gethostname())

    frame = Frame(window, bg="#21252B")
    frame.pack(expand=YES)
    frame_left = Frame(frame, bg="#21252B")
    frame_left.pack(side=LEFT, fill=X)
    frame_right = Frame(frame, bg="#21252B")
    frame_right.pack(side=RIGHT, fill=X)
    ram_title = Label(frame_left, text="Ram:", font=("Courrier", 15), fg="white", bg="#21252B")
    ram_value = Label(frame_right, text=f"{ref_deci((psutil.virtual_memory()[3] / 2 ** 30)-1.5)}GB/{ref_deci((psutil.virtual_memory()[0] / 2 ** 30)-1.5)}GB [{psutil.virtual_memory()[2]}%]", font=("Courrier", 15), bg="white", fg="#21252B")
    # cpu_title = Label(frame_left, text="CPU:", font=("Courrier", 15), fg="white", bg="#21252B")
    # cpu_value = Label(frame_right, text=f"", font=("Courrier", 15), bg="white", fg="#21252B")
    disk_title = Label(frame_left, text="Disk used:", font=("Courrier", 15), fg="white", bg="#21252B")
    disk_value = Label(frame_right, text=f"{int(storage.used / 2 ** 30)}Go/{int(storage.total / 2 ** 30)}Go [{int((storage.used / 2 ** 30)/(storage.total / 2 ** 30)*100)}%]", font=("Courrier", 15), bg="white", fg="#21252B")

    ram_used_title = Label(frame_left, text="Ram Used:", font=("Courrier", 15), bg="#21252B", fg="white")
    disk_title_used = Label(frame_left, text="Disk Used:", font=("Courrier", 15), bg="#21252B", fg="white")
    ram_used = Label(frame_right, text=f"{ref_deci((psutil.virtual_memory()[3] / 2 ** 30)-1.5)}GB [{psutil.virtual_memory()[2]}%]", font=("Courrier", 15), bg="white", fg="#21252B")
    disk_used = Label(frame_right, text=f"{int(storage.used / 2 ** 30)}Go [{int((storage.used / 2 ** 30)/(storage.total / 2 ** 30)*100)}%]", font=("Courrier", 15), bg="white", fg="#21252B")

    display()
    # cpu_btn = Menu(menu)
    # menu.add_cascade(label='CPU', command=cpu_display)
    acceuil_btn = Menu(menu)
    menu.add_cascade(label='All', command=lambda: [remove(), display()])
    ram_btn = Menu(menu)
    menu.add_cascade(label='RAM', command=ram_display)
    storage_btn = Menu(menu)
    menu.add_cascade(label='Storage', command=storage_display)
    window.after(1000, analyse)
    window.mainloop()

if __name__ == "__main__":
    main()
