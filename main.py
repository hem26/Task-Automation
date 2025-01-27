import shutil, os
import re
import pyperclip
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory
import ttkbootstrap as ttk

# window
window = ttk.Window(themename='vapor')
#window.iconbitmap("Project-1\logo1.ico")
window.title("Leapify - Your Desktop Automation Tool")
window.geometry("500x500")
window.minsize(500, 500)
window.resizable(False, False)

def tab1():
    def tab2():
        frame1.destroy()
        frame2.destroy()
        
        def folder_dialog_box():
            global folderpath
            folderpath = askdirectory()
            tab2label2.configure(text=folderpath, font=('Times_New_Roman', 9))
            
        def ZipBackup():
            if not os.path.exists(folderpath):
                print(f"Error: The source folder {folderpath} does not exist")
                return
            shutil.make_archive(tab2entry1.get(), 'zip', folderpath)

            tab2label4.configure(text=f"Backup Created'")


        tab2frame = ttk.Frame(window)
        tab2label1 = ttk.Label(tab2frame, text="Enter your source folder: ", font=('Times_New_Roman', 14))

        tab2label2Var = tk.StringVar()
        tab2label2 = ttk.Label(tab2frame, width=40)

        tab2selectFolder = ttk.Button(tab2frame, text="select folder", command=folder_dialog_box)

        tab2label3 = ttk.Label(tab2frame, text='Enter the name of backup folder', font=('Times_New_Roman',14))
        tab2entry1 = ttk.Entry(tab2frame, width=40)
        
        #Label to display the backup is created
        tab2label4 = ttk.Label(tab2frame, width=40, font=('Times_New_Roman', 12))

        # button to backup the folder
        def back():
            tab2frame.destroy()
            tab1()
        
        
        tab2BackupButton = ttk.Button(tab2frame, text="Backup to Zip File", command=ZipBackup)
        tab2back = ttk.Button(tab2frame, text='Back', command=back)
       

        tab2label1.pack(side="top", pady=40)
        tab2label2.pack(side='top', pady=10, expand=True)
        tab2selectFolder.pack(side='top', pady=10)
        tab2label3.pack(side="top", pady=10)
        tab2entry1.pack(side="top")
        tab2back.pack(side="top")
        tab2BackupButton.pack(side="bottom", pady=70)
        
        tab2label4.pack(side="top")
        tab2frame.pack(side='top')

    def emailAddressExtractor():
        text = str(pyperclip.paste())
        emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+
        @
        [a-zA-Z0-9.-]+
        (\.[a-zA-Z]{2,4})           
    )''', re.VERBOSE)

# Find matches in clipboard text. 
        matches = []

        for groups in emailRegex.findall(text):
            matches.append(groups[0])

        # Copy results to the clipboard.
        if len(matches) >0:
            pyperclip.copy('\n'.join(matches))
            # print('Copied to clipboard')
            # print('\n'.join(matches))
            label1.configure(text=f"Found emails: {' '.join(matches)}")
        else:
            label1.configure(text=f"No email addresses found")

    frame1=  ttk.Frame(window)
    frame2 = ttk.Frame(window)
    button1 = ttk.Button(frame1, text='Extract Email Addresses', command = emailAddressExtractor)
    button2 = ttk.Button(frame1, text='Backup to Zip File', command=tab2)

    button1.pack(side='left',expand=True, fill='both')
    button2.pack(side='left',expand=True, fill='both')

    label1 = ttk.Label(frame2, text="Label1")
    label1.pack(side="top", expand=True, fill='both')

    frame1.pack(side='top',padx=10, expand=True, fill='both')
    frame2.pack(side='top',expand=True, fill='both')
tab1()
window.mainloop()
