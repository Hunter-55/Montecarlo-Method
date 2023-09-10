from matplotlib import pyplot as plt
import random

class Monte_Carlos:

    # SE CREAN VARIABLES GLOBALES PARA EL USO DE LAS CONFIGURACIONES DEL DISEÑO DE LA GRAFICA
    global background,circle,colorPointInsider,colorPointOut,colorText
    global title,nameEjeX,nameEjeY,fontSizeText,radioPonit,coordinates

    # CONFIGURACIÓN DE COLORES
    # background:        COLOR DE FONDO DE LA GRAFICA
    # circle:            COLOR DEL CONTORNO DEL CUARTO DE CIRCULO
    # colorPointInsider: COLOR DE LOS PUNTOS QUE CAEN DENTRO DEL CIRCULO
    # colorPointOut:     COLOR DE LOS PUNTOS DE CAEN FUERA DEL CIRCULO
    # colorText:         COLOR DEL TEXTO QUE MUESTRA LA INFORMACIÓN
    background        = "dark_background"
    circle            = "orange"
    colorPointInsider = "darkgreen"
    colorPointOut     = "darkred"
    colorText         = 'white'

    # CONFIGURACION DE DATOS DE LA GRAFICA
    # title:        NOMBRE DE LA GRAFICA
    # nameEjeX:     NOMBRE DEL EJE 'X'
    # nameEjeY:     NOMBRE DEL EJE 'Y'
    # fontSizeText: TAMAÑO DEL TEXTO QUE MUESTRA LA INFORMACIÓN
    # radioPonit:   TAMAÑO DE LOS PUNTOS QUE CAEN DENTRO Y FUERA DEL CIRCULO
    # coordinates:  POSICION DEL CUARTO DE CIRCULO
    title        = "METODO MONTECARLO"
    nameEjeX     = "EJE ( X )"
    nameEjeY     = "EJE ( Y )"
    fontSizeText = 15
    radioPonit   = 0.003
    coordinates  = (0, 0)


    #----- CONSTRUCTOR -----
    def __init__(self) -> None:
        self.radio        = 1             # TAMAÑO DEL CUARTO DEL CIRCULO
        self.points       = 0             # TOTAL DE PUNTOS 
        self.pointsInside = 0             # CANTIDAD DE PUNTOS DENTRO DEL CIRCULO
        self.pointsOut    = 0             # CANTIDAD DE PUNTOS FUERA DEL CIRCULO
        self.radioSquared = self.radio**2 # CALCULO DEL RADIO CUADRADO
        self.isRunning    = True          # NOS PERMITE LA DETENCIÓN DEL CICLO WHILE A COMPLETAR EL VALOR DE PI
        self.pi           = 0             # ALMACENA EL VALOR DE PI
        self.fig          = ""            # CREA INSTANCIA DEL METODO plt.subplots()
        self.ax           = ""            # CREA INSTANCIA DEL METODO plt.subplots()
        self.cicleArea    = 0.0           # ÁREA DEL CIRCULO


    #----- METODO PARA INICIALIZAR EL DISEÑO DE LA GRAFICA -----
    def Graph(self):
        plt.style.use(background)                                               # AGREGAMOS UN COLOR DE FONDO
        self.fig, self.ax = plt.subplots()                                      # GENERAMOS EL GRAFICO
        self.ax.set_title(title)                                                # AGREGAMOS UN TITULO A LA GRAFICA
        self.ax.set_xlabel(nameEjeX)                                            # AGREGAMOS LOS EJES 'X'
        self.ax.set_ylabel(nameEjeY)                                            # AGREGAMOS LOS EJES 'Y'
        circle1 = plt.Circle(coordinates, self.radio, color=circle, fill=False) # CREAMOS EL CUARTO DE CIRCULO
        self.ax.add_patch(circle1)                                              # AGREGAMOS EL CIRCULO GRAFICO


    #----- METODO PARA CARCULAR PI -----
    def PiCalculate(self):
        while self.isRunning:
            # GENERAMOS NUMEROS ALEATORIOS 
            x = random.uniform(0.0, 1.0)
            y = random.uniform(0.0, 1.0)

            self.points   += 1
            xSquared      = x**2
            ySquared      = y**2
            position      = xSquared + ySquared
            
            # LA SUMA DE LOS CUADRADOS DE LA POSICIÓN 'X' Y 'Y' DEBE SER MENOR AL CUADRADO DEL RADIO
            # SI SE CUMPLE LA CONDICIÓN LOS PUNTOS ENTRAN EN EL CIRCULO DE COLOR VERDE
            if position < self.radioSquared:
                pointInsider = plt.Circle((x,y),radioPonit, color=colorPointInsider)
                self.ax.add_patch(pointInsider)
                self.pointsInside += 1
            # SI NO SE CUMPLE LA CONDICIÓN LOS PUNTOS SE COLOCAN FUERA DEL CIRCULO DE COLOR ROJO
            else:
                pointOut = plt.Circle((x,y),radioPonit, color=colorPointOut)
                self.ax.add_patch(pointOut)
                self.pointsOut += 1

            # SE REALIZA EL CALCULO DE PI HASTA OBTENER EL NÚMERO MAS CERCANO
            self.pi = 4 * self.pointsInside / self.points

            # SEGUIRA GENERANDO PUNTOS HASTA QUE EL VALOR DE PI SEA 3.1416
            if str(self.pi).find('3.1416') != -1:
                self.isRunning = False


    #----- METODO PARA CALCULAR ÁREA DE UN CIRCULO -----
    def CicleCalculateArea(self):
        self.cicleArea = self.pi * self.radioSquared


    #----- METODO PARA AGREGAR TEXTO A LA GRAFICA -----
    def TextAdd(self):
        # AGREGAMOS TEXTO
        # REDONDEAMOS LOS VALORES DEL PORCENTAJE DE PUNTOS DENTRO Y FUERA DEL CIRCULO
        percentageInternalPoints = round(self.pointsInside / self.points,2)
        percentageExternalPoints = round(1 - percentageInternalPoints,2)

        # CREAMOS LOS TEXTO QUE SE IMPRIMIRA EN LA GRAFICA CON LA INFORMACIÓN PARA EL USUARIO 
        self.ax.text(0.05,0.9,f"PUNTOS: {self.points}",fontsize=fontSizeText,color=colorText)
        self.ax.text(0.05,0.84,f"PUNTOS INTERNOS: {self.pointsInside} , {percentageInternalPoints}%",fontsize=fontSizeText,color=colorText)
        self.ax.text(0.05,0.78,f"PUNTOS EXTERNOS: {self.pointsOut} , {percentageExternalPoints}%",fontsize=fontSizeText,color=colorText)
        self.ax.text(0.05,0.72,f"π: {self.pi}",fontsize=fontSizeText,color=colorText)
        self.ax.text(0.05,0.66,f"ÁREA DEL CIRCULO: {self.cicleArea}",fontsize=fontSizeText,color=colorText)


    #----- METODO PARA IMPRIMIR UNA IMAGEN DE LA GRAFICA EN PNG -----
    def PrintPicture(self):
        self.fig.savefig('montecarlo.png')
        plt.show()


#----- FUNCIÓN MAIN PARA INSTANCIAR EL LLAMADO A LA CLASE -----
def main():
    metodoMonteCarlos = Monte_Carlos() 

    metodoMonteCarlos.Graph()
    metodoMonteCarlos.PiCalculate()
    metodoMonteCarlos.CicleCalculateArea()
    metodoMonteCarlos.TextAdd()
    metodoMonteCarlos.PrintPicture()


if __name__ == "__main__":
    main()


"""
El número π (pi) es la relación entre la longitud de una circunferencia y su diámetro en geometría euclidiana.
Es un número irracional
"""