"""Code of degree converter"""

import tkinter
root = tkinter.Tk()

#main window
root.title("degree converter")
root.resizable(width=False, height=False)
root.grid()

#function of converting Fahrenheit to Celsius
def far_to_sel():
    input = entry2.get()
    cel = (float(input) - 32)*(5/9)
    label2["text"] = "{0:02f}  C`".format(cel)

#function to convert Celsius to Fahrenheit
def cel_to_far():
    input = entry4.get()
    far = float(input)*(9/5) +32
    label4["text"]= "{0:02f}  F`".format(far)

#Frames, labels and buttons of the main window
label1 = tkinter.Label(root, text="fahreheit to celsius")
label1.grid()
entry2 = tkinter.Entry(root, bg="light cyan")
entry2.grid(row=1, column=0, sticky="nsew")
button2 = tkinter.Button(root, text="=>", command= lambda: far_to_sel())
button2.grid(row=1, column=1, sticky="nsew")
label2 = tkinter.Label(root, text="--", relief=tkinter.RAISED)
label2.grid(row=1, column=2, sticky="nsew")

label3 = tkinter.Label(root, text="Celsius to fahrenheit")
label3.grid()

entry4 = tkinter.Entry(root, bg="light yellow")
entry4.grid(row=3, column=0, sticky="nsew")
button4 = tkinter.Button(root, text="=>", command=lambda: cel_to_far())
button4.grid(row=3, column=1, sticky="nsew")
label4 = tkinter.Label(root, text="--", relief=tkinter.SUNKEN)
label4.grid(row=3, column=2, sticky="nsew")

button5 = tkinter.Button(text="Exit", command=root.destroy)
button5.grid(row=5,column=2, sticky="ne")

root.mainloop()