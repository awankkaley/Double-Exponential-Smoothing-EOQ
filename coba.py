from tkinter import *

class Application(object):

    def __init__(self, event=None):

        self.root = Tk()

        self.root.configure(bg="darkorchid1", padx=10, pady=10)
        self.root.title("WELCOME")

        self.username = "Bob"

        self.welcome = Label(self.root, text="WELCOME TO MY PROGRAM", bg="lightgrey", fg="darkorchid1")
        self.welcome.pack()

        self.label0 = Label(self.root, text="ENTER NAME:", bg="purple", fg="white", height=5, width=50)
        self.label0.pack()

        self.entry = Entry(self.root, width=25)
        self.entry.configure(fg= "white",bg="grey20")
        self.entry.pack()
        self.root.bind("<Return>", self.submit)

        self.button = Button(self.root, text="SUBMIT", highlightbackground="green", width=48, command=self.submit)
        self.button.pack()

        self.button1 = None
        self.button2 = None
        self.attempts = 0

    def submit(self, event=None):
        username = self.entry.get()
        if username == self.username:
            if (self.button2 != None): # after I added disabling the submit button this check might not be necessary
                return
            if (self.button1 == None):
                self.button1 = Button(self.root, text='LOGIN', highlightbackground="green", width=28, command=self.root.destroy)
                self.button1.pack()
                self.root.bind("<Return>", self.login)
                self.button.config(state="disabled")
        else:
            if (self.button2 == None):
                self.button2 = Button(self.root, text="INCORRECT- CLICK TO DIMISS THIS MESSAGE", highlightbackground="red", width=48, command=self.incorrect)
                self.button2.pack()
                self.root.bind("<Return>", self.incorrect)
                self.button.config(state="disabled")

    def incorrect(self, event=None):
        self.attempts += 1
        if (self.attempts > 2):
            self.root.destroy()
        else:
            self.root.bind("<Return>", self.submit)
            self.button.config(state="normal")
            self.button2.destroy()
            self.button2 = None

    def login(self, event=None):
        self.root.destroy()

app=Application()

mainloop()