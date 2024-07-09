import os    #Limpiar pantalla y crear archivo
import time  #Esperar un lapso de tiempo
import sys   #Abandonar el programa
from graphviz import Digraph #Graficar el AFD
from reportlab.lib.pagesizes import A4 #Gnerar las paginas
from reportlab.pdfgen import canvas #Generar el pdf

#--------------------------------------------------------
    #Variables globales

alfabeto=""
NroEstados=""
Matriz=[]
Estados=[]
lista2=[]
nombreGramatica=""
EstadoInicio=""
EstadosAceptacion=""
nombreAFD=""
NombreGuardarAFD=""
NombreGuardarGramatica=""
NTInicio=""
terminales=""
NroNT=""
NT=""
nombrePDF=""
Alfabeto=""
Aceptacion=""
NomNT=""
AlfabetoGR=""
PalabraEvaluar=""
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
            "1. Crear AFD\n"
            "2. Crear Gramática\n"
            "3. Evaluar Cadenas\n"
            "4. Cargar archivo de entrada\n"
            "5. Guardar un archivo\n"
            "6. Reportes\n"
            "7. Salir\n")
    entrada=input("Ingrese una opción: ")
    opcion(entrada)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++       
def opcion(entrada):
        if (entrada=="1"):
            os.system('cls')
            print("--------------------Menú de AFD--------------------")
            print(" ")
            global nombreAFD
            nombreAFD=input("Ingrese el nombre del AFD: ")
            MenuAFD()

        elif (entrada=="2"):
            os.system('cls')
            print("--------------------Menú de Gramática--------------------")
            global nombreGramatica
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
            print("--------------------Menú de Guardar--------------------")
            MenuGuardar()

        elif (entrada=="6"):
            os.system('cls')
            print("--------------------Menú de Reportes--------------------")
            MenuReportes()

        elif(entrada=="7"):
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
def MenuAFD():
    print("--------------------------------------------------")
    print(  "1. Ingresar Estados\n"
            "2. Ingresar Alfabeto\n"
            "3. Estado Inicial\n"
            "4. Estados de aceptación\n"
            "5. Transiciones\n"
            "6. Graficar AFD\n"
            "7. Ayuda\n"
            "8. Menú Principal")
    entradaAFD=input("Ingrese una opción: ")
    EntradaAFD(entradaAFD)
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def MenuGramatica():
    print(" ")
    print("--------------------------------------------------\n"
            "1. Ingresar NT\n"
            "2. Ingresar Terminales\n"
            "3. NT Inicial\n"
            "4. Producciones\n"
            "5. Mostrar Gramática Transformada\n"
            "6. Ayuda\n"
            "7. Menú Principal")
    entradaGramatica=input("Ingrese una opción: ")
    EntradaGramatica(entradaGramatica)
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def MenuEvaluarCadenas():
    global nombreAFD
    global nombreGramatica
    nombreEvaluarCadenas=input("Ingrese el nombre de la Gramática o el AFD: ")
    if nombreEvaluarCadenas==nombreAFD:
            print("--------------------------------------------------\n"
            "1. Solo validar\n"
            "2. Ruta en AFD\n"
            "3. Expandir con Gramática\n"
            "4. Ayuda\n"
            "5. Menú Principal")
            entradaEvaluarCadenas=input("Ingrese una opción: ")
            EntradaEvaluarCadenas(entradaEvaluarCadenas)
    elif nombreEvaluarCadenas==nombreGramatica:
            print("--------------------------------------------------\n"
            "1. Solo validar\n"
            "2. Ruta en AFD\n"
            "3. Expandir con Gramática\n"
            "4. Ayuda\n"
            "5. Menú Principal")
            entradaEvaluarCadenas=input("Ingrese una opción: ")
            EntradaEvaluarCadenas(entradaEvaluarCadenas)
    else:
        print("El nombre del AFD o gramática no es correcto...")
        print("Ingrese un nombre válido: ")
        print("")
        MenuEvaluarCadenas()
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def MenuCargarArchivos():
    print(" ")
    print("--------------------------------------------------\n"
            "1. AFD\n"
            "2. Gramática\n"
            "3. Menú Principal")
    entradaCargarArchivos=input("Ingrese una opción: ")
    EntradaCargarArchivos(entradaCargarArchivos)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def MenuGuardar():
    global nombreAFD
    global nombreGramatica
    global NombreGuardar
    global NombreGuardarAFD
    global NombreGuardarGramatica
    
    print(" ")
    NombreAFDGramatica=input("Ingrese el nombre del AFD o Gramática a guardar: ")
    if NombreAFDGramatica==nombreAFD:
        NombreGuardarAFD=input("Ingrese el nombre con el que guardara el archivo AFD: ")
        Guardar_AFD()
    elif NombreAFDGramatica==nombreGramatica:
        NombreGuardarGramatica=input("Ingrese el nombre con el que guardara el archivo AFD: ")
        Guardar_Gramatica()
    else:
        print("El nombre del AFD o gramática no es correcto...")
        print("Ingrese un nombre válido: ")
        print("")
        MenuGuardar()
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def MenuReportes():
    global nombreAFD
    global nombreGramatica
    global nombrePDF
    print(" ")
    nombreGramaticaAFD=input("Ingrese el nombre de la Gramática o el AFD: ")
    if nombreGramaticaAFD==nombreAFD:
            print("--------------------------------------------------\n"
            "1. Ver detalle\n"
            "2. Generar reporte\n"
            "3. Ayuda\n"
            "4. Menú Principal")
            entradaReportes=input("Ingrese una opción: ")
            EntradaReportes(entradaReportes)
    elif nombreGramaticaAFD==nombreGramatica:
            print("--------------------------------------------------\n"
            "1. Ver detalle\n"
            "2. Generar reporte\n"
            "3. Ayuda\n"
            "4. Menú Principal")
            entradaReportes=input("Ingrese una opción: ")
            EntradaReportes2(entradaReportes)
    else:
        print("El nombre del AFD o gramática no es correcto...")
        print("Ingrese un nombre válido: ")
        print("")
        MenuReportes()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    
