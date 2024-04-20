import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import time
def muutus():
    tekst.pack(fill="both", expand=True)
def teave():
    messagebox.showinfo("Teave", "Kirju - Pythoniga tehtud kirjutamiseprogramm, mis on kerge! Versioon 0.2. Veebileht kauritarkvara.github.io/Kirjutamiseprogramm. Litsents on GNU GENERAL PUBLIC LICENSE 3")
def sule():
    def välju():
       exit()
    def jah():
        hoiatus.destroy()
        fail = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Tekstifailid", "*.txt"), ("Kõik failid", "*.*")])
        if fail:
          with open(fail, 'w') as file:
                   file.write(tekst.get("1.0", "end"))
                   exit()
    hoiatus = tk.Toplevel(aken)
    hoiatus.title("Kas salvestada?")
    miks = tk.Label(hoiatus, text="Kas salvestada?")
    miks.pack()
    ei = tk.Button(hoiatus, text="Ei", command=välju)
    ei.pack()
    jah = tk.Button(hoiatus, text="Jah", command=jah)
    jah.pack()
    hoiatus.mainloop()
def ava():
    file_path = filedialog.askopenfilename(filetypes=[("Tekstifailid", "*.txt"), ("Kõik failid", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            tekst.delete("1.0", "end")
            tekst.insert("1.0", file.read())
def salvesta():
    fail = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Tekstifailid", "*.txt"), ("Kõik failid", "*.*")])
    if fail:
        with open(fail, 'w') as file:
            file.write(tekst.get("1.0", "end"))
aken = tk.Tk()
aken.title("Kirju")
tekst = tk.Text(aken, wrap=tk.WORD, height=10, width=50)
tekst.pack(pady=10)
menüü = tk.Menu(aken)
valikfail=tk.Menu(menüü, tearoff=0)
valikfail.add_command(label="Salvesta", command=salvesta)
valikfail.add_command(label="Ava", command=ava)
valikfail.add_command(label="Välju", command=sule)
valikfail.add_command(label="Teave", command=teave)
menüü.add_cascade(label="Fail", menu=valikfail)
aken.configure(menu=menüü)
aken.protocol("WM_DELETE_WINDOW", sule)
aken.bind("<Control-s>", lambda event: salvesta())
aken.bind("<Control-o>", lambda event: ava())
aken.bind("<Configure>", lambda event: muutus())
aken.mainloop()
