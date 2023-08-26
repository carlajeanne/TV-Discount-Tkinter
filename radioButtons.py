print("************ Programmed by ***********")
print("******* Carla Jeanne B. Golena *******")
print("************** BSCOE 1-3 *************\n\n\n")

from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Radiobutton & Checkbox")

def computediscount1():
    if subtotalLabel.get() == '':
        discountLabel.insert(END, '')
    else:
        n = int(subtotalLabel.get())
        discountValue = 0.05 * n
        discountLabel.insert(END, discountValue)

def computediscount2():
    if subtotalLabel.get() == '':
        discountLabel.insert(END, '')
    else:
        n = int(subtotalLabel.get())
        discountValue = 0.10 * n
        discountLabel.insert(END, discountValue)

def computediscount3():
    if subtotalLabel.get() == '':
        discountLabel.insert(END, '')
    else:
        n = int(subtotalLabel.get())
        discountValue = 0.15 * n
        discountLabel.insert(END, discountValue)

# function for compute button
def shownetamount():
    if subtotalLabel.get() == '':
        discountLabel.insert(END, '0.00')
        netamountLabel.insert(END, '0.00')
        subtotalLabel.insert(END, '0.00')
    else:
        netamount = float(subtotalLabel.get()) - float(discountLabel.get())
        netamountLabel.insert(END, netamount)

# function for clear button
def clear_text():
    tv1.deselect()
    tv2.deselect()
    tv3.deselect()
    subtotalLabel.delete(0, END)
    discountLabel.delete(0, END)
    netamountLabel.delete(0, END)
    discount1.deselect()
    discount2.deselect()
    discount3.deselect()

# items selection
item_var = IntVar()
item_var.set(0)

items = Label(root, text="Select Items Here: ")
items.place(x=50, y=30)

tv1 = Checkbutton(root, text="TV 21'' (PHP 10, 000.00) ", variable=item_var, offvalue='', onvalue=10000)
tv1.place(x=50, y=50)
tv2 = Checkbutton(root, text="TV 14'' (PHP 7, 500.00) ", variable=item_var, offvalue='', onvalue=7500)
tv2.place(x=50, y=70)
tv3 = Checkbutton(root, text="TV 12'' (PHP 5, 000.00) ", variable=item_var, offvalue='', onvalue=5000)
tv3.place(x=50, y=90)

# discount selection
discount_var = IntVar()
discount_var.set(0)

discountFrame = Label(root, text="Discount: ")
discountFrame.place(x=250, y=30)

discount1 = Radiobutton(root, text="5 %", value=0.05, variable=discount_var, command=computediscount1)
discount1.place(x=250, y=50)
discount2 = Radiobutton(root, text="10 %", value=0.10, variable=discount_var, command=computediscount2)
discount2.place(x=250, y=70)
discount3 = Radiobutton(root, text="15 %", value=0.15, variable=discount_var, command=computediscount3)
discount3.place(x=250, y=90)

# buttons
compute = Button(root, text="Compute", padx=12, pady=1, command=shownetamount)
compute.place(x=30, y=150)
clear = Button(root, text="Clear All", command=clear_text, padx=15, pady=1)
clear.place(x=30, y=180)
close = Button(root, text="Close", command=root.destroy, padx=22, pady=1)
close.place(x=30, y=210)

# Labels
subtotal = Label(root, text=" Sub-Total ")
subtotal.place(x=150, y=150)
dscnt = Label(root, text=" Discount ")
dscnt.place(x=150, y=180)
netamnt = Label(root, text=" Net-Amount ")
netamnt.place(x=150, y=210)

# output boxes
subtotalLabel = Entry(root, textvariable=item_var, width=12)
subtotalLabel.place(x=270, y=150)

discountLabel = Entry(root, width=12)
discountLabel.place(x=270, y=180)

netamountLabel = Entry(root, width=12)
netamountLabel.place(x=270, y=210)

root.mainloop()

