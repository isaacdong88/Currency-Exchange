from tkinter import Tk, ttk
from tkinter import *

window = Tk()
window.geometry('300x320')
window.title('Currency Converter')
window.configure(bg='white')
window.resizable(height=FALSE, width=FALSE)

top =Frame(window, width=300, height=60, bg="green")
top.grid(row=0, column=0)

main = Frame(window, width=300, height=260, bg="white")
main.grid(row=1, column=0)

result_display = Label(main, text= " ", width=16, height=2, pady=7, relief="solid", anchor= CENTER, font= ('Ariel 16 bold'), bg="white", fg="black")
result_display.place(x=55, y=10)

currency = ['ARS','AUD','BRL','CAD','KYD','CNY','DKK','DOP','EGP','EUR','HKD','INR','IRR','ILS','JPY','KPW','KRW','MXN','RUB','SAR','SGD','GBP','USD']

from_currency = Label(main, text= "FROM", width=8, height=1, padx=0, pady=0, relief="flat", anchor= NW, font= ('Ariel 10'), bg="white", fg="black")
from_currency.place(x=58, y=90)
combo_box1 = ttk.Combobox(main, width=8, justify=CENTER, font= ("Ivy 8 bold"))
combo_box1['values'] = (currency)
combo_box1.place(x=50, y=115)


to_currency = Label(main, text= "To", width=8, height=1, padx=0, pady=0, relief="flat", anchor= NW, font= ('Ariel 10'), bg="white", fg="black")
to_currency.place(x=158, y=90)
combo_box2 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 8 bold"))
combo_box2['values'] = (currency)
combo_box2.place(x=160, y=115)

amount = Entry(main, width=29, justify=CENTER, font=("Ivy 9 bold"), relief='solid')
amount.place(x=40, y=155)

button = Button(main, text="Convert", width=22, padx=5, height=2, highlightbackground="green", fg="white", font=("Ivy 9 bold"), relief=SOLID)
button.place(x=62, y=210)

window.mainloop()