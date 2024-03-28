from tkinter import *
from PIL import Image, ImageTk

root = Tk() 
root.title("MEDARDO YALAZA")
root.geometry('590x790')

lbl = Label(root, text="XD")
lbl.grid(row=0, column=0, padx=0, pady=0)


# Cargar imagen de cafe
img_coffee1 = Image.open("Images/sherk.jpg")
img_coffee1 = img_coffee1.resize((70, 70))

image_tk = ImageTk.PhotoImage(img_coffee1)

# Crea Label para mostrar la imagen
lbl_image = Label(root, image=image_tk)
lbl_image.grid(row=3, column=0,padx=20,pady=20)

lbl_img_coffee2 = Label(root, image=image_tk)
lbl_img_coffee2.grid(row=3, column=1, padx=20,pady=20)

lbl_img_coffee3 = Label(root, image=image_tk)
lbl_img_coffee3.grid(row=3, column=2, padx=20,pady=20)

lbl_img_coffee4 = Label(root, image=image_tk)
lbl_img_coffee4.grid(row=4, column=0, padx=20,pady=20)

lbl_img_coffee5 = Label(root, image=image_tk)
lbl_img_coffee5.grid(row=4, column=1, padx=20,pady=20)

lbl_img_coffee6 = Label(root, image=image_tk)
lbl_img_coffee6.grid(row=4, column=2, padx=20,pady=20)

lbl_img_coffee7 = Label(root, image=image_tk)
lbl_img_coffee7.grid(row=5, column=0, padx=20,pady=20)

lbl_img_coffee8 = Label(root, image=image_tk)
lbl_img_coffee8.grid(row=5, column=1, padx=20,pady=20)

lbl_img_coffee9 = Label(root, image=image_tk)
lbl_img_coffee9.grid(row=5, column=2, padx=20,pady=20)

root.mainloop()
