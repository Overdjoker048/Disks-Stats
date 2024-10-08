import psutil
import win32api
from tkinter import *

def analyse():
    drives = win32api.GetLogicalDriveStrings().split('\000')[:-1]

    #Retrieve the list of disks and retrieve the information
    storage = []
    for i in drives:
        try:
            storage.append(psutil.disk_usage(i))
        except PermissionError:
            storage.append("pass")

    #Format the text to display it on the gui
    drives_values = ""
    for i in range(len(storage)):
        if storage[i] != "pass":
            if i != 0:
                drives_values = drives_values + "\n"
            drives_values = f"{drives_values}({drives[i]}): {round(storage[i].used/10**9, 2)}Go/{round(storage[i].total/10**9, 2)}Go"

    #Update the storage display
    drives_display['text'] = drives_values
    #Restart the function
    window.after(200, analyse)

#Create the GUI
window = Tk()
window.overrideredirect(True)
window.config(bg="#1E1E1E")
window.wm_attributes("-topmost", True)
drives_display = Label(window, font=("Courrier", 11, "bold"), fg="#252525", bg="white", highlightbackground="#1E1E1E", highlightcolor="#1E1E1E", highlightthickness=2)
drives_display.pack()

#Allows you to close the page by pressing Ctrl+m
window.bind("<Control-m>", lambda event: window.destroy())
#Actualise l affichage des stockages
window.after(0, analyse)

#Display the GUI
window.mainloop()