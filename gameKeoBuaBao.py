import tkinter as tk
from tkinter import messagebox
import random

# Hàm xử lý kết quả
def play_game(user_choice):
    # Các lựa chọn của người dùng và máy tính
    choices = ['Kéo', 'Búa', 'Bao']
    computer_choice = random.choice(choices)
    
    # Quy tắc game
    if user_choice == computer_choice:
        result = "Hòa!"
    elif (user_choice == 'Kéo' and computer_choice == 'Búa') or \
         (user_choice == 'Búa' and computer_choice == 'Bao') or \
         (user_choice == 'Bao' and computer_choice == 'Kéo'):
        result = f"Bạn thắng! Máy tính chọn {computer_choice}"
    else:
        result = f"Bạn thua! Máy tính chọn {computer_choice}"
    
    # Hiển thị kết quả
    messagebox.showinfo("Kết quả", result)

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Game Kéo Búa Bao")
root.geometry("400x400")  # Kích thước cửa sổ
root.config(bg="#f0f0f0")  # Màu nền của cửa sổ

# Thêm tiêu đề game
title_label = tk.Label(root, text="Kéo Búa Bao", font=("Helvetica", 24, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=20)

# Tạo các nút cho người dùng chọn
button_style = {
    'font': ("Helvetica", 14, "bold"),
    'width': 20,
    'height': 2,
    'bd': 4,
    'relief': 'raised',
    'bg': '#4CAF50',  # Màu nền xanh cho nút
    'fg': 'white',    # Màu chữ trắng
    'activebackground': '#45a049',  # Màu nền khi nhấn nút
    'activeforeground': 'white'     # Màu chữ khi nhấn
}

# Tạo nút cho các lựa chọn
tk.Button(root, text="Kéo", **button_style, command=lambda: play_game('Kéo')).pack(pady=10)
tk.Button(root, text="Búa", **button_style, command=lambda: play_game('Búa')).pack(pady=10)
tk.Button(root, text="Bao", **button_style, command=lambda: play_game('Bao')).pack(pady=10)

# Chạy giao diện Tkinter
root.mainloop()
