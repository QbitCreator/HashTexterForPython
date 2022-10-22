
import tkinter as tk
import hashTexterFunction as hashtxt

def encrypt():
  ciphertext.delete("1.0", tk.END)
  ciphertext.insert("1.0", hashtxt.encrypt(password.get().rstrip(), cleartext.get("1.0", tk.END).rstrip()))

def decrypt():
  cleartext.delete("1.0", tk.END)
  cleartext.insert("1.0", hashtxt.decrypt(password.get().rstrip(), ciphertext.get("1.0", tk.END)))

def get_pos(event):
  global ywin
  global xwin
  xwin = window.winfo_x()
  ywin = window.winfo_y()
  startx = event.x_root
  starty = event.y_root
  ywin = ywin - starty
  xwin = xwin - startx

def move_window(event):
  window.geometry('+{0}+{1}'.format(event.x_root + xwin, event.y_root + ywin))
  startx = event.x_root
  starty = event.y_root
    
window = tk.Tk()
window.configure(bg="black")
window.title("HashTexter by Leif-Erik Hallmann")
window.iconbitmap('hashcryptorlogo.ico')
window.overrideredirect(True)
window.geometry("1500x400")


heading = tk.Label(text="HashTexter by Leif-Erik Hallmann", fg="#22ff22", bg="#222", font=("Courier New", 30), height=2, width=35)
cleartextlabel = tk.Label(text="Cleartext:", fg="#22ff22", bg="black", font=("Courier New", 20))
cleartext = tk.Text(height=8)
passwordlabel = tk.Label(text="Password:", fg="#22ff22", bg="black", font=("Courier New", 20))
password = tk.Entry(font=("Courier New", 14))
ciphertextlabel = tk.Label(text="Ciphertext:", fg="#22ff22", bg="black", font=("Courier New", 20))
ciphertext = tk.Text(height=8)
encrypt = tk.Button(text=">>>Encrypt!>>>", width=15, height=2, bg="#777", fg="#22ff22", font=("Courier New", 20), command=encrypt)
decrypt = tk.Button(text="<<<Decrypt!<<<", width=15, height=2, bg="#777", fg="#22ff22", font=("Courier New", 20), command=decrypt)
exit_button = tk.Button(text="EXIT", width=15, height=2, bg="#777", fg="#22ff22", font=("Courier New", 20), command=window.destroy)
canvas = tk.Frame(window, bg='#333')

heading.grid(row=0, column=0)
cleartextlabel.grid(row=3, column=0)
cleartext.grid(row=4, column=0)
passwordlabel.grid(row=1, column=0)
password.grid(row=2, column=0)
decrypt.grid(row=5, column=1)
encrypt.grid(row=5, column=0)
ciphertextlabel.grid(row=3, column=1)
ciphertext.grid(row=4, column=1)
exit_button.grid(row=0, column=1)

heading.bind('<Button-1>', get_pos)
heading.bind('<B1-Motion>', move_window)


window.mainloop()



