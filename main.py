import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x600")
app.title("Calculator")
app.resizable(False, False)

# Title
label = ctk.CTkLabel(
    app,
    text="Calculator",
    font=("Times New Roman", 40)
)

label.grid(row=0, column=0, columnspan=4, pady=20)

# Display
display = ctk.CTkEntry(
    app,
    width=300,
    height=50,
    font=("Times New Roman", 24),
    justify="right"
)

display.grid(row=1, column=0, columnspan=4, padx=10, pady=20)

# Row 2
btn1 = ctk.CTkButton(app, text="7", width=70, height=70)
btn1.grid(row=2, column=0, padx=5, pady=5)

btn2 = ctk.CTkButton(app, text="8", width=70, height=70)
btn2.grid(row=2, column=1, padx=5, pady=5)

btn3 = ctk.CTkButton(app, text="9", width=70, height=70)
btn3.grid(row=2, column=2, padx=5, pady=5)

btn4 = ctk.CTkButton(app, text="/", width=70, height=70)
btn4.grid(row=2, column=3, padx=5, pady=5)

# Row 3
btn5 = ctk.CTkButton(app, text="4", width=70, height=70)
btn5.grid(row=3, column=0, padx=5, pady=5)

btn6 = ctk.CTkButton(app, text="5", width=70, height=70)
btn6.grid(row=3, column=1, padx=5, pady=5)

btn7 = ctk.CTkButton(app, text="6", width=70, height=70)
btn7.grid(row=3, column=2, padx=5, pady=5)

btn8 = ctk.CTkButton(app, text="*", width=70, height=70)
btn8.grid(row=3, column=3, padx=5, pady=5)

# Row 4
btn9 = ctk.CTkButton(app, text="1", width=70, height=70)
btn9.grid(row=4, column=0, padx=5, pady=5)

btn10 = ctk.CTkButton(app, text="2", width=70, height=70)
btn10.grid(row=4, column=1, padx=5, pady=5)

btn11 = ctk.CTkButton(app, text="3", width=70, height=70)
btn11.grid(row=4, column=2, padx=5, pady=5)

btn12 = ctk.CTkButton(app, text="-", width=70, height=70)
btn12.grid(row=4, column=3, padx=5, pady=5)

# Row 5
btn13 = ctk.CTkButton(app, text=".", width=70, height=70)
btn13.grid(row=5, column=0, padx=5, pady=5)

btn14 = ctk.CTkButton(app, text="0", width=70, height=70)
btn14.grid(row=5, column=1, padx=5, pady=5)

btn15 = ctk.CTkButton(app, text="+", width=70, height=70)
btn15.grid(row=5, column=2, padx=5, pady=5)

btn16 = ctk.CTkButton(app, text="=", width=70, height=70)
btn16.grid(row=5, column=3, padx=5, pady=5)

#alignment 

for i in range(4):
    app.grid_columnconfigure(i, weight=1)

for i in range(6):
    app.grid_rowconfigure(i, weight=1)

app.mainloop()