def EntradaAFD(entradaAFD):
        if (entradaAFD=="1"):
            os.system('cls')
            print("Ingresar Estados...")
            EstadosAFD()

        elif (entradaAFD=="2"):
            os.system('cls')
            print("Ingresar Alfabeto...")
            AlfabetoAFD()

        elif (entradaAFD=="3"):
            os.system('cls')
            print("Estado Inicial...")
            EstadoInicial()

        elif (entradaAFD=="4"):
            os.system('cls')
            print("Estados de aceptación...")
            EstadosAceptacion()

        elif (entradaAFD=="5"):
            os.system('cls')
            print("Transiciones...")
            print("1. Modo 1")
            print("2. Modo 2")
            Modo=input("Ingrese el modo para ingresar las transiciones: ")
            if (Modo=="1"):
                print("Ingresando al modo 1...")
                time.sleep(1)
                TransicionModo1()
            elif (Modo=="2"):
                print("Ingresando al modo 2...")
                time.sleep(1)
                TransicionModo2()
            else:
                print("El carácter no es aceptado...")
                time.sleep(1)
                os.system('cls')
                MenuAFD()

        elif(entradaAFD=="6"):
            os.system('cls')
            print("Graficando el AFD...")
            time.sleep(2)
            Graficar_AFD()
                
            
        elif(entradaAFD=="7"):
            os.system('cls')
            print("Ayuda...")
            time.sleep(2)
            FuncionAyuda()
            
        elif(entradaAFD=="8"):
            os.system('cls')
            print("Retornando al menú principal...")
            time.sleep(2)
            MenuPrincipal()
            
        else:
            print("El carácter no es aceptado...")
            validoAFD=input("Debe de ingresar un carácter válido: ")
            EntradaAFD(validoAFD)
