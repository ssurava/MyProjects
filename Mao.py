import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import Listbox,Message,Button,Canvas
from PIL import Image,ImageTk
m = tk.Tk()
m.configure(background="blue")
m.title("This is Mao") 
ourMessage ='Mao, there are no rules'
messageVar = Message(m, text = ourMessage) 
messageVar.config(bg='orange') 
messageVar.pack( )



y = np.array(["1)Rule1","2)Rule2","3)Rule3","4)Rule4","5)Rule5","6)Rule6","7)Rule7"])
lb = Listbox(m)

def easy():
    x= np.random.randint(0,3)
    lb.insert(x,y[x])
    lb.pack()
        
def medium():
    x= np.random.randint(0,5)
    lb.insert(x,y[x])
    lb.pack()

def hard():
    x=np.random.randint(0,7)
    lb.insert(x,y[x])
    lb.pack()
        

        


b1= Button(m, text = "Easy",command = easy,activebackground = "pink",pady=10)  
b2 = Button(m, text = "Medium",command = medium,activebackground = "pink",pady = 10)  
b3= Button(m, text = "Hard",command = hard,activebackground = "pink",pady = 10)  
b1.pack()  
b2.pack()  
b3.pack() 

suits =["Hearts","Clubs","Spades","Diamonds"]  
numbers=[1,2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
deck=[]
for string in suits:
    for number in numbers:
      deck.append((string,number))
      print(deck[-1])
      

 
c=Canvas(m,bg="white",height=400)
c.create_rectangle(150, 200, 50, 75, outline="black")
c.create_rectangle(250,200,50,75,outline="black")
c.pack()
gif1 =Image.open("C:\\Users\\Shravan Suravarjjala\\Downloads\\618Vt-ogdEL._SY355_.jpg")
gif1.thumbnail((300,200))
# gif1.show()
gif1_tk = ImageTk.PhotoImage(gif1)
c.create_image(300, 100, image=gif1_tk, anchor=tk.CENTER)

m.mainloop()

