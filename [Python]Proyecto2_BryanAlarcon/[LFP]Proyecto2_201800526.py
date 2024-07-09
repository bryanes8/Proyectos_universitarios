import os    #Limpiar pantalla y crear archivo
import time  #Esperar un lapso de tiempo
import sys   #Abandonar el programa
from graphviz import Digraph #Graficar el AFD
from reportlab.lib.pagesizes import A4 #Generar las paginas
from reportlab.pdfgen import canvas #Generar el pdf

#--------------------------------------------------------
    #Variables globales


nombreGramatica=""
NombreGuardarGramatica=""
nombrePDF=""
PalabraEvaluar=""


ListaProducciones=[]
ListaTerminales=[]
ListaNoTerminales=[]
ListaNoTerminalInicial=[]
NombreArchivo=""
lectura=[]
NuevasProducciones=[]
ListaNuevasProducciones=[]
Final=["#"]
ListaDiferencias = []
NombreGrafo = ""
CadenaValidar = ""
#--------------------------------------------------------



def main(): 
#--------------------------------------------------------
    print ("Lenguajes Formales y de Programacion")
    print ("Sección B+")
    print ("Bryan Estiveen Alarcón Aldana - 201800526")
    print ("-----------------------------------------")
    input("Enter para continuar...")
    print (" ")
    os.system('cls')
    MenuPrincipal()

def MenuPrincipal():
    print("----------------------MENU PRICIPAL----------------------\n"
            "1. Generar Autómata de Pila\n"
            "2. Crear Gramática\n"
            "3. Evaluar Cadenas\n"
            "4. Cargar archivo de entrada\n"
            "5. Reportes\n"
            "6. Salir\n")
    entrada=input("Ingrese una opción: ")
    opcion(entrada)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++       
def opcion(entrada):
    global nombreGramatica
    if (entrada=="1"):
        os.system('cls')
        print("--------------------Menú de Autómata de Pila--------------------")
        print(" ")
        nombreEvaluarCadenas=input("Ingrese el nombre de la Gramática: ")
        if nombreEvaluarCadenas==nombreGramatica:
            print("Se ha convertido la gramática...")
            print("")
            GraficarAutomata()
            print("")
            input("Enter para retornar al menú de principal...") #Menú principal
            print (" ")
            os.system('cls')
            MenuPrincipal()
        else:
            print("El nombre ingresado no es válido")
            MenuAFD()

    elif (entrada=="2"):
        os.system('cls')
        print("--------------------Menú de Gramática--------------------")
        nombreGramatica=input("Ingrese el nombre de la Gramática: ")
        MenuGramatica()

    elif (entrada=="3"):
        os.system('cls')
        print("--------------------Menú de Evaluar cadenas--------------------")
        MenuEvaluarCadenas()

    elif (entrada=="4"):
        os.system('cls')
        print("--------------------Menú de Cargar archivos--------------------")
        MenuCargarArchivos()


    elif (entrada=="5"):
        os.system('cls')
        print("--------------------Menú de Reportes--------------------")
        MenuReportes()

    elif(entrada=="6"):
        os.system('cls')
        print("Abandondando el programa...")
        time.sleep(2)
        os.system('cls')
        sys.exit()
    else:
        print("El carácter no es aceptado...")
        valido=input("Debe de ingresar un carácter válido: ")
        opcion(valido)

    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def MenuGramatica():
    print(" ")
    print("--------------------------------------------------\n"
            "1. Ingresar Terminales\n"
            "2. Ingresar No Terminales\n"
            "3. Ingresar Producciones\n"
            "4. Eliminar Producciones\n"
            "5. No Terminal Inicial\n"
            "6. Ayuda\n"
            "7. Menú Principal")
    entradaGramatica=input("Ingrese una opción: ")
    EntradaGramatica(entradaGramatica)
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def MenuEvaluarCadenas():
    global nombreGramatica
    nombreEvaluarCadenas=input("Ingrese el nombre de la Gramática: ")
    if nombreEvaluarCadenas==nombreGramatica:
            print("--------------------------------------------------\n"
            "1. Solo validar\n"
            "2. Ayuda\n"
            "3. Menú Principal")
            entradaEvaluarCadenas=input("Ingrese una opción: ")
            EntradaEvaluarCadenas(entradaEvaluarCadenas)
    else:
        print("El nombre de la gramática no es correcto...")
        print("Ingrese un nombre válido: ")
        print("")
        MenuEvaluarCadenas()
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def MenuCargarArchivos():   
    print("1. Gramática\n"
          "2. Menú Principal")
    entradaCargarArchivos=input("Ingrese una opción: ")
    EntradaCargarArchivos(entradaCargarArchivos)
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def MenuReportes():
    global nombreGramatica
    global nombrePDF
    print(" ")
    nombreGramaticaAFD=input("Ingrese el nombre de la Gramática: ")
    if nombreGramaticaAFD==nombreGramatica:
            print("--------------------------------------------------\n"
            "1. Ver detalle\n"
            "2. Generar reporte\n"
            "3. Ayuda\n"
            "4. Menú Principal")
            entradaReportes=input("Ingrese una opción: ")
            EntradaReportes(entradaReportes)
    else:
        print("El nombre del Gramática no es correcto...")
        print("Ingrese un nombre válido: ")
        print("")
        MenuReportes()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    

