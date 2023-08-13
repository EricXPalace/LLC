import tkinter as tk
import hashlib
import json
import os
import sys

# 定義存儲使用者資訊的json文件名
USER_DATA_FILE = "user_data.json"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


class LoginApp:

    def __init__(self, root):
        self.root = root
        self.user_data = self.load_user_data()
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.create_widgets()

    def load_user_data(self):
        if os.path.exists(USER_DATA_FILE):
            with open(USER_DATA_FILE, 'r') as f:
                return json.load(f)
        else:
            return {}

    def save_user_data(self):
        with open(USER_DATA_FILE, 'w') as f:
            json.dump(self.user_data, f)

    def create_widgets(self):
        self.message = tk.Label(self.root, text="")
        self.message.grid(row=0, column=0, columnspan=2)

        tk.Label(self.root, text="使用者名稱").grid(row=1, column=0)
        tk.Entry(self.root, textvariable=self.username).grid(row=1, column=1)
        
        tk.Label(self.root, text="密碼").grid(row=2, column=0)
        tk.Entry(self.root, textvariable=self.password, show="*").grid(row=2, column=1)
        
        tk.Button(self.root, text="登入", command=self.login).grid(row=3, column=0)
        tk.Button(self.root, text="註冊", command=self.register).grid(row=3, column=1)

    def login(self):
        username = self.username.get()
        password = hash_password(self.password.get())

        if username in self.user_data and self.user_data[username] == password:
            self.message.config(text="登入成功，歡迎您，{}!".format(username))
            self.root.after(2000, self.root.destroy)  # 2秒後關閉視窗
            self.root.after(2000, self.connect_to_main_program)  # 2秒後連接主程式
        else:
            self.message.config(text="登入失敗，程式終止。")
            sys.exit()

    def register(self):
        username = self.username.get()
        password = hash_password(self.password.get())

        if username in self.user_data:
            self.message.config(text="用戶名已存在，請選擇其他的用戶名。")
        else:
            self.user_data[username] = password
            self.save_user_data()
            self.message.config(text="註冊成功，歡迎您，{}!".format(username))
            self.root.after(2000, self.root.destroy)  # 2秒後關閉視窗
            self.root.after(2000, self.connect_to_main_program)  # 2秒後連接主程式

    def connect_to_main_program(self):
        # 在這裡插入連接主程式的代碼
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
