import tkinter as tk
from tkinter import filedialog, Text
import os

apps = []
def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="C:/",title="Select File", filetypes=(("executables","*.exe"),("all files","*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for ap in apps:
        os.startfile(app)

#root element
root = tk.Tk()
#canvas in root
canvas = tk.Canvas(root, height=700, width=700, bg="#263d42")
canvas.pack()
#frame in root
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.7, relheight=0.7, relx=0.1, rely=0.1)
#button to select .exe file
openFile = tk.Button(root, text="Open File", padx=10, pady=10, fg="white", bg="#263D42", command=addApp)
openFile.pack()
#button to run the selected .exe
runApps = tk.Button(root, text="Run Apps", padx=10, pady=10, fg="white", bg="#263D42", command=runApps)
runApps.pack()
#render the root
root.mainloop()