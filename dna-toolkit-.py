# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 14:20:04 2021
Last updated on Mon Sep 20 23:52:30 2021

@author: mbioinf (Sergio Alías Segura)
"""


### MODULES IMPORT ###

import pickle # Para guardar los objetos en el disco
import os # Para tener acceso a los ficheros y directorios, borrar y demás
import re # Para la función que lista los ficheros del directorio
from random import randint # Para generar mutaciones y elegir nucleótidos al azar
from datetime import datetime # Para generar nombres de fichero únicos

###----------------###



### DNA CLASS DEFINITION ###

class DNA:

    """
    Esta clase servirá para instanciar objetos de tipo DNA, que tendrán
    la cadena de DNA como atributo.
    El atributo _chain contiene la cadena, que se genera con un setter,
    cubriendo así la opción 1 del programa simplemente instanciando un objeto.
    También tiene un getter que no hace nada especial, pero se me hacía raro
    tener setter y no getter así que más adelante en el programa accedo a _chain
    siempre con él.

    El resto de métodos cubren todas las operaciones del submenú de Operaciones
    con cadenas de DNA. Hay métodos para regenerar (el propio setter), validar,
    mutar, contar frecuencias y contar patrones en la cadena de DNA
    (esto es, en el atributo _chain)
    """

    nucleotides = ("A", "C", "G", "T") # Una tupla con los 4 nucleótidos que será muy utilizada
    
    def __init__(self, n):
        """
        n -> Longitud de la cadena (número de nucleótidos). P. ej., 30
        El constructor llama al setter de _chain para que se genere la cadena.
        """
        self.set_chain(n)

    def set_chain(self, n):
        """
        El setter de _chain, genera una cadena de longitud n.
        Para cada posición escoge de la tupla de nucleótidos uno al azar.
        """
        self._chain = ""
        for i in range(n):
            self._chain = self._chain + self.nucleotides[randint(0,3)]

    def get_chain(self): # El getter de _chain
        return self._chain

    def is_chain_valid(self):
        """
        Comprueba que cada nucleótido esté dentro de la tupla de nucleótidos.
        Retorna True si la cadena es válida y False si no lo es.
        Más adelante en el programa describo cómo he comprobado yo 
        que funciona validando una cadena incorrecta.
        """
        is_valid = True
        for i in self._chain:
            if i not in self.nucleotides:
                is_valid = False
        return is_valid

    def mutate(self, n):
        """
        n -> Cantidad de mutaciones deseada. P. ej., 3
        Sustituye n nucleótidos de n posiciones al azar.
        Se asegura de que las n mutaciones ocurran en n posiciones diferentes entre sí,
        siempre y cuando el nº de mutaciones no sea mayor a la longitud de la cadena (en
        ese caso no tiene en cuenta posiciones repetidas).
        También se asegura de que no se sustituya un nucleótido por sí mismo,
        p. ej., cambio de A por otra A. Si hay más mutaciones que posiciones, puede
        darse el caso de que parezca que no ha mutado (si por ejemplo mutamos
        la cadena "A" 3 veces y ocurre que A -> G -> T -> A), pero es por pura casualidad.
        """
        list_chain = list(self._chain) # La cadena en forma de lista, que es más comodo para cambiar las mutaciones
        prev_positions = [] # Una lista donde voy llevando la cuenta de qué posiciones han mutado ya, para no repetirlas
        for i in range(n): # Repetir por cada mutación deseada
            next_position = randint(0, len(list_chain) - 1) # Saco una posición al azar
            if n < len(self._chain): # "Si hay menos mutaciones que posiciones:"
                while next_position in prev_positions: # "Comprueba que la posición haya mutado antes, y en tal caso..."
                    next_position = randint(0, len(list_chain) - 1) # "... busca otra posición"
            """
            El bloque if anterior se ignora si hay más mutaciones que posiciones,
            permitiendo así que se repitan los sitios.
            """
            mutation = self.nucleotides[randint(0,3)] # Un nucleótido al azar
            while list_chain[next_position] == mutation: # "Comprueba que el nucleótido que quiero cambiar y el que voy a introducir sean el mismo, y en tal caso..."
                mutation = self.nucleotides[randint(0,3)] # "... genera otro nucleótido al azar"
            list_chain[next_position] = mutation # Cuando sean diferentes ocurrirá la mutación
            prev_positions.append(next_position) # Y añado la posición a la lista para que se tenga en cuenta para posibles próximas mutaciones
        self._chain = "".join(list_chain) # Al acabar, uno la lista en un string y se la asigno a _chain

    def freq_count(self):
        """
        Método para contar frecuencias. No tiene mucho misterio.
        Abro un diccionario y recorro la cadena contando cuantas veces
        aparece cada nucleótido, y lo voy guardando en el diccionario.
        Retorna el diccionario.
        """
        freq_dict = {}
        for i in self._chain:
            if i in freq_dict:
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1
        return freq_dict

    def pattern_count(self, pattern):
        """
        pattern -> patrón de nucleótidos. P. ej., "ATG"
        Método para contar apariciones de un patrón.
        Recorro la cadena hasta que llegue a la última posición
        donde tendría sentido buscar el patrón. Por ejemplo,
        si busco un patrón de 3 nucleótidos itero hasta la antepenúltima
        posición de la cadena, porque es la última posición donde cabría
        un patrón de 3. Por eso en el bucle for le resto a la longitud de
        la cadena la longitud del patrón + 1.
        Retorna el número de veces que aparece el patrón.
        """
        count = 0
        for i in range(len(self._chain) - len(pattern) + 1):
            if self._chain[i:i+len(pattern)] == pattern:
                count += 1
        return count

###----------------------###



### FUNCTIONS ###

"""
Las funciones cubren todas las opciones del menú principal,
exceptuando la de generar una cadena, que va en el setter de la clase;
y la de borrar una cadena, que es simplemente una línea corta
y la pongo directamente en el programa.
Además de eso hay: un generador de nombres, funciones para pedir
por input un integer, un nombre de fichero y un patrón de DNA,
funciones para el menú principal y el submenú de operaciones,
y una función que se usa para preguntar si estás seguro de
hacer alguna acción "importante" (borrar ficheros, sobreescribirlos,
salir del programa, etc).
"""


def name_generator():
    '''
    Genera un nombre para el fichero donde se guardará el objeto de tipo DNA.
    El formato del nombre será 'chain_YYYYMMDD_hhmmss_ss.pickle'.
    Añado décima y centésima de segundo por si acaso la persona que use el código 
    fuese tan veloz que pudiese generar dos ficheros en un mismo segundo.
    Retorna el nombre generado.
    '''
    add_name = str(datetime.now()) # Cuardo el datetime como string
    add_name = "chain_" + add_name[0:4] + add_name[5:7] + add_name[8:10] + "_" + add_name[11:13] + add_name[14:16] + add_name[17:19] + "_" + add_name[20:22] + ".pickle"
    # Y arriba lo modifico para que quede a mi gusto
    return add_name


def save_chain(DNA_obj, name):
    '''
    DNA_obj -> un objeto instanciado de la clase DNA.
    name -> nombre de fichero, creado desde fuera con name_generator.
    Función para guardar en formato pickle.
    '''
    with open('{}'.format(name), 'wb') as mysavedchain:
        pickle.dump(DNA_obj, mysavedchain)


def load_chain(filename):
    '''
    filename -> nombre del fichero que se quiere cargar.
    Función para cargar un objeto guardado previamente.
    '''
    with open(filename, 'rb') as myrestoredchain:
        loaded_data = pickle.load(myrestoredchain)
    return loaded_data


def chain_file_sorter():
    '''
    Itera sobre los ficheros del directorio de trabajo y
    se queda con los 'chain_YYYYMMDD_hhmmss_ss.pickle'.
    Retorna una lista con sus nombres de fichero.
    '''
    chain_list = [] # La lista de ficheros comienza vacía
    for i in os.listdir(os.getcwd()): # "Por cada fichero en mi directorio de trabajo..."
        if (re.match(r'chain_[0-9]{8}_[0-9]{6}_[0-9]{2}.pickle', i)): # "Si cumple con mi formato de nombres..."
            chain_list.append(i) # "... añade su nombre a la lista"
    return chain_list # Retorno la lista


def ask_for_int(input_msg):
    """
    input_msg --> Mensaje para que pida input al usuario.
    Esta función retorna el imput dado por el usuario,
    asegurándose de que sea un integer mayor que 0.
    """
    my_int = None # Creo la variable, por ahora vale None
    while my_int is None: # "Mientras que my_int valga None..."
        try:
            my_int = eval(input(input_msg)) # Pido un número. Si eval falla, no habrá asignación a my_int y seguirá valiendo None. Si eval no falla pero no tengo un integer mayor que 0...
            if isinstance(my_int, str) or isinstance(my_int, float) or my_int <= 0: # ... lo compruebo aquí.
                """
                Este if comprueba si el input es una cadena entre comillas
                o un número menor o igual a 0. El orden de las comprobaciones importa.
                Si pongo primero la comparación numérica y el input es un string
                con comillas, se dispara un TypeError que por alguna razón que
                no comprendo no puedo capturar en el bloque except. Supongo que
                tendrá que ver con que la excepción esté dentro de un if, pero
                como así ya funciona no le doy más vueltas.
                """
                my_int = None # Como en este punto my_int tendrá asignado algún valor tipo "cadena" o -5, le vuelvo a asignar None para que no se salga del bucle while
                raise NameError # Disparo un NameError. Podría haber disparado cualquier otro, pero así aprovecho que iba a capturarlo abajo de todos modos.
        except (NameError, SyntaxError): 
            """ Este except captura el NameError del eval y el que dispara el if, y también el SyntaxError
            cuando haces un input vacío.
            """
            print("Parece que has introducido un dato no numérico o menor de 1")
    return my_int # Retorno el integer mayor que 0.


def ask_for_file():
    """
    Esta función retorna el imput dado por el usuario,
    asegurándose de que sea el nombre de un fichero existente y
    de la forma 'chain_YYYYMMDD_hhmmss_ss.pickle'.
    """
    if not chain_file_sorter(): # "Si al listar los ficheros de tipo 'chain_YYYYMMDD_hhmmss_ss.pickle' no encuentra ninguno:"
        print("No tienes archivos del tipo \'chain_YYYYMMDD_hhmmss_ss.pickle\' en el directorio de trabajo.")
    else: # "Si hay ficheros del tipo 'chain_YYYYMMDD_hhmmss_ss.pickle' en el directorio:"
        my_file = (input("Indica el nombre del fichero: ")).lower() # "Pide el nombre"
        while my_file not in chain_file_sorter(): # "Mientras que el usuario siga dando nombres que no estás en la lista:"
            my_file = (input("Parece que ese fichero no existe. Comprueba su nombre (debe seguir la estructura \'chain_YYYYMMDD_hhmmss_ss.pickle\') e inténtalo de nuevo: ")).lower() # "Sigue pidiéndole nombres válidos"
        return my_file # Retorna el nombre de fichero válido y existente


def ask_for_pattern():
    """
    Esta función retorna el imput dado por el usuario,
    asegurándose de que sea un patrón de nucleótidos.
    Dentro de ella hay una variable que declaro luego
    en el programa principal:
    current_obj -> El objeto de clase DNA con el que se
    esté trabajando en ese momento.
    """   
    valid_pattern = False # Variable de control
    while valid_pattern == False: # Mientras sea falsa:
        valid_pattern = True # La pongo en True
        my_pattern = (input("Indica el patrón de nucleótidos: ")).upper() # Pido el patrón
        for i in my_pattern:
            if i not in current_obj.nucleotides:
                valid_pattern = False # Y si algún nucleótido no es válido vuelve a ser False
        if valid_pattern == False:
            print("El patrón \'{}\' no es válido".format(my_pattern)) # Mensajito de aviso y vuelve a empezar el while
    return my_pattern # Finalmente retorna un patrón válido


def main_menu():
    '''
    Función que imprime el menú. Dentro de ella hay variables
    que declaro luego en el programa principal:
    current_chain -> lleva la cadena actual.
    current_chain_filename -> lleva el fichero donde se guarda.
    unsaved_changes = Booleano para saber si hay cambios sin guardar.

    '''
    print("""Por favor, selecciona una opción:

