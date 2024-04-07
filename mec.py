from tkinter import *
from PIL import Image, ImageTk
# from proceso import ProcesoAutomata

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

# Función para imprimir el string actual
def print_strings():
    print("Tipo de cafe seleccionado:", tipo_cafe_value)
    print("Con cafeina o descafeinado:", cafeina_descafeinado_value)

# Función para actualizar el tipo de cafe según la selección
def update_tipo_cafe(value):
    global tipo_cafe_value
    tipo_cafe_value =  tipo_cafe_codigos[tipo_de_cafe[value]]

# Función para actualizar el con cafeina o descafeinado según la selección
def update_cafeina_descafeinado(value):
    global cafeina_descafeinado_value
    cafeina_descafeinado_value = cafeina_descafeinado[value]


#imagen de  cafe con marca
drink_coffee = Frame(root)
drink_coffee.place(x=30,y=170)
# Cargar una sola imagen cafe (imagen representativa de la marca de cafe)
img_coffee1 = load_image("images/java.png", 370, 370)
lbl_img_coffee1 = Label(drink_coffee, image=img_coffee1)
lbl_img_coffee1.grid(row=0, column=0)


# RADIO BUTTONS

# Seleccionar con cafeina, sin cafeina
cafeina_descafeinado = ["S", "N"]
x = IntVar()
x.set(-1)
# 440 190
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
btn_print_string = Button(root, text="Imprimir valor del string", command=print_strings)
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
    radiobutton.place(x=410,y=210+index*40)

# String para almacenar el valor seleccionado de tipo de cafe
tipo_cafe_value = ""







# BOTONES PARA AGREGADOS EXTRA
# MARCAR, DESMARCAR, 1 SOLO, NINGUNO, O LOS DOS
agregado_extra = ["Vainilla", "Azucar"]
z_vainilla = BooleanVar()
z_azucar = BooleanVar()

# Función para manejar la lógica de activación/desactivación de los botones de agregados extra
def update_agregados_extra():
    pass  # No necesitamos realizar ninguna acción específica aquí

# Botones para Vainilla y Azucar
btn_vainilla = Checkbutton(root, text="Vainilla", variable=z_vainilla, onvalue=True, offvalue=False, font=50)
btn_azucar = Checkbutton(root, text="Azucar", variable=z_azucar, onvalue=True, offvalue=False, font=50)

btn_vainilla.place(x=560, y=210)  # Posicionar botón "Vainilla"
btn_azucar.place(x=560, y=250)    # Posicionar botón "Azucar"



# Función para construir la cadena según el estado de los botones
def construir_cadena():
    global cadena
    if z_vainilla.get() and z_azucar.get():
        cadena.set("AV")
    elif z_azucar.get():
        cadena.set("AZ")
    elif z_vainilla.get():
        cadena.set("VA")
    else:
        cadena.set("NA")

# Variables de control para la cadena
cadena = StringVar()
cadena.set("NA")

# Etiqueta para mostrar la cadena actual
lbl_cadena = Label(root, textvariable=cadena)
lbl_cadena.place(x=560, y=290)  # Posicionar la etiqueta

# Asignar la función construir_cadena a los botones de verificación
z_vainilla.trace_add("write", lambda *args: construir_cadena())
z_azucar.trace_add("write", lambda *args: construir_cadena())



# BOTONES PARA INDICAR MONEDAS INGRESADAS
# APRETABLES MÁS DE 1 VEZ, VARIAS OPCIONES
# Seleccionar moneda ingresada
tipo_moneda = ["S/. 0.5", "S/. 1", "S/. 2", "S/. 5"]
w = IntVar()
w.set(-1)
for index in range(len(tipo_moneda)):
    radiobutton = Radiobutton(root,
                              text = tipo_moneda[index],
                              variable=w,
                              value=index,
                              font=50)    
        # Posicionar los radio buttons usando place()
    if index == 0:
        radiobutton.place(x=450, y=470)  # Primer botón en la posición especificada
    elif index == 1:
        radiobutton.place(x=450, y=560)  # Segundo botón debajo del primer botón
    elif index == 2:
        radiobutton.place(x=550, y=470)  # Tercer botón al lado del primer botón
    else:
        radiobutton.place(x=550, y=560)  # Cuarto botón debajo del tercer botón


# Botones con azucar, check y con vainilla en la tercera fila
img_sugar = load_image("images/sugar.webp", 50, 50)
img_check = load_image("images/sherk.jpg", 50, 50)
img_vanilla = load_image("images/vainilla.png", 50, 50)



#imagen de la bandeja donde se entregara el cafe


# prueba = ProcesoAutomata("hola")
# prueba.validarCadena()


# Inicializar ventana
root.mainloop()
