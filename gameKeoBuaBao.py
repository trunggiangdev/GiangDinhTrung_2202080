import tkinter as tk
from tkinter import messagebox
import random

# Hàm xử lý kết quả
def play_game(user_choice):
    # Các lựa chọn của người dùng và máy tính
    choices = ['Scissors', 'Rock', 'Paper']
    computer_choice = random.choice(choices)
    
    # Quy tắc game
    if user_choice == computer_choice:
        result = "Draw!"
    elif (user_choice == 'Scissors' and computer_choice == 'Rock') or \
         (user_choice == 'Rock' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Scissors'):
        result = f"You lost! Computer choice {computer_choice}"
    else:
        result = f"You lost! Computer choice {computer_choice}"
    
    # Hiển thị kết quả
    messagebox.showinfo("Result", result)

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x400")  # Kích thước cửa sổ
root.config(bg="#f0f0f0")  # Màu nền của cửa sổ

# Thêm tiêu đề game
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 24, "bold"), bg="#f0f0f0", fg="#333")
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
tk.Button(root, text="Scissors", **button_style, command=lambda: play_game('Scissors')).pack(pady=10)
tk.Button(root, text="Rock", **button_style, command=lambda: play_game('Rock')).pack(pady=10)
tk.Button(root, text="Paper", **button_style, command=lambda: play_game('Paper')).pack(pady=10)

# Chạy giao diện Tkinter
root.mainloop()
