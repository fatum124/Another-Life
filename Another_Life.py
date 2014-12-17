"""
PSIT Project 2014 : Another Life
Author :   57070124 Sarandar Foongyai 
            57070139 Achiraya Songput
KMITL : King Mongkut's Institute of Technology Ladkrabang
"""

from Tkinter import *
import datetime

class About(Toplevel):
    """docstring for About"""
    def __init__(self):
        Toplevel.__init__(self)
        
        self.frame1 = Frame(self, bg = '#19392b', width = 340, height = 100)
        self.frame2 = Frame(self, bg = '#a5ffd8', width = 340, height = 150)
        self.text1 = Label(self, text = 'Another Life', fg='white', bg='#19392b', font = ('Arial', 30, 'bold'))
        self.text2 = Label(self, text = 'PSIT Project 2014', fg = 'white', bg = '#19392b', font = ('Arial', 10, 'bold'))
        self.text3 = Label(self, text = 'Author :', bg = '#a5ffd8', font = ('Arial', 16))
        self.text4 = Label(self, text = '57070124 Sarandar Foongyai', bg = '#a5ffd8', font = ('Arial', 10))
        self.text5 = Label(self, text = '57070139 Achiraya Songput', bg = '#a5ffd8', font = ('Arial', 10))
        self.text6 = Label(self, text = 'King Mongkut\'s Institute of Technology Ladkrabang', fg = '#587f6e', bg = '#a5ffd8', font = ('Arial', 10))

        self.frame1.place(x = 0, y = 0)
        self.frame2.place(x = 0, y = 100)
        self.text1.place(x = 55, y = 10)
        self.text2.place(x = 100, y = 65)
        self.text3.place(x = 40, y = 130)
        self.text4.place(x = 123, y = 135)
        self.text5.place(x = 123, y = 165)
        self.text6.place(x = 15, y = 210)        
        
class Home(Tk):
    def __init__(self):
        """home"""
        root = Tk()
        root.geometry("450x550")
        root.title("Another Life")
        root.resizable(0, 0)
        #--root bg
        photo_bg = PhotoImage(file = "Picture/BG01.gif")
        root = Label(image = photo_bg)
        root.pack()

        #--date
        now_date = Label(bg = 'white', text = self.date_main())
        now_date.place(x = 55, y = 90)

        #--botton
        photo_bot1 = PhotoImage(file = "Picture/bot1.gif")
        photo_bot2 = PhotoImage(file = "Picture/bot2.gif")
        #photo_bot3 = PhotoImage(file = "picture/bot3.gif")

        b1 = Button(image = photo_bot1, bg = '#a5ffd8', relief = FLAT, command = self.add_b)
        #b2 = Button(image = photo_bot3, bg = '#a5ffd8', relief = FLAT, state=DISABLED)
        b3 = Button(image = photo_bot2, bg = '#a5ffd8', relief = FLAT, command = self.about_b)
        b1.place(x = 335, y = 130)
        #b2.place(x = 335, y = 265)
        b3.place(x = 335, y = 400)

        self.gole_today()

        root.mainloop()
    
    def date_main(self):
        date_d = datetime.date.today().strftime("%d")
        date_m = datetime.date.today().strftime("%B")
        date_y = datetime.date.today().strftime("%Y")
        return date_d, date_m, date_y

    def about_b(self):
        about_win = About()
        about_win.geometry("340x250")
        about_win.title("About")
        about_win.resizable(0, 0)

    def add_b(self):
        #self.destroy()
        add_win = Tk()#Add_goal()
        add_win.geometry("300x200")
        add_win.title("Create new gole")
        add_win.resizable(0, 0)

        new_goal = StringVar()
        n_goal = Entry(add_win, width = 33)
        n_goal.place(x = 40, y = 100)
        new_goal.set("your a new gole")

        frame = Frame(add_win, bg = '#19392b', width = 300, height = 80)
        name = Label(add_win, text = 'Create New', fg='white', bg='#19392b', font = ('Arial', 30, 'bold'))
        frame.place(x = 0, y = 0)
        name.place(x = 50, y = 10)

        self.b1 = Button(add_win, text = "Ok", command = lambda : self.add_n(n_goal.get(), add_win), padx = 20, pady = 5, bg = 'lightgreen', fg = 'white')
        self.b2 = Button(add_win, text = "Cancle", command = add_win.destroy, padx = 15, pady = 5, bg = 'lightgreen', fg = 'white')
        
        
        self.b1.place(x = 50, y = 150)
        self.b2.place(x = 175, y = 150)
        add_win.mainloop()

    def add_n(self, goal_now, add_win):
        gole_list[goal_now] = 0
        #print gole_list
        self.gole_today()
        add_win.destroy()

    def up(self, event):
        widget = event.widget
        index = int(widget.curselection()[0])
        value = widget.get(index)
        global select
        select = value

        ans = select[:-10]
        gole_list[ans] += 1
        self.gole_today()

    def connext(self):
        for chack in gole_list:
            if gole_list[chack] == 21:
                chack_T = chack
                break
        gole_list.pop(chack_T)
        self.gole_today()

    def gole_today(self):
        today_gole = Listbox(bg = 'white', width = 40, height = 19)
        #today_gole = ()
        today_gole.place(x = 38, y = 190)
        if 21 in gole_list.values():
            self.connext()
        for i in gole_list:
            o = ""
            if gole_list[i] < 10:
                o = "0"
            today_gole.insert(END, i + " (" + o +str(gole_list[i]) + " / 21)")

        global select
        select = 0
        today_gole.bind("<Double-Button-1>", lambda event: self.up(event))
        
gole_list = {"ex1" : 1, "ex2" : 20, "ex3" : 3}
Home()