#-------------------------------------------------------------------------
def EntradaGramatica(entradaGramatica):
        if (entradaGramatica=="1"):
            os.system('cls')
            print("Ingresar los No Terminales...")
            EstadosGramatica()

        elif (entradaGramatica=="2"):
            os.system('cls')
            print("Ingresar Terminales...")
            AlfabetoGramatica()

        elif (entradaGramatica=="3"):
            os.system('cls')
            print("Ingresar No Terminal Inicial...")
            EstadoInicialGramatica()

        elif (entradaGramatica=="4"):
            os.system('cls')
            print("Ingresar Producciones...")

        elif (entradaGramatica=="5"):
            os.system('cls')
            print("Mostrando la gramática transformada...")
            
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
            print("Ingresar cadena para validar...")
            Valuar_Cadena()

        elif (entradaEvaluarCadenas=="2"):
            os.system('cls')
            print("Ingresar una cadena a ver su ruta...")
            Ruta_AFD()

        elif (entradaEvaluarCadenas=="3"):
            os.system('cls')
            print("Ingresar una cadena para expandir...")

        elif(entradaEvaluarCadenas=="4"):
            os.system('cls')
            print("Ayuda...")
            time.sleep(2)
            FuncionAyuda()

        elif(entradaEvaluarCadenas=="5"):
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
            os.system('cls')
            print("Ingresar nombre de archivo con extensión; .afd ")

        elif(entradaCargarArchivos=="2"):
            os.system('cls')
            print("Ingresar nombre de archivo con extensión; .grm ")

        elif(entradaCargarArchivos=="3"):
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
            Ver_DetalleAFD()

        elif (entradaReportes=="2"):
            os.system('cls')
            print("Generando reportes...")
            Generar_PDF()

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
def EntradaReportes2(entradaReportes):
        if (entradaReportes=="1"):
            os.system('cls')
            print("")
            print("Mostrando detalle...")
            Ver_DetalleGramatica()

        elif (entradaReportes=="2"):
            os.system('cls')
            print("Generando reportes...")
            Generar_PDF()

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
def FuncionAyuda():
    print ("Lenguajes Formales y de Programacion")
    print ("Sección B+")
    print ("José Véliz")
    print ("6")
    time.sleep(2)
    os.system('cls')
    MenuPrincipal()


#Funciones del AFD
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def EstadosAFD():
    global NroEstados #Se llama a la variable global
    global NomEstados
    NomEstados=input("Ingrese los Estados: ")
    NomEstados=NomEstados.replace("[","").replace(" ", "").replace("]","")
    EstadosNro=NomEstados.split(",") #Los estados se separan para poderlos contar
    NroEstados=len(EstadosNro) #Se cuentan la cantidad de estados

    global Estados #Se llama a la variable global
    Estados=EstadosNro #Los estados se ingresan en un arreglo
    print("Los estados que se ingresaron fueron: ",Estados)
    
    time.sleep(1)
    MenuAFD()
#---------------------------------------------
def AlfabetoAFD():
    global alfabeto #Se llama a la variable global
    global Alfabeto
    Alfabeto=input("Ingrese el alfabeto: ")
    Alfabeto=Alfabeto.replace("[", "").replace(" ", "").replace("]", "")
    alfabeto=Alfabeto.split(",") #Se separan los caracteres del alfabeto para poderlos contar

    print("El alfabeto ingresado fue: ",alfabeto)
    Matriz_Vacia() #Se envian los datos a la matriz vacia
    time.sleep(1)
    MenuAFD()
#---------------------------------------------
def EstadoInicial():
    global EstadoInicio
    
    EstadoInicial=str(input("Ingrese el Estado inicial: "))
    EstadoInicio=EstadoInicial.replace("[","").replace(" ","").replace("]","")
    time.sleep(1)
    MenuAFD()
#---------------------------------------------
def EstadosAceptacion():
    global EstadosAceptacion
    global Aceptacion
    
    Aceptacion=input("Ingrese los Estados de aceptación: ")
    Aceptacion=Aceptacion.replace("[","").replace(" ","").replace("]","")
    EstadosAceptacion=Aceptacion.split(",") #Los estados se separan para poderlos contar
    time.sleep(1)
    MenuAFD()
#---------------------------------------------
    
#------------Se crea una matriz vacía ----------------
def Matriz_Vacia():
    global alfabeto #Se llama a la variable global
    global NroEstados #Se llama a la variable global
    for i in range(NroEstados):
        Matriz.append([])
        for j in range(len(alfabeto)):
            Matriz[i].append(None)
