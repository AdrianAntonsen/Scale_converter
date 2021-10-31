import tkinter as tk

root = tk.Tk()
root.title("Vekt konvertering")

e = tk.Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current= e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, tk.END)

def button_LBS():
    number_1 = e.get()
    global lbs_sum
    global math
    lbs_sum = float(number_1)
    math = "gange"

    if math == "gange":
        e.insert(0, lbs_sum * (2.2046))

def button_KG():
    number_2 = e.get()
    global KG_sum
    math = "dele"
    KG_sum = float(number_2)

    if math == "dele":
        e.insert(0, KG_sum / (2.2046))
    

#deffinere knappene
button_1= tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2= tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3= tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4= tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5= tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6= tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7= tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8= tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9= tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0= tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_clear= tk.Button(root, text="clear", padx=79, pady=20, command=button_clear)
button_LBS= tk.Button(root, text="til LBS", padx=27, pady=20, command=button_LBS)
button_KG= tk.Button(root, text="til KG", padx=28.5, pady=20, command=button_KG)


#hvor det skal stå på skjermen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_LBS.grid(row=4, column=1,)
button_KG.grid(row=4, column=2,)

button_clear.grid(row=5, column=0, columnspan=2)


root.mainloop()

