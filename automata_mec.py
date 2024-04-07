"""
Las cadenas que acepta el autómata(crea la máquina) para que pueda servir el cafe son:

(S | N) ( CN | ES | AM | CA | LA ) ( 2.5 | 3.0 | 4.0 | 4.5 | 5.0 ) ( EL PROCESO, LA MAQUINA LO AGREGA
A LA CADENA LUEGO DE ESCOGER EL TIPO DE CAFE ) ( V | A | NA ) SE

Las cadenas que acepta el autómata para regresar al inicio y no servir cafe son:

(S | N) ( CN | ES | AM | CA | LA ) ( CUALQUIER PRECIO DIFERENTE A LOS ESTABLECIDOS ) <- AQUI EL AUTOMATA VUELVE
AL INICIO PORQUE VALIDARA EL PRECIO Y SERA INCORRETO

 ( EL PROCESO, LA MAQUINA LO AGREGA
A LA CADENA LUEGO DE ESCOGER EL TIPO DE CAFE ) ( V | A | NA ) SE

"""
class automata_mec:
    def __init__(self, entrada):
        self.entrada = entrada



# con cafeina, cafe negro, 2 soles 50 centimos (proceso, esto se agrega solo) sin añadidos extra, servir
cadena = "SCN2.5" + "CPACCOFNASE" + "NASE"

# sin cafeina, cafe negro, 2 soles 50 centimos (proceso, esto se agrega solo) añadir vainilla, servir
# cadena = "NCN205CPACCOFVSE"
 
# con cafeina, cafe negro, 5 soles(dinero incorrecto) (proceso, esto se agrega solo) sin añadidos extra, servir
# cadena = "SCN5CPACCOFNASE"

validar_cafeina = cadena [0:1]
validar_tipo_de_cafe = cadena[1:3]
validar_precio_cafe = cadena[3:6]
print(validar_precio_cafe)

if (validar_cafeina == "S"):
    print("Preparando cafe con cafeina")

elif (validar_cafeina == "N"):
    print("Preparando cafe descafeinado")  

if (validar_tipo_de_cafe == "CN"):
    print("Cafe negro")
    if(validar_precio_cafe == "2.5"):
        print("Continuando con proceso de cafe negro...")
    else:
        print("No se pudo continuar, volviendo al inicio...")

elif (validar_tipo_de_cafe == "ES"):
    print("Cafe Espresso")        
    if(validar_precio_cafe == "3.0"):
        print("Continuando con proceso de cafe Espresso...")
    else:
        print("No se pudo continuar, volviendo al inicio...")

elif (validar_tipo_de_cafe == "AM"):
    print("Cafe Americano")        
    if(validar_precio_cafe == "4.0"):
        print("Continuando con proceso de cafe Americano...")
    else:
        print("No se pudo continuar, volviendo al inicio...")

elif (validar_tipo_de_cafe == "CA"):
    print("Cafe Capuccino")        
    if(validar_precio_cafe == "4.5"):
        print("Continuando con proceso de cafe Capuccino...")
    else:
        print("No se pudo continuar, volviendo al inicio...")

elif (validar_tipo_de_cafe == "LA"):
    print("Cafe Latte")
    if(validar_precio_cafe == "5.0"):
        print("Continuando con proceso de cafe Latte...")
    else:
        print("No se pudo continuar, volviendo al inicio...")



# con cafeina, cafe negro 2 soles 50 centimos (proceso, esto se agrega solo) sin añadidos extra, servir
cadena = "SLA5CPACCOFNASE"

# con cafeina, cafe negro 2 soles 50 centimos (proceso, esto se agrega solo) sin añadidos extra, servir
cadena = "SCN205CPACCOFNASE"

# con cafeina, cafe negro 2 soles 50 centimos (proceso, esto se agrega solo) sin añadidos extra, servir
cadena = "SCN205CPACCOFNASE"

# con cafeina, cafe negro 2 soles 50 centimos (proceso, esto se agrega solo) sin añadidos extra, servir
cadena = "SCN205CPACCOFNASE"