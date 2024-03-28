from tkinter import *
from PIL import Image, ImageTk

# Funcion para validar combinaciones
def validar(texto):
    combinaciones_permitidas = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2"]
    if texto in combinaciones_permitidas:
        lbl_texto.config(text=texto, fg="green")
    else:
        lbl_texto.config(text="ERROR", fg="red")
        root.after(1000, lambda: lbl_texto.config(text=""))

# funcion para indicar la letra presionada y validar
def btn_presionado(letra):
    letras_presionadas.append(letra)
    if len(letras_presionadas) == 2:
        combinacion = ''.join(letras_presionadas)
        if combinacion in combinaciones_permitidas:
            lbl_texto.config(text=combinacion, fg="green")
        else:
            lbl_texto.config(text="ERROR", fg="red")
            root.after(1000, lambda: limpiar_error())

# Función para limpiar el error
def limpiar_error():
    lbl_texto.config(text="")
    letras_presionadas.clear()

# Crear ventana
root = Tk() 
root.title("Maquina expendedora de cafe")
root.geometry('690x900')

# Establecer un color de fondo
# root.configure(bg='blue')

# Inicializar la lista de letras presionadas
letras_presionadas = []

# Combinaciones permitidas
combinaciones_permitidas = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2"]

# Funcion para cargar imagenes
def load_image(ruta, size_x, size_y):
    image = Image.open(ruta)
    image = image.resize((size_x, size_y))
    return ImageTk.PhotoImage(image)

# Cargar imagenes con/sin cafeina
img_caffeinated= load_image("Images/caffeinated.jpg", 70, 70)
img_decaffeinated= load_image("Images/decaffeinated.jpg", 70, 70)

# Marco de con cafeina o descafeinado
type_of_coffee = Frame(root)
type_of_coffee.place(x=440,y=190)
btn_img_caffeinated = Button(type_of_coffee, image=img_caffeinated, command=lambda: btn_presionado("Con cafeina"))
btn_img_caffeinated.grid(row=0,column=0,padx=10)
btn_img_decaffeinated = Button(type_of_coffee, image=img_decaffeinated, command=lambda: btn_presionado("Sin cafeina"))
btn_img_decaffeinated.grid(row=0,column=1,padx=10)

# Marco de botones para seleccionar tipo de cafe
select_coffee = Frame(root)
select_coffee.place(x=430,y=290)

# Botones primera fila
btn_A = Button(select_coffee, text="A", command=lambda: btn_presionado("A"),padx=15,pady=10)
btn_A.grid(row=0, column=0)

btn_B = Button(select_coffee, text="B", command=lambda: btn_presionado("B"),padx=15,pady=10)
btn_B.grid(row=0, column=1)

btn_C = Button(select_coffee, text="C", command=lambda: btn_presionado("C"),padx=15,pady=10)
btn_C.grid(row=0, column=2)

# Botones 1, 2, 3 en la segunda fila
btn_1 = Button(select_coffee, text="1", command=lambda: btn_presionado("1"),padx=15,pady=10)
btn_1.grid(row=1, column=0)

btn_2 = Button(select_coffee, text="2", command=lambda: btn_presionado("2"),padx=15,pady=10)
btn_2.grid(row=1, column=1)

btn_3 = Button(select_coffee, text="3", command=lambda: btn_presionado("3"),padx=15,pady=10)
btn_3.grid(row=1, column=2)

# Botones con azucar, check y con vainilla en la tercera fila
img_sugar = load_image("Images/sugar.webp", 50, 50)
img_check = load_image("Images/sherk.jpg", 50, 50)
img_vanilla = load_image("Images/vainilla.png", 50, 50)

btn_img_sugar = Button(select_coffee, image=img_sugar, command=lambda: btn_presionado("Con azucar"))
btn_img_sugar.grid(row=2,column=0)

btn_img_check = Button(select_coffee, image=img_check, command=lambda: btn_presionado("Pedido realizado"))
btn_img_check.grid(row=2, column=1)

btn_img_vanilla = Button(select_coffee, image=img_vanilla, command=lambda: btn_presionado("Con vainilla"))
btn_img_vanilla.grid(row=2,column=2)

# Crear un canvas para espacio donde ira el codigo de cafe
canvas = Canvas(root, width=200, height=100)
canvas.place(x=440, y=100)  # Coloca el canvas en la posición (100, 100) dentro de la ventana

# Dibujar un rectángulo negro en el canvas
canvas.create_rectangle(0, 25, 250, 75, fill="black")

# Cuadro de texto para mostrar letras presionadas
lbl_texto = Label(root, text="", bg="black", fg="green", font=("Arial", 24))
lbl_texto.place(x=510, y=130)

# Cargar imagenes de cafe
img_coffee1 = Image.open("Images/sherk.jpg")
img_coffee1 = img_coffee1.resize((70, 70))



# FIXME cambiar sherk por imagenes reales
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

# Inicializar ventana
root.mainloop()