#-------------------------------------------------------------------------
def EntradaGramatica(entradaGramatica):
        if (entradaGramatica=="1"):
            os.system('cls')
            print("Ingresar los Terminales... ")
            TerminalesGramatica()

        elif (entradaGramatica=="2"):
            os.system('cls')
            print("Ingresar los No Terminales... ")
            NoTerminalesGramatica()

        elif (entradaGramatica=="3"):
            os.system('cls')
            print("Ingresar Producciones... ")
            ProduccionesGramatica()

        elif (entradaGramatica=="4"):
            os.system('cls')
            print("Borrar Producciones... ")
            EliminarProduccionesGramatica()

        elif (entradaGramatica=="5"):
            os.system('cls')
            print("No Terminal Inicial... ")
            NoTerminalInicialGramatica()
            
        elif(entradaGramatica=="6"):
            os.system('cls')
            print("Ayuda...")
            time.sleep(2)
            FuncionAyuda()
            
        elif(entradaGramatica=="7"):
            os.system('cls')
            print("Retornando al menú principal...")
            time.sleep(2)
            MenuPrincipal()

        else:
            print("El carácter no es aceptado...")
            validoGramatica=input("Debe de ingresar un carácter válido: ")
            EntradaGramatica(validoGramatica)
            
#-------------------------------------------------------------------------
def EntradaEvaluarCadenas(entradaEvaluarCadenas):
        if (entradaEvaluarCadenas=="1"):
            os.system('cls')
            cadena = input("Ingresar cadena para validar: ")
            ValidarCadena(cadena)

        elif(entradaEvaluarCadenas=="2"):
            os.system('cls')
            print("Ayuda...")
            time.sleep(2)
            FuncionAyuda()

        elif(entradaEvaluarCadenas=="3"):
            os.system('cls')
            print("Retornando al menú principal...")
            time.sleep(2)
            MenuPrincipal()

        else:
            print("El carácter no es aceptado...")
            validoEvaluarCadenas=input("Debe de ingresar un carácter válido: ")
            EntradaEvaluarCadenas(validoEvaluarCadenas)
            
#-------------------------------------------------------------------------
def EntradaCargarArchivos(entradaCargarArchivos):
        if (entradaCargarArchivos=="1"):
            global nombreGramatica #Se llama la variable global
            global lectura #Se llama la variable global
            global ListaProducciones #Se llama a la variable global
            os.system('cls')
            try:
                nombreGramatica = input("Por favor ingrese su archivo de entrada: ")
                archivo = open(nombreGramatica, 'r')
                lineas = [linea.replace('\n', "").replace(" ", "") for linea in archivo]
                lectura = [item for item in lineas if len(item)>0]
                ListaProducciones = lectura
                archivo.close
                print("El archivo se ha cargado...")
                print(lectura)
                print("")
                gr5 = ingresarGramatica(nombreGramatica, lectura)
            except:
                validoCargarArchivos=input("Debe de ingresar un nombre válido: ")
                nombreGramatica=validoCargarArchivos

        elif(entradaCargarArchivos=="2"):
            os.system('cls')
            print("Retornando al menú principal...")
            time.sleep(2)
            MenuPrincipal()

        else:
            print("El carácter no es aceptado...")
            validoCargarArchivos=input("Debe de ingresar un carácter válido: ")
            EntradaCargarArchivos(validoCargarArchivos)
            