#-----------------------------------------------
def TransicionModo1():
    print("---------------------------------------")
    print("Transición de los Estados: ")
    time.sleep(1)

    global alfabeto #Se llama a la variable global
    global NroEstados #Se llama a la variable global
    global Estados #Se llama a la variable global
    global Matriz #Se llama a la variable global

    for i in range(NroEstados):
        for j in range(len(alfabeto)):
            print("Ingrese la transición que va de; ", Estados [i],"--->",alfabeto[j],"; ")
            simbolos=input("Transición: ")
            simbolos=simbolos.replace("[", "").replace(" ", "").replace(";", ",").replace("]", "")
            destino1=simbolos.split(",") #Se separan por vectores
            Elemento=destino1[-2] #Se obtiene el penultimo elemento de la lista
            cadena="".join(Elemento) #Se convierte en tipo str para poderlo ingresar en la matriz
            Matriz[i][j]=cadena
    time.sleep(1)
    MenuAFD()

#-----------------------------------------------
def TransicionModo2():
    print("---------------------------------------")
    print("Transición de los Estados: ")
    time.sleep(1)
    
    global alfabeto #Se llama a la variable global
    global NroEstados #Se llama a la variable global
    global Estados #Se llama a la variable global
    global Matriz #Se llama a la variable global
    
    simbolos=input("Ingrese los simbolos destino: ")
    simbolos=simbolos.replace("[", "").replace(" ","").replace("]", "")
    destino1=simbolos.split(";") #Se separan por vectores

    cadena=" ".join(destino1) #Se unen los simbolos en una cadena
    cadena=cadena.replace(" ",",") #Para separarlos por comas
    destino2=cadena.split(",") #La cadena se convierte en una lista

    global lista2 #Se crea una lista, filas = cantidad de alfabeto
    for i in range(0,len(destino2),len(alfabeto)):
        lista2.append(destino2[i:i+len(alfabeto)])

    print("---------------------------------------")
    print("Se muestra la transición de los Estados... ")
    time.sleep(1)

    for i in range(NroEstados):
        for j in range(len(alfabeto)):
            print(Estados[i], "---->", alfabeto[j])
            
    #----Se ingresan los elementos de los simbolos destino en la matriz----
    for f in range(NroEstados):
        for c in range(len(alfabeto)):
            Matriz[f][c]=lista2[f][c]
    time.sleep(1)
    MenuAFD()
#-----------------------------------------------
def FuncionTransicion(matriz, lista, sx, alfa, k):
    global alfabeto
    alfa=alfabeto
    s=list(sx)
    n=alfa.index(lista[k]) #Encuentra un elemento en la lista y devuelve su posicion
    sx=matriz[len(s[0])][n]
    print(" ",sx)
    return sx
#-----------------------------------------------
def Extendida(matriz, lista, sx, alfa, k):
    global alfabeto
    global EstadoInicio
    global EstadosAceptacion
    Aceptacion="".join(EstadosAceptacion)
    alfa=alfabeto
    while(k<len(lista)):
        sx=FuncionTransicion(matriz, lista, sx, alfa, k)
        k+=1
    print("")
    for i in range(len(EstadosAceptacion)):
        if sx==EstadosAceptacion[i]:
            print("La cadena ingresada ES VALIDA")
            print("Empieza desde el estado: (",EstadoInicio,","," ".join(lista),")"," culimando en; Estado de aceptación: ", sx)
        else:
            print("La cadena ingresada NO ES VALIDA")
    time.sleep(2)
    print("")
    print("Retornando al Menu de Evaluar Cadenas...")
    time.sleep(3)
    os.system('cls')
    MenuEvaluarCadenas()
#-----------------------------------------------
def Imprimir_Matriz(m, alfa):
    global Estados
    global alfabeto
    alfa=alfabeto
    t="   | "
    for k in range(len(alfabeto)):
        t+=" "+alfabeto[k]+ " "
    print(t)
    t=""
    print("-"*(4+2*len(m)+1))
    for k in range(len(m)):
        t=Estados[k] + " | "
        for j in range(len(m[k])):
            t+=m[k][j]+"  "
        print(t)
        t=""
#-----------------------------------------------
def Valuar_Cadena():
    global EstadoInicio
    global Matriz
    global alfabeto
    global PalabraEvaluar
    PalabraEvaluar=input("Ingrese palabra: ")
    lista=list(PalabraEvaluar)
    print("")
    Extendida(Matriz, lista, EstadoInicio, alfabeto, 0)
    
    
