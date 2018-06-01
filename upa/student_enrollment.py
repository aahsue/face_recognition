
import tkinter
import cv2
import PIL.Image, PIL.ImageTk


# Callback for the "Blur" button
def blur_image():
    global cv_img
    global photo
    
    cv_img = cv2.blur(cv_img, (3, 3))
    photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

from cv2 import *
import numpy as np
cam = VideoCapture(0)
s, cv_img = cam.read()

window = tkinter.Tk()
window.title("Student Registration")

# Get the image dimensions (OpenCV stores image data as NumPy ndarray)
height, width, no_channels = cv_img.shape
 
# Create a canvas that can fit the above image
canvas = tkinter.Canvas(window, width = width, height = height)
canvas.pack()
 
# Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
 
# Add a PhotoImage to the Canvas
canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
 
# Button that lets the user blur the image
btn_blur=tkinter.Button(window, text="Save", width=50, command=blur_image)
btn2_blur=tkinter.Button(window, text="Retake", width=50, command=blur_image)
btn_blur.pack(anchor=tkinter.CENTER, expand=True)
btn2_blur.pack(anchor=tkinter.CENTER, expand=True)
 
window.mainloop()
    
