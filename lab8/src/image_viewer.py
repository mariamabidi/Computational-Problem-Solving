__author__ = 'MA'
"""
CSCI-603 Lab 8: Image Viewer 

A program to view images from compressed and uncompressed file.

Author: Mariam Abidi
"""
from qttree import QTTree
from qtexception import QTException
import sys
import tkinter as tk


def hex_representation(pixel):
    """
    Function for hexadecimal representation of the color.
    """
    if type(pixel) is not int:
        raise QTException("Pixel is not an integer")
    if pixel > 255 or pixel < 0:
        raise QTException("Pixel value is not in range 0-255")
    hex_value = format(pixel, '02X')
    return hex_value


def display_image(rawImage, dimension):
    """
    Function to display the image using tkinter.

    @param rawImage the 2d array of pixels
    @param dimension the dimensions of the image
    """
    window = tk.Tk()
    photoImage = tk.PhotoImage(width=dimension, height=dimension)
    canvas = tk.Canvas(window, width=dimension, height=dimension)
    canvas.pack()
    for row in range(len(rawImage)):
        for column in range(len(rawImage[row])):
            hexa = hex_representation(rawImage[row][column])
            photoImage.put("#"+hexa+hexa+hexa, to=(column, row))
    canvas.create_image(dimension//2, dimension//2, anchor=tk.CENTER, image=photoImage)
    window.mainloop()


def compressed_file(filename: str):
    """
    Function to render compressed image files.

    @param filename Variable to store the file name.
    """
    print("Uncompressing: " + str(filename))
    newImage = QTTree()
    rawImageFile, dimension = newImage.compressed_file(filename)
    display_image(rawImageFile, dimension)


def uncompressed_file(filename: str):
    """
    Function to render uncompressed image files.

    @param filename Variable to store the file name.
    """
    newImage = QTTree()
    rawImageFile, dimension = newImage.uncompressed_file(filename)
    display_image(rawImageFile, dimension)


def main():
    """
    The main function
    """
    try:
        num = len(sys.argv)
        if num < 2 or num > 3:
            raise QTException("Usage: python image_viewer.py [-c] <filename>")
        else:
            if num == 3 and sys.argv[1] == "-c":
                filename = sys.argv[2]
                compressed_file(filename)
            elif num == 2:
                filename = sys.argv[1]
                uncompressed_file(filename)
            else:
                print("Usage: python image_viewer.py [-c] <filename>")
    except QTException as e:
        print(e)


# Main Conditional Guard
if __name__ == '__main__':
    main()