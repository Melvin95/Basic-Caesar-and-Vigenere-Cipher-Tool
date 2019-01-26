'''
BASIC UI
'''
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import main_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Crypto_Tool (root)
    main_support.init(root, top)
    root.mainloop()

w = None
def create_Crypto_Tool(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Crypto_Tool (w)
    unknown_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Crypto_Tool():
    global w
    w.destroy()
    w = None


class Crypto_Tool:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = 'white'  # X11 color: 'gray85'
        _fgcolor = 'white'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'

        top.geometry("1099x628+496+92")
        top.title("Crypto Tool")
        top.configure(background="white")
        top.configure(highlightbackground="#4b4e68")
        top.configure(highlightcolor="#4b4e68")


        self.Label1 = Text(top)
        self.Label1.place(relx=0.073, rely=0.04, relheight=0.627, relwidth=0.404)
        self.Label1.configure(font="TkMenuFont")
        self.Label1.insert('1.0',"ENTER TEXT HERE:")
        self.Label1.configure(state=DISABLED)

        self.Label2 = Text(top)
        self.Label2.place(relx=0.2, rely=0.732, relheight=0.054, relwidth=0.2)
        self.Label2.configure(font="TkMenuFont")
        self.Label2.insert('1.0',"ENTER KEY HERE:")
        self.Label2.configure(state=DISABLED)

        self.Label3 = Text(top)
        self.Label3.place(relx=0.18, rely=0.844, relheight=0.054, relwidth=0.2)
        self.Label3.configure(font="TkMenuFont")
        self.Label3.insert('1.0',"SELECT AN OPTION:")
        self.Label3.configure(state=DISABLED)

        self.Label4 = Text(top)
        self.Label4.place(relx=0.537, rely=0.01, relheight=0.627, relwidth=0.404)
        self.Label4.configure(font="TkMenuFont")
        self.Label4.configure(state=DISABLED)

        self.menubar = Menu(top,font="TkMenuFont",bg='#4b4e68',fg='#4b4e68')
        top.configure(menu = self.menubar)

        self.UserText = Entry(top)
        self.UserText.place(relx=0.073, rely=0.08, relheight=0.627
                , relwidth=0.404)
        self.UserText.configure(background="#4b4e68")
        self.UserText.configure(font="TkTextFont")
        self.UserText.configure(foreground="black")
        self.UserText.configure(highlightbackground="#d9d9d9")
        self.UserText.configure(highlightcolor="black")
        self.UserText.configure(insertbackground="black")
        self.UserText.configure(selectbackground="#c4c4c4")
        self.UserText.configure(selectforeground="black")
        self.UserText.configure(width=444)

        self.CrypText = Text(top)
        self.CrypText.place(relx=0.537, rely=0.08, relheight=0.627
                , relwidth=0.404)
        self.CrypText.configure(background="#4b4e68")
        self.CrypText.configure(font="TkTextFont")
        self.CrypText.configure(foreground="black")
        self.CrypText.configure(highlightbackground="#d9d9d9")
        self.CrypText.configure(highlightcolor="black")
        self.CrypText.configure(insertbackground="black")
        self.CrypText.configure(selectbackground="#c4c4c4")
        self.CrypText.configure(selectforeground="black")
        self.CrypText.configure(width=444)
        self.CrypText.configure(wrap=WORD)
        self.CrypText.configure(state=DISABLED)

        self.KeyText =  Entry(top)
        self.KeyText.place(relx=0.3, rely=0.732, relheight=0.054, relwidth=0.404)
        self.KeyText.configure(background="#4b4e68")
        self.KeyText.configure(font="TkTextFont")
        self.KeyText.configure(foreground="black")
        self.KeyText.configure(highlightbackground="#d9d9d9")
        self.KeyText.configure(highlightcolor="black")
        self.KeyText.configure(insertbackground="black")
        self.KeyText.configure(selectbackground="#c4c4c4")
        self.KeyText.configure(selectforeground="black")
        self.KeyText.configure(width=444)

        self.SubmitButton = Button(top,command=self.submission)
        self.SubmitButton.place(relx=0.764, rely=0.828, height=64, width=217)
        self.SubmitButton.configure(activebackground="#d8d8d8")
        self.SubmitButton.configure(activeforeground="#f7f7f7")
        self.SubmitButton.configure(background="#4b4e68")
        self.SubmitButton.configure(disabledforeground="#a3a3a3")
        self.SubmitButton.configure(foreground="#000000")
        self.SubmitButton.configure(highlightbackground="#d9d9d9")
        self.SubmitButton.configure(highlightcolor="black")
        self.SubmitButton.configure(pady="0")
        self.SubmitButton.configure(text='''GO''')
        self.SubmitButton.configure(width=217)

        self.Options = ["CAESAR ENCRYPTION","CAESAR DECRYPTION",
                        "VIGENERE ENCRYPTION","VIGENERE DECRYPTION",
                        "BREAK CAESAR","BREAK VIGENERE"]

        self.variable = StringVar(top)
        self.variable.set(self.Options[0])

        self.DropList = OptionMenu(top,self.variable,*self.Options)
        self.DropList.place(relx=0.3, rely=0.84, relheight=0.054, relwidth=0.404)
        #self.DropList.pack()

    def submit_text(self,text):
        self.CrypText.configure(state=NORMAL) #allow label to be edited
        self.CrypText.delete('1.0',END) #delete any text from previous submission
        self.CrypText.insert('1.0',text) #insert text
        self.CrypText.configure(state=DISABLED) #make non-editable

    def submission(self):
        try:
            user_text = self.UserText.get()
            key = self.KeyText.get()
            option = self.variable.get()
            self.helper_submission(user_text,key,option)
        except Exception as e:
            print(e)

    def submit_key(self,key):
        try:
            self.Label4.configure(state=NORMAL)
            self.Label4.delete('1.0',END)
            self.Label4.insert('1.0',str(key))
            self.Label4.configure(state=DISABLED)
        except Exception as e:
            print(e)

    def helper_submission(self,text=None,key=None,option=None):
        import caesar_cipher as CAESAR
        import vigenere_cipher as VIGENERE
        ctext = ""
        if option=="CAESAR ENCRYPTION":
            ctext = CAESAR.encrypt(text,int(key)) #display
        elif option=="CAESAR DECRYPTION":
            ctext = CAESAR.decrypt(text,int(key))
        elif option=="VIGENERE ENCRYPTION":
            ctext = VIGENERE.encrypt(text,key)
        elif option=="VIGENERE DECRYPTION":
            ctext = VIGENERE.decrypt(text,key)
        elif option=="BREAK CAESAR":
            key = CAESAR.breakCaesar(text)
            ctext = CAESAR.decrypt(text,key)
            self.submit_key(key)
        else:
            key = VIGENERE.breakVigenere(text)
            ctext = VIGENERE.decrypt(text,key)
            self.submit_key(key)

        self.submit_text(ctext)

if __name__ == '__main__':
    vp_start_gui()