#-------------------------------------------------------------------------
def EntradaReportes(entradaReportes):
        if (entradaReportes=="1"):
            os.system('cls')
            print("")
            print("Mostrando detalle...")
            VerDetalleGramatica()

        elif (entradaReportes=="2"):
            os.system('cls')
            print("Generando reportes...")
            Generar_PDF() #Agregar despues

        elif(entradaReportes=="3"):
            os.system('cls')
            print("Ayuda...")
            time.sleep(2)
            FuncionAyuda()

        elif(entradaReportes=="4"):
            os.system('cls')
            print("Retornando al menú principal...")
            time.sleep(2)
            MenuPrincipal()

        else:
            print("El carácter no es aceptado...")
            validoReportes=input("Debe de ingresar un carácter válido: ")
            EntradaReportes(validoReportes)
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
def FuncionAyuda():
    print ("Lenguajes Formales y de Programacion")
    print ("Sección B+")
    print ("José Véliz")
    print ("6")
    time.sleep(2)
    os.system('cls')
    MenuPrincipal()

#-----------------------------------------------

#Funciones de la Gramática
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def TerminalesGramatica():
    global ListaTerminales #Se llama a la variable global
    while True:
        Terminal = input("Ingrese los Terminales: ")
        ListaTerminales.append(Terminal)
        if Terminal == "":
            ListaTerminales = [item for item in ListaTerminales if len(item)>0]
            break
        print(ListaTerminales)
    
    time.sleep(1)
    MenuGramatica()
#---------------------------------------------
def NoTerminalesGramatica():
    global ListaNoTerminales #Se llama a la variable global
    while True:
        NoTerminal = input("Ingrese No Terminales: ")
        ListaNoTerminales.append(NoTerminal)
        if NoTerminal == "":
            ListaNoTerminales = [item for item in ListaNoTerminales if len(item)>0]
            break
        print(ListaNoTerminales)
    time.sleep(1)
    MenuGramatica()
#---------------------------------------------
def ProduccionesGramatica():
    global ListaProducciones #Se llama a la variable global
    while True:
        Produccion = input("Ingrese Produccion: ")
        ListaProducciones.append(Produccion)
        if Produccion == "":
            ListaProducciones = [item for item in ListaProducciones if len(item)>0]
            break
        print(ListaProducciones)
    time.sleep(1)
    MenuGramatica()
#---------------------------------------------
def EliminarProduccionesGramatica():
    global ListaProducciones #Se llama a la variable global
    EliminarProduccion = input("Ingrese Producción a Eliminar: ")
    try:
        ListaProducciones.index(EliminarProduccion)
        ListaProducciones.remove(EliminarProduccion)
        print("Se ha eliminado la producción...")
    except:
        print("La producción no existe")
    time.sleep(1)
    MenuGramatica()
#---------------------------------------------
def NoTerminalInicialGramatica():
    global ListaNoTerminalInicial #Se llama a la variable global
    NoTerminalInicial = input("Ingrese No Terminal inicial: ")
    try:
        ListaNoTerminales.index(NoTerminalInicial)
        ListaNoTerminalInicial.append(NoTerminalInicial)
        print("Se ha registrado el No Terminal Inicial: ")
        print(ListaNoTerminalInicial)               
    except:
        print("El No Terminal no existe en la lista")
    time.sleep(1)
    MenuGramatica()
#------------------------------------------------------------
def Ver_DetalleGramatica():
    global NroNT
    global NT
    global terminales
    global NTInicio
    print("Detalles de la Gramatica: ",nombreGramatica)
    print("No Terminales: ",NT)
    print("No Terminal Inicial: ",NTInicio)
    print("Terminales: ",terminales)

    print ("-----------------------------------------")
    input("Enter para retornar al menú de Reportes...")
    print (" ")
    os.system('cls')
    MenuReportes()
#------------------------------------------------------------
#++++++++++++REPORTES++++++++++++++++++++++++++++++++++++++++
class Nodo:
    def __init__(self, valor, isNT):
        self.valor = valor
        self.isNT = isNT
