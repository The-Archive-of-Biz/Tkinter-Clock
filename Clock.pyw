import sys    

from tkinter import *

import time


print("background colour")

answer=input()







print("font colour")

answer2=input()




def tick():

    global time1

    time2 = time.strftime('%H:%M:%S')

    if time2 != time1:

        time1 = time2

        clock.config(text=time2)

    clock.after(200, tick)



root = Tk()

root.geometry("1343x370")

root.title("Clock")

time1 = ''




status = Label(root, text="", bd=1, relief=SUNKEN, anchor=W)

status.grid(row=0, column=0)




clock = Label(root, font=('Helvetica', 250, 'bold'),fg=answer2, bg=answer)

clock.grid(row=0, column=1) 




tick()

root.mainloop()
