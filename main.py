import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x500")
app.title("GUI Calculator")

label = ctk.CTkLabel(app, text="Calculator", font=("Arial", 28))
label.pack(pady=20)

app.mainloop()