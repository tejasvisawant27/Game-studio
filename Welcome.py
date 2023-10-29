from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from subprocess import call
import pymysql
import requests 



root = Tk() 
root.title('welcome')  
root.geometry('470x560+400+60')

Label(root, text = 'WELCOME TO THE GAME STUDIO', font =('Verdana', 15)).pack(side = TOP, pady = 10)
  
def fun():  
    messagebox.showinfo("Hello", "Start!!!")
    root.destroy
    import snake 

photo = PhotoImage(file = "slogo.png")
photoimage = photo.subsample(4, 4)
      
b1 = Button(root,text = "Snake Game",command = fun,image = photoimage,compound =TOP)
b1.place(x=20,y=100)

def fun2():
    messagebox.showinfo("Hello", "Start!!!")
    #root.destroy()
    import WordWipe

photo2 = PhotoImage(file = "Word.png")
photoimage2 = photo2.subsample(4, 4)    

b2 = Button(root, text = " WordWipe Game  ",command= fun2,image = photoimage2,compound =TOP)
b2.place(x=300,y=100)


def fun3():
    messagebox.showinfo("Hello", "Start!!!")
    #root.destroy()
    import xo
photo3 = PhotoImage(file = "xox.png")
photoimage3 = photo3.subsample(4, 4)    

    
    
b3 = Button(root, text = "Tic-Tac-Toe",command= fun3,image = photoimage3,compound =TOP,padx=30,pady=20)
b3.place(x=20,y=300)


def fun4():
    messagebox.showinfo("Hello", "Start!!!")
    #root.destroy()
    import suduko

photo4 = PhotoImage(file = "suduku.png")
photoimage4 = photo4.subsample(4, 4)     
  
b4 = Button(root, text = "Suduko",command= fun4,image = photoimage4,compound =TOP)
b4.place(x=300,y=290) 

def fun5():
    messagebox.showinfo("Hello", "Do you Want to Go Back?")
    root.destroy()
    import login

photo5 = PhotoImage(file = "back.png")
photoimage5 = photo5.subsample(4, 4)     
      

b5 = Button(root, text = "Back",command=fun5,image = photoimage5) 
b5.place(x=250,y=500)   

def fun6():
    messagebox.showinfo("Hello", "Do you Want to Go QUIT")
    root.destroy()
    

photo6 = PhotoImage(file = "quit.png")
photoimage6 = photo6.subsample(4, 4)     
      

b6 = Button(root, text = "Quit!!",command=fun6,image = photoimage6) 
b6.place(x=150,y=500)   


  
root.mainloop()


