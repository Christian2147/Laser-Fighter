# Copyright (C) [2024] [Christian Marinkovich]
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import ctypes
import tkinter
from tkinter import ttk
from tkinter import filedialog
from PIL import Image


class ImageScalerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Scaler")
        self.root.geometry("400x500")
        self.root.iconbitmap('./icon/icon.ico')

        self.title_label = ttk.Label(root, text="Laser Fighter Image Scaler Tool", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=(5, 20))

        self.insert_button = ttk.Button(root, text="Insert File", command=self.insert_file)
        self.insert_button.pack(pady=1)

        self.file_label = ttk.Label(root, text="No file selected")
        self.file_label.pack(pady=(1, 10))

        self.image_width_label = ttk.Label(root, text="New Image Width:")
        self.image_width_label.pack(pady=(8, 0.5))
        self.image_width_input = ttk.Entry(root)
        self.image_width_input.pack(pady=0.5)

        self.image_height_label = ttk.Label(root, text="New Image Height:")
        self.image_height_label.pack(pady=(8, 0.5))
        self.image_height_input = ttk.Entry(root)
        self.image_height_input.pack(pady=0.5)

        self.submit_button = ttk.Button(root, text="Submit", command=self.rescale_image)
        self.submit_button.pack(pady=(10, 0))

    def insert_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_label.config(text=file_path)

    def get_file_path(self):
        return self.file_label.cget("text")

    def get_width(self):
        try:
            width = int(self.image_width_input.get())
            return width
        except ValueError:
            return 0

    def get_height(self):
        try:
            height = int(self.image_height_input.get())
            return height
        except ValueError:
            return 0

    def rescale_image(self):
        input_file_path = self.get_file_path()
        new_width = self.get_width()  # Retrieve text from the first input box
        new_height = self.get_height()  # Retrieve text from the second input box

        if input_file_path and new_width > 0 and new_height > 0:
            try:
                image = Image.open(input_file_path)
                resized_image = image.resize((new_width, new_height))

                output_file_path = filedialog.asksaveasfilename(
                    defaultextension=".gif",
                    filetypes=[("GIF files", "*.gif"), ("All files", "*.*")]
                )

                if output_file_path:
                    resized_image.save(output_file_path)

            except Exception as e:
                self.show_error_message(f"An error occurred: {e}")
        else:
            self.show_error_message("Invalid input values. Please check the file path and dimensions.")

        self.image_width_input.delete(0, tkinter.END)
        self.image_height_input.delete(0, tkinter.END)

    def show_error_message(self, message):
        # Display a Windows error message box
        ctypes.windll.user32.MessageBoxW(0, message, "Error", 0x10 | 0x0)
