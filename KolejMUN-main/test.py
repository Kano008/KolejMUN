import tkinter as tk
from tkinter import ttk

class Uygulama(tk.Tk):
    def init(self):
        super().init()

        self.title("Python Arayüzü")
        self.geometry("600x400")

        # Logo
        self.logo = tk.PhotoImage(file="logo.png")
        self.logo_label = tk.Label(self, image=self.logo)
        self.logo_label.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        # 4 İmge
        self.image1 = tk.PhotoImage(file="image1.jpg")
        self.image2 = tk.PhotoImage(file="image2.jpg")
        self.image3 = tk.PhotoImage(file="image3.jpg")
        self.image4 = tk.PhotoImage(file="image4.jpg")

        self.image_label1 = tk.Label(self, image=self.image1)
        self.image_label1.grid(row=0, column=1, padx=10, pady=10)

        self.image_label2 = tk.Label(self, image=self.image2)
        self.image_label2.grid(row=0, column=2, padx=10, pady=10)

        self.image_label3 = tk.Label(self, image=self.image3)
        self.image_label3.grid(row=0, column=3, padx=10, pady=10)

        self.image_label4 = tk.Label(self, image=self.image4)
        self.image_label4.grid(row=0, column=4, padx=10, pady=10)

        # Ayarlar İmgesi
        self.settings_image = tk.PhotoImage(file="instalogo.png")
        self.settings_button = ttk.Button(self, image=self.settings_image, command=self.ayarlar_ac)
        self.settings_button.grid(row=0, column=5, padx=10, pady=10, sticky="ne")

    def ayarlar_ac(self):
        # Ayarlar penceresi açılabilir
        pass