1. Crear nueva cadena de DNA
2. Guardar cadena de DNA
3. Cargar cadena de DNA
4. Listar cadenas de DNA guardadas
5. Borrar cadena de DNA del disco
6. Operaciones con cadenas de DNA (+)
7. Salir
""")
    print("Cadena actual: [{}]".format(current_chain))
    if unsaved_changes == False:
        print("Guardada en: {}".format(current_chain_filename))
    else:
        print("Guardada en: {} (Cambios sin guardar)".format(current_chain_filename))


def operation_menu(): # Igual para el submenú de operaciones
    print("""Operaciones para cadenas de DNA:

1. Regenerar cadena de DNA
2. Validar cadena de DNA
3. Mutar cadena de DNA
4. Medir frecuencia de nucleótidos
5. Contar patrones en la cadena de DNA
6. Atrás
""")
    print("Cadena actual: [{}]".format(current_chain))
    if unsaved_changes == False:
        print("Guardada en: {}".format(current_chain_filename))
    else:
        print("Guardada en: {} (Cambios sin guardar)".format(current_chain_filename))


def ask_if_sure(ask_msg, ask_again_msg):
    """
    ask_msg -> String para pedir hacer tal ("S") o cual cosa ("N")
    ask_again_msg -> String cuando se introduce algo diferente de "S" y "N".
    Función para confirmar acciones.
    Retorna "S" o "N".
    """
    sure = (input(ask_msg)).upper()
    while sure != "S" and sure != "N":
        sure = (input(ask_again_msg)).upper()
    return sure


###-----------###



### PROGRAMA PRINCIPAL ###

# Primero defino algunas variables que necesito.

no_current_chain = "No hay ninguna cadena de DNA cargada"
current_chain = no_current_chain # La cadena actual, por defecto le asigno un mensaje de que no hay cadena.
current_chain_not_saved = "[la cadena no está guardada en disco]"
current_chain_filename = current_chain_not_saved # Lo mismo para el fichero donde está guardada la cadena.

option = 0 # La opción escogida en el menú.
are_you_sure = "N" # La confirmación para salir del programa (la uso en la condición del próximo bucle while).
unsaved_changes = False # Variable para saber si hay cambios no guardados, así puedo personalizar el menú y las confirmaciones al salir del programa.

# Mensajito de bienvenida:

print("""
 ___________________________________________________________
