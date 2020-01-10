# MODULO PARA EL LLAMADO DE FUNCIONES

def menusit():
    #os.system("cls") # Limpiar consola en windows es "cls" y en Linux "clear"
    print("#####| (APRENDE PYTHON :)) | #####")
    print("\t1 - ¿Que son las variables?")
    print("\t2 - TIPOS DE DATOS :)")
    print("\t3 - Como definir variables con los tipos de datos")
    print("\t4 - SALIR")
    print("\t ⚠️NOTA: Este script esta en su forma beta aún, faltan muchas cosas para aprender⚠️")

# CONTENIDO SOBRE VARIABLES

def varia():
    print("Haz elegido la opción 1, material a estudiar VARIABLES")
    print("#######################################################\n")
    print("""Una variable sirve para almacenar un tipo de dato dentro de ella & guardarlo ya sea 
        permanentemente o también para luego cambiarle su valor que estaría dentro. Para definir una variable
        solo debes ponerle un tipo de nombre el que desees, recuerda que no puedes colocarle un número inicial
        a esta variable por ejemplo: '1variable = 'hola'. Eso no se puede ya que Python lo detectará como error
        & también te recomiendo no poner espacios en las variables para que así no tengas problemas ejemplo:
        Variable_de = 'hola'. Ahora si para definir una variable debes poner el nombre que deseas & 
        ponerle el signo de igual con espacio para así luego asignarle el valor correspondiente por ejemplo:
        'variable = 'hola como estas'
        Allí tendriamos nuestra variable con el valor dentro que sería un String, recuerda que Python es
        sensible a las mayusculas por lo tanto 'variable & Variable' no son iguales porque una tiene un MAYUS
        & la otra no. Eso sería todo por la materia de VARIABLES""")
    print("#######################################################\n")
        
# TIPO DE DATOS STRING, FLOAT, INT Y BOOLEANO

def tipo():
    print("Haz elegido la opción 1, material a estudiar TIPOS DE DATOS")
    print("#######################################################\n")
    print("""Hay cuatro tipos de datos en Python que serían 'STRING, FLOAT, INT(EGER) & BOOLEANOS
        Primero empezaremos por el mas basico que sería el String.
        
        String: es el tipo de dato donde podemos almacenar una cadena de texto y cadena de texto se hace
        complejo pensar en como una cadena de texto, & sí yo también me confundia dentro de Python cuando
        estaba empezando en esto. Pero a cadena de texto me refiero a que puedes ingresar cualquier tipo de texto
        como el que se te antoje puede ser 'Hola', también en mayusculas 'HOLA' o 'HoLa' puedes escribir lo que 
        desees y este tipo de dato sirve para las variables o para diferentes tipos de cosas. Para definirlo dentro
        de una variable es así 'Mi_Variable = \"hola\"' y así es como podemos meter un String dentro de una
        variable también puedes hacerlo con comillas dobles o comillas simples, solo es cuestión de comodidad.""")
    print("#######################################################\n")
    
    # INPUT PARA SALTAR AL SIGUIENTE TIPO DE DATO
    input("Presione ENTER para continuar con el siguiente tipo de dato.")

    #os.system("cls") # Limpiar
    print("#######################################################\n")
    print("""Int(eger): Este tipo de dato es para los números con el podemos definir números en las
        diferentes tipos de funciones que deseemos emplearlas. Para esto solo debemos escribir el nombre de
        nuestra variable y ponerlo por ejemplo así: ' Mi_Variable = 24' en este caso a 'Mi_Variable' le agregamos
        el valor de tipo integer que sería el número 24 y eso es todo por el tipo de dato integer.""")

    input("Presione ENTER para continuar con el siguiente tipo de dato.")
   # os.system("cls") # Limpiar
    print("#######################################################\n")
    print("""Float: Este tipo de dato es utilizado para número pero con comas entre medio osea
    los números reales que podríamos decirle por ejemplo 'Mi_Variable = 24,1' esto se escribe sin comillas
    arriba como el string, este tipo de dato se describe poniendole una coma al número y ahí pasa a ser
    un dato de tipo float """)

    input("Presione ENTER para continuar con el siguiente tipo de dato.")
   # os.system("cls") # Limpiar
    print("#######################################################\n")
    print("""Booleanos: En esta sección estan dos tipos el False y el True, normalmente se usan cuando los
    usas con un if, elif o else. ahí es cuando todo se llama y por ejemplo si es if resulta ser un valor TRUE
    o else que sería un valor False y así, el elif es solo una abreviación para el if y else, luego lo
    podrás aprender :) """)