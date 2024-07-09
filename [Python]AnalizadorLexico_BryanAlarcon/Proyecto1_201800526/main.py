from tkinter import *               # ventana
from tkinter import Menu            # barra de tareas
from tkinter import filedialog      # filechooser
from tkinter import scrolledtext    # textarea
from tkinter import messagebox      # message box
from AnalisisLexicoCSS import ScannerCSS  # llamando a una funcion externa
from AnalisisLexicoJS import ScannerJS
from AnalisisLexicoHTML import ScannerHTML
from AnalisisSintacticoJS import ParserJS
import os

class GUI:
    # Metodo que contiene la definicion de la interfaz grafica 
    def __init__(self):
        self.window = Tk()
        self.txtEntrada = Entry(self.window,width=10)
        self.txtConsola = Entry(self.window,width=10)
        # Propiedades de la ventana
        self.window.title("Proyecto 1 - 201800526 - ML WEB EDITOR")
        self.window.geometry('925x700')
        self.window.configure(bg = '#48C9B0')
        self.lbl = Label(self.window, text="ML WEB EDITOR", font=("Arial Bold", 15))
        self.lbl.place(x=375, y = 10)

        # propiedades del menu 
        self.menu = Menu(self.window)
        self.file_item = Menu(self.menu)  #Menu File
        self.file_item.add_command(label='Abrir Archivo', command=self.abrirFile)
        self.file_item.add_separator()
        self.file_item.add_command(label='Guardar')

        self.menu.add_cascade(label='Archivo', menu=self.file_item)
        self.window.config(menu=self.menu)
        
        # propiedades del textarea
        self.txtEntrada = scrolledtext.ScrolledText(self.window,width=100,height=25)   # textArea Entrada
        self.txtEntrada.place(x=50, y = 50)
        #ent = txtEntrada.get("1.0","10.10")
        #print("ent: ",ent)


        self.lbl = Label(self.window, text="Consola:")  #label 
        self.lbl.place(x=50, y = 465)
        self.txtConsola = scrolledtext.ScrolledText(self.window,width=100,height=12)   # textArea consola
        self.txtConsola.place(x=50, y = 490)

        selected = IntVar() 
        self.rad1 = Radiobutton(self.window,text='HTML', value=1, variable=selected)
        self.rad2 = Radiobutton(self.window,text='CSS', value=2, variable=selected)
        self.rad3 = Radiobutton(self.window,text='JavaScript', value=3, variable=selected)
        self.rad4 = Radiobutton(self.window,text='SintacticoJS', value=4, variable=selected)
        self.rad1.place(x=130, y = 460)
        self.rad2.place(x=180, y = 460)
        self.rad3.place(x=226, y = 460)
        self.rad4.place(x=305, y = 460)

        def clicked(): #Abre el analizador lexico seleccionado
            if selected.get() == 1:
                self.AnalyzeHTML()
            elif selected.get() == 2:
                self.AnalyzeCSS()
            elif selected.get() == 3:
                self.AnalyzeJS()
            elif selected.get() == 4:
                self.AnalyzeParserJS()
            else:
                messagebox.showinfo('Error', '¡Debe de seleccionar una opción!')
                
           
        self.btn = Button(self.window, text="Analyze", bg="#C9BA41", fg="black", command=clicked)    #btn Analyze
        self.btn.place(x=400, y = 460)
        # Dispara la interfaz A$AP
        self.window.mainloop()
        
    def AnalyzeCSS(self):
        entrada = self.txtEntrada.get("1.0", END) #fila 1 col 0 hasta fila 2 col 10
        miScanner = ScannerCSS()
        retorno = miScanner.analizar(entrada)
        self.txtConsola.delete("1.0", END)
        messagebox.showinfo('Projecto 1', 'Analizado Finalizado')
        for token in miScanner.lista_tokens:
            self.txtConsola.insert(END, "-Token: "+repr(token.getTipo()).rjust(15) + "     -Lexema: "+repr(token.lexema).rjust(20) + "     -Linea: "+repr(token.linea).rjust(2) + "\n")
        self.txtConsola.insert(END, "\n")

        #imprimir la cadena sin errores ---------------- entrada+++++++++++++++++++++++++++++++++++
        file = open("CadenaLimpia-CSS.css", "w")
        for x in miScanner.lista_errores:
            entrada=entrada.replace(x, " ")
        file.write(entrada + os.linesep)
        file.close()
        #Errores
        for error in miScanner.lista_errores:
            self.txtConsola.insert(END, "Error Lexico: " + error + " encontrado. \n")
        
    def AnalyzeJS(self):
        entrada = self.txtEntrada.get("1.0", END) #fila 1 col 0 hasta fila 2 col 10
        miScanner = ScannerJS()
        retorno = miScanner.analizar(entrada)
        self.txtConsola.delete("1.0", END)
        messagebox.showinfo('Projecto 1', 'Analisis Finalizado')
        for token in miScanner.lista_tokens:
            self.txtConsola.insert(END, "-Token: "+repr(token.getTipo()).rjust(15) + "     -Lexema: "+repr(token.lexema).rjust(20) + "     -Linea: "+repr(token.linea).rjust(2) + "\n")
        self.txtConsola.insert(END, "\n")

        #imprimir la cadena sin errores ---------------- entrada+++++++++++++++++++++++++++++++++++
        file = open("CadenaLimpia-JS.js", "w")
        for x in miScanner.lista_errores:
            entrada=entrada.replace(x, " ")
        file.write(entrada + os.linesep)
        file.close()
        #Errores
        for error in miScanner.lista_errores:
            self.txtConsola.insert(END, "Error Lexico: " + error + " encontrado. \n")
        '''Color de las letras, ejemplo
        box.insert(END, "Ehila", 'name')  # <-- tagging `name`
        box.insert(END, "Now", 'time')  # <-- tagging `time`
        box.tag_config('name', foreground='green')  # <-- Change colors of texts tagged `name`
        box.tag_config('time', foreground='red')  # <--  Change colors of texts tagged `time`
        '''
        
    def AnalyzeHTML(self):
        entrada = self.txtEntrada.get("1.0", END) #fila 1 col 0 hasta fila 2 col 10
        miScanner = ScannerHTML()
        retorno = miScanner.analizar(entrada)
        self.txtConsola.delete("1.0", END)
        messagebox.showinfo('Projecto 1', 'Analisis Finalizado')
        for token in miScanner.lista_tokens:
            self.txtConsola.insert(END, "-Token: "+repr(token.getTipo()).rjust(15) + "     -Lexema: "+repr(token.lexema).rjust(20) + "     -Linea: "+repr(token.linea).rjust(2) + "\n")
        self.txtConsola.insert(END, "\n")

        #imprimir la cadena sin errores ---------------- entrada+++++++++++++++++++++++++++++++++++
        file = open("CadenaLimpia-HTML.hml", "w")
        for x in miScanner.lista_errores:
            entrada=entrada.replace(x, " ")
        file.write(entrada + os.linesep)
        file.close()
        #Errores
        for error in miScanner.lista_errores:
            self.txtConsola.insert(END, "Caracter desconocido: " + error + " encontrado. \n")

    def AnalyzeParserJS(self):
        entrada = self.txtEntrada.get("1.0", END) #fila 1 col 0 hasta fila 2 col 10
        miScanner = ScannerJS()
        retorno = miScanner.analizar(entrada)
        contador1 = 0
        contador2 = 0
        self.txtConsola.delete("1.0", END)
        messagebox.showinfo('Projecto 1', 'Analisis Finalizado')
        for token in miScanner.lista_tokens:
            self.txtConsola.insert(END, "-Token: "+repr(token.getTipo()).rjust(15) + "     -Lexema: "+repr(token.lexema).rjust(20) + "     -Linea: "+repr(token.linea).rjust(2) + "\n")
            if(token.lexema=="("):
                contador1+=1
            if(token.lexema==")"):
                contador2+=1
        if(contador1 == contador2):
            tokensP = miScanner.lista_tokens
            miParser = ParserJS(tokensP)
            retorno = miParser.begin() #Analisis sintactico
        else:
            print("Existen errores sintacticos, se esperaba '(|)'")
        #Errores
        for error in miScanner.lista_errores:
            self.txtConsola.insert(END, "Error Lexico: " + error + " encontrado. \n")

            
        #Reporte en HTML----------------------------------------------------------------
        file = open("ReporteSintacticoJS.html", "w")
        file.write("<!DOCTYPE html>\n")
        file.write("<html>\n")
        file.write('<body bgcolor="#D7FB5A">')
        file.write("<head>\n")
        file.write("<title>Reporte de Analisis Sintactico</title>\n")
        file.write("</head>\n")
        file.write("<center><h1>Reporte de Analisis Sintactico: JS </h1></center>\n")
        file.write('<center><table border="1">\n')
        file.write("<thead>\n")
        file.write("<tr>\n")
        file.write('<th scope="row">Numero</th>\n')
        file.write("<th>Operacion</th>\n")
        file.write("<th>Análisis</th>\n")
        file.write("</tr>\n")
        file.write("</thead>\n")
        if (contador1 != contador2):
            file.write("<tr>")
            file.write("<td>{}</td>".format("1")) #Ingresar valor especifico en la tabla
            file.write("<td>{}</td>".format(entrada))
            file.write("<td>{}</td>".format("Incorrecto"))
            file.write("</tr>")
        else:
            file.write("<tr>")
            file.write("<td>{}</td>".format("1")) #Ingresar valor especifico en la tabla
            file.write("<td>{}</td>".format(entrada))
            file.write("<td>{}</td>".format("Correcto"))
            file.write("</tr>")
            file.write("<marquee><h2>El archivo esta limpio de errores</h2></marquee>\n")
        file.write("</table></center>\n")
        file.write("</body>\n")
        file.write("<br>\n")
        file.write("<br>\n")
        file.write("<br>\n")
        file.write("<footer>201800526</footer>")
        file.write("</html>")
        file.close()
        os.system("start ReporteSintacticoJS.html")

        
    # Dispara el Filechooser
    def abrirFile(self):
        nameFile=filedialog.askopenfilename(title = "Seleccione archivo",filetypes = (("js files","*.js"), ("html files","*.html"),("css files","*.css"),("All Files","*.*")))
        if nameFile!='':
            archi1=open(nameFile, "r", encoding="utf-8")
            contenido=archi1.read()
            archi1.close()
            self.txtEntrada.delete("1.0", END) 
            self.txtEntrada.insert("1.0", contenido)


start = GUI()
