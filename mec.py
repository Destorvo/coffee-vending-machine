from tkinter import *
from PIL import Image, ImageTk
# from proceso import ProcesoAutomata

# Funcion para validar combinaciones
def validar(texto):
    combinaciones_permitidas = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2"]
    if texto in combinaciones_permitidas:
        lbl_texto.config(text=texto, fg="green")
    else:
        lbl_texto.config(text="ERROR", fg="red")
        root.after(1000, lambda: lbl_texto.config(text=""))

# Funcion para cambiar el color del btn cuando se presiona
def toggle_color():
    if btn_circular['bg'] == 'red':
        btn_circular.config(bg='green')
    else:
        btn_circular.config(bg='red')

# Crear ventana
root = Tk() 
root.title("Maquina expendedora de cafe")
root.geometry('690x900')

# Establecer un color de fondo
# root.configure(bg='blue')

# Inicializar la lista de letras presionadas
letras_presionadas = []

# Combinaciones permitidas al escoger tipo de cafe
combinaciones_permitidas = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2"]

# Funcion para cargar imagenes
def load_image(ruta, size_x, size_y):
    image = Image.open(ruta)
    image = image.resize((size_x, size_y))
    return ImageTk.PhotoImage(image)

# Funcion para crear un btn circular
def create_circle_button(x, y):
    btn_circular = Button(root, text="Presionar", command=toggle_color, bg='red', fg='white', borderwidth=0, width=10, height=2, relief="flat")
    btn_circular.place(x=x, y=y)
    btn_circular.config(width=btn_circular.winfo_height())  # Hacer el botón circular
    return btn_circular



# Cargar imagenes con/sin cafeina
img_caffeinated= load_image("Images/caffeinated.jpg", 20, 20)
img_decaffeinated= load_image("Images/decaffeinated.jpg", 20, 20)

# Marco boton con cafeina o descafeinado
type_of_coffee = Frame(root)
type_of_coffee.place(x=440,y=190)
btn_img_caffeinated = Button(type_of_coffee, image=img_caffeinated, command=lambda: btn_presionado("Con cafeina"))
btn_img_caffeinated.grid(row=0,column=0,padx=10)
btn_img_decaffeinated = Button(type_of_coffee, image=img_decaffeinated, command=lambda: btn_presionado("Sin cafeina"))
btn_img_decaffeinated.grid(row=0,column=1,padx=10)

# Marco de botones para seleccionar tipo de cafe





select_coffee = Frame(root)
select_coffee.place(x=440,y=290)

# Botones primera fila
btn_A = Button(select_coffee, text="A", command=lambda: btn_presionado("A"),padx=25,pady=20)
btn_A.grid(row=0, column=0)

btn_B = Button(select_coffee, text="B", command=lambda: btn_presionado("B"),padx=25,pady=20)
btn_B.grid(row=0, column=1)

btn_C = Button(select_coffee, text="C", command=lambda: btn_presionado("C"),padx=25,pady=20)
btn_C.grid(row=0, column=2)

# Botones 1, 2, 3 en la segunda fila
btn_1 = Button(select_coffee, text="1", command=lambda: btn_presionado("1"),padx=25,pady=20)
btn_1.grid(row=1, column=0)

btn_2 = Button(select_coffee, text="2", command=lambda: btn_presionado("2"),padx=25,pady=20)
btn_2.grid(row=1, column=1)

btn_3 = Button(select_coffee, text="3", command=lambda: btn_presionado("3"),padx=25,pady=20)
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


# Cargar imagenes de tipos de vaso
img_coffee_size_small = load_image("Images/coffee_size.png", 50, 50)

# Botones para size del vaso
type_of_glass = Frame(root)
type_of_glass.place(x=440,y=550)
btn_image_coffee_size_small = Button(type_of_glass, image=img_coffee_size_small,command=lambda: btn_presionado("small cup"))
btn_image_coffee_size_small.grid(row=0,column=0)
empty = Label(type_of_glass)
empty.grid(row=0,column=1, padx=20)
btn_image_coffee_size_medium = Button(type_of_glass, image=img_coffee_size_small,command=lambda: btn_presionado("medium cup"))
btn_image_coffee_size_medium.grid(row=0,column=2)


# FIXME cambiar sherk por imagenes reales
#imagen de  cafe con marca
drink_coffee = Frame(root)
drink_coffee.place(x=30,y=170)

# Cargar una sola imagen cafe (imagen representativa de la marca de cafe)
img_coffee1 = load_image("Images/sherk.jpg", 370, 370)

lbl_img_coffee1 = Label(drink_coffee, image=img_coffee1)
lbl_img_coffee1.grid(row=0, column=0)

#imagen de la bandeja donde se entregara el cafe





# prueba = ProcesoAutomata("hola")
# prueba.validarCadena()



# Inicializar ventana
root.mainloop()