class NT:
    def __init__(self, valor):
        self.valor = valor
        self.producciones = []
    def agregarProduccion(self, p):
        self.producciones.append(p)
    def agregarProduccion_idx(self, idx, p):
        self.producciones[idx].append(p)
    def toString(self):
        string_producciones = ''
        for p in self.producciones:
            for el in p.elementos:
                string_producciones += '| ' + el.valor + ' |'
                global PRODUCCIONES #Producciones----------------------------
                global NuevasProducciones 
                PRODUCCIONES=el.valor
                NuevasProducciones.append(PRODUCCIONES) #Hasta Aqui-----------
            string_producciones += '\n'
        global NOTERMINALES #Lista de No Terminales----------
        global ListaNoTerminales
        NOTERMINALES=self.valor 
        ListaNoTerminales.append(NOTERMINALES)  #Hasta aqui--
        global ListaTerminales #Lista de Terminales ------------------------------------------
        list_difference = set(NuevasProducciones).difference(ListaNoTerminales)
        ListaTerminales = list(list_difference)  #Hasta aquí----------------------------------
        return self.valor + ' -> ' + string_producciones

class Produccion:
    def __init__(self):
        self.elementos = []
    def agregarElemento(self, el):
        self.elementos.append(el)
    def getElementoSig(self, idx):
        if len(self.elementos) -1 <= idx:
            return None
        return self.elementos[idx + 1]

class Gramatica:
    def __init__(self, nombre):
        self.nombre = nombre
        self.no_terminales = []
        self.nt_inicial = ''
    def setInicial(self, inicial):
        self.nt_inicial = inicial
        global INICIAL # No terminal inicial------------------
        global ListaNoTerminalInicial
        INICIAL=inicial
        ListaNoTerminalInicial.append(INICIAL) #Aqui termina--
    def agregar_NT(self, noterminal):
        self.no_terminales.append(noterminal)
    def existeNT(self, val):
        for nt in self.no_terminales:
            if nt.valor == val:
                return True
        
        return False

    def getIndex(self, val):
        for i in range(len(self.no_terminales)):
            nt = self.no_terminales[i]
            if nt.valor == val:
                return i
        return -1 

    def getNT(self, val):
        for nt in self.no_terminales:
            if nt.valor == val:
                return nt
        return None 
    
    def evaluar(self, nt_name, cadena, ptr):
        nt = self.getNT(nt_name)
        for produccion in nt.producciones:      
            for i in range(len(produccion.elementos)):
                el = produccion.elementos[i]
                if cadena[ptr] == el.valor:
                    siguiente = produccion.getElementoSig(i)
                    if siguiente != None:
                        if ptr == len(cadena) - 1:
                            if self.contieneEpsilon(siguiente.valor):
                                print("La cadena: " + cadena + " es VALIDA")
                            else:
                                print("La cadena: " + cadena + " es invalida")
                            
                            return
                        return self.evaluar(siguiente.valor, cadena, ptr + 1)
                    else:
                        if ptr == len(cadena) - 1:
                            print("La cadena: " + cadena + " es VALIDA")
                        else:
                            print("La cadena: " + cadena + " es invalida")                       
                        return

        print("La cadena: " + cadena + " es invalida")

    def contieneEpsilon(self, valor):
        for nt in self.no_terminales:          
            if nt.valor == valor:
                for prods in nt.producciones:             
                    for el in prods.elementos:
                        if el.valor == 'epsilon':
                            return True
        return False


