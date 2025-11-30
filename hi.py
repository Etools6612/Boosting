import tkinter as tk
from tkinter import ttk

# ========== MAIN WINDOW ==========
app = tk.Tk()
app.title("Service Selector UI")
app.geometry("900x400")   # mas malaki window
app.config(bg="#E4EBF2")

# ==================== BOX 1 (LEFT - SERVICES) ====================
frame1 = tk.LabelFrame(app, text=" - SERVICES", bg="#D5DEE7", padx=5, pady=5)
frame1.place(x=80, y=30, width=250, height=740)   # 🔥 mas malaki

services = {
    "Test 1": "RESULT: You selected Test 1 ✔",
    "Test 2": "RESULT: You selected Test 2 ✔"
}

tk.Label(frame1, text="1. Test 1", bg="#D5DEE7", font=("Arial",12)).pack(anchor="w", pady=5)
tk.Label(frame1, text="2. Test 2", bg="#D5DEE7", font=("Arial",12)).pack(anchor="w", pady=5)


# ==================== BOX 2 (CENTER - SELECT SERVICE) ====================
frame2 = tk.LabelFrame(app, text="BOX 2 - Choose Service", bg="#D7E8F5", padx=10, pady=10)
frame2.place(x=80, y=1650, width=550, height=300)

select_service = ttk.Combobox(frame2, values=list(services.keys()), width=25)
select_service.pack(pady=20)

def show_result():
    choice = select_service.get()
    result_box.delete("1.0", tk.END)

    if choice in services:
        result_box.insert(tk.END, services[choice])
    else:
        result_box.insert(tk.END, "⚠ Select a service first.")

tk.Button(frame2, text="Show Outcome", command=show_result, width=20).pack(pady=10)


# ==================== BOX 3 (RIGHT - OUTCOME) ====================
frame3 = tk.LabelFrame(app, text="BOX 3 - RESULT", bg="#D0DEEB", padx=10, pady=10)
frame3.place(x=70, y=830, width=880, height=800)   # 🔥 mas malapad at mas mataas

result_box = tk.Text(frame3, width=32, height=13, font=("Arial",11))  # 🔥 mas malaki font at area
result_box.pack()


app.mainloop()