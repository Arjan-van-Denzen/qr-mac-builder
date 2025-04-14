import qrcode
from PIL import Image
import numpy as np
from collections import Counter
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter.filedialog import askopenfilename
import os

# Start a GUI app (but hide the main window)
root = tk.Tk()
root.withdraw()

# Ask for URL
url = simpledialog.askstring("Input", "Enter the URL to encode:")

if not url:
    messagebox.showwarning("No URL", "No URL entered. Exiting.")
    exit()

# Generate QR code
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data(url)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="black")

# Save & show
downloads_folder = os.path.expanduser("~/Downloads")
output_path = os.path.join(downloads_folder, "qr_code.png")
qr_img.save(output_path)

messagebox.showinfo("Done", f"QR code saved to:\n{output_path}")