def ingresarGramatica(nombre, prods):
    gr = Gramatica(nombre)
    first = True
    for p in prods:
        aux = p.split('>')
        lado_izq = aux[0]
        lado_der = aux[1]
        if first:
            first = False
            gr.setInicial(lado_izq)
        produccion_temp = Produccion()
        if lado_der == 'epsilon':
            nodo_temp = Nodo(lado_der, True)    
            produccion_temp.agregarElemento(nodo_temp)
            if gr.existeNT(lado_izq):
                nt_existente = gr.getNT(lado_izq)
                nt_existente.agregarProduccion(produccion_temp)
            else:
                nt_izq = NT(lado_izq)
                nt_izq.agregarProduccion(produccion_temp)  
                gr.agregar_NT(nt_izq)
            continue

        for c in lado_der:        
            nodo_temp = None
            if ord(c) >= 65 and ord(c) <= 90:
                nodo_temp = Nodo(c, True)
            else:
                nodo_temp = Nodo(c, False)
            produccion_temp.agregarElemento(nodo_temp)
        if gr.existeNT(lado_izq):
            nt_existente = gr.getNT(lado_izq)
            nt_existente.agregarProduccion(produccion_temp)
        else:
            nt_izq = NT(lado_izq)
            nt_izq.agregarProduccion(produccion_temp)          
            gr.agregar_NT(nt_izq)
    text = ''
    for nt in gr.no_terminales:
       text += nt.toString()

    print('Gramática:  ' + gr.nombre + '\n' + text + '-------------------------------------\n')
    input("Enter para retornar al menú de principal...") #Menú principal
    print (" ")
    os.system('cls')
    MenuPrincipal()
    return gr
#---------------------------------------------------------------------
def VerDetalleGramatica():
    global ListaProducciones #Se llama a la variable global
    global ListaTerminales #Se llama a la variable global
    global ListaNoTerminales #Se llama a la variable global
    global ListaTerminalInicial #Se llama a la variable global
    global nombreGramatica #Se llama a la variable global
    global NuevasProducciones #Se llama a la variable global
    global Final #Se llama a la variable global
    print("")
    print("--------------------------------------")
    print("")
    print("Detalles de Autómata de Pila")
    print("Estados:   S: i, P, q, F")
    print("Aldabeto:  Σ:")
    print(ListaTerminales)
    print("Símbolos de la Pila:  Γ:")
    SimbolosPila=ListaTerminales + ListaNoTerminales + Final
    print(SimbolosPila)
    print("Estado inicial:  L: i")
    print("Estados de aceptación:  F: F")
    print("")
    print("--------------------------------------")
    print("Detalles de Gramática: ")
    print("")
    print("Lista de Terminales: ")
    print(ListaTerminales)
    print("Lista de No Terminales: ")
    print(ListaNoTerminales)
    print("Lista de Producciones: ")
    print(ListaProducciones)
    print("No Terminal Inicial: ")
    print(ListaNoTerminalInicial)
    print("")
    GRAMATICA = ingresarGramatica(nombreGramatica, ListaProducciones)
    
#----------------------------------------------------------------------    
def ValidarCadena(cadena):
    global ListaTerminales #Llama a la variable global
    global lectura
    global ListaDiferencias
    global ListaNoTerminales
    
    nuevo = " ".join(lectura)
    nuevos=nuevo.split(">")
    nuevo = " ".join(nuevos)
    nuevos=nuevo.split(" ")
    ListaDiferencias = [item for item in nuevos if item not in ListaNoTerminales]
    ListaCadena=cadena.split()
    validar=set(ListaCadena).difference(set(ListaTerminales))
    Validacion=list(validar)
    if len((Validacion))==0:
        Automata(cadena)
    else:
        print("La cadena ingresada NO ES VALIDA")
        print("")
        NuevaCadena = input("Ingrese una nueva cadena: ")
        ValidarCadena(NuevaCadena)
        
