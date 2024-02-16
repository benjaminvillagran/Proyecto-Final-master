import customtkinter
def radiobutton_event():
    print("radiobutton toggled, current value:", radio_var.get())

radio_var = tkinter.IntVar(value=0)
radiobutton_1 = customtkinter.CTkRadioButton(app, text="CTkRadioButton 1",
                                             command=radiobutton_event, variable= radio_var, value=1)
radiobutton_2 = customtkinter.CTkRadioButton(app, text="CTkRadioButton 2",
                                             command=radiobutton_event, variable= radio_var, value=2)