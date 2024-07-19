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

"""
    File: Main.py
    Author: Christian Marinkovich
    Date: 2024-07-19
    Description:
    This file contains most of the logic for the image scaler application.
    The application itself is one big class that consists of all the functions it is required to preform.
    Since the application is so small, only one class is needed.
"""

import ctypes
import tkinter
from tkinter import ttk
from tkinter import filedialog
from PIL import Image


class ImageScalerApp:
    """
        Represents the Image Scaler Application

        Attributes:
            root (tkinter.Tk()): The window itself
            title_label (ttk.Label()): The title text inside the canvas
            insert_button (ttk.Button()): The insert file path button
            file_label (ttk.Label()): Displays the open file path on the canvas
            image_width_label (ttk.Label()): Displays the label for the new image width text input
            image_width_input (ttk.Entry()): The input box for the new image width
            image_height_label (ttk.Label()): Displays the label for the new image height text input
            image_height_input (ttk.Entry()): The input box for the new image height
            submit_button (ttk.Button()): The execute button to rescale and save the image
    """

    def __init__(self, root):
        """
            Populates the application window

            :param root: The empty application window
            :type root: tkinter.Tk()
        """

        # Creates the screen
        self.root = root
        self.root.title("Image Scaler")
        self.root.geometry("400x500")
        self.root.iconbitmap('./icon/icon.ico')

        # Create the title
        self.title_label = ttk.Label(root, text="Laser Fighter Image Scaler Tool", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=(5, 20))

        # Create insert button
        self.insert_button = ttk.Button(root, text="Insert File", command=self.insert_file)
        self.insert_button.pack(pady=1)

        # Create input file text label on the canvas
        self.file_label = ttk.Label(root, text="No file selected")
        self.file_label.pack(pady=(1, 10))

        # Create image width input
        self.image_width_label = ttk.Label(root, text="New Image Width:")
        self.image_width_label.pack(pady=(8, 0.5))
        self.image_width_input = ttk.Entry(root)
        self.image_width_input.pack(pady=0.5)

        # Create image height input
        self.image_height_label = ttk.Label(root, text="New Image Height:")
        self.image_height_label.pack(pady=(8, 0.5))
        self.image_height_input = ttk.Entry(root)
        self.image_height_input.pack(pady=0.5)

        # Create the submit button
        self.submit_button = ttk.Button(root, text="Submit", command=self.rescale_image)
        self.submit_button.pack(pady=(10, 0))

    def insert_file(self):
        """
            Opens the "file open" dialog to extract a file path for the file to open and stores it in the "file_label"
                variable

            :return: None
        """

        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_label.config(text=file_path)

    def get_file_path(self):
        """
            Extracts the file path from the file label and returns it as a string.

            :return: The input file path
            :type: string
        """

        return self.file_label.cget("text")

    def get_width(self):
        """
            Extracts the new file width from the image width input box and returns it as an integer.

            :return: width: The new width as an integer
            :type: int
        """

        try:
            width = int(self.image_width_input.get())
            return width
        except ValueError:
            return 0

    def get_height(self):
        """
            Extracts the new file height from the image height input box and returns it as an integer.

            :return: height: The new height as an integer
            :type: int
        """

        try:
            height = int(self.image_height_input.get())
            return height
        except ValueError:
            return 0

    def rescale_image(self):
        """
            Preforms the image rescale and saves the new image to a specified location through the dialog box.

            :return: None
        """

        # Extract the input path, new width, and the new height
        input_file_path = self.get_file_path()
        new_width = self.get_width()  # Retrieve text from the first input box
        new_height = self.get_height()  # Retrieve text from the second input box

        # If the variables are valid
        if input_file_path and new_width > 0 and new_height > 0:
            try:
                # Open the input image and resize it
                image = Image.open(input_file_path)
                resized_image = image.resize((new_width, new_height))

                # Open the save dialog box
                output_file_path = filedialog.asksaveasfilename(
                    defaultextension=".gif",
                    filetypes=[("GIF files", "*.gif"), ("All files", "*.*")]
                )

                # Save it in the new location
                if output_file_path:
                    resized_image.save(output_file_path)

            # Otherwise, throw an exception
            except Exception as e:
                self.show_error_message(f"An error occurred: {e}")
        # else throw an exception
        else:
            self.show_error_message("Invalid input values. Please check the file path and dimensions.")

        # Empty the input boxes
        self.image_width_input.delete(0, tkinter.END)
        self.image_height_input.delete(0, tkinter.END)

    def show_error_message(self, message):
        """
            Displays an error message as a windows error pop up when there is an error in the program.

            :param message: The error message to be displayed
            :type message: string

            :return: None
        """

        # Display a Windows error message box
        ctypes.windll.user32.MessageBoxW(0, message, "Error", 0x10 | 0x0)