#-----------------------------------------------
def Ruta_AFD():
    global EstadoInicio
    global Matriz
    global alfabeto
    l=input("Ingrese palabra: ")
    lista=list(l)
    print("")
    print("Matriz de transicion: ")
    print("")
    Imprimir_Matriz(Matriz,alfabeto)
    print("")
    Extendida(Matriz, lista, EstadoInicio, alfabeto, 0)
    
#------------------------------------------------------------



#-------------------Graficar el AFD--------------------------

#----------------------------------------------------------------------

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_aristas = []
        self.inicial = False

    def crearArista(self, nodo_final, valor):
        self.lista_aristas.append(Arista(self, nodo_final, valor))


class Arista:
    def __init__(self, inicial, final, valor):
        self.nodo_inicial = inicial
        self.nodo_final = final
        self.valor = valor

class Grafo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nodos = []
        self.nodos_aceptacion = []

    def agregarNodo(self, nodo):
        self.nodos.append(nodo)
    
    def obtenerNodo(self, nombre):
        for n in self.nodos:
            if n.nombre == nombre:
                return n

    def setearNodoAceptacion(self, nombre):
        self.nodos_aceptacion.append(self.obtenerNodo(nombre))

    def esAceptacion(self, nombre):
        for n in self.nodos_aceptacion:
            if n.nombre == nombre:
                return True
        
        return False
    
    def setEstadoInicial(self, nombre):
        self.obtenerNodo(nombre).inicial = True
    
    def getEstadoInicial(self):
        for n in self.nodos:
            if n.inicial:
                return n
        
        return None

    def graficar(self):
        global nombreAFD
        f = Digraph(format='jpg', name=nombreAFD)
        f.attr(rankdir='LR', size='8,5')
        f.attr('node', shape='circle')

        for n in self.nodos:
            
            if not self.esAceptacion(n.nombre):
                f.node(n.nombre)


        f.attr('node', shape='doublecircle')


        for n in self.nodos_aceptacion:
            f.node(n.nombre)

        for n in self.nodos:
            for a in n.lista_aristas:
                f.edge(n.nombre, a.nodo_final.nombre, label=a.valor)

        
        # ------------------ estado de aceptacion ------------------
        f.attr('node', shape='none')
        f.attr('edge', arrowhead='empty', arrowsize='1.5')
        
        f.edge('', self.getEstadoInicial().nombre, None)

        f.render()
        # ----------------------------------------------------------

#------------------------------------------------------------------------
def Graficar_AFD():
    global Estados
    global EstadosAceptacion
    global Matriz
    global EstadoInicio
    nt= Estados
    ac="".join(EstadosAceptacion)
    grafo_prueba = Grafo('g1')
    
    for x in nt:
        grafo_prueba.agregarNodo(Nodo(x))
        
    for i in range(NroEstados): #Destino y estados del grafo
        for j in range(len(alfabeto)):
            grafo_prueba.obtenerNodo(Estados[i]).crearArista(grafo_prueba.obtenerNodo(Matriz[i][j]), alfabeto[j])
            
    grafo_prueba.setEstadoInicial(EstadoInicio) #Estado inicial
    for i in range(len(ac)): #Estados de aceptacion
        ac ="".join(EstadosAceptacion[i])
        grafo_prueba.setearNodoAceptacion(ac)
        
    grafo_prueba.graficar() #Se grafica el grafo
    MenuAFD()
#------------------------------------------------------------


    
#------------------------------------------------------------
def Ver_DetalleAFD():
    global Estados
    global EstadosAceptacion
    global EstadoInicio
    global alfabeto
    global nombreAFD
    global NroEstados
    print("Detalles del AFD: ",nombreAFD)
    print("Estados: ",Estados)
    print("Estados de Aceptación: ",EstadosAceptacion)
    print("Estado Inicial: ",EstadoInicio)
    print("Alfabeto: ",alfabeto)
    print("Transiciones: ")
    for i in range(NroEstados):
        for j in range(len(alfabeto)):
            print(Estados[i], "---->", alfabeto[j])
    print ("-----------------------------------------")
    input("Enter para retornar al menú de Reportes...")
    print (" ")
    os.system('cls')
    MenuReportes()
