"""
Las cadenas que acepta el autómata(crea la máquina) para que pueda servir el cafe son:

(S | N) ( CN | ES | AM | CA | LA ) ( 2.5 | 3.0 | 4.0 | 4.5 | 5.0 ) ( EL PROCESO, LA MAQUINA LO AGREGA
A LA CADENA LUEGO DE ESCOGER EL TIPO DE CAFE ) ( VA | AZ | VZ | NA ) SE

Las cadenas que acepta el autómata para regresar al inicio y no servir cafe son:

(S | N) ( CN | ES | AM | CA | LA ) ( CUALQUIER PRECIO DIFERENTE A LOS ESTABLECIDOS ) ( EL PROCESO, LA MAQUINA LO AGREGA
A LA CADENA LUEGO DE ESCOGER EL TIPO DE CAFE ) ( VA | AZ | VZ | NA ) SE

"""
class automata_mec:
    def _init_(self, entrada):
        self.entrada = entrada
        
def validar_cadena(entrada):
    validar_cafeina = entrada [0:1]
    validar_tipo_de_cafe = entrada[1:3]
    validar_precio_cafe = entrada[3:8]

    if (validar_cafeina == "S"):
        print("Preparando cafe con cafeina")

    elif (validar_cafeina == "N"):
        print("Preparando cafe descafeinado")  
    else:
        return "Por favor, seleccione entre café descafeinado o con cafeina para continuar..."
    
    if (validar_tipo_de_cafe == "CN"):
        print("Cafe negro")
        if(validar_precio_cafe == "==2.5"):
            print("Continuando con proceso de cafe negro...")
            # PROCESO PARA CAFÉ NEGRO
            print("Cargando el portafiltro y poniendo el vaso ... ")
            print("Agregando agua caliente...")
            print("Agregando cafe molido ...")

        elif (validar_precio_cafe == "!=2.5"):
            # DEVOLVER MENSAJE DE ERROR
            return "Cantidad de monedas incorrecta, devolviendo dinero..."

    elif (validar_tipo_de_cafe == "ES"):
        print("Cafe Espresso")        
        if(validar_precio_cafe == "==3.0"):
            print("Continuando con proceso de cafe Espresso...")
            # PROCESO PARA CAFÉ ESPRESSO
            print("Cargando el portafiltro y colocando el vaso ... ")
            print("Agregando café molido ...")
            print("Agregando agua caliente a presión ...")

        elif(validar_precio_cafe == "!=3.0"):
            return "Cantidad de monedas incorrecta, devolviendo dinero..."

    elif (validar_tipo_de_cafe == "AM"):
        print("Cafe Americano")        
        if(validar_precio_cafe == "==4.0"):
            print("Continuando con proceso de cafe Americano...")
            # PROCESO PARA CAFÉ AMERICANO
            print("Cargando el portafiltro y colocando el vaso ... ")
            print("Agregando café molido ...")
            print("Agregando agua caliente a presión ...")
            print("Agregando agua caliente final ... ")

        elif(validar_precio_cafe == "!=4.0"):
            return "Cantidad de monedas incorrecta, devolviendo dinero..."

    elif (validar_tipo_de_cafe == "CA"):
        print("Cafe Capuccino")        
        if(validar_precio_cafe == "==4.5"):
            print("Continuando con proceso de cafe Capuccino...")
            # PROCESO PARA CAFÉ CAPUCCINO
            print("Cargando el portafiltro y colocando el vaso ... ")
            print("Agregando café molido ...")
            print("Agregando agua caliente a presión ...")
            print("Agregando Leche ... ")
            print("Agregando espuma de leche  ... ")

        elif(validar_precio_cafe == "!=4.5"):
            return "Cantidad de monedas incorrecta, devolviendo dinero..."

    elif (validar_tipo_de_cafe == "LA"):
        print("Cafe Latte")
        if(validar_precio_cafe == "==5.0"):
            print("Continuando con proceso de cafe Latte...")
            # PROCESO PARA CAFÉ LATTE
            print("Cargando el portafiltro y colocando el vaso ... ")
            print("Agregando café molido ...")
            print("Agregando agua caliente a presión ...")
            print("Agregando Leche ... ")
            print("Cargando espuma de leche ... ")
            print("Agregando cacao ...")

        elif(validar_precio_cafe == "!=5.0"):            
            return "Cantidad de monedas incorrecta, devolviendo dinero...\n\n"
    
    if (entrada[-4:-2]=="NA"):
        print("No agregados extra")
    elif (entrada[-4:-2]=="VA"):
        print("Agregando vainilla...")
    elif (entrada[-4:-2]=="AZ"):
        print("Agregando azucar...")
    elif (entrada[-4:-2]=="VZ"):
        print("Agregando vainilla y azucar...")
    if (entrada[-2:]=="SE"):
        print("Sirviendo cafe...")
        # DEVOLVER MENSAJE DE CAFE NEGRO ENTREGADO CORRECTAMENTE
        return "Cafe entregado correctamente\n\n"
    else:
        return "Error: Se ingreso una cadena invalida\n\n"





""""
# con cafeina, cafe negro 2 soles 50 centimos (proceso, esto se agrega solo) sin añadidos extra, servir
cadena = "SLA5CPACCOFNASE"

# con cafeina, cafe negro 2 soles 50 centimos (proceso, esto se agrega solo) sin añadidos extra, servir
cadena = "SCN205CPACCOFNASE"

# con cafeina, cafe negro 2 soles 50 centimos (proceso, esto se agrega solo) sin añadidos extra, servir
cadena = "SCN205CPACCOFNASE"

# con cafeina, cafe negro 2 soles 50 centimos (proceso, esto se agrega solo) sin añadidos extra, servir
cadena = "SCN205CPACCOFNASE"
"""