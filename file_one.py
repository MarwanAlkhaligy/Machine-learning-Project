from tkinter import ttk
from tkinter import *


root = Tk()
root.title("Machine Learning Classifier")

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/3 - windowWidth/3)
positionDown = int(root.winfo_screenheight()/3 - windowHeight/2)
root.geometry('580x580')
root.geometry("+{}+{}".format(positionRight, positionDown))

top_frame =Frame(root, height = 600)
top_frame.pack()
bottum_frame =Frame(root)
bottum_frame.pack(side = BOTTOM)

label_one = Label(top_frame, text = "Parkinsons Disease Classifier" ,font=("Helvetica",  30), foreground = "blue")
label_one.pack()
canvas = Canvas(root,width = 50,height = 1000,bg = "#8CCCC0")
canvas.pack()

button_one = Button(canvas, text = "Show Data" ,fg = "black" ,bg = "#3A7171"  ,padx = 10,font=("Helvetica",  15))
button_one.pack()
#button_two = Button(canvas, text = "Data" ,fg = "black" ,bg = "#3A7171"  ,padx = 10,font=("Helvetica",  15))
#button_two.pack()


labelTop = Label(canvas, text = "Choose your Algorithm",font=("Helvetica",  13), foreground = "blue")
labelTop.pack()

comboExample = tkk.Combobox(canvas, 
                            values=[
                                    "Neural Network", 
                                    "Support Vector Machines",
                                    "Decision Tree",
                                    "Naïve Bayes"])
comboExample.pack()
comboExample.current(0)



root.mainloop()