|                                                           |
|  Bienvenidx a DNA-Toolkit v1.0 (powered by Sergio Alías)  |
|___________________________________________________________|

<< DNA-Toolkit te permitirá crear, gestionar y trabajar con cadenas de DNA >>
""")


while not(option == "7" and are_you_sure == "S"): # Mientras que no se escoja la opción de salir y se esté seguro de querer hacerlo:

    main_menu() # Imrpimo el menú principal

    option = input("Selecciona una opción: ") # Pido una opción

    if option == "1":
        print("Has seleccionado 1: Crear nueva cadena de DNA")
        print("Esta acción sustituirá tu cadena actual, la cual perderás si no la has guardado previamente")
        longitud = ask_for_int("Indica la longitud de la cadena a generar: ") # Llama a la función que se asegura de que sea integer mayor que 0
        current_obj = DNA(longitud) # Instancio un objeto de la clase DNA que tendrá una cadena de longitud "longitud"
        current_chain = current_obj.get_chain() # Le asigno la cadena del objeto usando su getter
        print("Cadena generada: {}".format(current_chain)) # Mensajito de confirmación
        unsaved_changes = True # ¡Ahora tenemos cambios sin guardar!
        current_chain_filename = current_chain_not_saved # Si teníamos cargado un fichero antes, al generar otra cadena en el menú debe aparecer que la cadena no está guardada en ninguna parte.
    
    elif option == "2":
        print("Has seleccionado 2: Guardar cadena de DNA")
        if current_chain_filename == current_chain_not_saved: # Si la cadena no está guardada:
            if current_chain != no_current_chain: # Si tengo cadena actual:
                current_chain_filename = name_generator() # Genera un nombre de fichero
                save_chain(current_obj, current_chain_filename) # Guarda el objeto en disco
                print("Se ha guardado la cadena en el fichero {}".format(current_chain_filename)) # Y mensajito de confirmación
                unsaved_changes = False # Los cambios, de haberlos, ya están guardados
            else: # Si por el contrario no tienes cadena actual:
                print("Debes tener alguna 'Cadena actual' para usar esta opción") # Recuérdaselo al usuario amablemente
        else: # Si resulta que la cadena proviene de algún fichero que ya existe:
            save_decision = ask_if_sure("¿Sobreescribir el archivo {} (S) o crear uno nuevo (N)? ".format(current_chain_filename), "Por favor, responde con Sobreescribir (S) o Nuevo fichero (N): ")
            # Arriba pregunta si quieres sobreescribir ese fichero o si prefieres crear un nuevo
            if save_decision == "S": # Si quieres sobreescribirlo:
                save_chain(current_obj, current_chain_filename) # Pues dicho y hecho
                print("Se ha sobreescrito la cadena del fichero {}".format(current_chain_filename)) # Mensajito
                unsaved_changes = False # Y ya estarían guardados los cambios
            if save_decision == "N": # Si prefieres guardarlo en un fichero nuevo:
                current_chain_filename = name_generator() # Genero otro nombre
                save_chain(current_obj, current_chain_filename) # Y lo guardo ahí
                print("Se ha guardado la cadena en el fichero {}".format(current_chain_filename)) # Mensajito
                unsaved_changes = False # Y cambios guardados

    elif option == "3":
        print("Has seleccionado 3: Cargar cadena de DNA")
        print("Esta acción sustituirá tu cadena actual, la cual perderás si no la has guardado previamente")
        chain_loading = ask_for_file() # Pido un fichero existente con nombre válido
        if chain_file_sorter():
            """
            "Si hay ficheros con nombre válido en el directorio:". Hay que asegurarse porque, si no los hay, ask_for_file retorna None, y entonces si se intentase ejecutar el código de abajo el programa petaría.
            """
            try: #Intenta:
                current_obj = load_chain(chain_loading) # Cargar el objeto
                current_chain = current_obj.get_chain() # Asignar la cadena a su correspondiente variable
                current_chain_filename = chain_loading # Lo mismo con el nombre del fichero
                print("Cadena {} cargada correctamente desde {}".format(current_chain, current_chain_filename)) # Mensajito
                unsaved_changes = False # Y no hay cambios sin guardar
            except Exception:
                """
                Si el bloque anterior dispara un error, será porque en el fichero especificado no hay un objeto de clase DNA guardado. Esto puede deberse a que alguien haya creado desde fuera del programa un fichero respetando el formato que uso para los nombres. Si eso pasa, capturo aquí el error y se lo hago saber de forma pasivo-agresiva.
                """
                print("Parece que estás haciendo cosas extrañas con ficheros desde fuera del programa. Se te enviará de vuelta al menú principal")

    elif option == "4":
        print("Has seleccionado 4: Listar cadenas de DNA guardadas")
        if chain_file_sorter(): # Si hay ficheros de nombre válido en el directorio:
            print("La cadenas de DNA guardadas en el directorio {} son:".format(os.getcwd()))
            j = 1 # Variable para numerar el output
            for i in chain_file_sorter(): # Recorro la lista de ficheros de nombre válido
                try:
                    print("{}.- {} ({})".format(j, load_chain(i).get_chain(), i)) 
                    # Arriba intento acceder al atributo de la cadena para hacer el print
                except Exception: # Si lo de arriba falla es porque es un fichero creado desde fuera
                    print("{}.- Fichero corrupto ({})".format(j, i)) # Así que se lo hago saber al usuario
                j += 1 # Aumento la variable
        else: # Si no encuentra ficheros con nombre válido:
            print("No existen cadenas de DNA guardadas en {}".format(os.getcwd())) # Se lo dice al usuario

    elif option == "5":
        del_choice = None
        """
        Preparo la variable ya y le doy cualquier valor (por ejemplo None) porque
        si resulta que no hay ficheros en el directorio, cuando llegue al if de la línea
        442 se dispararía un error al no estar definida la variable del_choice.
        """
        print("Has seleccionado 5: Borrar cadena de DNA del disco")
        chain_deleting = ask_for_file() # Pido nombre válido de fichero, en caso de que haya ficheros válidos
        if chain_file_sorter(): # Este if exsite por la misma razón que el de la línea 400
            del_choice = ask_if_sure("¿Estás segurx de que quieres borrar el fichero \'{}\'? (S/N): ".format(chain_deleting), "Por favor, responde con Sí (S) o No (N): ") # Pregunto si está seguro
        if del_choice == "S": # Si lo está:
            if chain_deleting == current_chain_filename: # Compruebo si la cadena que intenta borrar es la que está cargada, y en tal caso:
                current_chain_filename = current_chain_not_saved # Le quito el nombre de fichero a la cadena y le pongo el mensaje de "la cadena no está guardada"
                unsaved_changes = True # Como ahora no está guardada, hay cambios sin guardar
            os.remove(chain_deleting) # Finalmente borro el fichero
            # Lo bueno de esto es que aunque borres el fichero del disco, si tenías la cadena cargada se mantendrá en la memoria de Python por si decides volver a guardarla.

    elif option == "6":
        print("Has seleccionado 6: Operaciones con cadenas de DNA")
        if current_chain == no_current_chain: # Si no tienes cadena cargada no te deja entrar al submenú
            print("No tienes ninguna cadena generada o cargada")
        else: # Si tienes cadena cargada sí te deja entrar
            sec_option = 0 # La variable para las opciones del submenú
            while sec_option != "6": # Mientras que no selecciones la opción 'Atrás'
                
                operation_menu() # Imprime el submenú
            
                sec_option = input("Selecciona una operación: ") # Pide que selecciones una opción

                if sec_option == "1":
                    print("Operación 1: Regenerar cadena de DNA")
                    regen_longitud = ask_for_int("Indica la longitud de la cadena que será regenerada: ") # Llama a la función que se asegura de que sea integer mayor que 0
                    current_obj.set_chain(regen_longitud) # Uso el setter del objeto para regenerar la cadena
                    current_chain = current_obj.get_chain() # Pongo la cadena en su variable para que se vea en el menú
                    unsaved_changes = True # Hay cambios sin guardar
                    print("Cadena regenerada: {}".format(current_chain)) # Mensajito de confirmación
                
                elif sec_option == "2":
                    """
                    La forma más rápida que se me ocurrió para comprobar que esta opción funciona
                    cuando la cadena NO es válida es:
                    1. Sustituir un nucleótido de la tupla 'nucleotides' de la clase DNA por otra letra
                       p. ej. que se quede así ('A', 'C', 'G', 'Z')
                    2. Creo una cadena relativamente larga para que tenga la letra Z y la guardo en disco
                    3. Cierro programa y vuelvo a poner la tupla bien -> ('A', 'C', 'G', 'T')
                    4. Abro programa, cargo la cadena inválida y la intento validar
                    """
                    print("Operación 2: Validar cadena de DNA")
                    print("Comprobando que cada nucleótido sea uno de los siguientes: {}".format(current_obj.nucleotides)) # Mensajito para que parezca que el programa piensa
                    if current_obj.is_chain_valid(): # El método is_chain_valid retorna True cuando es válida
                        print("La cadena {} es válida".format(current_chain))
                    else: # Y False cuando no lo es
                        print("Parece que la cadena {} no es válida".format(current_chain))

                elif sec_option == "3":
                    print("Operación 3: Mutar cadena de DNA")
                    print("Ten en cuenta que, si introduces un número de mutaciones mayor que la longitud de la cadena, el programa permitirá que se repitan las posiciones de las mutaciones")
                    print("Longitud de tu cadena actual: {}".format(len(current_chain))) # Para que se vea lo que mide
                    mut_number = ask_for_int("Indica el número de mutaciones: ") # Llama a la función que se asegura de que sea integer mayor que 0
                    print("Cadena inicial: {}".format(current_chain)) # Imprimo la cadena antes de mutar
                    current_obj.mutate(mut_number) # Uso el método para mutarla
                    current_chain = current_obj.get_chain() # Actualizo la variable current_chain
                    unsaved_changes = True # ¡Tenemos cambios sin guardar!
                    print("Cadena mutada:  {}".format(current_chain)) # Imprimo la cadena mutada

                elif sec_option == "4":
                    print("Operación 4: Medir frecuencia de nucleótidos")
                    print("Frecuencia de nucleótidos: {}".format(current_obj.freq_count())) # Simplemente llama al método para medir frecuencias

                elif sec_option == "5":
                    print("Operación 5: Contar patrones en la cadena de DNA")
                    dna_pattern = ask_for_pattern() # La función para obtener un patrón válido por parte del usuario
                    if current_obj.pattern_count(dna_pattern) == 1: # Esto es simplemente para que cuando sea 1 ponga "vez" en lugar de "veces"
                        print("El patrón {} aparece {} vez en la cadena {}".format(dna_pattern, current_obj.pattern_count(dna_pattern), current_chain)) # Llamo al método directamente en el print
                    else:
                        print("El patrón {} aparece {} veces en la cadena {}".format(dna_pattern, current_obj.pattern_count(dna_pattern), current_chain)) # Y aquí igual pero con "veces" en el print

                elif sec_option != "6":
                    print("La opción \'{}\' no es válida".format(sec_option)) # Por si pones una opción no válida 

    elif option == "7": # La opción para salir del programa
        if unsaved_changes == False: # Personalizo el mensaje dependiendo de si hay cambios sin guardar o no
            are_you_sure = ask_if_sure("¿Estás segurx de que quieres salir? (S/N): ", "Por favor, responde con Sí (S) o No (N): ") # Se lo asigno a are_you_sure, cuyo valor compruebo en el while principal del programa
        else:
            are_you_sure = ask_if_sure("Tienes cambios sin guardar ¿Estás segurx de que quieres salir? (S/N): ", "Por favor, responde con Sí (S) o No (N): ") # Lo mismo pero te dice que hay cambios sin guardar
    
    else:
        print("La opción \'{}\' no es válida".format(option)) # Por si pones una opción no válida en el menú principal


print("Saliendo del programa...")
print("Programa cerrado con éxito") # Mensajitos para que parezca que el programa hace cosas antes de cerrar

###--------------------###