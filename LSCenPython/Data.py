#Importar Librerias
import cv2
import os

# Importarr la clase
import SeguimientoManos as sm

# Creacion de la carpeta
# nombre = 'Letra_A'
# nombre = 'Letra_B'
nombre = 'Letra_C'
# nombre = 'Letra_D'
# nombre = 'Letra_E'
# nombre = 'Letra_F'
# nombre = 'Letra_G'
# nombre = 'Letra_H'
# nombre = 'Letra_I'
# nombre = 'Letra_J'
# nombre = 'Letra_K'
# nombre = 'Letra_L'
# nombre = 'Letra_M'
# nombre = 'Letra_N'
# nombre = 'Letra_Ñ'
# nombre = 'Letra_O'
# nombre = 'Letra_P'
# nombre = 'Letra_Q'
# nombre = 'Letra_R'
# nombre = 'Letra_S'
# nombre = 'Letra_T'
# nombre = 'Letra_U'
# nombre = 'Letra_V'
# nombre = 'Letra_W'
# nombre = 'Letra_X'
# nombre = 'Letra_Y'
# nombre = 'Letra_Z'

direccion = 'C:/Users/LENOVO/Documents/LSCenPython/data'
carpeta = direccion + '/' + nombre

# Si no esta creada la carpeta
if not os.path.exists(carpeta):
    print("CARPETA CREADA: ", carpeta)
    # Creamos la carpeta
    os.makedirs(carpeta)
    
# Lectura de la camara
cap = cv2.VideoCapture(1)

# Cambiar la resolucion
cap.set(3, 1280)
cap.set(4, 720)

# Declaramos contador
cont = 0

# Declarar detector
detector = sm.detectormanos(Confdeteccion = 0.9)

while True:
    # Realizar la lectura de la captura
    ret, frame = cap.read()
    
    # Extraer informacion de la mano
    frame = detector.encontrarmanos(frame, dibujar = False)
    
    # Posicion de una sola mano
    lista1, bbox, mano = detector.encontrarposicion(frame, ManoNum = 0, dibujarPuntos = False, DibujarBox = False, color = [0, 255, 0])
    
    # Si hay mano
    if mano == 1:
        
        # Extrear la informacion del cuadro
        xmin, ymin, xmax, ymax = bbox
        
        # Asignamos margen
        xmin = xmin - 40
        ymin = ymin - 40
        xmax = xmax + 40
        ymax = ymax + 40
        
        # Realizar recorte de nuestra mano
        recorte = frame[ymin:ymax, xmin:xmax]
        
        # Almacenar nuestras imagenes
        # cv2.imwrite(carpeta + "/A_{}.jpg".format(cont), recorte)
        # cv2.imwrite(carpeta + "/B_{}.jpg".format(cont), recorte)
        cv2.imwrite(carpeta + "/C_{}.jpg".format(cont), recorte)
        # cv2.imwrite(carpeta + "/D_{}.jpg".format(cont), recorte)
        # cv2.imwrite(carpeta + "/E_{}.jpg".format(cont), recorte)
        # cv2.imwrite(carpeta + "/F_{}.jpg".format(cont), recorte)
        # cv2.imwrite(carpeta + "/G_{}.jpg".format(cont), recorte)
        # cv2.imwrite(carpeta + "/H_{}.jpg".format(cont), recorte)
        # cv2.imwrite(carpeta + "/I_{}.jpg".format(cont), recorte)
        # cv2.imwrite(carpeta + "/J_{}.jpg".format(cont), recorte)
        # cv2.imwrite(carpeta + "/K_{}.jpg".format(cont), recorte)
        # cv2.imwrite(carpeta + "/L_{}.jpg".format(cont), recorte)
        # cv2.imwrite(carpeta + "/M_{}.jpg".format(cont), recorte)
        # cv2.imwrite(carpeta + "/N_{}.jpg".format(cont), recorte)
        # cv2.imwrite(carpeta + "/Ñ_{}.jpg".format(cont), recorte)
        # cv2.imwrite(carpeta + "/O_{}.jpg".format(cont), recorte)
        # cv2.imwrite(carpeta + "/P_{}.jpg".format(cont), recorte)
        # cv2.imwrite(carpeta + "/Q_{}.jpg".format(cont), recorte)
        # cv2.imwrite(carpeta + "/R_{}.jpg".format(cont), recorte)
        # cv2.imwrite(carpeta + "/S_{}.jpg".format(cont), recorte)
        # cv2.imwrite(carpeta + "/T_{}.jpg".format(cont), recorte)
        # cv2.imwrite(carpeta + "/U_{}.jpg".format(cont), recorte)
        # cv2.imwrite(carpeta + "/V_{}.jpg".format(cont), recorte)
        # cv2.imwrite(carpeta + "/W_{}.jpg".format(cont), recorte)
        # cv2.imwrite(carpeta + "/X_{}.jpg".format(cont), recorte)
        # cv2.imwrite(carpeta + "/Y_{}.jpg".format(cont), recorte)
        # cv2.imwrite(carpeta + "/Z_{}.jpg".format(cont), recorte)
        
        # Aumentamos contador
        cont = cont + 1
        
        cv2.imshow("RECORTE", recorte)
            
    # Mosttrar FPS
    cv2.imshow("Lengua de senas colombiana", frame)
    
    # Leer nuestro teclado
    t = cv2.waitKey(1)
    if t == 27 or cont == 11:
        break
    
cap.release()
cv2.destroyAllWindows() 