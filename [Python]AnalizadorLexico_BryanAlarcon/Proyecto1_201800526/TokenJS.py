from enum import Enum

class Token(Enum):
    #Expresiones regulares
    ID = 1
    CADENA = 2
    VALOR = 3
    #Simbolos del lenguaje
    LLAVE_IZQ = 4
    LLAVE_DER = 5
    D_PUNTOS = 6
    COMA = 7
    P_COMA = 8
    PUNTO = 9
    COMILLAS = 10
    IGUAL = 11
    ASTERISCO = 12
    BARRA = 13
    MAS = 14
    MENOS = 15
    PAREN_IZQ = 16
    PAREN_DER = 17
    MENOR = 18
    MAYOR = 19
    CONJUNCION = 20
    DISYUNCION = 21
    ENTERO = 22
    DECIMAL = 23
    RESERVADA = 24
    DISTINTO = 25
    MENORIGUAL = 26
    MAYORIGUAL = 27

class TipoToken:

    def __init__(self, tipoToken, lexema, linea):
        self.tipoToken = tipoToken
        self.lexema = lexema
        self.linea = linea
    #Obtener el tipo del token
    def getTipo(self):
        
        if self.tipoToken is Token.ID:
            return "ID"
        elif self.tipoToken is Token.CADENA:
            return "CADENA"
        elif self.tipoToken is Token.VALOR:
            return "VALOR"
        #-------------------------------------
        elif self.tipoToken is Token.LLAVE_IZQ:
            return "LLAVE_IZQ"
        elif self.tipoToken is Token.LLAVE_DER:
            return "LLAVE_DER"
        elif self.tipoToken is Token.D_PUNTOS:
            return "D_PUNTOS"
        elif self.tipoToken is Token.COMA:
            return "COMA"
        elif self.tipoToken is Token.P_COMA:
            return "P_COMA"
        elif self.tipoToken is Token.PUNTO:
            return "PUNTO"
        elif self.tipoToken is Token.COMILLAS:
            return "COMILLAS"
        elif self.tipoToken is Token.IGUAL:
            return "IGUAL"
        elif self.tipoToken is Token.ASTERISCO:
            return "ASTERISCO"
        elif self.tipoToken is Token.BARRA:
            return "BARRA"
        elif self.tipoToken is Token.MAS:
            return "MAS"
        elif self.tipoToken is Token.MENOS:
            return "MENOS"
        elif self.tipoToken is Token.PAREN_IZQ:
            return "PAREN_IZQ"
        elif self.tipoToken is Token.PAREN_DER:
            return "PAREN_DER"
        elif self.tipoToken is Token.MENOR:
            return "MENOR"
        elif self.tipoToken is Token.MAYOR:
            return "MAYOR"
        elif self.tipoToken is Token.CONJUNCION:
            return "CONJUNCION"
        elif self.tipoToken is Token.DISYUNCION:
            return "DISYUNCION"
        elif self.tipoToken is Token.ENTERO:
            return "ENTERO"
        elif self.tipoToken is Token.DECIMAL:
            return "DECIMAL"
        elif self.tipoToken is Token.RESERVADA:
            return "RESERVADA"
        elif self.tipoToken is Token.DISTINTO:
            return "DISTINTO"
        elif self.tipoToken is Token.MENORIGUAL:
            return "MENORIGUAL"
        elif self.tipoToken is Token.MAYORIGUAL:
            return "MAYORIGUAL"
        else:
            return "UNKNOWN"

