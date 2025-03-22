from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km =round(miles * 1.609)
    kilometer_result_label.config(text = f"{km}")

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx= 20, pady = 20, bg = "pink")

miles_input = Entry(width=7, bg = "white", fg = "purple")
miles_input.grid(column = 1, row = 0)

miles_label= Label(text = "Miles", bg = "pink", fg = "white")
miles_label.grid(column = 2, row= 0)

is_equal_label = Label(text = "is equal to", bg = "pink", fg = "white" )
is_equal_label.grid(column = 0, row =1)

kilometer_result_label = Label(text = 0, bg = "pink", fg = "white")
kilometer_result_label.grid(column =1, row = 1)

kilometer_label = Label(text = "Km", bg = "pink", fg = "white")
kilometer_label.grid(column= 2, row = 1)

calculate_button = Button(text = "Calculate", command = miles_to_km, bg = "pink", fg = "white")
calculate_button.grid(column=1, row =2)

window.mainloop()