#----------------------------------------------------------------------
def Automata(cadena):
    global ListaDiferencias #Llama a la variable global
    global lectura #Se llama a la variable global
    global ListaTerminales #Se llama a la variable global
    global ListaNoTerminales
    global ListaNoTerminalInicial
    global CadenaValidar
    ND = [item for item in ListaNoTerminales if item not in ListaNoTerminalInicial]
    In = "".join(ListaNoTerminalInicial)
    dot = Digraph(comment='ARBOL')
    dot
    
    #-------------------------------------------------------------
    nuevo = " ".join(lectura)
    NODOS = nuevo.replace(">", ";")
    NODOS = NODOS.split()
    LISTA = [] #Se crea una lista solo para los nodos
    LISTA2 = [] #Se crea una lista solo para los nodos
    for i in range(len(NODOS)):
        LISTA.append("λ," + NODOS[i])
    for i in range(len(ListaTerminales)):
        LISTA2.append(ListaTerminales[i] + "," + ListaTerminales[i] + ";λ")
    LISTANODOS = LISTA + LISTA2 #Se unen las dos listas
    #--------------------------------------------------------------
    
    cadena = cadena.split()
    CadenaValidar = "".join(cadena)
    pila = ["#"]
    print("")
    print("Estado inicial de la pila: λ")
    print("Estado de aceptación de la pila: F")
    print("Cadena ingresada: " + CadenaValidar)
    print("")
    print("--------------------------------------------------------------------------")
    Rango = len(ListaDiferencias)/2
    Rango = int(Rango)
    #-----------------Archivo
    file = open("Transicion.csv", "w")
    file.write("Pila;Entrada;Transición\n")
    #---------------------
    RangoCadenaNueva = len(CadenaValidar)
    RangoCadena = len(CadenaValidar)/2
    RangoCadena = int(RangoCadena)
    try:
        for i in range(0, RangoCadena):
            for j in range(-1, Rango):
                PilA="".join(pila) #Se crea el documento----------
                file.write(PilA + ";" + CadenaValidar + ";" + "---" + "\n")#-----
                pila.append(ListaDiferencias[j+1])
                
        for i in range(RangoCadena, RangoCadenaNueva):
            for j in range(-1, Rango):
                pila.pop()
                PilA="".join(pila)
                file.write(PilA +";"+ CadenaValidar + ";" + "---" + "\n")
        print("")
        if len(pila)==1 and pila[0]=="#":
            print("La cadena ingresada ->" + CadenaValidar + " es VALIDA")
            print("Transiciones: ")
            print("i,λ,λ;p,#")
            for i in range (len(LISTANODOS)):
                print(LISTANODOS[i])
            for i in reversed(LISTANODOS):
                print(i)
            print("q,λ,#;f,λ")
            file.write("---")
            file.write(";")
            file.write("---")
            file.write(";")
            file.write("ACEPTACIÓN")
            file.close()
            dot.node(In, In)
            for i in ND:
                dot.node(i, i)
            for i in ND:
                dot.edges([In+i])
            print(dot.source)
            dot.render('test-output/round-table.gv', view=True)
        elif pila[0]=="#":
            print("La cadena ingresada ->" + CadenaValidar + " es valida")
            print("Transiciones: ")
            print("i,λ,λ;p,#")
            for i in range (len(LISTANODOS)):
                print(LISTANODOS[i])
            for i in reversed(LISTANODOS):
                print(i)
            print("q,λ,#;f,λ")
            file.write("---")
            file.write(";")
            file.write("---")
            file.write(";")
            file.write("ACEPTACIÓN")
            file.close()
            dot.node(In, In)
            for i in ND:
                dot.node(i, i)
            for i in ND:
                dot.edges([In+i])
            print(dot.source)
            dot.render('test-output/round-table.gv', view=True)

        else:
            print("La cadena ingresada NO ES VALIDA")
    except:
        print("La cadena ingresada NO ES VALIDA")
    print("")
    input("Enter para retornar al menú de principal...") #Menú principal
    print (" ")
    os.system('cls')
    MenuPrincipal()

#Pila
#-----------------------------------------------------------------------
class Pila:
    def __init__(self):
        self.pila = []
        self.size = 0
        
    def push(self, valor):
        self.pila.append(valor)
        self.size = self.size + 1
        
    def pop(self):
        valor = self.pila[self.size - 1]
        del self.pila[self.size - 1]
        self.size = self.size - 1
        return valor
    
    def cima(self):
        if self.size == 0:
            print("La pila esta vacia")
        else:
            valor = self.pila[self.size - 1]
            return valor
        return "Debe de ingresar algun valor"
    
    def copy(self):
        temp = []
        for x in self.pila:
            temp.append(x)
        return temp
    
def multiplicar(arr):
    for i in range(len(arr)):
        arr[i] = arr[i]*2

def deshapilar(pila):
    temp = pila
    temp.pop()

    
