from tkinter import *
from PyDictionary import *
import json
root=Tk()
root.title('DCITIONARY')
root.config(bg='gray25')
root.geometry('1500x700+0+0')

#############################
data = json.load(open("dictionary.json"))


############################
def click(d):
    
    display.config(state=NORMAL)
    
 
    text=entry.get()
    entry.delete(0,END)
    
    display.delete(0.0,END)
    try:                   				# exception handling
        definition=data[text]
        display.insert(END,definition)
        display.config(state=DISABLED)
	
    except:
        definition='Information regarding the text entered is not available!!!'
        display.insert(END,definition)
        
   


###################################


x={}
def click2(d,x):
     
    
    try:
         text=entry2.get()
         entry2.delete(0,END)
         y=entry3.get('1.0',END) 
         x[text]=y
         d.update(x)
         entry3.delete(0.0,END)
    except:
        
        entry3.delete(0.0,END)
        entry3.insert(END,"sorry action can't be performed")
        entry3.config(state=DISABLED)
        



###################################
d=PyDictionary()



########################################
# creates a grid 50 x 50 in the main window
c=0

while c < 50:
    root.columnconfigure(c,weight=1)
    root.rowconfigure(c,weight=1)
    c += 1

Label(root,text='DICTIONARY',font=('arial',50,'bold'),fg='gray18',relief=GROOVE).grid(row=11,column=18)

Label(root,text='ENTER ANY WORD',font=('arial'),fg='gray18',relief=GROOVE).grid(row=16, column=17)
entry=Entry(root,width=25,relief=GROOVE)
entry.grid(row=16, column=18)
entry.focus()

button=Button(root,text='SUBMIT',font=('arial',10),fg='gray18',relief=RIDGE,command= lambda :click(d)).grid(column=19, row=16)

c=0

while c < 50:
    root.columnconfigure(c,weight=1)
    root.rowconfigure(c,weight=1)
    c += 1

Label(root,text='DEFINITION',font=('arial',50,'bold'),fg='gray18',relief=GROOVE).grid(row=23,column=18)

display=Text(root,height=12,width=80,relief=GROOVE)
display.grid(row=30,column=18)

root.mainloop()
