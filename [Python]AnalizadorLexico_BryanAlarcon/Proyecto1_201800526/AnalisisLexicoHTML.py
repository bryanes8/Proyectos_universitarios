from TokenHTML import TipoToken
from TokenHTML import Token
import os

class ScannerHTML:
    lista_tokens = list()   # lista de tokens
    lista_errores = list()  # lista errores lexico
    lista_erroresLinea = list() #Lista de errores de linea
    estado = 0
    lexema = ""
    error = ""
    
    def __init__(self):
        self.lista_tokens = list()
        lista_errores = list()
        lista_erroresLinea = list()
        self.estado = 0
        self.lexema = ""
        self.fila = 1
        self.reservadas = ["html","head","tile","body","h1","h2","h3","h4","h5","h6",
                            "img","img src","a href","ul","li","p style","table border","br",
                            "caption","tr","th","td","caption","colgroup","col","thead","tbody","tfoot"]
        
    def analizar(self, cadena):
        self.cadena = cadena + "$"
        posActual = ''
        c = 0
        #Lista de estados
        estado1 = 1
        estado2 = 2
        estado3 = 3
        estado4 = 4
        estado5 = 5
        estado6 = 6
        estado7 = 7
        estado8 = 8
        estado9 = 9
        estado10 = 10
        estado11 = 11

        while c < len(self.cadena):
            posActual = self.cadena[c] #Se verifica carac por carac para ver a que estado mandarlo
           #Caracter de entrada---------------------------------------------------- 
            if self.estado == 0:
                if posActual == '$' and c == (len(self.cadena) - 1): #Se verifica si estamos al final de la cadena
                    print("\n")
                    print("¡Analisis finalizado con exito...!")
                    self.ReporteErrores()
                elif posActual == '\n': #Contario, vemos si tenemos un salto o parecido
                    self.estado = 0
                    self.lexema = ""
                    self.fila += 1 #Contador de lineas
                elif posActual == ' ': #Contario, vemos si tenemos un espacio
                    self.estado = 0
                    self.lexema = ""
                elif posActual == '\t': #Contario, vemos si tenemos un salto o parecido
                    self.estado = 0
                    self.lexema = ""
                elif posActual == '\r': #Contario, vemos si tenemos un salto o parecido
                    self.estado = 0
                    self.lexema = ""
                    self.fila += 1 #Contador de lineas
                elif posActual.isalpha():
                    self.lexema += posActual
                    self.estado = estado1  #Se envia al estado 1
                elif posActual.isdigit(): 
                    self.lexema += posActual
                    self.estado = estado2  #Se envia al estado 2
            #-----------------------------------------
                elif posActual == '{':
                    self.lexema += posActual
                    self.addToken(Token.LLAVE_IZQ)
                elif posActual == '}':
                    self.lexema += posActual
                    self.addToken(Token.LLAVE_DER)
                elif posActual == ':':
                    self.lexema += posActual
                    self.addToken(Token.D_PUNTOS)
                elif posActual == ',':
                    self.lexema += posActual
                    self.addToken(Token.COMA)
                elif posActual == ';':
                    self.lexema += posActual
                    self.addToken(Token.P_COMA)
                elif posActual == '.':
                    self.lexema += posActual
                    self.addToken(Token.PUNTO)
                elif posActual == '"':
                    self.lexema += posActual
                    self.estado = estado5   #Se envia al estado 5
                elif posActual == "'":
                    self.lexema += posActual
                    self.estado = estado5   #Se envia al estado 5
                elif posActual == '=':
                    self.lexema += posActual
                    self.addToken(Token.IGUAL)
                elif posActual == '*':
                    self.lexema += posActual
                    self.addToken(Token.ASTERISCO)
                elif posActual == '/':
                    self.lexema += posActual
                    self.estado = estado6  #Se envia al estado 6
                elif posActual == '+':
                    self.lexema += posActual
                    self.addToken(Token.MAS)
                elif posActual == '-':
                    self.lexema += posActual
                    self.addToken(Token.MENOS)
                elif posActual == '(':
                    self.lexema += posActual
                    self.addToken(Token.PAREN_IZQ)
                elif posActual == ')':
                    self.lexema += posActual
                    self.addToken(Token.PAREN_DER)
                elif posActual == '<':
                    self.lexema += posActual
                    self.estado = estado10   #Se envia al estado 10
                elif posActual == '!':
                    self.lexema += posActual
                    self.addToken(Token.DISTINTO)
                else:
                    self.addError(posActual)
                    self.addErrorLinea(self.fila)
                    print("\n")
                    print("Caracter desconocido: " + posActual + " en Fila: " + str(self.fila)+ "\n")
                    print("------------------------------------------------------------")
                        
            #Estados-----------------------------------------------------------------------------

                    #Estado 1------------- Inicial: Num - ID - Reservada 
            elif self.estado == estado1:
                if posActual.isalpha() or posActual.isdigit() or posActual == '_': #Al inicio, puede venir cualquiera de estos carac concatenados
                    self.estado = estado1
                    self.lexema += posActual
                else:
                    if self.lexema in self.reservadas: #Sino viene uno de esos, se espera una reservada
                        self.addToken(Token.RESERVADA)
                    else:
                        self.addToken(Token.ID) #De lo contrario es un ID
                    c -= 1
                    #Estado 2----------------- Num - Decimal
            elif self.estado == estado2:
                if posActual.isdigit(): #Se comprueba si es un entero, de ser asi se sigue leyendo hasta que termine
                    self.estado = estado2
                    self.lexema += posActual
                elif posActual == '.': #Contrario un decimal
                    self.estado = estado3        #Si llega a serlo, pasar al siguiente
                    self.lexema += posActual
                else:
                    self.addToken(Token.ENTERO) #Por ultimo se añade al token
                    c -= 1
                    #Estado 3
            elif self.estado == estado3:
                if posActual.isdigit():   #Se comprueba si el decimal tiene digitos, y no solo el punto a la par xd
                    self.estado = estado4            #Si es asi, pasa al siguiente estado
                    self.lexema += posActual
                else:
                    self.addError(posActual)
                    self.addErrorLinea(self.fila)
                    c -= 1
                    #Estado 4------------- Decimal
            elif self.estado == estado4:
                if posActual.isdigit():   #Se ve si tiene mas numeros concatenados
                    self.estado = estado4             #Si es asi, se queda ahí
                    self.lexema += posActual
                else:
                    self.addToken(Token.DECIMAL)  #Muestra que solo es decimal
                    c -= 1
                    #Estado 5------------- Comilla - Cualquier cosa
            elif self.estado == estado5:               #Aqui puede venir cualquier cosa, tipo comentario
                if posActual == '"' or posActual == "'":
                    self.lexema += posActual
                    self.addToken(Token.CADENA)  #Se queda aqui hasta que " sea distinto, asi termina la cadena
                else:
                    self.estado = estado5
                    self.lexema += posActual
                    #Estado 6-------------- Comentario 1 o multi
            elif self.estado == estado6:
                if posActual == '/':       #Se comprueba si el signo que viene es * o / para ver si es multi o una
                    self.lexema += posActual
                    self.estado = estado7             #Si es una lo manda al 8
                elif posActual == '*':
                    self.lexema += posActual
                    self.estado = estado8             #Si es multi lo manda al 9
                else:
                    self.addToken(Token.BARRA)
                    c -= 1
                    #Estado 7------------- Comentario una linea
            elif self.estado == estado7:
                if posActual == '\n': #Se ve si tiene un salto de linea para que termine el comentario
                    print("\n")
                    print("Comentario de una linea:  " + self.lexema)
                    self.estado = 0
                    self.fila += 1 #Contador de lineas
                else:
                    self.lexema += posActual #Continua hasta que pase a la siguiente linea
                    self.estado = estado7
                    #Estado 8 ------------- Cierre - * - Salto - Caracter 
            elif self.estado == estado8:         #Si encuentra / el cierre es multi
                if posActual == '/':
                    self.lexema += posActual
                    print("Comentario multilinea:\n\n" + self.lexema)
                    self.estado = 0
                    self.fila += 1 #Contador de lineas
                elif posActual == '\n':
                    self.lexema += posActual
                    self.estado = estado8     #Revisar al final porque no muestra ordenado el comentario---------------
                    self.fila += 1 #Contador de lineas
                elif posActual == '*':
                    self.lexema += posActual
                    self.estado = estado8     #Revisar al final porque no muestra ordenado el comentario---------------
                else:
                    self.lexema += posActual #Sino, regresa al anterior esperando que termine
                    self.estado = estado9
                    #Estado 9 ------------- Comentario multi - cualquier cosa
            elif self.estado == estado9:            #En este caso es multi, por eso se repite hasta que encuentre un *
                if posActual == '*':
                    self.lexema += posActual
                    self.estado = estado8
                elif posActual == '\n':
                    self.lexema += posActual
                    self.estado = estado8
                    self.fila += 1
                else:
                    self.lexema += posActual
                    self.estado = estado9
                    #Estado 10------------ INICIO ETIQUETA
            elif self.estado == estado10:
                if posActual == '>':
                    self.lexema += posActual
                    c += 1
                    self.addToken(Token.RESERVADA)
                    c -= 1
                else:
                    self.lexema += posActual
                    self.estado = estado10
            c += 1
            
    def addToken(self, tipoToken):
        token = TipoToken(tipoToken, self.lexema, self.fila)
        self.lista_tokens.append(token)
        self.estado = 0
        self.lexema = ""

    def addError(self, error):
        self.lista_errores.append(error)
        self.estado = 0
        self.lexema = ""

    def addErrorLinea(self, linea):
        self.lista_erroresLinea.append(linea)
        self.estado = 0
        self.lexema = ""

    def ReporteErrores(self):
        file = open("ReporteCSS.html", "w")
        file.write("<!DOCTYPE html>\n")
        file.write("<html>\n")
        file.write('<body bgcolor="#EED4A0">')
        file.write("<head>\n")
        file.write("<title>Reporte de Errores Lexicos</title>\n")
        file.write("</head>\n")
        file.write("<center><h1>Reporte de Errores Lexicos: HTML </h1></center>\n")
        file.write('<center><table border="1">\n')
        file.write("<thead>\n")
        file.write("<tr>\n")
        file.write('<th scope="row">Numero</th>\n')
        file.write("<th>Caracter Desconocido</th>\n")
        file.write("<th>Fila No.</th>\n")
        file.write("</tr>\n")
        file.write("</thead>\n")
        if len(self.lista_errores) == 0:
            file.write("<tr>")
            file.write("<td>-</td>")
            file.write("<td>-</td>")
            file.write("<td>-</td>")
            file.write("</tr>")
            file.write("<marquee><h2>El archivo esta limpio de errores</h2></marquee>\n")
        else:
            x = 1
            for error in range(len(self.lista_errores)):
                file.write("<tr>")
                file.write("<td>{}</td>".format(x)) #Ingresar valor especifico en la tabla
                file.write("<td>{}</td>".format(self.lista_errores[error]))
                file.write("<td>{}</td>".format(self.lista_erroresLinea[error]))
                file.write("</tr>")
                x += 1
        file.write("</table></center>\n")
        file.write("</body>\n")
        file.write("<br>\n")
        file.write("<br>\n")
        file.write("<br>\n")
        file.write("<footer>201800526</footer>")
        file.write("</html>")
        file.close()

        os.system("start ReporteCSS.html")
