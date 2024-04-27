import tkinter
import time

class StopWatch(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Stopwatch")
        self.configure(bg="black")
        self.resizable(False, False)
        self.iconbitmap("stopwatch.ico")

        self.start_time = 0
        self.elapsed_time = 0
        self.running = False

        self.time_var = tkinter.StringVar()
        self.time_var.set("00:00:00.00")

        self.label = tkinter.Label(self, textvariable=self.time_var, font=("Helvetica", 28), bg='black', fg='white')
        self.label.pack(padx=10, pady=10)

        self.start_stop_button = tkinter.Button(self, text="Start", command=self.start_stop, bg='gray30', fg='white', activebackground='gray40', activeforeground='white', relief=tkinter.FLAT, padx=10, pady=5, borderwidth=0)
        self.start_stop_button.pack(side=tkinter.LEFT, padx=5, pady=5, fill=tkinter.BOTH, expand=True)

        self.restart_button = tkinter.Button(self, text="Restart", command=self.restart, bg='gray30', fg='white', activebackground='gray40',activeforeground='white', relief=tkinter.FLAT, padx=10, pady=5, borderwidth=0)
        self.restart_button.pack(side=tkinter.LEFT, padx=5, pady=5, fill=tkinter.BOTH, expand=True)

        self.close_button = tkinter.Button(self, text="Close", command=self.close, bg='gray30', fg='white', activebackground='gray40',activeforeground='white', relief=tkinter.FLAT, padx=10, pady=5, borderwidth=0)
        self.close_button.pack(side=tkinter.LEFT, padx=5, pady=5, fill=tkinter.BOTH, expand=True)
        self.update_time()

    def start_stop(self):
        if self.running:
            self.running = False
            self.start_stop_button.config(text="Start")
        else:
            if not self.running:  
                self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.update_time()
            self.start_stop_button.config(text="Stop")

    def update_time(self):
        if self.running:
            current_time = time.time()
            self.elapsed_time = current_time - self.start_time
            hours = int(self.elapsed_time // 3600)
            minutes = int((self.elapsed_time % 3600) // 60)
            seconds = int(self.elapsed_time % 60)
            milliseconds = int((self.elapsed_time * 100) % 100)
            self.time_var.set("{:02d}:{:02d}:{:02d}.{:02d}".format(hours, minutes, seconds, milliseconds))
        self.after(10, self.update_time)

    def restart(self):
        self.elapsed_time = 0
        self.time_var.set("00:00:00.00")
        self.running = False
        self.start_stop_button.config(text="Start")

    def close(self):
        self.destroy()

if __name__ == "__main__":
    StopWatch().mainloop()