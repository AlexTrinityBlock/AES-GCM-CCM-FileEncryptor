import tkinter as tk
from tkinter import filedialog
from util.CryptUtil import *

aesKey=bytes()

root= tk.Tk()
root.title("AES-GCM-CCM-FileEncryptor")

#Page 1
page1 = tk.Canvas(root, width = 400, height = 150)
page1.pack()

InputSecretEntry = tk.Entry (root) 
page1.create_window(200, 50, window=InputSecretEntry)

InputSecretLabel = tk.Label(root, text="Input your secret")
page1.create_window(200, 20, window=InputSecretLabel)

def onClickFunc ():
    global aesKey
    aesKey = hash256(InputSecretEntry.get())
    root.destroy()
    
setSecretBtn = tk.Button(text='continue', command=onClickFunc)
page1.create_window(200, 100, window=setSecretBtn)

root.mainloop()

#Page 2
encryptFilePath = filedialog.askopenfilename(title='Select file')
AESGCMFileEncrypt(encryptFilePath,encryptFilePath+".cipher",aesKey)