#------------------------------------------------------------
def Guardar_AFD():
    global NombreGuardarAFD
    global Estados
    global Matriz
    global alfabeto
    global NroEstados
    Archivo = NombreGuardarAFD + ".afd"
    file = open(Archivo, "w")
    for i in range(NroEstados):
        for j in range(len(alfabeto)):
            file.write(Estados[i]+"," + Matriz[i][j] +"," + alfabeto[j] + ";false,false"+ os.linesep)
    file.close()
    input("Enter para retornar al menú de principal...")
    print (" ")
    os.system('cls')
    MenuPrincipal()
#------------------------------------------------------------------------   


#Funciones de la Gramática
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def EstadosGramatica():
    global NroNT #Se llama a la variable global
    NomNT=input("Ingrese los No Terminales: ")
    NomNT=NomNT.replace("[","").replace(" ", "").replace("]","")
    EstadosNro=NomNT.split(",") #Los estados se separan para poderlos contar
    NroNT=len(EstadosNro) #Se cuentan la cantidad de estados

    global NT #Se llama a la variable global
    NT=EstadosNro #Los NT se ingresan en un arreglo
    print("Los No Terminales que se ingresaron fueron: ",NT)
    
    time.sleep(1)
    MenuGramatica()
#---------------------------------------------
def AlfabetoGramatica():
    global terminales #Se llama a la variable global
    global AlfabetoGR
    AlfabetoGR=input("Ingrese los Terminales: ")
    AlfabetoGR=AlfabetoGR.replace("[", "").replace(" ", "").replace("]", "")
    terminales=AlfabetoGR.split(",") #Se separan los caracteres del alfabeto para poderlos contar

    print("Los terminales ingresados fueron: ",terminales)
    time.sleep(1)
    MenuGramatica()
#---------------------------------------------
def EstadoInicialGramatica():
    global NTInicio
    
    NTInicial=str(input("Ingrese el No Terminal Inicial: "))
    NTInicio=NTInicial.replace("[","").replace(" ","").replace("]","")
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
def Guardar_Gramatica():
    global NombreGuardarGramatica
    global NT #Estados
    global terminales #alfabeto
    global NroNT
    global NTInicio
    Archivo = NombreGuardarGramatica + ".grm"
    file = open(Archivo, "w")
    for i in range(NroNT):
        for j in range(len(terminales)):
            file.write("No Terminales: "+ NT[i] +"  Terminales: " + terminales[j]+ os.linesep)
    file.write("No Terminal Inicio: "+ NTInicio)
    file.close()
    input("Enter para retornar al menú de principal...")
    print (" ")
    os.system('cls')
    MenuPrincipal()

#------------------------------------------------------------
def Generar_PDF():
    global nombrePDF
    nombrePDF=input("Ingrese el nombre del PDF a guardar...")
    Archivo= nombrePDF + ".pdf"
    #AFD----------------
    global Aceptacion
    global EstadoInicio
    global Alfabeto
    global nombreAFD
    global NroEstados
    global NomEstados
    global nombreAFD
    global PalabraEvaluar
    nombreNuevo= nombreAFD + ".jpg"
    #Gramatica---------
    global NomNT
    global AlfabetoGR
    global NTInicio

    #PDF---------
    w, h = A4
    c = canvas.Canvas(Archivo, pagesize=A4)
    c.drawString(50, h - 50, "-------- AFD ------- ")
    c.drawString(50, h - 65, "- Estados: " + NomEstados)
    c.drawString(50, h - 80, "- Alfabeto: " + Alfabeto)
    c.drawString(50, h - 95, "- Estado inicial: " + EstadoInicio)
    c.drawString(50, h - 110, "- Estados de aceptacion: " + Aceptacion)
    c.drawString(50, h - 125, "- Cadena evaluada: " + PalabraEvaluar)

    
    c.drawString(50, h - 230, "- Grafo: " + nombreAFD)
    c.drawImage(nombreNuevo, 200, h - 300, width=170, height=120)
    
    c.drawString(50, h - 365, "-------- Gramatica ------- ")
    c.drawString(50, h - 380, "- No Terminales: " + NomNT)
    c.drawString(50, h - 395, "- Terminales: " + AlfabetoGR)
    c.drawString(50, h - 410, "- Inicio: " + NTInicio)
    c.showPage()
    c.save()
    print ("-----------------------------------------")
    input("Presione enter para regresar al menú principal...")
    print (" ")
    os.system('cls')
    MenuPrincipal()
#------------------------------------------------------------------------
    
    
main()
