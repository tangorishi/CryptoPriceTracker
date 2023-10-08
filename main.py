import tkinter as tk
from tkinter import ttk
import requests

class CryptoPriceTracker(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Cryptocurrency Price Tracker")
        self.geometry("400x200")
        
        self.label = ttk.Label(self, text="Select a cryptocurrency:")
        self.label.pack(pady=20)
        
        self.crypto_var = tk.StringVar()
        self.crypto_dropdown = ttk.Combobox(self, textvariable=self.crypto_var, values=["Select a cryptocurrency", "bitcoin", "ethereum", "litecoin", "dogecoin", "ripple", "cardano"])
        self.crypto_dropdown.pack(pady=10)
        self.crypto_dropdown.bind("<<ComboboxSelected>>", self.fetch_price)
        
        self.price_label = ttk.Label(self, text="")
        self.price_label.pack(pady=20)
        
    def fetch_price(self, event):
        crypto = self.crypto_var.get()
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        price = data[crypto]['usd']
        self.price_label.config(text=f"Price of {crypto.capitalize()}: ${price}")

if __name__ == "__main__":
    app = CryptoPriceTracker()
    app.mainloop()
