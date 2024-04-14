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
        if (validar_precio_cafe == "==2.5"):
            print("Continuando con proceso de café negro...")
            # PROCESO PARA CAFÉ NEGRO
            if (entrada[8:10] == "CP"):
                print("Cargando portafiltro y colocando vaso... ")
            if (entrada[10:12] == "AC"):
                print("Agregando agua caliente...")
            if (entrada[12:15] == "COF"):
                print("Agregando cafe molido...")

        elif (validar_precio_cafe == "!=2.5"):
            # DEVOLVER MENSAJE DE ERROR
            return "Cantidad de monedas incorrecta, devolviendo dinero..."

    elif (validar_tipo_de_cafe == "ES"):
        print("Cafe Espresso")        
        if (validar_precio_cafe == "==3.0"):
            print("Continuando con proceso de café Espresso...")
            # PROCESO PARA CAFÉ ESPRESSO
            if (entrada[8:10] == "CP"):
                print("Cargando portafiltro y colocando vaso ... ")
            if (entrada[10:13] == "COF"):
                print("Agregando café molido...")                
            if (entrada[13:16] == "ACP"):
                print("Agregando agua caliente a presión...")
        elif (validar_precio_cafe == "!=3.0"):
            return "Cantidad de monedas incorrecta, devolviendo dinero..."

    elif (validar_tipo_de_cafe == "AM"):
        print("Cafe Americano")        
        if(validar_precio_cafe == "==4.0"):
            print("Continuando con proceso de cafe Americano...")
            # PROCESO PARA CAFÉ AMERICANO
            if (entrada[8:10] == "CP"):
                print("Cargando portafiltro y colocando vaso ... ")
            if (entrada[10:13] == "COF"):
                print("Agregando café molido...")                
            if (entrada[13:16] == "ACP"):
                print("Agregando agua caliente a presión...")
            if (entrada[16:18] == "AC"):
                print("Agregando agua caliente...")
        elif(validar_precio_cafe == "!=4.0"):
            return "Cantidad de monedas incorrecta, devolviendo dinero..."

    elif (validar_tipo_de_cafe == "CA"):
        print("Cafe Capuccino")        
        if(validar_precio_cafe == "==4.5"):
            print("Continuando con proceso de café Capuccino...")
            # PROCESO PARA CAFÉ CAPUCCINO
            if (entrada[8:10] == "CP"):
                print("Cargando portafiltro y colocando vaso ... ")
            if (entrada[10:13] == "COF"):
                print("Agregando café molido...")                
            if (entrada[13:16] == "ACP"):
                print("Agregando agua caliente a presión...")
            if (entrada[16:18] == "LE"):
                print("Agregando leche...")
            if (entrada[18:21] == "ESP"):
                print("Agregando espuma de leche...")
        elif(validar_precio_cafe == "!=4.5"):
            return "Cantidad de monedas incorrecta, devolviendo dinero..."

    elif (validar_tipo_de_cafe == "LA"):
        print("Cafe Latte")
        if(validar_precio_cafe == "==5.0"):
            print("Continuando con proceso de café Latte...")
            # PROCESO PARA CAFÉ LATTE            
            if (entrada[8:10] == "CP"):
                print("Cargando portafiltro y colocando vaso ... ")
            if (entrada[10:13] == "COF"):
                print("Agregando café molido...")                
            if (entrada[13:16] == "ACP"):
                print("Agregando agua caliente a presión...")
            if (entrada[16:18] == "LE"):
                print("Agregando leche...")
            if (entrada[18:21] == "ESP"):
                print("Agregando espuma de leche...")
            if (entrada[21:23] == "CC"):
                print("Agregando cacao...")
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