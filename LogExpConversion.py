import tkinter as tk


class LogExpConversionCalc:

    def __init__(self):

        self.root = tk.Tk()

        self.labLog = tk.Label(self.root, text = "Log")
        self.labLog.grid(row = 0, column = 0)

        self.entN = tk.Entry(self.root, width = 1)
        self.entN.grid(row = 1,column  = 1)

        self.entX = tk.Entry(self.root,width = 3)
        self.entX.grid(row = 0, column = 2)

        self.labEqu = tk.Label(self.root, text = "=")
        self.labEqu.grid(row = 0, column = 3)

        self.entA = tk.Entry(self.root,width = 4)
        self.entA.grid(row = 0, column = 4)

        self.butSub = tk.Button(self.root,text = "Submit")
        self.butSub.grid(row = 2,column = 0,columnspan = 5,sticky = "NESW")


        self.root.mainloop()


game = LogExpConversionCalc()