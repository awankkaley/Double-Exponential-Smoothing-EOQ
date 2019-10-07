import tkinter as tk
import tkinter.ttk as ttk
import time
import sys


class ProgressBar:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('250x50+20+20')
        self.root.title('Sixty Seconds progress bar')

        self.max = 120
        self.step = tk.DoubleVar()
        self.step.set(0)
        self.progbar = ttk.Progressbar

        self.frame = tk.Frame()
        self.frame.pack(fill=tk.BOTH, padx=2, pady=2)
        btn = tk.Button(self.frame, text='Start', bd=4, command=self.start_progbar)
        btn.pack()
        self.root.mainloop()

    def add_progbar(self):
        self.progbar = ttk.Progressbar(
            self.frame,
            orient=tk.HORIZONTAL,
            mode='determinate',
            variable=self.step,
            maximum=self.max)
        self.progbar.pack(fill=tk.X, expand=True)

    def start_progbar(self):
        self.add_progbar()
        for x in range(0, 120, 2):
            self.step.set(x)
            time.sleep(.1)
            self.root.update()
        self.progbar.destroy()


if __name__ == '__main__':
    ProgressBar()