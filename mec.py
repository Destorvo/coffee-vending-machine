from tkinter import *
from PIL import Image, ImageTk
from automata_mec import validar_cadena

# Crear ventana
root = Tk() 
root.title("Maquina expendedora de cafe")
root.geometry('690x900')

# Establecer un color de fondo
# root.configure(bg='blue')

# Funcion para cargar imagenes
def load_image(ruta, size_x, size_y):
    image = Image.open(ruta)
    image = image.resize((size_x, size_y))
    return ImageTk.PhotoImage(image)

# Función para imprimir los valores de las cadenas
# Función para imprimir los valores de las cadenas
def print_strings():
    global precio_validado, cadena

        
    # Determinar el precio del café seleccionado
    precio_cafe = 0
    if tipo_cafe_value == "CN":
        precio_cafe = 2.5
    elif tipo_cafe_value == "ES":
        precio_cafe = 3.0
    elif tipo_cafe_value == "AM":
        precio_cafe = 4.0
    elif tipo_cafe_value == "CA":
        precio_cafe = 4.5
    elif tipo_cafe_value == "LA":
        precio_cafe = 5.0
    else:
        print("Error: No se ha seleccionado un tipo de cafe válido.")
        return
    
    # Validar el precio ingresado
    if precio_ingresado_value == precio_cafe:
        precio_validado = "=={}".format(precio_cafe)
    else:
        precio_validado = "!={}".format(precio_cafe)

    # Crear la cadena
    cadena = cafeina_descafeinado_value + tipo_cafe_value + precio_validado + extra_value.get() + "SE"

    print("Tipo de cafe seleccionado:", tipo_cafe_value)
    print("Con cafeina o descafeinado:", cafeina_descafeinado_value)
    print("Cadena de Vainilla/Azucar seleccionados:", extra_value.get())
    print("Cantidad de monedas ingresadas:", precio_ingresado_value)
    print("Precio validado:", precio_validado)
    print("Cadena:", cadena)
    print("=======================")    
    print(validar_cadena(cadena))


# Función para actualizar el tipo de cafe según la selección
def update_tipo_cafe(value):
    global tipo_cafe_value
    tipo_cafe_value =  tipo_cafe_codigos[tipo_de_cafe[value]]

# Función para actualizar el con cafeina o descafeinado según la selección
def update_cafeina_descafeinado(value):
    global cafeina_descafeinado_value
    cafeina_descafeinado_value = cafeina_descafeinado[value]

# Función para construir la cadena según el estado de los botones
def update_extra():
    global extra_value
    if z_vainilla.get() and z_azucar.get():
        extra_value.set("VZ")
    elif z_azucar.get():
        extra_value.set("AZ")
    elif z_vainilla.get():
        extra_value.set("VA")
    else:
        extra_value.set("NA")

# Función para manejar la lógica de selección/deselección de los botones de monedas y actualizar el precio ingresado
def update_precio_ingresado(valor):
    global precio_ingresado_value
    precio_ingresado_value += valor
    # No necesitamos deseleccionar el botón aquí

# Función para desmarcar el botón después de medio segundo
def desmarcar_boton():
    w.set(-1)

# Función para marcar un botón de moneda y programar su desmarca después de un tiempo
def marcar_boton(index):
    w.set(index)
    root.after(500, desmarcar_boton)  # Desmarcar el botón después de 500 milisegundos (medio segundo)


# String para almacenar el valor seleccionado de Vainilla/Azúcar
extra_value = StringVar()

#imagen de  cafe con marca
drink_coffee = Frame(root)
drink_coffee.place(x=30,y=170)
# Cargar una sola imagen cafe (imagen representativa de la marca de cafe)
img_coffee1 = load_image("images/java.png", 350, 370)
lbl_img_coffee1 = Label(drink_coffee, image=img_coffee1)
lbl_img_coffee1.grid(row=0, column=0)


# RADIO BUTTONS
# Seleccionar con cafeina, sin cafeina
cafeina_descafeinado = ["S", "N"]
x = IntVar()
x.set(-1)
for index in range(len(cafeina_descafeinado)):
    radiobutton = Radiobutton(root,
                              text = ["Con cafeina", "Descafeinado"][index],
                              variable=x,
                              value=index,
                              font=50,
                              command=lambda: update_cafeina_descafeinado(x.get()))    
    radiobutton.place(x=490,y=70+index*40)
    # radiobutton.pack(anchor=W)

