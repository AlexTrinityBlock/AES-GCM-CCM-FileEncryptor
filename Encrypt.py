import tkinter as tk
import argparse
from tkinter import filedialog
from util.CryptUtil import *
from sys import exit

aesKey=bytes()
root= tk.Tk()
root.protocol("WM_DELETE_WINDOW",exit)
root.title("AES-GCM-CCM-FileEncryptor")

#Parameter
parser = argparse.ArgumentParser("python3 client.py")
parser.add_argument("--GCM", help="use AES GCM on your chat room",action="store_true")
parser.add_argument("--CCM", help="use AES CCM on your chat room",action="store_true")
args = parser.parse_args()

if args.CCM:
	AES_MODE = "CCM"
else:
	AES_MODE = "GCM"

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
AESFileEncrypt(encryptFilePath,encryptFilePath+".cipher",aesKey,AES_MODE)