p1 = Pila()
#------------------------------------------------------------------------
def GraficarAutomata():
    global NombreGrafo
    global lectura #Se llama a la variable global
    global ListaTerminales #Se llama a la variable global

    NombreGrafo = input("Ingrese el nombre para guardar el grafo del automata: ")
    nuevo = " ".join(lectura)
    NODOS = nuevo.replace(">", ";")
    NODOS = NODOS.split()
    LISTA = [] #Se crea una lista solo para los nodos
    LISTA2 = [] #Se crea una lista solo para los nodos
    for i in range(len(NODOS)):
        LISTA.append("λ," + NODOS[i])
    for i in range(len(ListaTerminales)):
        LISTA2.append(ListaTerminales[i] + "," + ListaTerminales[i] + ";λ")
    LISTANODOS = LISTA + LISTA2 #Se unen las dos listas

    f = Digraph(format='jpg', name=NombreGrafo)
    f.attr(rankdir='LR', size='8,5')
    q_node = LISTANODOS
    f.attr('node', shape='circle')
    f.edge('i', 'p', label='λ,λ;#')
    f.edge('p', 'q', label='λ,λ;S')
    trans = ''
    for tran in q_node:
        trans += tran + '\n'
    #se ingresa una transicion invisible para darle altura al label
    f.edge('q', 'q', style='invis')
    f.edge('q', 'q', label=trans)
    f.edge('q', 'f', label='λ,#;λ')
    f.node('f', peripheries='2')
    f.attr('node', shape='none')
    f.attr('edge', arrowhead='empty', arrowsize='1.5')
    f.edge('', 'i', None)
    f.render()
#---------------------------------------------------------------------------
def Generar_PDF():
    global nombrePDF
    nombrePDF=input("Ingrese el nombre del PDF a guardar...")
    Archivo= nombrePDF + ".pdf"
    #Variables---------------------------------------------
    global ListaProducciones #Se llama a la variable global
    global ListaTerminales #Se llama a la variable global
    global ListaNoTerminales #Se llama a la variable global
    global ListaTerminalInicial #Se llama a la variable global
    global nombreGramatica #Se llama a la variable global
    global NuevasProducciones #Se llama a la variable global
    global Final #Se llama a la variable global
    print("")
    print("--------------------------------------")
    #print("Detalles de Autómata de Pila")
    #print("Estados:   S: i, P, q, F")
    #print("Aldabeto:  Σ:")
    Alfabeto=" ".join(ListaTerminales)
    #print("Símbolos de la Pila:  Γ:")
    SimbolosPila=ListaTerminales + ListaNoTerminales + Final
    simbolos = " ".join(SimbolosPila)
    #print("Estado inicial:  L: i")
    #print("Estados de aceptación:  F: F")

    #print("Detalles de Gramática: ")
    #print("Lista de Terminales: ")
    AlfabetoGR = " ".join(ListaTerminales)
    #print("Lista de No Terminales: ")
    NomNT = " ".join(ListaNoTerminales)
    #print("Lista de Producciones: ")
    prod = " ".join(ListaProducciones)
    #print("No Terminal Inicial: ")
    NTInicio = "".join(ListaNoTerminalInicial)
    
    nombreNuevo= NombreGrafo+ ".jpg"

    #PDF---------
    w, h = A4
    c = canvas.Canvas(Archivo, pagesize=A4)
    c.drawString(50, h - 50, "-------- Automata pila ------- ")
    c.drawString(50, h - 65, "- Estados:   S: i, P, q, F: ")
    c.drawString(50, h - 80, "- Aldabeto:  Σ:" + Alfabeto)
    c.drawString(50, h - 95, "- Símbolos de la Pila:  Γ: " + simbolos)
    c.drawString(50, h - 110, "- Estado inicial:  L: i ")
    c.drawString(50, h - 125, "- Estados de aceptación:  F: F")
    c.drawString(50, h - 140, "- Cadena evaluada: " + CadenaValidar)

    
    c.drawString(50, h - 230, "- Grafo: " + NombreGrafo)
    c.drawImage(nombreNuevo, 200, h - 300, width=180, height=140)
    
    c.drawString(50, h - 365, "-------- Gramatica ------- ")
    c.drawString(50, h - 380, "- No Terminales: " + NomNT)
    c.drawString(50, h - 395, "- Terminales: " + AlfabetoGR)
    c.drawString(50, h - 410, "- Inicio: " + NTInicio)
    c.drawString(50, h - 425, "- Producciones: " + prod)
    c.showPage()
    c.save()
    print ("-----------------------------------------")
    input("Presione enter para regresar al menú principal...")
    print (" ")
    os.system('cls')
    MenuPrincipal()
    
#------------------------------------------------------------------------
main()
