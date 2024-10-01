import customtkinter

app = customtkinter.CTk()
app.geometry("400x150")
button = customtkinter.CTkButton(app,text="Yes")
button.pack(padx="20",pady="20")

app.mainloop()
