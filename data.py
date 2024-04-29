import mysql.connector as mysql
import tkinter as gui
import tkinter.messagebox

cn = mysql.connect(database = "userdatabase1", user = "root", password = "Srini@12345@")
w = gui.Tk()
w.geometry("300x200")

def save(e1, e2, e3, e4):
    rno = e1.get()
    name = e2.get()
    s1 = int(e3.get())
    s2 = int(e4.get())
    
    c= cn.cursor()
    
    try:
        c.execute("INSERT INTO student_marks (rollno, name, s1, s2) ,VALUES (%s, %s, %s, %s)",(rno, name, sub1, sub2))
        cn.commit()
        tkinter.messagebox.showinfo(title="Info", message = "Marks details are saved")
        e1.delete(0, gui.END)
        e2.delete(0, gui.END)
        e3.delete(0, gui.END)
        e4.delete(0, gui.END)
        
    except mysql.Error as e:
        tkinter.messagebox.showerror(title="Error",
                                    message="Error saving marks : {}".format(e))
        
def marks_window():
    w1 = gui.Toplevel(w)
    w1 =geometry("300x200")
    
    l1 = gui.Label(w1, text ="Rollno", font=("Arial", 14))
    l2 = gui.Label(w1, text ="Name", font=("Arial", 14))
    l3 = gui.Label(w1, text ="Subject1", font=("Arial", 14))
    l4 = gui.Label(w1, text ="Subject2", font=("Arial", 14))
    
    e1 = gui.Entry(w1, width=10)
    e2 = gui.Entry(w1, width=10)
    e3 = gui.Entry(w1, width=10)
    e4 = gui.Entry(w1, width=10)
    
    l1.grid(row=1, column=1)
    l2.grid(row=2, column=1)
    l3.grid(row=3, column=1)
    l4.grid(row=4, column=1)
    e1.grid(row=1, column=2)
    e2.grid(row=2, column=2)
    e3.grid(row=3, column=2)
    e4.grid(row=4, column=2)
    
    b1 = gui.Button(w1, text="Save", commad=lambda: save(e1, e2, e3, e4))
    b1.grid(row5, column=1)
    
def find_window():
    w3 = gui.Toplevel(w)
    w3.geometry("300x200")
    w3.title("Find Result")
    
    l1 = gui.Label(w3, text="Rollno", font=("Arial", 14))
    e1 = gui.Entry(w3, width=10)
    
    l1.grid(row = 1, column = 1)
    e1.grid(row = 1, column = 2)
    
    def find():
        c = cn.cursor()
        
        c.execte("SELECT rollno, name, sub1, sub2, sub1 + sub2 FROM stundent_marks WHERE rollno = %s", (e1.get(),))
        row = c.fetchoone()
        
        if row is None:
            tkinter.messagebox.showinfo(title="Info", message = "Invalid Rollno")
            
        else:
            result = "pass" if row[2] >= 40 and row[3] >= 40 else "fall"
            a = map(str, row)
            s = "".join(a)
            s = s + " " + result
            
            l2 = gui.Label(w3, text=s, font=("Arial", 14))
            l2.grid(row = 2 , column = 1)
            
        b1 = gui.Button(w3, text="Find Result", command=find)
        b1.grid(row=2, column=1)
    
    def on_closing():
        cn.close()
        w.destroy()
        
    b1 = gui.Button(w, text = "Marks Entry", font=("Arial", 14), command = marks_window)
    b2 = gui.Button(w, text = "Find Result", font=("Arial", 14), command=find_window)
    
    b1.pack(fill=gui.BOTH, expand=True)
    b2.pack(fill=gui.BOTH, expand=True)
    
    w.protocol("WM_DELETE_WINDOW", on_closing)
    w.mainloop()
    cn.close()
