
import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from cv2 import *
import numpy as np
from tkinter import *

def next_student():
    global cam
    global photo
    global window
    global canvas
    global cv_img
    
    window.destroy()
    cam.release()

    cam = VideoCapture(0)
    s, cv_img = cam.read()

    window = tkinter.Tk()
    window.title("Student Registration")
    height, width, no_channels = cv_img.shape
    canvas = tkinter.Canvas(window, width = width, height = height)
    canvas.pack()
    photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
    btn_blur=tkinter.Button(window, text="Save", width=50, command=save_image)
    btn2_blur=tkinter.Button(window, text="Retake", width=50, command=retake_image)
    btn3_blur=tkinter.Button(window, text="Next", width=50, command=next_student)
    btn_blur.pack(anchor=tkinter.CENTER, expand=True)
    btn2_blur.pack(anchor=tkinter.CENTER, expand=True)
    btn3_blur.pack(anchor=tkinter.CENTER, expand=True)

    window.mainloop()

def save_image():
    global cv_img
    
    def save_name():
            name = e1.get() + "_" + e2.get()
            imwrite("./images/" + name + ".jpg", cv_img)
            print("Student saved")
            current.destroy()
    current = Tk()
    Label(current, text="First Name").grid(row=0)
    Label(current, text="Last Name").grid(row=1)

    e1 = Entry(current)
    e2 = Entry(current)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)


    Button(current, text='Save', command=save_name).grid(row=3, column=1, sticky=W, pady=4)
    #name = e1 + "_" + e2
    #imwrite("./images/" + name + ".jpg", cv_img)
    #print("Student saved")

    
def retake_image():
    global photo
    global cam
    global canvas
    global cv_img
    
    cam.release()

    cam = VideoCapture(0)
    s, cv_img = cam.read()
    photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
    canvas.create_image(0, 0, image = photo , anchor = tkinter.NW)


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
btn_blur=tkinter.Button(window, text="Save", width=50, command=save_image)
btn2_blur=tkinter.Button(window, text="Retake", width=50, command=retake_image)
btn3_blur=tkinter.Button(window, text="Next Student", width=50, command=next_student)
btn_blur.pack(anchor=tkinter.CENTER, expand=True)
btn2_blur.pack(anchor=tkinter.CENTER, expand=True)
btn3_blur.pack(anchor=tkinter.CENTER, expand=True)
 
window.mainloop()
    