# Botón para imprimir el valor del string
btn_print_string = Button(root, text="Entregar cafe", command=print_strings)
btn_print_string.place(x=440, y=700 + len(cafeina_descafeinado) * 30)  # Posicionamos el botón debajo de los radio buttons


# String para almacenar el valor seleccionado de cafeina o descafeinado
cafeina_descafeinado_value = ""


# Seleccionar tipo de cafe
# Tipos de cafe
tipo_de_cafe = ["Cafe negro (CN)", "Espresso (ES)", "Americano (AM)", "Capuccino (CA)", "Latte (LA)"]
# Diccionario para mapear nombres de tipos de café a abreviaturas
tipo_cafe_codigos = {
    "Cafe negro (CN)": "CN",
    "Espresso (ES)": "ES",
    "Americano (AM)": "AM",
    "Capuccino (CA)": "CA",
    "Latte (LA)": "LA"
}

y = IntVar()
y.set(-1)
for index in range(len(tipo_de_cafe)):
    radiobutton = Radiobutton(root,
                              text = tipo_de_cafe[index],
                              variable=y,
                              value=index,
                              font=50,
                              command=lambda: update_tipo_cafe(y.get()))    
    radiobutton.place(x=370,y=210+index*40)

# String para almacenar el valor seleccionado de tipo de cafe
tipo_cafe_value = ""


# BOTONES PARA AGREGADOS EXTRA
# MARCAR, DESMARCAR, 1 SOLO, NINGUNO, O LOS DOS
agregado_extra = ["Vainilla", "Azucar"]
z_vainilla = BooleanVar()
z_azucar = BooleanVar()


# Botones para Vainilla y Azucar
btn_vainilla = Checkbutton(root, text="Vainilla", variable=z_vainilla, onvalue=True, offvalue=False, font=50)
btn_azucar = Checkbutton(root, text="Azucar", variable=z_azucar, onvalue=True, offvalue=False, font=50)

btn_vainilla.place(x=560, y=210)  # Posicionar botón "Vainilla"
btn_azucar.place(x=560, y=250)    # Posicionar botón "Azucar"

# Variables de control para la extra_value
extra_value = StringVar()
extra_value.set("NA")


# Etiqueta para mostrar la cadena actual
lbl_cadena = Label(root, textvariable=extra_value)
lbl_cadena.place(x=560, y=290)  # Posicionar la etiqueta

# Asignar la función update_extra a los botones de verificación
z_vainilla.trace_add("write", lambda *args: update_extra())
z_azucar.trace_add("write", lambda *args: update_extra())





# BOTONES PARA INDICAR MONEDAS INGRESADAS
# APRETABLES MaS DE 1 VEZ, VARIAS OPCIONES
# Seleccionar moneda ingresada

# Botones para indicar moneda ingresada
tipo_moneda = [0.5, 1, 2, 5]
w = IntVar()
w.set(-1)

 # Inicializar el precio ingresado
precio_ingresado_value= 0 



for index in range(len(tipo_moneda)):
    radiobutton = Radiobutton(root,
                              text="S/. " + str(tipo_moneda[index]),
                              variable=w,
                              value=index,
                              font=50,
                              command=lambda index=index: update_precio_ingresado(tipo_moneda[index]))
    # Posicionar los radio buttons usando place()
    if index == 0:
        radiobutton.place(x=450, y=470)  # Primer botón en la posición especificada
    elif index == 1:
        radiobutton.place(x=450, y=560)  # Segundo botón debajo del primer botón
    elif index == 2:
        radiobutton.place(x=550, y=470)  # Tercer botón al lado del primer botón
    else:
        radiobutton.place(x=550, y=560)  # Cuarto botón debajo del tercer botón
    
    # Llamar a la función para marcar el botón
    radiobutton.bind("<ButtonPress-1>", lambda event, index=index: marcar_boton(index))


# imagen de la bandeja donde se entregara el cafe




# Inicializar ventana
root.mainloop()
