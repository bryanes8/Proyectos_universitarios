from TokenJS import TipoToken
from TokenJS import Token
#from graphviz import Digraph
import os
class ParserJS:
    lista_tokens = list()   # lista de tokens del analisis lexico
    cont = 0
    bandera = True
    
    def __init__(self, listT):
        self.lista_tokens = listT
        self.cont = 0
        self.bandera = True
        
    def getToken(self):
        token = self.lista_tokens[self.cont]
        return token

    #Comienzo ->'(' reglas ')'
    def begin(self):
        cadError = ""
        token = self.getToken()
        self.cont+=1
        #Parentesis como primera linea
        if(token.tipoToken == Token.PAREN_IZQ):
            self.regla() #Llamando a la produccion
            token = self.getToken()
            #self.cont+=1
            if(token.tipoToken == Token.PAREN_DER):
                if(self.bandera == False and len(self.lista_tokens) < self.cont):
                    print("Existen errores sintacticos. \n" +cadError)
                else: 
                    ("Cadena valida sintacticamente.")
            elif(self.bandera==True):
                self.regla()
            else:
                cadError ="Error Sintactico, se esperaba un ')'"
                self.bandera = False
        else:
            cadError ="Error Sintactico, se esperaba un '('"
            self.bandera = False
        if(self.bandera == False):
            print("Existen errores sintacticos \n" +cadError)
        else: 
            print("La cadena ingresada es valida")


    # regla -> ID 'OPERADOR' ID
    # regla -> ID | DECIMAL | ENTERO
    def regla(self):

        self.bandera = self.operador() #Llamando a la produccion
        if(self.bandera == False):
            return False
        token = self.getToken()
        self.cont+=1
        if(token.tipoToken == Token.ID or token.tipoToken == Token.DECIMAL or token.tipoToken == Token.ENTERO):
            self.bandera = True
            token = self.getToken()
            #Validacion:(5+2)
            if(token.tipoToken == Token.MAS or token.tipoToken == Token.MENOS or token.tipoToken == Token.ASTERISCO or token.tipoToken == Token.BARRA):
                self.bandera = True
                self.cont+=1
                token = self.getToken()
                if(token.tipoToken == Token.ID or token.tipoToken == Token.DECIMAL or token.tipoToken == Token.ENTERO):
                    self.bandera = True
                    self.cont+=1
                    return True
                else:
                    self.regla() #Llamando a la produccion
            #Validacion: (5(+|2
            elif(token.tipoToken == Token.PAREN_IZQ):
                self.bandera = True
                self.cont+=1
                token = self.getToken()
                if(token.tipoToken == Token.ID or token.tipoToken == Token.DECIMAL or token.tipoToken == Token.ENTERO or token.tipoToken == Token.MAS or token.tipoToken == Token.MENOS or token.tipoToken == Token.ASTERISCO or token.tipoToken == Token.BARRA):
                    self.bandera = True
                    self.cont+=1
                    token = self.getToken()
                    if(token.tipoToken == Token.ID or token.tipoToken == Token.DECIMAL or token.tipoToken == Token.ENTERO):
                        self.bandera = True
                        self.cont+=1
                        token = self.getToken()
                        if(token.tipoToken == Token.PAREN_DER):
                            self.bandera = True
                            self.cont+=1
                            return True
                        else:
                            self.regla() #Llamando a la produccion
                    else:
                        self.regla() #Llamando a la produccion
                else:
                    self.regla()
            #Validacion: ((5+2))
        elif(token.tipoToken == Token.PAREN_IZQ or token.tipoToken == Token.MAS or token.tipoToken == Token.MENOS or token.tipoToken == Token.ASTERISCO or token.tipoToken == Token.BARRA):
            self.bandera = True
            token = self.getToken()
            if(token.tipoToken == Token.ID or token.tipoToken == Token.DECIMAL or token.tipoToken == Token.ENTERO):
                self.bandera = True
                self.cont+=1
                token = self.getToken()
                if(token.tipoToken == Token.MAS or token.tipoToken == Token.MENOS or token.tipoToken == Token.ASTERISCO or token.tipoToken == Token.BARRA):
                    self.bandera = True
                    self.cont+=1
                    token = self.getToken()
                    if(token.tipoToken == Token.ID or token.tipoToken == Token.DECIMAL or token.tipoToken == Token.ENTERO):
                        self.bandera = True
                        self.cont+=1
                        token = self.getToken()
                        if(token.tipoToken == Token.PAREN_DER):
                            self.bandera = True
                            self.cont+=1
                            return True
                        else:
                            self.regla() #Llamando a la produccion
                    else:
                        self.regla() #Llamando a la produccion
                else:
                    self.regla() #Llamando a la produccion
            else:
                self.regla() #Llamando a la produccion
        else:
            self.cadError ="Error Sintactico, se esperaba un OPERADOR"
            self.bandera = False
            
    #OPERADOR  -> +
    #           | -
    #           | *
    #           | /

    def operador(self):
        token = self.getToken()
        if(token.tipoToken == Token.MAS or token.tipoToken == Token.MENOS or token.tipoToken == Token.ASTERISCO or token.tipoToken == Token.BARRA):
            self.bandera = True
            self.cont+=1
        else:
            self.cadError ="Error Sintactico, se esperaba una operador (+|-|*|/)"
            self.bandera = False
            
    #OPERANDO  -> +
    #           | -
    #           | *
    #           | /
    def operando(self):
        token = self.getToken()
        if(token.tipoToken == Token.ID or token.tipoToken == Token.DECIMAL or token.tipoToken == Token.ENTERO):
            self.bandera = True
            self.cont+=1
        else:
            self.cadError ="Error Sintactico, se esperaba una operador (ID|DECIMAL|ENTERO)"
            self.bandera = False



