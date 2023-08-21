import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


def calculate_halfway():
    dt1_str = entry1.get()
    dt2_str = entry2.get()

    try:
        halfway_result = datetime_halfway(dt1_str, dt2_str)
        result_label.config(text=f"Halfway: {halfway_result}")
    except:
        messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD HH:MM:SS")


def datetime_halfway(dt1_str, dt2_str, format="%Y-%m-%d %H:%M:%S"):
    dt1 = datetime.strptime(dt1_str, format)
    dt2 = datetime.strptime(dt2_str, format)
    timestamp1 = dt1.timestamp()
    timestamp2 = dt2.timestamp()
    average_timestamp = (timestamp1 + timestamp2) / 2
    halfway_datetime = datetime.fromtimestamp(average_timestamp)
    return halfway_datetime.strftime(format)


# 创建主窗口
root = tk.Tk()
root.title("Halfway DateTime Calculator")

# 创建并放置标签、文本框和按钮
label1 = ttk.Label(root, text="Enter DateTime 1 (YYYY-MM-DD HH:MM:SS):")
label1.pack(padx=20, pady=5)

entry1 = ttk.Entry(root, width=30)
entry1.pack(padx=20, pady=5)

label2 = ttk.Label(root, text="Enter DateTime 2 (YYYY-MM-DD HH:MM:SS):")
label2.pack(padx=20, pady=5)

entry2 = ttk.Entry(root, width=30)
entry2.pack(padx=20, pady=5)

calculate_button = ttk.Button(root, text="Calculate", command=calculate_halfway)
calculate_button.pack(pady=10)

result_label = ttk.Label(root, text="Halfway: ")
result_label.pack(padx=20, pady=20)

root.mainloop()
